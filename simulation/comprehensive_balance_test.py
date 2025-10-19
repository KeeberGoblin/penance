#!/usr/bin/env python3
"""
Comprehensive balance testing across all 10 factions and 4 casket classes
"""

from combat_simulator import *
from collections import defaultdict

def run_comprehensive_balance_test(num_runs: int = 10):
    """Run comprehensive balance tests across all factions"""

    print("=" * 80)
    print(f"PENANCE: Comprehensive Balance Test ({num_runs} runs per matchup)")
    print("=" * 80)

    # All 10 factions
    factions = [
        "church", "dwarves", "ossuarium", "elves",
        "crucible", "exchange", "nomads", "bloodlines",
        "emergent", "wyrd"
    ]

    # Track faction performance
    faction_stats = {faction: {"wins": 0, "losses": 0, "total_damage_dealt": 0} for faction in factions}

    # Track class matchups
    class_matchups = {
        "scout_vs_warden": {"scout": 0, "warden": 0},
        "scout_vs_vanguard": {"scout": 0, "vanguard": 0},
        "scout_vs_colossus": {"scout": 0, "colossus": 0},
        "warden_vs_vanguard": {"warden": 0, "vanguard": 0},
        "warden_vs_colossus": {"warden": 0, "colossus": 0},
        "vanguard_vs_colossus": {"vanguard": 0, "colossus": 0}
    }

    # ========================================================================
    # TEST 1: All Factions Round Robin (Warden vs Warden)
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 1: Faction Balance (All 10 factions, Warden class)")
    print("=" * 80)

    for i in range(num_runs):
        print(f"\n[Round {i+1}/{num_runs}]")
        for idx, faction1 in enumerate(factions):
            for faction2 in factions[idx+1:]:
                casket1 = create_test_casket(f"{faction1.capitalize()}", faction1, CasketClass.WARDEN)
                casket2 = create_test_casket(f"{faction2.capitalize()}", faction2, CasketClass.WARDEN)

                combat = CombatSimulator(casket1, casket2, verbose=False)
                result = combat.run_combat()

                if result['winner'] == faction1.capitalize():
                    faction_stats[faction1]["wins"] += 1
                    faction_stats[faction2]["losses"] += 1
                elif result['winner'] == faction2.capitalize():
                    faction_stats[faction2]["wins"] += 1
                    faction_stats[faction1]["losses"] += 1

        print(f"  Completed {len(factions) * (len(factions) - 1) // 2} matchups")

    # ========================================================================
    # TEST 2: Class Balance Testing
    # ========================================================================
    print("\n" + "=" * 80)
    print("TEST 2: Casket Class Balance")
    print("=" * 80)

    for i in range(num_runs):
        print(f"\n[Run {i+1}/{num_runs}]")

        # Scout vs Warden
        scout = create_test_casket("Scout", "elves", CasketClass.SCOUT)
        warden = create_test_casket("Warden", "church", CasketClass.WARDEN)
        combat = CombatSimulator(scout, warden, verbose=False)
        result = combat.run_combat()
        if result['winner'] == "Scout":
            class_matchups["scout_vs_warden"]["scout"] += 1
        else:
            class_matchups["scout_vs_warden"]["warden"] += 1
        print(f"  Scout vs Warden: {result['winner']} ({result['turns']} turns)")

        # Scout vs Vanguard
        scout = create_test_casket("Scout", "elves", CasketClass.SCOUT)
        vanguard = create_test_casket("Vanguard", "dwarves", CasketClass.VANGUARD)
        combat = CombatSimulator(scout, vanguard, verbose=False)
        result = combat.run_combat()
        if result['winner'] == "Scout":
            class_matchups["scout_vs_vanguard"]["scout"] += 1
        else:
            class_matchups["scout_vs_vanguard"]["vanguard"] += 1
        print(f"  Scout vs Vanguard: {result['winner']} ({result['turns']} turns)")

        # Scout vs Colossus
        scout = create_test_casket("Scout", "elves", CasketClass.SCOUT)
        colossus = create_test_casket("Colossus", "dwarves", CasketClass.COLOSSUS)
        combat = CombatSimulator(scout, colossus, verbose=False)
        result = combat.run_combat()
        if result['winner'] == "Scout":
            class_matchups["scout_vs_colossus"]["scout"] += 1
        else:
            class_matchups["scout_vs_colossus"]["colossus"] += 1
        print(f"  Scout vs Colossus: {result['winner']} ({result['turns']} turns)")

        # Warden vs Vanguard
        warden = create_test_casket("Warden", "church", CasketClass.WARDEN)
        vanguard = create_test_casket("Vanguard", "dwarves", CasketClass.VANGUARD)
        combat = CombatSimulator(warden, vanguard, verbose=False)
        result = combat.run_combat()
        if result['winner'] == "Warden":
            class_matchups["warden_vs_vanguard"]["warden"] += 1
        else:
            class_matchups["warden_vs_vanguard"]["vanguard"] += 1
        print(f"  Warden vs Vanguard: {result['winner']} ({result['turns']} turns)")

        # Warden vs Colossus
        warden = create_test_casket("Warden", "church", CasketClass.WARDEN)
        colossus = create_test_casket("Colossus", "dwarves", CasketClass.COLOSSUS)
        combat = CombatSimulator(warden, colossus, verbose=False)
        result = combat.run_combat()
        if result['winner'] == "Warden":
            class_matchups["warden_vs_colossus"]["warden"] += 1
        else:
            class_matchups["warden_vs_colossus"]["colossus"] += 1
        print(f"  Warden vs Colossus: {result['winner']} ({result['turns']} turns)")

        # Vanguard vs Colossus
        vanguard = create_test_casket("Vanguard", "crucible", CasketClass.VANGUARD)
        colossus = create_test_casket("Colossus", "exchange", CasketClass.COLOSSUS)
        combat = CombatSimulator(vanguard, colossus, verbose=False)
        result = combat.run_combat()
        if result['winner'] == "Vanguard":
            class_matchups["vanguard_vs_colossus"]["vanguard"] += 1
        else:
            class_matchups["vanguard_vs_colossus"]["colossus"] += 1
        print(f"  Vanguard vs Colossus: {result['winner']} ({result['turns']} turns)")

    # ========================================================================
    # GENERATE COMPREHENSIVE REPORT
    # ========================================================================
    print("\n" + "=" * 80)
    print("GENERATING COMPREHENSIVE REPORT")
    print("=" * 80)

    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append(f"PENANCE: Comprehensive Balance Report ({num_runs} runs)")
    report_lines.append("=" * 80)
    report_lines.append("")

    # Faction Win Rates
    report_lines.append("\n### FACTION BALANCE (Warden vs Warden) ###\n")
    total_matches = num_runs * (len(factions) - 1)

    # Sort factions by win rate
    faction_winrates = []
    for faction, stats in faction_stats.items():
        total_games = stats["wins"] + stats["losses"]
        winrate = (stats["wins"] / total_games * 100) if total_games > 0 else 0
        faction_winrates.append((faction, winrate, stats["wins"], stats["losses"]))

    faction_winrates.sort(key=lambda x: x[1], reverse=True)

    for faction, winrate, wins, losses in faction_winrates:
        report_lines.append(f"{faction.capitalize():15} {winrate:5.1f}% WR ({wins:2} wins / {losses:2} losses)")

    # Class Matchups
    report_lines.append("\n\n### CASKET CLASS MATCHUPS ###\n")

    for matchup, stats in class_matchups.items():
        class1, class2 = matchup.split("_vs_")
        class1_wins = stats[class1]
        class2_wins = stats[class2]
        class1_wr = class1_wins / num_runs * 100
        class2_wr = class2_wins / num_runs * 100

        report_lines.append(f"--- {class1.capitalize()} vs {class2.capitalize()} ---")
        report_lines.append(f"{class1.capitalize():12} {class1_wins:3} wins ({class1_wr:5.1f}%)")
        report_lines.append(f"{class2.capitalize():12} {class2_wins:3} wins ({class2_wr:5.1f}%)")
        report_lines.append("")

    # Balance Insights
    report_lines.append("\n" + "=" * 80)
    report_lines.append("BALANCE INSIGHTS")
    report_lines.append("=" * 80 + "\n")

    report_lines.append("FACTION TIER LIST:")
    for i, (faction, winrate, wins, losses) in enumerate(faction_winrates):
        if i < 3:
            report_lines.append(f"  S-Tier: {faction.capitalize()} ({winrate:.1f}% WR)")
        elif i < 6:
            report_lines.append(f"  A-Tier: {faction.capitalize()} ({winrate:.1f}% WR)")
        else:
            report_lines.append(f"  B-Tier: {faction.capitalize()} ({winrate:.1f}% WR)")

    report_lines.append("")
    report_lines.append("CLASS BALANCE OBSERVATIONS:")

    # Analyze class matchups
    scout_total_wr = (class_matchups["scout_vs_warden"]["scout"] +
                      class_matchups["scout_vs_vanguard"]["scout"] +
                      class_matchups["scout_vs_colossus"]["scout"]) / (num_runs * 3) * 100
    report_lines.append(f"  - Scout overall winrate: {scout_total_wr:.1f}%")

    if class_matchups["scout_vs_colossus"]["scout"] / num_runs > 0.6:
        report_lines.append(f"  - Scout beats Colossus ({class_matchups['scout_vs_colossus']['scout'] / num_runs * 100:.1f}% WR) - may need mobility nerf")
    elif class_matchups["scout_vs_colossus"]["colossus"] / num_runs > 0.6:
        report_lines.append(f"  - Colossus beats Scout ({class_matchups['scout_vs_colossus']['colossus'] / num_runs * 100:.1f}% WR) - HP advantage too strong")

    # Print to console
    print("\n" + "\n".join(report_lines))

    # Write to file
    report_path = "C:\\GAMES\\GitHub\\penance\\simulation\\comprehensive_balance_report.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\nComprehensive report saved to: {report_path}")
    print("\n" + "=" * 80)
    print("COMPREHENSIVE BALANCE TEST COMPLETE!")
    print("=" * 80)

if __name__ == "__main__":
    run_comprehensive_balance_test(num_runs=10)
