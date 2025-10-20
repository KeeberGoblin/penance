# New Equipment Balance Report
## Post-Implementation Testing Results

**Date:** October 20, 2025
**Test:** 225 battles (10 factions × 9 matchups × 5 runs per matchup)
**Database Version:** 5.1 (with 66 new physical equipment cards)

---

## Executive Summary

**Result:** Mixed - Equipment implementation successful, but reveals major balance issues

- **2/10 factions balanced** (Crucible 53.3%, Exchange 48.9%)
- **3 factions overpowered** (Church 95.6%, Dwarves 84.4%, Elves 71.1%)
- **5 factions underpowered** (Nomads 37.8%, Ossuarium 35.6%, Wyrd 28.9%, Bloodlines 26.7%, Emergent 17.8%)

---

## Balance Results

| Faction | Win Rate | Record | Status | Change from Pre-Equipment |
|---------|----------|--------|--------|---------------------------|
| **Church** | 95.6% | 43-2 | ❌ CATASTROPHIC | +11.2% (was 84.4%) |
| **Dwarves** | 84.4% | 38-7 | ❌ TOO STRONG | +15.5% (was 68.9%) |
| **Elves** | 71.1% | 32-13 | ⚠️ TOO STRONG | +20.0% (was 51.1%) |
| **Crucible** | 53.3% | 24-21 | ✅ BALANCED | -17.8% (was 71.1%) |
| **Exchange** | 48.9% | 22-23 | ✅ BALANCED | -15.5% (was 64.4%) |
| **Nomads** | 37.8% | 17-28 | ⚠️ TOO WEAK | +4.5% (was 33.3%) |
| **Ossuarium** | 35.6% | 16-29 | ⚠️ TOO WEAK | +2.3% (was 33.3%) |
| **Wyrd** | 28.9% | 13-32 | ⚠️ TOO WEAK | +13.3% (was 15.6%) |
| **Bloodlines** | 26.7% | 12-33 | ⚠️ TOO WEAK | -37.7% (was 64.4%!) |
| **Emergent** | 17.8% | 8-37 | ❌ CATASTROPHIC | +4.5% (was 13.3%) |

---

## Key Findings

### 1. **Church is Completely Broken (95.6% WR)**

**Evidence:**
- 43 wins, 2 losses (only lost to Dwarves and Elves)
- 100% win rate vs 7/9 opponents
- Average damage: 25.4 per game (highest in test)
- Equipment gives too much burst damage

**Root Cause:**
- Church equipment has highest average damage (4.6 per attack)
- Combined with Blood Offering faction mechanic (+3 damage)
- Results in 7-10 damage per attack combos
- No faction can survive sustained 7+ damage attacks

**Fix Needed:**
- Reduce Church equipment damage: 4.6 avg → 3.5 avg
- OR nerf Blood Offering: +3 damage → +2 damage
- OR add self-harm cost to equipment usage

---

### 2. **Elves Jumped from Balanced to Overpowered (+20% WR)**

**Evidence:**
- Was 51.1% WR (balanced) → Now 71.1% WR (too strong)
- Gained +20% win rate from equipment addition
- Bleed stacking + equipment damage = oppressive

**Analysis:**
- Elves equipment maintains damage while applying bleed
- Bleed stacks compound with equipment attacks
- Total damage per turn: 3 (equipment) + 4-8 (bleed) = 7-11 damage
- Opponents can't recover fast enough

**Fix Needed:**
- Reduce Elves equipment damage slightly
- OR reduce bleed cap from 6 → 4 stacks
- OR increase bleed SP cost

---

### 3. **Bloodlines Catastrophic Collapse (-37.7% WR)**

**Evidence:**
- Was 64.4% WR (too strong) → Now 26.7% WR (catastrophic)
- Dropped -37.7% win rate (largest swing in test)
- Equipment didn't provide enough support

**Analysis:**
- Bloodlines equipment relies on Biomass tokens
- Biomass generation is too slow (1 per kill/action)
- Equipment cards cost Biomass to activate bonuses
- Results in weak early game, can't build momentum

**Fix Needed:**
- Increase Biomass generation rate
- OR reduce Biomass costs on equipment
- OR buff base equipment damage (no Biomass required)

---

### 4. **Crucible & Exchange Are Balanced! ✅**

**Evidence:**
- Crucible: 53.3% WR (24-21 record)
- Exchange: 48.9% WR (22-23 record)
- Both in 45-55% target range

**What Worked:**
- Crucible equipment has Forge token synergy (matches faction)
- Exchange equipment has Credit generation/spending (matches faction)
- Balanced mix of offense and defense
- Equipment costs align with faction economy

**Lesson:** **Equipment must synergize with faction mechanics!**

---

### 5. **Combat Length Increased Significantly**

**Evidence:**
- Average combat length: 35.6 turns (was 21.7 turns pre-equipment)
- +64% increase in game length
- Matches now take 15-42 turns

**Analysis:**
- Equipment added defensive options (shields, reactive cards)
- Players can block/reduce more damage
- Results in longer attrition battles
- May be desired (tactical depth) or problematic (slow gameplay)

**Consideration:**
- Is 35-turn average acceptable?
- Target was 15-30 turns optimal
- May need to increase damage output across the board

---

## Equipment Quality Analysis

### **High-Quality Equipment** (Well-Designed)

#### **Crucible Equipment** ✅
- **Forge Blessing** (2 SP): Reduce damage by 2, gain 1 Forge token
- **Ember Strike** (2 SP): 3 damage, +1 in lava terrain
- **Volcanic Cleave** (3 SP): 4 damage, spend 1 Forge for 5 damage + burn

**Why It Works:**
- Synergizes with Forge token economy
- Provides meaningful choices (spend tokens now or save?)
- Balanced costs and effects

#### **Exchange Equipment** ✅
- **Contract Blade** (2 SP): 3 damage, gain 1 Credit
- **Mercenary Strike** (3 SP): 4 damage, spend 1 Credit for 5 damage
- **Expense Report** (0 SP, reactive): Reduce damage by 2, gain 1 Credit

**Why It Works:**
- Synergizes with Credit economy
- Defensive options also generate Credits
- Creates strategic tension (attack or defend?)

---

### **Problematic Equipment** (Needs Rebalancing)

#### **Church Equipment** ❌
- **Average damage: 4.6** (highest in game)
- **Multiple 4-5 damage attacks** at 2-3 SP cost
- **No self-harm cost** on equipment (unlike faction cards)

**Problems:**
- Too much burst damage
- Combined with Blood Offering (+3 damage) = 7-8 damage attacks
- No trade-off for high damage

**Fix:**
- Reduce damage: 4-5 → 3-4
- OR add self-harm: "Deal 4 damage, discard 1 card"
- OR increase SP costs: 2-3 SP → 3-4 SP

#### **Bloodlines Equipment** ❌
- **Relies heavily on Biomass tokens**
- **Biomass generation too slow** (1 per kill)
- **Equipment bonuses require spending Biomass**

**Problems:**
- Weak early game (no Biomass yet)
- Can't activate equipment bonuses
- Opponents kill you before you build up

**Fix:**
- Increase base damage (before Biomass bonus)
- OR make some equipment generate Biomass
- OR reduce Biomass costs (2 → 1)

#### **Emergent Equipment** ❌
- **Relies on Metamorph form**
- **Requires allied units for bonuses**
- **Equipment weak without synergies**

**Problems:**
- Metamorph form costs SP to activate
- Allied units not present in 1v1 combat (simulator limitation)
- Equipment does nothing without prerequisites

**Fix:**
- Add base effects (work without Metamorph)
- OR buff base damage values
- OR reduce Metamorph activation cost

---

## Recommendations

### **Immediate Fixes (Priority 1)**

1. **Nerf Church Equipment Damage**
   - Reduce average damage: 4.6 → 3.5
   - Target: Church 95.6% → 55-60% WR

2. **Buff Bloodlines Biomass Generation**
   - Increase generation: 1 per kill → 2 per kill
   - OR reduce equipment costs: 2 Biomass → 1 Biomass
   - Target: Bloodlines 26.7% → 45-50% WR

3. **Buff Emergent Base Damage**
   - Increase damage on cards without Metamorph requirement
   - Target: Emergent 17.8% → 40-45% WR

### **Secondary Fixes (Priority 2)**

4. **Nerf Elves Bleed Stacking**
   - Reduce bleed cap: 6 → 4 stacks
   - OR reduce bleed damage: 2 per stack → 1 per stack
   - Target: Elves 71.1% → 50-55% WR

5. **Buff Ossuarium Lifesteal**
   - Reduce Soul Harvest cost: 3 SP → 2 SP
   - OR increase recovery: 4 cards → 5 cards
   - Target: Ossuarium 35.6% → 45-50% WR

6. **Buff Wyrd Equipment**
   - Increase base damage: 3.0 avg → 3.5 avg
   - OR reduce Taint costs
   - Target: Wyrd 28.9% → 45-50% WR

### **Testing Protocol**

After each fix:
1. Change **ONE faction only**
2. Run 20 battles per matchup (200 total)
3. Check for catastrophic swings (>60% or <40%)
4. Iterate incrementally

---

## Success Metrics

**Current State:**
- ✅ Equipment cards successfully added (66 new cards)
- ✅ All factions have 11-13 equipment cards
- ✅ 2 factions balanced (Crucible, Exchange)
- ❌ 8 factions unbalanced
- ❌ Church catastrophically overpowered

**Target State:**
- 7-10 factions in 45-55% WR range
- No faction >60% or <40% WR
- Average combat length: 20-30 turns
- No 100% or 0% matchups

---

## Lessons Learned

1. **Equipment MUST synergize with faction mechanics**
   - Crucible/Exchange work because equipment matches their economy
   - Bloodlines/Emergent fail because equipment doesn't support their playstyle

2. **Defensive equipment lengthens games**
   - Reactive cards increased combat length by 64%
   - May need to increase offensive power across the board

3. **High-damage factions dominate**
   - Church (4.6 avg damage) has 95.6% WR
   - Lower damage factions struggle

4. **Token economies need careful balance**
   - Crucible Forge tokens work (generates AND spends naturally)
   - Bloodlines Biomass fails (generates too slowly, spends too fast)

---

## Next Steps

1. **Apply Priority 1 fixes** (Church nerf, Bloodlines buff, Emergent buff)
2. **Re-run simulation** (200+ battles)
3. **Check for ripple effects** (did Church nerf help bottom factions?)
4. **Iterate on Priority 2 fixes**
5. **Repeat until 7+ factions balanced**

---

**Report Version:** 1.0
**Test Date:** October 20, 2025
**Database Version:** 5.1
**Total Battles:** 225
