#!/usr/bin/env python3
"""
Faction Matchup Test v2.0 - Realistic Damage Scaling
Tests all 10 factions against each other with proper damage values (1-4 range)
"""

from combat_simulator_v2 import *

def run_faction_matchup_test_v2(num_runs: int = 20, casket_class: CasketClass = CasketClass.WARDEN):
    """Test all factions against each other"""

    factions = ["church", "dwarves", "ossuarium", "elves", "crucible",
                "exchange", "nomads", "bloodlines", "emergent", "wyrd"]

    print("=" * 80)
    print(f"FACTION MATCHUP TEST V2.0 (Realistic Damage)")
    print(f"{num_runs} runs per matchup, {casket_class.value[0]} class")
    print("=" * 80)
    print()

    # Track results
    results = {faction: {"wins": 0, "losses": 0, "draws": 0} for faction in factions}
    matchup_details = {}

    total_matchups = len(factions) * (len(factions) - 1)
    current = 0

    # Run all matchups
    for faction1 in factions:
        for faction2 in factions:
            if faction1 == faction2:
                continue

            current += 1
            matchup_key = f"{faction1}_vs_{faction2}"
            matchup_details[matchup_key] = {"wins": 0, "losses": 0, "draws": 0, "total_turns": 0}

            print(f"[{current}/{total_matchups}] {faction1.capitalize()} vs {faction2.capitalize()}...", end=" ")

            # Run multiple tests
            for run in range(num_runs):
                casket1 = create_test_casket(f"{faction1}-{run}", faction1, casket_class)
                casket2 = create_test_casket(f"{faction2}-{run}", faction2, casket_class)

                combat = CombatSimulator(casket1, casket2, verbose=False)
                result = combat.run_combat(max_turns=150)

                matchup_details[matchup_key]["total_turns"] += result["turns"]

                if result["winner"] == casket1.name:
                    results[faction1]["wins"] += 1
                    results[faction2]["losses"] += 1
                    matchup_details[matchup_key]["wins"] += 1
                elif result["winner"] == casket2.name:
                    results[faction1]["losses"] += 1
                    results[faction2]["wins"] += 1
                    matchup_details[matchup_key]["losses"] += 1
                else:
                    results[faction1]["draws"] += 1
                    results[faction2]["draws"] += 1
                    matchup_details[matchup_key]["draws"] += 1

            # Calculate matchup stats
            total = matchup_details[matchup_key]["wins"] + matchup_details[matchup_key]["losses"] + matchup_details[matchup_key]["draws"]
            avg_turns = matchup_details[matchup_key]["total_turns"] / num_runs

            wins = matchup_details[matchup_key]["wins"]
            losses = matchup_details[matchup_key]["losses"]
            draws = matchup_details[matchup_key]["draws"]

            if wins + losses > 0:
                wr = (wins / (wins + losses)) * 100
            else:
                wr = 0.0

            print(f"{wins}-{losses}-{draws} ({wr:.1f}% WR, {avg_turns:.1f} avg turns)")

    # Generate summary report
    print()
    print("=" * 80)
    print("FACTION OVERALL PERFORMANCE")
    print("=" * 80)
    print()

    print(f"{'Faction':<15} {'WR%':>6} {'Wins':>6} {'Losses':>6} {'Draws':>6} {'Total':>6}")
    print("-" * 60)

    # Sort by win rate
    faction_stats = []
    for faction in factions:
        total_games = results[faction]["wins"] + results[faction]["losses"] + results[faction]["draws"]
        if results[faction]["wins"] + results[faction]["losses"] > 0:
            win_rate = (results[faction]["wins"] / (results[faction]["wins"] + results[faction]["losses"])) * 100
        else:
            win_rate = 0.0

        faction_stats.append({
            "faction": faction,
            "win_rate": win_rate,
            "wins": results[faction]["wins"],
            "losses": results[faction]["losses"],
            "draws": results[faction]["draws"],
            "total": total_games
        })

    faction_stats.sort(key=lambda x: x["win_rate"], reverse=True)

    for stats in faction_stats:
        print(f"{stats['faction'].capitalize():<15} {stats['win_rate']:>5.1f}% "
              f"{stats['wins']:>6} {stats['losses']:>6} {stats['draws']:>6} {stats['total']:>6}")

    print()
    print("=" * 80)
    print("BALANCE INSIGHTS")
    print("=" * 80)
    print()

    # Identify overpowered factions (>55% WR)
    overpowered = [f for f in faction_stats if f["win_rate"] > 55]
    if overpowered:
        print("OVERPOWERED FACTIONS (>55% WR):")
        for f in overpowered:
            print(f"  - {f['faction'].capitalize()}: {f['win_rate']:.1f}% WR")
        print()

    # Identify underpowered factions (<45% WR)
    underpowered = [f for f in faction_stats if f["win_rate"] < 45]
    if underpowered:
        print("UNDERPOWERED FACTIONS (<45% WR):")
        for f in underpowered:
            print(f"  - {f['faction'].capitalize()}: {f['win_rate']:.1f}% WR")
        print()

    # Identify balanced factions (45-55% WR)
    balanced = [f for f in faction_stats if 45 <= f["win_rate"] <= 55]
    if balanced:
        print("WELL-BALANCED FACTIONS (45-55% WR):")
        for f in balanced:
            print(f"  - {f['faction'].capitalize()}: {f['win_rate']:.1f}% WR ✅")
        print()

    print(f"Balance Score: {len(balanced)}/10 factions balanced")
    print()

    # Save detailed report
    report_path = "C:\\GAMES\\GitHub\\penance\\simulation\\faction_matchup_report_v2.txt"
    with open(report_path, "w") as f:
        f.write("=" * 80 + "\n")
        f.write("PENANCE: Faction Matchup Analysis v2.0 (Realistic Damage)\n")
        f.write(f"{num_runs} runs per matchup, {casket_class.value[0]} class\n")
        f.write("=" * 80 + "\n\n")

        f.write("### OVERALL FACTION PERFORMANCE ###\n\n")
        f.write(f"{'Faction':<15} {'WR%':>6} {'Wins':>6} {'Losses':>6} {'Draws':>6} {'Total':>6}\n")
        f.write("-" * 60 + "\n")

        for stats in faction_stats:
            f.write(f"{stats['faction'].capitalize():<15} {stats['win_rate']:>5.1f}% "
                   f"{stats['wins']:>6} {stats['losses']:>6} {stats['draws']:>6} {stats['total']:>6}\n")

        f.write("\n\n" + "=" * 80 + "\n")
        f.write("BALANCE INSIGHTS\n")
        f.write("=" * 80 + "\n\n")

        if overpowered:
            f.write("OVERPOWERED FACTIONS (>55% WR):\n")
            for faction in overpowered:
                f.write(f"  - {faction['faction'].capitalize()}: {faction['win_rate']:.1f}% WR\n")
            f.write("\n")

        if underpowered:
            f.write("UNDERPOWERED FACTIONS (<45% WR):\n")
            for faction in underpowered:
                f.write(f"  - {faction['faction'].capitalize()}: {faction['win_rate']:.1f}% WR\n")
            f.write("\n")

        if balanced:
            f.write("WELL-BALANCED FACTIONS (45-55% WR):\n")
            for faction in balanced:
                f.write(f"  - {faction['faction'].capitalize()}: {faction['win_rate']:.1f}% WR ✅\n")
            f.write("\n")

        f.write(f"Balance Score: {len(balanced)}/10 factions balanced\n")

    print(f"Detailed report saved to: {report_path}")
    print()
    print("=" * 80)
    print("FACTION MATCHUP TEST V2.0 COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    run_faction_matchup_test_v2(num_runs=20, casket_class=CasketClass.WARDEN)
