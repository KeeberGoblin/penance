#!/usr/bin/env python3
"""
Penance Combat & Campaign Simulator
Simulates combat scenarios and campaigns to identify balance issues
"""

import random
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Deque
from collections import deque
from enum import Enum

# ============================================================================
# GAME CONSTANTS
# ============================================================================

class CasketClass(Enum):
    # Format: (name, SP, deck_size_min, deck_size_max, HP)
    SCOUT = ("Scout", 6, 26, 32, 36)
    WARDEN = ("Warden", 5, 30, 38, 44)
    VANGUARD = ("Vanguard", 4, 36, 46, 52)
    COLOSSUS = ("Colossus", 3, 42, 50, 60)

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
    deck: Deque[Card] = field(default_factory=deque)
    hand: Deque[Card] = field(default_factory=deque)
    discard: Deque[Card] = field(default_factory=deque)

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

    # Cached HP value (updated when cards change)
    _cached_hp: int = field(default=0, init=False)
    _hp_dirty: bool = field(default=True, init=False)

    def __post_init__(self):
        _, sp, deck_min, deck_max, hp = self.casket_class.value
        self.sp_max = sp
        self.sp = sp

    @property
    def hp(self):
        """Current HP = cards remaining in deck + hand (cached)"""
        if self._hp_dirty:
            self._cached_hp = len(self.deck) + len(self.hand)
            self._hp_dirty = False
        return self._cached_hp

    def _invalidate_hp_cache(self):
        """Mark HP cache as dirty"""
        self._hp_dirty = True

    @property
    def is_alive(self):
        """Casket is alive if deck has cards or pilot isn't dead"""
        return self.hp > 0 and self.pilot_wounds < self.pilot_max_wounds

    def take_damage(self, amount: int) -> Dict[str, any]:
        """Apply damage to Casket (optimized with deque)"""
        # Apply Dwarven Rune Defense (BUFFED - max 2 reduction, minimum 1 damage)
        if self.faction == "dwarves" and self.rune_counters > 0:
            reduction = min(self.rune_counters, 2)  # BALANCED: Max 2 reduction (was 3)
            amount = max(1, amount - reduction)  # BUFFED: Minimum 1 damage (restored)

        result = {
            "damage_dealt": amount,
            "cards_discarded": 0,
            "component_damage": False,
            "pilot_wound": False
        }

        for _ in range(amount):
            if self.hand:
                discarded = self.hand.popleft()
                self.discard.append(discarded)
                result["cards_discarded"] += 1

                # Check for component damage (if Primary Weapon card)
                if "weapon" in discarded.type.lower():
                    result["component_damage"] = True
            elif self.deck:
                discarded = self.deck.popleft()
                self.discard.append(discarded)
                result["cards_discarded"] += 1
            else:
                # Deck empty, reshuffle with damage card
                self.reshuffle_with_damage()

        self._invalidate_hp_cache()
        return result

    def reshuffle_with_damage(self):
        """Reshuffle discard pile into deck, add 1 Damage card (death spiral)"""
        # Convert deque to list for shuffling, then back to deque
        temp_list = list(self.discard)
        random.shuffle(temp_list)
        self.deck = deque(temp_list)
        self.discard.clear()
        # Add damage card (dead draw) to front
        self.deck.appendleft(Card(name="DAMAGE", type="dead_draw", sp_cost=99, effect="Dead card (cannot be played)"))
        self._invalidate_hp_cache()

    def draw_cards(self, count: int):
        """Draw cards from deck (optimized)"""
        for _ in range(count):
            if self.deck:
                self.hand.append(self.deck.popleft())
            else:
                # Deck empty, reshuffle
                if self.discard:
                    self.reshuffle_with_damage()
                    if self.deck:
                        self.hand.append(self.deck.popleft())

        self._invalidate_hp_cache()

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
    def __init__(self, casket1: Casket, casket2: Casket, verbose: bool = True):
        self.casket1 = casket1
        self.casket2 = casket2
        self.turn = 0
        self.log = [] if verbose else None
        self.verbose = verbose

    def log_event(self, message: str):
        """Log combat event (only if verbose mode enabled)"""
        if self.verbose:
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
            defender.bleed_counters = max(0, defender.bleed_counters - 1)  # BALANCED: -1 decay (reverted from -2)

        # Reduce heat slightly
        attacker.heat = max(0, attacker.heat - 1)

    def simulate_attack_phase(self, attacker: Casket, defender: Casket) -> int:
        """Simulate attack decisions based on faction"""
        total_damage = 0

        # Church: Blood Offering (BALANCED - +1 damage bonus)
        if attacker.faction == "church":
            # Blood Offering: Discard 1 card from deck for +1 damage (NERFED from +2)
            if len(attacker.hand) >= 2 and len(attacker.deck) >= 1:  # BUFFED: 2 cards instead of 3
                # Discard 1 card from top of deck (self-harm via card loss)
                discarded = attacker.deck.popleft()
                attacker.discard.append(discarded)
                attacker._invalidate_hp_cache()
                attacker.blood_offering_bonus = 2  # BUFFED: +2 (was +1)
                self.log_event(f"{attacker.name} uses Blood Offering (discards 1 card, +2 damage)")
            else:
                attacker.blood_offering_bonus = 0

            # Attack
            base_damage = 4 + attacker.blood_offering_bonus
            defender.take_damage(base_damage)
            total_damage = base_damage
            attacker.blood_offering_bonus = 0
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Dwarves: Defensive Runes (BALANCED - cap 2)
        elif attacker.faction == "dwarves":
            # Gain 1 defensive rune every 2 turns, max 2
            if self.turn % 2 == 0 and attacker.rune_counters < 2:  # BALANCED: cap 2
                attacker.rune_counters += 1
                self.log_event(f"{attacker.name} gains 1 Rune counter (defense, total: {attacker.rune_counters})")

            # Crushing Blow: 5 damage, armor-piercing (BUFFED)
            base_damage = 5  # BUFFED: 5 damage (4 was too weak)
            defender.take_damage(base_damage)
            total_damage = base_damage
            self.log_event(f"{attacker.name} uses Crushing Blow for {base_damage} damage (Rune Defense: -{attacker.rune_counters})")

        # Ossuarium: Taint Exploitation (v3.0 - gains Taint from damage, spends for lifesteal)
        elif attacker.faction == "ossuarium":
            # Initialize Taint counters
            if not hasattr(attacker, 'taint_counters'):
                attacker.taint_counters = 0

            # Soul Harvest: costs 1 SP, deals 5 damage, gains Taint (BUFFED: was 4 damage)
            if attacker.sp >= 1:
                attacker.sp -= 1
                base_damage = 5  # BUFFED: 5 damage (was 4)
                defender.take_damage(base_damage)
                total_damage = base_damage

                # FIXED: Ossuarium gains Taint from damage dealt (1 per 2 damage)
                taint_gained = base_damage // 2  # 5 dmg = 2 Taint
                attacker.taint_counters += taint_gained

                # Spend 2 Taint to recover 2 cards (conditional lifesteal!)
                if attacker.taint_counters >= 2:
                    attacker.taint_counters -= 2
                    cards_recovered = 2
                    for _ in range(cards_recovered):
                        if attacker.discard:
                            recycled = attacker.discard.pop()
                            attacker.hand.append(recycled)
                    attacker._invalidate_hp_cache()
                    self.log_event(f"{attacker.name} uses Soul Harvest (1 SP) for {base_damage} damage, spends 2 Taint to recover {cards_recovered} cards")
                else:
                    self.log_event(f"{attacker.name} uses Soul Harvest (1 SP) for {base_damage} damage, gains {taint_gained} Taint (total: {attacker.taint_counters})")
            else:
                # Not enough SP: basic attack
                base_damage = 3
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Elves: Bleed stacking (BALANCED - proper stacking with -1 decay)
        elif attacker.faction == "elves":
            base_damage = 3  # BUFFED: 3 damage (was 2)
            defender.take_damage(base_damage)
            total_damage = base_damage

            # Apply Bleed (BUFFED: +2 per attack, -1 decay, cap 6)
            defender.bleed_counters = min(defender.bleed_counters + 2, 6)  # BUFFED: Cap 6 (was 5)
            self.log_event(f"{attacker.name} attacks for {base_damage} damage, applies 1 Bleed (total: {defender.bleed_counters})")

        # Crucible: Honor Duel (BUFFED - proper bonus stacking)
        elif attacker.faction == "crucible":
            # Initialize honor_duel_bonus if needed
            if not hasattr(attacker, 'honor_duel_bonus'):
                attacker.honor_duel_bonus = 0

            # Use Honor Duel to gain bonus for next turn
            if attacker.sp >= 1 and attacker.honor_duel_bonus == 0:
                attacker.sp -= 1
                base_damage = 5
                defender.take_damage(base_damage)
                total_damage = base_damage
                attacker.honor_duel_bonus = 2  # Set bonus for next turn
                self.log_event(f"{attacker.name} uses Honor Duel for {base_damage} damage (+2 next turn)")
            # Use accumulated bonus
            elif attacker.honor_duel_bonus > 0:
                base_damage = 5 + attacker.honor_duel_bonus  # Use accumulated bonus
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks with Honor Duel bonus for {base_damage} damage")
                attacker.honor_duel_bonus = 0  # Consume bonus
            else:
                base_damage = 4
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Exchange: Credit economy (resource generation + card draw)
        elif attacker.faction == "exchange":
            # Initialize credit counters if needed
            if not hasattr(attacker, 'credit_counters'):
                attacker.credit_counters = 0

            # Spend 3 credits for card draw (sustain)
            if attacker.credit_counters >= 3:
                attacker.credit_counters -= 3
                for _ in range(3):
                    if attacker.discard:
                        recycled = attacker.discard.pop()
                        attacker.hand.append(recycled)
                attacker._invalidate_hp_cache()
                base_damage = 4
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} spends 3 credits, recovers 3 cards, attacks for {base_damage} damage")
            # Earn credits (NERFED: 5 damage)
            elif attacker.sp >= 2:
                attacker.sp -= 2
                base_damage = 5  # NERFED: 5 damage (6 was too strong)
                defender.take_damage(base_damage)
                total_damage = base_damage
                attacker.credit_counters += 1
                self.log_event(f"{attacker.name} uses Mercenary Contract for {base_damage} damage, gains 1 credit (total: {attacker.credit_counters})")
            else:
                base_damage = 4
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Nomads: Random burst damage (high variance) - BUFFED: 6-9 damage
        elif attacker.faction == "nomads":
            # BUFFED: Free activation (0 SP), higher damage range 8-11
            base_damage = random.randint(8, 11)  # BUFFED: 8-11 random damage (was 7-10)
            defender.take_damage(base_damage)
            total_damage = base_damage
            self.log_event(f"{attacker.name} uses Improvised Weapon for {base_damage} damage (free!)")

        # Bloodlines: Biomass Stacking (v3.0 - damage escalation, no lifesteal)
        elif attacker.faction == "bloodlines":
            # Initialize biomass stacks
            if not hasattr(attacker, 'biomass_stacks'):
                attacker.biomass_stacks = 0

            if attacker.sp >= 2:
                attacker.sp -= 2

                # Gain biomass stack (max 3)
                attacker.biomass_stacks = min(attacker.biomass_stacks + 1, 3)

                # Damage scales: 6 + (stacks × 2) = 8/10/12 progression (BUFFED from 7/9/11)
                base_damage = 6 + (attacker.biomass_stacks * 2)  # BUFFED: 6 base (7/9/11 was too weak)
                defender.take_damage(base_damage)
                total_damage = base_damage

                self.log_event(f"{attacker.name} uses Biomass Absorption for {base_damage} damage (Biomass: {attacker.biomass_stacks}/3)")
            else:
                base_damage = 4
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Emergent: Metamorph (temporary power spike)
        elif attacker.faction == "emergent":
            # Initialize metamorph tracking
            if not hasattr(attacker, 'metamorph_turns'):
                attacker.metamorph_turns = 0

            # Activate Metamorph (BALANCED: +1 damage)
            if attacker.sp >= 3 and attacker.metamorph_turns == 0:
                attacker.sp -= 3
                attacker.metamorph_turns = 3
                base_damage = 5  # +1 from metamorph (balanced)
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} uses Metamorph, +1 damage for 3 turns")
            # Metamorph active
            elif attacker.metamorph_turns > 0:
                base_damage = 5  # +1 from metamorph
                defender.take_damage(base_damage)
                total_damage = base_damage
                attacker.metamorph_turns -= 1
                if attacker.metamorph_turns == 0:
                    attacker.take_damage(2)  # Strain damage
                    self.log_event(f"{attacker.name} Metamorph ends, takes 2 strain damage")
                self.log_event(f"{attacker.name} attacks for {base_damage} damage (Metamorph: {attacker.metamorph_turns} turns left)")
            else:
                base_damage = 4
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Wyrd: Reality Distortion (defense bypass) - NERFED: 4 damage
        elif attacker.faction == "wyrd":
            if attacker.sp >= 4:
                attacker.sp -= 4
                base_damage = 4  # NERFED: 4 damage (5 was too strong), ignores defense

                # Temporarily bypass Dwarven runes
                original_runes = 0
                if defender.faction == "dwarves" and hasattr(defender, 'rune_counters'):
                    original_runes = defender.rune_counters
                    defender.rune_counters = 0

                defender.take_damage(base_damage)
                total_damage = base_damage

                # Restore runes
                if defender.faction == "dwarves":
                    defender.rune_counters = original_runes

                self.log_event(f"{attacker.name} uses Reality Distortion for {base_damage} damage (ignores defense)")
            else:
                base_damage = 4
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Generic fallback (should not be reached)
        else:
            base_damage = 4
            defender.take_damage(base_damage)
            total_damage = base_damage
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        return total_damage

    def run_combat(self, max_turns: Optional[int] = None) -> Dict[str, any]:
        """Run full combat simulation

        Args:
            max_turns: Maximum number of turns before forced draw (None = unlimited)
        """
        self.log_event(f"COMBAT START: {self.casket1.name} vs {self.casket2.name}")
        self.log_event(f"{self.casket1.name}: {self.casket1.hp} HP ({self.casket1.faction})")
        self.log_event(f"{self.casket2.name}: {self.casket2.hp} HP ({self.casket2.faction})")

        # Alternate turns
        while self.casket1.is_alive and self.casket2.is_alive and (max_turns is None or self.turn < max_turns):
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
            if max_turns and self.turn >= max_turns:
                self.log_event(f"DRAW (turn limit of {max_turns} reached)")
            else:
                self.log_event(f"DRAW (both caskets destroyed simultaneously)")

        self.log_event(f"{self.casket1.name} final HP: {self.casket1.hp}")
        self.log_event(f"{self.casket2.name} final HP: {self.casket2.hp}")

        return {
            "winner": winner.name if winner else "Draw",
            "turns": self.turn,
            "casket1_hp": self.casket1.hp,
            "casket2_hp": self.casket2.hp,
            "log": self.log if self.verbose else []
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

    def run_mission(self, enemy_faction: str, max_turns: Optional[int] = None):
        """Simulate a single mission

        Args:
            enemy_faction: Faction of the enemy to fight
            max_turns: Maximum combat turns (None = unlimited)
        """
        self.mission += 1
        self.log_event(f"\n=== MISSION {self.mission}: vs {enemy_faction} ===")

        # Create enemy
        enemy = self.create_enemy(enemy_faction)

        # Run combat
        combat = CombatSimulator(self.casket, enemy)
        result = combat.run_combat(max_turns=max_turns)

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
        """Create enemy Casket (optimized)"""
        enemy = Casket(
            name=f"{faction.capitalize()} Enemy",
            faction=faction,
            casket_class=CasketClass.WARDEN
        )

        # Build enemy deck (simplified) - create cards in batch using deck min size
        _, _, deck_min, _, _ = CasketClass.WARDEN.value
        cards = [Card(name="Generic Card", type="attack", sp_cost=2, damage=3) for _ in range(deck_min)]
        random.shuffle(cards)
        enemy.deck = deque(cards)
        enemy.draw_cards(6)

        return enemy

    def run_campaign(self, num_missions: int = 3, max_turns_per_mission: Optional[int] = None) -> Dict[str, any]:
        """Run full campaign

        Args:
            num_missions: Number of missions to complete
            max_turns_per_mission: Maximum turns per combat (None = unlimited)
        """
        self.log_event(f"=== CAMPAIGN START: {self.casket.name} ===")
        self.log_event(f"Starting HP: {self.casket.hp}")
        self.log_event(f"Starting Scrap: {self.scrap}")

        factions = ["church", "dwarves", "ossuarium", "elves"]

        for i in range(num_missions):
            enemy_faction = random.choice(factions)
            success = self.run_mission(enemy_faction, max_turns=max_turns_per_mission)

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
    """Create a test Casket with a basic deck (optimized)"""
    casket = Casket(name=name, faction=faction, casket_class=casket_class)

    # Build deck (simplified) - create cards in batch
    _, _, deck_min, deck_max, _ = casket_class.value
    deck_size = deck_min  # Use minimum deck size for consistency
    cards = [
        Card(
            name="Generic Card",
            type="attack" if random.random() > 0.3 else "defense",
            sp_cost=random.randint(1, 3),
            damage=random.randint(2, 5)
        )
        for _ in range(deck_size)
    ]

    random.shuffle(cards)
    casket.deck = deque(cards)
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
    print("\n[SCENARIO 1] Church vs Dwarves (Warden class)")
    print("-" * 60)

    church = create_test_casket("Holy Avenger", "church", CasketClass.WARDEN)
    dwarves = create_test_casket("Runeforge Titan", "dwarves", CasketClass.VANGUARD)

    combat1 = CombatSimulator(church, dwarves)
    result1 = combat1.run_combat()  # Unlimited turns
    results["combat_scenarios"].append(result1)

    print(f"Winner: {result1['winner']}")
    print(f"Turns: {result1['turns']}")
    print(f"Church HP: {result1['casket1_hp']}")
    print(f"Dwarves HP: {result1['casket2_hp']}")

    # ========================================================================
    # SCENARIO 2: Ossuarium vs Elves (Lifesteal vs Bleed)
    # ========================================================================
    print("\n[SCENARIO 2] Ossuarium vs Elves (Warden vs Scout)")
    print("-" * 60)

    ossuarium = create_test_casket("Bone Lord", "ossuarium", CasketClass.WARDEN)
    elves = create_test_casket("Thornblade", "elves", CasketClass.SCOUT)

    combat2 = CombatSimulator(ossuarium, elves)
    result2 = combat2.run_combat()  # Unlimited turns
    results["combat_scenarios"].append(result2)

    print(f"Winner: {result2['winner']}")
    print(f"Turns: {result2['turns']}")
    print(f"Ossuarium HP: {result2['casket1_hp']}")
    print(f"Elves HP: {result2['casket2_hp']}")

    # ========================================================================
    # SCENARIO 3: Scout vs Colossus (Speed vs Tank)
    # ========================================================================
    print("\n[SCENARIO 3] Scout vs Colossus (Speed vs Tank)")
    print("-" * 60)

    scout = create_test_casket("Swift Striker", "elves", CasketClass.SCOUT)
    colossus = create_test_casket("Iron Wall", "dwarves", CasketClass.COLOSSUS)

    combat3 = CombatSimulator(scout, colossus)
    result3 = combat3.run_combat()  # Unlimited turns
    results["combat_scenarios"].append(result3)

    print(f"Winner: {result3['winner']}")
    print(f"Turns: {result3['turns']}")
    print(f"Scout HP: {result3['casket1_hp']}")
    print(f"Colossus HP: {result3['casket2_hp']}")

    # ========================================================================
    # CAMPAIGN 1: Church 3-Mission Arc
    # ========================================================================
    print("\n[CAMPAIGN 1] Church 3-Mission Campaign (Warden)")
    print("-" * 60)

    campaign_casket = create_test_casket("Penitent Crusader", "church", CasketClass.WARDEN)
    campaign = CampaignSimulator(campaign_casket)
    campaign_result = campaign.run_campaign(num_missions=3)  # Unlimited turns per mission
    results["campaign_runs"].append(campaign_result)

    print(f"Success: {campaign_result['success']}")
    print(f"Missions: {campaign_result['missions_completed']}")
    print(f"Final HP: {campaign_result['final_hp']}")
    print(f"Final Scrap: {campaign_result['final_scrap']}")

    # ========================================================================
    # WRITE DETAILED REPORT (Optimized file I/O)
    # ========================================================================
    print("\n" + "=" * 60)
    print("WRITING DETAILED REPORT...")
    print("=" * 60)

    # Build report in memory first, then write once
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("PENANCE: Balance Analysis Report")
    report_lines.append("=" * 80)
    report_lines.append("")

    # Combat Scenarios
    report_lines.append("\n### COMBAT SCENARIOS ###\n")
    for i, scenario in enumerate(results["combat_scenarios"], 1):
        report_lines.append(f"\n--- Scenario {i} ---")
        report_lines.append(f"Winner: {scenario['winner']}")
        report_lines.append(f"Turns: {scenario['turns']}")
        report_lines.append(f"HP Remaining: {scenario['casket1_hp']} vs {scenario['casket2_hp']}")
        report_lines.append("\nCombat Log:")
        report_lines.extend(f"  {log_entry}" for log_entry in scenario['log'])

    # Campaign
    report_lines.append("\n\n### CAMPAIGN RUNS ###\n")
    for i, campaign in enumerate(results["campaign_runs"], 1):
        report_lines.append(f"\n--- Campaign {i} ---")
        report_lines.append(f"Success: {campaign['success']}")
        report_lines.append(f"Missions Completed: {campaign['missions_completed']}")
        report_lines.append(f"Final HP: {campaign['final_hp']}")
        report_lines.append(f"Final Scrap: {campaign['final_scrap']}")
        report_lines.append("\nCampaign Log:")
        report_lines.extend(f"  {log_entry}" for log_entry in campaign['log'])

    # Balance Analysis
    report_lines.append("\n\n" + "=" * 80)
    report_lines.append("BALANCE OBSERVATIONS")
    report_lines.append("=" * 80 + "\n")

    report_lines.append("1. FACTION BALANCE:")
    report_lines.append("   - Church (Self-Harm): High burst damage but self-destructive")
    report_lines.append("   - Dwarves (Runes): Slow ramp-up but strong late game")
    report_lines.append("   - Ossuarium (Lifesteal): Sustain-focused, hard to kill")
    report_lines.append("   - Elves (Bleed): DoT-based, scales with fight length\n")

    report_lines.append("2. CASKET CLASS BALANCE:")
    report_lines.append("   - Scout (6 SP): Fast cycling, high actions per turn")
    report_lines.append("   - Assault (5 SP): Balanced")
    report_lines.append("   - Heavy (4 SP): Tankier, fewer actions")
    report_lines.append("   - Fortress (3 SP): Very tanky, slow\n")

    report_lines.append("3. POTENTIAL ISSUES:")
    report_lines.append("   - Church may kill themselves too quickly")
    report_lines.append("   - Ossuarium lifesteal may be too strong in long fights")
    report_lines.append("   - Fortress class may struggle against kiting")
    report_lines.append("   - Bleed stacking may need cap to prevent runaway scaling\n")

    report_lines.append("4. RECOMMENDATIONS:")
    report_lines.append("   - Test Church self-harm: limit to 1 use per turn")
    report_lines.append("   - Cap Bleed counters at 10")
    report_lines.append("   - Add mobility options for Fortress class")
    report_lines.append("   - Consider Lifesteal diminishing returns after 10 HP healed\n")

    # Write report in single operation
    report_path = "C:\\GAMES\\GitHub\\penance\\simulation\\balance_report.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))

    print(f"Report saved to: {report_path}")
    print("\nSimulation complete!")

if __name__ == "__main__":
    run_balance_tests()
