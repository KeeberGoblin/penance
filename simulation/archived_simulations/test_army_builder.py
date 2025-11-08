#!/usr/bin/env python3
"""
Test script for Point-Based Army Builder
Demonstrates random army generation at different difficulty levels
"""

from equipment_simulator_dice import *
import random

def print_army_composition(army: Army, title: str):
    """Pretty print army composition"""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Faction: {army.faction.upper()}")
    print(f"Total Points: {army.total_points:.1f}")
    print(f"\nCaskets ({len(army.caskets)}):")
    for i, casket in enumerate(army.caskets, 1):
        print(f"  {i}. {casket.casket_class.name} - {casket.casket_class.point_cost} pts "
              f"({casket.casket_class.sp_max} SP, {casket.casket_class.deck_size} HP)")

    if army.support_units:
        print(f"\nSupport Units ({len(army.support_units)}):")
        for i, support in enumerate(army.support_units, 1):
            print(f"  {i}. {support.name} - {support.point_cost} pts ({support.hp} HP)")

    print(f"\nTotal Units: {len(army.active_units)}")
    print("="*60)

if __name__ == "__main__":
    print("=" * 80)
    print("POINT-BASED ARMY BUILDER TEST")
    print("=" * 80)

    # Load card database
    card_db = load_card_database()
    deck_builder = DeckBuilder(card_db)
    army_builder = PointBudgetArmyBuilder(deck_builder)

    # Test different difficulty levels
    difficulties = [
        Difficulty.EASY,
        Difficulty.MEDIUM,
        Difficulty.HARD,
        Difficulty.BOSS,
        Difficulty.CAMPAIGN
    ]

    factions = ['church', 'elves', 'nomads', 'crucible']

    for difficulty in difficulties:
        print(f"\n\n{'#'*80}")
        print(f"# {difficulty.name} DIFFICULTY ({difficulty.point_budget} points)")
        print(f"{'#'*80}")

        # Generate 3 random armies for this difficulty
        for i in range(3):
            faction = random.choice(factions)
            army = army_builder.build_random_army(
                faction=faction,
                point_budget=difficulty.point_budget,
                allow_supports=True,
                support_ratio=0.3  # Max 30% on supports
            )
            print_army_composition(army, f"Random Army #{i+1}")

    # Test specific compositions
    print(f"\n\n{'#'*80}")
    print(f"# SPECIFIC ARMY COMPOSITIONS")
    print(f"{'#'*80}")

    # Scout Swarm (4 points)
    scout_swarm = army_builder.build_specific_army(
        faction='elves',
        composition=[CasketClass.SCOUT] * 4,
        num_supports=0
    )
    print_army_composition(scout_swarm, "Scout Swarm (4 Scouts)")

    # Balanced Army (4 points)
    balanced = army_builder.build_specific_army(
        faction='church',
        composition=[CasketClass.WARDEN, CasketClass.WARDEN],
        num_supports=0
    )
    print_army_composition(balanced, "Balanced Army (2 Wardens)")

    # Boss Army (4 points)
    boss = army_builder.build_specific_army(
        faction='crucible',
        composition=[CasketClass.COLOSSUS],
        num_supports=0
    )
    print_army_composition(boss, "Boss Army (1 Colossus)")

    # Mixed Army with Supports (4 points total)
    mixed = army_builder.build_specific_army(
        faction='nomads',
        composition=[CasketClass.VANGUARD],  # 3 points
        num_supports=2  # 2 × 0.5 = 1 point
    )
    print_army_composition(mixed, "Mixed Army (1 Vanguard + 2 Supports)")

    print("\n" + "="*80)
    print("ARMY BUILDER TEST COMPLETE")
    print("="*80)
    print("\nExamples show:")
    print("  - Random army generation within point budgets")
    print("  - Different difficulty levels (4-12 points)")
    print("  - Support unit integration (0.5 points each)")
    print("  - Specific army compositions")
    print("\nNext step: Integrate into faction balance testing")
    print("="*80)
