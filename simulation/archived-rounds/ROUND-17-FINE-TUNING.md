# Round 17 - Fine-Tuning Pass
## "Tightening the Margins"

**Date:** October 19, 2025
**Goal:** Bring remaining 6 factions into 45-55% WR range

---

## ROUND 16 RESULTS (Before Round 17)

| Faction | WR% | Status | Action |
|---------|-----|--------|--------|
| **Wyrd** | 61.4% | TOO STRONG | Nerf Reality Distortion |
| **Exchange** | 61.1% | TOO STRONG | Nerf Mercenary Contract |
| **Emergent** | 50.0% | PERFECT ✅ | No changes |
| **Nomads** | 47.5% | PERFECT ✅ | No changes |
| **Elves** | 45.3% | PERFECT ✅ | No changes |
| **Crucible** | 45.3% | PERFECT ✅ | No changes |
| Church | 44.7% | Close | Buff Blood Offering |
| Bloodlines | 40.8% | Too weak | Buff Biomass |
| Ossuarium | 39.2% | Too weak | Buff Soul Harvest |
| Dwarves | 38.9% | Too weak | Buff damage |

**Progress:** 4/10 factions balanced (Emergent, Nomads, Elves, Crucible)

---

## ROUND 17 FIXES IMPLEMENTED

### Fix 1: Exchange - Mercenary Contract (6 → 5 damage)
**File:** `combat_simulator.py:348`

**BEFORE (Round 16 - TOO STRONG):**
```python
base_damage = 6  # 6 damage for 2 SP
```

**AFTER (Round 17 - NERFED):**
```python
base_damage = 5  # NERFED: 5 damage (6 was too strong)
```

**Why:** Exchange had 61.1% WR (100% vs Emergent). Reduce damage 6 → 5.
**Expected WR:** 61.1% → 50-55%

---

### Fix 2: Wyrd - Reality Distortion (5 → 4 damage)
**File:** `combat_simulator.py:425`

**BEFORE (Round 16 - TOO STRONG):**
```python
base_damage = 5  # 5 damage, ignores defense
```

**AFTER (Round 17 - NERFED):**
```python
base_damage = 4  # NERFED: 4 damage (5 was too strong), ignores defense
```

**Why:** Wyrd had 61.4% WR (100% vs Crucible, 85% vs Dwarves). Reduce damage 5 → 4.
**Expected WR:** 61.4% → 50-55%

---

### Fix 3: Church - Blood Offering (+1 → +2)
**File:** `combat_simulator.py:229`

**BEFORE (Round 16 - SLIGHTLY WEAK):**
```python
attacker.blood_offering_bonus = 1  # +1 damage
```

**AFTER (Round 17 - BUFFED):**
```python
attacker.blood_offering_bonus = 2  # BUFFED: +2 (was +1)
```

**Why:** Church had 44.7% WR (close to target). Restore +2 bonus.
**Expected WR:** 44.7% → 48-52%

---

### Fix 4: Dwarves - Base Damage (4 → 5)
**File:** `combat_simulator.py:249`

**BEFORE (Round 16 - TOO WEAK):**
```python
base_damage = 4  # 4 damage
```

**AFTER (Round 17 - BUFFED):**
```python
base_damage = 5  # BUFFED: 5 damage (4 was too weak)
```

**Why:** Dwarves had 38.9% WR. Tried in Round 13 with rune cap 3 (73.1% WR = catastrophic). This time ONLY buffing damage, keeping rune cap at 2.
**Expected WR:** 38.9% → 48-52%

---

### Fix 5: Bloodlines - Biomass (7/9/11 → 8/10/12)
**File:** `combat_simulator.py:380`

**BEFORE (Round 16 - TOO WEAK):**
```python
base_damage = 5 + (attacker.biomass_stacks * 2)  # 7/9/11 progression
```

**AFTER (Round 17 - BUFFED):**
```python
base_damage = 6 + (attacker.biomass_stacks * 2)  # BUFFED: 8/10/12 progression
```

**Why:** Bloodlines had 40.8% WR. 8/10/12 was catastrophic in Rounds 10 (82.8%) and 15 (81.9%), BUT those rounds had Bloodlines as the ONLY strong faction. In Round 17, Wyrd/Exchange are also strong, which should keep Bloodlines in check.
**Expected WR:** 40.8% → 48-53%

---

### Fix 6: Ossuarium - Soul Harvest (4 → 5 damage, FREE → 1 SP)
**File:** `combat_simulator.py:263`

**BEFORE (Round 16 - TOO WEAK):**
```python
if attacker.sp >= 0:
    # FREE activation (0 SP cost)
    base_damage = 4
```

**AFTER (Round 17 - BUFFED):**
```python
if attacker.sp >= 1:
    attacker.sp -= 1
    base_damage = 5  # BUFFED: 5 damage (was 4)
```

**Why:** Ossuarium had 39.2% WR. Increase damage 4 → 5, restore 1 SP cost (better than free 4 damage).
**Expected WR:** 39.2% → 48-52%

---

## KEY INSIGHT: BLOODLINES 8/10/12 - THIRD ATTEMPT

**Previous Attempts:**
- **Round 10:** 8/10/12 = 82.8% WR (CATASTROPHIC) - Bloodlines was god-tier, crushed everyone
- **Round 15:** 8/10/12 = 81.9% WR (CATASTROPHIC) - Church also at 72.2%, Bloodlines dominated
- **Round 17:** 8/10/12 = ??? - Wyrd/Exchange/Church all strong now, Bloodlines may be balanced

**Theory:** 8/10/12 damage is only catastrophic when Bloodlines is the ONLY strong faction. With multiple S-tier factions, Bloodlines should be kept in check.

---

## EXPECTED RESULTS (Target: 45-55% WR)

### Should Be Balanced After Round 17:
- **Emergent:** 50.0% ✅ (no changes)
- **Nomads:** 47.5% ✅ (no changes)
- **Elves:** 45.3% ✅ (no changes)
- **Crucible:** 45.3% ✅ (no changes)
- **Exchange:** 61.1% → 50-55% (Mercenary 5 damage)
- **Wyrd:** 61.4% → 50-55% (Reality Distortion 4 damage)
- **Church:** 44.7% → 48-52% (Blood Offering +2)
- **Dwarves:** 38.9% → 48-52% (5 damage)
- **Bloodlines:** 40.8% → 48-53% (8/10/12 damage, but with strong meta)
- **Ossuarium:** 39.2% → 48-52% (5 damage, 1 SP cost)

**Expected Progress:** 9-10/10 factions balanced after Round 17!

---

## DWARVES SINGLE-BUFF APPROACH

**Round 13 Catastrophe:** Dwarves got TWO buffs (rune cap 3 + damage 5) = 73.1% WR

**Round 17 Conservative Approach:** ONLY buff damage (4 → 5), keep rune cap at 2

**Why This Should Work:**
- 5 damage is balanced (tested in many factions)
- Rune cap 2 prevents over-defense
- Single buff avoids Round 13 catastrophe

---

## FILES MODIFIED

1. **combat_simulator.py:229** - Church Blood Offering (+1 → +2)
2. **combat_simulator.py:249** - Dwarves base damage (4 → 5)
3. **combat_simulator.py:263** - Ossuarium Soul Harvest (FREE 4 dmg → 1 SP 5 dmg)
4. **combat_simulator.py:348** - Exchange Mercenary Contract (6 → 5 damage)
5. **combat_simulator.py:380** - Bloodlines Biomass (7/9/11 → 8/10/12)
6. **combat_simulator.py:425** - Wyrd Reality Distortion (5 → 4 damage)

---

## BLOODLINES ROLLERCOASTER (Complete History)

| Round | WR% | Biomass Damage | Result |
|-------|-----|----------------|--------|
| 5 | 36.1% | 6/8/10 | Too weak |
| 10 | 82.8% | 8/10/12 | CATASTROPHIC (god-tier) |
| 11 | 54.2% | 7/9/11 | BALANCED! |
| 14 | 39.2% | 7/9/11 | Too weak (meta shift) |
| 15 | 81.9% | 8/10/12 | CATASTROPHIC (god-tier again) |
| 16 | 40.8% | 7/9/11 | Too weak |
| 17 | ??? | 8/10/12 | Third attempt (with strong meta) |

---

## STATUS

**Running:** Round 17 fine-tuning test (1,800 battles)
**Expected Completion:** ~3-5 minutes
**Goal:** 9-10/10 factions in 45-55% range

**Total Battles So Far:** 28,800 (16 rounds × 1,800 battles)
