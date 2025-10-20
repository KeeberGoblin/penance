#!/usr/bin/env python3
"""
Add equipment for weak factions: Emergent, Wyrd, Elves, Ossuarium
"""

import json

# Load existing database
with open('../docs/cards/complete-card-data.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

equipment_items = db.get('equipment_items', [])

print("Fixing equipment for weak factions...")
print(f"Current equipment count: {len(equipment_items)}")

# EMERGENT - Biomass Weapons (adaptive, shape-shifting)
emergent_claw = {
    "name": "BIOMASS CLAW",
    "faction": "emergent",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Light",
    "cards": [
        {
            "name": "Morphic Strike",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Melee",
            "effect": "Adaptive melee attack",
            "cardCount": 2
        },
        {
            "name": "Tendril Lash",
            "type": "Attack",
            "cost": 1,
            "damage": 2,
            "range": "Melee",
            "effect": "Quick biomass strike",
            "cardCount": 2
        }
    ]
}

emergent_launcher = {
    "name": "SPORE LAUNCHER",
    "faction": "emergent",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Medium",
    "cards": [
        {
            "name": "Toxic Spores",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Ranged",
            "effect": "Ranged spore attack",
            "cardCount": 2
        },
        {
            "name": "Spore Burst",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Ranged",
            "effect": "Heavy spore barrage",
            "cardCount": 1
        },
        {
            "name": "Regenerate",
            "type": "Reactive",
            "cost": 1,
            "defense": 1,
            "effect": "Biomass shields",
            "cardCount": 1
        }
    ]
}

# WYRD - Reality Magic (unpredictable, powerful)
wyrd_staff = {
    "name": "REALITY WARPER",
    "faction": "wyrd",
    "totalCards": 4,
    "craftingCost": "4 Scrap",
    "weight": "Medium",
    "cards": [
        {
            "name": "Chaos Bolt",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Ranged",
            "effect": "Unpredictable magic missile",
            "cardCount": 2
        },
        {
            "name": "Reality Rift",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Ranged",
            "effect": "Tear in reality",
            "cardCount": 1
        },
        {
            "name": "Phase Dodge",
            "type": "Reactive",
            "cost": 1,
            "defense": 2,
            "effect": "Shift through reality",
            "cardCount": 1
        }
    ]
}

wyrd_blade = {
    "name": "VOID EDGE",
    "faction": "wyrd",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Light",
    "cards": [
        {
            "name": "Void Strike",
            "type": "Attack",
            "cost": 2,
            "damage": 4,
            "range": "Melee",
            "effect": "Cut through reality",
            "cardCount": 2
        },
        {
            "name": "Shadow Slash",
            "type": "Attack",
            "cost": 1,
            "damage": 2,
            "range": "Melee",
            "effect": "Quick void strike",
            "cardCount": 2
        }
    ]
}

# ELVES - Nature Weapons (precise, elegant)
elves_bow = {
    "name": "HEARTWOOD BOW",
    "faction": "elves",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Light",
    "cards": [
        {
            "name": "Precision Shot",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Ranged",
            "effect": "Accurate arrow",
            "cardCount": 2
        },
        {
            "name": "Volley",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Ranged",
            "effect": "Multiple arrows",
            "cardCount": 1
        },
        {
            "name": "Evasion",
            "type": "Reactive",
            "cost": 0,
            "defense": 1,
            "effect": "Graceful dodge",
            "cardCount": 1
        }
    ]
}

elves_blade = {
    "name": "MOONSILVER BLADE",
    "faction": "elves",
    "totalCards": 4,
    "craftingCost": "4 Scrap",
    "weight": "Light",
    "cards": [
        {
            "name": "Flowing Strike",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Melee",
            "effect": "Elegant melee strike",
            "cardCount": 2
        },
        {
            "name": "Whirlwind Slash",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Melee",
            "effect": "Spinning blade attack",
            "cardCount": 1
        },
        {
            "name": "Parry",
            "type": "Reactive",
            "cost": 1,
            "defense": 2,
            "effect": "Deflect attack",
            "cardCount": 1
        }
    ]
}

# OSSUARIUM - Bone/Death Magic (sustained damage, lifesteal)
ossuarium_scythe = {
    "name": "BONE SCYTHE",
    "faction": "ossuarium",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Medium",
    "cards": [
        {
            "name": "Soul Reap",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Melee",
            "effect": "Harvest souls",
            "cardCount": 2
        },
        {
            "name": "Death Strike",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Melee",
            "effect": "Powerful scythe swing",
            "cardCount": 1
        },
        {
            "name": "Bone Armor",
            "type": "Reactive",
            "cost": 1,
            "defense": 2,
            "effect": "Bone shield",
            "cardCount": 1
        }
    ]
}

ossuarium_staff = {
    "name": "NECROMANCER'S ROD",
    "faction": "ossuarium",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Light",
    "cards": [
        {
            "name": "Death Bolt",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Ranged",
            "effect": "Necrotic missile",
            "cardCount": 2
        },
        {
            "name": "Drain Life",
            "type": "Attack",
            "cost": 2,
            "damage": 2,
            "range": "Ranged",
            "effect": "Steal life force",
            "cardCount": 2
        }
    ]
}

# Add new equipment
new_equipment = [
    emergent_claw,
    emergent_launcher,
    wyrd_staff,
    wyrd_blade,
    elves_bow,
    elves_blade,
    ossuarium_scythe,
    ossuarium_staff
]

equipment_items.extend(new_equipment)
db['equipment_items'] = equipment_items

# Save updated database
with open('../docs/cards/complete-card-data.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"\nAdded {len(new_equipment)} new equipment items:")
for item in new_equipment:
    attack_cards = [c for c in item['cards'] if c['type'] == 'Attack']
    total_dmg = sum(c.get('damage', 0) * c.get('cardCount', 1) for c in attack_cards)
    print(f"  - {item['name']:<25} ({item['faction']:<12}): {len(item['cards'])} cards, {total_dmg} total dmg")

print(f"\nNew equipment count: {len(equipment_items)}")
print("\nDone! Re-run faction balance test to see improvements.")
