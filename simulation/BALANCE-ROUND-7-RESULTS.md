# Balance Round 7: Post-Equipment Balance Changes

**Date**: 2025-10-20
**Database Version**: 5.2 (after first balance pass)
**Test Size**: 225 battles (10 factions × 9 matchups × 5 runs)

---

## Results Summary

| Faction | Win Rate | Change from Round 6 | Status |
|---------|----------|---------------------|--------|
| Church | 93.3% | -2.3% | ❌ STILL CATASTROPHIC |
| Dwarves | 84.4% | +22.5% | ❌ WORSE |
| Elves | 71.1% | +5.5% | ❌ WORSE |
| Crucible | 60.0% | +6.7% | ⚠️ SLIGHTLY HIGH |
| Exchange | 53.3% | +4.4% | ✅ BALANCED |
| Nomads | 37.8% | -10.0% | ❌ COLLAPSED |
| Ossuarium | 31.1% | -35.8% | ❌ CATASTROPHIC COLLAPSE |
| Bloodlines | 28.9% | +2.2% | ❌ STILL WEAK |
| Emergent | 20.0% | +2.2% | ❌ STILL CATASTROPHIC |
| Wyrd | 20.0% | -8.9% | ❌ WORSE |

**Balance Score**: 1/10 factions in target range (45-55%)

---

## Critical Findings

### The Balance Changes FAILED

**What We Changed**:
- Church: -7 damage nerfs (average damage reduced ~1.0 per card)
- Dwarves: -5 damage nerfs
- Elves: Noted bleed cap needs reduction (not equipment)
- Emergent: +6 damage buffs (+1 per attack)
- Bloodlines: +2 damage buffs, reduced Biomass costs
- Wyrd: +6 damage buffs (+1 per attack)

**What Happened**:
- Church BARELY dropped (95.6% → 93.3% = -2.3%)
- Dwarves SKYROCKETED (+22.5% = from 61.9% to 84.4%)
- Emergent only gained +2.2% (17.8% → 20.0%)
- Ossuarium COLLAPSED (-35.8% = from 66.9% to 31.1%)

### Root Cause Analysis

**Church is NOT overpowered due to equipment**:
- Equipment damage nerfs had almost no effect (-2.3%)
- Church's power comes from **faction cards** (Blood Offering, Martyr's Resolve)
- **Blood Offering**: Discard 2 cards → +3 damage, ignore 1 Armor (broken combo card)
- Average 23.4 damage/game indicates faction card abuse, not equipment

**Ossuarium collapse mystery**:
- Lost 35.8% WR in one round (66.9% → 31.1%)
- **No changes were made to Ossuarium equipment**
- Hypothesis: New equipment for other factions countered Ossuarium's lifesteal strategy
- Nomads also collapsed (-10% = 47.8% → 37.8%), similar issue

**Emergent/Wyrd buffs too small**:
- +1 damage per card = +6 total damage over entire game
- Still losing 80% of matches (20% WR)
- Need +2-3 damage per card, not +1

---

## Why Equipment Balance Alone Won't Fix This

### Equipment Impact: ~20-40% of Total Damage

From simulation data:
- Church: 23.4 avg damage/game (equipment contributes ~8-10 damage)
- Dwarves: 12.8 avg damage/game (equipment contributes ~5-7 damage)
- Bloodlines: 0.0 avg damage/game (equipment contributes ~6-8 damage)

**Equipment damage is NOT the primary balance lever.**

### Faction Cards Are the Real Problem

**Overpowered Faction Mechanics**:
- **Church Blood Offering**: +3 damage, ignore Armor (combo enabler)
- **Elves Bleed Stacking**: 6 bleed cap × 1 dmg/turn = 30+ free damage over game
- **Dwarves Rune Defense**: Permanent +1 Defense per Rune = invincibility

**Underpowered Faction Mechanics**:
- **Emergent Metamorph**: Requires 3 turns of setup, minimal payoff
- **Bloodlines Biomass**: Takes 5+ turns to generate enough tokens
- **Wyrd Taint**: Hurts user more than opponent (anti-synergy)

---

## Action Items

### Immediate: Faction Card Balance Pass

**Nerf These Cards**:
1. **Church - Blood Offering**: Change from "Discard 2 cards → +3 damage" to "Discard 2 cards → +2 damage"
2. **Elves - Bleed Cap**: Reduce from 6 stacks to 4 stacks (already noted)
3. **Dwarves - Rune Defense**: Change from "+1 Defense per Rune" to "+1 Defense per 2 Runes"

**Buff These Cards**:
1. **Emergent - Metamorph Activation**: Reduce from "Discard 3 cards" to "Discard 2 cards"
2. **Bloodlines - Biomass Generation**: Double generation rate (2 tokens per kill instead of 1)
3. **Wyrd - Taint Effects**: Remove self-damage, keep only opponent penalties

### Medium-Term: Equipment Damage Increase

**Current Problem**: Average combat length 37.6 turns (too grindy)

**Solution**: Global +1 damage to ALL equipment attacks (compensate for long games)

### Long-Term: Casket Class Rebalancing

**Scout (28 HP, 6 SP)**: Too fragile, dies in 5-6 hits
**Colossus (50 HP, 4 SP)**: Too slow, can't kill before dying of attrition

---

## Test Plan

1. **Faction Card Balance Pass**: Modify 6 faction core cards
2. **Re-run Simulation**: Test faction card changes (Round 8)
3. **If still imbalanced**: Apply global equipment damage buffs
4. **Target**: 7-10 factions in 45-55% WR range

---

## Conclusion

**Equipment balance alone cannot fix Penance.**

The core faction mechanics (Blood Offering, Bleed, Runes, Biomass) are the primary balance drivers. Equipment contributes only 20-40% of total damage.

**Next Step**: Balance faction cards (not equipment) to achieve game-wide balance.

---

**[← Previous: Round 6](archived-rounds/round-6-equipment-update.md)** | **[Next: Faction Card Balance Pass →](FACTION-CARD-BALANCE-NEEDED.md)**
