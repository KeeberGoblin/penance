# Mutation Strain Mechanic - Balance Update v5.30

**Date**: 2025-10-21
**Version**: v5.30
**Issue**: Vestige Bloodlines infinite scaling from Biomass spending
**Solution**: Mutation Strain cap with transformation loss condition

---

## Problem Identified

**Previous balance (v5.29):**
- Vestige Bloodlines: **60.0% win rate** (tied for #1 most overpowered)
- Adaptive Evolution allowed **infinite damage stacking** with no drawbacks
- Biomass spending had no meaningful limitations
- Players could spam Bloodline Shift and Adaptive Evolution endlessly

**Root cause:**
- No penalty for excessive Biomass spending
- Infinite scaling potential broke balance
- Thematically inconsistent (they're supposed to be struggling, not dominating)

---

## Solution: Mutation Strain Mechanic

### Core Concept

**"The Casket suppresses mutations, but it has limits."**

Every time you spend Biomass, you force a controlled mutation. The Casket's neural threads can only suppress so much. Push too hard, and the suppression fails - you transform into an Abomination and lose.

### Tracking

**Mutation Strain Track:**
- Starts at 0 each mission
- Increases every time you spend Biomass
- **Never resets** during the mission
- Hard cap at 30 (transformation = instant loss)

### Thresholds

| Strain Level | Status | Effect |
|--------------|--------|--------|
| **0-9** | Stable | Normal operation, no penalties |
| **10-19** | Unstable | All attacks generate +1 Heat |
| **20-29** | Feral | Must attack each turn if able, cannot use Reactive defense cards |
| **30+** | Transformation | **Mission ends immediately, you lose** |

### Biomass Costs & Strain

| Card | Biomass Cost | Strain Added |
|------|--------------|--------------|
| Bloodline Shift | 2 | +2 |
| Adaptive Evolution | 1 | +1 |
| Regenerative Flesh | 1 | +1 |
| Reactive Scales (Biomass) | 1 | +1 |
| Carapace Molt (Vexis) | 2 | +2 |
| Hibernation Trance (Urtok) | 4 | +4 |
| Ancestral Memory | 3 | +3 |

---

## Balance Impact

### Simulation Results

**Before (v5.29):**
```
Vestige Bloodlines: 27-18 (60.0% WR) - OVERPOWERED
```

**After (v5.30):**
```
Vestige Bloodlines: 26-19 (57.8% WR) - Needs slight adjustment
```

**Change:** -2.2% win rate reduction

### Analysis

**Positive outcomes:**
- No longer tied for #1 most overpowered faction
- Still competitive (57.8% is high but not broken)
- Infinite scaling eliminated (hard cap at 29 Strain)
- Thematically consistent (fighting to stay human)

**Still needs work:**
- 57.8% is still above ideal 50-55% range
- May need further tuning (possibly reduce Biomass generation)

---

## Gameplay Impact

### Strategic Decisions

**Players now must budget Mutation Strain carefully:**

1. **Conservative play (0-9 Strain):**
   - 4-5 Biomass spends maximum
   - Example: 2x Bloodline Shift (4 Strain) + 3x Regenerative Flesh (3 Strain) = 7 Strain
   - Safe, no penalties

2. **Aggressive play (10-19 Strain):**
   - 10-15 Biomass spends
   - Example: 5x Bloodline Shift (10 Strain) + 5x Adaptive Evolution (5 Strain) = 15 Strain
   - Unstable status (+1 Heat per attack)
   - Manageable if Heat purge available

3. **Desperate play (20-29 Strain):**
   - 20-25 Biomass spends
   - Example: Hibernation (4) + 5x Shift (10) + 10x Evolution (10) = 24 Strain
   - Feral status (must attack, no Reactive defenses)
   - **Win NOW or lose**

4. **Suicide (30+ Strain):**
   - Instant loss, mission ends
   - **NEVER DO THIS**

### Typical Mission Budget

**Most missions should aim for 10-15 total Strain:**
- Allows moderate Biomass spending
- Unstable penalty is manageable
- Leaves safety margin before Feral threshold

**Emergency scenarios might push to 20-25 Strain:**
- Final desperate push to win
- Feral status makes you ultra-aggressive
- Cannot defend, must win through pure offense

---

## Thematic Integration

### Perfect Alignment with New Lore

**From the Casket Dependency revision:**
> "Caskets don't just help them fight. Caskets keep them human. But the neural threads can only suppress so much."

**The Mutation Strain mechanic embodies this:**
- Every Biomass spend = forcing a controlled mutation
- The Casket struggles to suppress it
- Push too hard = suppression fails completely
- Transformation at 30+ Strain = the beast wins, you lose

### Narrative Tension

**Before:** "I'm unstoppable, infinite power!"
**After:** "How much can I risk? One more Bloodline Shift might push me over..."

Creates constant tension between:
- **Power** (Biomass abilities are strong)
- **Control** (but using them risks transformation)
- **Desperation** (late-mission choices: win now or lose to Feral status)

---

## Implementation Details

### Card Updates

**All Biomass-spending cards now include:**
- Mutation Strain cost in effect text
- Warning about transformation risk
- Updated lore reflecting the danger

**Example (Adaptive Evolution):**
```
Effect: Gain 1 mutation counter (+1 damage permanently).
Add +1 to Mutation Strain track.
Warning: Spending too much Biomass risks losing control.

Lore: "What doesn't kill us makes us deadlier. But also... less human."
```

### Tactical Guidelines Section

**New "Biomass Economy & Mutation Strain Management" section:**
- Detailed Strain budgeting advice
- Example builds with Strain calculations
- Threshold management strategies
- Warning about 30+ transformation

### Simulation Implementation

**Added to equipment_simulator_dice.py:**
- `mutation_strain` attribute to CasketPilot class
- Strain tracking on Biomass spends
- Transformation check (30+ = instant loss via deck depletion)
- Unstable heat penalty (+1 Heat at 10+ Strain)
- Feral status logging (20+ Strain, though AI doesn't enforce "must attack" yet)

---

## Files Modified

1. **docs/factions/vestige-bloodlines/deck-equipment-system.md**
   - Added "MUTATION STRAIN MECHANIC" section (full mechanic explanation)
   - Updated all Biomass-spending cards with Strain costs
   - Updated "Biomass Economy" tactical guidelines
   - Updated Balance Considerations in Design Notes

2. **simulation/equipment_simulator_dice.py**
   - Added `mutation_strain: int = 0` to CasketPilot
   - Updated Biomass spending logic with Strain tracking
   - Added transformation check (30+ = instant loss)
   - Added Unstable heat penalty implementation

3. **docs/factions/vestige-bloodlines/MUTATION-STRAIN-BALANCE-UPDATE.md** (this file)
   - Complete documentation of the new mechanic

---

## Future Considerations

### Potential Further Nerfs

If 57.8% WR is still too high:

**Option 1: Reduce Biomass generation**
- Change Vestige Heritage from 2 Biomass per kill to 1
- Currently: Kill = 2 Biomass (+1 if prey type matches)
- Proposed: Kill = 1 Biomass (+1 if prey type matches)

**Option 2: Increase Strain costs**
- Bloodline Shift: 2 Biomass, +3 Strain (was +2)
- Adaptive Evolution: 1 Biomass, +2 Strain (was +1)
- Would reduce total spends per mission by ~30%

**Option 3: Lower transformation threshold**
- Change cap from 30 to 25 Strain
- More punishing, forces even tighter budgeting

### Campaign Mode Implications

**Current mechanic is per-mission:**
- Strain resets between missions
- No cumulative penalty across campaign

**Potential campaign variant:**
- Strain carries over between missions
- Requires "rest and recovery" downtime to reduce Strain
- Creates long-term resource pressure
- Thematically fits with "generational degradation" lore

---

## Summary

**Mutation Strain successfully:**
✅ Eliminates infinite scaling (hard cap at 29 Strain)
✅ Reduces Vestige win rate (60.0% → 57.8%)
✅ Creates meaningful strategic decisions (risk vs reward)
✅ Aligns perfectly with new lore (Casket suppression limits)
✅ Maintains faction identity (strong but tragic)

**Still needs:**
⚠️ Minor further tuning (57.8% still above ideal 50-55%)
⚠️ Possible Biomass generation reduction
⚠️ Testing in actual gameplay (simulation can't capture all nuances)

**Overall:** A successful balance update that fixes the infinite scaling problem while enhancing thematic resonance. Vestige Bloodlines are now mechanically powerful but narratively tragic - exactly as intended.
