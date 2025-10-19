#!/usr/bin/env python3
"""
Test combo system to validate synergy vs burst mechanics
"""

import sys
sys.path.insert(0, '..')

from equipment_simulator import *

# Load card database
card_db = load_card_database()
builder = DeckBuilder(card_db)

print("=" * 80)
print("COMBO SYSTEM TEST")
print("=" * 80)
print("\nCombo Bonuses:")
print("  2-card combo: +1 damage bonus")
print("  3-card combo: +2 damage bonus")
print("\nPriority: Synergy (combos) > Burst (single high-damage card)")
print("=" * 80)

# Test 1: Warden vs Warden (5 SP - best for combos)
print("\n=== TEST 1: Warden vs Warden (5 SP allows versatile combos) ===")
warden1 = builder.build_random_deck("church", CasketClass.WARDEN)
warden2 = builder.build_random_deck("dwarves", CasketClass.WARDEN)

print(f"\nChurch Warden: {warden1.hp} HP, {warden1.sp_max} SP")
print(f"Equipment: {', '.join(set([c.equipment_name for c in warden1.equipment_cards]))}")

print(f"\nDwarves Warden: {warden2.hp} HP, {warden2.sp_max} SP")
print(f"Equipment: {', '.join(set([c.equipment_name for c in warden2.equipment_cards]))}")

combat = EquipmentCombatSimulator(warden1, warden2, verbose=True)
result = combat.run_combat(max_turns=10)

print(f"\n--- RESULT ---")
print(f"Winner: {result['winner']} in {result['turns']} turns")
print(f"Church: {result['casket1_hp']} HP remaining")
print(f"Dwarves: {result['casket2_hp']} HP remaining")

# Test 2: Compare Warden (5 SP) vs Colossus (4 SP) for combo effectiveness
print("\n" + "=" * 80)
print("=== TEST 2: Warden (5 SP) vs Colossus (4 SP) - Combo Effectiveness ===")

warden = builder.build_random_deck("elves", CasketClass.WARDEN)
colossus = builder.build_random_deck("crucible", CasketClass.COLOSSUS)

print(f"\nElves Warden: {warden.hp} HP, {warden.sp_max} SP (5 SP = more combo options)")
print(f"Crucible Colossus: {colossus.hp} HP, {colossus.sp_max} SP (4 SP = limited combos)")

combat = EquipmentCombatSimulator(warden, colossus, verbose=True)
result = combat.run_combat(max_turns=10)

print(f"\n--- RESULT ---")
print(f"Winner: {result['winner']} in {result['turns']} turns")
print(f"Warden: {result['casket1_hp']} HP remaining")
print(f"Colossus: {result['casket2_hp']} HP remaining")

# Test 3: Statistical comparison (20 runs)
print("\n" + "=" * 80)
print("=== TEST 3: Combo vs Burst Statistical Comparison (20 runs) ===")

warden_wins = 0
colossus_wins = 0
warden_combos = 0
colossus_combos = 0

for run in range(20):
    warden = builder.build_random_deck("church", CasketClass.WARDEN)
    colossus = builder.build_random_deck("dwarves", CasketClass.COLOSSUS)

    combat = EquipmentCombatSimulator(warden, colossus, verbose=False)
    result = combat.run_combat(max_turns=50)

    if result['winner'] == warden.name:
        warden_wins += 1
    else:
        colossus_wins += 1

print(f"\nWarden (5 SP): {warden_wins}-{colossus_wins} ({(warden_wins/20)*100:.1f}% WR)")
print(f"Colossus (4 SP): {colossus_wins}-{warden_wins} ({(colossus_wins/20)*100:.1f}% WR)")

print("\nAnalysis:")
print("  - Warden 5 SP allows more combo opportunities (2-3 card combos)")
print("  - Colossus 4 SP limits to 2-card combos or single attacks")
print("  - Combo system encourages synergy over burst damage")
print("  - Higher SP = more flexible combo options = better value")

print("\n" + "=" * 80)
