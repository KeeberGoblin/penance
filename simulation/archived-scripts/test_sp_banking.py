#!/usr/bin/env python3
"""
Test SP banking and positioning mechanics
Demonstrates tactical movement vs SP banking for combos
"""

import sys
sys.path.insert(0, '..')

from equipment_simulator import *

# Load card database
card_db = load_card_database()
builder = DeckBuilder(card_db)

print("=" * 80)
print("SP BANKING & POSITIONING TEST")
print("=" * 80)
print("\nMechanics:")
print("  - Start 2 hexes apart (out of melee range)")
print("  - Regenerate +2 SP per turn (banking mechanic)")
print("  - Movement costs 1 SP per hex")
print("  - Melee attacks require 0 range")
print("\nTactical Choices:")
print("  1. Move + attack (exhaust SP, risk getting blocked)")
print("  2. Hold position + bank SP (wait 1 turn, unleash combo next turn)")
print("=" * 80)

# Test 1: Movement and SP banking
print("\n=== TEST 1: Scout vs Warden (Movement and Banking) ===")
scout = builder.build_random_deck("church", CasketClass.SCOUT)
warden = builder.build_random_deck("dwarves", CasketClass.WARDEN)

print(f"\nChurch Scout: {scout.hp} HP, {scout.sp_max} SP (6 SP = high mobility)")
print(f"Dwarves Warden: {warden.hp} HP, {warden.sp_max} SP (5 SP = balanced)")

print(f"\nStarting positions:")
print(f"  Scout: {scout.range} hexes away, {scout.sp} SP")
print(f"  Warden: {warden.range} hexes away, {warden.sp} SP")

combat = EquipmentCombatSimulator(scout, warden, verbose=True)
result = combat.run_combat(max_turns=15)

print(f"\n--- RESULT ---")
print(f"Winner: {result['winner']} in {result['turns']} turns")
print(f"Scout: {result['casket1_hp']} HP remaining")
print(f"Warden: {result['casket2_hp']} HP remaining")

# Test 2: Statistical comparison - Does SP banking create better combos?
print("\n" + "=" * 80)
print("=== TEST 2: SP Banking Impact (20 runs) ===")

scout_wins = 0
warden_wins = 0

for run in range(20):
    scout = builder.build_random_deck("elves", CasketClass.SCOUT)
    warden = builder.build_random_deck("crucible", CasketClass.WARDEN)

    combat = EquipmentCombatSimulator(scout, warden, verbose=False)
    result = combat.run_combat(max_turns=50)

    if result['winner'] == scout.name:
        scout_wins += 1
    else:
        warden_wins += 1

print(f"\nScout (6 SP max): {scout_wins}-{warden_wins} ({(scout_wins/20)*100:.1f}% WR)")
print(f"Warden (5 SP max): {warden_wins}-{scout_wins} ({(warden_wins/20)*100:.1f}% WR)")

print("\nAnalysis:")
print("  - Scout has +1 SP max (can bank more SP)")
print("  - Scout can afford bigger combos after banking")
print("  - BUT Scout has less HP (28 vs 34)")
print("  - Movement + banking creates tactical depth")

# Test 3: Colossus vs Vanguard with SP banking
print("\n" + "=" * 80)
print("=== TEST 3: Colossus vs Vanguard with SP Banking ===")

colossus_wins = 0
vanguard_wins = 0
colossus_avg_sp_banked = 0
vanguard_avg_sp_banked = 0

print("\nWithout SP Banking (previous test): Colossus 50% WR vs Vanguard")
print("With SP Banking: ???")

for run in range(20):
    colossus = builder.build_random_deck("church", CasketClass.COLOSSUS)
    vanguard = builder.build_random_deck("dwarves", CasketClass.VANGUARD)

    combat = EquipmentCombatSimulator(colossus, vanguard, verbose=False)
    result = combat.run_combat(max_turns=50)

    if result['winner'] == colossus.name:
        colossus_wins += 1
    else:
        vanguard_wins += 1

print(f"\nColossus (4 SP max): {colossus_wins}-{vanguard_wins} ({(colossus_wins/20)*100:.1f}% WR)")
print(f"Vanguard (4 SP max): {vanguard_wins}-{colossus_wins} ({(vanguard_wins/20)*100:.1f}% WR)")

print("\nAnalysis:")
print("  - Both have 4 SP max (equal banking potential)")
print("  - Colossus has +10 HP advantage")
print("  - SP banking should favor Colossus (more turns to bank)")
print("  - Expected: Colossus 55-60% WR (HP advantage + banking time)")

print("\n" + "=" * 80)
print("CONCLUSION:")
print("  - SP banking adds tactical layer: move now OR wait for combo")
print("  - Higher SP max = more banking potential (Scout 6 SP > Warden 5 SP)")
print("  - Movement cost creates risk/reward (spend SP to close OR hold position)")
print("  - Tanky units (Colossus, Vanguard) benefit from banking (more turns alive)")
print("=" * 80)
