# Archived Simulation Scripts

This directory contains older simulation scripts that have been superseded by the main simulation engine.

## Archived Files

### `faction_balance_DICE.py`
- **Purpose:** 1v1 Casket battles with dice mechanics
- **Status:** Superseded by `faction_balance_MULTIUNIT.py`
- **Reason:** Only tests single-unit battles, doesn't include army composition

### `faction_balance_ARMIES.py`
- **Purpose:** Army composition testing with simplified power metrics
- **Status:** Superseded by `faction_balance_MULTIUNIT.py`
- **Reason:** Uses simplified power calculation instead of actual combat simulation

### `test_army_builder.py`
- **Purpose:** Demonstrates point-based army building
- **Status:** Functionality integrated into main simulation
- **Reason:** Testing/demo script, not needed for production runs

### `test_dice_probabilities.py`
- **Purpose:** Validates dice probability distributions
- **Status:** Validation complete
- **Reason:** One-time testing script for dice mechanics

### `test_multiunit_combat.py`
- **Purpose:** Basic multi-unit combat demonstration
- **Status:** Superseded by `faction_balance_MULTIUNIT.py`
- **Reason:** Redundant with main simulation script

## Active Simulation Files

The current active simulation system consists of:

1. **`equipment_simulator_dice.py`** - Core simulation engine
   - Custom dice mechanics (Attack/Defense)
   - Combat simulation
   - Army building
   - Multi-unit combat
   - Support units

2. **`faction_balance_MULTIUNIT.py`** - Main simulation script
   - Full multi-unit army battles
   - Focus fire mechanics
   - Random army compositions
   - Comprehensive faction balance testing

## Running Simulations

To run the complete faction balance test:

```bash
cd simulation
python3 faction_balance_MULTIUNIT.py
```

This will simulate all 10 factions against each other with multi-unit armies.
