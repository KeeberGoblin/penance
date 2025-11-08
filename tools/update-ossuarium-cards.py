#!/usr/bin/env python3
"""
Update Ossuarium cards in complete-card-data.json with Soul Shard system redesign
"""

import json
import sys

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def create_new_ossuarium_cards():
    """Create the new Ossuarium card list with Soul Shard system"""
    return [
        {
            "id": "soul-harvest",
            "name": "Soul Harvest",
            "type": "Attack",
            "cost": 3,
            "damage": 3,
            "range": "Melee",
            "effect": "Deal 3 damage. If this destroys an enemy, gain 3 Soul Shards.",
            "keywords": ["attack", "shard-generation", "execution", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "bone-scythe-swing",
            "name": "Bone Scythe Swing",
            "type": "Attack",
            "cost": 3,
            "damage": 3,
            "range": "Melee",
            "effect": "Deal 3 damage. Basic Ossuarium attack.",
            "keywords": ["attack", "melee", "ossuarium"],
            "cardCount": 2,
            "cardType": "faction"
        },
        {
            "id": "death-grasp",
            "name": "Death Grasp",
            "type": "Attack",
            "cost": 2,
            "damage": 2,
            "range": "Ranged 2-5",
            "effect": "Deal 2 damage at range.",
            "keywords": ["attack", "ranged", "ossuarium"],
            "cardCount": 2,
            "cardType": "faction"
        },
        {
            "id": "siphon-essence",
            "name": "Siphon Essence",
            "type": "Attack",
            "cost": 2,
            "damage": 2,
            "range": "Ranged 2-4",
            "effect": "Deal 2 damage. If this destroys an enemy, gain 2 Soul Shards.",
            "keywords": ["attack", "ranged", "shard-generation", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "necrotic-touch",
            "name": "Necrotic Touch",
            "type": "Attack",
            "cost": 2,
            "damage": 2,
            "range": "Melee",
            "effect": "Deal 2 damage. If this destroys an enemy, gain 4 Soul Shards (execution bonus).",
            "keywords": ["attack", "execution", "shard-generation", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "soul-rend",
            "name": "Soul Rend",
            "type": "Attack",
            "cost": 4,
            "damage": 4,
            "range": "Melee",
            "effect": "Deal 4 damage. On kill, gain 3 Soul Shards.",
            "keywords": ["attack", "powerful", "shard-generation", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "drain-life",
            "name": "Drain Life",
            "type": "Attack",
            "cost": 5,
            "damage": 5,
            "range": "Ranged 2-6",
            "effect": "Deal 5 damage at long range. On kill, gain 4 Soul Shards.",
            "keywords": ["attack", "ranged", "powerful", "shard-generation", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "bone-scythe-reap",
            "name": "Bone Scythe Reap",
            "type": "Attack",
            "cost": 4,
            "damage": "3 primary, 2 AoE",
            "range": "Melee AoE",
            "effect": "Deal 3 damage to primary target and 2 damage to all adjacent enemies. For each enemy destroyed, gain 2 Soul Shards.",
            "keywords": ["attack", "aoe", "shard-generation", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "corpse-explosion",
            "name": "Corpse Explosion",
            "type": "Attack",
            "cost": 3,
            "damage": "3 AoE",
            "range": "Ranged 2-4 AoE",
            "effect": "Deal 3 damage to target hex and all adjacent hexes.",
            "keywords": ["attack", "aoe", "explosive", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "salvage-protocol",
            "name": "Salvage Protocol",
            "type": "Utility",
            "cost": 1,
            "damage": None,
            "range": "Self",
            "effect": "Spend 3 Soul Shards to recover 3 cards from discard pile. Gain 2 Taint.",
            "keywords": ["utility", "salvage", "taint", "shard-spending", "ossuarium"],
            "cardCount": 2,
            "cardType": "faction"
        },
        {
            "id": "emergency-rebuild",
            "name": "Emergency Rebuild",
            "type": "Utility",
            "cost": 2,
            "damage": None,
            "range": "Self",
            "effect": "Spend 5 Soul Shards to recover 5 cards from discard pile. Gain 3 Taint.",
            "keywords": ["utility", "salvage", "taint", "powerful", "shard-spending", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "corpse-fuel",
            "name": "Corpse Fuel",
            "type": "passive",
            "cost": 0,
            "damage": None,
            "range": "Self",
            "effect": "Passive: Whenever an enemy is destroyed within 3 hexes, gain 2 Soul Shards.",
            "keywords": ["passive", "shard-generation", "proximity", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "death-mark",
            "name": "Death Mark",
            "type": "debuff",
            "cost": 2,
            "damage": None,
            "range": "Ranged 1-6",
            "effect": "Mark target enemy. When the marked enemy is destroyed, gain +2 bonus Soul Shards (5 total instead of 3). Lasts until enemy dies or you mark a different target.",
            "keywords": ["debuff", "mark", "shard-generation", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "grave-pact",
            "name": "Grave Pact",
            "type": "Utility",
            "cost": 3,
            "damage": 6,
            "range": "Ranged 1-6",
            "effect": "Discard 3 cards. Deal 6 damage (2 damage per card discarded). If this destroys an enemy, gain 4 Soul Shards.",
            "keywords": ["utility", "sacrifice", "high-damage", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "scavenge-wreckage",
            "name": "Scavenge Wreckage",
            "type": "Utility",
            "cost": 1,
            "damage": None,
            "range": "Ranged 1-4",
            "effect": "Target a destroyed enemy wreck within 4 hexes. Gain 3 Soul Shards. That wreck is removed from play (cannot be scavenged again).",
            "keywords": ["utility", "shard-generation", "scavenge", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "reanimate",
            "name": "Reanimate",
            "type": "summon",
            "cost": 4,
            "damage": None,
            "range": "Ranged 1-3",
            "effect": "Spend 3 Soul Shards. Summon a Skeletal Minion within 3 hexes (3 HP, 3 Movement, 2 melee damage). Minion acts immediately after your turn.",
            "keywords": ["summon", "minion", "shard-spending", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "phylactery",
            "name": "Phylactery",
            "type": "passive",
            "cost": 0,
            "damage": None,
            "range": "Self",
            "effect": "Passive: The first time you would be reduced to 0 HP, if you have 5+ Soul Shards, automatically spend 5 Shards to recover to 3 HP. Gain 5 Taint. Once per mission only.",
            "keywords": ["passive", "emergency", "revival", "taint", "shard-spending", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "deathless-advance",
            "name": "Deathless Advance",
            "type": "movement",
            "cost": 2,
            "damage": None,
            "range": "Self",
            "effect": "Move up to 3 hexes. Until end of turn, you cannot take more than 5 damage from any single attack (damage cap).",
            "keywords": ["movement", "defensive", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "bone-armor",
            "name": "Bone Armor",
            "type": "Reactive",
            "cost": 0,
            "damage": None,
            "range": "Self",
            "effect": "Reactive: When attacked, reduce damage by 2.",
            "keywords": ["reactive", "defense", "block", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "corpse-shield",
            "name": "Corpse Shield",
            "type": "Reactive",
            "cost": 0,
            "damage": None,
            "range": "Self",
            "effect": "Passive: When an enemy within 3 hexes is destroyed, gain +3 Defense until end of your next turn.",
            "keywords": ["reactive", "defense", "conditional", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        },
        {
            "id": "taint-purge",
            "name": "Taint Purge",
            "type": "Utility",
            "cost": 3,
            "damage": None,
            "range": "Self",
            "effect": "Discard 4 cards. Remove up to 4 Taint. You cannot spend Soul Shards this turn.",
            "keywords": ["utility", "taint-removal", "sacrifice", "desperate", "ossuarium"],
            "cardCount": 1,
            "cardType": "faction"
        }
    ]

def main():
    print("Updating Ossuarium cards with Soul Shard system...")

    # Load main database
    db_path = 'docs/cards/complete-card-data.json'
    card_db = load_json(db_path)

    # Create new Ossuarium cards
    new_ossuarium_cards = create_new_ossuarium_cards()

    # Replace Ossuarium cards
    card_db['ossuarium'] = new_ossuarium_cards

    # Save updated database
    save_json(db_path, card_db)

    print(f"✅ Updated {len(new_ossuarium_cards)} Ossuarium cards")
    print(f"✅ Saved to {db_path}")

    # Print summary
    print("\n" + "="*60)
    print("OSSUARIUM CARD SUMMARY")
    print("="*60)
    attack_cards = [c for c in new_ossuarium_cards if c['type'] == 'Attack']
    utility_cards = [c for c in new_ossuarium_cards if c['type'] == 'Utility']
    passive_cards = [c for c in new_ossuarium_cards if c['type'] in ['passive', 'Reactive']]

    print(f"Attack cards: {len(attack_cards)}")
    print(f"Utility cards: {len(utility_cards)}")
    print(f"Passive/Reactive cards: {len(passive_cards)}")
    print(f"Movement cards: 1")
    print(f"Summon cards: 1")
    print(f"\nTotal: {len(new_ossuarium_cards)} cards")

    print("\n✅ Soul Shard system implemented!")
    print("   - Removed all lifesteal mechanics")
    print("   - Added Soul Shard generation from kills")
    print("   - Added Salvage Protocol cards (spend Shards for repairs)")
    print("   - Added Taint costs to salvage actions")
    print("   - Reduced base damage across the board")

if __name__ == '__main__':
    main()
