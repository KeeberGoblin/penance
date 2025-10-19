"""
Extract equipment items from equipment-pool-complete.md
Groups cards by weapon/shield/accessory name

Version: 1.0
Date: 2025-10-18
"""

import json
import re
from pathlib import Path

# Path setup
REPO_ROOT = Path(__file__).parent.parent
CARD_DB_PATH = REPO_ROOT / "docs" / "cards" / "complete-card-data.json"
EQUIPMENT_MD_PATH = REPO_ROOT / "docs" / "reference" / "equipment-pool-complete.md"

def extract_equipment_items(content):
    """Extract all equipment items (weapons, shields, accessories) from markdown."""
    items = []

    # Pattern to match equipment sections like:
    # #### LONGSWORD
    # **Card Count**: 6 cards
    # **Crafting Cost**: 4 Scrap
    # **Weight**: Medium
    # **Faction Restrictions**: None (Universal)
    #
    # **Cards**:
    # 1. **Slash** (2 SP, Melee): Deal 4 damage
    # 2. **Thrust** (2 SP, Melee): Deal 3 damage...

    item_pattern = r'####\s+([A-Z\s\-\']+)\n(.*?)(?=\n####|\n###|\n##|\Z)'
    item_sections = re.findall(item_pattern, content, re.DOTALL)

    for item_name, item_content in item_sections:
        item_name = item_name.strip()

        # Skip section headers that aren't actual items
        if item_name in ['CATEGORY', 'LIGHT WEAPONS', 'MEDIUM WEAPONS', 'HEAVY WEAPONS']:
            continue

        item = {
            'name': item_name,
            'cards': []
        }

        # Extract metadata
        card_count_match = re.search(r'\*\*Card Count\*\*:\s*(\d+)', item_content)
        if card_count_match:
            item['totalCards'] = int(card_count_match.group(1))

        crafting_match = re.search(r'\*\*Crafting Cost\*\*:\s*(.+)', item_content)
        if crafting_match:
            item['craftingCost'] = crafting_match.group(1).strip()

        weight_match = re.search(r'\*\*Weight\*\*:\s*(.+)', item_content)
        if weight_match:
            item['weight'] = weight_match.group(1).strip()

        faction_match = re.search(r'\*\*Faction Restrictions\*\*:\s*(.+)', item_content)
        if faction_match:
            restrictions = faction_match.group(1).strip()
            if 'None' in restrictions or 'Universal' in restrictions:
                item['faction'] = 'universal'
            else:
                # Extract first faction mentioned
                factions = restrictions.lower().replace('and', ',').split(',')
                item['faction'] = factions[0].strip()
        else:
            item['faction'] = 'universal'

        # Determine category from position in file
        if '## CATEGORY 1: WEAPONS' in content[:content.find(item_name)]:
            item['category'] = 'Weapon'
        elif '## CATEGORY 2: SHIELDS' in content[:content.find(item_name)]:
            item['category'] = 'Shield'
        elif '## CATEGORY 3: ACCESSORIES' in content[:content.find(item_name)]:
            item['category'] = 'Accessory'
        else:
            item['category'] = 'Equipment'

        # Extract individual cards
        cards_section_match = re.search(r'\*\*Cards\*\*:(.*?)(?=\n\n---|\n\n####|\n\n###|\Z)', item_content, re.DOTALL)
        if cards_section_match:
            cards_text = cards_section_match.group(1)

            # Pattern for card lines like: 1. **Slash** (2 SP, Melee): Deal 4 damage
            card_pattern = r'\d+\.\s+\*\*([^*]+)\*\*\s*\(([^)]+)\):\s*(.+?)(?=\n\d+\.|\Z)'
            card_matches = re.findall(card_pattern, cards_text, re.DOTALL)

            for card_name, card_meta, card_effect in card_matches:
                card = {
                    'name': card_name.strip(),
                    'effect': card_effect.strip()
                }

                # Parse metadata (2 SP, Melee, Range 1-4, etc.)
                meta_lower = card_meta.lower()

                # Extract SP cost
                sp_match = re.search(r'(\d+)\s*sp', meta_lower)
                if sp_match:
                    card['cost'] = int(sp_match.group(1))

                # Extract range
                if 'melee' in meta_lower:
                    card['range'] = 'Melee'
                elif 'ranged' in meta_lower:
                    range_match = re.search(r'ranged\s+(\d+-?\d*)', meta_lower)
                    if range_match:
                        card['range'] = f"Ranged {range_match.group(1)}"
                    else:
                        card['range'] = 'Ranged'

                # Extract type
                if 'reactive' in meta_lower or 'reaction' in meta_lower:
                    card['type'] = 'Reactive'
                elif 'utility' in meta_lower:
                    card['type'] = 'Utility'
                elif 'defense' in meta_lower:
                    card['type'] = 'Defense'
                elif 'attack' in meta_lower or card.get('range'):
                    card['type'] = 'Attack'
                else:
                    card['type'] = 'Action'

                # Extract damage
                damage_match = re.search(r'deal\s+(\d+)\s+damage', card['effect'].lower())
                if damage_match:
                    card['damage'] = int(damage_match.group(1))

                item['cards'].append(card)

        # Only add items that have cards
        if item['cards']:
            items.append(item)

    return items

def main():
    """Extract equipment and update card database."""
    print("=" * 60)
    print("Equipment Extractor v1.0")
    print("=" * 60)

    # Read equipment markdown
    print(f"\nReading: {EQUIPMENT_MD_PATH}")
    with open(EQUIPMENT_MD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract equipment items
    equipment_items = extract_equipment_items(content)

    print(f"\nExtracted {len(equipment_items)} equipment items:")
    for item in equipment_items:
        print(f"  - {item['name']} ({item['category']}, {item['faction']}) - {len(item['cards'])} cards")

    # Calculate total cards
    total_cards = sum(len(item['cards']) for item in equipment_items)
    print(f"\nTotal equipment cards: {total_cards}")

    # Load existing card database
    print(f"\nLoading: {CARD_DB_PATH}")
    with open(CARD_DB_PATH, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # Add equipment items (grouped by weapon/shield/accessory)
    db['equipment_items'] = equipment_items

    # Update metadata
    db['_meta']['version'] = '4.1'
    db['_meta']['lastUpdated'] = '2025-10-18'
    db['_meta']['description'] = f"Complete Penance card database v4.1 - All 10 factions (21 cards each) + Universal (10) + Equipment Items ({len(equipment_items)} weapons/shields/accessories, {total_cards} cards) + Special cards (6) + Support Units (39 units, 156 behavior cards)"

    if 'equipmentItems' not in db['_meta']['cardCounts']:
        db['_meta']['cardCounts']['equipmentItems'] = 0

    db['_meta']['cardCounts']['equipmentItems'] = len(equipment_items)

    # Save updated database
    print(f"\nSaving to: {CARD_DB_PATH}")
    with open(CARD_DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 60)
    print("✅ SUCCESS!")
    print(f"   Equipment items added: {len(equipment_items)}")
    print(f"   Total equipment cards: {total_cards}")
    print("=" * 60)

if __name__ == "__main__":
    main()
