#!/usr/bin/env python3
"""Deep dive analysis of problem factions."""

import json
from collections import defaultdict

def load_card_data():
    with open('/workspaces/penance/docs/cards/complete-card-data.json', 'r') as f:
        return json.load(f)

def analyze_card_efficiency(cards):
    """Analyze damage-per-cost efficiency."""
    attack_cards = []
    for card in cards:
        cost = card.get('cost', 0)
        effect = card.get('effect', '') + ' ' + card.get('text', '')

        # Try to extract damage
        damage = 0
        if 'damage' in card:
            dmg = card['damage']
            if isinstance(dmg, (int, float)):
                damage = dmg
            elif isinstance(dmg, str):
                try:
                    damage = int(dmg)
                except:
                    pass

        if damage > 0 and isinstance(cost, int):
            efficiency = damage / max(cost, 1)
            attack_cards.append({
                'name': card.get('name'),
                'damage': damage,
                'cost': cost,
                'efficiency': efficiency,
                'effect': effect[:150]
            })

    return sorted(attack_cards, key=lambda x: x['efficiency'], reverse=True)

def analyze_synergies(cards):
    """Look for synergistic mechanics."""
    synergies = defaultdict(list)

    for card in cards:
        name = card.get('name', '')
        effect = (card.get('effect', '') + ' ' + card.get('text', '')).lower()

        # Token generation
        if any(word in effect for word in ['gain', 'token', 'counter', 'biomass', 'credit', 'bargain']):
            synergies['token_generation'].append(name)

        # Token spending
        if any(word in effect for word in ['spend', 'cost:', 'consume']):
            synergies['token_spending'].append(name)

        # Card draw
        if 'draw' in effect and 'card' in effect:
            synergies['card_draw'].append(name)

        # Deck recovery
        if 'recover' in effect and ('discard' in effect or 'pile' in effect):
            synergies['deck_recovery'].append(name)

        # Damage buffs
        if '+' in effect and 'damage' in effect:
            synergies['damage_buffs'].append(name)

        # Passive abilities
        if 'passive:' in effect:
            synergies['passives'].append(name)

        # On-kill effects
        if any(word in effect for word in ['kill', 'destroyed', 'dies', 'death']):
            synergies['on_kill'].append(name)

    return synergies

def main():
    data = load_card_data()

    problem_factions = {
        'ossuarium': '64% WR',
        'vestige-bloodlines': '69% WR',
        'church': '27% WR',
        'dwarves': '29% -> 47% WR'
    }

    print("=" * 100)
    print("DEEP DIVE: FACTION BALANCE ANALYSIS")
    print("=" * 100)

    for faction, wr in problem_factions.items():
        if faction not in data:
            continue

        cards = data[faction]
        print(f"\n{'=' * 100}")
        print(f"{faction.upper()} - {wr}")
        print(f"{'=' * 100}")

        # Card efficiency
        efficiency = analyze_card_efficiency(cards)
        print(f"\nDamage Efficiency (Damage per Cost):")
        print(f"{'Card':<30} {'Damage':<10} {'Cost':<10} {'Efficiency':<15}")
        print("-" * 100)
        for card in efficiency[:10]:
            print(f"{card['name']:<30} {card['damage']:<10} {card['cost']:<10} {card['efficiency']:<15.2f}")

        # Synergies
        synergies = analyze_synergies(cards)
        print(f"\n\nSYNERGY ANALYSIS:")
        for synergy_type, card_list in synergies.items():
            if card_list:
                print(f"\n{synergy_type.upper().replace('_', ' ')} ({len(card_list)} cards):")
                for card_name in card_list[:8]:
                    print(f"  - {card_name}")

        # Look for unique mechanics
        print(f"\n\nUNIQUE MECHANICS:")
        unique_keywords = set()
        for card in cards:
            keywords = card.get('keywords', [])
            if isinstance(keywords, list):
                unique_keywords.update(keywords)
        print(f"Keywords: {', '.join(sorted(unique_keywords))}")

        # Count card types
        card_types = defaultdict(int)
        for card in cards:
            card_types[card.get('type', 'unknown')] += 1
        print(f"\nCard Type Distribution:")
        for ctype, count in sorted(card_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  {ctype}: {count}")

    # Comparative metrics
    print(f"\n\n{'=' * 100}")
    print("COMPARATIVE METRICS")
    print(f"{'=' * 100}")

    metrics = {}
    for faction in problem_factions.keys():
        if faction not in data:
            continue
        cards = data[faction]
        efficiency = analyze_card_efficiency(cards)
        synergies = analyze_synergies(cards)

        metrics[faction] = {
            'avg_efficiency': sum(c['efficiency'] for c in efficiency) / len(efficiency) if efficiency else 0,
            'top_efficiency': efficiency[0]['efficiency'] if efficiency else 0,
            'token_economy': len(synergies['token_generation']) + len(synergies['token_spending']),
            'card_advantage': len(synergies['card_draw']) + len(synergies['deck_recovery']),
            'damage_buffs': len(synergies['damage_buffs']),
            'on_kill_synergies': len(synergies['on_kill']),
            'passives': len(synergies['passives']),
            'deck_recovery': len(synergies['deck_recovery'])
        }

    print(f"\n{'Faction':<20} {'Avg Eff':<12} {'Top Eff':<12} {'Token Eco':<12} {'Card Adv':<12} {'Dmg Buffs':<12} {'On-Kill':<12} {'Passives':<12}")
    print("-" * 100)
    for faction, m in metrics.items():
        print(f"{faction:<20} {m['avg_efficiency']:<12.2f} {m['top_efficiency']:<12.2f} {m['token_economy']:<12} {m['card_advantage']:<12} {m['damage_buffs']:<12} {m['on_kill_synergies']:<12} {m['passives']:<12}")

    # Key findings
    print(f"\n\n{'=' * 100}")
    print("KEY FINDINGS")
    print(f"{'=' * 100}")

    print(f"\nOSSUARIUM (64% WR):")
    print(f"  - Has {metrics['ossuarium']['on_kill_synergies']} on-kill synergy cards")
    print(f"  - Has {metrics['ossuarium']['deck_recovery']} deck recovery mechanics")
    print(f"  - Average damage efficiency: {metrics['ossuarium']['avg_efficiency']:.2f}")

    print(f"\nVESTIGE-BLOODLINES (69% WR):")
    print(f"  - Has {metrics['vestige-bloodlines']['token_economy']} token economy cards")
    print(f"  - Has {metrics['vestige-bloodlines']['damage_buffs']} damage buff cards")
    print(f"  - Has {metrics['vestige-bloodlines']['card_advantage']} card advantage mechanics")
    print(f"  - Top damage efficiency: {metrics['vestige-bloodlines']['top_efficiency']:.2f}")

    print(f"\nCHURCH (27% WR):")
    print(f"  - Has {metrics['church']['damage_buffs']} damage buff cards")
    print(f"  - Has {metrics['church']['card_advantage']} card advantage mechanics")
    print(f"  - Average damage efficiency: {metrics['church']['avg_efficiency']:.2f}")
    print(f"  - Note: Only 4 actual damage cards (rest are 0 damage)")

    print(f"\nDWARVES (29% -> 47% WR):")
    print(f"  - Has {metrics['dwarves']['token_economy']} token economy cards (Rune Counters)")
    print(f"  - Has {metrics['dwarves']['damage_buffs']} damage buff cards")
    print(f"  - Top damage efficiency: {metrics['dwarves']['top_efficiency']:.2f}")

if __name__ == '__main__':
    main()
