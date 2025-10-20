#!/usr/bin/env python3
"""
Faction Balance Test with Combo System and SP Banking
Tests all 10 factions with realistic equipment-randomized combat
"""

import sys
sys.path.insert(0, '..')

from equipment_simulator import *
import itertools

# Load card database
card_db = load_card_database()
builder = DeckBuilder(card_db)

FACTIONS = [
    "church",
    "dwarves",
    "elves",
    "crucible",
    "exchange",
    "nomads",
    "bloodlines",
    "emergent",
    "ossuarium",
    "wyrd"
]

print("=" * 80)
print("FACTION BALANCE TEST - Equipment Randomized Combat")
print("=" * 80)
print("\nNew Mechanics:")
print("  - Combo system: 2-card (+1 dmg), 3-card (+2 dmg)")
print("  - SP banking: +2 SP per turn (not reset to max)")
print("  - Positioning: Start 2 hexes apart, movement costs 1 SP/hex")
print("  - Casket classes: Scout (28 HP, 6 SP), Warden (34 HP, 5 SP),")
print("                    Vanguard (40 HP, 4 SP), Colossus (50 HP, 4 SP)")
print("\nTest: 10 factions x 9 matchups x 5 runs = 450 battles")
print("=" * 80)

# Track results
results = {}
for faction in FACTIONS:
    results[faction] = {
        'wins': 0,
        'losses': 0,
        'total_damage_dealt': 0,
        'total_damage_taken': 0,
        'avg_turns': []
    }

# Run all matchups
battle_count = 0
total_battles = len(FACTIONS) * (len(FACTIONS) - 1) // 2 * 5

print(f"\nRunning {total_battles} battles...")

for faction1, faction2 in itertools.combinations(FACTIONS, 2):
    # Run 5 battles per matchup
    for run in range(5):
        battle_count += 1

        # Build Warden-class caskets (standard for balance testing)
        casket1 = builder.build_random_deck(faction1, CasketClass.WARDEN)
        casket2 = builder.build_random_deck(faction2, CasketClass.WARDEN)

        # Run combat
        combat = EquipmentCombatSimulator(casket1, casket2, verbose=False)
        result = combat.run_combat(max_turns=50)

        # Record results
        if result['winner'] == casket1.name:
            results[faction1]['wins'] += 1
            results[faction2]['losses'] += 1
        else:
            results[faction2]['wins'] += 1
            results[faction1]['losses'] += 1

        # Track damage
        damage_dealt_1 = 34 - result['casket2_hp']  # Warden starts with 34 HP
        damage_dealt_2 = 34 - result['casket1_hp']

        results[faction1]['total_damage_dealt'] += damage_dealt_1
        results[faction1]['total_damage_taken'] += damage_dealt_2
        results[faction2]['total_damage_dealt'] += damage_dealt_2
        results[faction2]['total_damage_taken'] += damage_dealt_1

        results[faction1]['avg_turns'].append(result['turns'])
        results[faction2]['avg_turns'].append(result['turns'])

        # Progress indicator
        if battle_count % 50 == 0:
            print(f"  Progress: {battle_count}/{total_battles} battles...")

print(f"\nCompleted {total_battles} battles!")

# Calculate statistics
print("\n" + "=" * 80)
print("FACTION BALANCE RESULTS")
print("=" * 80)

faction_stats = []
for faction in FACTIONS:
    total_games = results[faction]['wins'] + results[faction]['losses']
    win_rate = (results[faction]['wins'] / total_games * 100) if total_games > 0 else 0
    avg_dmg_dealt = results[faction]['total_damage_dealt'] / total_games if total_games > 0 else 0
    avg_dmg_taken = results[faction]['total_damage_taken'] / total_games if total_games > 0 else 0
    avg_turns = sum(results[faction]['avg_turns']) / len(results[faction]['avg_turns']) if results[faction]['avg_turns'] else 0

    faction_stats.append({
        'faction': faction.capitalize(),
        'wins': results[faction]['wins'],
        'losses': results[faction]['losses'],
        'win_rate': win_rate,
        'avg_dmg_dealt': avg_dmg_dealt,
        'avg_dmg_taken': avg_dmg_taken,
        'avg_turns': avg_turns
    })

# Sort by win rate
faction_stats.sort(key=lambda x: x['win_rate'], reverse=True)

# Print results
print(f"\n{'Faction':<12} {'Record':<10} {'WR%':<8} {'Avg Dmg':<10} {'Avg Turns':<10} {'Status':<20}")
print("-" * 80)

for stats in faction_stats:
    record = f"{stats['wins']}-{stats['losses']}"
    status = "✅ BALANCED" if 45 <= stats['win_rate'] <= 55 else "⚠️ NEEDS ADJUSTMENT"

    print(f"{stats['faction']:<12} {record:<10} {stats['win_rate']:>5.1f}%  "
          f"{stats['avg_dmg_dealt']:>4.1f}/{stats['avg_dmg_taken']:<4.1f}  "
          f"{stats['avg_turns']:>6.1f}     {status}")

# Balance score
balanced_count = sum(1 for s in faction_stats if 45 <= s['win_rate'] <= 55)
print("\n" + "=" * 80)
print(f"BALANCE SCORE: {balanced_count}/10 factions in 45-55% WR range")
print("=" * 80)

# Analysis
print("\nKEY INSIGHTS:")
print("-" * 80)

# Find outliers
overpowered = [s for s in faction_stats if s['win_rate'] > 55]
underpowered = [s for s in faction_stats if s['win_rate'] < 45]

if overpowered:
    print(f"\nOVERPOWERED (>55% WR):")
    for s in overpowered:
        print(f"  - {s['faction']}: {s['win_rate']:.1f}% WR (Avg {s['avg_dmg_dealt']:.1f} dmg/game)")

if underpowered:
    print(f"\nUNDERPOWERED (<45% WR):")
    for s in underpowered:
        print(f"  - {s['faction']}: {s['win_rate']:.1f}% WR (Avg {s['avg_dmg_dealt']:.1f} dmg/game)")

if balanced_count == 10:
    print("\n🎉 PERFECT BALANCE! All 10 factions in 45-55% WR range!")
elif balanced_count >= 7:
    print(f"\n✅ GOOD BALANCE: {balanced_count}/10 factions balanced")
elif balanced_count >= 5:
    print(f"\n⚠️ MODERATE BALANCE: {balanced_count}/10 factions balanced (needs work)")
else:
    print(f"\n❌ POOR BALANCE: Only {balanced_count}/10 factions balanced (major issues)")

# Combat length analysis
avg_combat_length = sum(s['avg_turns'] for s in faction_stats) / len(faction_stats)
print(f"\nAverage combat length: {avg_combat_length:.1f} turns")

if avg_combat_length < 8:
    print("  ⚠️ Combats are very quick (burst damage meta)")
elif avg_combat_length < 12:
    print("  ✅ Good combat length (tactical play)")
else:
    print("  ⚠️ Combats are very long (may need more damage)")

print("\n" + "=" * 80)
