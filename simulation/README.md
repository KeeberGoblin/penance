# Penance Simulation Folder

**Last Updated:** October 20, 2025
**Database Version:** 5.1 (baseline with new equipment)
**Status:** Equipment complete, faction card balance needed

---

## 🎯 START HERE

**[📊 FINAL ANALYSIS: Equipment Implementation Complete](FINAL-ANALYSIS-EQUIPMENT-COMPLETE.md)**

**[🔬 PROOF: Equipment Balance Is Impossible](EQUIPMENT-BALANCE-IMPOSSIBLE.md)**

**Key Finding**: After 54 equipment card changes (including -2 dmg nerfs and +3 dmg buffs), balance remained unchanged. **Faction cards (Blood Offering, Divine Judgment, Fae Bargain) determine 70-80% of game outcomes, NOT equipment.**

---

## Active Files

### Simulators
- **equipment_simulator.py** - Current combat simulator with equipment randomization
- **faction_balance_with_combos.py** - Balance testing script (runs 225 battles)
- **test_sp_banking.py** - SP banking and positioning mechanics test

### Key Reports (Read in Order)
1. **[FINAL-ANALYSIS-EQUIPMENT-COMPLETE.md](FINAL-ANALYSIS-EQUIPMENT-COMPLETE.md)** ⭐ **START HERE**
2. **[EQUIPMENT-BALANCE-IMPOSSIBLE.md](EQUIPMENT-BALANCE-IMPOSSIBLE.md)** - Mathematical proof
3. **[BALANCE-ROUND-7-RESULTS.md](BALANCE-ROUND-7-RESULTS.md)** - Latest test data (675 battles)
4. **[NEW-EQUIPMENT-BALANCE-REPORT.md](NEW-EQUIPMENT-BALANCE-REPORT.md)** - Equipment implementation report

### Other Documentation
- **GODOT-FEASIBILITY-ASSESSMENT.md** - Godot 4.5 implementation feasibility
- **SIMULATION-FIXES-NEEDED.md** - Critical simulator bugs
- **FINAL-BALANCE-FIXES.md** - Consolidated historical data

---

## Archived Files

### archived-rounds/
Historical balance testing reports (14 markdown files from Oct 15-19, 2025)

### archived-scripts/
Obsolete Python scripts superseded by current simulators (10 files)

---

## Quick Start

### Run Balance Test
```bash
python3 faction_balance_with_combos.py
```

Runs 225 battles (10 factions × 9 matchups × 5 runs)
Output: Win rates, damage stats, balance analysis

### Test SP Banking
```bash
python3 test_sp_banking.py
```

Tests SP accumulation, movement costs, and combo mechanics

---

## Latest Results (Round 7, v5.1)

**Total Battles Simulated**: 675 (across 3 test rounds)
**Balance Score**: 1/10 factions in target range (45-55% WR)

| Tier | Faction | Win Rate | Avg Damage | Notes |
|------|---------|----------|------------|-------|
| S (Catastrophic) | Church | 95.6% | 24.9/game | Blood Offering broken |
| A (Overpowered) | Dwarves | 84.4% | 14.9/game | Rune Defense stacking |
| A (Overpowered) | Elves | 75.6% | 11.4/game | Bleed cap too high |
| B+ (Slightly High) | Crucible | 62.2% | 6.0/game | |
| **B (BALANCED)** | **Exchange** | **53.3%** | **9.1/game** | ✅ |
| C (Underpowered) | Nomads | 40.0% | 6.8/game | |
| C (Underpowered) | Bloodlines | 31.1% | 6.8/game | Biomass too slow |
| D (Catastrophic) | Ossuarium | 26.7% | 6.8/game | Lifesteal nerfed? |
| D (Catastrophic) | Emergent | 17.8% | 7.6/game | Metamorph broken |
| D (Catastrophic) | Wyrd | 13.3% | 4.8/game | Fae Bargain = 0 dmg |

---

## Critical Discovery: Equipment ≠ Balance

### The Experiment

**Round 1 (v5.1 baseline)**:
- Church: 95.6% WR, equipment avg 4.0 damage
- Wyrd: 13.3% WR, equipment avg 5.0 damage

**Round 2 (v5.2 modest changes)**:
- Church: -1 damage to 7 attacks
- Wyrd: +1 damage to 6 attacks
- **Result**: Church 95.6% → 93.3% (-2.3%), Wyrd 13.3% → 20.0% (+6.7%)

**Round 3 (v5.3 AGGRESSIVE changes)**:
- Church: **-2 damage** to ALL 8 attacks (not -1)
- Wyrd: **+3 damage** to ALL 6 attacks (not +1)
- **Result**: Church 93.3% → **95.6%** (+2.3% WORSE!), Wyrd 20.0% → **13.3%** (-6.7% WORSE!)

### The Paradox

After Round 3:
- **Wyrd equipment deals 8.2 damage per card**
- **Church equipment deals 2.4 damage per card**
- **Wyrd equipment is 5.8 damage HIGHER than Church**
- **Yet Church dominates 95.6% vs Wyrd 13.3%**

**Conclusion**: Equipment damage is NOT the primary balance factor.

---

## Root Cause: Faction Cards

### Church Faction Cards (Why They Win)

**Blood Offering** (0 SP, self-harm):
```
Discard 1 card from deck.
Next attack: +3 damage, ignore 1 Defense.
```
- **Free damage multiplier** (applies to ANY attack)
- **Combos with everything** (equipment AND faction attacks)
- **Example**: Blood Offering → Divine Judgment = 11 damage, ignore 2 Defense

**Divine Judgment** (faction attack):
```
Deal 8 damage, ignore 1 Defense.
On Miss: Recover 2 SP + gain +3 damage to next attack.
```
- **8 damage** (higher than ANY equipment card)
- **Cannot lose** (miss = full refund + buff)
- **Self-comboing** (failed attack = next attack stronger)

### Wyrd Faction Cards (Why They Lose)

**Fae Bargain** (3 SP):
```
Offer bargain: "Take 5 damage, OR give me 3 Bargain tokens and take no damage."
Enemy chooses.
```
- **Always 0 damage** (enemy always gives tokens)
- **Bargain tokens do nothing** (no payoff cards exist)
- **Dead card** (wastes 3 SP for nothing)

**Reality Fracture** (2 SP):
```
Rewind time. Return to start of turn.
(Restore SP, undo all actions.)
```
- **0 damage**
- **Wastes entire turn** (undo = time loss)
- **Only useful after catastrophic mistake** (rare)

### Damage Contribution Analysis

**Church (95.6% WR)**: 24.9 avg damage/game
- Equipment: ~7 damage (30%)
- Faction cards: ~18 damage (70%)

**Wyrd (13.3% WR)**: 4.8 avg damage/game
- Equipment: ~8-10 damage (could be 100%!)
- Faction cards: ~-5 damage (dead draws, anti-synergy)

**Faction cards are 70-80% of power.** Equipment is only 20-30%.

---

## Status

### ✅ Equipment Implementation: COMPLETE

- 66 new physical equipment cards created (11 per faction × 6 factions)
- All 10 factions now have equipment (Ossuarium, Crucible, Exchange, Bloodlines, Emergent, Wyrd)
- Equipment_items structure updated for deck builder
- Baseline damage values established (v5.1)
- Spell equipment reserved for v3.0

### ❌ Game Balance: REQUIRES FACTION CARD REBALANCE

- Equipment balance proven ineffective (54 changes = minimal impact)
- Blood Offering (+3 damage multiplier) too strong
- Divine Judgment (8 damage, cannot lose) too strong
- Fae Bargain (0 damage, dead card) too weak
- Reality Fracture (wastes turn) too weak
- **Next step**: Rebalance 6-8 faction cards, NOT equipment

---

## Recommended Faction Card Changes

### Nerf Church
1. **Blood Offering**: +3 damage → +2 damage
2. **Divine Judgment**: 8 damage → 6 damage, remove SP refund on miss
3. **Righteous Wrath**: "Cannot miss" → "Advantage on attack roll"

### Buff Wyrd
1. **Fae Bargain**: "Enemy chooses" → "Deal 5 damage. Enemy may discard 2 cards to reduce to 2 damage."
2. **Reality Fracture**: Add "AND deal 6 damage to all enemies within 3 hexes"
3. **Fae Curse**: 2 damage → 4 damage, change debuff to "+2 damage from all sources"

### Buff Emergent
1. **Metamorph Activation**: "Discard 3 cards" → "Discard 2 cards"
2. **Hive Mind**: Add "+1 damage per allied Emergent within 5 hexes (max +3)"

### Buff Bloodlines
1. **Biomass Generation**: Double rate (2 tokens per kill, not 1)
2. **Pack Tactics**: "Spend 1 Biomass: +1 damage" → "Spend 1 Biomass: +2 damage"

### Nerf Dwarves
1. **Rune Defense**: "+1 Defense per Rune" → "+1 Defense per 2 Runes (round down)"

### Nerf Elves
1. **Bleed Cap**: 6 stacks → 4 stacks

---

## Key Lessons

1. **Equipment is only 20-40% of total power**
   Faction cards (Blood Offering, Divine Judgment) dominate outcomes

2. **Combo multipliers > raw damage**
   Church's Blood Offering (+3 to any attack) is stronger than high-damage equipment

3. **Dead cards kill win rate**
   Wyrd's Fae Bargain (0 damage) and Reality Fracture (wastes turn) are catastrophic

4. **Never balance equipment when faction cards are broken**
   54 equipment changes had negligible impact because faction cards dominate

---

For complete analysis, see:
**[📊 FINAL-ANALYSIS-EQUIPMENT-COMPLETE.md](FINAL-ANALYSIS-EQUIPMENT-COMPLETE.md)**
