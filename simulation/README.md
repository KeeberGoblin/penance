# Penance Combat Simulator

**Version:** 5.14 (Complete Deck Implementation)
**Date:** October 20, 2025

---

## Overview

This is the complete combat simulator for Penance, a tactical card-based combat game where your **deck is your HP**. The simulator implements:

- **Custom Dice Mechanics**: 2d6 attack dice, 1d6 defense dice per damage
- **Complete Deck System**: Faction cards + Universal cards + Equipment cards
- **Resource Economies**: Credits, Biomass, Faith, Forge tokens, Bleed stacks
- **10 Asymmetric Factions**: Each with unique mechanics and strategies

---

## Quick Start

### Run a Single Combat Test
```bash
python3 equipment_simulator_dice.py
```

This runs a test battle between Church and Wyrd-Conclave factions with verbose output showing every turn, attack roll, and damage calculation.

### Run Full Faction Balance Test
```bash
python3 faction_balance_DICE.py
```

This runs 225 battles (10 factions × 9 matchups × 5 runs) and outputs:
- Win rates for each faction
- Balance score (how many factions are in 45-55% WR range)
- Hit rate statistics and dice mechanics analysis

**Runtime:** ~3 minutes for 225 battles

### NEW: Test Point-Based Army Builder (v5.14b)
```bash
# Test random army generation at different difficulty levels
python3 test_army_builder.py

# Test faction balance with varied army compositions (simplified)
python3 faction_balance_ARMIES.py
```

This demonstrates the point-based army builder system:
- Random army generation within point budgets (4-12 points)
- Difficulty presets (Easy/Medium/Hard/Boss/Campaign)
- Support unit integration (0.5 points each)
- Varied compositions (Scout swarms, Colossus boss, mixed armies)

**See:** [/docs/ARMY-BUILDER-SYSTEM.md](/docs/ARMY-BUILDER-SYSTEM.md) for details

---

## Files

### Active Scripts

#### `equipment_simulator_dice.py`
**Primary simulator** - Complete implementation with:
- FactionCard class (gambits, passives, movement, etc.)
- EquipmentCard class (attacks, reactives, utilities)
- Custom dice mechanics (2d6 attack, 1d6 defense)
- Deck-as-HP system
- Resource economy tracking (Credits, Biomass, etc.)
- 10 faction-specific mechanics

**Usage:**
```python
from equipment_simulator_dice import *

# Load card database
card_db = load_card_database()
builder = DeckBuilder(card_db)

# Build caskets with complete deck system
casket1 = builder.build_random_deck("church", CasketClass.WARDEN)
casket2 = builder.build_random_deck("elves", CasketClass.WARDEN)

# Run combat
simulator = DiceCombatSimulator(casket1, casket2, verbose=True)
result = simulator.run_combat()
```

#### `faction_balance_DICE.py`
**Balance testing script** - Runs all matchups and calculates win rates

**Usage:**
```bash
python3 faction_balance_DICE.py
```

**Output:**
```
================================================================================
FACTION BALANCE RESULTS (WITH DICE MECHANICS)
================================================================================

Faction              Record       WR%      Hit%     Rolls    Status
--------------------------------------------------------------------------------
Crucible             36-9          80.0%   52.3%  459      ⚠️ NEEDS ADJUSTMENT
Ossuarium            23-22         51.1%   57.5%  656      ✅ BALANCED
Dwarves              2-43           4.4%   55.0%  456      ⚠️ NEEDS ADJUSTMENT

================================================================================
BALANCE SCORE: 1/10 factions in 45-55% WR range
================================================================================
```

### Archived Files

#### `archived-scripts/`
- `equipment_simulator.py` - Old simulator without dice mechanics
- `faction_balance_with_combos.py` - Old balance tester (pre-dice)
- `test_sp_banking.py` - SP banking feature test

#### `archived-rounds/`
- Old markdown analysis files from v5.1-v5.13 (equipment-only testing)
- Historical balance reports

---

## Complete Deck System

### Deck Composition (v5.14)

Each casket's deck contains:

1. **6 Faction Cards** (randomly chosen from 21 available)
   - Gambits (strategic one-time effects)
   - Passives (ongoing effects)
   - Movement (repositioning)
   - Reactive-defense (counter-attacks)
   - Utilities (support effects)

2. **10 Universal Cards** (all included)
   - Movement cards (Desperate Lunge, etc.)
   - Generic utilities available to all factions

3. **Equipment Cards** (varies by faction)
   - 2 equipment items chosen from available pool
   - Each item has 5-8 cards (attacks, reactives, utilities)
   - Total: ~13-19 equipment cards

**Total Deck Size:** ~29-35 cards (varies by equipment choice)

### Why Complete Deck Matters

**v5.1-v5.13 (Equipment-Only):**
- Only tested equipment cards (~13-19 per deck)
- Missing 57% of cards (faction + universal)
- Token economies broken (Exchange: 0% WR)
- False balance data

**v5.14 (Complete Deck):**
- Tests all card types (~29-35 per deck)
- Token economies functional (Exchange: 67% WR)
- Accurate faction balance data
- Strategic depth from faction card choices

---

## Dice Mechanics

### Attack Dice (2d6 Custom)

**Faces:** 1, 2, 3, 4, 5, 0 (JAM)

**Attack Results:**
- **Catastrophic Failure** (2 JAMs): Weapon jams, +2 Heat, next attack -2 damage
- **Miss** (< 5): No effect
- **Hit** (5-6): Normal damage
- **Strong Hit** (7-8): +1 damage
- **Critical Hit** (9): +2 damage, bypass 1 Defense die
- **Execution** (Double 5s, total 10): Destroy component, bypass all defense

**To-Hit Target Number:** 5+ (base)
- Modified by range, enemy evasion, buffs/debuffs

### Defense Dice (1d6 per damage)

**Faces (6 symbols):**
- **Shield** (⛨): Block 1 damage
- **Absorb** (◎): Block 1 damage
- **Flesh Wound** (○): Take damage (no effect)
- **Critical** (⚠): Take damage + 1 Component Damage
- **Pierce** (⚡): Take damage, disable reactive cards
- **Heat** (🔥): Take damage + 1 Heat

**Example:**
```
Attacker deals 5 damage
→ Defender rolls 5 defense dice
→ Results: 2 Shields, 1 Absorb, 1 Flesh Wound, 1 Critical
→ Blocks: 2 + 1 = 3 damage blocked
→ Actual damage: 5 - 3 = 2 HP lost
→ Side effects: +1 Component Damage
```

---

## Faction Mechanics

### Resource Economies

| Faction | Resource | Generation | Spending | Cap |
|---------|----------|------------|----------|-----|
| **Exchange** | Credits | +1-2 per card | "Spend X Credits: effect" | None |
| **Bloodlines** | Biomass | +1-2 per attack | "Spend X Biomass: effect" | None |
| **Church** | Faith | +1 per gambit | "Spend X Faith: heal/buff" | 5 |
| **Crucible** | Forge | +1 per attack | "Spend X Forge: upgrade" | 5 |
| **Elves** | Bleed | +1-2 per attack | 1 dmg/turn per stack | 4 |

### Unique Mechanics

- **Church:** Self-harm gambits (discard cards for buffs), Faith healing
- **Dwarves:** Crafting system (currently non-functional in simulator)
- **Elves:** Bleed stacks (damage over time), Thornvine entangle
- **Nomads:** High mobility, ranged attacks
- **Ossuarium:** Durability, graveyard mechanics
- **Crucible:** Forge tokens, elemental damage
- **Emergent:** Hive-mind bonuses, metamorph states
- **Exchange:** Credit economy, contract blade combos
- **Bloodlines:** Biomass mutations, savage damage spikes
- **Wyrd-Conclave:** Chaos magic, random effects

---

## Current Balance Status (v5.14)

**Balanced (45-55% WR):** 1/10 factions
- ✅ Ossuarium: 51.1% WR

**Overpowered (>55% WR):** 5/10 factions
- ⚠️ Crucible: 80.0% WR
- ⚠️ Nomads: 75.6% WR
- ⚠️ Bloodlines: 73.3% WR
- ⚠️ Exchange: 66.7% WR
- ⚠️ Emergent: 64.4% WR

**Underpowered (<45% WR):** 4/10 factions
- ⚠️ Wyrd-Conclave: 42.2% WR
- ⚠️ Elves: 28.9% WR
- ⚠️ Church: 13.3% WR
- ❌ Dwarves: 4.4% WR (CRITICAL)

**Balance Goal:** 7-8/10 factions in 45-55% WR range

---

## Development History

### Major Versions

- **v5.1-v5.7:** Equipment-only testing (incomplete)
- **v5.8-v5.13:** Equipment balance attempts (6 major patches)
  - Church yo-yoed from 9% → 98% → 9% WR
  - Exchange broken at 0% WR (token economy missing)
- **v5.14:** Complete deck implementation (current)
  - Added faction cards (6 of 21 per deck)
  - Added universal cards (10 per deck)
  - First accurate balance data

### Key Breakthroughs

1. **Type Capitalization Bug** (v5.9, v5.10, v5.11)
   - Lowercase "type": "attack" cards ignored by simulator
   - Single-character fix caused +27% to +76% WR swings

2. **Card Pool Size Discovery** (v5.12-v5.13)
   - Church had 56 equipment cards vs 13-18 for others
   - Caused 98% WR (massive advantage)
   - Moved weapons to universal pool

3. **Complete Deck System** (v5.14)
   - Revealed all previous testing was incomplete
   - Bloodlines jumped from 11% → 73% WR
   - Dwarves crashed from 40% → 4% WR

---

## Next Steps (v5.15)

### Immediate Priorities

1. **Fix Dwarves (4% WR)** - Replace crafting faction cards with combat-viable alternatives
2. **Buff Church (13% WR)** - Reduce self-harm costs or add healing
3. **Buff Elves (29% WR)** - Increase Bleed damage or attack density
4. **Nerf Bloodlines (73% WR)** - Increase Biomass costs
5. **Nerf Crucible (80% WR)** - Reduce Forge token effects

### Long-Term Goals

- Achieve 7-8/10 factions balanced (45-55% WR)
- Implement all faction mechanics (crafting, graveyard, etc.)
- Add support units, tactics, and advanced mechanics
- Create UI/visualization for combat

---

## Contributing

### Adding New Cards

Cards are defined in `/workspaces/penance/docs/cards/complete-card-data.json`

#### Faction Card Example
```json
{
  "id": "blood-offering",
  "name": "Blood Offering",
  "type": "gambit",
  "cost": 0,
  "range": "Self",
  "effect": "Discard 1 card from deck. Next attack: +2 damage, ignore 1 Defense.",
  "keywords": ["gambit", "self-harm", "buff"],
  "cardCount": 1,
  "cardType": "faction"
}
```

#### Equipment Card Example
```json
{
  "name": "Strike",
  "type": "Attack",
  "cost": 2,
  "damage": 4,
  "effect": "Deal 4 damage.",
  "range": "Melee"
}
```

### Running Custom Tests

```python
from equipment_simulator_dice import *

# Custom casket class (Scout, Warden, Vanguard, Colossus)
casket = builder.build_random_deck("nomads", CasketClass.SCOUT)

# Custom verbose level
simulator = DiceCombatSimulator(casket1, casket2, verbose=True)
```

---

## Technical Notes

### Card Type Requirements

**CRITICAL:** Card types are case-sensitive!

✅ Correct:
```json
{"type": "Attack"}
{"type": "Reactive"}
{"type": "Utility"}
```

❌ Wrong (will be ignored):
```json
{"type": "attack"}
{"type": "reactive"}
```

### Heat Value Formats

Simulator handles multiple formats:
- Integer: `"heat": 1`
- String: `"heat": "+1"`
- Complex (ignored): `"heat": "-1d3"`

### Performance

- **Single combat:** <1 second
- **225 battles:** ~3 minutes
- **Memory usage:** <50MB

---

## Documentation

- `/workspaces/penance/docs/V5.14-COMPLETE-DECK-IMPLEMENTATION.md` - Complete v5.14 analysis
- `/workspaces/penance/docs/V5.9-RESULTS.md` - v5.9 balance pass
- `/workspaces/penance/docs/V5.10-RESULTS.md` - v5.10 economy fixes
- `/workspaces/penance/docs/V5.11-TECHNICAL-FIXES.md` - Type capitalization bug
- `/workspaces/penance/simulation/archived-rounds/` - Historical analysis

---

## License

Penance is a proprietary game system. This simulator is for development and balance testing purposes only.

---

**Maintained by:** Claude AI Assistant
**Last Updated:** October 20, 2025
**Simulator Version:** 5.14
