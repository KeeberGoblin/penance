#!/usr/bin/env python3
"""
Penance Combat Simulator v2.0 - Realistic Damage Scaling
Properly models component damage system with 1-4 damage range
"""

import random
from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict, Optional
from enum import Enum

# ============================================================================
# COMPONENT HP CONSTANTS (from component-damage-system.md)
# ============================================================================

COMPONENT_HP = {
    "head": {"total": 6, "ap": 2, "structure": 4, "exposure": 5},
    "right_arm": {"total": 8, "ap": 3, "structure": 4, "exposure": 6},
    "left_arm": {"total": 8, "ap": 3, "structure": 4, "exposure": 6},
    "chassis": {"total": 10, "ap": 4, "structure": 5, "exposure": 7},
    "legs": {"total": 8, "ap": 3, "structure": 4, "exposure": 999}  # No pilot exposure
}

# ============================================================================
# CASKET CLASSES
# ============================================================================

class CasketClass(Enum):
    # Format: (name, SP, deck_size, HP)
    SCOUT = ("Scout", 6, 28, 28)       # Fast, fragile
    WARDEN = ("Warden", 5, 34, 34)     # Balanced
    VANGUARD = ("Vanguard", 4, 40, 40) # Slow, tanky
    COLOSSUS = ("Colossus", 3, 50, 50) # Boss unit

# ============================================================================
# CASKET DATA CLASS
# ============================================================================

@dataclass
class Casket:
    """Represents a Casket (mech) with card-based HP and component damage"""
    name: str
    faction: str
    casket_class: CasketClass

    # Card-based HP system
    deck: Deque = field(default_factory=deque)
    hand: Deque = field(default_factory=deque)
    discard: Deque = field(default_factory=deque)

    # SP and Heat
    sp: int = 0
    sp_max: int = 0
    heat: int = 0

    # Component Damage (0-8 per component)
    component_damage: Dict[str, int] = field(default_factory=lambda: {
        "head": 0, "right_arm": 0, "left_arm": 0, "chassis": 0, "legs": 0
    })

    # Pilot Wounds
    pilot_wounds: int = 0
    pilot_max_wounds: int = 10

    # Faction-specific counters
    rune_counters: int = 0       # Dwarves
    bleed_counters: int = 0      # Elves
    taint_counters: int = 0      # Ossuarium
    lifesteal_cooldown: int = 0  # Ossuarium (ROUND 6: prevent infinite stalemates)
    credit_counters: int = 0     # Exchange
    biomass_stacks: int = 0      # Bloodlines
    metamorph_turns: int = 0     # Emergent

    # Cached HP
    _cached_hp: int = field(default=0, init=False)
    _hp_dirty: bool = field(default=True, init=False)

    def __post_init__(self):
        _, sp, deck_size, hp = self.casket_class.value
        self.sp_max = sp
        self.sp = sp

        # Initialize deck with generic cards
        for i in range(deck_size):
            self.deck.append(f"Card-{i}")

        self._invalidate_hp_cache()

    @property
    def hp(self):
        """Current HP = cards in deck + hand"""
        if self._hp_dirty:
            self._cached_hp = len(self.deck) + len(self.hand)
            self._hp_dirty = False
        return self._cached_hp

    def _invalidate_hp_cache(self):
        self._hp_dirty = True

    @property
    def is_alive(self):
        return self.hp > 0 and self.pilot_wounds < self.pilot_max_wounds

    def refresh_sp(self):
        """Start of turn SP refresh"""
        self.sp = self.sp_max

    def draw_cards(self, count: int):
        """Draw cards from deck to hand"""
        for _ in range(min(count, len(self.deck))):
            card = self.deck.popleft()
            self.hand.append(card)
        self._invalidate_hp_cache()

    def take_damage(self, amount: int, component: str = "chassis"):
        """Take damage - discard cards and track component damage"""
        if amount <= 0:
            return

        # ROUND 3: Removed Dwarven rune defense (was fundamentally overpowered)

        # Discard cards from hand/deck
        cards_to_discard = min(amount, self.hp)
        for _ in range(cards_to_discard):
            if self.hand:
                self.hand.pop()
            elif self.deck:
                self.deck.pop()
            else:
                break

        self._invalidate_hp_cache()

        # Component damage = 1 per damage dealt (simplified)
        self.add_component_damage(component, cards_to_discard)

    def add_component_damage(self, component: str, amount: int):
        """Add component damage and check for pilot exposure wounds"""
        if amount <= 0 or component not in self.component_damage:
            return

        old_damage = self.component_damage[component]
        new_damage = min(old_damage + amount, COMPONENT_HP[component]["total"])
        self.component_damage[component] = new_damage

        # Check for pilot exposure wounds
        exposure_threshold = COMPONENT_HP[component]["exposure"]
        if exposure_threshold < 999:  # Legs have no exposure
            # Count damage that occurred while in exposure zone
            for dmg_point in range(old_damage + 1, new_damage + 1):
                if dmg_point >= exposure_threshold:
                    self.pilot_wounds += 1

# ============================================================================
# COMBAT SIMULATOR
# ============================================================================

class CombatSimulator:
    """Simulates 1v1 combat between two Caskets"""

    def __init__(self, casket1: Casket, casket2: Casket, verbose: bool = True):
        self.casket1 = casket1
        self.casket2 = casket2
        self.turn = 0
        self.log = [] if verbose else None
        self.verbose = verbose

    def log_event(self, message: str):
        if self.verbose:
            self.log.append(f"[Turn {self.turn}] {message}")

    def run_combat(self, max_turns: Optional[int] = None):
        """Run combat simulation"""
        self.log_event(f"COMBAT START: {self.casket1.name} vs {self.casket2.name}")

        # Combat loop
        while self.casket1.is_alive and self.casket2.is_alive:
            self.turn += 1

            # Check turn limit
            if max_turns and self.turn > max_turns:
                self.log_event("DRAW (turn limit reached)")
                return {
                    "winner": None,
                    "turns": self.turn,
                    "casket1_hp": self.casket1.hp,
                    "casket2_hp": self.casket2.hp,
                    "log": self.log if self.verbose else []
                }

            # Casket 1 turn
            self.simulate_turn(self.casket1, self.casket2)
            if not self.casket2.is_alive:
                break

            # Casket 2 turn
            self.simulate_turn(self.casket2, self.casket1)

        # Determine winner
        winner = None
        if self.casket1.is_alive and not self.casket2.is_alive:
            winner = self.casket1.name
        elif self.casket2.is_alive and not self.casket1.is_alive:
            winner = self.casket2.name

        self.log_event(f"COMBAT END - Winner: {winner if winner else 'DRAW'}")

        return {
            "winner": winner,
            "turns": self.turn,
            "casket1_hp": self.casket1.hp,
            "casket2_hp": self.casket2.hp,
            "log": self.log if self.verbose else []
        }

    def simulate_turn(self, attacker: Casket, defender: Casket):
        """Simulate one turn of combat"""
        # Phase 1: Refresh
        attacker.refresh_sp()
        attacker.draw_cards(3)

        # Phase 2: Action Phase - Simulate attacks based on faction
        self.simulate_attack_phase(attacker, defender)

        # Phase 3: End Phase
        # Bleed damage (ROUND 4: back to 1 damage per stack)
        if defender.bleed_counters > 0:
            bleed_dmg = defender.bleed_counters  # 1 damage per stack
            defender.take_damage(bleed_dmg, "chassis")
            self.log_event(f"{defender.name} takes {bleed_dmg} Bleed damage ({defender.bleed_counters} stacks)")
            defender.bleed_counters = max(0, defender.bleed_counters - 1)

        # Reduce heat
        attacker.heat = max(0, attacker.heat - 1)

    def simulate_attack_phase(self, attacker: Casket, defender: Casket):
        """Simulate faction-specific attack patterns - REALISTIC DAMAGE (1-3)"""

        # Church: Self-harm for bonus damage
        if attacker.faction == "church":
            # Blood Offering: Discard 1 card for +1 damage (ROUND 7: back to 3 baseline)
            if len(attacker.hand) >= 2:
                attacker.hand.pop()
                attacker._invalidate_hp_cache()
                base_damage = 4  # 3 base + 1 bonus
                self.log_event(f"{attacker.name} uses Blood Offering (+1 damage)")
            else:
                base_damage = 3  # ROUND 7: 3 damage baseline

            defender.take_damage(base_damage, "right_arm")
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Dwarves: HP regeneration (ROUND 6: increased regen rate)
        elif attacker.faction == "dwarves":
            # Recover 1 card from discard EVERY turn (was every 2 turns)
            if len(attacker.discard) > 0:
                card = attacker.discard.pop()
                attacker.deck.append(card)
                self.log_event(f"{attacker.name} recovers 1 card from discard (HP regen)")

            base_damage = 3  # ROUND 6: reduce to 3 (compensate with faster regen)
            defender.take_damage(base_damage, "right_arm")
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Ossuarium: Lifesteal (recover cards from discard) (ROUND 7: back to 3 baseline)
        elif attacker.faction == "ossuarium":
            if attacker.sp >= 2:
                attacker.sp -= 2
                base_damage = 3  # ROUND 7: 3 damage baseline
                defender.take_damage(base_damage, "right_arm")

                # Gain Taint (1 per damage dealt)
                attacker.taint_counters += base_damage

                # Spend 2 Taint to recover 1 card (ROUND 6: cap to prevent infinite stalemates)
                if attacker.taint_counters >= 2 and attacker.lifesteal_cooldown == 0:
                    attacker.taint_counters -= 2
                    if attacker.discard:
                        card = attacker.discard.pop()
                        attacker.hand.append(card)
                        attacker._invalidate_hp_cache()
                        attacker.lifesteal_cooldown = 3  # 3 turn cooldown
                        self.log_event(f"{attacker.name} uses Soul Harvest (2 SP), recovers 1 card")
                    else:
                        self.log_event(f"{attacker.name} uses Soul Harvest (2 SP), gains Taint")
                else:
                    self.log_event(f"{attacker.name} attacks for {base_damage} damage, gains Taint")

                # Reduce cooldown
                if attacker.lifesteal_cooldown > 0:
                    attacker.lifesteal_cooldown -= 1
            else:
                base_damage = 3  # ROUND 7: 3 damage baseline
                defender.take_damage(base_damage, "right_arm")
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Elves: Bleed stacking (damage over time) (ROUND 7: back to 2 base)
        elif attacker.faction == "elves":
            base_damage = 2  # ROUND 7: 2 base (Bleed compensates for lower damage)
            defender.take_damage(base_damage, "right_arm")

            # Apply +1 Bleed, cap at 4
            defender.bleed_counters = min(defender.bleed_counters + 1, 4)
            self.log_event(f"{attacker.name} attacks for {base_damage} damage, applies Bleed (total: {defender.bleed_counters})")

        # Crucible: Standard attacks (ROUND 6: reduced to 3 to avoid "free" high damage)
        elif attacker.faction == "crucible":
            base_damage = 3  # ROUND 6: reduced to 3 (high damage should have cost)
            defender.take_damage(base_damage, "right_arm")
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Exchange: Credit system (ROUND 7: back to 3 baseline)
        elif attacker.faction == "exchange":
            if attacker.sp >= 2:
                attacker.sp -= 2
                base_damage = 3  # ROUND 7: 3 damage baseline
                defender.take_damage(base_damage, "right_arm")
                attacker.credit_counters += 1
                self.log_event(f"{attacker.name} uses Mercenary Contract (2 SP), gains 1 credit (total: {attacker.credit_counters})")
            else:
                base_damage = 3  # ROUND 7: 3 damage baseline
                defender.take_damage(base_damage, "right_arm")
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Nomads: Random burst damage (ROUND 2: 2-4 range, was 1-3)
        elif attacker.faction == "nomads":
            base_damage = random.randint(2, 4)  # BUFFED: 2-4 (avg 3, was 1-3)
            defender.take_damage(base_damage, "right_arm")
            self.log_event(f"{attacker.name} uses Improvised Weapon for {base_damage} damage")

        # Bloodlines: Burst damage (ROUND 8: reduce burst to 3, remove burst mechanic)
        elif attacker.faction == "bloodlines":
            # ROUND 8: Flat 3 damage (burst mechanic removed, too swingy)
            base_damage = 3  # Same as everyone else
            defender.take_damage(base_damage, "right_arm")
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Emergent: Metamorph (temporary power spike) (ROUND 7: back to 3 turns, 3 baseline)
        elif attacker.faction == "emergent":
            if attacker.sp >= 3 and attacker.metamorph_turns == 0:
                attacker.sp -= 3
                attacker.metamorph_turns = 3  # ROUND 7: 3 turns
                base_damage = 3  # ROUND 7: 3 damage baseline
                defender.take_damage(base_damage, "right_arm")
                self.log_event(f"{attacker.name} uses Metamorph (3 SP), +1 damage for 3 turns")
            elif attacker.metamorph_turns > 0:
                base_damage = 3  # ROUND 7: 3 damage baseline
                defender.take_damage(base_damage, "right_arm")
                attacker.metamorph_turns -= 1
                self.log_event(f"{attacker.name} attacks for {base_damage} damage (Metamorph: {attacker.metamorph_turns} turns left)")
            else:
                base_damage = 3  # ROUND 7: 3 damage baseline
                defender.take_damage(base_damage, "right_arm")
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Wyrd: Defense bypass (ROUND 6: nerfed to 3 damage)
        elif attacker.faction == "wyrd":
            if attacker.sp >= 3:
                attacker.sp -= 3
                base_damage = 3  # ROUND 6: reduced to 3 (was 4, defense bypass compensates)

                # Defense bypass (no longer needed for runes, but keep for future-proofing)
                defender.take_damage(base_damage, "right_arm")

                self.log_event(f"{attacker.name} uses Reality Distortion (3 SP) for {base_damage} damage (ignores defense)")
            else:
                base_damage = 3  # ROUND 6: reduced to 3 (was 4)
                defender.take_damage(base_damage, "right_arm")
                self.log_event(f"{attacker.name} attacks for {base_damage} damage")

        # Generic faction (ROUND 7: back to 3 baseline)
        else:
            base_damage = 3  # ROUND 7: 3 damage baseline
            defender.take_damage(base_damage, "right_arm")
            self.log_event(f"{attacker.name} attacks for {base_damage} damage")


# ============================================================================
# TEST CASKET CREATION
# ============================================================================

def create_test_casket(name: str, faction: str, casket_class: CasketClass) -> Casket:
    """Create a test casket with specified faction and class"""
    return Casket(
        name=name,
        faction=faction,
        casket_class=casket_class
    )


# ============================================================================
# MAIN TEST
# ============================================================================

if __name__ == "__main__":
    print("Penance Combat Simulator v2.0 - Realistic Damage Scaling")
    print("=" * 80)

    # Test combat with realistic damage
    church = create_test_casket("Church-Confessor", "church", CasketClass.WARDEN)
    dwarves = create_test_casket("Dwarf-Ironclad", "dwarves", CasketClass.WARDEN)

    combat = CombatSimulator(church, dwarves, verbose=True)
    result = combat.run_combat(max_turns=50)

    print(f"\nWinner: {result['winner']}")
    print(f"Turns: {result['turns']}")
    print(f"\nComponent Damage:")
    print(f"  Church Right Arm: {church.component_damage['right_arm']}/8 HP")
    print(f"  Church Chassis: {church.component_damage['chassis']}/10 HP")
    print(f"  Dwarves Right Arm: {dwarves.component_damage['right_arm']}/8 HP")
    print(f"  Dwarves Chassis: {dwarves.component_damage['chassis']}/10 HP")

    print(f"\nPilot Wounds:")
    print(f"  Church: {church.pilot_wounds}/10")
    print(f"  Dwarves: {dwarves.pilot_wounds}/10")

    print("\n" + "=" * 80)
    print("Combat Log:")
    for event in result['log'][:20]:  # Show first 20 events
        print(event)
