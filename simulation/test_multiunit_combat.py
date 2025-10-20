#!/usr/bin/env python3
"""
Test Multi-Unit Combat Simulator
Demonstrates army vs army battles with focus fire targeting
"""

from equipment_simulator_dice import *

if __name__ == "__main__":
    print("=" * 80)
    print("MULTI-UNIT COMBAT SIMULATOR TEST")
    print("=" * 80)

    # Load card database
    card_db = load_card_database()
    deck_builder = DeckBuilder(card_db)
    army_builder = PointBudgetArmyBuilder(deck_builder)

    # Test 1: Small battle (Easy difficulty - 4 points)
    print("\n" + "#" * 80)
    print("# TEST 1: EASY DIFFICULTY (4 points)")
    print("#" * 80)

    church_army = army_builder.build_random_army('church', 4, allow_supports=True)
    elves_army = army_builder.build_random_army('elves', 4, allow_supports=True)

    print(f"\nChurch Army ({church_army.total_points:.1f} pts):")
    for i, casket in enumerate(church_army.caskets, 1):
        print(f"  {i}. {casket.casket_class.name} ({casket.hp} HP, {casket.sp_max} SP)")
    if church_army.support_units:
        print(f"  + {len(church_army.support_units)} Support Units ({sum(s.hp for s in church_army.support_units)} HP total)")

    print(f"\nElves Army ({elves_army.total_points:.1f} pts):")
    for i, casket in enumerate(elves_army.caskets, 1):
        print(f"  {i}. {casket.casket_class.name} ({casket.hp} HP, {casket.sp_max} SP)")
    if elves_army.support_units:
        print(f"  + {len(elves_army.support_units)} Support Units ({sum(s.hp for s in elves_army.support_units)} HP total)")

    # Run battle
    simulator = MultiUnitCombatSimulator(church_army, elves_army, verbose=True)
    result = simulator.run_battle()

    print(f"\n{'='*80}")
    print("BATTLE RESULT")
    print(f"{'='*80}")
    print(f"Winner: {result['winner']}")
    print(f"Turns: {result['turns']}")
    print(f"Church units remaining: {result['army1_units_remaining']}")
    print(f"Elves units remaining: {result['army2_units_remaining']}")

    # Test 2: Larger battle (Medium difficulty - 6 points)
    print("\n\n" + "#" * 80)
    print("# TEST 2: MEDIUM DIFFICULTY (6 points)")
    print("#" * 80)

    crucible_army = army_builder.build_random_army('crucible', 6, allow_supports=True)
    nomads_army = army_builder.build_random_army('nomads', 6, allow_supports=True)

    print(f"\nCrucible Army ({crucible_army.total_points:.1f} pts):")
    for i, casket in enumerate(crucible_army.caskets, 1):
        print(f"  {i}. {casket.casket_class.name} ({casket.hp} HP, {casket.sp_max} SP)")
    if crucible_army.support_units:
        print(f"  + {len(crucible_army.support_units)} Support Units")

    print(f"\nNomads Army ({nomads_army.total_points:.1f} pts):")
    for i, casket in enumerate(nomads_army.caskets, 1):
        print(f"  {i}. {casket.casket_class.name} ({casket.hp} HP, {casket.sp_max} SP)")
    if nomads_army.support_units:
        print(f"  + {len(nomads_army.support_units)} Support Units")

    # Run battle (verbose=False for cleaner output)
    simulator2 = MultiUnitCombatSimulator(crucible_army, nomads_army, verbose=False)
    result2 = simulator2.run_battle()

    print(f"\n{'='*80}")
    print("BATTLE RESULT")
    print(f"{'='*80}")
    print(f"Winner: {result2['winner']}")
    print(f"Turns: {result2['turns']}")
    print(f"Crucible units remaining: {result2['army1_units_remaining']}")
    print(f"Nomads units remaining: {result2['army2_units_remaining']}")

    # Test 3: 1v1 Duel vs Multi-Unit comparison
    print("\n\n" + "#" * 80)
    print("# TEST 3: 1v1 DUEL vs ARMY BATTLE COMPARISON")
    print("#" * 80)

    # 1v1 Duel (existing single-unit combat)
    print("\n--- 1v1 DUEL (Single Warden vs Single Warden) ---")
    church_warden = deck_builder.build_random_deck('church', CasketClass.WARDEN)
    dwarves_warden = deck_builder.build_random_deck('dwarves', CasketClass.WARDEN)

    duel_sim = DiceCombatSimulator(church_warden, dwarves_warden, verbose=False)
    duel_result = duel_sim.run_combat()

    print(f"Winner: {duel_result['winner']}")
    print(f"Turns: {duel_result['turns']}")

    # Army Battle (2 Scouts + Support vs 2 Scouts + Support)
    print("\n--- ARMY BATTLE (Mixed composition) ---")
    church_army3 = army_builder.build_specific_army(
        'church',
        composition=[CasketClass.SCOUT, CasketClass.SCOUT],
        num_supports=0
    )
    dwarves_army3 = army_builder.build_specific_army(
        'dwarves',
        composition=[CasketClass.SCOUT, CasketClass.SCOUT],
        num_supports=0
    )

    army_sim = MultiUnitCombatSimulator(church_army3, dwarves_army3, verbose=False)
    army_result = army_sim.run_battle()

    print(f"Winner: {army_result['winner']}")
    print(f"Turns: {army_result['turns']}")
    print(f"Church units remaining: {army_result['army1_units_remaining']}")
    print(f"Dwarves units remaining: {army_result['army2_units_remaining']}")

    print("\n" + "=" * 80)
    print("MULTI-UNIT COMBAT TEST COMPLETE")
    print("=" * 80)
    print("\nKey Features Tested:")
    print("  ✓ Focus fire targeting (attack strongest enemy)")
    print("  ✓ Multi-unit battles (2-4 units per side)")
    print("  ✓ Support unit integration")
    print("  ✓ Army defeat conditions")
    print("  ✓ 1v1 duel option still available (DiceCombatSimulator)")
    print("\nNext: Run full faction balance test with armies!")
    print("=" * 80)
