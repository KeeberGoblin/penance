#!/usr/bin/env python3
"""Analyze equipment balance."""

import json
from collections import defaultdict

def load_card_data():
    with open('/workspaces/penance/docs/cards/complete-card-data.json', 'r') as f:
        return json.load(f)

def main():
    data = load_card_data()

    if 'equipment_items' in data:
        print("=" * 100)
        print("EQUIPMENT ANALYSIS")
        print("=" * 100)

        equipment = data['equipment_items']

        weapons = []
        armor = []
        accessories = []

        for item in equipment:
            name = item.get('name', 'Unknown')
            item_type = item.get('type', 'unknown')
            damage = item.get('damage', 0)
            defense = item.get('defense', 0)
            effect = item.get('effect', '') + ' ' + item.get('text', '')

            if isinstance(damage, str):
                try:
                    damage = int(damage)
                except:
                    damage = 0

            if isinstance(defense, str):
                try:
                    defense = int(defense)
                except:
                    defense = 0

            item_data = {
                'name': name,
                'type': item_type,
                'damage': damage,
                'defense': defense,
                'effect': effect[:150]
            }

            if 'weapon' in item_type.lower():
                weapons.append(item_data)
            elif 'armor' in item_type.lower():
                armor.append(item_data)
            else:
                accessories.append(item_data)

        print(f"\nWEAPONS ({len(weapons)} total):")
        print(f"{'Name':<30} {'Damage':<10} {'Special Effect':<60}")
        print("-" * 100)
        for w in sorted(weapons, key=lambda x: x['damage'], reverse=True):
            effect_summary = w['effect'][:60] if w['effect'] else 'None'
            print(f"{w['name']:<30} {w['damage']:<10} {effect_summary:<60}")

        print(f"\n\nARMOR ({len(armor)} total):")
        print(f"{'Name':<30} {'Defense':<10} {'Special Effect':<60}")
        print("-" * 100)
        for a in sorted(armor, key=lambda x: x['defense'], reverse=True):
            effect_summary = a['effect'][:60] if a['effect'] else 'None'
            print(f"{a['name']:<30} {a['defense']:<10} {effect_summary:<60}")

        print(f"\n\nACCESSORIES ({len(accessories)} total):")
        print(f"{'Name':<30} {'Type':<20} {'Effect':<60}")
        print("-" * 100)
        for acc in accessories[:15]:
            effect_summary = acc['effect'][:60] if acc['effect'] else 'None'
            print(f"{acc['name']:<30} {acc['type']:<20} {effect_summary:<60}")

        # Analyze weapon damage distribution
        if weapons:
            weapon_damages = [w['damage'] for w in weapons if w['damage'] > 0]
            if weapon_damages:
                avg_damage = sum(weapon_damages) / len(weapon_damages)
                print(f"\n\nWEAPON STATISTICS:")
                print(f"  Average Damage: {avg_damage:.2f}")
                print(f"  Min Damage: {min(weapon_damages)}")
                print(f"  Max Damage: {max(weapon_damages)}")
                print(f"  Range: {max(weapon_damages) - min(weapon_damages)}")

        # Analyze armor defense distribution
        if armor:
            armor_defenses = [a['defense'] for a in armor if a['defense'] > 0]
            if armor_defenses:
                avg_defense = sum(armor_defenses) / len(armor_defenses)
                print(f"\n\nARMOR STATISTICS:")
                print(f"  Average Defense: {avg_defense:.2f}")
                print(f"  Min Defense: {min(armor_defenses)}")
                print(f"  Max Defense: {max(armor_defenses)}")
                print(f"  Range: {max(armor_defenses) - min(armor_defenses)}")

if __name__ == '__main__':
    main()
