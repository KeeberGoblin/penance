# Round 7 - Emergency Ossuarium Fix
## "Taint Mechanic Corrected"

**Date:** October 19, 2025
**Crisis:** Ossuarium crashed from 66.9% → 16.7% WR due to broken Taint implementation

---

## THE PROBLEM (Round 6 Catastrophe)

**Round 6 Implementation (BROKEN):**
```python
# Defender gains Taint (1 per 2 damage dealt)
taint_gained = base_damage // 2  # 4 dmg = 2 Taint
defender.taint_counters += taint_gained  # ❌ WRONG! Applied to defender

# Attacker can spend 2 Taint to recover 2 cards
if attacker.taint_counters >= 2:  # ❌ Attacker has 0 Taint!
    attacker.taint_counters -= 2
    cards_recovered = 2
```

**What Went Wrong:**
- Ossuarium applied Taint **to the defender**, not itself
- Ossuarium never gained Taint counters
- Could never spend Taint to recover cards
- Result: 4 damage attack with **0 sustain** for 3 SP = terrible value
- **Ossuarium WR: 66.9% → 16.7%** (weakest faction in game!)

---

## THE FIX (Round 7 Emergency)

**Round 7 Implementation (FIXED):**
```python
# FIXED: Ossuarium gains Taint from damage dealt (1 per 2 damage)
taint_gained = base_damage // 2  # 4 dmg = 2 Taint
attacker.taint_counters += taint_gained  # ✅ CORRECT! Applied to Ossuarium

# Spend 2 Taint to recover 2 cards (conditional lifesteal!)
if attacker.taint_counters >= 2:
    attacker.taint_counters -= 2
    cards_recovered = 2
    for _ in range(cards_recovered):
        if attacker.discard:
            recycled = attacker.discard.pop()
            attacker.hand.append(recycled)
    attacker._invalidate_hp_cache()
```

**How It Works Now:**
- **Turn 1:** Deal 4 damage → Gain 2 Taint → Spend 2 Taint → Recover 2 cards (50% lifesteal)
- **Turn 2+:** Deal 4 damage → Gain 2 Taint → Spend 2 Taint → Recover 2 cards (50% lifesteal)
- **Every turn:** Consistent 50% lifesteal (2 cards per 4 damage)
- **Cost:** 3 SP per use (tactical decision vs movement/defense)

---

## EXPECTED RESULTS

**Ossuarium Recovery:**
- Round 6: 16.7% WR (0% vs Dwarves/Elves/Wyrd)
- Round 7 Target: 45-55% WR (with working Taint mechanic)

**Why This Should Work:**
- 50% lifesteal (2 cards per 4 damage) is balanced
- 3 SP cost forces tactical choices
- No longer free sustain (must use ability)
- Similar to Round 2 Ossuarium (68.6% WR with 75% lifesteal)
- Reduced from 75% → 50% lifesteal should bring WR down to 45-55%

---

## OTHER FACTIONS (Still Need Attention)

From Round 6 results, these factions also need fixes:

**Still Overpowered:**
- **Wyrd: 74.4% WR** (100% vs 4 factions) - Reality Distortion 4 SP cost too expensive, spamming basic attacks
- **Elves: 70.0% WR** (100% vs 4 factions) - Bleed cap 6 still too strong
- **Exchange: 63.9% WR** (80% vs 3 factions) - Mercenary Contract damage too high
- **Emergent: 61.7% WR** (85% vs 2 factions) - Metamorph too strong

**Still Underpowered:**
- **Nomads: 33.3% WR** (0% vs 2 factions) - Needs buffs
- **Bloodlines: 36.7% WR** (0% vs 2 factions) - Biomass 7/9/11 still too weak
- **Crucible: 43.6% WR** (0% vs 2 factions) - Slightly weak
- **Dwarves: 44.2% WR** (0% vs 1 faction) - Slightly weak

**Perfectly Balanced:**
- **Church: 48.9% WR** ✅ (no changes needed!)

---

## FILES MODIFIED

1. **combat_simulator.py:254-288** - Ossuarium Taint Exploitation fix
   - Changed `defender.taint_counters += taint_gained` → `attacker.taint_counters += taint_gained`

2. **team_combat_test.py:146-178** - Ossuarium Taint Exploitation fix
   - Same fix as combat_simulator.py

---

## NEXT STEPS (After Round 7 Results)

If Ossuarium is fixed (45-55% WR), then address remaining imbalances:

**Round 8 Candidate Fixes:**
1. **Wyrd** - Reduce Reality Distortion SP cost to 2 (from 4) OR increase base damage
2. **Elves** - Reduce bleed cap to 5 (from 6) OR reduce base damage to 1
3. **Exchange** - Reduce Mercenary Contract damage to 6 (from 7)
4. **Emergent** - Reduce Metamorph bonus to +0 (from +1) OR increase SP cost to 3
5. **Bloodlines** - Increase Biomass damage to 8/10/12 (from 7/9/11)
6. **Nomads** - Increase random damage to 5-8 (from 4-7)

---

## STATUS

**Running:** Round 7 emergency fix test (1,800 battles)
**Expected Completion:** ~3-5 minutes
**Critical Fix:** Ossuarium Taint mechanic (16.7% → 45-55% WR expected)
