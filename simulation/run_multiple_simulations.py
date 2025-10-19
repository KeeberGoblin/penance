#!/usr/bin/env python3
"""
Run multiple simulation iterations and collect statistics
"""

import subprocess
import json
from collections import defaultdict
from combat_simulator import *

def run_simulation_batch(num_runs: int = 10):
    """Run simulations multiple times and collect statistics"""

    print("=" * 80)
    print(f"Running {num_runs} simulation iterations...")
    print("=" * 80)

    # Track results across all runs
    combat_stats = {
        "church_vs_dwarves": {"church_wins": 0, "dwarves_wins": 0, "draws": 0, "avg_turns": []},
        "ossuarium_vs_elves": {"ossuarium_wins": 0, "elves_wins": 0, "draws": 0, "avg_turns": []},
        "scout_vs_fortress": {"scout_wins": 0, "fortress_wins": 0, "draws": 0, "avg_turns": []}
    }

    campaign_stats = {
        "successes": 0,
        "failures": 0,
        "avg_missions_completed": [],
        "avg_final_hp": [],
        "avg_final_scrap": []
    }

    for run in range(1, num_runs + 1):
        print(f"\n[RUN {run}/{num_runs}]")

        # ====================================================================
        # SCENARIO 1: Church vs Dwarves
        # ====================================================================
        church = create_test_casket("Holy Avenger", "church", CasketClass.ASSAULT)
        dwarves = create_test_casket("Runeforge Titan", "dwarves", CasketClass.HEAVY)

        combat1 = CombatSimulator(church, dwarves, verbose=False)
        result1 = combat1.run_combat()  # Unlimited turns

        if result1['winner'] == "Holy Avenger":
            combat_stats["church_vs_dwarves"]["church_wins"] += 1
        elif result1['winner'] == "Runeforge Titan":
            combat_stats["church_vs_dwarves"]["dwarves_wins"] += 1
        else:
            combat_stats["church_vs_dwarves"]["draws"] += 1
        combat_stats["church_vs_dwarves"]["avg_turns"].append(result1['turns'])

        print(f"  Church vs Dwarves: {result1['winner']} ({result1['turns']} turns)")

        # ====================================================================
        # SCENARIO 2: Ossuarium vs Elves
        # ====================================================================
        ossuarium = create_test_casket("Bone Lord", "ossuarium", CasketClass.ASSAULT)
        elves = create_test_casket("Thornblade", "elves", CasketClass.SCOUT)

        combat2 = CombatSimulator(ossuarium, elves, verbose=False)
        result2 = combat2.run_combat()  # Unlimited turns

        if result2['winner'] == "Bone Lord":
            combat_stats["ossuarium_vs_elves"]["ossuarium_wins"] += 1
        elif result2['winner'] == "Thornblade":
            combat_stats["ossuarium_vs_elves"]["elves_wins"] += 1
        else:
            combat_stats["ossuarium_vs_elves"]["draws"] += 1
        combat_stats["ossuarium_vs_elves"]["avg_turns"].append(result2['turns'])

        print(f"  Ossuarium vs Elves: {result2['winner']} ({result2['turns']} turns)")

        # ====================================================================
        # SCENARIO 3: Scout vs Fortress
        # ====================================================================
        scout = create_test_casket("Swift Striker", "elves", CasketClass.SCOUT)
        fortress = create_test_casket("Iron Wall", "dwarves", CasketClass.FORTRESS)

        combat3 = CombatSimulator(scout, fortress, verbose=False)
        result3 = combat3.run_combat()  # Unlimited turns

        if result3['winner'] == "Swift Striker":
            combat_stats["scout_vs_fortress"]["scout_wins"] += 1
        elif result3['winner'] == "Iron Wall":
            combat_stats["scout_vs_fortress"]["fortress_wins"] += 1
        else:
            combat_stats["scout_vs_fortress"]["draws"] += 1
        combat_stats["scout_vs_fortress"]["avg_turns"].append(result3['turns'])

        print(f"  Scout vs Fortress: {result3['winner']} ({result3['turns']} turns)")

        # ====================================================================
        # CAMPAIGN: Church 3-Mission Arc
        # ====================================================================
        campaign_casket = create_test_casket("Penitent Crusader", "church", CasketClass.ASSAULT)
        campaign = CampaignSimulator(campaign_casket)
        campaign_result = campaign.run_campaign(num_missions=3)  # Unlimited turns per mission

        if campaign_result['success']:
            campaign_stats["successes"] += 1
        else:
            campaign_stats["failures"] += 1

        campaign_stats["avg_missions_completed"].append(campaign_result['missions_completed'])
        campaign_stats["avg_final_hp"].append(campaign_result['final_hp'])
        campaign_stats["avg_final_scrap"].append(campaign_result['final_scrap'])

        print(f"  Campaign: {'SUCCESS' if campaign_result['success'] else 'FAILED'} ({campaign_result['missions_completed']} missions)")

    # ========================================================================
    # GENERATE SUMMARY REPORT
    # ========================================================================
    print("\n" + "=" * 80)
    print("GENERATING SUMMARY REPORT")
    print("=" * 80)

    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append(f"PENANCE: Simulation Summary ({num_runs} runs)")
    report_lines.append("=" * 80)
    report_lines.append("")

    # Combat Statistics
    report_lines.append("\n### COMBAT SCENARIOS ###\n")

    # Church vs Dwarves
    report_lines.append("--- Church vs Dwarves ---")
    report_lines.append(f"Church wins:  {combat_stats['church_vs_dwarves']['church_wins']:>3} ({combat_stats['church_vs_dwarves']['church_wins']/num_runs*100:>5.1f}%)")
    report_lines.append(f"Dwarves wins: {combat_stats['church_vs_dwarves']['dwarves_wins']:>3} ({combat_stats['church_vs_dwarves']['dwarves_wins']/num_runs*100:>5.1f}%)")
    report_lines.append(f"Draws:        {combat_stats['church_vs_dwarves']['draws']:>3} ({combat_stats['church_vs_dwarves']['draws']/num_runs*100:>5.1f}%)")
    avg_turns = sum(combat_stats['church_vs_dwarves']['avg_turns']) / len(combat_stats['church_vs_dwarves']['avg_turns'])
    report_lines.append(f"Avg turns:    {avg_turns:.1f}")
    report_lines.append("")

    # Ossuarium vs Elves
    report_lines.append("--- Ossuarium vs Elves ---")
    report_lines.append(f"Ossuarium wins: {combat_stats['ossuarium_vs_elves']['ossuarium_wins']:>3} ({combat_stats['ossuarium_vs_elves']['ossuarium_wins']/num_runs*100:>5.1f}%)")
    report_lines.append(f"Elves wins:     {combat_stats['ossuarium_vs_elves']['elves_wins']:>3} ({combat_stats['ossuarium_vs_elves']['elves_wins']/num_runs*100:>5.1f}%)")
    report_lines.append(f"Draws:          {combat_stats['ossuarium_vs_elves']['draws']:>3} ({combat_stats['ossuarium_vs_elves']['draws']/num_runs*100:>5.1f}%)")
    avg_turns = sum(combat_stats['ossuarium_vs_elves']['avg_turns']) / len(combat_stats['ossuarium_vs_elves']['avg_turns'])
    report_lines.append(f"Avg turns:      {avg_turns:.1f}")
    report_lines.append("")

    # Scout vs Fortress
    report_lines.append("--- Scout vs Fortress ---")
    report_lines.append(f"Scout wins:    {combat_stats['scout_vs_fortress']['scout_wins']:>3} ({combat_stats['scout_vs_fortress']['scout_wins']/num_runs*100:>5.1f}%)")
    report_lines.append(f"Fortress wins: {combat_stats['scout_vs_fortress']['fortress_wins']:>3} ({combat_stats['scout_vs_fortress']['fortress_wins']/num_runs*100:>5.1f}%)")
    report_lines.append(f"Draws:         {combat_stats['scout_vs_fortress']['draws']:>3} ({combat_stats['scout_vs_fortress']['draws']/num_runs*100:>5.1f}%)")
    avg_turns = sum(combat_stats['scout_vs_fortress']['avg_turns']) / len(combat_stats['scout_vs_fortress']['avg_turns'])
    report_lines.append(f"Avg turns:     {avg_turns:.1f}")
    report_lines.append("")

    # Campaign Statistics
    report_lines.append("\n### CAMPAIGN STATISTICS ###\n")
    report_lines.append(f"Successes: {campaign_stats['successes']:>3} ({campaign_stats['successes']/num_runs*100:>5.1f}%)")
    report_lines.append(f"Failures:  {campaign_stats['failures']:>3} ({campaign_stats['failures']/num_runs*100:>5.1f}%)")
    avg_missions = sum(campaign_stats['avg_missions_completed']) / len(campaign_stats['avg_missions_completed'])
    avg_hp = sum(campaign_stats['avg_final_hp']) / len(campaign_stats['avg_final_hp'])
    avg_scrap = sum(campaign_stats['avg_final_scrap']) / len(campaign_stats['avg_final_scrap'])
    report_lines.append(f"Avg missions completed: {avg_missions:.1f}")
    report_lines.append(f"Avg final HP:           {avg_hp:.1f}")
    report_lines.append(f"Avg final Scrap:        {avg_scrap:.1f}")
    report_lines.append("")

    # Balance Analysis
    report_lines.append("\n" + "=" * 80)
    report_lines.append("BALANCE INSIGHTS")
    report_lines.append("=" * 80 + "\n")

    report_lines.append("FACTION MATCHUPS:")
    church_wr = combat_stats['church_vs_dwarves']['church_wins'] / num_runs * 100
    if church_wr > 60:
        report_lines.append(f"  - Church appears STRONG vs Dwarves ({church_wr:.1f}% winrate)")
    elif church_wr < 40:
        report_lines.append(f"  - Church appears WEAK vs Dwarves ({church_wr:.1f}% winrate)")
    else:
        report_lines.append(f"  - Church vs Dwarves appears BALANCED ({church_wr:.1f}% winrate)")

    oss_wr = combat_stats['ossuarium_vs_elves']['ossuarium_wins'] / num_runs * 100
    if oss_wr > 60:
        report_lines.append(f"  - Ossuarium appears STRONG vs Elves ({oss_wr:.1f}% winrate)")
    elif oss_wr < 40:
        report_lines.append(f"  - Ossuarium appears WEAK vs Elves ({oss_wr:.1f}% winrate)")
    else:
        report_lines.append(f"  - Ossuarium vs Elves appears BALANCED ({oss_wr:.1f}% winrate)")

    report_lines.append("")
    report_lines.append("CASKET CLASS BALANCE:")
    scout_wr = combat_stats['scout_vs_fortress']['scout_wins'] / num_runs * 100
    fortress_wr = combat_stats['scout_vs_fortress']['fortress_wins'] / num_runs * 100
    if scout_wr > 60:
        report_lines.append(f"  - Scout DOMINATES Fortress ({scout_wr:.1f}% winrate)")
    elif fortress_wr > 60:
        report_lines.append(f"  - Fortress DOMINATES Scout ({fortress_wr:.1f}% winrate)")
    else:
        report_lines.append(f"  - Scout vs Fortress appears BALANCED")

    report_lines.append("")
    report_lines.append("CAMPAIGN DIFFICULTY:")
    campaign_success_rate = campaign_stats['successes'] / num_runs * 100
    if campaign_success_rate < 30:
        report_lines.append(f"  - Campaign appears TOO HARD ({campaign_success_rate:.1f}% success rate)")
    elif campaign_success_rate > 70:
        report_lines.append(f"  - Campaign appears TOO EASY ({campaign_success_rate:.1f}% success rate)")
    else:
        report_lines.append(f"  - Campaign difficulty appears BALANCED ({campaign_success_rate:.1f}% success rate)")

    # Print to console
    print("\n" + "\n".join(report_lines))

    # Write to file
    report_path = "C:\\GAMES\\GitHub\\penance\\simulation\\summary_report.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\nSummary report saved to: {report_path}")
    print("\n" + "=" * 80)
    print("BATCH SIMULATION COMPLETE!")
    print("=" * 80)

if __name__ == "__main__":
    run_simulation_batch(num_runs=10)
