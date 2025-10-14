#!/usr/bin/env python3
"""
Rebuild Penance Card Database v3.0
- Add cardType field to all cards
- Balance Church to 6 core faction cards
- Create tactics section for targeting/accuracy cards
- Add v3.0 optional cards (Taint Exploitation, Grit-related)
- Add support_units section
"""

import json
import sys

def add_card_type_to_cards(cards, card_type):
    """Add cardType field to a list of cards"""
    for card in cards:
        card['cardType'] = card_type
    return cards

def main():
    print("Loading original card database...")
    with open('/workspaces/penance/docs/cards/complete-card-data.json', 'r') as f:
        old_db = json.load(f)

    print("Building new v3.0 card database structure...")

    new_db = {
        "_meta": {
            "version": "3.0",
            "lastUpdated": "2025-10-14",
            "description": "Complete Penance card database with v3.0 mechanics"
        }
    }

    # =================================================================
    # UNIVERSAL CARDS (10 cards) - add cardType: "core"
    # =================================================================
    print("Processing universal cards...")
    new_db['universal'] = add_card_type_to_cards(old_db['universal'], 'core')

    # =================================================================
    # CHURCH CARDS - Balance from 13 to 6 core cards
    # =================================================================
    print("Balancing Church faction cards...")

    # Keep these 6 as core Church faction cards:
    church_core_ids = [
        'blood-offering',           # Self-harm buff
        'martyrdom-protocol',       # Ally protection
        'righteous-fury',          # Vengeance scaling
        'consecrated-ground',      # Zone healing
        'last-rites',              # Death trigger
        'righteous-wrath'          # Auto-hit attack
    ]

    church_core = []
    church_tactics = []  # Will go in tactics section

    for card in old_db['church']:
        if card['id'] in church_core_ids:
            card['cardType'] = 'faction'
            church_core.append(card)
        elif card['id'] in ['divine-guidance', 'martyrdoms-certainty', 'zealots-focus']:
            # These are targeting/accuracy cards - move to tactics
            card['cardType'] = 'tactic'
            if 'slot' in card:
                del card['slot']  # Remove equipment slot marker
            church_tactics.append(card)
        elif card['id'] == 'divine-judgment-revised':
            # Skip the revised version - it's a duplicate
            continue
        # Skip other cards (confession-under-duress, point-blank-execution, original divine-judgment)

    new_db['church'] = church_core
    print(f"  Church core cards: {len(church_core)}")
    print(f"  Church tactics moved: {len(church_tactics)}")

    # =================================================================
    # DWARVES, OSSUARIUM, ELVES - add cardType: "faction"
    # =================================================================
    print("Processing other faction cards...")
    new_db['dwarves'] = add_card_type_to_cards(old_db['dwarves'], 'faction')
    new_db['ossuarium'] = add_card_type_to_cards(old_db['ossuarium'], 'faction')
    new_db['elves'] = add_card_type_to_cards(old_db['elves'], 'faction')

    # =================================================================
    # EQUIPMENT - add cardType: "equipment" to all items
    # =================================================================
    print("Processing equipment...")
    new_db['equipment'] = old_db['equipment']

    # Add cardType to all equipment items
    for category_name, items in new_db['equipment'].items():
        for item in items:
            item['cardType'] = 'equipment'
            # Also add cardType to individual cards within equipment
            if 'cards' in item:
                for card in item['cards']:
                    card['cardType'] = 'equipment'

    # =================================================================
    # TACTICS - New section for targeting/accuracy/buff cards
    # =================================================================
    print("Creating tactics section...")
    new_db['tactics'] = {
        "church": church_tactics,
        "dwarves": [],  # To be filled with future cards
        "ossuarium": [],
        "elves": [],
        "universal": []
    }

    # =================================================================
    # V3.0 OPTIONAL CARDS - New section for Taint/Grit mechanics
    # =================================================================
    print("Creating v3.0 optional cards...")

    new_db['v3_optional'] = {
        "taint_exploitation": [
            {
                "id": "tainted-fury",
                "name": "Tainted Fury",
                "cardType": "v3_optional",
                "type": "gambit",
                "cost": 0,
                "range": "Self",
                "effect": "Spend 2 Taint Markers: Your next attack this turn deals +2 damage. Gain 1 Heat.",
                "taintCost": 2,
                "heat": "+1",
                "keywords": ["taint", "self-exploit", "gambit"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "ignore-pain",
                "name": "Ignore Pain",
                "cardType": "v3_optional",
                "type": "reactive-defense",
                "cost": 0,
                "range": "Self",
                "effect": "Spend 3 Taint Markers: Reduce next damage taken by 3 (before Defense roll). Gain 1 Heat.",
                "taintCost": 3,
                "heat": "+1",
                "keywords": ["taint", "self-exploit", "reactive"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "void-step",
                "name": "Void Step",
                "cardType": "v3_optional",
                "type": "movement",
                "cost": 0,
                "range": "Self",
                "effect": "Spend 1 Taint Marker: Move 2 hexes (costs 0 SP). Gain 1 Heat.",
                "taintCost": 1,
                "heat": "+1",
                "keywords": ["taint", "self-exploit", "movement"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "exposed-weakness",
                "name": "Exposed Weakness",
                "cardType": "v3_optional",
                "type": "tactic",
                "cost": 0,
                "range": "Target",
                "effect": "Spend 1 enemy Taint Marker: Gain Advantage on your next attack against that enemy (roll 3 Attack Dice, take 2 highest).",
                "taintCost": 1,
                "keywords": ["taint", "enemy-exploit", "advantage"],
                "faction": "universal",
                "cardCount": 2
            },
            {
                "id": "force-reroll",
                "name": "Force Reroll",
                "cardType": "v3_optional",
                "type": "reactive",
                "cost": 0,
                "range": "Target",
                "effect": "Spend 2 enemy Taint Markers: Force target to reroll up to 2 successful Defense Dice.",
                "taintCost": 2,
                "keywords": ["taint", "enemy-exploit", "reactive"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "heat-spike",
                "name": "Heat Spike",
                "cardType": "v3_optional",
                "type": "debuff",
                "cost": 0,
                "range": "Target",
                "effect": "Spend 1 enemy Taint Marker: Target gains +1 Heat immediately.",
                "taintCost": 1,
                "keywords": ["taint", "enemy-exploit", "debuff"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "taint-overload",
                "name": "Taint Overload",
                "cardType": "v3_optional",
                "type": "attack",
                "cost": 0,
                "range": "Target",
                "effect": "Spend 5 enemy Taint Markers: Target immediately flips 1 Pilot Wound card (neural feedback).",
                "taintCost": 5,
                "keywords": ["taint", "enemy-exploit", "pilot-damage"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "flagellants-zeal-taint",
                "name": "Flagellant's Zeal (Taint)",
                "cardType": "v3_optional",
                "type": "gambit",
                "cost": 2,
                "range": "Self",
                "effect": "Discard 3 cards (self-harm), gain 2 Taint Markers. Gain +2 SP this turn only (temporary burst).",
                "taintGain": 2,
                "keywords": ["taint", "self-harm", "church", "gambit"],
                "faction": "church",
                "cardCount": 1
            },
            {
                "id": "decay-aura",
                "name": "Decay Aura",
                "cardType": "v3_optional",
                "type": "passive",
                "cost": 0,
                "range": "3 hexes",
                "effect": "Enemies within 3 hexes gain +1 Taint per turn (passive corruption radiation).",
                "keywords": ["taint", "passive", "ossuarium", "aura"],
                "faction": "ossuarium",
                "cardCount": 1
            },
            {
                "id": "regeneration-purges-taint",
                "name": "Regeneration Purge",
                "cardType": "v3_optional",
                "type": "utility",
                "cost": 2,
                "range": "Self",
                "effect": "Recover 2 cards from discard pile. Remove 1 Taint Marker.",
                "taintRemoval": 1,
                "keywords": ["taint", "healing", "elves", "nature"],
                "faction": "elves",
                "cardCount": 1
            }
        ],
        "grit_related": [
            {
                "id": "iron-will-training",
                "name": "Iron Will Training",
                "cardType": "v3_optional",
                "type": "passive",
                "cost": 0,
                "range": "N/A",
                "effect": "Once per mission: When you would fail a Grit Check, reroll it. If you still fail, gain +1 Grit permanently (trauma builds character).",
                "keywords": ["grit", "passive", "training"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "grit-your-teeth",
                "name": "Grit Your Teeth",
                "cardType": "v3_optional",
                "type": "reactive",
                "cost": 0,
                "range": "Self",
                "effect": "When you take Pilot Damage: Add +2 to your Grit Check roll for this damage only.",
                "keywords": ["grit", "reactive", "resilience"],
                "faction": "universal",
                "cardCount": 1
            },
            {
                "id": "martyrs-endurance",
                "name": "Martyr's Endurance",
                "cardType": "v3_optional",
                "type": "passive",
                "cost": 0,
                "range": "N/A",
                "effect": "When you use Blood Offering or other self-harm Church cards: Gain +1 to your next Grit Check this mission.",
                "keywords": ["grit", "church", "martyrdom", "passive"],
                "faction": "church",
                "cardCount": 1
            },
            {
                "id": "stone-endurance-boost",
                "name": "Stone Endurance Boost",
                "cardType": "v3_optional",
                "type": "utility",
                "cost": 1,
                "range": "Self",
                "effect": "Until end of mission: +1 to all Grit Checks (not just vs Severe Injuries). Gain 1 Heat.",
                "heat": "+1",
                "keywords": ["grit", "dwarves", "buff", "utility"],
                "faction": "dwarves",
                "cardCount": 1
            }
        ]
    }

    # =================================================================
    # SUPPORT UNITS - New section
    # =================================================================
    print("Creating support units section...")

    new_db['support_units'] = [
        {
            "id": "medic",
            "name": "Field Medic",
            "cardType": "support",
            "type": "support-unit",
            "cost": 2,
            "range": "Adjacent",
            "effect": "Support Unit (1 HP, 0 attack). Action: Adjacent ally recovers 2 cards from discard pile. Can be destroyed by AoE or targeted attacks.",
            "keywords": ["support", "healing", "unit"],
            "faction": "universal",
            "cardCount": 1
        },
        {
            "id": "engineer",
            "name": "Field Engineer",
            "cardType": "support",
            "type": "support-unit",
            "cost": 2,
            "range": "Adjacent",
            "effect": "Support Unit (1 HP, 0 attack). Action: Adjacent ally removes 2 Heat. Can be destroyed by AoE or targeted attacks.",
            "keywords": ["support", "heat-management", "unit"],
            "faction": "universal",
            "cardCount": 1
        },
        {
            "id": "spotter",
            "name": "Spotter",
            "cardType": "support",
            "type": "support-unit",
            "cost": 2,
            "range": "6 hexes",
            "effect": "Support Unit (1 HP, 0 attack). Passive: Allies within 6 hexes ignore Disadvantage from cover. Can be destroyed by AoE or targeted attacks.",
            "keywords": ["support", "accuracy", "unit"],
            "faction": "universal",
            "cardCount": 1
        },
        {
            "id": "confessor-support",
            "name": "Confessor",
            "cardType": "support",
            "type": "support-unit",
            "cost": 3,
            "range": "2 hexes",
            "effect": "Support Unit (2 HP, 0 attack). Passive: Allies within 2 hexes gain +1 to Grit Checks. Can redirect 1 attack per turn to self (martyr).",
            "keywords": ["support", "grit", "church", "unit"],
            "faction": "church",
            "cardCount": 1
        },
        {
            "id": "forge-priest",
            "name": "Forge Priest",
            "cardType": "support",
            "type": "support-unit",
            "cost": 3,
            "range": "Adjacent",
            "effect": "Support Unit (2 HP, 0 attack). Action: Adjacent ally gains 1 Rune Counter. Passive: Remove 1 Heat from adjacent allies at end of round.",
            "keywords": ["support", "dwarves", "rune", "unit"],
            "faction": "dwarves",
            "cardCount": 1
        },
        {
            "id": "bone-servant",
            "name": "Bone Servant",
            "cardType": "support",
            "type": "support-unit",
            "cost": 2,
            "range": "3 hexes",
            "effect": "Support Unit (1 HP, 1 attack). Action: Deal 1 damage to target. Passive: When destroyed, owner recovers 3 cards from discard.",
            "keywords": ["support", "ossuarium", "expendable", "unit"],
            "faction": "ossuarium",
            "cardCount": 1
        },
        {
            "id": "ent-sapling",
            "name": "Ent Sapling",
            "cardType": "support",
            "type": "support-unit",
            "cost": 3,
            "range": "Adjacent",
            "effect": "Support Unit (3 HP, 2 attack). Action: Deal 2 damage to adjacent enemy. Passive: Owner recovers 1 card at start of each round while Ent alive.",
            "keywords": ["support", "elves", "nature", "unit"],
            "faction": "elves",
            "cardCount": 1
        }
    ]

    # =================================================================
    # SAVE NEW DATABASE
    # =================================================================
    print("\nSaving new database...")
    output_path = '/workspaces/penance/docs/cards/complete-card-data.json'

    with open(output_path, 'w') as f:
        json.dump(new_db, f, indent=2)

    print(f"\n✓ Successfully created v3.0 card database!")
    print(f"\nSummary:")
    print(f"  Universal core: {len(new_db['universal'])} cards")
    print(f"  Church faction: {len(new_db['church'])} cards (balanced from 13)")
    print(f"  Dwarves faction: {len(new_db['dwarves'])} cards")
    print(f"  Ossuarium faction: {len(new_db['ossuarium'])} cards")
    print(f"  Elves faction: {len(new_db['elves'])} cards")
    print(f"  Equipment items: {sum(len(items) for items in new_db['equipment'].values())}")
    print(f"  Tactics (all factions): {sum(len(t) for t in new_db['tactics'].values())} cards")
    print(f"  V3.0 Taint cards: {len(new_db['v3_optional']['taint_exploitation'])} cards")
    print(f"  V3.0 Grit cards: {len(new_db['v3_optional']['grit_related'])} cards")
    print(f"  Support Units: {len(new_db['support_units'])} units")

    return 0

if __name__ == '__main__':
    sys.exit(main())
