# Round 2 v2.0 - Post-Mortem Analysis
## "The Bloodlines Resurrection"

**Date:** October 19, 2025
**Result:** CATASTROPHIC - went from 5/10 balanced → 1/10 balanced

---

## ROUND 2 RESULTS

| Faction | Round 1 WR% | Round 2 WR% | Change | Status |
|---------|-------------|-------------|--------|--------|
| **Bloodlines** | 11.1% | 94.2% | +83.1% | CATASTROPHIC OVERBUFF (100% vs everyone except Dwarves) |
| **Dwarves** | 94.4% | 94.4% | 0.0% | UNCHANGED - rune cap 1 didn't work! |
| **Nomads** | 0.0% | 49.7% | +49.7% | PERFECT ✅ (only success!) |
| Church | 50.0% | 44.4% | -5.6% | Now slightly weak |
| Ossuarium | 50.0% | 44.2% | -5.8% | Now slightly weak |
| **Elves** | 88.9% | 43.9% | -45.0% | MASSIVE OVERCORRECTION |
| Emergent | 50.0% | 43.6% | -6.4% | Now slightly weak |
| Exchange | 50.0% | 43.1% | -6.9% | Now slightly weak |
| Crucible | 50.0% | 42.5% | -7.5% | Now slightly weak |
| **Wyrd** | 55.6% | 0.0% | -55.6% | CATASTROPHIC OVER-NERF (0% WR!) |

**Balance Score:** 1/10 factions (Nomads only)

**Regression:** Round 1 had 5 perfect factions (Church, Ossuarium, Crucible, Exchange, Emergent @ 50.0% WR), Round 2 has NONE of them balanced!

---

## WHAT WENT CATASTROPHICALLY WRONG

### Disaster #1: BLOODLINES 2/3/4 IS STILL GOD-TIER

**History:**
| Round | Damage Progression | WR% | Result |
|-------|-------------------|-----|--------|
| v2.0 Initial | 2/3/4 | 94.4% | GOD-TIER |
| Round 1 | 1/2/3 | 11.1% | CATASTROPHIC UNDER |
| Round 2 | 2/3/4 | 94.2% | GOD-TIER AGAIN! |

**Why 2/3/4 is Broken:**
- Turn 1: 2 damage (competitive with everyone's 3 damage)
- Turn 2: 3 damage (equal to everyone)
- Turn 3+: 4 damage (BEST in game, 33% more than everyone!)

**Matchup Results:**
- vs Dwarves: 100% WR (4 damage > 1 rune defense)
- vs Everyone Else: 100% WR (4 damage > their 3 damage)
- **Total: 94.2% WR**

**Conclusion:** ANY escalation ending at 4+ damage is fundamentally broken!

**Fix Needed:** Cap max damage at 3 (escalation 1/2/3 OR 2/2/3 OR flat 3)

---

### Disaster #2: DWARVEN RUNE CAP 1 DIDN'T FIX ANYTHING

**What I Changed:**
- Round 1: Rune cap 2 (max -2 damage reduction)
- Round 2: Rune cap 1 (max -1 damage reduction)

**Result:** Dwarves STILL 94.4% WR (unchanged!)

**Why It Failed:**
```
Everyone: Deals 3 damage/turn, takes 2 damage/turn (3 - 1 rune)
Dwarves: Deals 3 damage/turn, takes 2 damage/turn (from opponents)

Time to kill opponent: 34 HP ÷ 3 dmg/turn = ~11 turns
Time for opponent to kill Dwarves: 34 HP ÷ 2 dmg/turn = 17 turns

Dwarves win in 11 turns, opponents need 17 turns = Dwarves always win!
```

**CRITICAL ERROR IN MY LOGIC:**
- I thought reducing rune cap 2 → 1 would help
- BUT: 3 damage - 1 rune = 2 damage taken
- Dwarves still have 33% damage reduction (3 → 2)
- This is ENOUGH to dominate when everyone deals same damage!

**Matchup Results:**
- vs Everyone: 100% WR (2 damage taken < 3 damage dealt = slow grind wins)
- **Total: 94.4% WR**

**Fix Needed:** REMOVE rune defense entirely, give Dwarves different mechanic (maybe +1 HP/turn regen OR counter-attack)

---

### Disaster #3: WYRD 2 DAMAGE = CATASTROPHIC OVER-NERF

**What I Changed:**
- Round 1: 3 damage + defense bypass
- Round 2: 2 damage + defense bypass

**Result:** Wyrd 0.0% WR (loses to EVERYONE!)

**Why It Failed:**
- 2 damage < everyone's 3 damage/turn
- Defense bypass is WORTHLESS when base damage is too low
- Even vs Dwarves: 2 damage < Dwarves' 3 damage (defense bypass doesn't compensate for being 33% weaker!)

**Matchup Results:**
- vs Everyone: 0% WR (2 damage < 3 damage = always loses)
- **Total: 0.0% WR**

**Lesson:** Defense bypass is a utility mechanic, NOT a primary damage source. Cannot compensate for 33% damage deficit!

**Fix Needed:** Restore to 3 damage (defense bypass is niche advantage vs Dwarves, not main strength)

---

### Disaster #4: ELVES 2 DAMAGE + BLEED = OVERCORRECTED

**History:**
| Round | Base Damage | Bleed/Turn | Total Damage (Turn 3) | WR% | Result |
|-------|-------------|------------|----------------------|-----|--------|
| v2.0 Initial | 1 | 1 | 2 | 28.3% | Too weak |
| Round 1 | 3 | 1 | 6 | 88.9% | TOO STRONG (double damage!) |
| Round 2 | 2 | 1 | 4 | 43.9% | Too weak again |

**Why 2 Base + 1 Bleed is Too Weak:**
- Turn 1: 2 damage (vs everyone's 3 damage)
- Turn 2: 3 damage (2 base + 1 Bleed, equal to everyone)
- Turn 3+: 4 damage (2 base + 2 Bleed, slightly better)

**Problem:** Bleed takes 2-3 turns to ramp up, by which time Elves are already behind!

**Math:**
```
Turn 1-2: Elves deals 2+3 = 5 total, opponent deals 3+3 = 6 total (Elves -1 HP)
Turn 3-5: Elves deals 4×3 = 12, opponent deals 3×3 = 9 (Elves +3 HP)
Overall: Elves +2 HP advantage after 5 turns (not enough!)
```

**Fix Needed:** Increase Bleed to +2 per stack (2 base + 4 Bleed = 6 total by Turn 2) OR increase base to 3 and cap Bleed at 2 stacks

---

### Problem #5: The Ripple Effect - Why Did 5 Factions Drop?

**Round 1 Perfect Factions (all 50.0% WR):**
- Church, Ossuarium, Crucible, Exchange, Emergent

**Round 2 Results (all 42-44% WR):**
- Why did they all drop 6-8 percentage points?

**Answer: Bloodlines Dominated Them All!**

**Matchup Breakdown:**
- Church vs Bloodlines: 0-20 (0% WR)
- Ossuarium vs Bloodlines: 0-20 (0% WR)
- Crucible vs Bloodlines: 0-20 (0% WR)
- Exchange vs Bloodlines: 0-20 (0% WR)
- Emergent vs Bloodlines: 0-20 (0% WR)

**Ripple Effect:**
- Bloodlines went from 11.1% → 94.2% WR
- This crushed all 5 previously balanced factions
- They dropped from 50.0% → 42-44% WR

**Lesson:** Overbuffing ONE faction destroys the entire meta!

---

## THE ONLY SUCCESS: NOMADS

**What I Changed:**
- Round 1: 1-3 random damage (avg 2)
- Round 2: 2-4 random damage (avg 3)

**Result:** Nomads 49.7% WR (PERFECT!)

**Why It Worked:**
- Average 3 damage/turn = same as everyone else
- Variance (2-4 range) creates interesting gameplay
- High rolls (4 damage) beat Dwarves sometimes
- Low rolls (2 damage) lose to Bloodlines

**Matchup Breakdown:**
- vs Dwarves: 0% WR (Dwarves too strong)
- vs Bloodlines: 5% WR (Bloodlines too strong)
- vs Everyone Else: 60-85% WR (competitive)
- **Average: 49.7% WR ✅**

**Lesson:** 2-4 random (avg 3) is the correct random damage range for balance!

---

## KEY INSIGHTS

### 1. Escalating Damage MUST Cap at 3

**Tested:**
- 2/3/4 escalation = 94.4% WR (v2.0 Initial)
- 1/2/3 escalation = 11.1% WR (Round 1)
- 2/3/4 escalation = 94.2% WR (Round 2)

**Conclusion:** ANY escalation reaching 4+ damage is god-tier! Must cap at 3.

**Possible Fixes:**
- 1/2/3 (tested, too weak early)
- 2/2/3 (2 damage Turn 1-2, 3 damage Turn 3+)
- Flat 3 (remove escalation entirely)

---

### 2. Defense Reduction is Always Overpowered

**Dwarven Rune Defense History:**
- v2.0 Initial: -2 per rune (max 2 runes) = 88.9% WR
- Round 1: -1 per rune (max 2 runes) = 94.4% WR
- Round 2: -1 per rune (max 1 rune) = 94.4% WR

**Pattern:** EVERY iteration is overpowered (88-94% WR)!

**Why:** When everyone deals same damage, even small damage reduction creates massive advantage over time!

**Fix:** REMOVE damage reduction entirely, give Dwarves different mechanic

---

### 3. Defense Bypass Cannot Compensate for Low Damage

**Wyrd History:**
- Round 1: 3 damage + bypass = 55.6% WR (slightly strong)
- Round 2: 2 damage + bypass = 0.0% WR (catastrophic)

**Lesson:** 2 damage < 3 damage, regardless of bypass. Defense bypass is utility, not primary damage!

**Fix:** Keep Wyrd at 3 damage (bypass is niche advantage, not main strength)

---

### 4. Bleed Scaling is Deceptive

**Elves History:**
| Base | Bleed | Turn 3 Total | WR% |
|------|-------|-------------|-----|
| 1 | 1 | 2 | 28.3% (too weak) |
| 3 | 1 | 6 | 88.9% (BROKEN) |
| 2 | 1 | 4 | 43.9% (too weak) |

**Insight:** Bleed looks strong on paper, but takes 2-3 turns to ramp! By then, Elves are already behind.

**Fix:** Faster Bleed ramp (+2 per stack) OR higher base damage (3) with capped Bleed (2 stacks max)

---

### 5. Overbuffing ONE Faction Destroys the Meta

**Round 1 → Round 2:**
- Bloodlines went from 11.1% → 94.2% WR
- This crushed 5 previously balanced factions (Church, Ossuarium, Crucible, Exchange, Emergent)
- They dropped from 50.0% → 42-44% WR

**Lesson:** NEVER overbuff a faction! Better to underbuff and iterate up.

---

## ROUND 3 BALANCE PLAN

### Fix 1: Bloodlines - Remove Escalation Entirely
**Goal:** Flat 3 damage (no escalation)
**Expected WR:** 94.2% → 45-50%

---

### Fix 2: Dwarves - REMOVE Rune Defense
**Goal:** Give Dwarves +1 HP regen/turn OR counter-attack mechanic
**Expected WR:** 94.4% → 45-50%

---

### Fix 3: Wyrd - Restore to 3 Damage
**Goal:** 3 damage + defense bypass (niche advantage vs Dwarves)
**Expected WR:** 0.0% → 48-52%

---

### Fix 4: Elves - Increase Bleed to +2 Per Stack
**Goal:** 2 base + 2 Bleed/turn = 6 total by Turn 2 (faster ramp)
**Expected WR:** 43.9% → 50-55%

---

### Fix 5: Church/Ossuarium/Crucible/Exchange/Emergent - BUFF to 4 Damage
**Goal:** Compensate for Bloodlines/Dwarves dominance
**Expected WR:** 42-44% → 48-52%

---

## FILES MODIFIED IN ROUND 2

All changes in **combat_simulator_v2.py:**

1. Line 259: Dwarven rune cap (2 → 1) **← DIDN'T WORK**
2. Line 298: Elves base damage (3 → 2) **← OVERCORRECTED**
3. Line 326: Nomads random (1-3 → 2-4) **← SUCCESS! ✅**
4. Line 335: Bloodlines escalating (1/2/3 → 2/3/4) **← CATASTROPHIC OVERBUFF**
5. Lines 365, 381: Wyrd Reality Distortion (3 → 2) **← CATASTROPHIC OVER-NERF**

---

## STATISTICS

**Total Battles:** 3,600 (Round 1: 1,800 + Round 2: 1,800)
**Balance Score:** 1/10 factions (Nomads only)
**Regression:** Round 1 had 5 balanced factions, Round 2 has 1!

---

## LESSONS LEARNED

1. **Escalating damage MUST cap at 3** - Any progression reaching 4+ damage is god-tier
2. **Defense reduction is always overpowered** - Even 1 rune (-1 damage) dominates when everyone deals same damage
3. **Defense bypass cannot compensate for low damage** - 2 damage + bypass < 3 damage
4. **Bleed takes too long to ramp** - 2 base + 1 Bleed looks good but loses early game
5. **Overbuffing ONE faction destroys the meta** - Bloodlines 94.2% WR crushed 5 balanced factions

---

## STATUS

**Next Action:** Implement Round 3 fixes (remove Bloodlines escalation, remove Dwarven runes, restore Wyrd 3 dmg, buff Elves Bleed, buff bottom 5 to 4 damage)
**Expected Result:** 6-8/10 factions in 45-55% range
