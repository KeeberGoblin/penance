#!/usr/bin/env python3
"""Analyze faction card data for balance issues."""

import json
from collections import defaultdict
from typing import Dict, List, Any

def load_card_data():
    with open('/workspaces/penance/docs/cards/complete-card-data.json', 'r') as f:
        return json.load(f)

def analyze_faction(faction_name: str, cards: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze a single faction's card data."""
    stats = {
        'name': faction_name,
        'total_cards': len(cards),
        'attack_cards': [],
        'damage_values': [],
        'resource_cards': [],
        'special_abilities': [],
        'equipment_interactions': [],
        'card_types': defaultdict(int),
        'cost_distribution': defaultdict(int),
    }

    for card_data in cards:
        card_name = card_data.get('name', 'Unknown')

        # Card type
        card_type = card_data.get('type', 'unknown')
        stats['card_types'][card_type] += 1

        # Cost
        cost = card_data.get('cost', 0)
        stats['cost_distribution'][cost] += 1

        # Text for abilities (check both 'text' and 'effect' fields)
        text = card_data.get('text', '') + ' ' + card_data.get('effect', '')

        # Attack cards (cards that deal damage)
        if 'damage' in card_data or 'damage' in text.lower() or 'deal' in text.lower() or 'attack' in text.lower():
            damage = card_data.get('damage', 0)
            # Convert damage to int if it's a string
            if isinstance(damage, str):
                try:
                    damage = int(damage)
                except (ValueError, TypeError):
                    damage = 0
            stats['attack_cards'].append({
                'name': card_name,
                'damage': damage,
                'cost': cost,
                'text': text[:100]
            })
            if isinstance(damage, (int, float)) and damage > 0:
                stats['damage_values'].append(damage)

        # Resource economy
        if any(keyword in text.lower() for keyword in ['draw', 'gain', 'mana', 'resource', 'coin', 'gold']):
            stats['resource_cards'].append({
                'name': card_name,
                'cost': cost,
                'text': text[:100]
            })

        # Special abilities
        if any(keyword in text.lower() for keyword in ['summon', 'transform', 'counter', 'prevent', 'return', 'destroy']):
            stats['special_abilities'].append({
                'name': card_name,
                'ability_type': 'special',
                'text': text[:100]
            })

        # Equipment interactions
        if 'equipment' in text.lower() or 'weapon' in text.lower() or 'armor' in text.lower():
            stats['equipment_interactions'].append({
                'name': card_name,
                'text': text[:100]
            })

    # Calculate averages
    if stats['damage_values']:
        stats['avg_damage'] = sum(stats['damage_values']) / len(stats['damage_values'])
        stats['max_damage'] = max(stats['damage_values'])
        stats['min_damage'] = min(stats['damage_values'])
    else:
        stats['avg_damage'] = 0
        stats['max_damage'] = 0
        stats['min_damage'] = 0

    stats['num_attack_cards'] = len(stats['attack_cards'])
    stats['num_resource_cards'] = len(stats['resource_cards'])
    stats['num_special_abilities'] = len(stats['special_abilities'])
    stats['num_equipment_interactions'] = len(stats['equipment_interactions'])

    return stats

def main():
    data = load_card_data()

    # Focus on the main 10 factions
    main_factions = ['church', 'dwarves', 'ossuarium', 'elves', 'nomads',
                     'crucible', 'emergent', 'exchange', 'vestige-bloodlines', 'wyrd-conclave']

    print("=" * 80)
    print("FACTION CARD ANALYSIS")
    print("=" * 80)

    faction_stats = {}

    for faction in main_factions:
        if faction in data:
            stats = analyze_faction(faction, data[faction])
            faction_stats[faction] = stats

            print(f"\n{'=' * 80}")
            print(f"FACTION: {faction.upper()}")
            print(f"{'=' * 80}")
            print(f"Total Cards: {stats['total_cards']}")
            print(f"Attack Cards: {stats['num_attack_cards']}")
            print(f"Average Damage: {stats['avg_damage']:.2f}")
            print(f"Damage Range: {stats['min_damage']} - {stats['max_damage']}")
            print(f"Resource Economy Cards: {stats['num_resource_cards']}")
            print(f"Special Abilities: {stats['num_special_abilities']}")
            print(f"Equipment Interactions: {stats['num_equipment_interactions']}")
            print(f"\nCard Types: {dict(stats['card_types'])}")

            # Show top damage dealers
            if stats['attack_cards']:
                print(f"\nTop Damage Cards:")
                sorted_attacks = sorted(stats['attack_cards'], key=lambda x: x.get('damage', 0), reverse=True)[:5]
                for card in sorted_attacks:
                    print(f"  - {card['name']}: {card['damage']} damage (cost {card['cost']})")

            # Show resource cards
            if stats['resource_cards']:
                print(f"\nResource Cards (first 3):")
                for card in stats['resource_cards'][:3]:
                    print(f"  - {card['name']}: {card['text']}")

    # Comparative analysis
    print(f"\n\n{'=' * 80}")
    print("COMPARATIVE ANALYSIS")
    print(f"{'=' * 80}")

    print(f"\n{'Faction':<20} {'Avg Dmg':<10} {'Attack':<8} {'Resource':<10} {'Special':<10}")
    print("-" * 80)
    for faction in main_factions:
        if faction in faction_stats:
            s = faction_stats[faction]
            print(f"{faction:<20} {s['avg_damage']:<10.2f} {s['num_attack_cards']:<8} {s['num_resource_cards']:<10} {s['num_special_abilities']:<10}")

    # Problem faction deep dive
    print(f"\n\n{'=' * 80}")
    print("PROBLEM FACTION DEEP DIVE")
    print(f"{'=' * 80}")

    problem_factions = {
        'ossuarium': '64% WR - Strong without lifesteal',
        'vestige-bloodlines': '69% WR - Consistently overpowered',
        'church': '27% WR - Collapsed',
        'dwarves': '29% -> 47% WR - Recovered'
    }

    for faction, description in problem_factions.items():
        if faction in faction_stats:
            print(f"\n{faction.upper()} - {description}")
            print("-" * 80)
            s = faction_stats[faction]

            # Show all attack cards for problem factions
            print(f"All Attack Cards ({len(s['attack_cards'])} total):")
            for card in sorted(s['attack_cards'], key=lambda x: x.get('damage', 0), reverse=True):
                print(f"  - {card['name']}: {card['damage']} dmg @ {card['cost']} cost")

            # Show all resource cards
            print(f"\nResource Economy Cards ({len(s['resource_cards'])} total):")
            for card in s['resource_cards']:
                print(f"  - {card['name']}: {card['text']}")

            # Show special abilities
            print(f"\nSpecial Abilities ({len(s['special_abilities'])} total):")
            for card in s['special_abilities'][:5]:
                print(f"  - {card['name']}: {card['text']}")

if __name__ == '__main__':
    main()
