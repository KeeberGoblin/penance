#!/usr/bin/env python3
"""Analyze equipment cards by faction."""

import json
from collections import defaultdict

def load_card_data():
    with open('/workspaces/penance/docs/cards/complete-card-data.json', 'r') as f:
        return json.load(f)

def main():
    data = load_card_data()

    if 'equipment' not in data:
        print("No equipment data found")
        return

    equipment = data['equipment']

    print("=" * 100)
    print("EQUIPMENT CARD ANALYSIS")
    print("=" * 100)

    # Group by faction
    by_faction = defaultdict(list)
    for card in equipment:
        keywords = card.get('keywords', [])
        # Extract faction from keywords
        faction = 'universal'
        for kw in keywords:
            if kw in ['church', 'dwarves', 'ossuarium', 'elves', 'nomads',
                      'crucible', 'emergent', 'exchange', 'vestige-bloodlines', 'wyrd-conclave']:
                faction = kw
                break
        by_faction[faction].append(card)

    # Analyze each faction's equipment
    faction_equipment_stats = {}

    for faction in sorted(by_faction.keys()):
        cards = by_faction[faction]

        total_damage = 0
        damage_cards = []

        for card in cards:
            damage = card.get('damage', 0)
            if isinstance(damage, str):
                try:
                    damage = int(damage)
                except:
                    damage = 0

            if damage > 0:
                damage_cards.append({
                    'name': card.get('name'),
                    'damage': damage,
                    'cost': card.get('cost', 0),
                    'type': card.get('type'),
                    'range': card.get('range', 'Unknown')
                })
                total_damage += damage

        avg_damage = total_damage / len(damage_cards) if damage_cards else 0

        faction_equipment_stats[faction] = {
            'total_cards': len(cards),
            'damage_cards': len(damage_cards),
            'avg_damage': avg_damage,
            'total_damage': total_damage
        }

        print(f"\n{'=' * 100}")
        print(f"FACTION: {faction.upper()}")
        print(f"{'=' * 100}")
        print(f"Total Equipment Cards: {len(cards)}")
        print(f"Damage-Dealing Cards: {len(damage_cards)}")
        print(f"Average Damage: {avg_damage:.2f}")

        if damage_cards:
            print(f"\nDamage Cards:")
            print(f"{'Name':<35} {'Damage':<10} {'Cost':<8} {'Range':<15}")
            print("-" * 100)
            for dc in sorted(damage_cards, key=lambda x: x['damage'], reverse=True):
                print(f"{dc['name']:<35} {dc['damage']:<10} {dc['cost']:<8} {dc['range']:<15}")

    # Compare problem factions
    print(f"\n\n{'=' * 100}")
    print("EQUIPMENT COMPARISON - PROBLEM FACTIONS")
    print(f"{'=' * 100}")

    problem_factions = ['ossuarium', 'vestige-bloodlines', 'church', 'dwarves']

    print(f"\n{'Faction':<25} {'Total Cards':<15} {'Damage Cards':<15} {'Avg Damage':<15}")
    print("-" * 100)
    for faction in problem_factions:
        if faction in faction_equipment_stats:
            stats = faction_equipment_stats[faction]
            print(f"{faction:<25} {stats['total_cards']:<15} {stats['damage_cards']:<15} {stats['avg_damage']:<15.2f}")

    # Overall equipment stats
    print(f"\n\n{'=' * 100}")
    print("OVERALL EQUIPMENT STATISTICS")
    print(f"{'=' * 100}")

    all_damages = []
    for card in equipment:
        damage = card.get('damage', 0)
        if isinstance(damage, str):
            try:
                damage = int(damage)
            except:
                damage = 0
        if damage > 0:
            all_damages.append(damage)

    if all_damages:
        print(f"Total Equipment Cards: {len(equipment)}")
        print(f"Cards with Damage: {len(all_damages)}")
        print(f"Average Damage: {sum(all_damages) / len(all_damages):.2f}")
        print(f"Min Damage: {min(all_damages)}")
        print(f"Max Damage: {max(all_damages)}")
        print(f"Damage Range: {max(all_damages) - min(all_damages)}")

if __name__ == '__main__':
    main()
