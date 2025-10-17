#!/usr/bin/env python3
"""
Add Wyrd Conclave cards to complete-card-data.json
Extracts from deck-equipment-system.md and updates database
"""

import json
import re
from datetime import datetime

def extract_wyrd_faction_cards():
    """Extract faction cards from Wyrd Conclave deck file"""
    with open('docs/factions/wyrd-conclave/deck-equipment-system.md', 'r') as f:
        content = f.read()

    # Extract faction cards section
    faction_match = re.search(r'## FACTION CARDS.*?\n(.*?)(?=\n## PRIMARY WEAPON)', content, re.DOTALL)
    if not faction_match:
        return []

    faction_section = faction_match.group(1)

    # Pattern to match individual cards
    card_pattern = r'###\s+\d+\.\s+(.+?)\n-\s+\*\*Type\*\*:\s+(.+?)\n-\s+\*\*Cost\*\*:\s+(.+?)\n-\s+\*\*Range\*\*:\s+(.+?)\n(?:-\s+\*\*Damage\*\*:\s+(.+?)\n)?-\s+\*\*Effect\*\*:\s+(.+?)\n-\s+\*\*Keywords\*\*:\s+(.+?)\n-\s+\*\*Lore\*\*:\s+"(.+?)"'

    cards = []
    for match in re.finditer(card_pattern, faction_section, re.DOTALL):
        card = {
            "id": match.group(1).lower().replace(' ', '-'),
            "name": match.group(1),
            "type": match.group(2).lower(),
            "cost": match.group(3),
            "range": match.group(4),
            "effect": match.group(6).strip(),
            "keywords": [k.strip() for k in match.group(7).split(',')],
            "lore": match.group(8),
            "cardCount": 1,
            "cardType": "faction"
        }

        # Add damage if present
        if match.group(5):
            card["damage"] = match.group(5)

        cards.append(card)

    return cards

def extract_wyrd_primary_weapon():
    """Extract primary weapon cards"""
    with open('docs/factions/wyrd-conclave/deck-equipment-system.md', 'r') as f:
        content = f.read()

    # Extract primary weapon section
    weapon_match = re.search(r'## PRIMARY WEAPON:.*?\n(.*?)(?=\n## SECONDARY EQUIPMENT)', content, re.DOTALL)
    if not weapon_match:
        return []

    weapon_section = weapon_match.group(1)

    # Pattern to match weapon cards
    weapon_pattern = r'###\s+(.+?)\s+\(×(\d+)\)\n-\s+\*\*Cost\*\*:\s+(.+?)\n-\s+\*\*Range\*\*:\s+(.+?)\n-\s+\*\*Damage\*\*:\s+(.+?)\n-\s+\*\*Effect\*\*:\s+(.+?)\n-\s+\*\*Keywords\*\*:\s+(.+?)(?=\n\n|$)'

    cards = []
    for match in re.finditer(weapon_pattern, weapon_section, re.DOTALL):
        card = {
            "id": match.group(1).lower().replace(' ', '-'),
            "name": match.group(1),
            "type": "attack",
            "cost": match.group(3),
            "range": match.group(4),
            "damage": match.group(5),
            "effect": match.group(6).strip(),
            "keywords": [k.strip() for k in match.group(7).split(',')],
            "cardCount": int(match.group(2)),
            "cardType": "primary"
        }
        cards.append(card)

    return cards

def extract_wyrd_secondary():
    """Extract secondary equipment cards"""
    with open('docs/factions/wyrd-conclave/deck-equipment-system.md', 'r') as f:
        content = f.read()

    # Extract secondary section
    secondary_match = re.search(r'## SECONDARY EQUIPMENT:.*?\n(.*?)(?=\n## ADDITIONAL FACTION CARDS|$)', content, re.DOTALL)
    if not secondary_match:
        return []

    secondary_section = secondary_match.group(1)

    # Pattern to match secondary cards
    secondary_pattern = r'###\s+(.+?)\s+\(×(\d+)\)\n-\s+\*\*Cost\*\*:\s+(.+?)\n-\s+\*\*Range\*\*:\s+(.+?)\n(?:-\s+\*\*Damage\*\*:\s+(.+?)\n)?-\s+\*\*Effect\*\*:\s+(.+?)\n-\s+\*\*Keywords\*\*:\s+(.+?)(?=\n\n|$)'

    cards = []
    for match in re.finditer(secondary_pattern, secondary_section, re.DOTALL):
        card = {
            "id": match.group(1).lower().replace(' ', '-'),
            "name": match.group(1),
            "type": "utility" if not match.group(5) else "attack",
            "cost": match.group(3),
            "range": match.group(4),
            "effect": match.group(6).strip(),
            "keywords": [k.strip() for k in match.group(7).split(',')],
            "cardCount": int(match.group(2)),
            "cardType": "secondary"
        }

        # Add damage if present
        if match.group(5):
            card["damage"] = match.group(5)

        cards.append(card)

    return cards

def main():
    print("Extracting Wyrd Conclave cards...")

    # Extract all card types
    faction_cards = extract_wyrd_faction_cards()
    primary_cards = extract_wyrd_primary_weapon()
    secondary_cards = extract_wyrd_secondary()

    print(f"✓ Extracted {len(faction_cards)} faction cards")
    print(f"✓ Extracted {len(primary_cards)} primary weapon cards")
    print(f"✓ Extracted {len(secondary_cards)} secondary equipment cards")

    # Combine all cards
    all_wyrd_cards = faction_cards + primary_cards + secondary_cards

    # Load current database
    with open('docs/cards/complete-card-data.json', 'r') as f:
        db = json.load(f)

    # Add Wyrd Conclave cards
    db['wyrd-conclave'] = all_wyrd_cards

    # Update metadata
    db['_meta']['version'] = '3.2'
    db['_meta']['lastUpdated'] = datetime.now().strftime('%Y-%m-%d')
    db['_meta']['description'] = 'Complete Penance card database v3.2 - All 10 factions included (added Wyrd Conclave)'

    # Save updated database
    with open('docs/cards/complete-card-data.json', 'w') as f:
        json.dump(db, f, indent=2)

    print(f"\n✓ Added {len(all_wyrd_cards)} Wyrd Conclave cards to database")
    print(f"✓ Updated version: 3.1 → 3.2")
    print(f"✓ Database now contains {len([k for k in db.keys() if k != '_meta'])} faction groups")
    print("\nDatabase update complete!")

if __name__ == '__main__':
    main()
