#!/usr/bin/env python3
"""
Faction Balance Test with Point-Based Armies
Tests faction balance with varied army compositions at different difficulty levels
"""

from equipment_simulator_dice import *
import random

def test_army_matchup(
    faction1: str,
    faction2: str,
    army_builder: PointBudgetArmyBuilder,
    point_budget: float,
    runs: int = 3
) -> dict:
    """
    Test matchup between two factions with random army compositions

    NOTE: This is a simplified test. Full multi-unit combat would require
    updating the combat simulator to handle multiple units, focus fire, etc.

    For now, we compare army total power (HP + SP + unit count)
    """
    faction1_power = []
    faction2_power = []

    for _ in range(runs):
        # Generate random armies
        army1 = army_builder.build_random_army(faction1, point_budget, allow_supports=True)
        army2 = army_builder.build_random_army(faction2, point_budget, allow_supports=True)

        # Calculate total army power (simplified metric)
        # Power = Total HP + (Total SP × 5) + (Unit count × 10)
        def calc_power(army):
            total_hp = sum(c.hp for c in army.caskets)
            total_sp = sum(c.sp_max for c in army.caskets)
            unit_count = len(army.active_units)
            return total_hp + (total_sp * 5) + (unit_count * 10)

        power1 = calc_power(army1)
        power2 = calc_power(army2)

        faction1_power.append(power1)
        faction2_power.append(power2)

    # Calculate average power
    avg_power1 = sum(faction1_power) / len(faction1_power)
    avg_power2 = sum(faction2_power) / len(faction2_power)

    # Determine winner by average power
    if avg_power1 > avg_power2:
        winner = faction1
        power_diff = avg_power1 - avg_power2
    else:
        winner = faction2
        power_diff = avg_power2 - avg_power1

    return {
        'faction1': faction1,
        'faction2': faction2,
        'faction1_avg_power': avg_power1,
        'faction2_avg_power': avg_power2,
        'winner': winner,
        'power_difference': power_diff,
        'power_ratio': max(avg_power1, avg_power2) / min(avg_power1, avg_power2)
    }


if __name__ == "__main__":
    print("=" * 80)
    print("FACTION BALANCE TEST - POINT-BASED ARMIES (SIMPLIFIED)")
    print("=" * 80)
    print("\nNOTE: This is a simplified test using army power metrics.")
    print("Full multi-unit combat simulation would require:")
    print("  - Focus fire AI")
    print("  - Unit activation order")
    print("  - Support unit abilities")
    print("  - Multi-target attacks")
    print("\n" + "=" * 80)

    # Load card database
    card_db = load_card_database()
    deck_builder = DeckBuilder(card_db)
    army_builder = PointBudgetArmyBuilder(deck_builder)

    # Test factions
    factions = [
        'church', 'dwarves', 'elves', 'nomads',
        'crucible', 'ossuarium', 'emergent', 'exchange',
        'vestige-bloodlines', 'wyrd-conclave'
    ]

    # Test at EASY difficulty (4 points)
    difficulty = Difficulty.EASY
    print(f"\nTesting at {difficulty.name} difficulty ({difficulty.point_budget} points)")
    print(f"Army compositions: Random (Scouts/Wardens/Vanguards/Colossus + Supports)")
    print("=" * 80)

    # Generate sample armies for each faction to show variety
    print("\nSAMPLE ARMY COMPOSITIONS:")
    print("-" * 80)

    for faction in factions[:3]:  # Show 3 examples
        print(f"\n{faction.upper()} Sample Armies:")
        for i in range(2):
            army = army_builder.build_random_army(
                faction=faction,
                point_budget=difficulty.point_budget,
                allow_supports=True,
                support_ratio=0.3
            )

            composition = []
            for casket in army.caskets:
                composition.append(casket.casket_class.name)
            if army.support_units:
                composition.append(f"{len(army.support_units)}× Support")

            total_hp = sum(c.hp for c in army.caskets)
            print(f"  Army {i+1}: {' + '.join(composition)} "
                  f"({army.total_points:.1f} pts, {total_hp} HP, {len(army.active_units)} units)")

    print("\n" + "=" * 80)
    print("POWER-BASED BALANCE TEST")
    print("=" * 80)
    print("\nTesting all faction matchups (simplified power comparison)...")

    # Track faction power scores
    faction_power_scores = {f: [] for f in factions}

    # Test all matchups
    matchups_tested = 0
    for i, faction1 in enumerate(factions):
        for faction2 in factions[i+1:]:
            result = test_army_matchup(
                faction1, faction2,
                army_builder,
                difficulty.point_budget,
                runs=3
            )

            # Record power scores
            faction_power_scores[faction1].append(result['faction1_avg_power'])
            faction_power_scores[faction2].append(result['faction2_avg_power'])

            matchups_tested += 1

    print(f"\nCompleted {matchups_tested} matchups!")

    # Calculate average power for each faction
    print("\n" + "=" * 80)
    print("FACTION POWER RANKINGS (SIMPLIFIED)")
    print("=" * 80)

    faction_avg_power = {}
    for faction in factions:
        if faction_power_scores[faction]:
            avg = sum(faction_power_scores[faction]) / len(faction_power_scores[faction])
            faction_avg_power[faction] = avg

    # Sort by power
    sorted_factions = sorted(faction_avg_power.items(), key=lambda x: x[1], reverse=True)

    print(f"\n{'Rank':<6} {'Faction':<22} {'Avg Power':<12} {'Relative':<10}")
    print("-" * 80)

    max_power = sorted_factions[0][1]
    for rank, (faction, power) in enumerate(sorted_factions, 1):
        relative = (power / max_power) * 100
        print(f"{rank:<6} {faction.capitalize():<22} {power:<12.1f} {relative:<10.1f}%")

    print("\n" + "=" * 80)
    print("INTERPRETATION")
    print("=" * 80)
    print("\nPower Score = Total HP + (Total SP × 5) + (Unit count × 10)")
    print("\nThis simplified test shows:")
    print("  ✓ Army composition variety (Scouts, Wardens, Vanguards, Colossus)")
    print("  ✓ Support unit integration (0.5 points each)")
    print("  ✓ Point budget balance (4 points = varied compositions)")
    print("\nLimitations:")
    print("  ✗ No actual combat simulation (power comparison only)")
    print("  ✗ No focus fire or targeting AI")
    print("  ✗ No multi-unit combat mechanics")
    print("\nNext step: Implement full multi-unit combat simulator")
    print("=" * 80)
