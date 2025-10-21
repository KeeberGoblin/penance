#!/usr/bin/env python3
"""
Verify user's specific claims about dice probabilities
"""

import sys
sys.path.append('.')

from equipment_simulator_dice import *
import random

random.seed(42)

print("=" * 80)
print("VERIFYING USER CLAIMS")
print("=" * 80)
print()

# Run 100,000 attack rolls
catastrophic_count = 0
critical_hit_count = 0
miss_count = 0
hit_count = 0
total_rolls = 100000

target_5_hits = 0
target_6_hits = 0
target_4_hits = 0

for i in range(total_rolls):
    die1, die2, total = AttackDie.roll_2d6()

    # Check for catastrophic failure
    if die1 == 0 and die2 == 0:
        catastrophic_count += 1

    # Check for critical hit (total 9)
    if total == 9:
        critical_hit_count += 1

    # Check hit rates at different targets
    if total >= 4:
        target_4_hits += 1
    if total >= 5:
        target_5_hits += 1
    if total >= 6:
        target_6_hits += 1

    # Check for miss/hit at base 5+ (documented)
    if total < 5:
        miss_count += 1
    else:
        hit_count += 1

print("USER CLAIM #1: Catastrophic failures are 7-8%")
print(f"Actual Rate: {(catastrophic_count/total_rolls)*100:.2f}%")
print(f"Expected: 2.78%")
print(f"Verdict: {'❌ CLAIM IS WRONG' if catastrophic_count/total_rolls < 0.05 else '✓ CLAIM IS CORRECT'}")
print()

print("USER CLAIM #2: Critical hits are 5-6%")
print(f"Actual Rate: {(critical_hit_count/total_rolls)*100:.2f}%")
print(f"Expected (total 9 only): 5.56%")
print(f"Expected (total 9+10): 8.33%")
print(f"Verdict: {'✓ CLAIM IS CORRECT (for total 9)' if 0.05 <= critical_hit_count/total_rolls <= 0.06 else '❌ CLAIM IS WRONG'}")
print()

print("USER CLAIM #3: Hit rate is 57-61%")
print(f"Actual Rate at 5+: {(target_5_hits/total_rolls)*100:.2f}%")
print(f"Expected: 58.33%")
print(f"Verdict: {'✓ CLAIM IS CORRECT' if 0.57 <= target_5_hits/total_rolls <= 0.61 else '❌ CLAIM IS WRONG'}")
print()

print("USER CLAIM #4: Should be 72% hit rate")
print(f"Actual Rate at 4+: {(target_4_hits/total_rolls)*100:.2f}%")
print(f"Expected: 72.22%")
print(f"Verdict: Hit rate is 72% at base 4+, not base 5+")
print()

print("=" * 80)
print("ANALYSIS")
print("=" * 80)
print()

print("The user is observing:")
print("  1. Catastrophic failures: They CLAIM 7-8% but actual is 2.78%")
print("     → POSSIBLE EXPLANATION: Confusing catastrophic failures with total misses")
print("     → At base 5+, total miss rate (including catastrophic) is:")
print(f"        {(miss_count/total_rolls)*100:.2f}% (all rolls < 5)")
print("     → This does NOT match 7-8% either")
print()

print("  2. Critical hits: They CLAIM 5-6% but should be 11.11%")
print(f"     → ACTUAL: {(critical_hit_count/total_rolls)*100:.2f}%")
print("     → This matches the claim! But the docs say 11.11%")
print("     → EXPLANATION: Docs assume total 9 has 11.11% probability")
print("     → Reality: With JAM face, total 9 has 5.56% probability")
print()

print("  3. Hit rate: They CLAIM 57-61% but should be 72%")
print(f"     → ACTUAL at 5+: {(target_5_hits/total_rolls)*100:.2f}%")
print(f"     → ACTUAL at 4+: {(target_4_hits/total_rolls)*100:.2f}%")
print("     → This matches the 57-61% claim at base 5+!")
print("     → The 72% rate is achieved at base 4+ (current simulator)")
print()

print("=" * 80)
print("CONCLUSION")
print("=" * 80)
print()

print("The user's claims are CORRECT for base 5+ target number:")
print("  - Catastrophic: ~2.8% (not 7-8%, user may be misremembering)")
print("  - Critical hits: ~5.6% (not 11.11% from docs)")
print("  - Hit rate: ~58% at base 5+ (not 72% from docs)")
print()
print("The documentation expectations (72% hit, 11.11% crit) are for:")
print("  - Normal 2d6 dice (faces 1-6), OR")
print("  - Base 4+ target number with custom dice")
print()
print("The simulator currently uses base 4+ (Line 718), which gives 72% hit rate.")
print("If the game rules say base 5+, then the hit rate is indeed only 58%.")
print()

# Check base target in actual combat
print("=" * 80)
print("CHECKING SIMULATOR BASE TARGET")
print("=" * 80)
print()

# Create test caskets
card_db = load_card_database()
builder = DeckBuilder(card_db)
casket1 = builder.build_random_deck("church", CasketClass.WARDEN)
casket2 = builder.build_random_deck("elves", CasketClass.WARDEN)

# Set both at range 0 (melee, no range modifier)
casket1.range = 0
casket2.range = 0

simulator = DiceCombatSimulator(casket1, casket2, verbose=False)
base_target = simulator.calculate_to_hit_target(casket1, casket2)

print(f"Base target number (at range 0): {base_target}")
print(f"Expected hit rate: {(sum(1 for i in range(36) if sum(random.choices([1,2,3,4,5,0], k=2)) >= base_target) / 36) * 100:.2f}%")
print()

if base_target == 4:
    print("✓ Simulator uses base 4+ (72% hit rate)")
    print("  This does NOT match user's observation of 57-61% hit rate")
    print("  User may be testing with range modifiers active")
elif base_target == 5:
    print("✓ Simulator uses base 5+ (58% hit rate)")
    print("  This matches user's observation of 57-61% hit rate")
else:
    print(f"? Simulator uses base {base_target}+")

# Check with range 2 (default starting range)
casket1.range = 2
casket2.range = 2
target_at_range_2 = simulator.calculate_to_hit_target(casket1, casket2)
print()
print(f"Target number at range 2 (default): {target_at_range_2}")

if target_at_range_2 == 5:
    hit_rate_at_5 = (target_5_hits/total_rolls) * 100
    print(f"Expected hit rate at 5+: {hit_rate_at_5:.2f}%")
    print("✓ This matches user's 57-61% observation!")
    print("  User is testing at default range (2 hexes), not melee range")
