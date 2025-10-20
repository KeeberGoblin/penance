# Combat Simulator v2.0 - Realistic Damage Scaling
## Summary Report

**Date:** October 19, 2025
**Purpose:** Rebuild simulation with correct damage values (1-4 damage range, not 4-12)

---

## THE PROBLEM WITH V1.0

**Old Simulator Issues:**
- Damage values: 4-12 per attack
- Component HP: Head 6, Arms 8, Chassis 10, Legs 8
- **Result:** Single attacks destroying entire limbs!
- Bloodlines "8/10/12 damage" = instant limb destruction

**Why This Was Wrong:**
Looking at actual game design (component-damage-system.md), attacks should deal **1-3 damage** normally, with 4-6 damage being rare "ultimate" attacks. The v1.0 simulator was testing values that would one-shot limbs every turn.

---

## V2.0 REALISTIC DAMAGE SCALING

**New Damage Values:**
- **Basic attacks:** 1-2 damage
- **Strong attacks:** 3 damage
- **Escalating attacks:** 2/3/4 damage (Bloodlines)
- **Random burst:** 1-4 damage (Nomads)

**Component HP (unchanged):**
- Head: 6 HP (AP 0-2, Structure 3-4, Exposure 5-6)
- Arms: 8 HP (AP 0-3, Structure 4-5, Exposure 6-8)
- Chassis: 10 HP (AP 0-4, Structure 5-6, Exposure 7-10)
- Legs: 8 HP (AP 0-3, Structure 4-8, No exposure)

---

## V2.0 INITIAL RESULTS (1,800 battles)

### Faction Win Rates

| Faction | WR% | Status | Key Mechanic |
|---------|-----|--------|--------------|
| **Bloodlines** | 94.4% | GOD-TIER | 2/3/4 escalating damage |
| **Dwarves** | 88.9% | GOD-TIER | -2 damage reduction (rune defense) |
| **Emergent** | 76.1% | TOO STRONG | 3 damage Metamorph |
| **Nomads** | 65.8% | TOO STRONG | 1-4 random damage |
| Wyrd | 33.9% | Too weak | 2 damage, 3 SP cost |
| Elves | 28.3% | Too weak | 1 damage + 1 Bleed |
| Crucible | 28.3% | Too weak | 2 damage |
| Exchange | 28.3% | Too weak | 2 damage |
| Church | 28.1% | Too weak | 2-3 damage (self-harm) |
| Ossuarium | 27.8% | Too weak | 2 damage, lifesteal |

**Balance Score: 0/10 factions balanced** (no factions in 45-55% range!)

---

## KEY FINDINGS

### 1. Dwarven Rune Defense is Overpowered

**Mechanic:** Gain 1 rune every 2 turns, max 2 runes, reduces incoming damage by 2

**Why It's Broken:**
- Most factions deal 2 damage/turn
- 2 damage - 2 rune defense = **0 damage**
- Dwarves become invincible after Turn 4
- Only loses to factions with high burst damage (Bloodlines, Emergent, Nomads)

**Win Rate Breakdown:**
- **vs Bloodlines:** 0% (Bloodlines 2/3/4 damage > 2 rune defense)
- **vs Everyone else:** 100% (blocks all 2 damage attacks)

**Fix Needed:** Reduce rune defense to -1 per rune, or cap at 1 rune

---

### 2. Bloodlines Escalating Damage is God-Tier (Again!)

**Mechanic:** 2/3/4 damage progression (1 base + stacks)

**Why It's Overpowered:**
- Turn 1: 2 damage (bypasses 1 rune)
- Turn 2: 3 damage (bypasses 2 runes)
- Turn 3+: 4 damage (crushes everyone)
- Only loses to Dwarves (rune defense reduces 4 → 2 damage)

**Even with realistic 2/3/4 damage, Bloodlines is catastrophically strong!**

**Fix Needed:** Reduce to 1/2/3 damage progression

---

### 3. Emergent Metamorph is Too Strong

**Mechanic:** 3 SP for 3 turns of 3 damage

**Why It's Overpowered:**
- 3 damage bypasses 2 rune defense (3 - 2 = 1 damage)
- Cheaper than most attacks (3 SP for 3 attacks = 1 SP/attack)
- Only loses to Dwarves (100%) and Bloodlines (100%)

**Fix Needed:** Reduce to 2 damage Metamorph

---

### 4. Most Factions Stuck at 2 Damage

**Factions with 2 damage attacks:**
- Church (2-3 with self-harm)
- Ossuarium (2 damage + lifesteal)
- Elves (1 damage + 1 Bleed)
- Crucible (2 damage)
- Exchange (2 damage)
- Wyrd (2 damage, defense bypass)

**Problem:** All hard-countered by Dwarven rune defense (-2 damage = 0 damage)

**Fix Needed:** Increase base damage to 3, OR reduce Dwarven rune defense to -1

---

### 5. Nomads Random Damage is Actually Strong

**Mechanic:** 1-4 random damage (average 2.5)

**Why It Works:**
- High rolls (3-4 damage) bypass Dwarven rune defense
- Variance creates unpredictability
- Average 2.5 damage > most factions' 2 damage

**Result:** 65.8% WR (too strong)

**Fix Needed:** Reduce to 1-3 random damage

---

## COMPARISON: V1.0 VS V2.0

| Metric | V1.0 (Broken) | V2.0 (Realistic) |
|--------|---------------|------------------|
| Damage Range | 4-12 | 1-4 |
| Combat Length | 5-10 turns | 8-17 turns |
| Component Destruction | 1-2 hits | 4-8 hits |
| Bloodlines WR | 70-82% (broken) | 94.4% (STILL broken!) |
| Balance Score | 1-4/10 balanced | 0/10 balanced |

**Key Insight:** Even with realistic damage, Bloodlines and Dwarves dominate due to mechanics, not damage values!

---

## NEXT STEPS FOR V2.0 BALANCE

### Round 1 Fixes (Conservative Approach)

**Nerfs:**
1. **Dwarves:** Rune defense -2 → -1 per rune
2. **Bloodlines:** Damage 2/3/4 → 1/2/3
3. **Emergent:** Metamorph 3 damage → 2 damage
4. **Nomads:** Random 1-4 → 1-3 damage

**Buffs:**
5. **Bottom 6 factions:** Increase base damage from 2 → 3

**Expected Result:** Bring top 4 down, lift bottom 6 up, converge toward 45-55% WR

---

## LESSONS LEARNED

1. **Always validate against game design docs first** - v1.0 wasted 30,600 battles testing wrong damage values
2. **Mechanics > Numbers** - Dwarven rune defense is broken regardless of damage values
3. **Escalating damage is inherently strong** - Bloodlines 2/3/4 is still god-tier even with "realistic" scaling
4. **Defense is powerful in low-damage games** - When most attacks deal 2 damage, -2 defense = invincibility

---

## FILES CREATED

1. **combat_simulator_v2.py** - New simulator with realistic 1-4 damage scaling
2. **faction_matchup_test_v2.py** - Comprehensive testing script
3. **faction_matchup_report_v2.txt** - Detailed matchup results

---

## STATUS

**V1.0 Simulator:** Deprecated (wrong damage scaling)
**V2.0 Simulator:** Active (realistic damage scaling)
**Balance Score:** 0/10 factions (needs Round 1 fixes)
**Total Battles Tested:** 1,800 (v2.0) + 30,600 (v1.0 deprecated) = 32,400 total

**Recommendation:** Proceed with Round 1 balance fixes using v2.0 simulator
