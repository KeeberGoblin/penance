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
    SCOUT = ("Scout", 6, 22, 2)           # Fast, fragile, cheap (-20% HP: 28→22)
    WARDEN = ("Warden", 5, 28, 3)         # Balanced, standard (-20% HP: 34→28)
    VANGUARD = ("Vanguard", 4, 34, 4)     # Slow, tanky, expensive (-20% HP: 40→34)
    COLOSSUS = ("Colossus", 4, 44, 5)     # Boss unit (-20% HP: 50→44)

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
    discard: Deque = field(default_factory=deque)  # V5.20: Played cards (can reshuffle)
    damage_pile: Deque = field(default_factory=deque)  # V5.21: Destroyed cards (permanent loss)

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
    biomass_tokens: int = 0      # Bloodlines biomass mechanic (max 10)
    mutation_strain: int = 0     # V5.30: Bloodlines mutation strain tracker (max 29, 30+ = transformation loss)
    credit_tokens: int = 0       # Exchange credits mechanic (max 10)
    credit_attack_count: int = 0  # V5.17: Track attacks for credit generation (1 per 2 attacks)
    rune_counters: int = 0       # Dwarves rune counters (max 3)
    discards_this_turn: int = 0  # Church self-harm tracking
    taint_tokens: int = 0        # V5.18: Ossuarium taint from salvaging (max 10)
    soul_shards: int = 0         # V6.0: Ossuarium Soul Shards from kills (no cap)

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

    def recover_cards(self, count: int, source: str = "lifesteal") -> int:
        """
        Recover cards from discard pile to deck
        V5.22: Taint generation moved to lifesteal code (1.5x multiplier)
        Returns actual cards recovered
        """
        cards_recovered = 0
        for _ in range(count):
            if self.discard:
                card = self.discard.pop()
                self.deck.append(card)
                cards_recovered += 1

        # V5.22: Taint generation now handled in lifesteal code (not here)

        return cards_recovered

    def take_damage(self, damage: int, defense_results: Dict[str, int]) -> int:
        """
        Take damage with defense dice mechanics
        Returns actual damage taken (after blocks)
        """
        if damage <= 0:
            return 0

        # Count blocks from defense dice
        blocks = defense_results[DefenseDie.SHIELD] + defense_results[DefenseDie.ABSORB]

        # Dwarves: Rune Counters reduce damage
        # V5.25: Buffed from 3 → 4 damage per counter (Dwarves still struggling at 28.9% WR)
        if self.rune_counters > 0:
            remaining_damage = damage - blocks
            if remaining_damage > 0:
                # Each rune counter reduces 4 damage (V5.25 buff)
                rune_reduction = min(self.rune_counters * 4, remaining_damage)
                blocks += rune_reduction
                # Consume counters based on actual reduction (1 counter per 4 damage blocked)
                counters_consumed = min(self.rune_counters, (rune_reduction + 3) // 4)
                self.rune_counters -= counters_consumed

        final_damage = max(0, damage - blocks)

        # Apply component damage from CRITICAL symbols
        self.component_damage += defense_results[DefenseDie.CRITICAL]

        # Apply heat from HEAT symbols
        self.heat += defense_results[DefenseDie.HEAT]

        # V5.21: Move damaged cards to damage_pile (permanent loss)
        for _ in range(final_damage):
            if self.deck:
                card = self.deck.popleft()
                self.damage_pile.append(card)  # Destroyed cards go to damage_pile
            elif self.discard:
                # If deck empty, take from discard and destroy
                card = self.discard.popleft()
                self.damage_pile.append(card)

        return final_damage

    def get_taint_damage_penalty(self) -> int:
        """
        V6.0: Calculate damage penalty from Taint corruption
        Returns damage reduction amount based on current taint_tokens
        """
        if self.taint_tokens >= 9:
            return 4  # Catastrophic corruption
        elif self.taint_tokens >= 7:
            return 3  # Critical corruption
        elif self.taint_tokens >= 5:
            return 2  # Major corruption
        elif self.taint_tokens >= 3:
            return 1  # Minor corruption
        else:
            return 0  # No penalty (0-2 Taint)

    def get_taint_sp_penalty(self) -> int:
        """
        V6.0: Calculate SP cost increase from extreme Taint corruption
        Returns SP cost increase at catastrophic Taint levels
        """
        if self.taint_tokens >= 9:
            return 1  # All card costs +1 SP
        else:
            return 0

# ============================================================================
# SUPPORT UNIT (SIMPLIFIED FOR SIMULATION)
# ============================================================================

@dataclass
class SupportUnit:
    """Simplified support unit for point-based armies"""
    name: str
    faction: str
    hp: int = 10  # Support units have fixed HP
    point_cost: float = 1.0  # 1 point each

    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount: int):
        """Support units take flat damage (no deck system)"""
        self.hp = max(0, self.hp - amount)

# ============================================================================
# ARMY CLASS
# ============================================================================

@dataclass
class Army:
    """Represents an army of multiple Caskets and Support Units"""
    faction: str
    caskets: List[Casket] = field(default_factory=list)
    support_units: List[SupportUnit] = field(default_factory=list)

    @property
    def total_points(self) -> float:
        """Calculate total point cost of army"""
        casket_points = sum(c.casket_class.point_cost for c in self.caskets)
        support_points = sum(s.point_cost for s in self.support_units)
        return casket_points + support_points

    @property
    def is_defeated(self) -> bool:
        """Army is defeated if all units are dead"""
        caskets_alive = any(c.is_alive for c in self.caskets)
        supports_alive = any(s.is_alive for s in self.support_units)
        return not (caskets_alive or supports_alive)

    @property
    def active_units(self) -> List:
        """Get all alive units"""
        alive = []
        alive.extend([c for c in self.caskets if c.is_alive])
        alive.extend([s for s in self.support_units if s.is_alive])
        return alive

# ============================================================================
# DIFFICULTY PRESETS
# ============================================================================

class Difficulty(Enum):
    """Difficulty levels with point budgets"""
    EASY = ("Easy", 4)          # 2 Scouts OR 1 Warden + 1 Support OR 4 Supports (no Colossus)
    MEDIUM = ("Medium", 6)       # 2 Wardens OR 1 Warden + Scout + Support OR 3 Scouts
    HARD = ("Hard", 8)           # 2 Vanguards OR 4 Scouts OR 1 Colossus + Warden
    BOSS = ("Boss", 12)          # 2 Colossi + Warden OR 4 Wardens OR 6 Scouts
    CAMPAIGN = ("Campaign", 10)  # 2 Colossus OR 1 Colossus + Vanguard + Support OR 5 Scouts

    @property
    def point_budget(self):
        return self.value[1]

# ============================================================================
# POINT-BASED ARMY BUILDER
# ============================================================================

class PointBudgetArmyBuilder:
    """Builds armies within point budget with random composition"""

    def __init__(self, deck_builder: 'DeckBuilder'):
        self.deck_builder = deck_builder

    def build_random_army(
        self,
        faction: str,
        point_budget: float,
        allow_supports: bool = True,
        support_ratio: float = 0.3  # Max 30% of points on supports
    ) -> Army:
        """
        Build random army within point budget

        Args:
            faction: Faction name
            point_budget: Total points to spend
            allow_supports: Include support units
            support_ratio: Max % of budget for supports (0.0-1.0)

        Returns:
            Army with random composition
        """
        army = Army(faction=faction)
        remaining_points = point_budget

        # Determine support budget
        support_budget = 0
        if allow_supports and support_ratio > 0:
            support_budget = point_budget * support_ratio
            # Spend some points on supports first (0-100% of support budget)
            support_spend = random.uniform(0, support_budget)
            num_supports = int(support_spend / 1.0)  # 1 point per support

            for i in range(num_supports):
                support = SupportUnit(
                    name=f"{faction.capitalize()} Support {i+1}",
                    faction=faction
                )
                army.support_units.append(support)
                remaining_points -= 1.0

        # Spend remaining points on Caskets
        casket_classes = [
            CasketClass.COLOSSUS,   # 5 points
            CasketClass.VANGUARD,   # 4 points
            CasketClass.WARDEN,     # 3 points
            CasketClass.SCOUT       # 2 points
        ]

        while remaining_points >= 2:
            # Try to buy affordable caskets
            affordable = [c for c in casket_classes if c.point_cost <= remaining_points]

            if not affordable:
                break

            # Randomly choose from affordable options
            chosen_class = random.choice(affordable)

            # Build casket with complete deck
            casket = self.deck_builder.build_random_deck(faction, chosen_class)
            army.caskets.append(casket)
            remaining_points -= chosen_class.point_cost

        return army

    def build_specific_army(
        self,
        faction: str,
        composition: List[CasketClass],
        num_supports: int = 0
    ) -> Army:
        """Build army with specific composition"""
        army = Army(faction=faction)

        # Add Caskets
        for i, casket_class in enumerate(composition):
            casket = self.deck_builder.build_random_deck(faction, casket_class)
            army.caskets.append(casket)

        # Add Support Units
        for i in range(num_supports):
            support = SupportUnit(
                name=f"{faction.capitalize()} Support {i+1}",
                faction=faction
            )
            army.support_units.append(support)

        return army

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

    # v5.15: REMOVED artificial damage multipliers - testing real mechanics
    FACTION_DAMAGE_MULTIPLIER = {
        'church': 1.00,
        'ossuarium': 1.00,
        'dwarves': 1.00,
        'elves': 1.00,
        'wyrd-conclave': 1.00,
        'vestige-bloodlines': 1.00,
        'exchange': 1.00,
        'emergent': 1.00,
        'crucible': 1.00,
        'nomads': 1.00,
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

    def parse_resource_effect(self, effect: str, resource_type: str) -> Dict:
        """
        Parse resource-related effects from card text
        Returns dict with 'generate', 'spend', and 'bonus' values
        """
        import re
        effect_lower = effect.lower()
        result = {'generate': 0, 'spend': 0, 'bonus': 0}

        # Check for generation (e.g., "Gain 1 Forge", "Generate 2 Credits")
        gen_patterns = [
            rf'gain (\d+) {resource_type}',
            rf'generate (\d+) {resource_type}',
            rf'\+(\d+) {resource_type}'
        ]
        for pattern in gen_patterns:
            match = re.search(pattern, effect_lower)
            if match:
                result['generate'] = int(match.group(1))
                break

        # Check for spending (e.g., "Spend 2 Forge", "Cost: 3 Biomass")
        spend_patterns = [
            rf'spend (\d+) {resource_type}',
            rf'cost: (\d+) {resource_type}',
            rf'pay (\d+) {resource_type}'
        ]
        for pattern in spend_patterns:
            match = re.search(pattern, effect_lower)
            if match:
                result['spend'] = int(match.group(1))
                break

        # Check for bonus effects when spending
        if result['spend'] > 0:
            # Look for damage bonus (e.g., "+2 damage", "7 damage")
            dmg_match = re.search(r'(\+?\d+) damage', effect_lower)
            if dmg_match:
                result['bonus'] = int(dmg_match.group(1).replace('+', ''))

        return result

    def calculate_to_hit_target(self, attacker: Casket, defender: Casket) -> int:
        """
        Calculate to-hit target number (base 5+ - ORIGINAL DESIGN)
        V5.26: REVERTED from 4 to 5 (original 58% hit rate, not 72%)
        Simplified: Only range modifier for simulation
        """
        base_target = 5  # V5.26: REVERTED to original (agents found base 4 was causing 24% power inflation)

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
        attacker.discards_this_turn = 0  # Reset discard counter

        # Apply bleed damage at turn start (Elves mechanic)
        if attacker.bleed_stacks > 0:
            bleed_damage = attacker.bleed_stacks
            # V5.21: Apply bleed damage (no defense dice for bleed - it's unavoidable)
            for _ in range(bleed_damage):
                if attacker.deck:
                    card = attacker.deck.popleft()
                    attacker.damage_pile.append(card)  # Bleed destroys cards permanently
            self.log(f"{attacker.name} takes {bleed_damage} bleed damage ({attacker.bleed_stacks} stacks)")

        # V6.0: Apply Taint penalties at turn start (Soul Shard system - BRUTAL penalties)
        # Taint now ONLY gained from spending Soul Shards on salvage actions
        # No longer destroys cards - instead reduces attack damage and increases heat
        if attacker.taint_tokens > 0:
            heat_penalty = 0

            # Brutal Taint penalties (permanent corruption from necro-tech)
            if attacker.taint_tokens >= 9:
                heat_penalty = 2
                # Damage penalty applied during attack (see line ~1048)
                # SP cost penalty handled during card play
                self.log(f"{attacker.name} suffers CATASTROPHIC Taint corruption: +{heat_penalty} Heat, -4 damage, +1 SP costs ({attacker.taint_tokens}/10 Taint)")
            elif attacker.taint_tokens >= 7:
                heat_penalty = 2
                self.log(f"{attacker.name} suffers CRITICAL Taint corruption: +{heat_penalty} Heat, -3 damage ({attacker.taint_tokens}/10 Taint)")
            elif attacker.taint_tokens >= 5:
                heat_penalty = 2
                self.log(f"{attacker.name} suffers MAJOR Taint corruption: +{heat_penalty} Heat, -2 damage ({attacker.taint_tokens}/10 Taint)")
            elif attacker.taint_tokens >= 3:
                heat_penalty = 1
                self.log(f"{attacker.name} suffers MINOR Taint corruption: +{heat_penalty} Heat, -1 damage ({attacker.taint_tokens}/10 Taint)")
            # 0-2 Taint: No penalty

            if heat_penalty > 0:
                attacker.heat += heat_penalty

        # Clear weapon jam status (lasts 1 turn)
        if attacker.weapon_jammed:
            attacker.weapon_jammed = False
            self.log(f"{attacker.name} clears weapon jam")

        # Draw cards
        attacker.draw_cards(3)

        # V6.0: Ossuarium - Try to use Salvage Protocol if HP is low
        if attacker.faction.lower() == 'ossuarium':
            self.try_salvage_protocol(attacker)

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

                # Pay SP cost (V6.0: Apply Taint SP penalty for Ossuarium)
                sp_cost = attack_card.cost
                if attacker.faction.lower() == 'ossuarium':
                    sp_cost += attacker.get_taint_sp_penalty()
                attacker.sp -= sp_cost

                # Apply card effects BEFORE rolling dice
                effect_lower = attack_card.effect.lower()
                card_bonus_damage = 0

                # === RESOURCE GENERATION (on attack) ===

                # Elves: Apply bleed on ATTACK
                if 'bleed' in effect_lower:
                    import re
                    bleed_match = re.search(r'bleed (\d+)', effect_lower)
                    bleed_amount = int(bleed_match.group(1)) if bleed_match else 1
                    defender.bleed_stacks = min(defender.bleed_stacks + bleed_amount, 4)
                    self.log(f"  → Applied {bleed_amount} Bleed to {defender.name} ({defender.bleed_stacks}/4 stacks)")

                # Crucible: Gain Forge tokens
                forge_effect = self.parse_resource_effect(attack_card.effect, 'forge')
                if forge_effect['generate'] > 0:
                    attacker.forge_tokens = min(attacker.forge_tokens + forge_effect['generate'], 5)
                    self.log(f"  → Gained {forge_effect['generate']} Forge ({attacker.forge_tokens}/5 tokens)")

                # Exchange: Gain Credits
                # V5.17: Nerfed to gain 1 Credit per 2 attacks (was every attack at 78% WR)
                credit_effect = self.parse_resource_effect(attack_card.effect, 'credit')
                if credit_effect['generate'] > 0:
                    attacker.credit_attack_count += 1
                    if attacker.credit_attack_count >= 2:
                        attacker.credit_tokens = min(attacker.credit_tokens + credit_effect['generate'], 10)
                        attacker.credit_attack_count = 0  # Reset counter
                        self.log(f"  → Gained {credit_effect['generate']} Credits (every 2 attacks, {attacker.credit_tokens}/10 tokens)")

                # Dwarves: Gain Rune Counters
                rune_effect = self.parse_resource_effect(attack_card.effect, 'rune')
                if rune_effect['generate'] > 0:
                    attacker.rune_counters = min(attacker.rune_counters + rune_effect['generate'], 3)
                    self.log(f"  → Gained {rune_effect['generate']} Rune Counters ({attacker.rune_counters}/3 counters)")

                # === RESOURCE SPENDING ===

                # Crucible: Spend Forge tokens for bonuses
                if forge_effect['spend'] > 0 and attacker.forge_tokens >= forge_effect['spend']:
                    attacker.forge_tokens -= forge_effect['spend']
                    if forge_effect['bonus'] > 0:
                        card_bonus_damage += forge_effect['bonus']
                    self.log(f"  → Spent {forge_effect['spend']} Forge (+{forge_effect['bonus']} damage, {attacker.forge_tokens} remaining)")

                # Exchange: Spend Credits for bonuses
                if credit_effect['spend'] > 0 and attacker.credit_tokens >= credit_effect['spend']:
                    attacker.credit_tokens -= credit_effect['spend']
                    if credit_effect['bonus'] > 0:
                        card_bonus_damage += credit_effect['bonus']
                    self.log(f"  → Spent {credit_effect['spend']} Credits (+{credit_effect['bonus']} damage, {attacker.credit_tokens} remaining)")

                # Bloodlines: Spend Biomass for bonuses
                # V5.30: Added Mutation Strain cap (30+ = transformation loss)
                biomass_effect = self.parse_resource_effect(attack_card.effect, 'biomass')
                if biomass_effect['spend'] > 0:
                    # Check Mutation Strain cap (30+ = instant loss)
                    if attacker.mutation_strain >= 30:
                        self.log(f"  → {attacker.name} TRANSFORMED! Mutation Strain reached 30+ (instant loss)")
                        attacker.deck.clear()  # Instant death by deck depletion
                        return

                    # V5.30: Use normal cost, but add to Mutation Strain
                    actual_cost = biomass_effect['spend']
                    if attacker.biomass_tokens >= actual_cost:
                        attacker.biomass_tokens -= actual_cost
                        attacker.mutation_strain += actual_cost  # V5.30: Track cumulative strain
                        if biomass_effect['bonus'] > 0:
                            card_bonus_damage += biomass_effect['bonus']
                        self.log(f"  → Spent {actual_cost} Biomass (+{biomass_effect['bonus']} damage, {attacker.biomass_tokens} remaining, Strain: {attacker.mutation_strain}/29)")

                        # V5.30: Apply Mutation Strain penalties
                        if attacker.mutation_strain >= 20:
                            self.log(f"  → FERAL (Strain 20-29): Must attack each turn, no Reactive defenses")
                        elif attacker.mutation_strain >= 10:
                            self.log(f"  → UNSTABLE (Strain 10-19): +1 Heat on all attacks")
                            # Heat penalty applied during attack resolution

                # V5.19: Removed Taint spending bonus - penalties only now

                # Church: Discard effects
                # V5.27: 5x discard bonuses (was 3x, still too weak at 22.2% WR in v5.26)
                if 'discard' in effect_lower:
                    import re
                    discard_match = re.search(r'discard (\d+)', effect_lower)
                    if discard_match:
                        discard_count = int(discard_match.group(1))
                        for _ in range(discard_count):
                            if attacker.deck:
                                card = attacker.deck.popleft()
                                attacker.damage_pile.append(card)  # V5.22: Discard goes to damage_pile
                                attacker.discards_this_turn += 1
                        # Blood Offering: Discard 1 → +2 damage (now 5x = +10)
                        damage_bonus_match = re.search(r'\+(\d+) damage', effect_lower)
                        if damage_bonus_match:
                            discard_bonus = int(damage_bonus_match.group(1)) * 5  # V5.27: 5x multiplier
                            card_bonus_damage += discard_bonus
                            self.log(f"  → Discarded {discard_count} cards for +{discard_bonus} damage (5x bonus)")

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
                    total_damage = scaled_damage + bonus_damage + card_bonus_damage

                    if multiplier != 1.0:
                        self.log(f"  [BALANCE] {base_damage} base × {multiplier:.2f} = {scaled_damage} damage")

                    # Apply weapon jam penalty
                    if attacker.weapon_jammed:
                        total_damage = max(1, total_damage - 2)
                        self.log(f"  [JAMMED] Damage reduced by 2")

                    # V6.0: Apply Taint damage penalty (Ossuarium only)
                    if attacker.faction.lower() == 'ossuarium':
                        taint_penalty = attacker.get_taint_damage_penalty()
                        if taint_penalty > 0:
                            total_damage = max(1, total_damage - taint_penalty)
                            self.log(f"  [TAINT] Damage reduced by {taint_penalty} (corruption)")

                    # Roll defense dice
                    is_critical = (attack_result == AttackResult.CRITICAL_HIT)
                    defense_results = self.roll_defense(total_damage, is_critical)

                    # Apply damage
                    actual_damage = defender.take_damage(total_damage, defense_results)
                    self.log(f"{attacker.name} attacks with {attack_card.name} for {actual_damage}/{total_damage} damage ({defender.name}: {defender.hp} HP)")

                    # V5.30: Mutation Strain heat penalty (Unstable status)
                    if attacker.faction.lower() == 'vestige-bloodlines' and attacker.mutation_strain >= 10:
                        attacker.heat += 1
                        self.log(f"  → Unstable Mutations: +1 Heat (Strain: {attacker.mutation_strain}/29)")

                    # V6.0: Ossuarium - Gain Soul Shards on kill (Soul Shard system)
                    # Taint is now ONLY gained from spending Shards (salvage actions)
                    if not defender.is_alive and attacker.faction.lower() == 'ossuarium':
                        shards_gain = 3  # Base reward for kill
                        attacker.soul_shards += shards_gain
                        self.log(f"  → {attacker.name} salvaged {shards_gain} Soul Shards from kill ({attacker.soul_shards} total)")

                    # Bloodlines: Gain Biomass on kill (Vestige Heritage mechanic)
                    # V5.17: Nerfed from 2 → 1 per kill (was too strong at 82% WR)
                    if not defender.is_alive and attacker.faction.lower() == 'vestige-bloodlines':
                        biomass_gain = 1  # V5.17: Reduced from 2
                        attacker.biomass_tokens = min(attacker.biomass_tokens + biomass_gain, 10)
                        self.log(f"  → {attacker.name} gained {biomass_gain} Biomass from kill ({attacker.biomass_tokens}/10 tokens)")

                else:
                    # Miss - no effect
                    self.log(f"{attacker.name} misses with {attack_card.name}")

                # V5.20: Move played card to discard pile (card cycling)
                if attack_card in attacker.hand:
                    attacker.hand.remove(attack_card)
                    attacker.discard.append(attack_card)

            else:
                self.log(f"{attacker.name} out of range, banking {attacker.sp} SP")
        else:
            self.log(f"{attacker.name} has no valid attacks, banking {attacker.sp} SP")

        # V5.20: End of turn - discard entire hand (card cycling)
        while attacker.hand:
            card = attacker.hand.popleft()
            attacker.discard.append(card)

        # V5.18: Taint natural decay at end of turn (Ossuarium mechanic)
        if attacker.taint_tokens > 0:
            attacker.taint_tokens = max(0, attacker.taint_tokens - 1)
            if attacker.taint_tokens > 0:
                self.log(f"{attacker.name} Taint decays to {attacker.taint_tokens}/10")

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

    def try_salvage_protocol(self, casket: Casket) -> bool:
        """
        V6.0: Try to play Salvage Protocol or Emergency Rebuild cards (Ossuarium only)
        Returns True if a salvage card was played
        """
        if casket.faction.lower() != 'ossuarium':
            return False

        # Look for salvage cards in hand
        salvage_cards = []
        for c in casket.hand:
            if hasattr(c, 'name') and hasattr(c, 'effect'):
                effect_lower = c.effect.lower()
                # Detect salvage cards by effect text
                if 'spend' in effect_lower and 'soul shard' in effect_lower and 'recover' in effect_lower:
                    salvage_cards.append(c)

        if not salvage_cards:
            return False

        # Decision logic: Use salvage if HP is low (< 50%) and we have enough Shards
        hp_threshold = 15  # Use salvage if HP < 15 cards
        if casket.hp >= hp_threshold:
            return False  # HP is fine, don't salvage yet

        # Find best salvage card we can afford (SP and Soul Shards)
        for salvage_card in salvage_cards:
            # Parse effect to get shard cost and card recovery
            import re
            effect_lower = salvage_card.effect.lower()

            shard_match = re.search(r'spend (\d+) soul shard', effect_lower)
            recover_match = re.search(r'recover (\d+) card', effect_lower)
            taint_match = re.search(r'gain (\d+) taint', effect_lower)

            if not (shard_match and recover_match and taint_match):
                continue

            shard_cost = int(shard_match.group(1))
            cards_to_recover = int(recover_match.group(1))
            taint_gain = int(taint_match.group(1))

            # Check if we can afford it
            sp_cost = salvage_card.cost
            if casket.faction.lower() == 'ossuarium':
                sp_cost += casket.get_taint_sp_penalty()

            if casket.sp >= sp_cost and casket.soul_shards >= shard_cost:
                # Play the salvage card
                casket.sp -= sp_cost
                casket.soul_shards -= shard_cost
                cards_recovered = casket.recover_cards(cards_to_recover, source="salvage")
                casket.taint_tokens = min(casket.taint_tokens + taint_gain, 10)
                casket.hand.remove(salvage_card)
                casket.discard.append(salvage_card)

                self.log(f"{casket.name} plays {salvage_card.name}: Spent {shard_cost} Shards, recovered {cards_recovered} cards, gained {taint_gain} Taint ({casket.taint_tokens}/10)")
                self.log(f"  → Soul Shards: {casket.soul_shards}, HP: {casket.hp} cards")
                return True

        return False

# ============================================================================
# MULTI-UNIT COMBAT SIMULATOR
# ============================================================================

class MultiUnitCombatSimulator:
    """Simulates combat between two armies with focus fire targeting"""

    def __init__(self, army1: Army, army2: Army, verbose: bool = False):
        self.army1 = army1
        self.army2 = army2
        self.verbose = verbose
        self.turn = 0

    def log(self, message: str):
        """Print message if verbose mode enabled"""
        if self.verbose:
            print(message)

    def get_strongest_target(self, army: Army):
        """Get strongest target (prioritize Caskets, then Supports, prefer highest HP)"""
        # Prioritize Caskets over Supports
        alive_caskets = [c for c in army.caskets if c.is_alive]
        if alive_caskets:
            # Return casket with most HP
            return max(alive_caskets, key=lambda c: c.hp)

        # Fall back to Support units
        alive_supports = [s for s in army.support_units if s.is_alive]
        if alive_supports:
            return max(alive_supports, key=lambda s: s.hp)

        return None

    def execute_unit_attack(self, attacker, defender):
        """Execute a single unit's attack (Casket or Support)"""
        if isinstance(attacker, Casket):
            # Casket attack uses full combat system
            if isinstance(defender, Casket):
                # Casket vs Casket - use DiceCombatSimulator's execute_turn logic
                return self.casket_attacks_casket(attacker, defender)
            elif isinstance(defender, SupportUnit):
                # Casket vs Support - simplified attack
                return self.casket_attacks_support(attacker, defender)

        elif isinstance(attacker, SupportUnit):
            # Support units attack (simplified - just deal 2 damage)
            if isinstance(defender, Casket):
                damage = defender.take_damage(2, {symbol: 0 for symbol in DefenseDie.FACES})
                self.log(f"  {attacker.name} attacks {defender.name} for {damage} damage ({defender.hp} HP)")
                return damage
            elif isinstance(defender, SupportUnit):
                defender.take_damage(2)
                self.log(f"  {attacker.name} attacks {defender.name} for 2 damage ({defender.hp} HP)")
                return 2

        return 0

    def casket_attacks_casket(self, attacker: Casket, defender: Casket):
        """Casket attacks another Casket using FULL dice mechanics"""
        # Ensure hand is full (draw to 5 cards)
        cards_to_draw = 5 - len(attacker.hand)
        if cards_to_draw > 0:
            # Reshuffle discard if deck empty
            if len(attacker.deck) == 0 and len(attacker.discard) > 0:
                discard_list = list(attacker.discard)
                random.shuffle(discard_list)
                attacker.deck.extend(discard_list)
                attacker.discard.clear()

            # Draw cards
            for _ in range(min(cards_to_draw, len(attacker.deck))):
                if attacker.deck:
                    attacker.hand.append(attacker.deck.popleft())

        # Select attack card
        attack_cards = []
        for c in attacker.hand:
            if isinstance(c, EquipmentCard) and c.type == "Attack":
                attack_cards.append(c)
            elif isinstance(c, FactionCard) and (c.type.lower() == "attack" or c.damage > 0):
                attack_cards.append(c)

        if not attack_cards:
            return 0

        # Get highest damage attack that we can afford
        valid_attacks = [c for c in attack_cards if c.cost <= attacker.sp]
        if not valid_attacks:
            return 0

        attack_card = max(valid_attacks, key=lambda c: c.damage)

        # Pay SP cost (V6.0: Apply Taint SP penalty for Ossuarium)
        sp_cost = attack_card.cost
        if attacker.faction.lower() == 'ossuarium':
            sp_cost += attacker.get_taint_sp_penalty()
        attacker.sp -= sp_cost

        # Apply "on attack" effects (Bleed, Forge, Heat generation)
        effect_lower = attack_card.effect.lower() if hasattr(attack_card, 'effect') else ""

        # Elves: Apply bleed on ATTACK
        if 'bleed' in effect_lower:
            bleed_amount = 2 if 'bleed 2' in effect_lower else 1
            defender.bleed_stacks = min(defender.bleed_stacks + bleed_amount, 4)
            self.log(f"    → Applied {bleed_amount} Bleed to {defender.name} ({defender.bleed_stacks}/4 stacks)")

        # Crucible: Gain Forge on ATTACK
        if 'forge' in effect_lower and 'gain' in effect_lower:
            attacker.forge_tokens = min(attacker.forge_tokens + 1, 5)
            self.log(f"    → Gained 1 Forge ({attacker.forge_tokens}/5 tokens)")

        # Dwarves: Generate Heat on ATTACK
        if hasattr(attack_card, 'heat') and attack_card.heat > 0:
            attacker.heat += attack_card.heat
            self.log(f"    → Generated {attack_card.heat} Heat ({attacker.heat} total)")

        # Roll attack dice
        target_number = 5  # Standard to-hit target
        die1, die2, total = AttackDie.roll_2d6()

        # Check for special results
        if die1 == 0 and die2 == 0:
            # Catastrophic Failure (double JAM)
            attacker.weapon_jammed = True
            attacker.heat += 2
            self.log(f"    {attacker.name} JAMS with {attack_card.name}! (+2 Heat)")
            attacker.hand.remove(attack_card)
            attacker.discard.append(attack_card)
            return 0

        elif die1 == 5 and die2 == 5:
            # Execution (double DEATH BLOW)
            defender.component_damage = 999
            damage = attack_card.damage
            defender.take_damage(damage, {symbol: 0 for symbol in DefenseDie.FACES})
            self.log(f"    {attacker.name} EXECUTES {defender.name} with {attack_card.name}! {damage} damage (component destroyed)")
            attacker.hand.remove(attack_card)
            attacker.discard.append(attack_card)
            return damage

        elif total < target_number:
            # Miss
            self.log(f"    {attacker.name} misses {defender.name} with {attack_card.name} ([{die1}]+[{die2}]={total} < {target_number})")
            attacker.hand.remove(attack_card)
            attacker.discard.append(attack_card)
            return 0

        # Hit - calculate damage and bonus
        base_damage = attack_card.damage
        bonus_damage = 0
        is_critical = False

        if total >= 9:
            # Critical Hit (9+)
            bonus_damage = 2
            is_critical = True
        elif total >= 7:
            # Strong Hit (7-8)
            bonus_damage = 1

        # Apply weapon jam penalty
        if attacker.weapon_jammed:
            bonus_damage -= 2
            attacker.weapon_jammed = False

        total_damage = base_damage + bonus_damage

        # Roll defense dice
        dice_count = max(1, total_damage - (1 if is_critical else 0))
        defense_results = DefenseDie.roll_multiple(dice_count)

        # Apply damage
        actual_damage = defender.take_damage(total_damage, defense_results)

        blocks = defense_results[DefenseDie.SHIELD] + defense_results[DefenseDie.ABSORB]
        self.log(f"    {attacker.name} attacks {defender.name} with {attack_card.name}: [{die1}]+[{die2}]={total} → {actual_damage}/{total_damage} dmg ({blocks} blocked, {defender.hp} HP)")

        # Discard attack card
        attacker.hand.remove(attack_card)
        attacker.discard.append(attack_card)

        return actual_damage

    def casket_attacks_support(self, attacker: Casket, defender: SupportUnit):
        """Casket attacks Support Unit (simplified)"""
        # Support units have no deck, just take flat damage
        # Use average attack damage (4 damage)
        damage = 4
        defender.take_damage(damage)
        self.log(f"  {attacker.name} attacks {defender.name} for {damage} damage ({defender.hp} HP)")
        return damage

    def run_battle(self, max_turns: int = 30) -> dict:
        """
        Run full multi-unit battle until one army is defeated

        Args:
            max_turns: Maximum turns before declaring winner by HP remaining (default 30)
        """
        self.log(f"\n=== MULTI-UNIT BATTLE: {self.army1.faction} vs {self.army2.faction} ===\n")

        while not self.army1.is_defeated and not self.army2.is_defeated and self.turn < max_turns:
            self.turn += 1
            self.log(f"--- Turn {self.turn} ---")

            # Army 1 activates all units
            for unit in list(self.army1.active_units):  # Copy list to avoid modification during iteration
                if self.army2.is_defeated:
                    break

                # Process Casket mechanics
                if isinstance(unit, Casket):
                    # Apply bleed damage at turn start
                    if unit.bleed_stacks > 0:
                        bleed_damage = unit.bleed_stacks
                        for _ in range(bleed_damage):
                            if unit.deck:
                                unit.deck.popleft()
                        self.log(f"  {unit.name} takes {bleed_damage} bleed damage ({unit.bleed_stacks} stacks, {unit.hp} HP)")

                    # Clear weapon jam (lasts 1 turn)
                    if unit.weapon_jammed:
                        unit.weapon_jammed = False
                        self.log(f"  {unit.name} clears weapon jam")

                    # Regenerate SP (+2 per turn, up to max)
                    unit.sp = min(unit.sp + 2, unit.sp_max)

                # Find target (focus fire on strongest)
                target = self.get_strongest_target(self.army2)
                if target:
                    self.execute_unit_attack(unit, target)

            # Check if army2 defeated
            if self.army2.is_defeated:
                break

            # Army 2 activates all units
            for unit in list(self.army2.active_units):
                if self.army1.is_defeated:
                    break

                # Process Casket mechanics
                if isinstance(unit, Casket):
                    # Apply bleed damage at turn start
                    if unit.bleed_stacks > 0:
                        bleed_damage = unit.bleed_stacks
                        for _ in range(bleed_damage):
                            if unit.deck:
                                unit.deck.popleft()
                        self.log(f"  {unit.name} takes {bleed_damage} bleed damage ({unit.bleed_stacks} stacks, {unit.hp} HP)")

                    # Clear weapon jam (lasts 1 turn)
                    if unit.weapon_jammed:
                        unit.weapon_jammed = False
                        self.log(f"  {unit.name} clears weapon jam")

                    # Regenerate SP (+2 per turn, up to max)
                    unit.sp = min(unit.sp + 2, unit.sp_max)

                # Find target (focus fire on strongest)
                target = self.get_strongest_target(self.army1)
                if target:
                    self.execute_unit_attack(unit, target)

        # Determine winner
        if self.army1.is_defeated:
            winner = self.army2.faction
            self.log(f"\n=== BATTLE END: {winner} wins! (Army 1 defeated) ===\n")
        elif self.army2.is_defeated:
            winner = self.army1.faction
            self.log(f"\n=== BATTLE END: {winner} wins! (Army 2 defeated) ===\n")
        else:
            # Timeout - determine by remaining HP
            army1_hp = sum(c.hp for c in self.army1.caskets if c.is_alive)
            army2_hp = sum(c.hp for c in self.army2.caskets if c.is_alive)
            winner = self.army1.faction if army1_hp > army2_hp else self.army2.faction
            self.log(f"\n=== BATTLE TIMEOUT ({self.turn} turns): {winner} wins by HP! ===\n")
            self.log(f"  {self.army1.faction}: {army1_hp} HP remaining")
            self.log(f"  {self.army2.faction}: {army2_hp} HP remaining")

        return {
            'winner': winner,
            'turns': self.turn,
            'army1_units_remaining': len(self.army1.active_units),
            'army2_units_remaining': len(self.army2.active_units),
            'timeout': self.turn >= max_turns and not (self.army1.is_defeated or self.army2.is_defeated)
        }

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
