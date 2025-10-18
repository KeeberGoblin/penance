#!/usr/bin/env python3
"""
Validate Penance Card Database
Checks for missing fields, inconsistencies, and structural issues
"""

import json
import sys

def validate_database():
    """Validate the complete card database"""
    errors = []
    warnings = []

    print("🔍 Validating Penance card database...")
    print()

    # Load database
    try:
        with open('docs/cards/complete-card-data.json', 'r', encoding='utf-8') as f:
            db = json.load(f)
    except FileNotFoundError:
        print("❌ Error: complete-card-data.json not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON - {e}")
        return False

    # Check metadata
    if '_meta' not in db:
        errors.append("Missing _meta section")
    else:
        meta = db['_meta']
        if 'version' not in meta:
            warnings.append("Missing version in _meta")
        if 'lastUpdated' not in meta:
            warnings.append("Missing lastUpdated in _meta")
        print(f"✅ Metadata: v{meta.get('version', 'unknown')}")

    # Check required sections
    required_sections = ['universal', 'equipment']
    for section in required_sections:
        if section not in db:
            errors.append(f"Missing required section: {section}")
        else:
            print(f"✅ Section '{section}' present")

    # Get factions
    factions = [k for k in db.keys() if k not in ['_meta', 'universal', 'equipment', 'tactics', 'v3_optional', 'support_units']]
    print(f"✅ Found {len(factions)} factions: {', '.join(factions)}")
    print()

    # Validate universal cards
    if 'universal' in db:
        universal = db['universal']
        if len(universal) != 10:
            warnings.append(f"Universal cards should be 10, found {len(universal)}")

        for card in universal:
            validate_card(card, 'universal', errors, warnings)

    # Validate each faction
    for faction in factions:
        cards = db[faction]

        if not isinstance(cards, list):
            errors.append(f"Faction '{faction}' is not a list")
            continue

        if len(cards) == 0:
            errors.append(f"Faction '{faction}' has no cards")
            continue

        # Most factions should have 6-10 cards
        if len(cards) < 6:
            warnings.append(f"Faction '{faction}' has only {len(cards)} cards (expected 6-10)")
        elif len(cards) > 10:
            warnings.append(f"Faction '{faction}' has {len(cards)} cards (expected 6-10)")

        # Validate each card
        for card in cards:
            validate_card(card, faction, errors, warnings)

    # Print results
    print()
    print("=" * 50)
    if errors:
        print(f"❌ {len(errors)} ERRORS FOUND:")
        for err in errors:
            print(f"  • {err}")
    else:
        print("✅ No errors found")

    if warnings:
        print()
        print(f"⚠️  {len(warnings)} WARNINGS:")
        for warn in warnings:
            print(f"  • {warn}")
    else:
        print("✅ No warnings")

    print("=" * 50)
    print()

    # Summary
    if not errors:
        print("✅ DATABASE VALIDATION PASSED")
        print()
        print("Summary:")
        print(f"  Version: {db['_meta'].get('version', 'unknown')}")
        print(f"  Factions: {len(factions)}")
        print(f"  Total faction cards: {sum(len(db[f]) for f in factions)}")
        print(f"  Universal cards: {len(db.get('universal', []))}")
        return True
    else:
        print("❌ DATABASE VALIDATION FAILED")
        return False

def validate_card(card, context, errors, warnings):
    """Validate a single card"""
    if not isinstance(card, dict):
        errors.append(f"{context}: Card is not a dict")
        return

    # Check required fields
    required = ['id', 'name']
    for field in required:
        if field not in card:
            errors.append(f"{context}: Card '{card.get('name', 'unknown')}' missing '{field}'")

    # Check recommended fields
    recommended = ['cardType', 'type', 'cost', 'effect']
    for field in recommended:
        if field not in card:
            warnings.append(f"{context}: Card '{card.get('name', 'unknown')}' missing recommended field '{field}'")

    # Validate keywords
    if 'keywords' in card:
        if not isinstance(card['keywords'], list):
            errors.append(f"{context}: Card '{card.get('name', 'unknown')}' keywords is not a list")

    # Check for duplicate IDs (would need global tracking)
    # This is a simplified check

if __name__ == '__main__':
    success = validate_database()
    sys.exit(0 if success else 1)
