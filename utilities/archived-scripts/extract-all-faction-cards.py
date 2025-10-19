#!/usr/bin/env python3
"""
Extract All Faction Cards from deck-equipment-system.md files
Generates structured JSON data for card database
"""

import json
import re
from pathlib import Path

def extract_faction_cards(faction_file_path, faction_name):
    """Extract faction cards from a deck-equipment-system.md file"""
    with open(faction_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the FACTION CARDS section
    match = re.search(r'## FACTION CARDS.*?\n(.*?)(?=\n## |$)', content, re.DOTALL)
    if not match:
        print(f"  ⚠️ No FACTION CARDS section found in {faction_name}")
        return []

    cards_section = match.group(1)

    # Extract individual cards (they start with ### N. Card Name)
    card_pattern = r'###\s+\d+\.\s+(.+?)\n(.*?)(?=###\s+\d+\.|$)'
    card_matches = re.finditer(card_pattern, cards_section, re.DOTALL)

    cards = []
    for card_match in card_matches:
        card_name = card_match.group(1).strip()
        card_body = card_match.group(2).strip()

        # Extract card properties
        card = {
            'id': card_name.lower().replace(' ', '-').replace("'", ''),
            'name': card_name,
            'cardType': 'faction'
        }

        # Extract Type
        type_match = re.search(r'-\s+\*\*Type\*\*:\s+(.+)', card_body)
        if type_match:
            card['type'] = type_match.group(1).strip()

        # Extract Cost
        cost_match = re.search(r'-\s+\*\*Cost\*\*:\s+(.+)', card_body)
        if cost_match:
            cost_str = cost_match.group(1).strip()
            # Parse SP cost or special costs (Forge tokens, Credits, etc.)
            if 'SP' in cost_str:
                sp_num = re.search(r'(\d+)\s*SP', cost_str)
                if sp_num:
                    card['cost'] = int(sp_num.group(1))
            else:
                card['cost'] = cost_str  # Store as string for special costs

        # Extract Range
        range_match = re.search(r'-\s+\*\*Range\*\*:\s+(.+)', card_body)
        if range_match:
            card['range'] = range_match.group(1).strip()

        # Extract Effect
        effect_match = re.search(r'-\s+\*\*Effect\*\*:\s+(.+?)(?=\n-\s+\*\*|$)', card_body, re.DOTALL)
        if effect_match:
            card['effect'] = effect_match.group(1).strip()

        # Extract Keywords
        keywords_match = re.search(r'-\s+\*\*Keywords\*\*:\s+(.+)', card_body)
        if keywords_match:
            keywords_str = keywords_match.group(1).strip()
            card['keywords'] = [k.strip() for k in keywords_str.split(',')]
        else:
            card['keywords'] = [faction_name.lower()]

        # Extract Lore
        lore_match = re.search(r'-\s+\*\*Lore\*\*:\s+"(.+?)"', card_body)
        if lore_match:
            card['lore'] = lore_match.group(1).strip()

        # Add faction tag
        if faction_name.lower() not in card['keywords']:
            card['keywords'].append(faction_name.lower())

        card['cardCount'] = 1  # Default, can be adjusted

        cards.append(card)

    return cards

def main():
    print("🃏 Extracting faction cards from all deck-equipment-system.md files...")
    print()

    # Define factions to extract
    factions = {
        'crucible': 'docs/factions/crucible/deck-equipment-system.md',
        'emergent': 'docs/factions/emergent/deck-equipment-system.md',
        'exchange': 'docs/factions/exchange/deck-equipment-system.md',
        'vestige-bloodlines': 'docs/factions/vestige-bloodlines/deck-equipment-system.md'
    }

    all_faction_data = {}

    for faction_name, file_path in factions.items():
        print(f"📄 Processing {faction_name}...")

        if not Path(file_path).exists():
            print(f"  ❌ File not found: {file_path}")
            continue

        cards = extract_faction_cards(file_path, faction_name)

        if cards:
            all_faction_data[faction_name] = cards
            print(f"  ✅ Extracted {len(cards)} cards")
        else:
            print(f"  ⚠️ No cards extracted")
        print()

    # Save to JSON
    output_file = 'utilities/extracted-faction-cards.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_faction_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved extracted cards to {output_file}")
    print()
    print("=== SUMMARY ===")
    for faction, cards in all_faction_data.items():
        print(f"  {faction}: {len(cards)} cards")
    print()
    print(f"Total factions: {len(all_faction_data)}")
    print(f"Total cards: {sum(len(cards) for cards in all_faction_data.values())}")

if __name__ == '__main__':
    main()
