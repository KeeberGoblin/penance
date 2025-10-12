#!/usr/bin/env python3
"""
Generate Dwarven Clans TTS deck sheet.
"""

# Import the deck generation function
import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import after path is set
exec(open('generate-tts-deck.py').read())

# Dwarven Clans sample cards
DWARVEN_CARDS = [
    {
        'name': 'Crushing Blow',
        'type': 'Attack',
        'cost': 2,
        'initiative': '[2]',
        'range': 'Melee (Range 1)',
        'effect': 'Deal 5 damage. Armor-Piercing: Ignore all Defense buffs and shields.',
        'damage': '5 (Armor-Piercing)',
        'keywords': ['attack', 'melee', 'armor-piercing'],
        'quote': 'Stone breaks all.'
    },
    {
        'name': 'Rune of Protection',
        'type': 'Defense',
        'cost': 1,
        'initiative': '[3]',
        'range': 'Self',
        'effect': 'Gain 1 Rune Counter. At 3 Rune Counters: Reduce all damage taken by 3 until counters are spent.',
        'keywords': ['defense', 'rune', 'buff'],
        'quote': 'The old ways endure.'
    },
    {
        'name': 'Unbreakable',
        'type': 'Defense',
        'cost': 0,
        'initiative': '[—]',
        'range': 'Self',
        'effect': 'Reactive. When you take damage that would destroy a component: Prevent that Component Damage. Gain 1 Heat. (Once per turn)',
        'heat': '+1',
        'keywords': ['reactive', 'defense', 'durability'],
        'quote': 'Dwarven steel does not yield.'
    },
    {
        'name': 'Forge Fury',
        'type': 'Gambit',
        'cost': 1,
        'initiative': '[1]',
        'range': 'Self',
        'effect': 'Spend all Rune Counters. Your next attack this turn: +2 damage per Rune Counter spent.',
        'keywords': ['gambit', 'rune', 'buff'],
        'quote': 'Channel the forge. Strike like thunder.'
    },
    {
        'name': 'Stone Endurance',
        'type': 'Passive',
        'cost': 0,
        'initiative': '[—]',
        'range': 'Self',
        'effect': 'Passive. Your deck has 32 cards instead of 30 (includes 2 extra Universal Core cards). Dwarven resilience.',
        'keywords': ['passive', 'durability', 'racial'],
        'quote': 'We are the mountain. We do not fall.'
    },
]


if __name__ == '__main__':
    svg_content = create_deck_sheet(DWARVEN_CARDS, sheet_number=1)

    with open('/workspaces/penance/tools/dwarven-sample-sheet.svg', 'w') as f:
        f.write(svg_content)

    print("✅ Generated: dwarven-sample-sheet.svg")
    print(f"   Cards: {len(DWARVEN_CARDS)}/10")
    print("   Faction: Dwarven Clans")
