# Army-Based Balance Test Results (v5.14c)

**Date:** October 20, 2025
**Test Type:** Point-Based Army Power Comparison (Simplified)
**Difficulty:** Easy (4 points)
**Point Costs:** Scout=2, Warden=3, Vanguard=4, Colossus=5, Support=1

---

## Power Rankings

**Power Score = Total HP + (Total SP × 5) + (Unit count × 10)**

| Rank | Faction | Avg Power | Relative % | Variance from Single-Unit |
|------|---------|-----------|------------|---------------------------|
| 1 | **Ossuarium** | 109.1 | 100.0% | +48.9% (6th → 1st) |
| 2 | **Emergent** | 106.4 | 97.5% | +33.1% (5th → 2nd) |
| 3 | **Elves** | 105.3 | 96.4% | +67.5% (8th → 3rd) |
| 4 | **Church** | 101.0 | 92.5% | +79.2% (9th → 4th) |
| 5 | **Nomads** | 97.0 | 88.9% | +13.3% (2nd → 5th) |
| 6 | **Crucible** | 96.6 | 88.5% | -8.5% (1st → 6th) |
| 7 | **Exchange** | 96.0 | 87.9% | -21.2% (4th → 7th) |
| 8 | **Bloodlines** | 95.2 | 87.2% | -13.9% (3rd → 8th) |
| 9 | **Wyrd** | 94.3 | 86.4% | +44.2% (7th → 9th) |
| 10 | **Dwarves** | 74.5 | 68.2% | +63.8% (10th → 10th) |

---

## Comparison to Single-Unit Combat (v5.14)

### Single-Unit Combat Results (Actual Battles)

| Rank | Faction | WR% | Status |
|------|---------|-----|--------|
| 1 | Crucible | 80.0% | ⚠️ OP |
| 2 | Nomads | 75.6% | ⚠️ OP |
| 3 | Bloodlines | 73.3% | ⚠️ OP |
| 4 | Exchange | 66.7% | ⚠️ OP |
| 5 | Emergent | 64.4% | ⚠️ OP |
| 6 | Ossuarium | 51.1% | ✅ BALANCED |
| 7 | Wyrd | 42.2% | ⚠️ UP |
| 8 | Elves | 28.9% | ⚠️ UP |
| 9 | Church | 13.3% | ⚠️ UP |
| 10 | Dwarves | 4.4% | ❌ CRITICAL |

### Army Power Results (Power Metric)

| Rank | Faction | Power | Relative % |
|------|---------|-------|------------|
| 1 | Ossuarium | 109.1 | 100.0% |
| 2 | Emergent | 106.4 | 97.5% |
| 3 | Elves | 105.3 | 96.4% |
| 4 | Church | 101.0 | 92.5% |
| 5 | Nomads | 97.0 | 88.9% |
| 6 | Crucible | 96.6 | 88.5% |
| 7 | Exchange | 87.9% | 87.9% |
| 8 | Bloodlines | 95.2 | 87.2% |
| 9 | Wyrd | 94.3 | 86.4% |
| 10 | Dwarves | 74.5 | 68.2% |

---

## Major Divergences

### 1. **Ossuarium: 6th → 1st (+48.9%)**

**Single-Unit:** 51.1% WR (balanced)
**Army Power:** 100.0% (strongest)

**Why the difference?**
- Ossuarium likely has high HP cards in faction cards
- Power metric heavily weights HP (no damage multipliers applied)
- Single-unit combat applies DICE results and defense rolls
- Power metric = raw stats without combat modifiers

**Conclusion:** Ossuarium is tanky (high HP) but not necessarily strong in actual combat.

---

### 2. **Elves: 8th → 3rd (+67.5%)**

**Single-Unit:** 28.9% WR (underpowered)
**Army Power:** 96.4% (3rd strongest)

**Why the difference?**
- Elves have good base stats (HP + SP)
- Single-unit combat: Bleed synergy disrupted by faction cards
- Power metric: Doesn't account for strategy, just raw stats

**Conclusion:** Elves have good stats but poor combat effectiveness (Bleed needs buffs).

---

### 3. **Church: 9th → 4th (+79.2%)**

**Single-Unit:** 13.3% WR (underpowered)
**Army Power:** 92.5% (4th strongest)

**Why the difference?**
- Church has self-harm gambits that reduce HP in combat
- Power metric: Measures starting stats (before self-harm)
- Single-unit combat: Self-harm reduces survivability

**Conclusion:** Church has good base stats but self-harm mechanics kill them in combat.

---

### 4. **Crucible: 1st → 6th (-8.5%)**

**Single-Unit:** 80.0% WR (overpowered)
**Army Power:** 88.5% (6th)

**Why the difference?**
- Crucible has Forge tokens that multiply damage in combat
- Power metric: Doesn't account for Forge scaling
- Single-unit combat: Forge tokens make attacks much stronger

**Conclusion:** Crucible is stat-average but combat-dominant (Forge is strong).

---

### 5. **Dwarves: 10th → 10th (No Change)**

**Single-Unit:** 4.4% WR (worst)
**Army Power:** 68.2% (worst)

**Why both metrics agree?**
- Dwarves have low base stats AND non-functional combat cards
- Crafting faction cards don't work in simulator
- Power metric + combat both show weakness

**Conclusion:** Dwarves need card replacement (crafting → combat-viable).

---

## Sample Army Compositions

### Church (4 points)
```
Army 1: WARDEN (3 pts, 43 HP, 1 unit)
Army 2: WARDEN + 1 Support (4 pts, 42 HP, 2 units)
```

**Analysis:**
- Prefers Warden (balanced unit)
- Sometimes adds Support (1 pt filler)
- Total: 40-45 HP average

---

### Dwarves (4 points)
```
Army 1: SCOUT + SCOUT (4 pts, 68 HP, 2 units)
Army 2: WARDEN (3 pts, 31 HP, 1 unit)
```

**Analysis:**
- Higher HP than Church (68 vs 43)
- But loses in combat (crafting cards don't work)
- Power metric shows stats, not effectiveness

---

### Elves (4 points)
```
Army 1: VANGUARD (4 pts, 34 HP, 1 unit)
Army 2: WARDEN + 1 Support (4 pts, 36 HP, 2 units)
```

**Analysis:**
- Prefers tanky units (Vanguard)
- Low HP but good SP
- Bleed synergy not reflected in power metric

---

## Key Insights

### 1. **Power Metric ≠ Combat Effectiveness**

**Power metric measures:**
- Base HP (deck size)
- Base SP (action economy)
- Unit count (activation count)

**Power metric IGNORES:**
- Damage output
- Combat mechanics (Forge, Bleed, Credits)
- Self-harm costs (Church gambits)
- Token economies
- Dice variance
- Defense rolls

**Lesson:** Raw stats don't predict combat performance.

---

### 2. **Faction Card Quality Matters More Than Stats**

**High Stats, Low Combat:**
- Ossuarium: 109.1 power, 51.1% WR
- Elves: 105.3 power, 28.9% WR
- Church: 101.0 power, 13.3% WR

**Low Stats, High Combat:**
- Crucible: 96.6 power, 80.0% WR
- Bloodlines: 95.2 power, 73.3% WR
- Exchange: 96.0 power, 66.7% WR

**Lesson:** Card synergy > base stats.

---

### 3. **Dwarves Are Broken Regardless of Metric**

- Power metric: 74.5 (worst)
- Combat WR: 4.4% (worst)
- Both metrics agree: Dwarves need fixes

**Next Step:** Replace crafting cards with combat-viable alternatives.

---

### 4. **Army Composition Variety Works**

**Observed at Easy (4 points):**
- 2 Scouts (common)
- 1 Warden + 1 Support (common)
- 1 Vanguard (less common)
- No Colossus (too expensive) ✅

**Conclusion:** Point-based army builder creates variety as intended.

---

## Limitations

### This Test is SIMPLIFIED

**What it measures:**
- Base army stats (HP, SP, unit count)
- Faction card pool impact on stats

**What it DOESN'T measure:**
- Actual combat (no attacks, no damage)
- Focus fire AI (which enemy to target)
- Support unit abilities (healing, buffs)
- Multi-unit interactions
- Strategic depth

**Status:** Proof of concept only, not full simulation.

---

## Next Steps

### Option 1: Implement Simple Multi-Unit Combat
**Focus fire** all attacks on strongest enemy until dead.

**Pros:**
- Gives realistic combat results
- Tests army compositions in actual battles
- ~100 lines of code

**Cons:**
- No support abilities
- No positioning
- Simplified targeting

---

### Option 2: Focus on Single-Unit Balance First
Fix critical issues before adding multi-unit complexity:
1. Dwarves (4.4% WR) - Replace crafting cards
2. Church (13.3% WR) - Reduce self-harm costs
3. Elves (28.9% WR) - Buff Bleed damage

**Pros:**
- Addresses critical balance issues
- Simpler than multi-unit combat
- Uses existing tested simulator

**Cons:**
- Doesn't test army compositions in combat
- Delays multi-unit feature

---

## Recommendations

### Immediate
1. **Use single-unit combat results** (v5.14) for balance decisions
2. **Ignore power rankings** (not representative of combat)
3. **Fix Dwarves ASAP** (4.4% WR is unplayable)

### Short-Term
1. Implement simple multi-unit combat (focus fire)
2. Test army compositions at Easy/Medium/Hard
3. Compare multi-unit vs single-unit balance

### Long-Term
1. Full multi-unit combat with support abilities
2. AI behavior trees for support units
3. Hex grid positioning and flanking

---

## Conclusion

The point-based army builder **works as intended**:
✅ Creates varied army compositions
✅ Colossus doesn't appear at Easy difficulty
✅ Support units integrate at 1 point each
✅ Random compositions within budget

However, the power metric **doesn't predict combat effectiveness**:
- Ossuarium ranks #1 in power, #6 in combat WR
- Elves rank #3 in power, #8 in combat WR
- Crucible ranks #6 in power, #1 in combat WR

**Recommendation:** Implement simple multi-unit combat to get realistic army balance data, or continue with single-unit balance fixes (Dwarves, Church, Elves).

---

**Document Version:** 1.0
**Author:** Claude (AI Assistant)
**Test Type:** Simplified Power Comparison
**Status:** Army builder works, needs combat simulation for accurate balance
