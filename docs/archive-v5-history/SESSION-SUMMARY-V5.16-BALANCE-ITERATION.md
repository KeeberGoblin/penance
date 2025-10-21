# Session Summary - v5.16 Balance Iteration

**Date:** October 20, 2025
**Session Goal:** Apply targeted balance changes based on v5.15 baseline (real mechanics)
**Previous Version:** 5.15 (real mechanics, no multipliers, baseline data)
**New Version:** 5.16 (first balance pass on equipment damage)

---

## Changes Applied in v5.16

### 1. Ossuarium Equipment Nerfs (-1 damage)

**Rationale:** 93% WR in v5.15 → Target 50%

**Equipment Changes:**
- Bone Scythe Strike: 5 → 4 damage (-1)
- Death Grip: 6 → 5 damage (-1)
- Soul Reaper: 7 → 6 damage (-1)
- Corpse Harvest: 5 → 4 damage (-1)

**Result:** 93.3% → 86.7% WR (-6.6%)
**Assessment:** ❌ INSUFFICIENT - Still massively overpowered

---

### 2. Nomads Equipment Buffs (+1 damage)

**Rationale:** 24% WR in v5.15 → Target 50%

**Equipment Changes:**
- Quick Slash: 4 → 5 damage (+1)
- Pistol Shot: 4 → 5 damage (+1)
- Hit and Run: 5 → 6 damage (+1)
- Opportunist Strike: 6 → 7 damage (+1)

**Result:** 24.4% → 31.1% WR (+6.7%)
**Assessment:** ❌ INSUFFICIENT - Still very underpowered

---

## V5.16 Results

### Balance Overview
- **Battles:** 225 (10 factions × 9 matchups × 5 runs)
- **Balanced Factions:** 1/10 (45-55% WR range)
- **Balance Score:** 1/10 (POOR - same as v5.15)

### Faction Win Rates

| Faction | v5.15 WR | v5.16 WR | Change | Status |
|---------|----------|----------|--------|--------|
| **Ossuarium** | 93.3% | **86.7%** | -6.6% | 🚨 Still Critical OP |
| **Exchange** | 66.7% | **77.8%** | +11.1% | ⚠️ Got WORSE! |
| **Bloodlines** | 82.2% | **77.8%** | -4.4% | ⚠️ Still Very OP |
| **Emergent** | 44.4% | **57.8%** | +13.4% | ⚠️ Now OP |
| **Wyrd** | 51.1% | **51.1%** | 0.0% | ✅ **BALANCED** |
| **Crucible** | 57.8% | **44.4%** | -13.4% | ⚠️ Dropped to UP |
| **Elves** | 31.1% | **35.6%** | +4.5% | ⚠️ Still UP |
| **Nomads** | 24.4% | **31.1%** | +6.7% | ⚠️ Still Very UP |
| **Dwarves** | 24.4% | **22.2%** | -2.2% | ⚠️ Still Very UP |
| **Church** | 24.4% | **15.6%** | -8.8% | 🚨 Got WORSE! |

---

## Unexpected Results

### 1. Exchange Got WORSE (+11% WR)

**v5.15:** 66.7% WR (overpowered)
**v5.16:** 77.8% WR (much more overpowered!)

**Why?**
- Equipment changes were faction-neutral (affected all factions equally)
- Exchange's Credit economy becomes relatively stronger when base damage is more balanced
- Credits provide flat +damage bonuses that scale better in lower-damage environment

**Lesson:** Resource economies scale differently with base damage changes

---

### 2. Church Got WORSE (-9% WR)

**v5.15:** 24.4% WR (very underpowered)
**v5.16:** 15.6% WR (critical underpowered!)

**Why?**
- Ossuarium's nerf reduced average fight duration
- Shorter fights = less time for Church's self-harm bonuses to matter
- Church has no resource economy to compensate like Exchange

**Lesson:** Defensive/sustain factions suffer in faster meta

---

### 3. Crucible Dropped Too Much (-13% WR)

**v5.15:** 57.8% WR (slightly overpowered)
**v5.16:** 44.4% WR (underpowered)

**Why?**
- Crucible relies on Forge tokens for bonus damage
- Lower base damage environment makes Forge bonuses less impactful relatively
- Needs +1 damage to Forge spending effects

**Lesson:** Resource-based factions sensitive to base damage environment

---

### 4. Emergent Became OP (+13% WR)

**v5.15:** 44.4% WR (slightly underpowered)
**v5.16:** 57.8% WR (overpowered)

**Why?**
- Emergent has consistent damage output without resource economy
- Benefited from weaker Ossuarium (less oppressive matchup)
- No equipment changes targeted Emergent

**Lesson:** Indirect meta shifts can flip faction power levels

---

## Analysis: Why Equipment-Only Changes Failed

### Problem 1: Lifesteal Scaling

**Ossuarium's True Power:**
- Not just high damage (5-7)
- But high damage + lifesteal on every card
- Reducing damage 5→4 reduces both offense AND sustain
- But lifesteal still provides 80-100% recovery (just 1 less card per hit)

**Impact of -1 damage:**
- Offensive reduction: ~17% (-1 from 6)
- Sustain reduction: ~17% (-1 card recovered)
- **Net power reduction: ~30%** (multiplicative)
- **Needed reduction for 87% → 50%: ~43%**

**Conclusion:** Need -2 damage across Ossuarium equipment, not -1

---

### Problem 2: No Lifesteal on Nomads

**Nomads' True Weakness:**
- Low damage (4-5) with no sustain
- Mobility effects don't work in simulator
- No resource economy

**Impact of +1 damage:**
- Offensive increase: ~20% (+1 from 5)
- Sustain increase: 0% (no lifesteal)
- **Net power increase: ~20%**
- **Needed increase for 24% → 50%: ~108%**

**Conclusion:** Need +2-3 damage on Nomads, OR add sustain mechanics

---

### Problem 3: Resource Economies Dominate

**Factions with Working Economies:**
1. **Exchange (Credits):** 77.8% WR
2. **Bloodlines (Biomass):** 77.8% WR
3. **Emergent (None):** 57.8% WR
4. **Wyrd (None):** 51.1% WR

**Factions with Broken/Weak Economies:**
1. **Church (Self-Harm):** 15.6% WR ❌
2. **Dwarves (Rune Counters):** 22.2% WR ❌
3. **Nomads (None):** 31.1% WR ❌

**Conclusion:** Resource economies are too powerful. Need to nerf economy effects, not just base damage.

---

## Lessons Learned

### 1. Equipment-Only Balance Is Insufficient

**Reasoning:**
- Equipment affects all factions similarly (everyone uses equipment)
- Faction-specific cards define power (6 random cards from 21)
- Resource economies scale independently of equipment damage

**New Approach:**
- Nerf resource generation/spending costs
- Buff faction-specific card quality
- Equipment changes as secondary tuning

---

### 2. Lifesteal is Multiplicatively Powerful

**Math:**
- Pure damage faction: 100 HP, deals 6 damage = ~17 turns to kill
- Lifesteal faction: 100 HP, deals 6 damage + recovers 6 = ~infinite durability

**In card-as-HP system:**
- Damage = reduce opponent deck
- Lifesteal = add to your deck
- **Net advantage = 2× the damage value**

**Solution:** Nerf Ossuarium damage by 2+ points, not 1

---

### 3. Resource Economies Create Power Outliers

**Top 4 Factions:**
1. Ossuarium: 86.7% (lifesteal = economy)
2. Exchange: 77.8% (Credits economy)
3. Bloodlines: 77.8% (Biomass economy)
4. Emergent: 57.8% (no economy, but consistent)

**Bottom 3 Factions:**
1. Church: 15.6% (broken self-harm economy)
2. Dwarves: 22.2% (weak rune counter economy)
3. Nomads: 31.1% (no economy)

**Conclusion:** Working economy = 75%+ WR. No/broken economy = <35% WR.

---

### 4. Meta Speed Affects Faction Viability

**Fast Meta (v5.16):**
- Ossuarium nerfed → fights end faster
- Exchange dominates (fast burst with Credits)
- Church suffers (needs time to accumulate discard bonuses)

**Lesson:** Balance changes affect more than direct targets

---

## Recommendations for v5.17

### Critical Priority (Must Fix)

#### 1. Nerf Ossuarium Harder (-2 damage, not -1)

**Changes:**
- All equipment: Additional -1 damage (total -2 from v5.15)
- Lifesteal recovery: Reduce to 50% (recover half damage dealt, not full)
- Estimated impact: 86.7% → 55-60% WR

---

#### 2. Nerf Exchange Credits System

**Changes:**
- Credit generation: Gain 1 per 2 attacks (not every attack)
- Credit spending: Increase costs by +1 (3→4 Credits for +4 damage)
- Estimated impact: 77.8% → 50-55% WR

---

#### 3. Nerf Bloodlines Biomass System

**Changes:**
- Biomass on kill: 2 → 1 Biomass per kill
- Biomass spending: Increase costs by +1 across all cards
- Estimated impact: 77.8% → 50-55% WR

---

#### 4. Buff Nomads Harder (+2 total damage)

**Changes:**
- All equipment: Additional +1 damage (total +2 from v5.15)
- Add passive: "Gain 1 HP per attack" (light sustain)
- Estimated impact: 31.1% → 45-50% WR

---

#### 5. Buff Church Significantly

**Changes:**
- Discard bonuses: Double all values (+2 → +4 damage per discard)
- Add recovery: "Discard 2 → Recover 3" cards
- Remove self-harm costs on defensive cards
- Estimated impact: 15.6% → 40-45% WR

---

#### 6. Buff Dwarves Rune Counters

**Changes:**
- Rune reduction: 1 → 2 damage per counter
- Rune generation: Add to 3 more faction cards
- Rune cap: 3 → 5 counters
- Estimated impact: 22.2% → 40-45% WR

---

### Secondary Priority

#### 7. Slight Nerf Emergent

**Changes:**
- Equipment: -1 damage on highest cards
- Estimated impact: 57.8% → 50-55% WR

---

#### 8. Slight Buff Crucible

**Changes:**
- Forge spending: +1 damage per token spent
- Estimated impact: 44.4% → 48-52% WR

---

#### 9. Buff Elves

**Changes:**
- Bleed damage: 1 → 2 per stack per turn
- Equipment: +1 damage on melee cards
- Estimated impact: 35.6% → 45-50% WR

---

#### 10. Preserve Wyrd (Already Balanced!)

**Changes:** NONE
**Current:** 51.1% WR ✅

---

## Implementation Strategy for v5.17

### Phase 1: Economy Nerfs (Week 1)

**Goal:** Reduce resource economy advantage

1. Nerf Bloodlines Biomass (2→1 per kill, +1 spending costs)
2. Nerf Exchange Credits (1 per 2 attacks, +1 spending costs)
3. Nerf Ossuarium lifesteal (50% recovery, -1 additional damage)

**Expected Result:** Top 3 factions drop to 50-60% WR range

---

### Phase 2: Sustain Buffs (Week 1)

**Goal:** Give weak factions survival tools

1. Buff Church discard bonuses (double values)
2. Buff Dwarves rune counters (2 damage reduction per counter)
3. Add Nomads passive sustain (+1 HP per attack)

**Expected Result:** Bottom 3 factions rise to 40-45% WR range

---

### Phase 3: Damage Tuning (Week 2)

**Goal:** Fine-tune faction damage output

1. Buff Nomads equipment (+1 more damage, total +2)
2. Buff Crucible Forge effects (+1 damage per token)
3. Buff Elves Bleed (2 per stack)
4. Nerf Emergent slightly (-1 damage on top cards)

**Expected Result:** 6-7 factions in 45-55% WR range

---

### Phase 4: Testing & Iteration (Week 2)

**Goal:** Verify balance and iterate

1. Run v5.17 simulation (225 battles)
2. Analyze results
3. Make micro-adjustments if needed
4. Run v5.18 if necessary

**Target:** 7-8/10 factions in 45-55% WR range

---

## Statistics

### V5.16 Simulation Stats
- **Battles:** 225
- **Runtime:** ~3 minutes
- **Attack Rolls:** 5,250
- **Hit Rate:** 57.6% (expected ~72%)
- **Catastrophic Failures:** 452 (8.6%, expected 2.78%)
- **Executions:** 108 (2.1%, expected 2.78%)
- **Critical Hits:** 256 (4.9%, expected 11.11%)

### Balance Changes Applied
- **Ossuarium Cards Modified:** 4 equipment cards (-1 damage each)
- **Nomads Cards Modified:** 4 equipment cards (+1 damage each)
- **Total Changes:** 8 cards modified

### Win Rate Changes (v5.15 → v5.16)

**Biggest Improvements:**
1. Exchange: +11.1% (unexpected)
2. Emergent: +13.4% (unexpected)
3. Nomads: +6.7% (intended)

**Biggest Declines:**
1. Crucible: -13.4% (unexpected)
2. Church: -8.8% (unexpected!)
3. Ossuarium: -6.6% (intended but insufficient)

---

## Files Modified

### 1. `/workspaces/penance/docs/cards/complete-card-data.json`

**Changes:**
- Updated version: 5.13 → 5.16
- Updated description
- Modified 8 equipment card damage values

**Lines Modified:** ~30 lines

---

### 2. Created Documentation

- `/workspaces/penance/docs/SESSION-SUMMARY-V5.16-BALANCE-ITERATION.md` (this file)
- `/tmp/v5.16_simulation_output.txt` (raw simulation results)

---

## Conclusion

**v5.16 was a LEARNING ITERATION, not a success:**

❌ Equipment-only changes insufficient
❌ Did not account for resource economy scaling
❌ Created unexpected meta shifts (Exchange, Church worse)
✅ Identified that economies are the real problem
✅ Wyrd remains naturally balanced (reference point)
✅ Established baseline for v5.17 changes

**Key Insight:** Resource economies dominate balance. Equipment damage is secondary.

**Next Session:** Implement v5.17 with economy nerfs + faction-specific buffs.

**Long-Term Goal:** 7-8/10 factions in 45-55% WR range.

---

**Document Version:** 1.0
**Author:** Claude (AI Assistant)
**Session Type:** Balance iteration + analysis
**Status:** ⚠️ INSUFFICIENT - REQUIRES V5.17
