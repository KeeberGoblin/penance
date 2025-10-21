#!/usr/bin/env python3
"""
Test v5.15 mechanics implementation
Run battles with factions that have resource mechanics to verify they work
"""

import sys
sys.path.append('.')

from equipment_simulator_dice import *

print("=" * 80)
print("V5.15 MECHANICS VERIFICATION TEST")
print("=" * 80)

# Load card database
card_db = load_card_database()
builder = DeckBuilder(card_db)

# Test 1: Dwarves (Rune Counters)
print("\n" + "=" * 80)
print("TEST 1: DWARVES vs ELVES (Testing Rune Counters)")
print("=" * 80)
dwarves = builder.build_random_deck("dwarves", CasketClass.WARDEN)
elves = builder.build_random_deck("elves", CasketClass.WARDEN)
simulator = DiceCombatSimulator(dwarves, elves, verbose=True)
result = simulator.run_combat(max_turns=10)
print(f"\nWinner: {result['winner']}")
print(f"Dwarves HP: {dwarves.hp}, Rune Counters: {dwarves.rune_counters}")
print(f"Elves HP: {elves.hp}, Bleed Stacks: {elves.bleed_stacks}")

# Test 2: Bloodlines (Biomass)
print("\n" + "=" * 80)
print("TEST 2: BLOODLINES vs NOMADS (Testing Biomass)")
print("=" * 80)
bloodlines = builder.build_random_deck("vestige-bloodlines", CasketClass.WARDEN)
nomads = builder.build_random_deck("nomads", CasketClass.WARDEN)
simulator = DiceCombatSimulator(bloodlines, nomads, verbose=True)
result = simulator.run_combat(max_turns=10)
print(f"\nWinner: {result['winner']}")
print(f"Bloodlines HP: {bloodlines.hp}, Biomass: {bloodlines.biomass_tokens}")
print(f"Nomads HP: {nomads.hp}")

# Test 3: Crucible (Forge Tokens)
print("\n" + "=" * 80)
print("TEST 3: CRUCIBLE vs OSSUARIUM (Testing Forge Tokens)")
print("=" * 80)
crucible = builder.build_random_deck("crucible", CasketClass.WARDEN)
ossuarium = builder.build_random_deck("ossuarium", CasketClass.WARDEN)
simulator = DiceCombatSimulator(crucible, ossuarium, verbose=True)
result = simulator.run_combat(max_turns=10)
print(f"\nWinner: {result['winner']}")
print(f"Crucible HP: {crucible.hp}, Forge Tokens: {crucible.forge_tokens}")
print(f"Ossuarium HP: {ossuarium.hp}")

# Test 4: Exchange (Credits)
print("\n" + "=" * 80)
print("TEST 4: EXCHANGE vs EMERGENT (Testing Credits)")
print("=" * 80)
exchange = builder.build_random_deck("exchange", CasketClass.WARDEN)
emergent = builder.build_random_deck("emergent", CasketClass.WARDEN)
simulator = DiceCombatSimulator(exchange, emergent, verbose=True)
result = simulator.run_combat(max_turns=10)
print(f"\nWinner: {result['winner']}")
print(f"Exchange HP: {exchange.hp}, Credits: {exchange.credit_tokens}")
print(f"Emergent HP: {emergent.hp}")

# Test 5: Church (Discard)
print("\n" + "=" * 80)
print("TEST 5: CHURCH vs WYRD (Testing Discard Mechanics)")
print("=" * 80)
church = builder.build_random_deck("church", CasketClass.WARDEN)
wyrd = builder.build_random_deck("wyrd-conclave", CasketClass.WARDEN)
simulator = DiceCombatSimulator(church, wyrd, verbose=True)
result = simulator.run_combat(max_turns=10)
print(f"\nWinner: {result['winner']}")
print(f"Church HP: {church.hp}, Discards This Turn: {church.discards_this_turn}")
print(f"Wyrd HP: {wyrd.hp}")

print("\n" + "=" * 80)
print("MECHANICS TEST COMPLETE")
print("=" * 80)
