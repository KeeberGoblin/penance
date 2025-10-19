#!/usr/bin/env python3
"""
Extract Equipment Cards from Faction Markdown Files
====================================================

This script reads faction deck-equipment-system.md files and extracts:
- Primary Weapon cards (6 cards each)
- Secondary Equipment cards (5 cards each)

Outputs JSON format compatible with complete-card-data.json
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Any

# Configuration
FACTIONS = {
    "church": {
        "name": "Church of Absolution",
        "path": "docs/factions/church/deck-equipment-system.md",
        "faction_key": "church",
        "current_cards": 10  # Faction core only
    },
    "dwarves": {
        "name": "Dwarven Forge-Guilds",
        "path": "docs/factions/dwarves/deck-equipment-system.md",
        "faction_key": "dwarves",
        "current_cards": 10
    },
    "elves": {
        "name": "Elven Verdant Covenant",
        "path": "docs/factions/elves/deck-equipment-system.md",
        "faction_key": "elves",
        "current_cards": 10
    },
    "ossuarium": {
        "name": "The Ossuarium",
        "path": "docs/factions/ossuarium/deck-equipment-system.md",
        "faction_key": "ossuarium",
        "current_cards": 10
    },
    "emergent": {
        "name": "Emergent Syndicate",
        "path": "docs/factions/emergent/deck-equipment-system.md",
        "faction_key": "emergent",
        "current_cards": 10
    },
    "nomads": {
        "name": "Nomad Collective",
        "path": "docs/factions/nomads/deck-equipment-system.md",
        "faction_key": "nomads",
        "current_cards": 10
    },
    "exchange": {
        "name": "The Exchange",
        "path": "docs/factions/exchange/deck-equipment-system.md",
        "faction_key": "exchange",
        "current_cards": 10
    },
    "crucible": {
        "name": "Crucible Packs",
        "path": "docs/factions/crucible/deck-equipment-system.md",
        "faction_key": "crucible",
        "current_cards": 10
    },
    "vestige-bloodlines": {
        "name": "Vestige Bloodlines",
        "path": "docs/factions/vestige-bloodlines/deck-equipment-system.md",
        "faction_key": "vestige-bloodlines",
        "current_cards": 10
    }
}

def slugify(text: str) -> str:
    """Convert text to kebab-case ID"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def extract_damage(effect: str) -> str:
    """Extract damage value from effect text"""
    # Look for patterns like "Deal X damage", "X damage", etc.
    patterns = [
        r'Deal (\d+(?:\s*\+\s*\d+)?(?:\s+AoE)?)\s+damage',
        r'(\d+)\s+damage',
        r'Damage:\s*(\d+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, effect, re.IGNORECASE)
        if match:
            return match.group(1)

    return None

def parse_primary_weapon_cards(content: str, faction_key: str) -> List[Dict[str, Any]]:
    """Extract primary weapon cards from markdown content"""
    cards = []

    # Find PRIMARY WEAPON section
    primary_match = re.search(
        r'## PRIMARY WEAPON[:\s]+([^\n]+)\s+\((\d+)\s+cards?\)',
        content,
        re.IGNORECASE
    )

    if not primary_match:
        print(f"  ⚠️  No PRIMARY WEAPON section found for {faction_key}")
        return cards

    weapon_name = primary_match.group(1).strip()
    total_cards = int(primary_match.group(2))

    print(f"  Found PRIMARY WEAPON: {weapon_name} ({total_cards} cards)")

    # Find the PRIMARY WEAPON section content (from ## PRIMARY WEAPON to next ##)
    primary_section_pattern = r'## PRIMARY WEAPON[^\n]+\n(.*?)(?=\n## [A-Z]|$)'
    primary_section_match = re.search(primary_section_pattern, content, re.DOTALL)

    if not primary_section_match:
        print(f"  ⚠️  Could not extract PRIMARY WEAPON section content")
        return cards

    section_content = primary_section_match.group(1)

    # Extract individual card entries - look for ### Card Name (×N)
    card_pattern = re.compile(
        r'###\s+(.+?)\s+\(×(\d+)\)\s*\n'
        r'((?:-\s+\*\*.+?\n)+)',  # Capture all list items
        re.MULTILINE
    )

    for match in card_pattern.finditer(section_content):
        card_name = match.group(1).strip()
        card_count = int(match.group(2))
        list_items = match.group(3)

        # Parse list items
        cost_match = re.search(r'-\s+\*\*Cost\*\*:\s*(.+)', list_items)
        range_match = re.search(r'-\s+\*\*Range\*\*:\s*(.+)', list_items)
        damage_match = re.search(r'-\s+\*\*Damage\*\*:\s*(.+)', list_items)
        effect_match = re.search(r'-\s+\*\*Effect\*\*:\s*(.+?)(?=\n-\s+\*\*|$)', list_items, re.DOTALL)
        keywords_match = re.search(r'-\s+\*\*Keywords\*\*:\s*(.+)', list_items)

        cost = cost_match.group(1).strip() if cost_match else "0 SP"
        range_val = range_match.group(1).strip() if range_match else "Melee (1 hex)"
        damage = damage_match.group(1).strip() if damage_match else None
        effect = effect_match.group(1).strip() if effect_match else ""
        effect = re.sub(r'\s+', ' ', effect)  # Clean up whitespace

        # Extract keywords
        keywords = []
        if keywords_match:
            keyword_str = keywords_match.group(1).strip()
            keywords = [kw.strip() for kw in keyword_str.split(',')]

        # Auto-detect damage if not explicitly provided
        if not damage:
            damage = extract_damage(effect)

        # Parse cost
        cost_num = 0
        cost_match = re.search(r'(\d+)\s*SP', cost)
        if cost_match:
            cost_num = int(cost_match.group(1))

        card_id = slugify(card_name)

        card = {
            "id": f"{card_id}",
            "name": card_name,
            "type": "attack",  # Most primary weapons are attacks
            "cost": cost_num,
            "range": range_val,
            "effect": effect,
            "keywords": keywords if keywords else [faction_key, "primary"],
            "cardCount": card_count,
            "cardType": "primary"
        }

        if damage:
            card["damage"] = damage

        cards.append(card)
        print(f"    ✓ {card_name} (×{card_count})")

    return cards

def parse_secondary_equipment_cards(content: str, faction_key: str) -> List[Dict[str, Any]]:
    """Extract secondary equipment cards from markdown content"""
    cards = []

    # Find SECONDARY EQUIPMENT section
    secondary_match = re.search(
        r'## SECONDARY EQUIPMENT[:\s]+([^\n]+)\s+\((\d+)\s+cards?\)',
        content,
        re.IGNORECASE
    )

    if not secondary_match:
        print(f"  ⚠️  No SECONDARY EQUIPMENT section found for {faction_key}")
        return cards

    equipment_name = secondary_match.group(1).strip()
    total_cards = int(secondary_match.group(2))

    print(f"  Found SECONDARY EQUIPMENT: {equipment_name} ({total_cards} cards)")

    # Find the SECONDARY EQUIPMENT section content (from ## SECONDARY EQUIPMENT to next ##)
    secondary_section_pattern = r'## SECONDARY EQUIPMENT[^\n]+\n(.*?)(?=\n## [A-Z]|$)'
    secondary_section_match = re.search(secondary_section_pattern, content, re.DOTALL)

    if not secondary_section_match:
        print(f"  ⚠️  Could not extract SECONDARY EQUIPMENT section content")
        return cards

    section_content = secondary_section_match.group(1)

    # Extract individual card entries - look for ### Card Name (×N)
    card_pattern = re.compile(
        r'###\s+(.+?)\s+\(×(\d+)\)\s*\n'
        r'((?:-\s+\*\*.+?\n)+)',  # Capture all list items
        re.MULTILINE
    )

    for match in card_pattern.finditer(section_content):
        card_name = match.group(1).strip()
        card_count = int(match.group(2))
        list_items = match.group(3)

        # Parse list items
        cost_match = re.search(r'-\s+\*\*Cost\*\*:\s*(.+)', list_items)
        range_match = re.search(r'-\s+\*\*Range\*\*:\s*(.+)', list_items)
        damage_match = re.search(r'-\s+\*\*Damage\*\*:\s*(.+)', list_items)
        effect_match = re.search(r'-\s+\*\*Effect\*\*:\s*(.+?)(?=\n-\s+\*\*|$)', list_items, re.DOTALL)
        keywords_match = re.search(r'-\s+\*\*Keywords\*\*:\s*(.+)', list_items)

        cost = cost_match.group(1).strip() if cost_match else "0 SP"
        range_val = range_match.group(1).strip() if range_match else "Self"
        damage = damage_match.group(1).strip() if damage_match else None
        effect = effect_match.group(1).strip() if effect_match else ""
        effect = re.sub(r'\s+', ' ', effect)  # Clean up whitespace

        # Extract keywords
        keywords = []
        if keywords_match:
            keyword_str = keywords_match.group(1).strip()
            keywords = [kw.strip() for kw in keyword_str.split(',')]

        # Auto-detect damage if not explicitly provided
        if not damage:
            damage = extract_damage(effect)

        # Determine type based on keywords and effect
        card_type = "utility"
        if "reactive" in effect.lower() or "play when" in effect.lower():
            card_type = "reactive"
        elif damage:
            card_type = "attack"

        # Parse cost
        cost_num = 0
        if "Reactive" in cost or "reactive" in cost.lower():
            cost = "0 SP (Reactive)"
        cost_match = re.search(r'(\d+)\s*SP', cost)
        if cost_match:
            cost_num = int(cost_match.group(1))

        card_id = slugify(card_name)

        card = {
            "id": f"{card_id}",
            "name": card_name,
            "type": card_type,
            "cost": cost if "Reactive" in cost else cost_num,
            "range": range_val,
            "effect": effect,
            "keywords": keywords if keywords else [faction_key, "secondary"],
            "cardCount": card_count,
            "cardType": "secondary"
        }

        if damage:
            card["damage"] = damage

        cards.append(card)
        print(f"    ✓ {card_name} (×{card_count})")

    return cards

def extract_faction_equipment(faction_key: str, faction_info: Dict) -> Dict[str, Any]:
    """Extract all equipment cards for a faction"""
    print(f"\n{'='*60}")
    print(f"Processing: {faction_info['name']}")
    print(f"{'='*60}")

    base_path = Path("/workspaces/penance")
    file_path = base_path / faction_info["path"]

    if not file_path.exists():
        print(f"  ❌ File not found: {file_path}")
        return {"primary": [], "secondary": []}

    content = file_path.read_text(encoding='utf-8')

    primary_cards = parse_primary_weapon_cards(content, faction_key)
    secondary_cards = parse_secondary_equipment_cards(content, faction_key)

    print(f"\n  Summary: {len(primary_cards)} primary weapon cards, {len(secondary_cards)} secondary equipment cards")

    return {
        "faction": faction_key,
        "faction_name": faction_info["name"],
        "primary_cards": primary_cards,
        "secondary_cards": secondary_cards,
        "total_equipment": len(primary_cards) + len(secondary_cards),
        "expected_total": faction_info["current_cards"] + 11  # 10 faction + 6 primary + 5 secondary = 21
    }

def main():
    """Main extraction process"""
    print("="*60)
    print("FACTION EQUIPMENT CARD EXTRACTION")
    print("="*60)

    all_results = {}
    summary = {
        "total_factions": len(FACTIONS),
        "total_primary_cards": 0,
        "total_secondary_cards": 0,
        "factions": {}
    }

    # Extract from each faction
    for faction_key, faction_info in FACTIONS.items():
        result = extract_faction_equipment(faction_key, faction_info)
        all_results[faction_key] = result

        # Update summary
        summary["total_primary_cards"] += len(result["primary_cards"])
        summary["total_secondary_cards"] += len(result["secondary_cards"])
        summary["factions"][faction_key] = {
            "name": faction_info["name"],
            "primary_count": len(result["primary_cards"]),
            "secondary_count": len(result["secondary_cards"]),
            "total_equipment": result["total_equipment"],
            "expected_total": result["expected_total"]
        }

    # Save results
    output_file = Path("/workspaces/penance/utilities/extracted-equipment-cards.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"EXTRACTION COMPLETE")
    print(f"{'='*60}")
    print(f"Output saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  Total Factions: {summary['total_factions']}")
    print(f"  Total Primary Weapon Cards: {summary['total_primary_cards']}")
    print(f"  Total Secondary Equipment Cards: {summary['total_secondary_cards']}")
    print(f"  Grand Total: {summary['total_primary_cards'] + summary['total_secondary_cards']} equipment cards")

    # Generate report
    report_file = Path("/workspaces/penance/utilities/equipment-extraction-report.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Equipment Card Extraction Report\n\n")
        f.write(f"**Date**: 2025-10-18\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- **Total Factions Processed**: {summary['total_factions']}\n")
        f.write(f"- **Total Primary Weapon Cards**: {summary['total_primary_cards']}\n")
        f.write(f"- **Total Secondary Equipment Cards**: {summary['total_secondary_cards']}\n")
        f.write(f"- **Grand Total**: {summary['total_primary_cards'] + summary['total_secondary_cards']} cards\n\n")

        f.write("## Faction Breakdown\n\n")
        f.write("| Faction | Primary Weapons | Secondary Equipment | Total | Expected |\n")
        f.write("|---------|-----------------|---------------------|-------|----------|\n")

        for faction_key, faction_data in summary["factions"].items():
            f.write(f"| {faction_data['name']} | {faction_data['primary_count']} | {faction_data['secondary_count']} | {faction_data['total_equipment']} | {faction_data['expected_total']} |\n")

        f.write("\n## Detailed Card Lists\n\n")

        for faction_key, result in all_results.items():
            f.write(f"### {result['faction_name']}\n\n")

            f.write(f"#### Primary Weapons ({len(result['primary_cards'])} cards)\n\n")
            for card in result["primary_cards"]:
                f.write(f"- **{card['name']}** (×{card['cardCount']})\n")
                f.write(f"  - Type: {card['type']}\n")
                f.write(f"  - Cost: {card['cost']}\n")
                f.write(f"  - Range: {card['range']}\n")
                if 'damage' in card:
                    f.write(f"  - Damage: {card['damage']}\n")
                f.write(f"  - Effect: {card['effect'][:100]}...\n\n")

            f.write(f"#### Secondary Equipment ({len(result['secondary_cards'])} cards)\n\n")
            for card in result["secondary_cards"]:
                f.write(f"- **{card['name']}** (×{card['cardCount']})\n")
                f.write(f"  - Type: {card['type']}\n")
                f.write(f"  - Cost: {card['cost']}\n")
                f.write(f"  - Range: {card['range']}\n")
                if 'damage' in card:
                    f.write(f"  - Damage: {card['damage']}\n")
                f.write(f"  - Effect: {card['effect'][:100]}...\n\n")

            f.write("\n---\n\n")

    print(f"\nReport saved to: {report_file}")
    print("\n✨ Extraction complete! Review the JSON and report files.")

if __name__ == "__main__":
    main()
