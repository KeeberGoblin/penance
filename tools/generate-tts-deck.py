#!/usr/bin/env python3
"""
Generate Tabletop Simulator deck sheets from Penance card data.

TTS Requirements:
- 10 cards per sheet (2 columns × 5 rows)
- Each card: 750×1050 pixels
- Sheet size: 1500×5250 pixels
- Format: PNG (exported from SVG)

Usage:
    python generate-tts-deck.py --faction church --output church-deck.svg
"""

import xml.etree.ElementTree as ET
from typing import List, Dict

# Standard TTS deck sheet dimensions
CARD_WIDTH = 750
CARD_HEIGHT = 1050
CARDS_PER_ROW = 2
CARDS_PER_COLUMN = 5
CARDS_PER_SHEET = 10

SHEET_WIDTH = CARD_WIDTH * CARDS_PER_ROW
SHEET_HEIGHT = CARD_HEIGHT * CARDS_PER_COLUMN


def create_card_svg(card_data: Dict, x: int, y: int) -> str:
    """Generate SVG markup for a single card at given position."""

    # Extract card data
    name = card_data.get('name', '[CARD NAME]')
    card_type = card_data.get('type', 'UNKNOWN').upper()
    cost = card_data.get('cost', 0)
    initiative = card_data.get('initiative', '—')
    range_text = card_data.get('range', 'Self')
    effect = card_data.get('effect', '')
    damage = card_data.get('damage', None)
    heat = card_data.get('heat', None)
    keywords = card_data.get('keywords', [])
    quote = card_data.get('quote', '')

    # Build keywords string
    keywords_str = ' • '.join([k.upper() for k in keywords[:3]])

    # Build effect text with damage and heat
    effect_parts = [f'<strong style="color: #ffffff;">EFFECT:</strong>']
    effect_parts.append(f'<p style="margin: 10px 0;">{effect}</p>')

    if damage:
        effect_parts.append(f'<p style="margin: 10px 0; color: #8b0000;"><strong>DAMAGE:</strong> {damage}</p>')

    if heat:
        effect_parts.append(f'<p style="margin: 10px 0; color: #666666;"><strong>HEAT:</strong> {heat}</p>')

    effect_html = '\n'.join(effect_parts)

    return f'''
  <g transform="translate({x}, {y})">
    <!-- Background -->
    <rect class="card-bg" width="{CARD_WIDTH}" height="{CARD_HEIGHT}"/>

    <!-- Border -->
    <rect class="card-border" x="10" y="10" width="{CARD_WIDTH-20}" height="{CARD_HEIGHT-20}"/>

    <!-- Header Section -->
    <rect class="header-bg" x="20" y="20" width="{CARD_WIDTH-40}" height="120"/>
    <line class="accent-gold" x1="20" y1="140" x2="{CARD_WIDTH-20}" y2="140"/>

    <!-- Card Name -->
    <text class="text-title" x="{CARD_WIDTH/2}" y="75" text-anchor="middle">{name.upper()}</text>

    <!-- Card Type -->
    <text class="text-type" x="{CARD_WIDTH/2}" y="120" text-anchor="middle">{card_type}</text>

    <!-- Cost Circle -->
    <circle cx="{CARD_WIDTH-70}" cy="80" r="50" fill="#1a1a1a" stroke="#d4af37" stroke-width="4"/>
    <text class="text-cost" x="{CARD_WIDTH-70}" y="100" text-anchor="middle">{cost}</text>
    <text class="text-keywords" x="{CARD_WIDTH-70}" y="125" text-anchor="middle">SP</text>

    <!-- Initiative Badge -->
    <rect x="30" y="30" width="100" height="60" fill="#1a1a1a" stroke="#ffffff" stroke-width="2"/>
    <text class="text-keywords" x="80" y="55" text-anchor="middle">INIT</text>
    <text class="text-cost" x="80" y="85" text-anchor="middle" style="font-size: 32px;">{initiative}</text>

    <!-- Divider -->
    <line class="accent-line" x1="30" y1="160" x2="{CARD_WIDTH-30}" y2="160"/>

    <!-- Effect Text -->
    <foreignObject x="40" y="180" width="{CARD_WIDTH-80}" height="600">
      <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Courier New', monospace; font-size: 20px; color: #cccccc; line-height: 1.5;">
        <p style="margin: 0 0 15px 0;"><strong style="color: #ffffff;">RANGE:</strong> {range_text}</p>
        {effect_html}
      </div>
    </foreignObject>

    <!-- Keywords -->
    <rect x="30" y="800" width="{CARD_WIDTH-60}" height="60" fill="#1a1a1a" stroke="#666666" stroke-width="2"/>
    <text class="text-keywords" x="{CARD_WIDTH/2}" y="838" text-anchor="middle">{keywords_str}</text>

    <!-- Divider -->
    <line class="accent-line" x1="30" y1="880" x2="{CARD_WIDTH-30}" y2="880"/>

    <!-- Flavor Text -->
    <foreignObject x="50" y="900" width="{CARD_WIDTH-100}" height="120">
      <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Courier New', monospace; font-size: 17px; color: #666666; font-style: italic; text-align: center; line-height: 1.4;">
        <p style="margin: 0;">"{quote}"</p>
      </div>
    </foreignObject>

    <!-- Footer -->
    <text class="text-keywords" x="{CARD_WIDTH/2}" y="1030" text-anchor="middle" style="font-size: 14px;">PENANCE: ABSOLUTION THROUGH STEEL</text>
  </g>
'''


def create_deck_sheet(cards: List[Dict], sheet_number: int = 1) -> str:
    """Generate a complete TTS deck sheet SVG."""

    svg_header = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{SHEET_WIDTH}" height="{SHEET_HEIGHT}" viewBox="0 0 {SHEET_WIDTH} {SHEET_HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .card-bg {{ fill: #000000; }}
      .card-border {{ fill: none; stroke: #ffffff; stroke-width: 4; }}
      .header-bg {{ fill: #1a1a1a; }}
      .text-title {{ fill: #ffffff; font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; text-transform: uppercase; }}
      .text-type {{ fill: #8b0000; font-family: 'Courier New', monospace; font-size: 18px; font-weight: bold; text-transform: uppercase; }}
      .text-cost {{ fill: #d4af37; font-family: 'Courier New', monospace; font-size: 48px; font-weight: bold; }}
      .text-body {{ fill: #cccccc; font-family: 'Courier New', monospace; font-size: 22px; }}
      .text-keywords {{ fill: #666666; font-family: 'Courier New', monospace; font-size: 16px; text-transform: uppercase; }}
      .text-flavor {{ fill: #666666; font-family: 'Courier New', monospace; font-size: 18px; font-style: italic; }}
      .accent-line {{ fill: none; stroke: #8b0000; stroke-width: 2; }}
      .accent-gold {{ fill: none; stroke: #d4af37; stroke-width: 3; }}
    </style>
  </defs>

  <!-- Sheet {sheet_number} -->
'''

    card_svgs = []
    for i, card in enumerate(cards[:CARDS_PER_SHEET]):
        row = i // CARDS_PER_ROW
        col = i % CARDS_PER_ROW
        x = col * CARD_WIDTH
        y = row * CARD_HEIGHT
        card_svgs.append(create_card_svg(card, x, y))

    svg_footer = '</svg>'

    return svg_header + '\n'.join(card_svgs) + svg_footer


# Example card data for Church of Absolution
CHURCH_CARDS = [
    {
        'name': 'Blood Offering',
        'type': 'Gambit',
        'cost': 0,
        'initiative': '[1]',
        'range': 'Self',
        'effect': 'Discard 2 cards from the top of your deck. Your next attack this turn: +3 damage and ignore 1 Defense.',
        'keywords': ['gambit', 'self-harm', 'buff'],
        'quote': 'Pain purifies. Blood absolves.'
    },
    {
        'name': 'Faithful Thrust',
        'type': 'Attack',
        'cost': 2,
        'initiative': '[2]',
        'range': 'Melee (Range 1)',
        'effect': 'Deal 4 damage. If attacking from rear arc: +2 damage.',
        'damage': '4 (+2 from rear)',
        'keywords': ['attack', 'melee', 'positioning'],
        'quote': 'Strike true. Strike hard. Strike until forgiven.'
    },
    {
        'name': 'Brace for Impact',
        'type': 'Defense',
        'cost': 0,
        'initiative': '[—]',
        'range': 'Self',
        'effect': 'Reactive. Play when targeted by an attack. Reduce the next instance of damage you take this turn by 2.',
        'keywords': ['reactive', 'defense'],
        'quote': 'Stand firm.'
    },
    {
        'name': 'Desperate Lunge',
        'type': 'Movement',
        'cost': 1,
        'initiative': '[1]',
        'range': 'Self',
        'effect': 'Move up to 2 hexes in any direction. You may rotate once during this movement.',
        'heat': '+1',
        'keywords': ['movement', 'basic'],
        'quote': 'Speed is survival.'
    },
    {
        'name': 'Emergency Vent',
        'type': 'Heat Management',
        'cost': 2,
        'initiative': '[2]',
        'range': 'Self',
        'effect': 'Remove 3 Heat. Draw 1 card.',
        'heat': '-3',
        'keywords': ['heat', 'utility'],
        'quote': 'Breathe. Reset. Continue.'
    },
]


def load_cards_from_database(faction_name: str) -> List[Dict]:
    """Load cards from complete-card-data.json for a specific faction."""
    import json
    import os

    db_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'cards', 'complete-card-data.json')

    if not os.path.exists(db_path):
        print(f"⚠️  Card database not found at: {db_path}")
        print("   Using sample cards instead.")
        return CHURCH_CARDS

    with open(db_path, 'r') as f:
        data = json.load(f)

    # Map faction names to database keys
    faction_map = {
        'church': 'church',
        'dwarves': 'dwarves',
        'elves': 'elves',
        'ossuarium': 'ossuarium',
        'wyrd': 'wyrd-conclave',
        'emergent': 'emergent',
        'nomads': 'nomads',
        'exchange': 'exchange',
        'crucible': 'crucible',
        'vestige': 'vestige-bloodlines'
    }

    faction_key = faction_map.get(faction_name.lower())
    if not faction_key:
        print(f"⚠️  Unknown faction: {faction_name}")
        print(f"   Available: {', '.join(faction_map.keys())}")
        return CHURCH_CARDS

    # Database has factions at root level, not under "factions" key
    faction_cards = data.get(faction_key, [])

    if not faction_cards:
        print(f"⚠️  No cards found for faction: {faction_name}")
        print(f"   Available keys in database: {', '.join([k for k in data.keys() if k != '_meta'])}")
        return CHURCH_CARDS

    # Convert database format to TTS format
    tts_cards = []
    for card in faction_cards:
        tts_card = {
            'name': card.get('name', 'Unknown'),
            'type': card.get('type', 'utility'),
            'cost': card.get('cost', 0),
            'initiative': f"[{card.get('cost', 0)}]",
            'range': card.get('range', 'Self'),
            'effect': card.get('effect', ''),
            'damage': card.get('damage'),
            'keywords': card.get('keywords', []),
            'quote': ''  # Database doesn't have quotes
        }
        tts_cards.append(tts_card)

    return tts_cards


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Generate TTS deck sheets from Penance card data')
    parser.add_argument('--faction', type=str, default='church',
                       help='Faction name (church, dwarves, elves, ossuarium, etc.)')
    parser.add_argument('--database', action='store_true',
                       help='Load cards from complete-card-data.json instead of sample data')
    parser.add_argument('--output', type=str, default=None,
                       help='Output filename (default: {faction}-sample-sheet.svg)')

    args = parser.parse_args()

    # Load cards
    if args.database:
        print(f"📖 Loading {args.faction} cards from database...")
        cards = load_cards_from_database(args.faction)
        print(f"   Found {len(cards)} cards")
    else:
        print("📝 Using sample cards (add --database to use complete-card-data.json)")
        cards = CHURCH_CARDS

    # Generate sheets (10 cards per sheet)
    num_sheets = (len(cards) + CARDS_PER_SHEET - 1) // CARDS_PER_SHEET

    for sheet_num in range(num_sheets):
        start_idx = sheet_num * CARDS_PER_SHEET
        end_idx = min(start_idx + CARDS_PER_SHEET, len(cards))
        sheet_cards = cards[start_idx:end_idx]

        svg_content = create_deck_sheet(sheet_cards, sheet_number=sheet_num + 1)

        if args.output:
            filename = args.output.replace('.svg', f'-sheet{sheet_num + 1}.svg')
        else:
            filename = f'/workspaces/penance/tools/{args.faction}-sample-sheet{sheet_num + 1 if num_sheets > 1 else ""}.svg'

        with open(filename, 'w') as f:
            f.write(svg_content)

        print(f"✅ Generated: {filename}")
        print(f"   Dimensions: {SHEET_WIDTH}×{SHEET_HEIGHT}px")
        print(f"   Cards: {len(sheet_cards)}/{CARDS_PER_SHEET}")

    print(f"\n📊 Total: {len(cards)} cards across {num_sheets} sheet(s)")
    print("\nTo convert to PNG for TTS:")
    print("   1. Open in Inkscape or browser")
    print("   2. Export as PNG at exact dimensions")
    print("   3. Upload to TTS Custom Deck")

# Make functions available for import
__all__ = ['create_card_svg', 'create_deck_sheet', 'CARD_WIDTH', 'CARD_HEIGHT', 'SHEET_WIDTH', 'SHEET_HEIGHT']
