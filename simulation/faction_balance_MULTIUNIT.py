#!/usr/bin/env python3
"""
Faction Balance Test with Multi-Unit Combat
Tests all 10 factions with army vs army battles using focus fire mechanics
"""

from equipment_simulator_dice import *

def run_multiunit_matchup(
    faction1: str,
    faction2: str,
    army_builder: PointBudgetArmyBuilder,
    point_budget: float,
    runs: int = 5
) -> dict:
    """Run multiple army battles between two factions"""
    faction1_wins = 0
    faction2_wins = 0
    timeouts = 0

    for _ in range(runs):
        # Generate random armies
        army1 = army_builder.build_random_army(faction1, point_budget, allow_supports=True)
        army2 = army_builder.build_random_army(faction2, point_budget, allow_supports=True)

        # Run battle
        simulator = MultiUnitCombatSimulator(army1, army2, verbose=False)
        result = simulator.run_battle(max_turns=30)

        # Record result
        if result['winner'] == faction1:
            faction1_wins += 1
        else:
            faction2_wins += 1

        if result.get('timeout', False):
            timeouts += 1

    return {
        'faction1': faction1,
        'faction2': faction2,
        'faction1_wins': faction1_wins,
        'faction2_wins': faction2_wins,
        'timeouts': timeouts,
        'total_games': runs
    }


if __name__ == "__main__":
    print("=" * 80)
    print("FACTION BALANCE TEST - MULTI-UNIT ARMIES")
    print("=" * 80)
    print("\nFeatures:")
    print("  - Multi-unit combat with focus fire targeting")
    print("  - Random army compositions (Scouts, Wardens, Vanguards, Colossus)")
    print("  - Support unit integration")
    print("  - Actual combat simulation (not just power comparison)")
    print("\n" + "=" * 80)

    # Load database
    card_db = load_card_database()
    deck_builder = DeckBuilder(card_db)
    army_builder = PointBudgetArmyBuilder(deck_builder)

    # Test factions
    factions = [
        'church', 'dwarves', 'elves', 'nomads', 'ossuarium',
        'crucible', 'emergent', 'exchange', 'vestige-bloodlines', 'wyrd-conclave'
    ]

    # Test at EASY difficulty (4 points)
    difficulty = Difficulty.EASY
    runs_per_matchup = 5

    print(f"\nTesting at {difficulty.name} difficulty ({difficulty.point_budget} points)")
    print(f"Runs per matchup: {runs_per_matchup}")
    print(f"Total battles: {len(factions)} factions × {len(factions)-1} matchups × {runs_per_matchup} runs")
    print("=" * 80)

    # Track faction records
    faction_records = {f: {'wins': 0, 'losses': 0, 'timeouts': 0} for f in factions}

    # Run all matchups
    matchups_completed = 0
    total_matchups = len(factions) * (len(factions) - 1) // 2

    print(f"\nRunning {total_matchups} matchups...")

    for i, faction1 in enumerate(factions):
        for faction2 in factions[i+1:]:
            result = run_multiunit_matchup(
                faction1, faction2,
                army_builder,
                difficulty.point_budget,
                runs=runs_per_matchup
            )

            # Update records
            faction_records[faction1]['wins'] += result['faction1_wins']
            faction_records[faction1]['losses'] += result['faction2_wins']
            faction_records[faction1]['timeouts'] += result['timeouts']

            faction_records[faction2]['wins'] += result['faction2_wins']
            faction_records[faction2]['losses'] += result['faction1_wins']
            faction_records[faction2]['timeouts'] += result['timeouts']

            matchups_completed += 1
            if matchups_completed % 10 == 0:
                print(f"  Progress: {matchups_completed}/{total_matchups} matchups...")

    print(f"\nCompleted {matchups_completed} matchups!")

    # Calculate win rates
    print("\n" + "=" * 80)
    print("FACTION BALANCE RESULTS (MULTI-UNIT COMBAT)")
    print("=" * 80)

    results = []
    for faction in factions:
        record = faction_records[faction]
        total_games = record['wins'] + record['losses']
        win_rate = (record['wins'] / total_games * 100) if total_games > 0 else 0

        results.append({
            'faction': faction,
            'wins': record['wins'],
            'losses': record['losses'],
            'win_rate': win_rate,
            'timeouts': record['timeouts'],
            'total_games': total_games
        })

    # Sort by win rate
    results.sort(key=lambda x: x['win_rate'], reverse=True)

    # Print results
    print(f"\n{'Faction':<22} {'Record':<12} {'WR%':<10} {'Timeouts':<10} {'Status'}")
    print("-" * 80)

    balanced_count = 0
    for r in results:
        status = "✅ BALANCED" if 45 <= r['win_rate'] <= 55 else "⚠️ NEEDS ADJUSTMENT"
        if 45 <= r['win_rate'] <= 55:
            balanced_count += 1

        print(f"{r['faction'].capitalize():<22} {r['wins']}-{r['losses']:<10} {r['win_rate']:<10.1f} "
              f"{r['timeouts']:<10} {status}")

    print("\n" + "=" * 80)
    print(f"BALANCE SCORE: {balanced_count}/{len(factions)} factions in 45-55% WR range")
    print("=" * 80)

    # Identify overpowered and underpowered factions
    overpowered = [r for r in results if r['win_rate'] > 55]
    underpowered = [r for r in results if r['win_rate'] < 45]

    if overpowered:
        print("\nOVERPOWERED (>55% WR):")
        for r in overpowered:
            print(f"  - {r['faction'].capitalize()}: {r['win_rate']:.1f}% WR")

    if underpowered:
        print("\nUNDERPOWERED (<45% WR):")
        for r in underpowered:
            print(f"  - {r['faction'].capitalize()}: {r['win_rate']:.1f}% WR")

    if balanced_count >= 7:
        print("\n✅ EXCELLENT BALANCE: 7+ factions balanced")
    elif balanced_count >= 5:
        print("\n⚠️ GOOD BALANCE: 5-6 factions balanced (needs minor tweaks)")
    elif balanced_count >= 3:
        print("\n⚠️ FAIR BALANCE: 3-4 factions balanced (needs work)")
    else:
        print("\n❌ POOR BALANCE: <3 factions balanced (major issues)")

    print("\n" + "=" * 80)
    print("COMPARISON TO SINGLE-UNIT COMBAT (v5.14)")
    print("=" * 80)
    print("\nSingle-Unit WR (1v1 Warden vs Warden):")
    single_unit_wr = {
        'crucible': 80.0, 'nomads': 75.6, 'vestige-bloodlines': 73.3,
        'exchange': 66.7, 'emergent': 64.4, 'ossuarium': 51.1,
        'wyrd-conclave': 42.2, 'elves': 28.9, 'church': 13.3, 'dwarves': 4.4
    }

    print(f"\n{'Faction':<22} {'Multi-Unit WR':<15} {'Single-Unit WR':<15} {'Difference'}")
    print("-" * 80)

    for r in results:
        single_wr = single_unit_wr.get(r['faction'], 0)
        diff = r['win_rate'] - single_wr
        diff_str = f"{diff:+.1f}%"

        print(f"{r['faction'].capitalize():<22} {r['win_rate']:<15.1f} {single_wr:<15.1f} {diff_str}")

    print("\n" + "=" * 80)
