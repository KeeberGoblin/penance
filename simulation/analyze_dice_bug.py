#!/usr/bin/env python3
"""
Analyze the dice probability bug
"""

# According to dice-reference.md line 36-37:
# Face 6 = JAM = 0 value
# Die faces: 1, 2, 3, 4, 5, 0 (JAM on face 6)

# Current implementation in code (line 23):
# FACES = [1, 2, 3, 4, 5, 0]

# This means each face appears with probability 1/6

# Let's calculate the CORRECT probabilities for 2d6 with faces [1,2,3,4,5,0]

print("=" * 80)
print("CORRECT PROBABILITY CALCULATION FOR ATTACK DICE")
print("=" * 80)
print()
print("Die faces: 1, 2, 3, 4, 5, 0 (JAM)")
print("Each face: 1/6 probability")
print()

# Create all possible combinations
outcomes = {}
for die1 in [1, 2, 3, 4, 5, 0]:
    for die2 in [1, 2, 3, 4, 5, 0]:
        total = die1 + die2
        if total not in outcomes:
            outcomes[total] = []
        outcomes[total].append((die1, die2))

print("Total | Combinations | Count | Probability")
print("-" * 60)

total_combinations = 0
for total in sorted(outcomes.keys()):
    combos = outcomes[total]
    count = len(combos)
    prob = (count / 36) * 100
    total_combinations += count
    print(f"{total:5} | {str(combos):50s} | {count:5} | {prob:6.2f}%")

print(f"\nTotal combinations: {total_combinations} (should be 36)")

print("\n" + "=" * 80)
print("ANALYSIS: WHY ARE PROBABILITIES WRONG?")
print("=" * 80)
print()

print("Expected probabilities (from dice-reference.md line 473-484):")
print("  Total 8: 13.89% (5/36)")
print("  Total 9: 11.11% (4/36)")
print()
print("Actual probabilities from test:")
print("  Total 8: 8.27% (approximately 3/36)")
print("  Total 9: 5.61% (approximately 2/36)")
print()
print("FINDING: The test shows ~3/36 for total 8, but we should have 5/36!")
print()

# Count from our calculation
total_8_count = len(outcomes[8])
total_9_count = len(outcomes[9])

print(f"From combination analysis:")
print(f"  Total 8: {total_8_count} combinations = {(total_8_count/36)*100:.2f}%")
print(f"  Total 9: {total_9_count} combinations = {(total_9_count/36)*100:.2f}%")
print()

print("HYPOTHESIS: The dice-reference.md expected probabilities are WRONG!")
print("They assume normal 2d6 dice (faces 1-6), not custom dice with JAM face.")
print()

print("Let's check what normal 2d6 would give:")
normal_outcomes = {}
for die1 in [1, 2, 3, 4, 5, 6]:
    for die2 in [1, 2, 3, 4, 5, 6]:
        total = die1 + die2
        if total not in normal_outcomes:
            normal_outcomes[total] = 0
        normal_outcomes[total] += 1

print("\nNormal 2d6 (faces 1-6):")
print("Total | Count | Probability")
print("-" * 40)
for total in sorted(normal_outcomes.keys()):
    count = normal_outcomes[total]
    prob = (count / 36) * 100
    print(f"{total:5} | {count:5} | {prob:6.2f}%")

print("\n" + "=" * 80)
print("CONCLUSION")
print("=" * 80)
print()
print("BUG #1: The dice-reference.md document has INCORRECT probability tables!")
print("        It shows probabilities for normal 2d6, not custom dice with JAM face.")
print()
print("The simulator implementation is CORRECT for dice with faces [1,2,3,4,5,0].")
print()
print("Expected rates from dice-reference.md line 488-493:")
print("  5+ hit: 72.22%  <- This is for NORMAL 2d6, not JAM dice!")
print()
print("Actual rate with JAM dice [1,2,3,4,5,0]:")
print("  5+ hit: 58.27%  <- This is CORRECT for the actual dice!")
print()
print("=" * 80)

# Calculate hit rates for custom dice
print("\nCORRECT Hit Rates for Custom Dice [1,2,3,4,5,0]:")
print("Target | Hits/36 | Probability")
print("-" * 40)
for target in [4, 5, 6, 7, 8, 9, 10]:
    hits = sum(len(combos) for total, combos in outcomes.items() if total >= target)
    prob = (hits / 36) * 100
    print(f"{target:6}+ | {hits:7}/36 | {prob:6.2f}%")
