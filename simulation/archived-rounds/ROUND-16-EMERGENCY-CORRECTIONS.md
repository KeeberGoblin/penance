# Round 16 - Emergency Corrections
## "Bloodlines Catastrophe Revert"

**Date:** October 19, 2025
**Crisis:** Bloodlines 8/10/12 damage caused 81.9% WR (100% vs 7 factions!)

---

## ROUND 15 CATASTROPHE

| Faction | WR% | Status | Problem |
|---------|-----|--------|---------|
| **Bloodlines** | 81.9% | CATASTROPHIC | 100% vs 7 factions, 8/10/12 damage too strong |
| **Church** | 72.2% | TOO STRONG | Blood Offering +2 too powerful |
| **Elves** | 51.4% | PERFECT ✅ | No changes |
| **Emergent** | 45.8% | PERFECT ✅ | No changes |
| Crucible | 44.7% | Close | Slightly weak |
| Ossuarium | 43.6% | Close | Improved from 36.1% |
| Dwarves | 41.7% | Too weak | Slightly improved |
| Nomads | 33.3% | TOO WEAK | CRASHED from 43.6%! |
| Exchange | 31.7% | TOO WEAK | CRASHED from 65.8%! |
| Wyrd | 17.2% | CATASTROPHIC | 0% vs 3 factions, 4 damage too weak |

**Key Insight:** Bloodlines 8/10/12 damage = ALWAYS catastrophic (Round 10: 82.8% WR, Round 15: 81.9% WR)

---

## ROUND 16 FIXES IMPLEMENTED

### Fix 1: Bloodlines - Revert to 7/9/11
**File:** `combat_simulator.py:380`

**BEFORE (Round 15 - BROKEN):**
```python
base_damage = 6 + (attacker.biomass_stacks * 2)  # 8/10/12 progression
```

**AFTER (Round 16 - REVERTED):**
```python
base_damage = 5 + (attacker.biomass_stacks * 2)  # 7/9/11 progression (REVERTED)
```

**Why:** 8/10/12 damage has proven catastrophic in BOTH Round 10 and Round 15. 7/9/11 is the maximum safe damage.

---

### Fix 2: Church - Blood Offering Back to +1
**File:** `combat_simulator.py:229`

**BEFORE (Round 15 - TOO STRONG):**
```python
attacker.blood_offering_bonus = 2  # +2 damage
```

**AFTER (Round 16 - REVERTED):**
```python
attacker.blood_offering_bonus = 1  # +1 damage (was +2, too strong!)
```

**Why:** Round 15 Church had 72.2% WR (100% vs Bloodlines/Wyrd). Revert to Round 14 state (38.9% → 48.6% expected).

---

### Fix 3: Exchange - Restore to 6 Damage
**File:** `combat_simulator.py:348`

**BEFORE (Round 15 - TOO WEAK):**
```python
base_damage = 5  # 5 damage
```

**AFTER (Round 16 - RESTORED):**
```python
base_damage = 6  # 6 damage (5 was too weak)
```

**Why:** Round 15 Exchange crashed to 31.7% WR (0% vs Ossuarium/Bloodlines). Restore to Round 14 value (65.8% → 50-55% expected with Bloodlines nerf).

---

### Fix 4: Wyrd - Restore to 5 Damage
**File:** `combat_simulator.py:425`

**BEFORE (Round 15 - TOO WEAK):**
```python
base_damage = 4  # 4 damage
```

**AFTER (Round 16 - RESTORED):**
```python
base_damage = 5  # 5 damage (4 was too weak)
```

**Why:** Round 15 Wyrd crashed to 17.2% WR (0% vs Church/Ossuarium/Bloodlines). Restore to Round 14 value (62.2% → 50-55% expected with Bloodlines nerf).

---

### Fix 5: Nomads - Increase to 8-11 Damage
**File:** `combat_simulator.py:362`

**BEFORE (Round 15 - STILL TOO WEAK):**
```python
base_damage = random.randint(7, 10)  # 7-10 damage
```

**AFTER (Round 16 - BUFFED AGAIN):**
```python
base_damage = random.randint(8, 11)  # 8-11 damage
```

**Why:** Round 15 Nomads CRASHED to 33.3% WR (0% vs Church/Bloodlines, worse than Round 14's 43.6%). Average damage: 8.5 → 9.5.

---

## KEY INSIGHT: THE BLOODLINES EFFECT

**Bloodlines at 8/10/12 damage creates a "god faction" effect:**
- 100% win rate vs 7 different factions (Elves, Crucible, Exchange, Nomads, Emergent, Wyrd, and ties Dwarves)
- Only loses to Church (0%)
- Crushes entire meta, making all other factions appear weaker

**When Bloodlines is nerfed back to 7/9/11:**
- Church should drop from 72.2% → ~48-52% (loses free wins vs Bloodlines)
- Exchange should rise from 31.7% → ~50-55% (no longer crushed by Bloodlines)
- Wyrd should rise from 17.2% → ~50-55% (no longer crushed by Bloodlines)
- Elves/Emergent should remain balanced

---

## EXPECTED RESULTS (Target: 45-55% WR)

### Should Be Balanced After Round 16:
- **Elves:** 51.4% ✅ (no changes)
- **Emergent:** 45.8% ✅ (no changes)
- **Church:** 72.2% → 48-52% (Blood Offering +1, loses Bloodlines matchup)
- **Exchange:** 31.7% → 50-55% (restored to 6 damage, Bloodlines weakened)
- **Wyrd:** 17.2% → 50-55% (restored to 5 damage, Bloodlines weakened)
- **Bloodlines:** 81.9% → 48-52% (reverted to 7/9/11)
- **Nomads:** 33.3% → 45-50% (damage 8-11)

### Still Needs Attention:
- **Crucible:** 44.7% (close, may rise naturally)
- **Ossuarium:** 43.6% (close, may rise naturally)
- **Dwarves:** 41.7% (needs buffs)

**Expected Progress:** 7-8/10 factions balanced after Round 16!

---

## BLOODLINES HISTORY (Complete Rollercoaster)

- **Round 5:** 36.1% WR (too weak, Biomass 6/8/10)
- **Round 10:** 82.8% WR (CATASTROPHIC, Biomass 8/10/12)
- **Round 11:** 54.2% WR (reverted to 7/9/11, BALANCED!)
- **Round 14:** 39.2% WR (too weak after meta shift)
- **Round 15:** 81.9% WR (CATASTROPHIC AGAIN, tried 8/10/12)
- **Round 16:** ??? (reverted to 7/9/11 AGAIN)

**Lesson Learned:** Bloodlines 8/10/12 = Always catastrophic. 7/9/11 is the maximum safe damage.

---

## FILES MODIFIED

1. **combat_simulator.py:229** - Church Blood Offering (+2 → +1)
2. **combat_simulator.py:348** - Exchange Mercenary Contract (5 → 6 damage)
3. **combat_simulator.py:362** - Nomads Improvised Weapon (7-10 → 8-11 damage)
4. **combat_simulator.py:380** - Bloodlines Biomass (8/10/12 → 7/9/11)
5. **combat_simulator.py:425** - Wyrd Reality Distortion (4 → 5 damage)

---

## STATUS

**Running:** Round 16 emergency corrections test (1,800 battles)
**Expected Completion:** ~3-5 minutes
**Goal:** 7-8/10 factions in 45-55% range
