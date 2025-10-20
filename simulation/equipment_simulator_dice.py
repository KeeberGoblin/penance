#!/usr/bin/env python3
"""
Penance Equipment-Randomized Combat Simulator WITH DICE MECHANICS
Models realistic combat with custom attack/defense dice system
"""

import random
import json
from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict, List, Optional, Tuple
from enum import Enum

# ============================================================================
# CUSTOM DICE SYSTEM
# ============================================================================

class AttackDie:
    """
    Custom Attack Die (d6 with special faces)
    Face values: 1, 2, 3, 4, 5, 0 (JAM)
    """
    FACES = [1, 2, 3, 4, 5, 0]  # 0 = JAM face

    @staticmethod
    def roll() -> int:
        """Roll one attack die, return value (0-5)"""
        return random.choice(AttackDie.FACES)

    @staticmethod
    def roll_2d6() -> Tuple[int, int, int]:
        """
        Roll 2 attack dice, return (die1, die2, total)
        Returns individual die values and sum
        """
        die1 = AttackDie.roll()
        die2 = AttackDie.roll()
        total = die1 + die2
        return (die1, die2, total)

class DefenseDie:
    """
    Custom Defense Die (d6 with special effects)
    Faces: SHIELD, ABSORB, FLESH_WOUND, CRITICAL, PIERCE, HEAT
    """
    SHIELD = "shield"          # Block 1 damage
    ABSORB = "absorb"          # Block 1 damage
    FLESH_WOUND = "wound"      # Take damage (no effect)
    CRITICAL = "critical"      # Take damage + 1 Component Damage
    PIERCE = "pierce"          # Take damage, disable reactive cards
    HEAT = "heat"              # Take damage + 1 Heat

    FACES = [SHIELD, ABSORB, FLESH_WOUND, CRITICAL, PIERCE, HEAT]

    @staticmethod
    def roll() -> str:
        """Roll one defense die, return result symbol"""
        return random.choice(DefenseDie.FACES)

    @staticmethod
    def roll_multiple(count: int) -> Dict[str, int]:
        """
        Roll X defense dice, return count of each symbol
        """
        results = {
            DefenseDie.SHIELD: 0,
            DefenseDie.ABSORB: 0,
            DefenseDie.FLESH_WOUND: 0,
            DefenseDie.CRITICAL: 0,
            DefenseDie.PIERCE: 0,
            DefenseDie.HEAT: 0
        }

        for _ in range(count):
            result = DefenseDie.roll()
            results[result] += 1

        return results

# ============================================================================
# ATTACK RESULT ENUM
# ============================================================================

class AttackResult(Enum):
    """Attack roll result types"""
    CATASTROPHIC_FAILURE = "catastrophic"  # Double JAM (total 2)
    MISS = "miss"                          # Below target number
    HIT = "hit"                            # 5-6 total
    STRONG_HIT = "strong"                  # 7-8 total (+1 damage)
    CRITICAL_HIT = "critical"              # 9 total (+2 damage, bypass 1 Defense die)
    EXECUTION = "execution"                # Double 5 (total 10, destroy component)

# ============================================================================
# LOAD CARD DATABASE
# ============================================================================

def load_card_database():
    """Load complete card database from JSON"""
    with open('../docs/cards/complete-card-data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# ============================================================================
# EQUIPMENT CARD CLASS
# ============================================================================

@dataclass
class EquipmentCard:
    """Represents an equipment card (attack, defense, utility)"""
    name: str
    type: str  # Attack, Reactive, Utility
    cost: int  # SP cost
    effect: str
    damage: int = 0  # Damage dealt (if attack)
    defense: int = 0  # Damage reduced (if reactive)
    range: str = "Melee"
    equipment_name: str = ""  # Parent equipment (DAGGER, SWORD, etc.)
    cannot_miss: bool = False  # Church "cannot miss" mechanic

    def __repr__(self):
        return f"{self.name} ({self.type}, {self.cost} SP, {self.damage} dmg)"

# ============================================================================
# FACTION CARD CLASS
# ============================================================================

@dataclass
class FactionCard:
    """Represents a faction-specific or universal card (gambit, passive, movement, etc.)"""
    name: str
    type: str  # gambit, passive, movement, reactive-defense, utility, etc.
    cost: int  # SP cost
    effect: str
    range: str = "Self"
    damage: int = 0  # Damage dealt (if applicable)
    defense: int = 0  # Damage reduced (if applicable)
    heat: int = 0  # Heat generated (if applicable)
    card_type: str = "faction"  # "faction" or "core" (universal)
    keywords: List[str] = field(default_factory=list)

    def __repr__(self):
        return f"{self.name} ({self.type}, {self.cost} SP)"

# ============================================================================
# CASKET CLASSES
# ============================================================================

class CasketClass(Enum):
    """Casket class definitions with point costs"""
    SCOUT = ("Scout", 6, 22, 1)           # Fast, fragile, cheap (-20% HP: 28→22)
    WARDEN = ("Warden", 5, 28, 2)         # Balanced, standard (-20% HP: 34→28)
    VANGUARD = ("Vanguard", 4, 34, 3)     # Slow, tanky, expensive (-20% HP: 40→34)
    COLOSSUS = ("Colossus", 4, 44, 4)     # Boss unit (-20% HP: 50→44)

    @property
    def sp_max(self):
        return self.value[1]

    @property
    def deck_size(self):
        return self.value[2]

    @property
    def point_cost(self):
        return self.value[3]

# ============================================================================
# CASKET CLASS
# ============================================================================

@dataclass
class Casket:
    """Represents a Casket with equipment-based deck and dice mechanics"""
    name: str
    faction: str
    casket_class: CasketClass = CasketClass.WARDEN

    # Card-based HP system
    deck: Deque = field(default_factory=deque)
    hand: Deque = field(default_factory=deque)
    discard: Deque = field(default_factory=deque)

    # SP and Heat
    sp: int = 5
    sp_max: int = 5
    heat: int = 0

    # Positioning (range in hexes)
    range: int = 2  # Start at 2 hexes away
    moved_this_turn: bool = False

    # Equipment cards in deck
    equipment_cards: List[EquipmentCard] = field(default_factory=list)

    # Faction and universal cards in deck
    faction_cards: List[FactionCard] = field(default_factory=list)
    universal_cards: List[FactionCard] = field(default_factory=list)

    # Dice mechanics tracking
    weapon_jammed: bool = False  # Catastrophic failure state
    component_damage: int = 0    # Critical hits accumulate

    # Faction-specific mechanics
    bleed_stacks: int = 0        # Elves bleed mechanic (max 4)
    forge_tokens: int = 0        # Crucible forge mechanic (max 5)

    def __post_init__(self):
        """Initialize SP based on casket class"""
        self.sp = self.casket_class.sp_max
        self.sp_max = self.casket_class.sp_max

    @property
    def hp(self):
        """HP = cards remaining in deck"""
        return len(self.deck)

    @property
    def is_alive(self):
        """Casket is alive if deck has cards"""
        return len(self.deck) > 0

    def draw_cards(self, count: int):
        """Draw X cards from deck to hand"""
        for _ in range(count):
            if self.deck:
                self.hand.append(self.deck.popleft())
            elif self.discard:
                # Reshuffle discard into deck
                discard_list = list(self.discard)
                random.shuffle(discard_list)
                self.deck = deque(discard_list)
                self.discard.clear()

                # Try again
                if self.deck:
                    self.hand.append(self.deck.popleft())

    def take_damage(self, damage: int, defense_results: Dict[str, int]) -> int:
        """
        Take damage with defense dice mechanics
        Returns actual damage taken (after blocks)
        """
        if damage <= 0:
            return 0

        # Count blocks from defense dice
        blocks = defense_results[DefenseDie.SHIELD] + defense_results[DefenseDie.ABSORB]
        final_damage = max(0, damage - blocks)

        # Apply component damage from CRITICAL symbols
        self.component_damage += defense_results[DefenseDie.CRITICAL]

        # Apply heat from HEAT symbols
        self.heat += defense_results[DefenseDie.HEAT]

        # Discard cards equal to final damage
        for _ in range(final_damage):
            if self.deck:
                self.deck.popleft()  # Damage goes to graveyard (permanent loss)
            elif self.discard:
                # If deck empty, take from discard
                self.discard.popleft()

        return final_damage

# ============================================================================
# DECK BUILDER
# ============================================================================

class DeckBuilder:
    """Builds decks from card database with equipment randomization"""

    def __init__(self, card_db: Dict):
        self.card_db = card_db

    @staticmethod
    def parse_int_value(value, default=0) -> int:
        """Parse integer value from various formats (int, str, null)"""
        if value is None:
            return default
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            # Extract numeric part from strings like "0 SP", "2 Heat", etc.
            import re
            match = re.search(r'-?\d+', value)
            if match:
                return int(match.group())
        return default

    def build_random_deck(self, faction: str, casket_class: CasketClass = CasketClass.WARDEN) -> Casket:
        """
        Build a deck with complete card system:
        - 6 faction cards (randomly chosen from 21 available)
        - 10 universal cards (all included)
        - 2 equipment items (randomly chosen from available pool)
        """
        casket = Casket(
            name=f"{faction.capitalize()} {casket_class.name}",
            faction=faction,
            casket_class=casket_class
        )

        faction_key = faction.lower().replace(' ', '-')

        # ============================================================
        # STEP 1: Load 6 random faction cards from faction's card pool
        # ============================================================
        faction_cards_pool = self.card_db.get(faction_key, [])
        if faction_cards_pool and len(faction_cards_pool) >= 6:
            # Randomly select 6 faction cards (simulates strategic choice)
            selected_faction_cards = random.sample(faction_cards_pool, 6)

            for card_data in selected_faction_cards:
                # Parse heat value (can be "+1", "-1d3", etc.)
                heat_value = 0
                heat_raw = card_data.get('heat', 0)
                if isinstance(heat_raw, str):
                    # Simple numeric heat like "+1" or "-2"
                    heat_clean = heat_raw.replace('+', '')
                    if heat_clean.lstrip('-').isdigit():
                        heat_value = int(heat_clean)
                    # Complex heat like "-1d3" - just use 0 for now
                elif isinstance(heat_raw, int):
                    heat_value = heat_raw

                faction_card = FactionCard(
                    name=card_data['name'],
                    type=card_data.get('type', 'gambit'),
                    cost=self.parse_int_value(card_data.get('cost'), 0),
                    effect=card_data.get('effect', ''),
                    range=card_data.get('range', 'Self'),
                    damage=self.parse_int_value(card_data.get('damage'), 0),
                    defense=self.parse_int_value(card_data.get('defense'), 0),
                    heat=heat_value,
                    card_type='faction',
                    keywords=card_data.get('keywords', [])
                )

                # Add multiple copies if specified
                card_count = card_data.get('cardCount', 1)
                for _ in range(card_count):
                    casket.faction_cards.append(faction_card)
                    casket.deck.append(faction_card)

        # ============================================================
        # STEP 2: Load all 10 universal cards
        # ============================================================
        universal_cards_pool = self.card_db.get('universal', [])
        for card_data in universal_cards_pool:
            # Parse heat value (can be "+1", "-1d3", etc.)
            heat_value = 0
            heat_raw = card_data.get('heat', 0)
            if isinstance(heat_raw, str):
                # Simple numeric heat like "+1" or "-2"
                heat_clean = heat_raw.replace('+', '')
                if heat_clean.lstrip('-').isdigit():
                    heat_value = int(heat_clean)
                # Complex heat like "-1d3" - just use 0 for now
            elif isinstance(heat_raw, int):
                heat_value = heat_raw

            universal_card = FactionCard(
                name=card_data['name'],
                type=card_data.get('type', 'movement'),
                cost=self.parse_int_value(card_data.get('cost'), 0),
                effect=card_data.get('effect', ''),
                range=card_data.get('range', 'Self'),
                damage=self.parse_int_value(card_data.get('damage'), 0),
                defense=self.parse_int_value(card_data.get('defense'), 0),
                heat=heat_value,
                card_type='core',
                keywords=card_data.get('keywords', [])
            )

            # Add multiple copies if specified
            card_count = card_data.get('cardCount', 1)
            for _ in range(card_count):
                casket.universal_cards.append(universal_card)
                casket.deck.append(universal_card)

        # ============================================================
        # STEP 3: Load equipment items (existing logic)
        # ============================================================
        equipment_items = [item for item in self.card_db.get('equipment_items', [])
                          if item.get('faction', '').lower() == faction_key]

        # Randomly select equipment items for this deck
        for item in equipment_items:
            equipment_name = item['name']
            item_cards = item.get('cards', [])

            # Cards are stored inline in equipment_items (not as IDs)
            for card_data in item_cards:
                if not isinstance(card_data, dict):
                    continue

                # Check for "cannot miss" mechanic (Church cards)
                cannot_miss = 'cannot miss' in card_data.get('effect', '').lower()

                # Create equipment card object
                eq_card = EquipmentCard(
                    name=card_data['name'],
                    type=card_data.get('type', 'Attack'),
                    cost=card_data.get('cost', 0),
                    effect=card_data.get('effect', ''),
                    damage=card_data.get('damage', 0),
                    defense=card_data.get('defense', 0),
                    range=card_data.get('range', 'Melee'),
                    equipment_name=equipment_name,
                    cannot_miss=cannot_miss
                )

                # Add card to deck (default 1 copy)
                card_count = card_data.get('cardCount', 1)
                for _ in range(card_count):
                    casket.equipment_cards.append(eq_card)
                    casket.deck.append(eq_card)

        # Add generic HP cards to reach deck size
        target_deck_size = casket_class.deck_size
        while len(casket.deck) < target_deck_size:
            casket.deck.append(f"GenericCard-{len(casket.deck)}")

        # Shuffle deck
        deck_list = list(casket.deck)
        random.shuffle(deck_list)
        casket.deck = deque(deck_list)

        return casket

# ============================================================================
# COMBAT SIMULATOR WITH DICE
# ============================================================================

class DiceCombatSimulator:
    """Simulates combat with full dice mechanics"""

    # PHASE 2: EXTREME faction damage multipliers for balance
    FACTION_DAMAGE_MULTIPLIER = {
        'church': 0.50,           # -50% (100% → ~65%)
        'ossuarium': 0.60,        # -40% (86.7% → ~60%)
        'dwarves': 0.75,          # -25% (75.6% → ~58%)
        'elves': 0.80,            # -20% (71.1% → ~55%)
        'wyrd-conclave': 1.00,    # No change (55.6% = perfect!)
        'vestige-bloodlines': 1.15,  # +15% (44.4% → ~52%)
        'exchange': 1.50,         # +50% (33.3% → ~50%)
        'emergent': 1.70,         # +70% (22.2% → ~48%)
        'crucible': 1.90,         # +90% (11.1% → ~48%)
        'nomads': 2.50,           # +150% (0% → ~45%)
    }

    def __init__(self, casket1: Casket, casket2: Casket, verbose: bool = False):
        self.casket1 = casket1
        self.casket2 = casket2
        self.verbose = verbose
        self.turn = 0

        # Statistics tracking
        self.attack_rolls = []  # Track all attack roll results
        self.defense_rolls = []  # Track all defense roll results

    def log(self, message: str):
        if self.verbose:
            print(message)

    def calculate_to_hit_target(self, attacker: Casket, defender: Casket) -> int:
        """
        Calculate to-hit target number (base 4+ - IMPROVED from 5+)
        Simplified: Only range modifier for simulation
        """
        base_target = 4  # CHANGED: Was 5, now 4 (+17% hit rate)

        # Range modifier (0-3 hexes = short, 4+ = medium)
        if attacker.range <= 3:
            range_mod = 0  # Short range
        elif attacker.range <= 6:
            range_mod = 1  # Medium range
        else:
            range_mod = 2  # Long range

        return base_target + range_mod

    def roll_attack(self, attacker: Casket, attack_card: EquipmentCard, target_number: int) -> Tuple[AttackResult, int]:
        """
        Roll attack dice and determine result
        Returns (result_type, bonus_damage)
        """
        # PHASE 1 FIX: Removed "cannot miss" auto-hit (was too powerful)

        # Roll 2 attack dice
        die1, die2, total = AttackDie.roll_2d6()
        self.log(f"  Attack roll: [{die1}] + [{die2}] = {total} (need {target_number}+)")

        # Track roll
        self.attack_rolls.append(total)

        # Check for special results
        if die1 == 0 and die2 == 0:
            # Double JAM = Catastrophic Failure
            self.log(f"  💥 CATASTROPHIC FAILURE (double JAM)!")
            return (AttackResult.CATASTROPHIC_FAILURE, 0)

        if die1 == 5 and die2 == 5:
            # Double 5 = Execution
            self.log(f"  ⚔️ EXECUTION (double DEATH BLOW)!")
            return (AttackResult.EXECUTION, 0)

        # Check if hit
        if total < target_number:
            self.log(f"  ❌ MISS (rolled {total}, needed {target_number}+)")
            return (AttackResult.MISS, 0)

        # Determine hit quality
        if total == 9:
            self.log(f"  💀 CRITICAL HIT (+2 damage, bypass 1 Defense die)")
            return (AttackResult.CRITICAL_HIT, 2)
        elif total >= 7:
            self.log(f"  ⚡ STRONG HIT (+1 damage)")
            return (AttackResult.STRONG_HIT, 1)
        else:
            self.log(f"  ✓ HIT")
            return (AttackResult.HIT, 0)

    def roll_defense(self, damage: int, critical_hit: bool = False) -> Dict[str, int]:
        """
        Roll defense dice (1 per damage point)
        Critical hits bypass 1 defense die
        """
        dice_count = max(1, damage - (1 if critical_hit else 0))
        results = DefenseDie.roll_multiple(dice_count)

        # Log defense results
        blocks = results[DefenseDie.SHIELD] + results[DefenseDie.ABSORB]
        crits = results[DefenseDie.CRITICAL]
        heat = results[DefenseDie.HEAT]

        self.log(f"  Defense: {dice_count} dice → {blocks} blocks, {crits} crits, {heat} heat")

        return results

    def run_combat(self, max_turns: int = 50) -> Dict:
        """Run combat simulation with dice mechanics"""
        self.log(f"\n=== COMBAT START: {self.casket1.name} vs {self.casket2.name} ===")

        while self.turn < max_turns and self.casket1.is_alive and self.casket2.is_alive:
            self.turn += 1
            self.log(f"\n--- Turn {self.turn} ---")

            # Player 1 turn
            self.execute_turn(self.casket1, self.casket2)
            if not self.casket2.is_alive:
                break

            # Player 2 turn
            self.execute_turn(self.casket2, self.casket1)
            if not self.casket1.is_alive:
                break

        # Determine winner
        if not self.casket1.is_alive:
            winner = self.casket2.name
        elif not self.casket2.is_alive:
            winner = self.casket1.name
        else:
            # Timeout - HP tiebreaker
            winner = self.casket1.name if self.casket1.hp >= self.casket2.hp else self.casket2.name

        self.log(f"\n=== COMBAT END: {winner} wins! ===")

        return {
            'winner': winner,
            'turns': self.turn,
            'casket1_hp': self.casket1.hp,
            'casket2_hp': self.casket2.hp,
            'attack_rolls': self.attack_rolls.copy()
        }

    def execute_turn(self, attacker: Casket, defender: Casket):
        """Execute one player's turn with dice mechanics"""
        # Regenerate 2 SP per turn (banking mechanic)
        attacker.sp = min(attacker.sp + 2, attacker.sp_max)
        attacker.moved_this_turn = False

        # Apply bleed damage at turn start (Elves mechanic)
        if attacker.bleed_stacks > 0:
            bleed_damage = attacker.bleed_stacks
            # Apply bleed damage (no defense dice for bleed - it's unavoidable)
            for _ in range(bleed_damage):
                if attacker.deck:
                    attacker.deck.popleft()
            self.log(f"{attacker.name} takes {bleed_damage} bleed damage ({attacker.bleed_stacks} stacks)")

        # Clear weapon jam status (lasts 1 turn)
        if attacker.weapon_jammed:
            attacker.weapon_jammed = False
            self.log(f"{attacker.name} clears weapon jam")

        # Draw cards
        attacker.draw_cards(3)

        # Movement logic (simplified - move if needed to attack)
        if attacker.range > 0:
            melee_cards = [c for c in attacker.hand if isinstance(c, EquipmentCard)
                          and c.type == "Attack" and "Melee" in c.range]
            ranged_cards = [c for c in attacker.hand if isinstance(c, EquipmentCard)
                           and c.type == "Attack" and "Ranged" in c.range]

            # Move if we have ONLY melee cards, or if we have melee + spare SP
            should_move = (melee_cards and not ranged_cards) or (melee_cards and attacker.sp >= 4)

            if should_move:
                move_cost = min(attacker.range, max(1, attacker.sp - 2))
                if move_cost > 0:
                    attacker.sp -= move_cost
                    attacker.range -= move_cost
                    attacker.moved_this_turn = True
                    self.log(f"{attacker.name} moves {move_cost} hexes (→ {attacker.range} hexes, {attacker.sp} SP)")

        # Select best attack card
        attack_card = self.select_attack_card(attacker)

        if attack_card:
            # Check range compatibility (ranged cards can attack from any range, melee needs range 0)
            can_attack = ("Ranged" in attack_card.range or attacker.range == 0)

            if can_attack:
                # Calculate to-hit target
                target_number = self.calculate_to_hit_target(attacker, defender)

                # Pay SP cost
                attacker.sp -= attack_card.cost

                # PHASE 1 FIX: Apply "on attack" effects BEFORE rolling dice
                effect_lower = attack_card.effect.lower()

                # Elves: Apply bleed on ATTACK (not on HIT) - check for "bleed" in effect
                if 'bleed' in effect_lower:
                    # Extract bleed amount (e.g., "Bleed 1" or "Bleed 2")
                    bleed_amount = 1  # Default
                    if 'bleed 2' in effect_lower:
                        bleed_amount = 2
                    defender.bleed_stacks = min(defender.bleed_stacks + bleed_amount, 4)  # Cap at 4
                    self.log(f"  → Applied {bleed_amount} Bleed to {defender.name} ({defender.bleed_stacks}/4 stacks)")

                # Crucible: Gain Forge on ATTACK (not on HIT) - check for "forge" generation
                if 'forge' in effect_lower and 'gain' in effect_lower:
                    attacker.forge_tokens = min(attacker.forge_tokens + 1, 5)  # Cap at 5
                    self.log(f"  → Gained 1 Forge ({attacker.forge_tokens}/5 tokens)")

                # Roll attack
                attack_result, bonus_damage = self.roll_attack(attacker, attack_card, target_number)

                # Handle attack results
                if attack_result == AttackResult.CATASTROPHIC_FAILURE:
                    # Weapon jams
                    attacker.weapon_jammed = True
                    attacker.heat += 2
                    self.log(f"{attacker.name} weapon JAMS! (+2 Heat, next attack -2 damage)")

                elif attack_result == AttackResult.EXECUTION:
                    # Auto-destroy component, bypass all defense
                    defender.component_damage = 999  # Mark as destroyed
                    damage = attack_card.damage + bonus_damage
                    defender.take_damage(damage, {symbol: 0 for symbol in DefenseDie.FACES})
                    self.log(f"{attacker.name} EXECUTES with {attack_card.name}! Component destroyed, {damage} damage ({defender.name}: {defender.hp} HP)")

                elif attack_result != AttackResult.MISS:
                    # Hit - calculate damage
                    base_damage = attack_card.damage

                    # PHASE 2: Apply faction damage multiplier
                    faction_key = attacker.faction.lower()
                    multiplier = self.FACTION_DAMAGE_MULTIPLIER.get(faction_key, 1.0)
                    scaled_damage = int(base_damage * multiplier + 0.5)  # Round to nearest
                    total_damage = scaled_damage + bonus_damage

                    if multiplier != 1.0:
                        self.log(f"  [BALANCE] {base_damage} base × {multiplier:.2f} = {scaled_damage} damage")

                    # Apply weapon jam penalty
                    if attacker.weapon_jammed:
                        total_damage = max(1, total_damage - 2)
                        self.log(f"  [JAMMED] Damage reduced by 2")

                    # Roll defense dice
                    is_critical = (attack_result == AttackResult.CRITICAL_HIT)
                    defense_results = self.roll_defense(total_damage, is_critical)

                    # Apply damage
                    actual_damage = defender.take_damage(total_damage, defense_results)
                    self.log(f"{attacker.name} attacks with {attack_card.name} for {actual_damage}/{total_damage} damage ({defender.name}: {defender.hp} HP)")

                else:
                    # Miss - no effect
                    self.log(f"{attacker.name} misses with {attack_card.name}")

            else:
                self.log(f"{attacker.name} out of range, banking {attacker.sp} SP")
        else:
            self.log(f"{attacker.name} has no valid attacks, banking {attacker.sp} SP")

    def select_attack_card(self, casket: Casket):
        """
        Select best single attack card from hand (highest damage, affordable)
        Supports both EquipmentCard (type="Attack") and FactionCard (type="attack" or has damage)
        """
        attack_cards = []

        for c in casket.hand:
            # Check if it's an EquipmentCard with type "Attack"
            if isinstance(c, EquipmentCard) and c.type == "Attack":
                attack_cards.append(c)
            # Check if it's a FactionCard with type "attack" or has damage > 0
            elif isinstance(c, FactionCard) and (c.type.lower() == "attack" or c.damage > 0):
                attack_cards.append(c)

        if not attack_cards:
            return None

        # Select highest damage attack that we can afford
        valid_attacks = [c for c in attack_cards if c.cost <= casket.sp]
        if not valid_attacks:
            return None

        return max(valid_attacks, key=lambda c: c.damage)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("PENANCE DICE-BASED COMBAT SIMULATOR")
    print("=" * 80)

    # Load card database
    card_db = load_card_database()
    builder = DeckBuilder(card_db)

    # Build two test caskets
    church_casket = builder.build_random_deck("church", CasketClass.WARDEN)
    wyrd_casket = builder.build_random_deck("wyrd-conclave", CasketClass.WARDEN)

    # Run combat with verbose output
    simulator = DiceCombatSimulator(church_casket, wyrd_casket, verbose=True)
    result = simulator.run_combat()

    print("\n" + "=" * 80)
    print("COMBAT RESULT")
    print("=" * 80)
    print(f"Winner: {result['winner']}")
    print(f"Turns: {result['turns']}")
    print(f"{church_casket.name}: {result['casket1_hp']} HP")
    print(f"{wyrd_casket.name}: {result['casket2_hp']} HP")
    print(f"\nAttack rolls: {result['attack_rolls']}")
