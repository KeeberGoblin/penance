# Round 6 - Final Balance Fixes
## "Perfect Balance Achievement"

**Date:** October 19, 2025
**Goal:** Bring all 10 factions to 45-55% win rate target

---

## ROUND 5 RESULTS (Before Round 6)

| Faction | WR% | Status | Issues |
|---------|-----|--------|--------|
| **Ossuarium** | 66.9% | TOO STRONG | 100% vs 6 factions, lifesteal too powerful |
| **Elves** | 65.6% | TOO STRONG | 80% vs Exchange, 75% vs Dwarves, bleed cap 8 |
| **Dwarves** | 61.9% | TOO STRONG | 100% vs 5 factions, minimum 1 damage rule |
| **Church** | 50.0% | PERFECT ✅ | No changes needed |
| Nomads | 37.5% | Too weak | Needs buffs |
| Bloodlines | 36.1% | TOO WEAK | Biomass 6/8/10 too low |
| Crucible | 35.0% | Too weak | Needs buffs |
| Exchange | 35.0% | Too weak | Needs buffs |
| Wyrd | 34.4% | Too weak | Needs buffs |
| Emergent | 34.2% | Too weak | Needs buffs |

---

## ROUND 6 FIXES IMPLEMENTED

### Fix 1: Dwarves - Remove Minimum Damage Rule
**File:** `combat_simulator.py:107`, `team_combat_test.py`

**BEFORE:**
```python
amount = max(1, amount - reduction)  # Minimum 1 damage always goes through
```

**AFTER:**
```python
amount = max(0, amount - reduction)  # BALANCED: No minimum damage (was 1)
```

**Why This Fixes Dwarves:**
- Removes the guaranteed minimum 1 damage
- With 2 rune counters, 2 damage attacks now deal 0 damage
- Forces enemies to use higher damage abilities
- **Expected WR:** 61.9% → 50-55%

---

### Fix 2: Elves - Reduce Bleed Cap from 8 → 6
**File:** `combat_simulator.py:288`, `team_combat_test.py:188`

**BEFORE:**
```python
defender.bleed_counters = min(defender.bleed_counters + 2, 8)  # Cap 8
```

**AFTER:**
```python
defender.bleed_counters = min(defender.bleed_counters + 2, 6)  # BALANCED: Cap 6 (was 8)
```

**Why This Fixes Elves:**
- Max bleed damage reduced from 8 → 6
- Total damage per turn: 2 (attack) + 6 (bleed) = 8 damage (vs 10 before)
- Still strong DoT fantasy, but less overwhelming
- **Expected WR:** 65.6% → 52-57%

---

### Fix 3: Bloodlines - Increase Biomass Damage
**File:** `combat_simulator.py:377`, `team_combat_test.py`

**BEFORE:**
```python
# Damage scales: 4 + (stacks × 2) = 6/8/10 progression
base_damage = 4 + (attacker.biomass_stacks * 2)
```

**AFTER:**
```python
# Damage scales: 5 + (stacks × 2) = 7/9/11 progression (BUFFED from 6/8/10)
base_damage = 5 + (attacker.biomass_stacks * 2)  # BUFFED: 5 base (was 4)
```

**Why This Fixes Bloodlines:**
- Crashed from 84.7% WR to 36.1% WR (over-nerfed in Round 5)
- Damage progression: 7/9/11 (vs 6/8/10 before)
- Costs 2 SP per use, stacks up to 3 times
- **Expected WR:** 36.1% → 48-52%

---

### Fix 4: Ossuarium - Replace Lifesteal with Taint Exploitation (v3.0)
**File:** `combat_simulator.py:254-290`, `team_combat_test.py:146-180`

**BEFORE (Lifesteal - BROKEN):**
```python
# Ossuarium: Soul Harvest (BALANCED - costs 4 SP, 75% lifesteal)
if attacker.sp >= 4:
    attacker.sp -= 4
    base_damage = 4
    defender.take_damage(base_damage)

    # Recover cards equal to damage dealt (75% lifesteal, max 3)
    cards_recovered = 3
    for _ in range(cards_recovered):
        if attacker.discard:
            recycled = attacker.discard.pop()
            attacker.hand.append(recycled)
```

**AFTER (Taint Exploitation - v3.0 Mechanic):**
```python
# Ossuarium: Taint Exploitation (v3.0 mechanic - NO lifesteal!)
if attacker.sp >= 3:  # Reduced from 4 SP to 3 SP
    attacker.sp -= 3
    base_damage = 4
    defender.take_damage(base_damage)

    # Defender gains Taint (1 per 2 damage dealt)
    taint_gained = base_damage // 2  # 4 dmg = 2 Taint
    defender.taint_counters += taint_gained

    # Attacker can spend 2 Taint to recover 2 cards (NO FREE LIFESTEAL!)
    if attacker.taint_counters >= 2:
        attacker.taint_counters -= 2
        cards_recovered = 2
        for _ in range(cards_recovered):
            if attacker.discard:
                recycled = attacker.discard.pop()
                attacker.hand.append(recycled)
```

**Key Changes:**
1. **NO FREE LIFESTEAL** - Ossuarium must have Taint tokens to recover cards
2. **Taint Application** - Defender gains 2 Taint when Ossuarium deals 4 damage
3. **Taint Spending** - Ossuarium spends 2 Taint to recover 2 cards (50% lifesteal, NOT free)
4. **SP Cost Reduced** - 3 SP (vs 4 SP before) to compensate for conditional recovery
5. **Thematic v3.0 Mechanic** - Matches official Taint Exploitation rules

**Why This Fixes Ossuarium:**
- Lifesteal was fundamentally broken (free sustain every turn)
- Taint system requires setup (must build Taint before recovering)
- Recovery reduced from 3 cards → 2 cards (50% lifesteal)
- Still has sustain, but not infinite
- **Expected WR:** 66.9% → 48-53%

---

## EXPECTED RESULTS (Target: 45-55% WR)

### S-Tier → Balanced:
- **Ossuarium:** 66.9% → 48-53% (Taint replaces lifesteal)
- **Elves:** 65.6% → 52-57% (Bleed cap 6)
- **Dwarves:** 61.9% → 50-55% (No minimum damage)

### Church (Already Perfect):
- **Church:** 50.0% → 50-52% (No changes)

### Bottom-Tier → Balanced:
- **Bloodlines:** 36.1% → 48-52% (Biomass buffed to 7/9/11)
- Nomads: 37.5% → ? (needs monitoring)
- Crucible: 35.0% → ? (needs monitoring)
- Exchange: 35.0% → ? (needs monitoring)
- Wyrd: 34.4% → ? (needs monitoring)
- Emergent: 34.2% → ? (needs monitoring)

---

## FILES MODIFIED

1. **combat_simulator.py** - Main simulation engine
   - Line 107: Dwarves minimum damage removed
   - Line 254-290: Ossuarium Taint Exploitation
   - Line 288: Elves bleed cap reduced to 6
   - Line 377: Bloodlines Biomass damage buffed to 7/9/11

2. **team_combat_test.py** - Team combat scenarios
   - Line 146-180: Ossuarium Taint Exploitation
   - Line 188: Elves bleed cap reduced to 6

---

## TEST PLAN

**Running:** `faction_matchup_test.py` (1,800 battles: 10 factions × 9 opponents × 20 runs)

**Success Criteria:**
- All factions between 45-55% WR
- No faction has 100% or 0% matchups
- No matchup exceeds 70% WR
- Ossuarium vs Dwarves stalemate resolved (or acceptable)

---

## ROLLBACK PLAN

If any faction is still outside 45-55% range:
1. **Ossuarium too strong (>55%)** - Increase Taint cost to 3 tokens
2. **Ossuarium too weak (<45%)** - Reduce Taint cost to 1 token
3. **Elves too strong (>55%)** - Reduce bleed cap to 5
4. **Elves too weak (<45%)** - Increase bleed cap to 7
5. **Dwarves too strong (>55%)** - Reduce rune cap to 1
6. **Dwarves too weak (<45%)** - Restore minimum 1 damage
7. **Bloodlines too strong (>55%)** - Reduce Biomass to 6/8/10
8. **Bloodlines too weak (<45%)** - Increase Biomass to 8/10/12

---

## NOTES

- **Ossuarium Taint Exploitation** is a v3.0 official mechanic, not a placeholder
- **Church** has been perfectly balanced since Round 1 (no changes in 5 rounds!)
- **Bloodlines** had the wildest swing: 71.1% → 84.7% → 36.1% → ???
- **Dwarves vs Ossuarium** stalemate may persist (tank vs sustain matchup)

---

## STATUS

**In Progress:** Round 6 final balance test running...
**Expected Completion:** ~3-5 minutes (1,800 battles)
**Next Steps:** Analyze results, apply any final tweaks if needed
