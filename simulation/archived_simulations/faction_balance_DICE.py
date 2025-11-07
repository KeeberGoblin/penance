#!/usr/bin/env python3
"""
Penance Faction Balance Test WITH DICE MECHANICS
Tests all 10 factions against each other with attack/defense dice
"""

import sys
from equipment_simulator_dice import (
    load_card_database,
    DeckBuilder,
    DiceCombatSimulator,
    CasketClass
)

# ============================================================================
# FACTION BALANCE TESTER
# ============================================================================

def run_faction_matchup(faction1: str, faction2: str, builder: DeckBuilder, runs: int = 5) -> dict:
    """
    Run multiple battles between two factions
    Returns win rates and statistics
    """
    wins_faction1 = 0
    wins_faction2 = 0
    total_turns = 0
    total_attack_rolls = []

    for _ in range(runs):
        # Build caskets
        casket1 = builder.build_random_deck(faction1, CasketClass.WARDEN)
        casket2 = builder.build_random_deck(faction2, CasketClass.WARDEN)

        # Run combat
        simulator = DiceCombatSimulator(casket1, casket2, verbose=False)
        result = simulator.run_combat()

        # Track results
        if result['winner'] == casket1.name:
            wins_faction1 += 1
        else:
            wins_faction2 += 1

        total_turns += result['turns']
        total_attack_rolls.extend(result['attack_rolls'])

    return {
        'faction1': faction1,
        'faction2': faction2,
        'wins_f1': wins_faction1,
        'wins_f2': wins_faction2,
        'runs': runs,
        'avg_turns': total_turns / runs,
        'attack_rolls': total_attack_rolls
    }

def calculate_hit_rate(attack_rolls: list) -> float:
    """Calculate actual hit rate from attack rolls (5+ = hit)"""
    if not attack_rolls:
        return 0.0
    hits = sum(1 for roll in attack_rolls if roll >= 5)
    return (hits / len(attack_rolls)) * 100

def run_full_balance_test():
    """Run complete faction balance test"""
    print("=" * 80)
    print("FACTION BALANCE TEST - WITH DICE MECHANICS")
    print("=" * 80)
    print()
    print("Dice Mechanics:")
    print("  - Attack: 2d6 custom dice (faces: 1, 2, 3, 4, 5, 0/JAM)")
    print("  - Hit target: 5+ (base)")
    print("  - Defense: 1d6 per damage (33% block chance)")
    print("  - Critical hits (+2 dmg), Executions (instant component kill)")
    print("  - Catastrophic failures (weapon jam)")
    print()
    print("Test: 10 factions x 9 matchups x 5 runs = 450 battles")
    print("=" * 80)
    print()

    # Load card database
    card_db = load_card_database()
    builder = DeckBuilder(card_db)

    # All factions
    factions = [
        'church',
        'dwarves',
        'ossuarium',
        'elves',
        'nomads',
        'crucible',
        'emergent',
        'exchange',
        'vestige-bloodlines',
        'wyrd-conclave'
    ]

    # Track results
    faction_records = {faction: {'wins': 0, 'losses': 0, 'attack_rolls': []} for faction in factions}

    battle_count = 0
    total_battles = len(factions) * (len(factions) - 1) // 2 * 5

    print(f"Running {total_battles // 5} battles...")

    # Run all matchups
    for i, faction1 in enumerate(factions):
        for faction2 in factions[i+1:]:
            # Run matchup
            result = run_faction_matchup(faction1, faction2, builder, runs=5)

            # Update records
            faction_records[faction1]['wins'] += result['wins_f1']
            faction_records[faction1]['losses'] += result['wins_f2']
            faction_records[faction1]['attack_rolls'].extend(result['attack_rolls'])

            faction_records[faction2]['wins'] += result['wins_f2']
            faction_records[faction2]['losses'] += result['wins_f1']
            faction_records[faction2]['attack_rolls'].extend(result['attack_rolls'])

            battle_count += result['runs']

            # Progress update
            if battle_count % 50 == 0:
                print(f"  Progress: {battle_count}/{total_battles} battles...")

    print(f"\nCompleted {battle_count} battles!")

    # Calculate statistics
    faction_stats = []
    for faction, record in faction_records.items():
        total_games = record['wins'] + record['losses']
        win_rate = (record['wins'] / total_games * 100) if total_games > 0 else 0
        hit_rate = calculate_hit_rate(record['attack_rolls'])

        faction_stats.append({
            'faction': faction,
            'wins': record['wins'],
            'losses': record['losses'],
            'win_rate': win_rate,
            'hit_rate': hit_rate,
            'total_rolls': len(record['attack_rolls'])
        })

    # Sort by win rate (descending)
    faction_stats.sort(key=lambda x: x['win_rate'], reverse=True)

    # Print results
    print()
    print("=" * 80)
    print("FACTION BALANCE RESULTS (WITH DICE MECHANICS)")
    print("=" * 80)
    print()

    print(f"{'Faction':<20} {'Record':<12} {'WR%':<8} {'Hit%':<8} {'Rolls':<8} {'Status':<20}")
    print("-" * 80)

    balanced_count = 0
    for stat in faction_stats:
        faction_name = stat['faction'].capitalize()
        record = f"{stat['wins']}-{stat['losses']}"
        win_rate = stat['win_rate']
        hit_rate = stat['hit_rate']
        rolls = stat['total_rolls']

        # Status
        if 45 <= win_rate <= 55:
            status = "✅ BALANCED"
            balanced_count += 1
        elif win_rate > 55:
            status = "⚠️ NEEDS ADJUSTMENT"
        else:
            status = "⚠️ NEEDS ADJUSTMENT"

        print(f"{faction_name:<20} {record:<12} {win_rate:>5.1f}%  {hit_rate:>5.1f}%  {rolls:<8} {status}")

    print()
    print("=" * 80)
    print(f"BALANCE SCORE: {balanced_count}/10 factions in 45-55% WR range")
    print("=" * 80)
    print()

    # Insights
    print("KEY INSIGHTS:")
    print("-" * 80)
    print()

    # Overpowered factions
    overpowered = [s for s in faction_stats if s['win_rate'] > 55]
    if overpowered:
        print("OVERPOWERED (>55% WR):")
        for stat in overpowered:
            print(f"  - {stat['faction'].capitalize()}: {stat['win_rate']:.1f}% WR")
    print()

    # Underpowered factions
    underpowered = [s for s in faction_stats if s['win_rate'] < 45]
    if underpowered:
        print("UNDERPOWERED (<45% WR):")
        for stat in underpowered:
            print(f"  - {stat['faction'].capitalize()}: {stat['win_rate']:.1f}% WR")
    print()

    # Balance assessment
    if balanced_count >= 7:
        print("✅ GOOD BALANCE: 7+ factions in target range")
    elif balanced_count >= 5:
        print("⚠️ MODERATE BALANCE: 5-6 factions need adjustment")
    else:
        print("❌ POOR BALANCE: Only", balanced_count, "factions balanced (major issues)")

    print()

    # Dice mechanics insights
    print("DICE MECHANICS ANALYSIS:")
    print("-" * 80)
    all_rolls = []
    for record in faction_records.values():
        all_rolls.extend(record['attack_rolls'])

    if all_rolls:
        avg_hit_rate = calculate_hit_rate(all_rolls)
        catastrophic_fails = sum(1 for roll in all_rolls if roll == 2)
        executions = sum(1 for roll in all_rolls if roll == 10)
        critical_hits = sum(1 for roll in all_rolls if roll == 9)

        print(f"Total attack rolls: {len(all_rolls)}")
        print(f"Average hit rate: {avg_hit_rate:.1f}% (expected: ~72%)")
        print(f"Catastrophic failures: {catastrophic_fails} ({catastrophic_fails/len(all_rolls)*100:.1f}%, expected: 2.78%)")
        print(f"Executions: {executions} ({executions/len(all_rolls)*100:.1f}%, expected: 2.78%)")
        print(f"Critical hits: {critical_hits} ({critical_hits/len(all_rolls)*100:.1f}%, expected: 11.11%)")

    print()
    print("=" * 80)

if __name__ == "__main__":
    run_full_balance_test()
