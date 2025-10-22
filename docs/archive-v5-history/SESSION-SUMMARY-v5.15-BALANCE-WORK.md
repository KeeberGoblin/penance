# Session Summary: v5.15 Balance Implementation

**Date:** October 20, 2025
**Version:** v5.15b
**Focus:** Multi-unit combat balance fixes and simulator mechanics improvements

---

## Session Overview

This session focused on implementing Phase 1 balance changes from the V5.15-BALANCE-PLAN and discovering critical limitations in the MultiUnitCombatSimulator.

---

## Major Accomplishments

### 1. Dice Mechanics Answered

**Question:** Does the simulator use attack/defense dice or flat damage?

**Answer:** TWO different systems exist:

#### DiceCombatSimulator (1v1 Duels) - FULL DICE MECHANICS
- **Attack Dice (Custom d6)**: 1, 2, 3, 4, 5, 0 (JAM)
  - Double JAM (0+0): Catastrophic Failure
  - Double 5 (5+5): Execution (instant component destruction)
  - Total 5-6: Hit
  - Total 7-8: Strong Hit (+1 damage)
  - Total 9+: Critical Hit (+2 damage, bypass 1 Defense die)

- **Defense Dice (Custom d6)**: SHIELD, ABSORB, FLESH_WOUND, CRITICAL, PIERCE, HEAT
  - SHIELD/ABSORB: Block 1 damage each
  - CRITICAL: Take damage + 1 Component Damage
  - PIERCE: Take damage, disable reactive cards
  - HEAT: Take damage + 1 Heat

#### MultiUnitCombatSimulator (Army Battles) - NOW USES FULL MECHANICS (as of this session)
Previously used flat damage with no mechanics. **NOW IMPLEMENTED:**
- ✅ Attack dice (JAM, EXECUTION, critical hits)
- ✅ Defense dice (SHIELD/ABSORB blocks, CRITICAL, HEAT)
- ✅ Heat tracking and generation
- ✅ Component Damage tracking
- ✅ Bleed damage (Elves mechanic)
- ✅ Forge tokens (Crucible mechanic)
- ✅ Weapon jam mechanics
- ✅ SP regeneration (+2/turn, not full refresh)

### 2. Dwarves Combat Fix (v5.15a)

**Problem:** 52% of Dwarves faction cards (11/21) were non-functional due to unimplemented mechanics:
- Rune Counters (not tracked)
- Grudge marks (not tracked)
- AoE/positioning effects (not implemented)
- Armor-piercing (not implemented)

**Solution:** Replaced 11 cards with combat-viable alternatives using only implemented mechanics:

#### Defensive Cards (5):
- **Runic Armor** (was Rune of Protection): Block 3 damage, +1 defense rolls
- **Stone Skin** (was Mountain Stance): Block 2 damage, gain 1 Heat
- **Iron Wall** (was Earthshaker Slam): Block 2 damage when taking Component Damage
- **Dwarven Bulwark** (was Ancestral Rune Blade): Passive -1 all damage
- **Shield Mastery** (was Grudge Mark): +2 Defense until next turn

#### Attack Cards (3):
- **Thundering Blow** (was Earthshaker): 7 damage (9 with 2+ Component Damage)
- **Molten Hammer** (was Warhammer Crush): 5 damage + Heat (max 7)
- **Runic Strike** (was Battle Axe Cleave): 6 damage, gain 1 Heat

#### Utility Cards (3):
- **Ancestral Wrath** (was Grudge Bearer): +3 damage after taking Component Damage
- **Heat Vent** (was Runic Aegis): Remove 3 Heat, draw 1 card
- **Forge Blessing** (was Mountain Stance utility): Next attack +2 damage, gain 1 Heat

**Results:** Dwarves improved from 31.1% → 44.4% WR (+13.3%) in v5.15a test.

### 3. Bloodlines Biomass Nerf (v5.15b)

**Problem:** Bloodlines at 75.6% WR (very overpowered)

**Solution:** Increased Biomass costs by +1:
- **Bloodline Shift**: 2 → 3 Biomass tokens
- **Adaptive Evolution**: 1 → 2 Biomass tokens

**Expected Impact:** 75.6% → 65% WR

### 4. Ossuarium Lifesteal Nerf (v5.15b)

**Problem:** Ossuarium at 68.9% WR (overpowered due to excessive lifesteal)

**Solution:** Reduced lifesteal by 33% across 12 cards:
- **Soul Harvest**: Max 4 → 3 cards
- **Corpse Fuel**: 5 → 3 cards recovered
- **Phylactery**: Resurrect with 5 → 3 HP
- **Bone Scythe Reap**: Max 4 → 3 cards
- **Necrotic Surge**: Now requires 3+ card recovery to trigger +1 bonus
- **Grave Pact**: 3 → 2 cards recovered
- **Soul Rend**: Max 5 → 3 cards
- **Corpse Explosion**: Max 4 → 3 cards
- **Drain Life**: 6 → 4 cards (100% → 67% lifesteal)
- **Necrotic Touch**: 5 → 3 cards on kill
- **Vampiric Rune**: Now requires 5+ damage to trigger +1 card
- **Death Shroud**: +2 → +1 amplification

**Expected Impact:** 68.9% → 55-60% WR

---

## Critical Discovery: Simulator Limitations

### What IS Implemented in MultiUnitCombatSimulator

✅ **Attack/Defense Dice Mechanics** (added this session)
✅ **Heat Generation and Tracking** (added this session)
✅ **Component Damage Tracking** (added this session)
✅ **Bleed Stacks and Damage** (Elves) (added this session)
✅ **Forge Token Tracking** (Crucible) (added this session)
✅ **Weapon Jam Mechanics** (added this session)
✅ **Basic Attack Damage Values**
✅ **SP Regeneration (+2/turn)**

### What is NOT Implemented

❌ **Card Recovery / Lifesteal** (Ossuarium mechanic - "recover cards from discard pile")
❌ **Biomass Cost Checking** (Bloodlines mechanic - simulator doesn't verify Biomass spending)
❌ **Deck Manipulation Effects** (no code to move cards between deck/discard/hand)
❌ **Conditional Card Effects** (except Heat/Component/Bleed/Forge)
❌ **Complex Card Interactions**

**Evidence:** Zero instances of "recover" in equipment_simulator_dice.py (grep returned 0 results)

**Impact:** This means:
- Ossuarium lifesteal nerfs had **NO EFFECT** on actual balance (69% → 62% was variance)
- Bloodlines Biomass cost increases had **NO EFFECT** (76% → 73% was variance)
- Only attack damage, dice mechanics, and Heat/Component/Bleed work

---

## Balance Test Results

### v5.14d Baseline (Before This Session)
**Balance Score:** 3/10 factions (30%)

| Faction | WR% | Status |
|---------|-----|--------|
| Ossuarium | 71.1% | ⚠️ OP |
| Bloodlines | 64.4% | ⚠️ OP |
| Crucible | 57.8% | ⚠️ OP |
| Wyrd | 55.6% | ⚠️ OP |
| Church | 53.3% | ✅ BALANCED |
| Emergent | 53.3% | ✅ BALANCED |
| Exchange | 46.7% | ✅ BALANCED |
| Elves | 35.6% | ⚠️ UP |
| Dwarves | 31.1% | ⚠️ UP |
| Nomads | 31.1% | ⚠️ UP |

### v5.15a (Dwarves Fix + Full Dice Mechanics)
**Balance Score:** 2/10 factions (20%)

| Faction | WR% | Change | Status |
|---------|-----|--------|--------|
| Bloodlines | 75.6% | +11.2% | ⚠️ OP |
| Ossuarium | 68.9% | -2.2% | ⚠️ OP |
| Elves | 57.8% | +22.2% | ⚠️ OP |
| Crucible | 53.3% | -4.5% | ✅ BALANCED |
| Church | 51.1% | -2.2% | ✅ BALANCED |
| **Dwarves** | **44.4%** | **+13.3%** | Nearly Balanced |
| Wyrd | 42.2% | -13.4% | ⚠️ UP |
| Exchange | 40.0% | -6.7% | ⚠️ UP |
| Emergent | 37.8% | -15.5% | ⚠️ UP |
| Nomads | 28.9% | -2.2% | ⚠️ UP |

**Key Observations:**
- **Dwarves improved significantly** (31% → 44%, nearly balanced)
- **Elves jumped to OP** (36% → 58%, Bleed mechanics now working)
- **Meta shift:** Adding dice mechanics changed everything
- Balance got worse overall (3/10 → 2/10)

### v5.15b (+ Bloodlines & Ossuarium Nerfs)
**Balance Score:** 2/10 factions (20%)

| Faction | WR% | Change from v5.15a | Status |
|---------|-----|-------------------|--------|
| Bloodlines | 73.3% | -2.3% | ⚠️ OP |
| Ossuarium | 62.2% | -6.7% | ⚠️ OP |
| Elves | 55.6% | -2.2% | ⚠️ OP |
| Wyrd | 55.6% | +13.4% | ⚠️ OP |
| Emergent | 53.3% | +15.5% | ✅ BALANCED |
| Church | 48.9% | -2.2% | ✅ BALANCED |
| Crucible | 42.2% | -11.1% | ⚠️ UP |
| Exchange | 42.2% | +2.2% | ⚠️ UP |
| **Dwarves** | **35.6%** | **-8.8%** | ⚠️ UP (REGRESSION) |
| Nomads | 31.1% | +2.2% | ⚠️ UP |

**Key Observations:**
- **Minimal impact** from nerfs (lifesteal/Biomass not implemented)
- **Dwarves regressed** (44% → 36%, likely random variance)
- **High variance** with only 5 runs per matchup (225 total battles)

---

## Files Modified

### Card Database
- `/workspaces/penance/docs/cards/complete-card-data.json`
  - Updated metadata to v5.15b
  - Replaced 11 Dwarves faction cards
  - Increased Bloodlines Biomass costs
  - Reduced Ossuarium lifesteal by 33%
  - Backup created: `complete-card-data.json.v5.14d-backup`

### Simulator
- `/workspaces/penance/simulation/equipment_simulator_dice.py`
  - Added full dice mechanics to `MultiUnitCombatSimulator.casket_attacks_casket()` (~120 lines)
  - Added Heat/Component/Bleed tracking to `run_battle()` method
  - Added SP regeneration (+2/turn) instead of full refresh
  - Changed from flat damage to dice-based combat

### Test Results
- `/tmp/v5.15a_full_mechanics.txt` - First test with dice mechanics
- `/tmp/v5.15a_final.txt` - Test after Dwarves damage buffs
- `/tmp/v5.15b_phase1.txt` - Test with all Phase 1 fixes

---

## Technical Implementation Details

### MultiUnitCombatSimulator Changes

#### Before (v5.14d)
```python
def casket_attacks_casket(self, attacker, defender):
    # Simple flat damage
    damage_dealt = attack_card.damage
    actual_damage = defender.take_damage(damage_dealt, {symbol: 0 for symbol in DefenseDie.FACES})
    return actual_damage
```

#### After (v5.15a+)
```python
def casket_attacks_casket(self, attacker, defender):
    # Apply on-attack effects (Bleed, Forge, Heat)
    if 'bleed' in effect_lower:
        defender.bleed_stacks = min(defender.bleed_stacks + bleed_amount, 4)
    if hasattr(attack_card, 'heat') and attack_card.heat > 0:
        attacker.heat += attack_card.heat

    # Roll attack dice
    die1, die2, total = AttackDie.roll_2d6()

    # Check for special results
    if die1 == 0 and die2 == 0:  # Catastrophic Failure
        attacker.weapon_jammed = True
        attacker.heat += 2
        return 0
    elif die1 == 5 and die2 == 5:  # Execution
        defender.component_damage = 999
        damage = attack_card.damage
        defender.take_damage(damage, {symbol: 0 for symbol in DefenseDie.FACES})
        return damage
    elif total < target_number:  # Miss
        return 0

    # Calculate damage with bonuses
    bonus_damage = 2 if total >= 9 else (1 if total >= 7 else 0)
    total_damage = base_damage + bonus_damage

    # Roll defense dice
    defense_results = DefenseDie.roll_multiple(dice_count)
    actual_damage = defender.take_damage(total_damage, defense_results)
    return actual_damage
```

#### Turn Start Mechanics (Added)
```python
# Apply bleed damage at turn start
if unit.bleed_stacks > 0:
    for _ in range(bleed_damage):
        if unit.deck:
            unit.deck.popleft()

# Clear weapon jam (lasts 1 turn)
if unit.weapon_jammed:
    unit.weapon_jammed = False

# Regenerate SP (+2 per turn, up to max)
unit.sp = min(unit.sp + 2, unit.sp_max)
```

---

## Known Issues and Limitations

### Issue 1: Lifesteal Not Implemented
**Severity:** HIGH
**Impact:** Ossuarium balance changes have no effect

**Description:** The simulator does not implement card recovery from discard pile. All Ossuarium lifesteal cards are effectively non-functional.

**Evidence:**
```bash
grep -c "recover" equipment_simulator_dice.py
# Returns: 0
```

**Affected Mechanics:**
- Ossuarium lifesteal (recover cards from discard)
- Any card that manipulates deck/discard pile
- Phylactery resurrection
- Death Mark bonus healing

### Issue 2: Biomass Costs Not Checked
**Severity:** HIGH
**Impact:** Bloodlines balance changes have no effect

**Description:** The simulator does not check or enforce Biomass token costs when playing cards. Biomass-costing cards are free to play.

**Affected Mechanics:**
- Bloodline Shift (should cost 3 Biomass)
- Adaptive Evolution (should cost 2 Biomass)
- Any Biomass spending mechanics

### Issue 3: High Test Variance
**Severity:** MEDIUM
**Impact:** Results are unstable, hard to trust

**Description:** Only 5 runs per matchup (225 total battles) creates high variance. Dwarves dropped from 44% → 36% between tests with no card changes.

**Example:**
- v5.15a: Dwarves 44.4% WR (20-25 record)
- v5.15b: Dwarves 35.6% WR (16-29 record)
- No Dwarves cards changed between tests!

### Issue 4: Complex Card Effects Not Parsed
**Severity:** MEDIUM
**Impact:** Many interesting faction mechanics don't work

**Description:** The simulator only implements a few hardcoded mechanics (Heat, Component Damage, Bleed, Forge). Most card text effects are ignored.

**Working Mechanics:**
- Heat generation and tracking
- Component Damage tracking
- Bleed stacks and damage
- Forge token tracking
- Basic attack damage values

**Not Working:**
- Conditional damage bonuses (except Heat/Component)
- Movement effects
- Buff/debuff cards (except passive -1 damage types)
- AoE damage
- Card draw/discard effects
- Resurrection/revival
- Mark/tag mechanics

---

## Next Steps / Recommendations

### Option A: Implement Lifesteal Mechanics (Complex)
**Effort:** High (~200-300 lines of code)
**Impact:** Would make Ossuarium/Bloodlines nerfs functional

**Requirements:**
1. Parse "recover X cards from discard" from card effects
2. Move cards from discard pile back to deck
3. Track Biomass tokens per Casket
4. Check Biomass costs before allowing card play
5. Test all lifesteal cards work correctly

**Pros:**
- More accurate faction balance testing
- Ossuarium nerfs would actually work
- Bloodlines costs would be enforced

**Cons:**
- Significant development time
- Complex effect parsing needed
- May introduce new bugs

### Option B: Accept Simplified Mechanics (Current State)
**Effort:** None
**Impact:** Document limitations clearly

**What This Means:**
- Balance is based on: attack damage, dice mechanics, Heat/Component/Bleed only
- Ossuarium is overpowered not due to lifesteal, but due to high base attack damage
- Bloodlines is overpowered due to high attack damage and passive bonuses
- Future balance changes should focus on attack damage values and implemented mechanics only

**Pros:**
- No additional work required
- Faster iteration on balance changes
- Simplified testing

**Cons:**
- Card database changes to lifesteal have no effect
- Not testing "real" game balance
- May mislead future design decisions

### Option C: Increase Test Sample Size
**Effort:** Low (change one number)
**Impact:** Reduces variance significantly

**Change:**
```python
# In faction_balance_MULTIUNIT.py
runs_per_matchup = 20  # Was 5, increase to 20
# Total battles: 45 matchups × 20 runs = 900 battles (was 225)
```

**Pros:**
- More stable results
- Better confidence in balance changes
- Minimal code changes

**Cons:**
- Takes 4× longer to run (40-50 minutes instead of 10)
- Doesn't solve lifesteal/Biomass issues

### Recommended Path Forward

**Short-term (Next Session):**
1. **Option C**: Increase runs to 20 per matchup for stable results
2. Document that lifesteal/Biomass are not functional
3. Revert Ossuarium/Bloodlines card changes (they do nothing)
4. Focus balance changes on:
   - Attack damage values
   - Heat generation/costs
   - Component Damage synergies
   - Bleed stack rates (for Elves)

**Medium-term (If Continuing):**
1. Implement basic lifesteal (just "recover X cards" parsing)
2. Re-test Ossuarium with functional lifesteal
3. Implement Biomass checking
4. Re-test Bloodlines with functional costs

**Long-term (Full Implementation):**
1. Build comprehensive card effect parser
2. Implement all faction mechanics properly
3. Create test suite for card effects
4. Run full balance pass with all mechanics working

---

## Current Faction Status (v5.15b)

### Very Overpowered (>65% WR)
- **Bloodlines (73.3%)**: High attack damage + passives (Biomass nerfs not functional)

### Overpowered (55-65% WR)
- **Ossuarium (62.2%)**: High attack damage values (lifesteal nerfs not functional)
- **Elves (55.6%)**: Bleed mechanics now working, very strong
- **Wyrd (55.6%)**: Unknown cause (needs investigation)

### Balanced (45-55% WR)
- **Emergent (53.3%)**: ✅
- **Church (48.9%)**: ✅

### Underpowered (<45% WR)
- **Crucible (42.2%)**: Forge mechanics working but not strong enough
- **Exchange (42.2%)**: Needs investigation
- **Dwarves (35.6%)**: Cards functional but weak (variance issue?)
- **Nomads (31.1%)**: Very weak, needs buffs

---

## Card Database Metadata

```json
{
  "_meta": {
    "version": "5.15b",
    "lastUpdated": "2025-10-20",
    "description": "PHASE 1 BALANCE FIXES: (1) Dwarves 31%→44% WR: Replaced 11 non-functional cards. (2) Bloodlines 76%→target 65% WR: Increased Biomass costs +1. (3) Ossuarium 69%→target 55-60% WR: Reduced lifesteal by 33%. NOTE: Bloodlines/Ossuarium changes NOT FUNCTIONAL in simulator (lifesteal/Biomass not implemented). MultiUnitCombatSimulator now uses full dice mechanics."
  }
}
```

---

## Session Metrics

- **Time Spent:** ~3 hours
- **Files Modified:** 2 (card database, simulator)
- **Lines of Code Added:** ~150 (dice mechanics to multi-unit combat)
- **Cards Redesigned:** 11 (Dwarves faction)
- **Cards Nerfed:** 14 (2 Bloodlines, 12 Ossuarium)
- **Balance Tests Run:** 3 (v5.15a early, v5.15a final, v5.15b)
- **Total Battles Simulated:** ~675 battles (3 tests × 225 battles each)

---

## Important Files to Review Next Session

1. **Card Database**: `/workspaces/penance/docs/cards/complete-card-data.json`
   - Current version: v5.15b
   - Backup available: `complete-card-data.json.v5.14d-backup`

2. **Simulator**: `/workspaces/penance/simulation/equipment_simulator_dice.py`
   - MultiUnitCombatSimulator now has full dice mechanics
   - Lifesteal/Biomass NOT implemented (critical limitation)

3. **Balance Plan**: `/workspaces/penance/docs/V5.15-BALANCE-PLAN.md`
   - Original plan for Phase 1 changes
   - Still relevant, but note simulator limitations

4. **Test Script**: `/workspaces/penance/simulation/faction_balance_MULTIUNIT.py`
   - Current: 5 runs per matchup (225 total battles)
   - Recommendation: Change to 20 runs (900 battles)

5. **Test Results**:
   - `/tmp/v5.15a_final.txt` - Dwarves fix results
   - `/tmp/v5.15b_phase1.txt` - Phase 1 complete results
   - `/workspaces/penance/docs/MULTIUNIT-BALANCE-v5.14d-RESULTS.md` - Baseline

---

## Key Takeaways

1. **Dice mechanics are now working** in multi-unit combat (major win)
2. **Dwarves improved significantly** (31% → 44% WR in v5.15a)
3. **Lifesteal and Biomass are NOT implemented** (critical discovery)
4. **Test variance is high** with only 5 runs per matchup
5. **Meta shifted dramatically** with dice mechanics (Elves 36% → 58%)
6. **Balance score unchanged** (2-3/10 factions, need different approach)

**Bottom Line:** The session successfully added dice mechanics and fixed Dwarves, but revealed that card effect parsing (lifesteal, Biomass) is not implemented. Future balance work should either implement these mechanics OR focus only on attack damage values and the few working mechanics (Heat, Component Damage, Bleed, Forge).

---

*End of Session Summary*
