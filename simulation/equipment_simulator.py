#!/usr/bin/env python3
"""
Penance Equipment-Randomized Combat Simulator
Models realistic deck construction with equipment card randomization
"""

import random
import json
from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict, List, Optional
from enum import Enum

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

    def __repr__(self):
        return f"{self.name} ({self.type}, {self.cost} SP)"

# ============================================================================
# CASKET CLASSES
# ============================================================================

class CasketClass(Enum):
    """Casket class definitions with point costs"""
    # Format: (name, SP, deck_size/HP, point_cost)
    SCOUT = ("Scout", 6, 28, 1)           # Fast, fragile, cheap
    WARDEN = ("Warden", 5, 34, 2)         # Balanced, standard
    VANGUARD = ("Vanguard", 4, 40, 3)     # Slow, tanky, expensive
    COLOSSUS = ("Colossus", 4, 50, 4)     # Boss unit (BUFFED: 3 SP → 4 SP, point cost 5 → 4)

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
    """Represents a Casket with equipment-based deck"""
    name: str
    faction: str
    casket_class: CasketClass = CasketClass.WARDEN

    # Card-based HP system
    deck: Deque = field(default_factory=deque)
    hand: Deque = field(default_factory=deque)
    discard: Deque = field(default_factory=deque)

    # SP and Heat (SP banks between turns!)
    sp: int = 5
    sp_max: int = 5
    heat: int = 0

    # Positioning (range in hexes, 0 = melee range)
    range: int = 2  # Start at medium range (2 hexes away)
    moved_this_turn: bool = False

    # Equipment cards in deck
    equipment_cards: List[EquipmentCard] = field(default_factory=list)

    def __post_init__(self):
        """Initialize SP based on casket class"""
        self.sp = self.casket_class.sp_max
        self.sp_max = self.casket_class.sp_max

    @property
    def hp(self):
        """Current HP = cards in deck + hand"""
        return len(self.deck) + len(self.hand)

    @property
    def is_alive(self):
        return self.hp > 0

    def draw_cards(self, count: int):
        """Draw cards from deck to hand"""
        for _ in range(min(count, len(self.deck))):
            card = self.deck.popleft()
            self.hand.append(card)

    def take_damage(self, amount: int):
        """Take damage - discard cards"""
        if amount <= 0:
            return

        for _ in range(amount):
            if self.hand:
                card = self.hand.pop()
                self.discard.append(card)
            elif self.deck:
                card = self.deck.popleft()
                self.discard.append(card)
            else:
                break  # No more cards to discard

# ============================================================================
# DECK BUILDER
# ============================================================================

class DeckBuilder:
    """Builds equipment-randomized decks"""

    def __init__(self, card_db):
        self.card_db = card_db
        self.equipment_items = card_db.get('equipment_items', [])

    def build_random_deck(self, faction: str, casket_class: CasketClass = CasketClass.WARDEN,
                          num_equipment_items: int = 2) -> Casket:
        """
        Build a random deck with equipment cards scaled to casket class
        Prioritizes faction-specific equipment over universal equipment

        Scout (28 HP): 20 core + 8 equipment (2 items × 4 cards)
        Warden (34 HP): 26 core + 8 equipment (2 items × 4 cards)
        Vanguard (40 HP): 32 core + 8 equipment (2 items × 4 cards)
        Colossus (50 HP): 42 core + 8 equipment (2 items × 4 cards)
        """
        casket = Casket(name=f"{faction}-{casket_class.name.lower()}",
                       faction=faction,
                       casket_class=casket_class)

        # Normalize faction names for matching
        faction_normalized = faction.lower().replace('_', '-')

        # Faction name mappings for equipment matching
        faction_aliases = {
            'wyrd': 'wyrd-conclave',
            'bloodlines': 'vestige-bloodlines',
            'emergent': 'emergent',
            'ossuarium': 'ossuarium'
        }

        # Use alias if available
        search_name = faction_aliases.get(faction_normalized, faction_normalized)

        # Filter equipment by faction (flexible matching)
        faction_equipment = [
            item for item in self.equipment_items
            if search_name in item.get('faction', '').lower() or faction_normalized in item.get('faction', '').lower()
        ]

        universal_equipment = [
            item for item in self.equipment_items
            if item.get('faction', '') == 'universal'
        ]

        # Select equipment: prefer faction-specific, fill with universal
        selected_equipment = []

        # Add faction-specific equipment first (up to num_equipment_items)
        if faction_equipment:
            num_faction_items = min(len(faction_equipment), num_equipment_items)
            selected_equipment.extend(random.sample(faction_equipment, k=num_faction_items))

        # Fill remaining slots with universal equipment
        remaining_slots = num_equipment_items - len(selected_equipment)
        if remaining_slots > 0 and universal_equipment:
            num_universal_items = min(len(universal_equipment), remaining_slots)
            selected_equipment.extend(random.sample(universal_equipment, k=num_universal_items))

        # Add equipment cards to deck
        for equipment in selected_equipment:
            equipment_name = equipment['name']
            cards = equipment['cards']

            for card_data in cards:
                # Create equipment card object
                eq_card = EquipmentCard(
                    name=card_data['name'],
                    type=card_data['type'],
                    cost=card_data.get('cost', 0),
                    effect=card_data['effect'],
                    damage=card_data.get('damage', 0),
                    defense=card_data.get('defense', 0),
                    range=card_data.get('range', 'Melee'),
                    equipment_name=equipment_name
                )

                # Add card to deck (some equipment has multiple copies)
                card_count = card_data.get('cardCount', 1)
                for _ in range(card_count):
                    casket.equipment_cards.append(eq_card)
                    casket.deck.append(eq_card)

        # Add generic HP cards to reach deck size (filler cards)
        target_deck_size = casket_class.deck_size
        while len(casket.deck) < target_deck_size:
            casket.deck.append(f"GenericCard-{len(casket.deck)}")

        # Shuffle deck
        deck_list = list(casket.deck)
        random.shuffle(deck_list)
        casket.deck = deque(deck_list)

        return casket

# ============================================================================
# COMBAT SIMULATOR
# ============================================================================

class EquipmentCombatSimulator:
    """Simulates combat with equipment-based decks"""

    def __init__(self, casket1: Casket, casket2: Casket, verbose: bool = False):
        self.casket1 = casket1
        self.casket2 = casket2
        self.verbose = verbose
        self.turn = 0

    def log(self, message: str):
        if self.verbose:
            print(message)

    def run_combat(self, max_turns: int = 50) -> Dict:
        """Run combat simulation"""
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
            'casket2_hp': self.casket2.hp
        }

    def execute_turn(self, attacker: Casket, defender: Casket):
        """Execute one player's turn with combo/synergy support and positioning"""
        # Regenerate 2 SP per turn (banking mechanic!)
        attacker.sp = min(attacker.sp + 2, attacker.sp_max)
        attacker.moved_this_turn = False

        # Draw cards
        attacker.draw_cards(3)

        # TACTICAL DECISION: Move closer OR save SP for combo?
        # If out of range and have melee-only cards, consider moving
        if attacker.range > 0:
            melee_cards = [c for c in attacker.hand if isinstance(c, EquipmentCard)
                          and c.type == "Attack" and c.range == "Melee"]

            ranged_cards = [c for c in attacker.hand if isinstance(c, EquipmentCard)
                           and c.type == "Attack" and c.range == "Ranged"]

            # AGGRESSIVE: Always move if no ranged options OR if we have 3+ SP to spare
            should_move = False

            if melee_cards and not ranged_cards:
                # No ranged attacks - MUST move to do anything
                should_move = True
            elif melee_cards and attacker.sp >= 4:
                # Have SP to spare - move AND still attack
                should_move = True

            if should_move:
                # Movement costs 1 SP per hex
                move_cost = min(attacker.range, max(1, attacker.sp - 2))  # Leave at least 2 SP for attack
                if move_cost > 0:
                    attacker.sp -= move_cost
                    attacker.range -= move_cost
                    attacker.moved_this_turn = True
                    self.log(f"{attacker.name} moves {move_cost} hexes closer (now {attacker.range} hexes away, {attacker.sp} SP remaining)")

        # Try to find combo play (multi-card synergy)
        combo_cards = self.select_combo_play(attacker)

        if combo_cards:
            # Check range for combo attacks
            can_attack = all(c.range == "Ranged" or attacker.range == 0 for c in combo_cards)

            if can_attack:
                # Execute combo
                total_damage = 0
                total_cost = 0
                combo_names = []

                for card in combo_cards:
                    attacker.sp -= card.cost
                    total_cost += card.cost
                    total_damage += card.damage
                    combo_names.append(card.name)

                # Combo bonus: +1 damage for 2-card combo, +2 for 3-card combo
                combo_bonus = len(combo_cards) - 1
                total_damage += combo_bonus

                # Defender can use defense card
                defense_card = self.select_defense_card(defender)
                if defense_card:
                    total_damage = max(0, total_damage - defense_card.defense)
                    self.log(f"  {defender.name} defends with {defense_card.name} (-{defense_card.defense} dmg)")

                # Deal damage
                defender.take_damage(total_damage)
                self.log(f"{attacker.name} COMBO ({len(combo_cards)} cards): {' + '.join(combo_names)} for {total_damage} damage (bonus: +{combo_bonus}) ({defender.name}: {defender.hp} HP)")
            else:
                # Can't attack - out of range for melee combo
                if not attacker.moved_this_turn:
                    # Bank SP for next turn instead
                    self.log(f"{attacker.name} holds position, banking {attacker.sp} SP for next turn (out of melee range)")
                else:
                    self.log(f"{attacker.name} moved but still out of range")

        else:
            # Fallback: single attack card
            attack_card = self.select_attack_card(attacker)

            if attack_card and attacker.sp >= attack_card.cost:
                # Check range
                can_attack = (attack_card.range == "Ranged" or attacker.range == 0)

                if can_attack:
                    # Execute attack
                    attacker.sp -= attack_card.cost
                    damage = attack_card.damage

                    # Defender can use defense card
                    defense_card = self.select_defense_card(defender)
                    if defense_card:
                        damage = max(0, damage - defense_card.defense)
                        self.log(f"  {defender.name} defends with {defense_card.name} (-{defense_card.defense} dmg)")

                    # Deal damage
                    defender.take_damage(damage)
                    self.log(f"{attacker.name} attacks with {attack_card.name} for {damage} damage ({defender.name}: {defender.hp} HP)")
                else:
                    # Out of range - bank SP
                    if not attacker.moved_this_turn:
                        self.log(f"{attacker.name} out of range, banking {attacker.sp} SP for next turn")
                    else:
                        self.log(f"{attacker.name} moved but still out of range")
            else:
                if not attacker.moved_this_turn:
                    self.log(f"{attacker.name} has no valid attacks, banking {attacker.sp} SP")
                else:
                    self.log(f"{attacker.name} moved but has no valid attacks")

    def select_combo_play(self, casket: Casket) -> Optional[List[EquipmentCard]]:
        """
        Select best combo of attack cards to play this turn
        Prioritizes synergy (multi-card combos) over burst (single high-damage card)
        """
        attack_cards = [c for c in casket.hand if isinstance(c, EquipmentCard) and c.type == "Attack"]

        if not attack_cards:
            return None

        # Try to find best combo within SP budget
        best_combo = None
        best_value = 0  # damage + combo_bonus

        # Try 3-card combos (prioritize synergy)
        for i, card1 in enumerate(attack_cards):
            for j, card2 in enumerate(attack_cards[i+1:], start=i+1):
                for k, card3 in enumerate(attack_cards[j+1:], start=j+1):
                    total_cost = card1.cost + card2.cost + card3.cost
                    if total_cost <= casket.sp:
                        total_damage = card1.damage + card2.damage + card3.damage
                        combo_bonus = 2  # 3-card combo bonus
                        value = total_damage + combo_bonus

                        if value > best_value:
                            best_value = value
                            best_combo = [card1, card2, card3]

        # Try 2-card combos
        if not best_combo:
            for i, card1 in enumerate(attack_cards):
                for card2 in attack_cards[i+1:]:
                    total_cost = card1.cost + card2.cost
                    if total_cost <= casket.sp:
                        total_damage = card1.damage + card2.damage
                        combo_bonus = 1  # 2-card combo bonus
                        value = total_damage + combo_bonus

                        if value > best_value:
                            best_value = value
                            best_combo = [card1, card2]

        # Only return combo if it's better than single-card rush
        if best_combo and len(best_combo) > 1:
            # Calculate single-card rush value
            single_card = self.select_attack_card(casket)
            if single_card:
                single_value = single_card.damage

                # Combo must be AT LEAST as good as rush (encourages synergy)
                if best_value >= single_value:
                    return best_combo

        return None

    def select_attack_card(self, casket: Casket) -> Optional[EquipmentCard]:
        """Select best single attack card from hand (fallback if no combo)"""
        attack_cards = [c for c in casket.hand if isinstance(c, EquipmentCard) and c.type == "Attack"]

        if not attack_cards:
            return None

        # Select highest damage attack that we can afford
        valid_attacks = [c for c in attack_cards if c.cost <= casket.sp]
        if not valid_attacks:
            return None

        return max(valid_attacks, key=lambda c: c.damage)

    def select_defense_card(self, casket: Casket) -> Optional[EquipmentCard]:
        """Select best defense card from hand"""
        defense_cards = [c for c in casket.hand if isinstance(c, EquipmentCard) and c.type == "Reactive"]

        if not defense_cards:
            return None

        # Select highest defense value
        return max(defense_cards, key=lambda c: c.defense)

# ============================================================================
# TEAM BUILDER
# ============================================================================

class TeamBuilder:
    """Builds point-balanced teams"""

    @staticmethod
    def build_team(builder: DeckBuilder, faction: str, total_points: int = 5) -> List[Casket]:
        """
        Build a team with specified point total

        Examples:
        - 5 points: 1 Colossus OR 1 Vanguard + 1 Warden OR 2 Wardens + 1 Scout
        - 10 points: 2 Colossus OR 5 Wardens, etc.
        """
        team = []
        remaining_points = total_points

        # Greedy allocation: use largest units first
        while remaining_points > 0:
            if remaining_points >= 4:
                # Add Colossus (4 pts)
                team.append(builder.build_random_deck(faction, CasketClass.COLOSSUS))
                remaining_points -= 4
            elif remaining_points >= 3:
                # Add Vanguard (3 pts)
                team.append(builder.build_random_deck(faction, CasketClass.VANGUARD))
                remaining_points -= 3
            elif remaining_points >= 2:
                # Add Warden (2 pts)
                team.append(builder.build_random_deck(faction, CasketClass.WARDEN))
                remaining_points -= 2
            else:
                # Add Scout (1 pt)
                team.append(builder.build_random_deck(faction, CasketClass.SCOUT))
                remaining_points -= 1

        return team

    @staticmethod
    def print_team_composition(team: List[Casket]):
        """Print team composition with point values"""
        total_hp = sum(c.hp for c in team)
        total_points = sum(c.casket_class.point_cost for c in team)

        print(f"  Team: {len(team)} units, {total_hp} HP, {total_points} points")
        for casket in team:
            print(f"    - {casket.name} ({casket.casket_class.name}, "
                  f"{casket.hp} HP, {casket.sp_max} SP, {casket.casket_class.point_cost} pts)")

# ============================================================================
# MAIN TEST
# ============================================================================

if __name__ == "__main__":
    print("Penance Equipment-Randomized Combat Simulator")
    print("=" * 80)
    print("\nCasket Classes:")
    print("  Scout:     28 HP, 6 SP, 1 point  (Fast, fragile)")
    print("  Warden:    34 HP, 5 SP, 2 points (Balanced)")
    print("  Vanguard:  40 HP, 4 SP, 3 points (Tanky)")
    print("  Colossus:  50 HP, 4 SP, 4 points (Boss unit - BUFFED: 3 SP → 4 SP)")
    print("=" * 80)

    # Load card database
    card_db = load_card_database()
    builder = DeckBuilder(card_db)

    # ========================================================================
    # 6-POINT BATTLE TESTS (Realistic Army Compositions)
    # ========================================================================

    print("\n" + "=" * 80)
    print("6-POINT BATTLE TESTS (20 runs per matchup)")
    print("=" * 80)

    matchups = [
        ("Colossus + Warden", "church", 6, "2 Vanguards", "dwarves", 6),
        ("Colossus + Warden", "elves", 6, "3 Wardens", "crucible", 6),
        ("2 Vanguards", "nomads", 6, "3 Wardens", "exchange", 6),
        ("Colossus + Warden", "bloodlines", 6, "Vanguard + Warden + Scout", "emergent", 6),
    ]

    for idx, (team1_desc, faction1, pts1, team2_desc, faction2, pts2) in enumerate(matchups, 1):
        print(f"\n=== MATCHUP {idx}: {team1_desc} ({faction1}) vs {team2_desc} ({faction2}) ===")

        team1_wins = 0
        team2_wins = 0
        total_team1_hp = 0
        total_team2_hp = 0

        for run in range(20):
            # Build teams
            team1 = TeamBuilder.build_team(builder, faction1, total_points=pts1)
            team2 = TeamBuilder.build_team(builder, faction2, total_points=pts2)

            # For now, test with lead unit (1v1) since multi-unit combat not implemented
            casket1 = team1[0]
            casket2 = team2[0]

            combat = EquipmentCombatSimulator(casket1, casket2, verbose=False)
            result = combat.run_combat(max_turns=50)

            if result['winner'] == casket1.name:
                team1_wins += 1
            else:
                team2_wins += 1

            total_team1_hp += result['casket1_hp']
            total_team2_hp += result['casket2_hp']

        # Results
        team1_wr = (team1_wins / 20) * 100
        team2_wr = (team2_wins / 20) * 100
        avg_team1_hp = total_team1_hp / 20
        avg_team2_hp = total_team2_hp / 20

        print(f"\n{team1_desc} ({faction1}): {team1_wins}-{team2_wins} ({team1_wr:.1f}% WR, avg {avg_team1_hp:.1f} HP remaining)")
        print(f"{team2_desc} ({faction2}): {team2_wins}-{team1_wins} ({team2_wr:.1f}% WR, avg {avg_team2_hp:.1f} HP remaining)")

        if abs(team1_wr - 50) <= 10:
            print("✅ BALANCED (40-60% WR)")
        else:
            print(f"⚠️ UNBALANCED ({team1_desc if team1_wr > 60 else team2_desc} too strong)")

    # ========================================================================
    # COLOSSUS VALIDATION TEST
    # ========================================================================

    print("\n" + "=" * 80)
    print("COLOSSUS POINT COST VALIDATION (4 pts vs 3 pts)")
    print("=" * 80)
    print("\nTesting: Colossus (4 pts) should beat Vanguard (3 pts) consistently")

    colossus_wins = 0
    vanguard_wins = 0

    for run in range(20):
        colossus = builder.build_random_deck("church", CasketClass.COLOSSUS)
        vanguard = builder.build_random_deck("dwarves", CasketClass.VANGUARD)

        combat = EquipmentCombatSimulator(colossus, vanguard, verbose=False)
        result = combat.run_combat(max_turns=50)

        if result['winner'] == colossus.name:
            colossus_wins += 1
        else:
            vanguard_wins += 1

    colossus_wr = (colossus_wins / 20) * 100
    print(f"\nColossus: {colossus_wins}-{vanguard_wins} ({colossus_wr:.1f}% WR)")
    print(f"Vanguard: {vanguard_wins}-{colossus_wins} ({100 - colossus_wr:.1f}% WR)")

    if colossus_wr >= 60:
        print("✅ VALIDATED: Colossus worth 4 points (beats 3-point Vanguard)")
    else:
        print("⚠️ WARNING: Colossus may be undervalued at 4 points")

    print("\n" + "=" * 80)
    print("NOTE: Team battles (multiple units) not yet implemented.")
    print("      Current tests use lead unit (1v1 proxy for team strength).")
    print("      Future: Implement initiative system and multi-unit combat.")
    print("=" * 80)
