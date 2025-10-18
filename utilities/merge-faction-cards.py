#!/usr/bin/env python3
"""
Merge extracted faction cards into complete-card-data.json
"""

import json
from datetime import datetime

def main():
    print("🔄 Merging new faction cards into database...")
    print()

    # Load current database
    print("📖 Loading current database...")
    with open('docs/cards/complete-card-data.json', 'r', encoding='utf-8') as f:
        db = json.load(f)

    print(f"  Current version: {db['_meta']['version']}")
    print(f"  Current factions: {len([k for k in db.keys() if k not in ['_meta', 'universal', 'equipment', 'tactics', 'v3_optional', 'support_units']])}")
    print()

    # Load extracted cards
    print("📥 Loading extracted faction cards...")
    with open('utilities/extracted-faction-cards.json', 'r', encoding='utf-8') as f:
        new_factions = json.load(f)

    print(f"  New factions to add: {list(new_factions.keys())}")
    print()

    # Merge new factions
    print("🔧 Merging factions...")
    for faction_name, cards in new_factions.items():
        if faction_name in db:
            print(f"  ⚠️ {faction_name} already exists, overwriting with {len(cards)} cards")
        else:
            print(f"  ✅ Adding {faction_name} with {len(cards)} cards")

        db[faction_name] = cards

    # Update metadata
    db['_meta']['version'] = '3.1'
    db['_meta']['lastUpdated'] = datetime.now().strftime('%Y-%m-%d')
    db['_meta']['description'] = 'Complete Penance card database v3.1 - All 9 factions included'

    # Save updated database
    print()
    print("💾 Saving updated database...")
    with open('docs/cards/complete-card-data.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("  ✅ Saved to docs/cards/complete-card-data.json")
    print()

    # Summary
    print("=== DATABASE UPDATED ===")
    print(f"Version: {db['_meta']['version']}")
    print(f"Last Updated: {db['_meta']['lastUpdated']}")
    print()
    print("Factions:")
    factions = [k for k in db.keys() if k not in ['_meta', 'universal', 'equipment', 'tactics', 'v3_optional', 'support_units']]
    for faction in sorted(factions):
        card_count = len(db[faction])
        print(f"  • {faction}: {card_count} cards")
    print()
    print(f"Total factions: {len(factions)}")
    print(f"Total faction cards: {sum(len(db[f]) for f in factions)}")
    print()
    print("✅ Database merge complete!")

if __name__ == '__main__':
    main()
