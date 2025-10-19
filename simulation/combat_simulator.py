#!/usr/bin/env python3
"""
Penance Combat & Campaign Simulator
Simulates combat scenarios and campaigns to identify balance issues
"""

import random
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

# ============================================================================
# GAME CONSTANTS
# ============================================================================

class CasketClass(Enum):
    SCOUT = ("Scout", 6, 26)      # (name, SP, min_deck_size)
    ASSAULT = ("Assault", 5, 30)
    HEAVY = ("Heavy", 4, 40)
    FORTRESS = ("Fortress", 3, 50)

class FactionMechanic(Enum):
    CHURCH_SELFHARM = "blood_offering"
    DWARVES_RUNES = "rune_counters"
    OSSUARIUM_LIFESTEAL = "soul_harvest"
    ELVES_BLEED = "bleed_stacking"

# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class Card:
    name: str
    type: str
    sp_cost: int
    damage: int = 0
    defense: int = 0
    range: str = "Melee"
    heat: int = 0
    effect: str = ""

@dataclass
class Casket:
    """Represents a player's Casket (mech)"""
    name: str
    faction: str
    casket_class: CasketClass
    deck: List[Card] = field(default_factory=list)
    hand: List[Card] = field(default_factory=list)
    discard: List[Card] = field(default_factory=list)

    sp: int = 0
    sp_max: int = 0
    heat: int = 0
    component_damage: Dict[str, int] = field(default_factory=lambda: {
        "head": 0, "chassis": 0, "right_arm": 0, "left_arm": 0, "legs": 0
    })

    # Faction mechanics
    blood_offering_bonus: int = 0
    rune_counters: int = 0
    bleed_counters: int = 0
    lifesteal_healed: int = 0

    # Pilot wounds
    pilot_wounds: int = 0
    pilot_max_wounds: int = 10

    # Stats
    position: tuple = (0, 0)

    def __post_init__(self):
        _, sp, deck_size = self.casket_class.value
        self.sp_max = sp
        self.sp = sp

    @property
    def hp(self):
        """Current HP = cards remaining in deck + hand"""
        return len(self.deck) + len(self.hand)

    @property
    def is_alive(self):
        """Casket is alive if deck has cards or pilot isn't dead"""
        return (len(self.deck) > 0 or len(self.hand) > 0) and self.pilot_wounds < self.pilot_max_wounds

    def take_damage(self, amount: int) -> Dict[str, any]:
        """Apply damage to Casket"""
        result = {
            "damage_dealt": amount,
            "cards_discarded": 0,
            "component_damage": False,
            "pilot_wound": False
        }

        for _ in range(amount):
            if len(self.hand) > 0:
                discarded = self.hand.pop(0)
                self.discard.append(discarded)
                result["cards_discarded"] += 1

                # Check for component damage (if Primary Weapon card)
                if "weapon" in discarded.type.lower():
                    result["component_damage"] = True
            elif len(self.deck) > 0:
                discarded = self.deck.pop(0)
                self.discard.append(discarded)
                result["cards_discarded"] += 1
            else:
                # Deck empty, reshuffle with damage card
                self.reshuffle_with_damage()

        return result

    def reshuffle_with_damage(self):
        """Reshuffle discard pile into deck, add 1 Damage card (death spiral)"""
        self.deck = self.discard.copy()
        self.discard = []
        random.shuffle(self.deck)
        # Add damage card (dead draw)
        self.deck.insert(0, Card(name="DAMAGE", type="dead_draw", sp_cost=99, effect="Dead card (cannot be played)"))

    def draw_cards(self, count: int):
        """Draw cards from deck"""
        for _ in range(count):
            if len(self.deck) > 0:
                self.hand.append(self.deck.pop(0))
            else:
                # Deck empty, reshuffle
                if len(self.discard) > 0:
                    self.reshuffle_with_damage()
                    if len(self.deck) > 0:
                        self.hand.append(self.deck.pop(0))

    def refresh_sp(self):
        """Refresh SP at start of turn"""
        self.sp = self.sp_max

        # Chassis damage penalty
        if self.component_damage["chassis"] >= 3:
            self.sp = max(1, self.sp - 1)

# ============================================================================
# COMBAT SIMULATOR
# ============================================================================

class CombatSimulator:
    def __init__(self, casket1: Casket, casket2: Casket):
        self.casket1 = casket1
        self.casket2 = casket2
        self.turn = 0
        self.log = []

    def log_event(self, message: str):
        """Log combat event"""
        self.log.append(f"[Turn {self.turn}] {message}")

    def simulate_turn(self, attacker: Casket, defender: Casket):
        """Simulate one turn of combat"""
        self.turn += 1

        # Phase 1: Refresh
        attacker.refresh_sp()
        attacker.draw_cards(3)

        # Check Heat (strain roll if 5+)
        if attacker.heat >= 5:
            strain_roll = random.randint(1, 6)
            if strain_roll <= 3:
                attacker.sp -= 1
                self.log_event(f"{attacker.name} failed Strain roll! -1 SP")

        # Phase 2: Action Phase - Simulate tactical decisions
        damage_dealt = self.simulate_attack_phase(attacker, defender)

        # Phase 3: Draw phase (already did this in refresh for simplicity)

        # Phase 4: End phase
        # Bleed damage for Elves
        if defender.bleed_counters > 0:
            bleed_dmg = defender.bleed_counters
            defender.take_damage(bleed_dmg)
            self.log_event(f"{defender.name} takes {bleed_dmg} Bleed damage")
            defender.bleed_counters = max(0, defender.bleed_counters - 1)

        # Reduce heat slightly
        attacker.heat = max(0, attacker.heat - 1)

    def simulate_attack_phase(self, attacker: Casket, defender: Casket) -> int:
        """Simulate attack decisions based on faction"""
        total_damage = 0

        # Church: Self-harm for damage boost
        if attacker.faction == "church":
            # Blood Offering: discard 1 card, gain +3 damage (BALANCED from 2 HP)
            if len(attacker.hand) >= 3:
                attacker.take_damage(1)
                attacker.blood_offering_bonus = 3
                self.log_event(f"{attacker.name} uses Blood Offering (-1 HP, +3 damage)")

            # Attack
            base_damage = 4 + attacker.blood_offering_bonus
            defender.take_damage(base_damage)
            total_damage = base_damage
            attacker.blood_offering_bonus = 0
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Dwarves: Rune stacking
        elif attacker.faction == "dwarves":
            # Build runes
            attacker.rune_counters += 2
            attacker.heat += 1
            self.log_event(f"{attacker.name} gains 2 Rune counters (total: {attacker.rune_counters})")

            # Attack with rune bonus
            base_damage = 3 + min(attacker.rune_counters // 2, 5)  # Cap at +5
            defender.take_damage(base_damage)
            total_damage = base_damage
            self.log_event(f"{attacker.name} attacks for {base_damage} damage (Rune bonus: +{min(attacker.rune_counters // 2, 5)})")

        # Ossuarium: Lifesteal
        elif attacker.faction == "ossuarium":
            base_damage = 4
            defender.take_damage(base_damage)
            total_damage = base_damage

            # Lifesteal: recover 2 cards
            attacker.draw_cards(2)
            attacker.lifesteal_healed += 2
            self.log_event(f"{attacker.name} attacks for {base_damage} damage, lifesteals 2 HP")

        # Elves: Bleed stacking
        elif attacker.faction == "elves":
            base_damage = 3
            defender.take_damage(base_damage)
            total_damage = base_damage

            # Apply Bleed (capped at 10)
            defender.bleed_counters = min(defender.bleed_counters + 2, 10)
            self.log_event(f"{attacker.name} attacks for {base_damage} damage, applies 2 Bleed (total: {defender.bleed_counters})")

        # Generic attack
        else:
            base_damage = 4
            defender.take_damage(base_damage)
            total_damage = base_damage
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        return total_damage

    def run_combat(self, max_turns: int = 20) -> Dict[str, any]:
        """Run full combat simulation"""
        self.log_event(f"COMBAT START: {self.casket1.name} vs {self.casket2.name}")
        self.log_event(f"{self.casket1.name}: {self.casket1.hp} HP ({self.casket1.faction})")
        self.log_event(f"{self.casket2.name}: {self.casket2.hp} HP ({self.casket2.faction})")

        # Alternate turns
        while self.casket1.is_alive and self.casket2.is_alive and self.turn < max_turns:
            # Roll initiative (simplified)
            if random.randint(1, 6) >= 4:
                self.simulate_turn(self.casket1, self.casket2)
                if self.casket2.is_alive:
                    self.simulate_turn(self.casket2, self.casket1)
            else:
                self.simulate_turn(self.casket2, self.casket1)
                if self.casket1.is_alive:
                    self.simulate_turn(self.casket1, self.casket2)

        # Determine winner
        winner = None
        if self.casket1.is_alive and not self.casket2.is_alive:
            winner = self.casket1
        elif self.casket2.is_alive and not self.casket1.is_alive:
            winner = self.casket2

        self.log_event(f"\n=== COMBAT END ===")
        if winner:
            self.log_event(f"WINNER: {winner.name} ({winner.hp} HP remaining)")
        else:
            self.log_event(f"DRAW (turn limit reached)")

        self.log_event(f"{self.casket1.name} final HP: {self.casket1.hp}")
        self.log_event(f"{self.casket2.name} final HP: {self.casket2.hp}")

        return {
            "winner": winner.name if winner else "Draw",
            "turns": self.turn,
            "casket1_hp": self.casket1.hp,
            "casket2_hp": self.casket2.hp,
            "log": self.log
        }

# ============================================================================
# CAMPAIGN SIMULATOR
# ============================================================================

class CampaignSimulator:
    def __init__(self, starting_casket: Casket):
        self.casket = starting_casket
        self.mission = 0
        self.scrap = 5
        self.log = []

    def log_event(self, message: str):
        """Log campaign event"""
        self.log.append(f"[Mission {self.mission}] {message}")

    def run_mission(self, enemy_faction: str):
        """Simulate a single mission"""
        self.mission += 1
        self.log_event(f"\n=== MISSION {self.mission}: vs {enemy_faction} ===")

        # Create enemy
        enemy = self.create_enemy(enemy_faction)

        # Run combat
        combat = CombatSimulator(self.casket, enemy)
        result = combat.run_combat(max_turns=15)

        self.log.extend(result["log"])

        # Post-mission
        if result["winner"] == self.casket.name:
            # Victory rewards
            scrap_gained = random.randint(2, 4)
            self.scrap += scrap_gained
            self.log_event(f"VICTORY! Gained {scrap_gained} Scrap (total: {self.scrap})")

            # Check for pilot wounds (if low HP)
            if self.casket.hp < 10:
                wound_roll = random.randint(1, 10)
                if wound_roll <= 3:
                    self.casket.pilot_wounds += 1
                    self.log_event(f"Pilot suffered wound! (wounds: {self.casket.pilot_wounds}/10)")
        else:
            self.log_event(f"DEFEAT! Mission failed.")
            return False

        # Settlement phase (repair options)
        # Option 1: Standard repair (variable cost)
        repair_cost = (self.casket.hp // 10) + 1

        # Option 2: Field Repair Kit (NEW - 3 Scrap flat cost for 5 HP)
        # AI chooses better option
        if self.scrap >= 3 and self.casket.hp < 20:
            # Use Field Repair Kit if low HP
            self.scrap -= 3
            self.casket.draw_cards(5)
            self.log_event(f"Used Field Repair Kit: +5 HP (cost: 3 Scrap)")
        elif self.scrap >= repair_cost:
            # Use standard repair
            self.scrap -= repair_cost
            self.casket.draw_cards(5)
            self.log_event(f"Repaired +5 HP (cost: {repair_cost} Scrap)")

        return True

    def create_enemy(self, faction: str) -> Casket:
        """Create enemy Casket"""
        enemy = Casket(
            name=f"{faction.capitalize()} Enemy",
            faction=faction,
            casket_class=CasketClass.ASSAULT
        )

        # Build enemy deck (simplified)
        for _ in range(30):
            enemy.deck.append(Card(name="Generic Card", type="attack", sp_cost=2, damage=3))

        random.shuffle(enemy.deck)
        enemy.draw_cards(6)

        return enemy

    def run_campaign(self, num_missions: int = 3) -> Dict[str, any]:
        """Run full campaign"""
        self.log_event(f"=== CAMPAIGN START: {self.casket.name} ===")
        self.log_event(f"Starting HP: {self.casket.hp}")
        self.log_event(f"Starting Scrap: {self.scrap}")

        factions = ["church", "dwarves", "ossuarium", "elves"]

        for i in range(num_missions):
            enemy_faction = random.choice(factions)
            success = self.run_mission(enemy_faction)

            if not success or not self.casket.is_alive:
                self.log_event("\n=== CAMPAIGN FAILED ===")
                return {
                    "success": False,
                    "missions_completed": i,
                    "final_hp": self.casket.hp,
                    "final_scrap": self.scrap,
                    "log": self.log
                }

        self.log_event("\n=== CAMPAIGN COMPLETE ===")
        self.log_event(f"Final HP: {self.casket.hp}")
        self.log_event(f"Final Scrap: {self.scrap}")
        self.log_event(f"Pilot Wounds: {self.casket.pilot_wounds}/10")

        return {
            "success": True,
            "missions_completed": num_missions,
            "final_hp": self.casket.hp,
            "final_scrap": self.scrap,
            "log": self.log
        }

# ============================================================================
# MAIN SIMULATION
# ============================================================================

def create_test_casket(name: str, faction: str, casket_class: CasketClass) -> Casket:
    """Create a test Casket with a basic deck"""
    casket = Casket(name=name, faction=faction, casket_class=casket_class)

    # Build deck (simplified)
    deck_size = casket_class.value[2]
    for _ in range(deck_size):
        casket.deck.append(Card(
            name="Generic Card",
            type="attack" if random.random() > 0.3 else "defense",
            sp_cost=random.randint(1, 3),
            damage=random.randint(2, 5)
        ))

    random.shuffle(casket.deck)
    casket.draw_cards(6)

    return casket

def run_balance_tests():
    """Run comprehensive balance tests"""
    print("=" * 60)
    print("PENANCE: Combat & Campaign Simulation")
    print("=" * 60)

    results = {
        "combat_scenarios": [],
        "campaign_runs": []
    }

    # ========================================================================
    # SCENARIO 1: Church vs Dwarves (Self-harm vs Rune stacking)
    # ========================================================================
    print("\n[SCENARIO 1] Church vs Dwarves")
    print("-" * 60)

    church = create_test_casket("Holy Avenger", "church", CasketClass.ASSAULT)
    dwarves = create_test_casket("Runeforge Titan", "dwarves", CasketClass.HEAVY)

    combat1 = CombatSimulator(church, dwarves)
    result1 = combat1.run_combat(max_turns=15)
    results["combat_scenarios"].append(result1)

    print(f"Winner: {result1['winner']}")
    print(f"Turns: {result1['turns']}")
    print(f"Church HP: {result1['casket1_hp']}")
    print(f"Dwarves HP: {result1['casket2_hp']}")

    # ========================================================================
    # SCENARIO 2: Ossuarium vs Elves (Lifesteal vs Bleed)
    # ========================================================================
    print("\n[SCENARIO 2] Ossuarium vs Elves")
    print("-" * 60)

    ossuarium = create_test_casket("Bone Lord", "ossuarium", CasketClass.ASSAULT)
    elves = create_test_casket("Thornblade", "elves", CasketClass.SCOUT)

    combat2 = CombatSimulator(ossuarium, elves)
    result2 = combat2.run_combat(max_turns=15)
    results["combat_scenarios"].append(result2)

    print(f"Winner: {result2['winner']}")
    print(f"Turns: {result2['turns']}")
    print(f"Ossuarium HP: {result2['casket1_hp']}")
    print(f"Elves HP: {result2['casket2_hp']}")

    # ========================================================================
    # SCENARIO 3: Scout vs Fortress (Speed vs Tank)
    # ========================================================================
    print("\n[SCENARIO 3] Scout vs Fortress (Speed vs Tank)")
    print("-" * 60)

    scout = create_test_casket("Swift Striker", "elves", CasketClass.SCOUT)
    fortress = create_test_casket("Iron Wall", "dwarves", CasketClass.FORTRESS)

    combat3 = CombatSimulator(scout, fortress)
    result3 = combat3.run_combat(max_turns=20)
    results["combat_scenarios"].append(result3)

    print(f"Winner: {result3['winner']}")
    print(f"Turns: {result3['turns']}")
    print(f"Scout HP: {result3['casket1_hp']}")
    print(f"Fortress HP: {result3['casket2_hp']}")

    # ========================================================================
    # CAMPAIGN 1: Church 3-Mission Arc
    # ========================================================================
    print("\n[CAMPAIGN 1] Church 3-Mission Campaign")
    print("-" * 60)

    campaign_casket = create_test_casket("Penitent Crusader", "church", CasketClass.ASSAULT)
    campaign = CampaignSimulator(campaign_casket)
    campaign_result = campaign.run_campaign(num_missions=3)
    results["campaign_runs"].append(campaign_result)

    print(f"Success: {campaign_result['success']}")
    print(f"Missions: {campaign_result['missions_completed']}")
    print(f"Final HP: {campaign_result['final_hp']}")
    print(f"Final Scrap: {campaign_result['final_scrap']}")

    # ========================================================================
    # WRITE DETAILED REPORT
    # ========================================================================
    print("\n" + "=" * 60)
    print("WRITING DETAILED REPORT...")
    print("=" * 60)

    with open("/workspaces/penance/simulation/balance_report.txt", "w") as f:
        f.write("=" * 80 + "\n")
        f.write("PENANCE: Balance Analysis Report\n")
        f.write("=" * 80 + "\n\n")

        # Combat Scenarios
        f.write("\n### COMBAT SCENARIOS ###\n\n")
        for i, scenario in enumerate(results["combat_scenarios"], 1):
            f.write(f"\n--- Scenario {i} ---\n")
            f.write(f"Winner: {scenario['winner']}\n")
            f.write(f"Turns: {scenario['turns']}\n")
            f.write(f"HP Remaining: {scenario['casket1_hp']} vs {scenario['casket2_hp']}\n")
            f.write("\nCombat Log:\n")
            for log_entry in scenario['log']:
                f.write(f"  {log_entry}\n")

        # Campaign
        f.write("\n\n### CAMPAIGN RUNS ###\n\n")
        for i, campaign in enumerate(results["campaign_runs"], 1):
            f.write(f"\n--- Campaign {i} ---\n")
            f.write(f"Success: {campaign['success']}\n")
            f.write(f"Missions Completed: {campaign['missions_completed']}\n")
            f.write(f"Final HP: {campaign['final_hp']}\n")
            f.write(f"Final Scrap: {campaign['final_scrap']}\n")
            f.write("\nCampaign Log:\n")
            for log_entry in campaign['log']:
                f.write(f"  {log_entry}\n")

        # Balance Analysis
        f.write("\n\n" + "=" * 80 + "\n")
        f.write("BALANCE OBSERVATIONS\n")
        f.write("=" * 80 + "\n\n")

        f.write("1. FACTION BALANCE:\n")
        f.write("   - Church (Self-Harm): High burst damage but self-destructive\n")
        f.write("   - Dwarves (Runes): Slow ramp-up but strong late game\n")
        f.write("   - Ossuarium (Lifesteal): Sustain-focused, hard to kill\n")
        f.write("   - Elves (Bleed): DoT-based, scales with fight length\n\n")

        f.write("2. CASKET CLASS BALANCE:\n")
        f.write("   - Scout (6 SP): Fast cycling, high actions per turn\n")
        f.write("   - Assault (5 SP): Balanced\n")
        f.write("   - Heavy (4 SP): Tankier, fewer actions\n")
        f.write("   - Fortress (3 SP): Very tanky, slow\n\n")

        f.write("3. POTENTIAL ISSUES:\n")
        f.write("   - Church may kill themselves too quickly\n")
        f.write("   - Ossuarium lifesteal may be too strong in long fights\n")
        f.write("   - Fortress class may struggle against kiting\n")
        f.write("   - Bleed stacking may need cap to prevent runaway scaling\n\n")

        f.write("4. RECOMMENDATIONS:\n")
        f.write("   - Test Church self-harm: limit to 1 use per turn\n")
        f.write("   - Cap Bleed counters at 10\n")
        f.write("   - Add mobility options for Fortress class\n")
        f.write("   - Consider Lifesteal diminishing returns after 10 HP healed\n\n")

    print("Report saved to: /workspaces/penance/simulation/balance_report.txt")
    print("\nSimulation complete!")

if __name__ == "__main__":
    run_balance_tests()
