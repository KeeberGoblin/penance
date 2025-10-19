#!/usr/bin/env python3
"""
Comprehensive Card Database Audit
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

# Faction mapping
FACTION_MAP = {
    'church': 'church',
    'dwarves': 'dwarves',
    'elves': 'elves',
    'ossuarium': 'ossuarium',
    'wyrd': 'wyrd-conclave',
    'emergent': 'emergent',
    'nomads': 'nomads',
    'exchange': 'exchange',
    'crucible': 'crucible',
    'vestige-bloodlines': 'vestige-bloodlines'
}

def parse_markdown_cards(md_path):
    """Extract card names from markdown file"""
    if not md_path.exists():
        return []

    content = md_path.read_text()
    cards = []

    # Pattern 1: "### N. CARD NAME" (numbered headers)
    pattern1 = re.compile(r'^###\s+\d+\.\s+(.+?)(?:\s+\(.*?\))?$', re.MULTILINE)
    matches1 = pattern1.findall(content)

    # Pattern 2: "### CARD NAME" (unnumbered headers)
    pattern2 = re.compile(r'^###\s+([A-Z][A-Z\s\'-]+?)(?:\s+\(.*?\))?$', re.MULTILINE)
    matches2 = pattern2.findall(content)

    # Pattern 3: "#### CARD NAME" (equipment)
    pattern3 = re.compile(r'^####\s+([A-Z][A-Z\s\'-]+?)(?:\s+\(.*?\))?$', re.MULTILINE)
    matches3 = pattern3.findall(content)

    # Combine and clean
    all_matches = matches1 + matches2 + matches3
    for match in all_matches:
        # Clean up the card name
        name = match.strip()
        # Skip section headers
        if name in ['FACTION CARDS', 'PRIMARY EQUIPMENT CARDS', 'SECONDARY EQUIPMENT CARDS',
                    'UNIVERSAL CORE', 'FACTION CORE', 'EQUIPMENT CARDS', 'TACTICS',
                    'Light Weapons', 'Medium Weapons', 'Heavy Weapons', 'Ranged Weapons',
                    'Exotic Weapons', 'Light Shields', 'Medium Shields', 'Heavy Shields',
                    'Universal Sigils', 'Faction-Exclusive Sigils']:
            continue
        if len(name) > 3 and name.isupper():
            cards.append(name)

    return cards

def get_json_cards(section_name):
    """Get card names from JSON section"""
    cards = db.get(section_name, [])
    return [card.get('name', '') for card in cards]

print("=" * 100)
print("COMPREHENSIVE CARD DATABASE AUDIT REPORT")
print("=" * 100)
print()

# SECTION 1: Database Overview
print("SECTION 1: DATABASE OVERVIEW")
print("-" * 100)

sections_count = defaultdict(int)
for key, value in db.items():
    if key != '_meta' and isinstance(value, list):
        sections_count[key] = len(value)

print(f"\nTotal sections in JSON: {len(sections_count)}")
print(f"Total cards in JSON: {sum(sections_count.values())}")
print()

print(f"{'Section':<30} {'Card Count':<15}")
print("-" * 50)
for section in sorted(sections_count.keys()):
    print(f"{section:<30} {sections_count[section]:<15}")

# SECTION 2: Faction Completeness
print("\n" + "=" * 100)
print("SECTION 2: FACTION COMPLETENESS TABLE")
print("-" * 100)
print()

# Expected: 10 faction core (or 6 mandatory) + 6 primary + 5 secondary = 21 total (or 11-17 if only some equipment)
print(f"{'Faction':<25} {'JSON Cards':<12} {'MD Cards':<12} {'Status':<20} {'Notes':<30}")
print("-" * 100)

markdown_base = Path('/workspaces/penance/docs/factions')
missing_in_json = {}
extra_in_json = {}

for faction_dir, json_key in FACTION_MAP.items():
    md_path = markdown_base / faction_dir / 'deck-equipment-system.md'

    # Get cards from markdown
    md_cards = parse_markdown_cards(md_path)

    # Get cards from JSON
    json_cards = get_json_cards(json_key)

    # Find differences
    md_set = set(c.lower() for c in md_cards)
    json_set = set(c.lower() for c in json_cards)

    missing = md_set - json_set
    extra = json_set - md_set

    if missing:
        missing_in_json[faction_dir] = list(missing)
    if extra:
        extra_in_json[faction_dir] = list(extra)

    status = "COMPLETE" if not missing else f"MISSING {len(missing)}"
    notes = ""

    if not md_path.exists():
        notes = "NO MARKDOWN FILE"
        status = "N/A"

    print(f"{faction_dir:<25} {len(json_cards):<12} {len(md_cards):<12} {status:<20} {notes:<30}")

# SECTION 3: Missing Cards Detail
print("\n" + "=" * 100)
print("SECTION 3: MISSING CARDS (In Markdown but NOT in JSON)")
print("-" * 100)
print()

if missing_in_json:
    total_missing = sum(len(cards) for cards in missing_in_json.values())
    print(f"Total missing cards: {total_missing}")
    print()

    for faction, cards in sorted(missing_in_json.items()):
        print(f"\n{faction.upper()} ({len(cards)} missing):")
        for card in sorted(cards):
            print(f"  - {card.title()}")
else:
    print("✓ No missing cards found - JSON contains all markdown cards!")

# SECTION 4: Extra Cards in JSON
print("\n" + "=" * 100)
print("SECTION 4: EXTRA CARDS (In JSON but NOT in Markdown)")
print("-" * 100)
print()

if extra_in_json:
    total_extra = sum(len(cards) for cards in extra_in_json.values())
    print(f"Total extra cards: {total_extra}")
    print()

    for faction, cards in sorted(extra_in_json.items()):
        print(f"\n{faction.upper()} ({len(cards)} extra):")
        for card in sorted(cards):
            print(f"  - {card.title()}")
else:
    print("✓ No extra cards found - JSON matches markdown exactly!")

# SECTION 5: Data Quality Issues
print("\n" + "=" * 100)
print("SECTION 5: DATA QUALITY ISSUES")
print("-" * 100)
print()

issues = []

# Check for missing required fields
for section_name, cards in db.items():
    if section_name == '_meta' or not isinstance(cards, list):
        continue

    for card in cards:
        # Required fields
        if not card.get('name'):
            issues.append(f"{section_name}: Card with ID '{card.get('id', 'UNKNOWN')}' has no name")
        if card.get('cost') is None:
            issues.append(f"{section_name}/{card.get('name', 'UNKNOWN')}: Missing 'cost' field")
        if not card.get('effect'):
            issues.append(f"{section_name}/{card.get('name', 'UNKNOWN')}: Missing 'effect' field")
        if not card.get('type'):
            issues.append(f"{section_name}/{card.get('name', 'UNKNOWN')}: Missing 'type' field")

# Check for duplicate IDs
all_ids = defaultdict(list)
for section_name, cards in db.items():
    if section_name == '_meta' or not isinstance(cards, list):
        continue
    for card in cards:
        if 'id' in card:
            all_ids[card['id']].append(f"{section_name}/{card.get('name', 'UNKNOWN')}")

duplicates = {k: v for k, v in all_ids.items() if len(v) > 1}
for card_id, locations in duplicates.items():
    issues.append(f"Duplicate ID '{card_id}' found in: {', '.join(locations)}")

if issues:
    print(f"Found {len(issues)} data quality issues:\n")
    for issue in issues[:30]:  # Show first 30
        print(f"  ✗ {issue}")
else:
    print("✓ No data quality issues found!")

# SECTION 6: Recommendations
print("\n" + "=" * 100)
print("SECTION 6: RECOMMENDATIONS (Priority Order)")
print("-" * 100)
print()

print("Based on the audit, here are recommended actions:\n")

priority_order = []

# Priority 1: Factions with least cards
for faction, json_key in FACTION_MAP.items():
    card_count = sections_count.get(json_key, 0)
    if card_count < 21:
        priority_order.append((faction, card_count, 21 - card_count))

priority_order.sort(key=lambda x: x[1])  # Sort by current count (least first)

print("PRIORITY 1: Complete Incomplete Factions")
for i, (faction, current, needed) in enumerate(priority_order, 1):
    md_path = markdown_base / faction / 'deck-equipment-system.md'
    if md_path.exists():
        print(f"  {i}. {faction.upper()}: Add {needed} cards (currently {current}/21)")
    else:
        print(f"  {i}. {faction.upper()}: Create markdown file first, then add {needed} cards")

print("\nPRIORITY 2: Add Primary Equipment Cards (6 per faction)")
print("  - These should include faction-specific equipment")
print("  - Each faction needs 6 'primary' equipment cards")

print("\nPRIORITY 3: Add Secondary Equipment Cards (5 per faction)")
print("  - Universal equipment accessible to all factions")
print("  - Each faction needs 5 'secondary' equipment cards")

print("\nPRIORITY 4: Cross-Reference Equipment Pool")
print("  - Verify equipment cards match /docs/reference/equipment-pool-complete.md")
print("  - Ensure stats (cost, range, damage) are identical between JSON and markdown")

print("\n" + "=" * 100)
print("END OF COMPREHENSIVE AUDIT REPORT")
print("=" * 100)
