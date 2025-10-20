# Round 15 - Convergence Push
## "Bottom 5 Buffs + Top 2 Nerfs"

**Date:** October 19, 2025
**Goal:** Bring all factions closer to 45-55% WR target

---

## ROUND 14 RESULTS (Before Round 15)

| Faction | WR% | Status | Action Needed |
|---------|-----|--------|---------------|
| **Exchange** | 65.8% | TOO STRONG | Nerf Mercenary Contract |
| **Wyrd** | 62.2% | TOO STRONG | Nerf Reality Distortion |
| **Elves** | 51.1% | PERFECT ✅ | No changes |
| **Emergent** | 49.7% | PERFECT ✅ | No changes |
| **Crucible** | 45.6% | PERFECT ✅ | No changes |
| Nomads | 43.6% | Too weak | Buff damage |
| Dwarves | 40.0% | Too weak | Keep current |
| Bloodlines | 39.2% | Too weak | Buff Biomass |
| Church | 38.9% | Too weak | Buff Blood Offering |
| Ossuarium | 36.1% | TOO WEAK | FREE Soul Harvest |

**Progress:** 3/10 factions balanced (Elves, Emergent, Crucible)

---

## ROUND 15 FIXES IMPLEMENTED

### Fix 1: Church - Blood Offering Buff
**File:** `combat_simulator.py:229`

**BEFORE:**
```python
attacker.blood_offering_bonus = 1  # +1 damage
```

**AFTER:**
```python
attacker.blood_offering_bonus = 2  # BUFFED: +2 (was +1)
```

**Why This Should Work:**
- Restoration of Round 11 power level (was +3 → +2 → +1)
- 6 damage attack (4 base + 2 bonus) for cost of 1 card
- **Expected WR:** 38.9% → 48-52%

---

### Fix 2: Ossuarium - FREE Soul Harvest
**File:** `combat_simulator.py:260-282`

**BEFORE:**
```python
if attacker.sp >= 1:
    attacker.sp -= 1  # 1 SP cost
    self.log_event(f"Soul Harvest (1 SP) for {base_damage} damage...")
```

**AFTER:**
```python
if attacker.sp >= 0:
    # FREE activation (0 SP cost)
    self.log_event(f"Soul Harvest (FREE) for {base_damage} damage...")
```

**Why This Should Work:**
- Eliminates SP cost entirely (was 4 → 3 → 2 → 1 → 0)
- Every turn: Deal 4 damage, gain 2 Taint, recover 2 cards (50% lifesteal)
- Still requires Taint accumulation before recovery
- **Expected WR:** 36.1% → 48-53%

---

### Fix 3: Bloodlines - Biomass Buff (8/10/12)
**File:** `combat_simulator.py:380`

**BEFORE:**
```python
base_damage = 5 + (attacker.biomass_stacks * 2)  # 7/9/11 progression
```

**AFTER:**
```python
base_damage = 6 + (attacker.biomass_stacks * 2)  # BUFFED: 8/10/12 progression
```

**Why This Should Work:**
- Tried in Round 10: 38.6% → 82.8% (TOO STRONG with other buffs)
- This time ONLY Bloodlines getting buffed (no combo effects)
- **Expected WR:** 39.2% → 50-55%

---

### Fix 4: Nomads - Damage Increase (7-10)
**File:** `combat_simulator.py:362`

**BEFORE:**
```python
base_damage = random.randint(6, 9)  # 6-9 random damage
```

**AFTER:**
```python
base_damage = random.randint(7, 10)  # BUFFED: 7-10 random damage
```

**Why This Should Work:**
- Average damage: 7.5 → 8.5 (+13% increase)
- Free activation (0 SP)
- **Expected WR:** 43.6% → 48-52%

---

### Fix 5: Exchange - Mercenary Contract Nerf
**File:** `combat_simulator.py:348`

**BEFORE:**
```python
base_damage = 6  # 6 damage for 2 SP
```

**AFTER:**
```python
base_damage = 5  # NERFED: 5 damage (was 6)
```

**Why This Should Work:**
- Revert to Round 13 value (oscillated 6 → 5 → 6 → 5)
- **Expected WR:** 65.8% → 52-57%

---

### Fix 6: Wyrd - Reality Distortion Nerf
**File:** `combat_simulator.py:425`

**BEFORE:**
```python
base_damage = 5  # 5 damage, ignores defense, 4 SP cost
```

**AFTER:**
```python
base_damage = 4  # NERFED: 4 damage (was 5), ignores defense
```

**Why This Should Work:**
- 4 damage for 4 SP cost (1:1 ratio)
- Still bypasses all defense (including Dwarven runes)
- **Expected WR:** 62.2% → 52-57%

---

## DWARVES (NO CHANGES)

**Current State:** 40.0% WR
- Rune cap: 2
- Base damage: 4
- Minimum damage: 1

**Why No Changes:**
- Round 13 double-buff catastrophe (37.8% → 73.1% WR)
- Let other factions stabilize first
- Dwarves may rise naturally as meta shifts

---

## EXPECTED RESULTS (Target: 45-55% WR)

### Should Be Balanced After Round 15:
- **Church:** 38.9% → 48-52% (Blood Offering +2)
- **Ossuarium:** 36.1% → 48-53% (FREE Soul Harvest)
- **Bloodlines:** 39.2% → 50-55% (Biomass 8/10/12)
- **Nomads:** 43.6% → 48-52% (Damage 7-10)
- **Exchange:** 65.8% → 52-57% (Mercenary 5 damage)
- **Wyrd:** 62.2% → 52-57% (Reality Distortion 4 damage)

### Already Balanced:
- **Elves:** 51.1% ✅
- **Emergent:** 49.7% ✅
- **Crucible:** 45.6% ✅

### Still Needs Attention:
- **Dwarves:** 40.0% (monitoring)

**Expected Progress:** 9/10 factions balanced after Round 15!

---

## FILES MODIFIED

1. **combat_simulator.py:229** - Church Blood Offering (+1 → +2)
2. **combat_simulator.py:260-282** - Ossuarium Soul Harvest (1 SP → FREE)
3. **combat_simulator.py:348** - Exchange Mercenary Contract (6 → 5 damage)
4. **combat_simulator.py:362** - Nomads Improvised Weapon (6-9 → 7-10 damage)
5. **combat_simulator.py:380** - Bloodlines Biomass (7/9/11 → 8/10/12)
6. **combat_simulator.py:425** - Wyrd Reality Distortion (5 → 4 damage)

---

## ROUND HISTORY

- **Round 13:** Dwarves 37.8% → 73.1% (double-buff disaster)
- **Round 14:** Dwarves reverted, 3/10 balanced (Elves/Emergent/Crucible)
- **Round 15:** Bottom 5 buffs + Top 2 nerfs

---

## BLOODLINES HISTORY (The Rollercoaster)

- **Round 5:** 36.1% WR (too weak)
- **Round 10:** 82.8% WR (CATASTROPHIC OVERBUFF - 8/10/12 damage)
- **Round 11:** 54.2% WR (reverted to 7/9/11)
- **Round 14:** 39.2% WR (too weak again)
- **Round 15:** ??? (trying 8/10/12 again, but in isolation)

**Key Difference:** Round 10 had multiple simultaneous buffs. Round 15 only buffs Bloodlines.

---

## STATUS

**Running:** Round 15 convergence test (1,800 battles)
**Expected Completion:** ~3-5 minutes
**Goal:** 9/10 factions in 45-55% range
