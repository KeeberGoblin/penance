# Codex Outdated Information Report

**Date:** October 21, 2025
**Status:** CRITICAL - Major outdated information found
**Scope:** Balance files, equipment files, faction files

---

## Executive Summary

The codex contains **heavily outdated balance and mechanics information** from the old SP (Soulstone Points) system and equipment-only testing era (v5.1-v5.19). Current production is **v5.29-FINAL** which uses completely different mechanics.

**Recommendation:** Archive or delete outdated balance files, create new ones based on v5.29-FINAL data from `/docs/BALANCE-FINAL-V5.29.md`

---

## Outdated Files Found

### Category 1: Balance Files (COMPLETELY OUTDATED)

**1. `balance-simulation-results.html`**
- **Status:** ❌ OBSOLETE
- **Issues:**
  - References "Round 16/17" data (equipment-only era)
  - References SP costs (removed in v5.14+)
  - References lifesteal mechanics (removed v5.23)
  - Claims "30,600 battles" but uses wrong system
  - Win rate data from wrong simulator version
- **Last Valid Data:** October 19, 2025 (pre-v5.20)
- **Replacement Needed:** Yes - use v5.29-FINAL data

**Example Outdated Content:**
```
Soul Harvest SP Cost:
- 0 SP: 81.1% WR (BROKEN)
- 1 SP: 71.9% WR (TOO STRONG)
- 3 SP: 50-55% WR (BALANCED)
```
**Reality:** Soul Harvest doesn't exist anymore, lifesteal removed v5.23

**2. `balance-proposal-2025-10-19.html`**
- **Status:** ❌ OBSOLETE
- **Issues:**
  - Proposes changes to mechanics that don't exist
  - References "Extinction Clock" for Bloodlines (not in current system)
  - References "Photosynthesis" for Elves (not in current implementation)
  - Uses SP costs throughout
- **Last Valid Data:** October 19, 2025 (pre-v5.20)
- **Replacement Needed:** Yes or DELETE

**Example Outdated Content:**
```
Ossuarium:
- Phylactery resurrection: 5 HP → 3 HP
- Soul Harvest lifesteal: 100% → 50%
```
**Reality:** Lifesteal removed entirely in v5.23, Taint system implemented

**3. `balance-analysis.html`**
- **Status:** ❌ OBSOLETE (based on filename pattern)
- **Issues:** Likely contains Round 1-17 data
- **Replacement Needed:** Yes or DELETE

**4. `balance-comparison.html`**
- **Status:** ❌ OBSOLETE (based on filename pattern)
- **Issues:** Likely compares outdated rounds
- **Replacement Needed:** Yes or DELETE

---

### Category 2: Equipment Files (PARTIALLY OUTDATED)

**1. `equipment-decks.html`**
- **Status:** ⚠️ PARTIALLY OUTDATED
- **Issues:**
  - Uses SP costs for all attacks (e.g., "Stab: 1 SP, Deal 3 damage")
  - Casket classes listed with SP pools (Scout 6 SP, Assault 5 SP, etc.)
  - Equipment slots system outdated
- **Reality:**
  - v5.29 uses Heat costs, not SP
  - Deck composition: 6 Faction + 10 Universal + Equipment cards
  - No SP pools in current system
- **Replacement Needed:** Major revision needed

**Example Outdated Content:**
```
Scout: 6 SP
Assault: 5 SP
Heavy: 4 SP
Fortress: 3 SP
```
**Reality:** Casket classes exist but don't have SP pools in v5.29

**2. `support-equipment.html`**
- **Status:** ⚠️ LIKELY OUTDATED
- **Issues:** Probably uses SP costs
- **Replacement Needed:** Review and update

---

### Category 3: Faction Files (MECHANICS OUTDATED)

**Files with outdated mechanics:**
- `faction-exchange.html` - References SP costs
- Potentially others (need to check each one)

**Common Issues:**
1. **SP Costs:** All faction abilities listed with SP costs
2. **Lifesteal:** Ossuarium likely has outdated lifesteal mechanics
3. **Resource Economies:** May not reflect v5.29 implementations
   - Church: Faith system + 5x discard bonuses
   - Dwarves: Rune counters (4 damage block per counter)
   - Ossuarium: Taint system (no lifesteal)
   - Bloodlines: Biomass (1 per kill)

---

### Category 4: Rules Files (CHECK STATUS)

**Files to verify:**
- `rules-soulstone-energy.html` - May reference SP system
- `rules-combat.html` - May have outdated combat mechanics
- `rules-dice.html` - May have wrong base_target (should be 5, not 4)

---

## Current Reality (v5.29-FINAL)

### Correct Mechanics

**Dice System:**
- Attack: 2d6 custom dice [1,2,3,4,5,0/JAM]
- base_target = 5 (58% hit rate, NOT 4)
- Defense: 1d6 per damage (33% block rate)

**Resource Economies (NOT SP):**
| Faction | Resource | How It Works |
|---------|----------|--------------|
| Exchange | Credits | +1-2 per card played |
| Bloodlines | Biomass | +1 per kill |
| Church | Faith | +1 per gambit, cap 5 |
| Crucible | Forge | +1 per attack, cap 5 |
| Elves | Bleed | +1-2 per attack, cap 4 |
| Dwarves | Rune Counters | +1 per attack, blocks 4 dmg ea |
| Ossuarium | Taint | +1 per 3 dmg dealt, penalties |

**Equipment Costs:**
- Heat costs (0-2 Heat per attack)
- NO SP costs anymore

**Deck Composition:**
- 6 Faction cards (from 21 available)
- 10 Universal cards (all included)
- ~13-19 Equipment cards (2 items chosen)
- Total: ~29-35 cards per deck

**Major Mechanic Changes:**
- Lifesteal: REMOVED (v5.23)
- Church: 5x discard bonuses (v5.27)
- Dwarves: Rune counters block 4 damage (v5.25)
- Ossuarium: Taint system only, no lifesteal

### Correct Balance (v5.29-FINAL)

**Balanced Factions (45-55%):**
- Vestige-bloodlines: 53.3%
- Wyrd-conclave: 51.1%
- Ossuarium: 48.9%
- Church: 46.7%

**Close to Balanced (44-58%):**
- Nomads: 57.8%
- Exchange: 55.6%
- Dwarves: 44.4%

**Outliers:**
- Elves: 62.2% (high)
- Crucible: 42.2% (low)
- Emergent: 37.8% (low)

**Overall:** 7/10 factions in acceptable range
**WR Spread:** 24.4pp (37.8%-62.2%)

---

## Recommendations

### Option A: Archive Outdated Files (RECOMMENDED)

**Create archive folder:**
```
docs/codex/archive-pre-v529/
```

**Move these files:**
- `balance-simulation-results.html`
- `balance-proposal-2025-10-19.html`
- `balance-analysis.html`
- `balance-comparison.html`

**Create NEW file:**
- `balance-v529-final.html` - Based on `/docs/BALANCE-FINAL-V5.29.md`

### Option B: Delete Outdated Files

**Delete entirely:**
- All 4 balance files (completely obsolete)

**Update in place:**
- `equipment-decks.html` - Replace SP with Heat costs
- Faction files - Update mechanics to v5.29

### Option C: Create Disclaimer

**Add to top of outdated files:**
```html
<div style="background: #ff6b6b; padding: 1rem; margin-bottom: 2rem; border: 3px solid #d32f2f;">
    <strong>⚠️ OUTDATED INFORMATION</strong><br>
    This file contains data from the pre-v5.20 SP system and equipment-only testing.<br>
    For current balance data, see: <a href="balance-v529-final.html">v5.29-FINAL Balance Report</a>
</div>
```

---

## Priority Actions

### Immediate (Critical Misinformation)

1. **Archive or delete** `balance-simulation-results.html` (completely wrong)
2. **Archive or delete** `balance-proposal-2025-10-19.html` (proposes changes to nonexistent mechanics)
3. **Create NEW** `balance-v529-final.html` based on `/docs/BALANCE-FINAL-V5.29.md`

### High Priority

4. **Update** `equipment-decks.html`:
   - Replace all SP costs with Heat costs
   - Update deck composition formula
   - Remove SP pool references

5. **Verify** `rules-dice.html`:
   - Check if base_target is documented as 5 (correct)
   - Not 4 (bug fixed in v5.26)

### Medium Priority

6. **Review all faction files** for:
   - SP cost references → Update to resource economies
   - Lifesteal references → Remove/update
   - Outdated mechanics → Update to v5.29

---

## Implementation Plan

If proceeding with Option A (Recommended):

1. Create `docs/codex/archive-pre-v529/`
2. Move 4 balance files to archive
3. Create new `balance-v529-final.html` based on BALANCE-FINAL-V5.29.md
4. Update `equipment-decks.html` to remove SP references
5. Audit all faction files (10 files) for mechanics updates
6. Update `content-home.html` links

**Estimated Time:** 2-3 hours for comprehensive update

---

## Data Source for Updates

**Primary Source:** `/docs/BALANCE-FINAL-V5.29.md`
- Complete balance history
- Correct mechanics (v5.29-FINAL)
- Accurate win rates (7/10 in acceptable range)
- Meta ecology insights

**Secondary Source:** `/simulation/equipment_simulator_dice.py`
- Actual implementation of all mechanics
- Correct resource economies
- Heat costs, not SP costs

**Card Database:** `/docs/cards/complete-card-data.json`
- v5.29-FINAL equipment damage values
- Correct card counts and effects

---

## Conclusion

The codex contains **critical misinformation** from the old SP-based system (pre-v5.20) and equipment-only testing era. Users referencing these files will get completely wrong information about:
- Balance (outdated win rates)
- Mechanics (SP costs don't exist, lifesteal removed)
- Faction abilities (wrong resource systems)

**RECOMMENDED ACTION:** Archive all 4 balance files, create new balance file from v5.29-FINAL data, update equipment files to remove SP references.

---

**Status:** Awaiting user decision
**Last Updated:** October 21, 2025
