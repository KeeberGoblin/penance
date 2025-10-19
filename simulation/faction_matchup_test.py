#!/usr/bin/env python3
"""
Faction vs Faction Matchup Testing
Tests each faction against all others to identify balance issues
"""

from combat_simulator import *
from collections import defaultdict
import random

def run_faction_matchup_test(num_runs: int = 20, casket_class: CasketClass = CasketClass.WARDEN):
    """Test each faction against all others

    Args:
        num_runs: Number of iterations per matchup
        casket_class: Which casket class to use (default: WARDEN for balanced baseline)
    """

    print("=" * 80)
    print(f"FACTION MATCHUP TEST ({num_runs} runs per matchup, {casket_class.value[0]} class)")
    print("=" * 80)

    factions = [
        "church", "dwarves", "ossuarium", "elves",
        "crucible", "exchange", "nomads", "bloodlines",
        "emergent", "wyrd"
    ]

    # Track results: faction -> {opponent: {wins, losses, draws}}
    matchup_results = defaultdict(lambda: defaultdict(lambda: {"wins": 0, "losses": 0, "draws": 0, "total_turns": []}))

    # Track overall faction performance
    faction_stats = {faction: {"wins": 0, "losses": 0, "draws": 0} for faction in factions}

    # Run all matchups
    total_matchups = len(factions) * (len(factions) - 1)
    matchup_count = 0

    for faction1 in factions:
        print(f"\n{'=' * 80}")
        print(f"{faction1.upper()} vs ALL OTHER FACTIONS")
        print(f"{'=' * 80}\n")

        for faction2 in factions:
            if faction1 == faction2:
                continue  # Skip mirror matches

            matchup_count += 1
            print(f"  [{matchup_count}/{total_matchups}] {faction1.capitalize()} vs {faction2.capitalize()}... ", end="", flush=True)

            # Run multiple iterations of this matchup
            f1_wins = 0
            f2_wins = 0
            draws = 0
            turns_list = []

            for run in range(num_runs):
                casket1 = create_test_casket(faction1.capitalize(), faction1, casket_class)
                casket2 = create_test_casket(faction2.capitalize(), faction2, casket_class)

                combat = CombatSimulator(casket1, casket2, verbose=False)
                result = combat.run_combat(max_turns=150)  # 150 turn limit to prevent infinite stalemates

                turns_list.append(result['turns'])

                if result['winner'] == faction1.capitalize():
                    f1_wins += 1
                    faction_stats[faction1]["wins"] += 1
                    faction_stats[faction2]["losses"] += 1
                elif result['winner'] == faction2.capitalize():
                    f2_wins += 1
                    faction_stats[faction2]["wins"] += 1
                    faction_stats[faction1]["losses"] += 1
                else:
                    draws += 1
                    faction_stats[faction1]["draws"] += 1
                    faction_stats[faction2]["draws"] += 1

            # Record matchup results
            matchup_results[faction1][faction2]["wins"] = f1_wins
            matchup_results[faction1][faction2]["losses"] = f2_wins
            matchup_results[faction1][faction2]["draws"] = draws
            matchup_results[faction1][faction2]["total_turns"] = turns_list

            # Calculate winrate
            if f1_wins + f2_wins > 0:
                f1_winrate = f1_wins / (f1_wins + f2_wins) * 100
            else:
                f1_winrate = 0

            avg_turns = sum(turns_list) / len(turns_list)

            print(f"{f1_wins}-{f2_wins}-{draws} ({f1_winrate:.1f}% WR, {avg_turns:.1f} avg turns)")

    # ========================================================================
    # GENERATE COMPREHENSIVE REPORT
    # ========================================================================
    print("\n" + "=" * 80)
    print("GENERATING FACTION MATCHUP REPORT")
    print("=" * 80)

    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append(f"PENANCE: Faction Matchup Analysis ({num_runs} runs, {casket_class.value[0]} class)")
    report_lines.append("=" * 80)
    report_lines.append("")

    # ========================================================================
    # SECTION 1: Overall Faction Win Rates
    # ========================================================================
    report_lines.append("### OVERALL FACTION PERFORMANCE ###\n")

    # Calculate overall winrates
    faction_winrates = []
    for faction, stats in faction_stats.items():
        total_games = stats["wins"] + stats["losses"] + stats["draws"]
        if total_games > 0:
            winrate = stats["wins"] / total_games * 100
        else:
            winrate = 0

        faction_winrates.append((
            faction,
            winrate,
            stats["wins"],
            stats["losses"],
            stats["draws"],
            total_games
        ))

    # Sort by winrate (descending)
    faction_winrates.sort(key=lambda x: x[1], reverse=True)

    report_lines.append(f"{'Faction':<15} {'WR%':>6} {'Wins':>5} {'Losses':>7} {'Draws':>6} {'Total':>6}")
    report_lines.append("-" * 60)

    for faction, winrate, wins, losses, draws, total in faction_winrates:
        report_lines.append(f"{faction.capitalize():<15} {winrate:>5.1f}% {wins:>5} {losses:>7} {draws:>6} {total:>6}")

    # ========================================================================
    # SECTION 2: Individual Faction Deep Dives
    # ========================================================================
    report_lines.append("\n\n" + "=" * 80)
    report_lines.append("INDIVIDUAL FACTION MATCHUP BREAKDOWNS")
    report_lines.append("=" * 80)

    for faction in factions:
        report_lines.append(f"\n### {faction.upper()} ###\n")

        # Get all matchups for this faction
        matchups = []
        for opponent, results in matchup_results[faction].items():
            wins = results["wins"]
            losses = results["losses"]
            draws = results["draws"]
            total = wins + losses + draws

            if total > 0:
                winrate = wins / total * 100
            else:
                winrate = 0

            avg_turns = sum(results["total_turns"]) / len(results["total_turns"]) if results["total_turns"] else 0

            matchups.append((opponent, winrate, wins, losses, draws, avg_turns))

        # Sort by winrate (ascending to show worst matchups first)
        matchups.sort(key=lambda x: x[1])

        report_lines.append(f"{'Opponent':<15} {'WR%':>6} {'W-L-D':>10} {'Avg Turns':>10}")
        report_lines.append("-" * 50)

        for opponent, winrate, wins, losses, draws, avg_turns in matchups:
            wld = f"{wins}-{losses}-{draws}"
            report_lines.append(f"{opponent.capitalize():<15} {winrate:>5.1f}% {wld:>10} {avg_turns:>10.1f}")

        # Identify problem matchups
        report_lines.append("")
        worst_matchups = [m for m in matchups if m[1] < 40]
        best_matchups = [m for m in matchups if m[1] > 60]

        if worst_matchups:
            report_lines.append(f"  WEAK AGAINST: {', '.join([m[0].capitalize() for m in worst_matchups])}")
        if best_matchups:
            report_lines.append(f"  STRONG AGAINST: {', '.join([m[0].capitalize() for m in best_matchups])}")

    # ========================================================================
    # SECTION 3: Balance Insights and Recommendations
    # ========================================================================
    report_lines.append("\n\n" + "=" * 80)
    report_lines.append("BALANCE INSIGHTS & RECOMMENDATIONS")
    report_lines.append("=" * 80 + "\n")

    # Identify overpowered factions (>55% overall winrate)
    overpowered = [f for f in faction_winrates if f[1] > 55]
    if overpowered:
        report_lines.append("OVERPOWERED FACTIONS (>55% overall WR):")
        for faction, winrate, wins, losses, draws, total in overpowered:
            report_lines.append(f"  - {faction.capitalize()}: {winrate:.1f}% WR ({wins}-{losses}-{draws})")

            # Find their best matchups
            best = sorted([(o, matchup_results[faction][o]["wins"] / num_runs * 100)
                          for o in matchup_results[faction].keys()],
                          key=lambda x: x[1], reverse=True)[:3]
            report_lines.append(f"    Best vs: {', '.join([f'{o.capitalize()} ({w:.0f}%)' for o, w in best])}")
        report_lines.append("")

    # Identify underpowered factions (<45% overall winrate)
    underpowered = [f for f in faction_winrates if f[1] < 45]
    if underpowered:
        report_lines.append("UNDERPOWERED FACTIONS (<45% overall WR):")
        for faction, winrate, wins, losses, draws, total in underpowered:
            report_lines.append(f"  - {faction.capitalize()}: {winrate:.1f}% WR ({wins}-{losses}-{draws})")

            # Find their worst matchups
            worst = sorted([(o, matchup_results[faction][o]["wins"] / num_runs * 100)
                           for o in matchup_results[faction].keys()],
                           key=lambda x: x[1])[:3]
            report_lines.append(f"    Worst vs: {', '.join([f'{o.capitalize()} ({w:.0f}%)' for o, w in worst])}")
        report_lines.append("")

    # Identify balanced factions (45-55% winrate)
    balanced = [f for f in faction_winrates if 45 <= f[1] <= 55]
    if balanced:
        report_lines.append("WELL-BALANCED FACTIONS (45-55% WR):")
        for faction, winrate, wins, losses, draws, total in balanced:
            report_lines.append(f"  - {faction.capitalize()}: {winrate:.1f}% WR")
        report_lines.append("")

    # Identify rock-paper-scissors relationships
    report_lines.append("\nROCK-PAPER-SCISSORS DYNAMICS:")
    for faction1, wr1, _, _, _, _ in faction_winrates[:5]:  # Top 5 factions
        for faction2, wr2, _, _, _, _ in faction_winrates[-5:]:  # Bottom 5 factions
            if faction1 != faction2:
                f1_vs_f2 = matchup_results[faction1][faction2]["wins"] / num_runs * 100
                f2_vs_f1 = matchup_results[faction2][faction1]["wins"] / num_runs * 100

                # Check if weak faction beats strong faction
                if f2_vs_f1 > 55:
                    report_lines.append(f"  - {faction2.capitalize()} counters {faction1.capitalize()} ({f2_vs_f1:.0f}% WR) despite being weaker overall!")

    # Print to console
    print("\n" + "\n".join(report_lines))

    # Write to file
    report_path = "C:\\GAMES\\GitHub\\penance\\simulation\\faction_matchup_report.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\nFaction matchup report saved to: {report_path}")
    print("\n" + "=" * 80)
    print("FACTION MATCHUP TEST COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    # Test with Warden class (balanced baseline)
    run_faction_matchup_test(num_runs=20, casket_class=CasketClass.WARDEN)
