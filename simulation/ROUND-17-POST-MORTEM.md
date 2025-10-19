# Round 17 - Post-Mortem Analysis
## "The Great Overbuff Disaster"

**Date:** October 19, 2025
**Result:** Catastrophic failure - went from 4 balanced factions → 1 balanced faction

---

## WHAT WENT WRONG

### The Mistake: Simultaneous Multi-Faction Buffs

**Round 17 Changes (ALL applied at once):**
1. **Church:** Blood Offering +1 → +2 (BUFFED)
2. **Dwarves:** Base damage 4 → 5 (BUFFED)
3. **Ossuarium:** Soul Harvest FREE 4 dmg → 1 SP 5 dmg (BUFFED)
4. **Bloodlines:** Biomass 7/9/11 → 8/10/12 (BUFFED)
5. **Exchange:** Mercenary 6 → 5 damage (NERFED)
6. **Wyrd:** Reality Distortion 5 → 4 damage (NERFED)

**Result:** 4 bottom-tier factions all became overpowered simultaneously, crushing the balanced meta.

---

## ROUND 16 VS ROUND 17 COMPARISON

| Faction | R16 WR% | R17 WR% | Change | Result |
|---------|---------|---------|--------|--------|
| **Bloodlines** | 40.8% | 73.6% | +32.8% | CATASTROPHIC OVERBUFF |
| **Ossuarium** | 39.2% | 71.9% | +32.7% | CATASTROPHIC OVERBUFF |
| **Church** | 44.7% | 66.7% | +22.0% | Massive overbuff |
| **Dwarves** | 38.9% | 65.3% | +26.4% | Massive overbuff |
| Emergent | 50.0% | 51.1% | +1.1% | PERFECT (unchanged) |
| **Nomads** | 47.5% | 39.4% | -8.1% | CRUSHED by buffed factions |
| **Elves** | 45.3% | 41.9% | -3.4% | CRUSHED by buffed factions |
| **Crucible** | 45.3% | 34.7% | -10.6% | CRUSHED by buffed factions |
| **Exchange** | 61.1% | 27.5% | -33.6% | CATASTROPHIC OVER-NERF |
| **Wyrd** | 61.4% | 13.6% | -47.8% | CATASTROPHIC OVER-NERF |

---

## KEY INSIGHTS

### 1. Bloodlines 8/10/12 = ALWAYS Catastrophic

**History:**
- **Round 10:** 8/10/12 = 82.8% WR (CATASTROPHIC)
- **Round 15:** 8/10/12 = 81.9% WR (CATASTROPHIC)
- **Round 17:** 8/10/12 = 73.6% WR (CATASTROPHIC)

**Conclusion:** 8/10/12 damage is fundamentally broken. Max safe damage = 7/9/11.

---

### 2. Ossuarium 5 Damage Too Strong

**History:**
- **Round 16:** FREE 4 damage = 39.2% WR (too weak)
- **Round 17:** 1 SP 5 damage = 71.9% WR (CATASTROPHIC)

**Issue:** 25% damage increase (4 → 5) was too aggressive. Should have tried 1 SP 4 damage first.

---

### 3. Dwarves 5 Damage + Rune Cap 2 = Too Strong

**History:**
- **Round 13:** 5 damage + rune cap 3 = 73.1% WR (CATASTROPHIC, double buff)
- **Round 14-16:** 4 damage + rune cap 2 = 38-41% WR (too weak)
- **Round 17:** 5 damage + rune cap 2 = 65.3% WR (too strong)

**Lesson:** Even single buff (5 damage) is too strong. Need 4 damage + something else.

---

### 4. Church Blood Offering +2 = Too Strong

**History:**
- **Round 11-12:** +2 bonus = 69.7% → 48.6% WR (over-nerfed to +1)
- **Round 16:** +1 bonus = 44.7% WR (too weak)
- **Round 17:** +2 bonus = 66.7% WR (too strong again!)

**Pattern:** +2 consistently produces 65-70% WR. Need intermediate value (maybe +1.5 equivalent?).

---

### 5. Simultaneous Buffs Create Arms Race

**The Cascade Effect:**
1. Buffed 4 bottom-tier factions (Church/Dwarves/Ossuarium/Bloodlines)
2. All 4 became overpowered (65-74% WR range)
3. Previously balanced factions (Nomads/Elves/Crucible) got crushed
4. Entire meta collapsed into 4 god-tier factions vs 6 crushed factions

**Lesson:** ONLY buff ONE faction per round. Observe ripple effects before continuing.

---

## THE CORRECT APPROACH (Should Have Done)

**Round 17 Should Have Been:**
1. Start from Round 16 state (4 balanced factions: Emergent/Nomads/Elves/Crucible)
2. Address ONLY Exchange (61.1% → nerf Mercenary 6 → 5)
3. Run test
4. **Round 18:** Address ONLY Wyrd (61.4% → nerf Reality Distortion)
5. **Round 19:** Address ONLY Church (44.7% → micro-buff)
6. **Round 20:** Address ONLY Bloodlines (40.8% → micro-buff)
7. Etc.

**Result:** Incremental convergence instead of catastrophic collapse.

---

## ROLLBACK PLAN

**Round 18 Strategy:** Revert ALL Round 17 changes, return to Round 16 state.

**Round 16 State (4 balanced factions):**
- Church: Blood Offering +1, 44.7% WR
- Dwarves: 4 damage, rune cap 2, 38.9% WR
- Ossuarium: FREE 4 damage Soul Harvest, 39.2% WR
- Bloodlines: 7/9/11 Biomass, 40.8% WR
- Exchange: 6 damage Mercenary, 61.1% WR
- Wyrd: 5 damage Reality Distortion, 61.4% WR
- **Emergent: 50.0% WR ✅**
- **Nomads: 47.5% WR ✅**
- **Elves: 45.3% WR ✅**
- **Crucible: 45.3% WR ✅**

---

## LESSONS LEARNED

1. **NEVER buff multiple factions simultaneously** - causes arms race
2. **Bloodlines 8/10/12 is fundamentally broken** - always results in 70-80% WR
3. **Small incremental changes work better** - large swings cause catastrophic imbalance
4. **Test ONE change at a time** - isolate cause and effect
5. **Revert catastrophic changes immediately** - don't try to "fix forward"

---

## ROUND 18 PLAN

1. Revert ALL Round 17 changes
2. Return to Round 16 state (4 balanced factions)
3. Make ONLY ONE change: Exchange Mercenary 6 → 5 damage
4. Test and observe ripple effects
5. If successful, Round 19 addresses Wyrd ONLY

---

## STATISTICS

**Total Battles:** 30,600 (17 rounds × 1,800 battles)
**Best Result:** Round 16 (4/10 balanced: Emergent, Nomads, Elves, Crucible)
**Worst Result:** Round 17 (1/10 balanced: Emergent only)

---

## STATUS

**Next Action:** Implement Round 18 rollback to Round 16 state, then single Exchange nerf
