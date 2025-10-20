# Point-Based Army Builder System

**Version:** v5.14b (Army Builder Update)
**Date:** October 20, 2025
**Status:** Proof of Concept Implemented

---

## Overview

Added point-based army composition system to the combat simulator, enabling:
- **Random army generation** within point budgets
- **Difficulty presets** (Easy/Medium/Hard/Boss/Campaign)
- **Support unit integration** (1 point each)
- **Varied army compositions** (Scout swarms, Colossus boss, mixed armies)

This simulates the **campaign/skirmish mode** where players build armies within point budgets, choosing between:
- Many weak units (Scout swarms)
- Few strong units (Colossus + Vanguard)
- Mixed armies with support units

---

## Point Costs

### Casket Classes

| Class | Points | SP | HP | Role |
|-------|--------|----|----|------|
| **Scout** | 2 | 6 | 22 | Fast, fragile, cheap |
| **Warden** | 3 | 5 | 28 | Balanced, standard |
| **Vanguard** | 4 | 4 | 34 | Slow, tanky, expensive |
| **Colossus** | 5 | 4 | 44 | Boss unit (not available at Easy difficulty) |

### Support Units

| Unit | Points | HP | Notes |
|------|--------|----|-------|
| **Support Unit** | 1 | 10 | Simplified (no deck system) |

---

## Difficulty Presets

| Difficulty | Points | Example Compositions |
|------------|--------|---------------------|
| **Easy** | 4 | 2 Scouts OR 1 Vanguard OR 1 Warden + 1 Support OR 4 Supports (Colossus too expensive) |
| **Medium** | 6 | 2 Wardens OR 3 Scouts OR 1 Vanguard + 1 Scout OR 1 Colossus + 1 Support |
| **Hard** | 8 | 2 Vanguards OR 4 Scouts OR 1 Colossus + 1 Warden |
| **Boss** | 12 | 2 Colossi + 1 Warden OR 4 Wardens OR 6 Scouts |
| **Campaign** | 10 | Mixed armies for story missions |

---

## Implementation

### Classes Added

#### 1. **SupportUnit** (Simplified)
```python
@dataclass
class SupportUnit:
    """Simplified support unit for point-based armies"""
    name: str
    faction: str
    hp: int = 10  # Fixed HP (no deck system)
    point_cost: float = 0.5
```

**Note:** Support units use simplified HP system (not deck-as-HP) for faster simulation.

---

#### 2. **Army**
```python
@dataclass
class Army:
    """Represents an army of multiple Caskets and Support Units"""
    faction: str
    caskets: List[Casket]
    support_units: List[SupportUnit]

    @property
    def total_points(self) -> float:
        """Calculate total point cost"""

    @property
    def is_defeated(self) -> bool:
        """Check if all units are dead"""
```

---

#### 3. **Difficulty** (Enum)
```python
class Difficulty(Enum):
    EASY = ("Easy", 4)
    MEDIUM = ("Medium", 6)
    HARD = ("Hard", 8)
    BOSS = ("Boss", 12)
    CAMPAIGN = ("Campaign", 10)
```

---

#### 4. **PointBudgetArmyBuilder**
```python
class PointBudgetArmyBuilder:
    """Builds armies within point budget with random composition"""

    def build_random_army(
        faction: str,
        point_budget: float,
        allow_supports: bool = True,
        support_ratio: float = 0.3  # Max 30% on supports
    ) -> Army

    def build_specific_army(
        faction: str,
        composition: List[CasketClass],
        num_supports: int = 0
    ) -> Army
```

---

## Usage Examples

### Random Army Generation

```python
from equipment_simulator_dice import *

# Load database and create builders
card_db = load_card_database()
deck_builder = DeckBuilder(card_db)
army_builder = PointBudgetArmyBuilder(deck_builder)

# Generate random Easy difficulty army (4 points)
church_army = army_builder.build_random_army(
    faction='church',
    point_budget=4,
    allow_supports=True,
    support_ratio=0.3  # Max 30% on supports
)

# Possible compositions:
# - 1 Colossus (4 pts)
# - 2 Wardens (2+2 pts)
# - 1 Vanguard + 1 Scout (3+1 pts)
# - 1 Vanguard + 2 Supports (3+0.5+0.5 pts)
# - 3 Scouts + 2 Supports (1+1+1+0.5+0.5 pts)
```

---

### Specific Army Composition

```python
# Scout swarm (4 Scouts = 4 points)
scout_swarm = army_builder.build_specific_army(
    faction='elves',
    composition=[CasketClass.SCOUT] * 4,
    num_supports=0
)

# Boss army (1 Colossus = 4 points)
boss_army = army_builder.build_specific_army(
    faction='crucible',
    composition=[CasketClass.COLOSSUS],
    num_supports=0
)

# Mixed army (1 Vanguard + 2 Supports = 4 points)
mixed_army = army_builder.build_specific_army(
    faction='nomads',
    composition=[CasketClass.VANGUARD],
    num_supports=2
)
```

---

### Testing Army Compositions

```bash
# Test army builder with random compositions
python3 test_army_builder.py

# Test faction balance with varied armies (simplified)
python3 faction_balance_ARMIES.py
```

---

## Example Output

```
============================================================
Random Army #1
============================================================
Faction: CHURCH
Total Points: 3.5

Caskets (1):
  1. VANGUARD - 3 pts (4 SP, 34 HP)

Support Units (1):
  1. Church Support 1 - 0.5 pts (10 HP)

Total Units: 2
============================================================
```

---

## Sample Army Compositions (4 Points)

### Scout Swarm Strategy
```
4× Scout
Total: 4 points, 88 HP, 24 SP, 4 units
Strategy: Numbers advantage, high SP pool, fast activation
```

### Balanced Strategy
```
2× Warden
Total: 4 points, 56 HP, 10 SP, 2 units
Strategy: Standard balanced combat
```

### Boss Strategy
```
1× Colossus
Total: 4 points, 44 HP, 4 SP, 1 unit
Strategy: High HP tank, single powerful unit
```

### Mixed Strategy
```
1× Vanguard + 2× Support
Total: 4 points, 34 HP + 20 HP, 4 SP, 3 units
Strategy: Tanky core with support units
```

### Mobile Strategy
```
1× Warden + 1× Scout + 2× Support
Total: 4 points, 50 HP + 20 HP, 11 SP, 4 units
Strategy: Flexible composition with many activations
```

---

## Current Status

### ✅ Implemented
- Point-based army builder class
- Random army generation within budget
- Difficulty presets (Easy/Medium/Hard/Boss/Campaign)
- Support unit integration (simplified)
- Specific army composition builder
- Test scripts (`test_army_builder.py`, `faction_balance_ARMIES.py`)

### ⚠️ Proof of Concept (Not Full Implementation)
- **Simplified power comparison** (no actual combat)
- Power metric: `Total HP + (SP × 5) + (Unit count × 10)`
- No multi-unit combat mechanics

### ❌ Not Implemented (Would Require Major Work)
- **Multi-unit combat simulator**
  - Focus fire AI (which enemy to target)
  - Unit activation order (who acts first)
  - Support unit abilities (healing, buffs, debuffs)
  - Multi-target attacks (AoE, Cleave)
  - Positioning on battlefield (hex grid, flanking)
- **Support unit abilities**
  - Current: Simplified HP sponges
  - Needed: Healing, buffs, debuffs, special actions
- **AI behavior trees for support units**
  - Card database has 60 support units with behavior decks
  - Not integrated into simulator

---

## Limitations

### Current Simplified Test
The `faction_balance_ARMIES.py` script uses **power comparison**, not actual combat:

**Power Score = Total HP + (Total SP × 5) + (Unit count × 10)**

This gives a rough estimate of army strength but does NOT simulate:
- Actual combat (damage, defense dice, attacks)
- Focus fire (concentrating attacks on one target)
- Unit loss (what happens when first unit dies)
- Support abilities (healing, buffs)
- Strategic depth (positioning, flanking, focus targeting)

### Why Full Multi-Unit Combat is Hard

#### 1. **Focus Fire Problem**
```
Army 1: 4 Scouts (22 HP each)
Army 2: 1 Colossus (44 HP)

Question: Do all 4 Scouts attack the Colossus?
Or: Does the Colossus kill Scouts one-by-one?

Answer requires:
- Target selection AI
- Damage allocation logic
- Unit priority system
```

#### 2. **Activation Order Problem**
```
Turn 1: Who acts first?
- Highest SP unit?
- Random order?
- Initiative system?

Answer requires:
- Initiative/speed stat
- Activation queue system
- Turn order logic
```

#### 3. **Support Unit Problem**
```
Support unit should:
- Heal damaged Caskets?
- Buff strongest Casket?
- Debuff enemy?

Answer requires:
- AI behavior trees
- Card database integration (60 support units)
- Action economy system
```

---

## Next Steps

### Option A: Simple Multi-Unit Combat (Recommended)
**Focus fire** all attacks on strongest enemy unit until dead, then next strongest.

**Implementation:**
```python
class MultiUnitCombatSimulator:
    def run_battle(army1, army2):
        while not army1.is_defeated and not army2.is_defeated:
            # Army 1 activates all units
            for unit in army1.active_units:
                target = army2.strongest_unit()  # Focus fire
                damage = unit.attack(target)
                target.take_damage(damage)

            # Army 2 activates all units
            for unit in army2.active_units:
                target = army1.strongest_unit()  # Focus fire
                damage = unit.attack(target)
                target.take_damage(damage)
```

**Pros:**
- Simple to implement (~100 lines)
- Gives realistic combat results
- Tests army compositions

**Cons:**
- No strategic depth (everyone attacks strongest)
- No support unit abilities
- No positioning/flanking

---

### Option B: Full Multi-Unit Combat (Complex)
**Complete system** with AI behavior trees, support abilities, positioning.

**Implementation:**
- ~1000+ lines of new code
- AI behavior tree system
- Support unit ability system
- Hex grid positioning
- Multi-target attacks
- Damage type system (AoE, single-target, cleave)

**Pros:**
- Realistic simulation of actual game
- Tests all mechanics
- Support units functional

**Cons:**
- Requires weeks of work
- Complex debugging
- Slower simulations

---

## Recommendation

**Start with Option A (Simple Multi-Unit Combat)** to test point-based army balance, then add complexity if needed.

Current priority: Fix Dwarves (4% WR) and Church (13% WR) with single-unit combat before adding multi-unit complexity.

---

## Files Modified

### 1. `/workspaces/penance/simulation/equipment_simulator_dice.py`
**Added:**
- `SupportUnit` class (lines 269-283)
- `Army` class (lines 289-316)
- `Difficulty` enum (lines 322-332)
- `PointBudgetArmyBuilder` class (lines 338-429)

**Lines Added:** ~150 lines

---

### 2. New Test Scripts

#### `/workspaces/penance/simulation/test_army_builder.py`
- Demonstrates random army generation
- Shows all difficulty levels
- Tests specific compositions
- **Output:** Sample armies at Easy/Medium/Hard/Boss difficulty

#### `/workspaces/penance/simulation/faction_balance_ARMIES.py`
- Simplified faction balance test
- Power-based comparison (not actual combat)
- Shows army composition variety
- **Output:** Faction power rankings

---

## Documentation

- **This file:** `/workspaces/penance/docs/ARMY-BUILDER-SYSTEM.md`
- **Simulator README:** `/workspaces/penance/simulation/README.md` (updated with army builder info)

---

## Conclusion

Point-based army builder system is **proof of concept complete**. It demonstrates:

✅ Random army generation within budgets
✅ Support unit integration
✅ Varied army compositions (4 Scouts vs 1 Colossus)
✅ Difficulty presets

**Next step:** Implement simple multi-unit combat (Option A) or focus on single-unit balance improvements (Dwarves, Church fixes).

**User request fulfilled:** Army builder system works like "random event with point-based difficulty" as requested.

---

**Document Version:** 1.0
**Author:** Claude (AI Assistant)
**Status:** Proof of Concept Complete
**Next:** Implement simple multi-unit combat OR focus on v5.15 balance fixes
