#!/usr/bin/env python3
"""
Add missing equipment for factions that need it
Creates balanced equipment for Nomads, Crucible, Exchange, Bloodlines
"""

import json

# Load existing database
with open('../docs/cards/complete-card-data.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Get current equipment
equipment_items = db.get('equipment_items', [])

print("Adding equipment for underserved factions...")
print(f"Current equipment count: {len(equipment_items)}")

# NOMADS - Desert Raiders (hit-and-run, mobility)
nomads_scimitar = {
    "name": "SAND SCIMITAR",
    "faction": "nomads",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Light",
    "cards": [
        {
            "name": "Desert Strike",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Melee",
            "effect": "Quick melee strike",
            "cardCount": 2
        },
        {
            "name": "Sand Slash",
            "type": "Attack",
            "cost": 1,
            "damage": 2,
            "range": "Melee",
            "effect": "Fast attack",
            "cardCount": 1
        },
        {
            "name": "Mirage Step",
            "type": "Reactive",
            "cost": 1,
            "defense": 1,
            "effect": "Dodge incoming attack",
            "cardCount": 1
        }
    ]
}

nomads_bow = {
    "name": "NOMAD LONGBOW",
    "faction": "nomads",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Medium",
    "cards": [
        {
            "name": "Aimed Shot",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Ranged",
            "effect": "Precise ranged attack",
            "cardCount": 2
        },
        {
            "name": "Quick Shot",
            "type": "Attack",
            "cost": 1,
            "damage": 2,
            "range": "Ranged",
            "effect": "Fast ranged strike",
            "cardCount": 2
        }
    ]
}

# CRUCIBLE - Honor Duels (high-damage, honor-bound)
crucible_blade = {
    "name": "HONOR BLADE",
    "faction": "crucible",
    "totalCards": 4,
    "craftingCost": "4 Scrap",
    "weight": "Medium",
    "cards": [
        {
            "name": "Duel Strike",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Melee",
            "effect": "Honorable melee strike",
            "cardCount": 2
        },
        {
            "name": "Riposte",
            "type": "Reactive",
            "cost": 2,
            "defense": 2,
            "effect": "Parry and counter",
            "cardCount": 1
        },
        {
            "name": "Final Stand",
            "type": "Attack",
            "cost": 4,
            "damage": 5,
            "range": "Melee",
            "effect": "Powerful finishing blow",
            "cardCount": 1
        }
    ]
}

# EXCHANGE - Mercenary Weapons (versatile, balanced)
exchange_rifle = {
    "name": "MERCENARY RIFLE",
    "faction": "exchange",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Medium",
    "cards": [
        {
            "name": "Aimed Fire",
            "type": "Attack",
            "cost": 2,
            "damage": 3,
            "range": "Ranged",
            "effect": "Standard shot",
            "cardCount": 2
        },
        {
            "name": "Suppressing Fire",
            "type": "Attack",
            "cost": 3,
            "damage": 4,
            "range": "Ranged",
            "effect": "Heavy barrage",
            "cardCount": 1
        },
        {
            "name": "Combat Roll",
            "type": "Reactive",
            "cost": 1,
            "defense": 1,
            "effect": "Evasive maneuver",
            "cardCount": 1
        }
    ]
}

# BLOODLINES - Blood Magic (sacrifice HP for damage)
bloodlines_ritual_blade = {
    "name": "BLOODLETTING BLADE",
    "faction": "bloodlines",
    "totalCards": 4,
    "craftingCost": "3 Scrap",
    "weight": "Light",
    "cards": [
        {
            "name": "Blood Strike",
            "type": "Attack",
            "cost": 2,
            "damage": 4,
            "range": "Melee",
            "effect": "Empowered by blood magic",
            "cardCount": 2
        },
        {
            "name": "Crimson Slash",
            "type": "Attack",
            "cost": 1,
            "damage": 3,
            "range": "Melee",
            "effect": "Quick blood-infused strike",
            "cardCount": 2
        }
    ]
}

# Add new equipment
new_equipment = [
    nomads_scimitar,
    nomads_bow,
    crucible_blade,
    exchange_rifle,
    bloodlines_ritual_blade
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
    print(f"  - {item['name']} ({item['faction']}): {len(attack_cards)} attack cards, {total_dmg} total damage")

print(f"\nNew equipment count: {len(equipment_items)}")
print("\nDone! Re-run faction balance test to see improvements.")
