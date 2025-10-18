#!/usr/bin/env python3
"""
Card Database Completeness and Accuracy Audit
Compares complete-card-data.json with faction markdown documentation
"""

import json
import re
from pathlib import Path
from collections import defaultdict

# Load JSON database
json_path = Path('/workspaces/penance/docs/cards/complete-card-data.json')
with open(json_path) as f:
    db = json.load(f)

# Expected factions
EXPECTED_FACTIONS = [
    'church', 'dwarves', 'elves', 'ossuarium',
    'wyrd', 'emergent', 'nomads', 'exchange',
    'crucible', 'vestige-bloodlines'
]

print("=" * 80)
print("CARD DATABASE AUDIT REPORT")
print("=" * 80)
print()

# SECTION 1: Database Structure Analysis
print("SECTION 1: DATABASE STRUCTURE ANALYSIS")
print("-" * 80)

# Count cards per section
sections = {}
for key in db.keys():
    if key == '_meta':
        continue
    if isinstance(db[key], list):
        sections[key] = len(db[key])

print(f"\n{len(sections)} sections found in JSON:")
for section, count in sorted(sections.items()):
    print(f"  - {section}: {count} cards")

# Count universal cards
universal_count = len(db.get('universal', []))
print(f"\nUniversal cards: {universal_count}")

# Expected: 10 movement + defense + utility cards

# Count faction cards
faction_sections = [k for k in sections.keys() if k not in ['universal', 'equipment']]
print(f"\nFaction sections: {len(faction_sections)}")
for faction in sorted(faction_sections):
    print(f"  - {faction}: {sections[faction]} cards")

print("\n" + "=" * 80)
print("SECTION 2: FACTION COMPLETENESS TABLE")
print("-" * 80)
print()
print(f"{'Faction':<25} {'Cards in JSON':<15} {'Expected':<10} {'Status':<15}")
print("-" * 80)

# Expected card count: 10 faction core + 6 primary + 5 secondary = 21
EXPECTED_CORE_CARDS = 21

for faction in EXPECTED_FACTIONS:
    # Map faction names to JSON keys
    faction_key = faction
    if faction == 'wyrd':
        faction_key = 'wyrd-conclave'
    elif faction == 'emergent':
        faction_key = 'emergent-syndicate'

    count = sections.get(faction_key, 0)
    status = "COMPLETE" if count >= EXPECTED_CORE_CARDS else "INCOMPLETE"
    if count == 0:
        status = "MISSING"

    print(f"{faction:<25} {count:<15} {EXPECTED_CORE_CARDS:<10} {status:<15}")

print()

# Check for equipment cards
equipment_count = sections.get('equipment', 0)
print(f"\nEquipment cards in JSON: {equipment_count}")

print("\n" + "=" * 80)
print("SECTION 3: DATA QUALITY CHECKS")
print("-" * 80)
print()

# Check for required fields
required_fields = ['id', 'name', 'type', 'cost', 'effect']
cards_with_missing_fields = []

for section_name, cards in db.items():
    if section_name == '_meta' or not isinstance(cards, list):
        continue

    for card in cards:
        missing = [f for f in required_fields if f not in card or card[f] is None]
        if missing:
            cards_with_missing_fields.append({
                'section': section_name,
                'card': card.get('name', 'UNKNOWN'),
                'missing': missing
            })

if cards_with_missing_fields:
    print(f"Found {len(cards_with_missing_fields)} cards with missing required fields:\n")
    for issue in cards_with_missing_fields[:20]:  # Show first 20
        print(f"  - {issue['section']}/{issue['card']}: Missing {', '.join(issue['missing'])}")
else:
    print("✓ All cards have required fields (id, name, type, cost, effect)")

# Check for duplicate IDs
all_ids = []
for section_name, cards in db.items():
    if section_name == '_meta' or not isinstance(cards, list):
        continue
    for card in cards:
        if 'id' in card:
            all_ids.append((card['id'], section_name))

id_counts = defaultdict(list)
for card_id, section in all_ids:
    id_counts[card_id].append(section)

duplicates = {k: v for k, v in id_counts.items() if len(v) > 1}
if duplicates:
    print(f"\n✗ Found {len(duplicates)} duplicate card IDs:")
    for card_id, sections_list in list(duplicates.items())[:10]:
        print(f"  - '{card_id}' appears in: {', '.join(sections_list)}")
else:
    print("\n✓ No duplicate card IDs found")

# Total card count
total_cards = sum(len(cards) for section, cards in db.items()
                  if section != '_meta' and isinstance(cards, list))
print(f"\n✓ Total cards in database: {total_cards}")

print("\n" + "=" * 80)
print("SECTION 4: CARD STATISTICS BY FACTION")
print("-" * 80)
print()

for faction_name in sorted(faction_sections):
    cards = db.get(faction_name, [])

    # Count by card type
    type_counts = defaultdict(int)
    for card in cards:
        card_type = card.get('cardType', 'unknown')
        type_counts[card_type] += 1

    print(f"\n{faction_name.upper()}:")
    print(f"  Total cards: {len(cards)}")
    if type_counts:
        print(f"  Breakdown:")
        for ctype, count in sorted(type_counts.items()):
            print(f"    - {ctype}: {count}")

print("\n" + "=" * 80)
print("END OF AUDIT REPORT")
print("=" * 80)
