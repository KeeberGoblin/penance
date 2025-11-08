#!/usr/bin/env python3
"""
Test actual dice probabilities vs expected probabilities
"""

import sys
sys.path.append('.')

from equipment_simulator_dice import *
import random

# Set random seed for reproducibility
random.seed(42)

print("=" * 80)
print("DICE PROBABILITY TESTING")
print("=" * 80)

# Test Attack Dice Probabilities
print("\n" + "=" * 80)
print("ATTACK DICE (2d6) PROBABILITY TEST")
print("=" * 80)
print("Running 100,000 rolls...")

rolls = {}
for i in range(100000):
    die1, die2, total = AttackDie.roll_2d6()

    if total not in rolls:
        rolls[total] = 0
    rolls[total] += 1

    # Track special cases
    if die1 == 0 and die2 == 0:
        if 'catastrophic' not in rolls:
            rolls['catastrophic'] = 0
        rolls['catastrophic'] += 1

    if die1 == 5 and die2 == 5:
        if 'execution' not in rolls:
            rolls['execution'] = 0
        rolls['execution'] += 1

    if total == 9:
        if 'critical' not in rolls:
            rolls['critical'] = 0
        rolls['critical'] += 1

print("\nRoll Distribution:")
print("Total | Count | Actual % | Expected % | Difference")
print("-" * 60)

expected_probs = {
    0: 2.78,   # Double JAM
    1: 5.56,   # 1+0 or 0+1
    2: 8.33,   # 1+1 or 2+0 or 0+2
    3: 11.11,  # 1+2, 2+1, 3+0, 0+3
    4: 13.89,  # 1+3, 2+2, 3+1, 4+0, 0+4
    5: 16.67,  # 1+4, 2+3, 3+2, 4+1, 5+0, 0+5
    6: 13.89,  # 1+5, 2+4, 3+3, 4+2, 5+1
    7: 11.11,  # 2+5, 3+4, 4+3, 5+2
    8: 5.56,   # 3+5, 4+4, 5+3
    9: 2.78,   # 4+5, 5+4
    10: 2.78,  # 5+5 (EXECUTION)
}

for total in sorted([k for k in rolls.keys() if isinstance(k, int)]):
    count = rolls[total]
    actual_pct = (count / 100000) * 100
    expected_pct = expected_probs.get(total, 0)
    diff = actual_pct - expected_pct
    print(f"{total:5} | {count:5} | {actual_pct:7.2f}% | {expected_pct:7.2f}% | {diff:+7.2f}%")

print("\nSpecial Results:")
print(f"Catastrophic Failures (0+0): {rolls.get('catastrophic', 0)} ({rolls.get('catastrophic', 0)/1000:.2f}% - expected 2.78%)")
print(f"Executions (5+5): {rolls.get('execution', 0)} ({rolls.get('execution', 0)/1000:.2f}% - expected 2.78%)")
print(f"Critical Hits (total 9): {rolls.get('critical', 0)} ({rolls.get('critical', 0)/1000:.2f}% - expected 11.11%)")

# Calculate hit rates for different target numbers
print("\nHit Rates by Target Number:")
print("Target | Hits | Hit Rate | Expected")
print("-" * 50)

for target in [4, 5, 6, 7, 8, 9, 10]:
    hits = sum(count for total, count in rolls.items() if isinstance(total, int) and total >= target)
    hit_rate = (hits / 100000) * 100

    # Expected hit rates (from dice-reference.md)
    expected_rates = {
        4: 83.33,  # 4+ hits
        5: 72.22,  # 5+ hits (standard)
        6: 58.33,
        7: 41.67,
        8: 27.78,
        9: 13.89,
        10: 2.78
    }

    expected = expected_rates.get(target, 0)
    diff = hit_rate - expected
    print(f"{target:6}+ | {hits:5} | {hit_rate:7.2f}% | {expected:7.2f}% ({diff:+6.2f}%)")

# Test Defense Dice Probabilities
print("\n" + "=" * 80)
print("DEFENSE DICE PROBABILITY TEST")
print("=" * 80)
print("Running 100,000 rolls...")

defense_results = {
    DefenseDie.SHIELD: 0,
    DefenseDie.ABSORB: 0,
    DefenseDie.FLESH_WOUND: 0,
    DefenseDie.CRITICAL: 0,
    DefenseDie.PIERCE: 0,
    DefenseDie.HEAT: 0
}

for i in range(100000):
    result = DefenseDie.roll()
    defense_results[result] += 1

print("\nDefense Symbol Distribution:")
print("Symbol       | Count | Actual % | Expected % | Difference")
print("-" * 70)

for symbol, count in defense_results.items():
    actual_pct = (count / 100000) * 100
    expected_pct = 16.67  # Each face is 1/6
    diff = actual_pct - expected_pct
    print(f"{symbol:12} | {count:5} | {actual_pct:7.2f}% | {expected_pct:7.2f}% | {diff:+7.2f}%")

total_blocks = defense_results[DefenseDie.SHIELD] + defense_results[DefenseDie.ABSORB]
block_rate = (total_blocks / 100000) * 100
print(f"\nTotal Block Rate: {block_rate:.2f}% (expected 33.33%)")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
