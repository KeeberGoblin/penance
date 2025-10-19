# Round 1 v2.0 - Post-Mortem Analysis
## "The Elven Apocalypse"

**Date:** October 19, 2025
**Result:** Mixed - 5/10 factions perfectly balanced, but catastrophic failures in Elves/Bloodlines/Nomads

---

## ROUND 1 RESULTS

| Faction | WR% | Status | Change from v2.0 Initial |
|---------|-----|--------|--------------------------|
| **Dwarves** | 94.4% | STILL GOD-TIER | +5.5% (was 88.9%) |
| **Elves** | 88.9% | CATASTROPHIC OVERBUFF | +60.6% (was 28.3%) |
| Wyrd | 55.6% | Slightly too strong | +21.7% (was 33.9%) |
| **Church** | 50.0% | PERFECT ✅ | +21.9% (was 28.1%) |
| **Ossuarium** | 50.0% | PERFECT ✅ | +22.2% (was 27.8%) |
| **Crucible** | 50.0% | PERFECT ✅ | +21.7% (was 28.3%) |
| **Exchange** | 50.0% | PERFECT ✅ | +21.7% (was 28.3%) |
| **Emergent** | 50.0% | PERFECT ✅ | -26.1% (was 76.1%) |
| **Bloodlines** | 11.1% | CATASTROPHIC OVER-NERF | -83.3% (was 94.4%) |
| **Nomads** | 0.0% | COMPLETE FAILURE | -65.8% (was 65.8%) |

**Balance Score:** 5/10 factions (Church, Ossuarium, Crucible, Exchange, Emergent)

---

## WHAT WENT RIGHT

### Success #1: 3 Damage Baseline is PERFECT

**Factions with 3 damage all hit exactly 50.0% WR:**
- Church: 3-4 damage (with self-harm) = 50.0% ✅
- Ossuarium: 3 damage + lifesteal = 50.0% ✅
- Crucible: 3 damage = 50.0% ✅
- Exchange: 3 damage = 50.0% ✅
- Emergent: 3 damage (Metamorph also 3) = 50.0% ✅

**Conclusion:** 3 damage/turn is the correct baseline for balance in realistic damage scaling!

---

### Success #2: Emergent Balanced Without Changes

**Result:** Emergent went from 76.1% WR (v2.0 initial) → 50.0% WR (Round 1) with NO changes to Metamorph.

**Why:** Metamorph 3 damage was overpowered when everyone dealt 2 damage, but balanced when everyone deals 3 damage.

**Lesson:** Faction strength is relative to the meta, not absolute damage values.

---

## WHAT WENT CATASTROPHICALLY WRONG

### Disaster #1: ELVES 3 DAMAGE + BLEED = DOUBLE DAMAGE

**The Bug:**
- **v2.0 Initial:** 1 base damage + 1 Bleed/turn = 2 total damage (balanced)
- **Round 1:** 3 base damage + 1 Bleed/turn = **6 total damage after 3 turns**

**Math Breakdown:**
```
Turn 1: 3 damage + 1 Bleed stack
Turn 2: 3 damage + 2 Bleed stacks = 5 damage
Turn 3+: 3 damage + 3 Bleed stacks = 6 damage/turn
```

**Why This is Broken:** Elves deal **DOUBLE** the damage of every other 3-damage faction!

**Result:** Elves 88.9% WR (only loses to Dwarves who have rune defense)

**My Mistake:** I buffed Elves base damage 1 → 3 without realizing Bleed stacks MULTIPLICATIVELY with base damage. Should have kept Elves at 1 damage OR removed Bleed mechanic.

**Fix for Round 2:** Reduce Elves to 2 damage (2 base + 2 Bleed = 4 total, more reasonable)

---

### Disaster #2: BLOODLINES 1/2/3 = OVER-NERFED

**The Issue:**
- **v2.0 Initial:** 2/3/4 escalating = 94.4% WR (too strong)
- **Round 1:** 1/2/3 escalating = 11.1% WR (catastrophic over-nerf)

**Why This Failed:**
- Turn 1-2: Bloodlines deals 1-2 damage (weakest in game)
- Turn 3+: Bloodlines deals 3 damage (equal to everyone else)
- Gets crushed in early game before ramping up

**Math Breakdown:**
```
Turn 1: 1 damage (opponent deals 3, Bloodlines -2 HP advantage)
Turn 2: 2 damage (opponent deals 3, Bloodlines -3 HP advantage total)
Turn 3+: 3 damage (equal trading, but already behind)
```

**Result:** Bloodlines 11.1% WR (only beats Nomads who deal 0 damage effectively)

**Fix for Round 2:** Increase to 2/3/4 escalating OR try 2/4/6 (aggressive ramp)

---

### Disaster #3: NOMADS 1-3 RANDOM = UNDER-BUFFED

**The Issue:**
- **v2.0 Initial:** 1-4 random (avg 2.5) = 65.8% WR when everyone dealt 2 damage
- **Round 1:** 1-3 random (avg 2) = 0.0% WR when everyone deals 3 damage

**Why This Failed:**
- Average 2 damage/turn < everyone else's 3 damage/turn
- Variance doesn't compensate for lower average
- Gets crushed by EVERYONE (even Bloodlines!)

**Fix for Round 2:** Increase to 2-4 random (avg 3 damage, same as everyone else)

---

### Problem #4: DWARVES RUNE DEFENSE STILL BROKEN

**Why Dwarves Still 94.4% WR:**
- Most factions deal 3 damage/turn
- Dwarves have 2 runes after Turn 4 (reduces 3 damage → 1 damage)
- Combat becomes 1 damage/turn vs 3 damage/turn
- Dwarves win via slow attrition (34 HP vs opponent's ~34 HP, but Dwarves deal 3x damage)

**Math Breakdown:**
```
Opponent: 34 HP, deals 3 damage/turn, takes 1 damage/turn (due to runes)
Dwarves: 34 HP, deals 3 damage/turn, takes 1 damage/turn

Time to kill opponent: 34 HP ÷ 3 dmg/turn = ~11 turns
Time for opponent to kill Dwarves: 34 HP ÷ 1 dmg/turn = 34 turns

Dwarves win in 11 turns, opponent needs 34 turns!
```

**Fix for Round 2:** Cap at 1 rune (3 damage → 2 damage = still good defense) OR remove rune defense entirely

---

### Problem #5: WYRD 3 DAMAGE + DEFENSE BYPASS = SLIGHTLY TOO STRONG

**Why Wyrd 55.6% WR:**
- Wyrd deals 3 damage/turn, same as everyone else
- BUT bypasses defense (ignores Dwarven runes)
- This gives Wyrd 100% WR vs Dwarves (who otherwise have 94.4% WR)

**Result:** Wyrd beats Dwarves, loses to Elves, ties with everyone else → 55.6% WR

**Fix for Round 2:** Reduce Wyrd to 2 damage (defense bypass compensates for lower damage)

---

## KEY INSIGHTS

### 1. Multiplicative Mechanics Scale Exponentially

**Elves Bleed Stacking:**
- 1 base + 1 Bleed = 2 total (balanced)
- 3 base + 1 Bleed = 6 total (catastrophically overpowered)

**Lesson:** When buffing base damage, MUST consider how it interacts with stacking mechanics!

---

### 2. Escalating Damage Needs Faster Ramp

**Bloodlines 1/2/3:**
- Too weak early (1-2 damage vs 3 damage)
- Doesn't compensate in late game (3 damage = everyone else)

**Lesson:** Escalating mechanics need to reach parity by Turn 2, not Turn 3

**Better Progression:** 2/3/4 OR 1/3/5 (skips Turn 2 weakness)

---

### 3. Dwarven Rune Defense is Fundamentally Broken

**History:**
- **v2.0 Initial:** -2 per rune (max 2 runes) = 88.9% WR
- **Round 1:** -1 per rune (max 2 runes) = 94.4% WR (WORSE!)

**Why -1 Rune is WORSE Than -2 Rune:**
- When everyone dealt 2 damage, -2 rune = 0 damage (invincible vs some factions)
- When everyone deals 3 damage, -2 rune = 1 damage/turn (slow grind, but beatable)
- When everyone deals 3 damage, -1 rune = 2 damage/turn... WAIT, THIS IS WRONG!

**ERROR IN MY ANALYSIS:** Dwarves have MAX 2 runes, so:
- -1 per rune × 2 runes = -2 total damage reduction
- 3 damage - 2 reduction = 1 damage/turn

**ACTUAL ISSUE:** Dwarves still reduce 3 damage → 1 damage with 2 runes at -1 each!

**Fix for Round 2:** Cap at 1 rune max (3 damage → 2 damage = 33% reduction, not 66%)

---

### 4. Defense Bypass is Powerful in Defense-Heavy Meta

**Wyrd 55.6% WR:**
- Only faction that can beat Dwarves (bypasses rune defense)
- This single advantage pushes WR above 50%

**Lesson:** Defense bypass is balanced when defenses are rare, overpowered when defenses are common

---

## ROUND 2 BALANCE PLAN

### Fix 1: Elves - Reduce Base Damage (3 → 2)
**Goal:** 2 base + 2 Bleed = 4 total damage (reasonable)
**Expected WR:** 88.9% → 50-55%

---

### Fix 2: Bloodlines - Restore 2/3/4 Escalating
**Goal:** Competitive early game (2 damage Turn 1), scales to 4 damage late
**Expected WR:** 11.1% → 50-55%

---

### Fix 3: Nomads - Increase to 2-4 Random
**Goal:** Average 3 damage (same as everyone else)
**Expected WR:** 0.0% → 45-50%

---

### Fix 4: Dwarves - Cap Runes at 1 Max
**Goal:** 3 damage - 1 rune = 2 damage/turn (33% reduction, not 66%)
**Expected WR:** 94.4% → 50-55%

---

### Fix 5: Wyrd - Reduce to 2 Damage
**Goal:** 2 damage + defense bypass = competitive vs Dwarves, balanced vs others
**Expected WR:** 55.6% → 48-52%

---

## FILES MODIFIED IN ROUND 1

All changes in **combat_simulator_v2.py:**

1. Line 122: Dwarven rune defense (-2 per rune → -1 per rune)
2. Lines 248-251: Church Blood Offering (2-3 → 3-4 damage)
3. Line 263: Dwarves attack (2 → 3 damage)
4. Lines 271, 292: Ossuarium Soul Harvest (2 → 3 damage)
5. Line 298: Elves base attack (1 → 3 damage) **← CATASTROPHIC OVERBUFF**
6. Line 307: Crucible attack (2 → 3 damage)
7. Lines 315, 320: Exchange Mercenary (2 → 3 damage)
8. Line 326: Nomads random (1-4 → 1-3 damage) **← OVER-NERF**
9. Line 335: Bloodlines escalating (2/3/4 → 1/2/3) **← CATASTROPHIC OVER-NERF**
10. Line 357: Emergent base (2 → 3 damage)
11. Lines 365, 381: Wyrd Reality Distortion (2 → 3 damage) **← SLIGHT OVERBUFF**

---

## STATISTICS

**Total Battles:** 1,800 (Round 1)
**Balance Score:** 5/10 factions (improvement from v2.0 initial: 0/10)
**Perfect Factions:** Church, Ossuarium, Crucible, Exchange, Emergent (all 50.0% WR)
**Failed Factions:** Dwarves (94.4%), Elves (88.9%), Bloodlines (11.1%), Nomads (0.0%)

---

## LESSONS LEARNED

1. **Multiplicative mechanics scale exponentially** - Elves Bleed + base damage = disaster
2. **Escalating damage needs faster ramp** - Bloodlines 1/2/3 can't compete with 3-damage factions
3. **Defense reduction is always powerful** - Dwarves -1 or -2 per rune both catastrophic
4. **Variance doesn't compensate for low average** - Nomads 1-3 random (avg 2) loses to consistent 3 damage
5. **3 damage is the correct baseline** - 5 factions with 3 damage all hit exactly 50.0% WR!

---

## STATUS

**Next Action:** Implement Round 2 fixes (Elves 2 dmg, Bloodlines 2/3/4, Nomads 2-4, Dwarves 1 rune cap, Wyrd 2 dmg)
**Expected Result:** 8-9/10 factions in 45-55% range
