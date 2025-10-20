# Complete Damage System Implementation Needed

**Date**: 2025-10-20
**Status**: Dice mechanics implemented, full damage system pending

---

## What We Have Now

**Current Dice Simulator** includes:
- ✅ Attack dice (2d6 with JAM face, values 0-5)
- ✅ Defense dice (1d6 per damage, 33% block chance)
- ✅ Hit results (Miss, Hit, Strong Hit, Critical, Execution, Catastrophic Failure)
- ✅ Casket HP deck (card-based HP)
- ✅ Heat tracking (basic)
- ✅ Component damage tracking (accumulation only)

**Current Dice Simulator is MISSING**:
- ❌ DAMAGED cards (Major Wounds at 5+ damage)
- ❌ Damage Die rolls (1d6 when DAMAGED removed)
- ❌ Component AP/Structure/Pilot Exposure zones
- ❌ Pilot Wound deck (separate 10-card deck)
- ❌ Strain rolls (Heat 5+ Danger Zone)
- ❌ 3-pile system (Draw/Discard/Damage Graveyard distinction)
- ❌ Cascading failures (DAMAGED cards discarded by damage)
- ❌ Component destruction effects (SCRAP cards)

---

## Why This Matters for Balance

### 1. DAMAGED Cards Create Death Spirals

**Mechanic**: When you take 5+ damage in one hit → Add 1 DAMAGED card to Discard Pile

**What This Does**:
- DAMAGED cards persist in hand (dead draws)
- Removing DAMAGED requires 0 SP action + Damage Die roll
- Damage Die results: Strain, SP loss, more wounds, Heat, etc.
- **Multiple DAMAGED cards = hand pressure = can't play good cards**

**Balance Impact**:
- **Burst damage factions (Church, Dwarves) become STRONGER**
  - 8 damage Divine Judgment = instant DAMAGED card
  - Opponent's hand clogged with wounds
  - Cascading advantage (wounded enemy easier to wound again)

- **Chip damage factions (Elves Bleed) become WEAKER**
  - 3 damage Piercing Arrow × 2 = 6 total damage = 2 separate hits
  - **NO DAMAGED cards** (neither hit ≥5 damage)
  - Opponent takes same total damage but no wound pressure

**Expected Balance Shift**:
- Church 100% → **105%+** (if that were possible - total dominance)
- Elves 0% → **-5%** (even worse than current catastrophe)

### 2. Component Zones Change Damage Scaling

**Mechanic**: Each body part has 3 zones (AP/Structure/Pilot Exposure)

**Zone Effects**:
- **AP Zone**: No penalties, pilot safe
- **Structure Zone**: Functional penalties (-1 to -2 damage, +1 SP costs)
- **Pilot Exposure Zone**: **Every damage = +1 Pilot Wound** (CRITICAL)

**Example** (Right Arm, 8 HP total):
- 0-3 HP damage: AP zone (safe)
- 4-5 HP damage: Structure zone (-1 damage penalty)
- 6-8 HP damage: Pilot Exposure (**every hit wounds pilot!**)

**Balance Impact**:
- **Focus fire is MANDATORY**
  - Spreading damage across limbs = all stay in AP zone = no penalties
  - Focusing one limb = reach Pilot Exposure = start wounding pilot
  - **Optimal play**: Always attack same component

- **"Cannot miss" cards become GOD-TIER AGAIN**
  - Church Righteous Wrath can consistently target same limb
  - Elves bleed requires hitting (already collapsed at 0% WR)
  - Wyrd Reality Fracture becomes even stronger (waste enemy focus fire)

**Expected Balance Shift**:
- Church 100% → **Literally unbeatable** (focus fire + cannot miss)
- Tactical depth added (component targeting matters)

### 3. Pilot Wound Deck Adds Lethality

**Mechanic**: Separate 10-card Wound deck

**Pilot Takes Wounds When**:
- Component in Pilot Exposure zone takes damage (+1 Wound per damage)
- Chassis destroyed (+3 Wounds + ejection save)
- Head destroyed (+1 Wound)
- Total Component Damage ≥ 15 (+1 Wound)
- Casket HP deck empty (save or +2 Wounds)

**Wound Card Effects**:
- Minor Injury (5 cards): -1 SP, -2 damage, +1 Heat per Heat gain, etc.
- Severe Injury (3 cards): PERMANENT -2 SP max, PERMANENT +1 SP per hex, etc.
- Trauma (2 cards): Cannot attack from behind, 33% chance to lose 1 SP/turn

**Balance Impact**:
- **Two win conditions now**:
  1. Destroy Casket (deplete HP deck)
  2. Kill Pilot (10 Wounds)

- **Focus fire gets EVEN STRONGER**:
  - Target one limb → Reach Pilot Exposure → Start wounding pilot
  - Pilot dies at 10 Wounds (might happen before Casket dies!)
  - **New strategy**: Wound pilot to death, ignore Casket HP

- **Ossuarium lifesteal becomes weaker**:
  - Lifesteal recovers Casket HP (cards from discard)
  - Does NOT heal Pilot Wounds
  - Can have 40 HP Casket but 8/10 Wounds = 2 hits from death

**Expected Balance Shift**:
- Focus-fire burst damage (Church/Dwarves) even stronger
- Attrition/lifesteal (Ossuarium) weaker than dice sim showed
- Wyrd might stay strong (Reality Fracture prevents wounds)

### 4. Strain System (Heat 5+) Adds Penalty Loops

**Mechanic**: At 5+ Heat, roll Strain at start of turn

**Strain Roll** (1d6 + Heat):
- 6-8: Lose 1 SP this turn
- 9-11: Take 2 damage
- 12+: Component malfunction (lose 1 random component)

**Balance Impact**:
- **Heat generation becomes DANGEROUS**
  - Defense dice showing HEAT () = build toward Strain
  - Taking damage in Pilot Exposure → Might get HEAT → Build to Strain
  - Strain roll → More damage → More HEAT → Death spiral

- **Venting Heat becomes MANDATORY**
  - Emergency Vent (2 SP): Remove 3 Heat
  - Pass turn (0 SP): Remove 1 Heat
  - **SP opportunity cost** = less attacks/movement

**Expected Balance Shift**:
- Factions with Heat generation (Crucible Forge burns) become weaker
- Factions with Heat removal (Church Heat-neutral) become stronger
- Long combats have more variance (Heat spirals can kill suddenly)

### 5. Cascading Failures (DAMAGED Discarded by Damage)

**Mechanic**: If you take damage while DAMAGED cards are in deck/hand:

**Scenario**:
1. You have 2 DAMAGED cards in your 20-card deck (from previous wounds)
2. Enemy hits you for 6 damage → Discard 6 cards
3. You choose to discard from deck (keep hand intact)
4. Draw cards from deck: 1 is DAMAGED → **Must roll Damage Die immediately**
5. Damage Die result: "Critical Malfunction" (+1 Pilot Wound)
6. **You just took +1 Pilot Wound from OLD wounds cascading!**

**Balance Impact**:
- **Wounded factions spiral FASTER**
  - First Major Wound → DAMAGED card → Eventually drawn
  - While DAMAGED in deck, taking more damage risks cascading failures
  - **Snowball effect**: Wounded → More wounds → Faster death

- **Healing/recovery becomes CRITICAL**
  - Purging DAMAGED cards (remove permanently) = huge value
  - Ossuarium lifesteal (recover cards) doesn't remove DAMAGED
  - Need ways to interact with DAMAGED cards specifically

**Expected Balance Shift**:
- Early damage becomes even more important (start snowball)
- Factions that can heal/purge DAMAGED (none exist yet) would be meta
- Church burst damage snowballs even harder

---

## Summary: What Complete Mechanics Would Show

**Current Dice Simulation Results**:
- Church: 100% WR (unbeatable with "cannot miss")
- Elves: 0% WR (bleed requires hitting)
- Wyrd: 66.7% WR (Reality Fracture OP)
- Ossuarium: 75.6% WR (lifesteal viable)

**Predicted Results With Complete Damage System**:
- **Church: 100%** (unchanged - already perfect, complete system makes them even more dominant)
- **Elves: 0%** (unchanged - can't apply bleed if can't hit, chip damage doesn't create DAMAGED cards)
- **Wyrd: 70-80%** (STRONGER - Reality Fracture prevents Pilot Wounds + focus fire)
- **Ossuarium: 60-70%** (WEAKER - lifesteal doesn't heal Pilot Wounds, focus fire kills pilots)
- **Dwarves: 85-90%** (STRONGER - high burst damage creates DAMAGED cards, focus fire viable)
- **Crucible: 15-20%** (WEAKER - Forge burns create Heat → Strain → Death spirals)

**Key Findings**:
1. **Burst damage dominates even more** (DAMAGED cards, Pilot Wounds, focus fire)
2. **Chip damage becomes unviable** (Elves bleed, Crucible Forge burns)
3. **Two win conditions favor focus fire** (Pilot Wounds before Casket dies)
4. **Church "cannot miss" is GAME-BREAKING** (guaranteed focus fire, guaranteed wounds)
5. **Wyrd Reality Fracture becomes S-tier** (prevents ALL wound cascades)

---

## Implementation Complexity

**Implementing complete damage system requires**:

### Code Changes (Estimated 500-800 lines):

1. **DAMAGED Card Class** (~50 lines)
   - Persist in hand mechanic
   - Sacrifice/Purge actions
   - Damage Die integration

2. **Damage Die System** (~80 lines)
   - 6 result types (Strain, Glitch, Bleeding, Weakness, Malfunction, Surge)
   - State tracking (next turn penalties)
   - Cascading failure triggers

3. **Component Damage Zones** (~150 lines)
   - 5 components × 3 zones each
   - Zone thresholds by Casket class (Scout/Warden/Vanguard/Colossus)
   - Functional penalties (Structure zone)
   - Pilot Wound triggers (Exposure zone)
   - Component destruction effects (SCRAP cards)

4. **Pilot Wound Deck** (~120 lines)
   - Separate 10-card deck
   - 3 card types (Minor/Severe/Trauma)
   - Effect application (permanent vs temporary)
   - Death condition (10 Wounds)

5. **Strain System** (~60 lines)
   - Heat tracking (0-4 Safe, 5+ Danger, 10+ Critical)
   - Strain roll (1d6 + Heat)
   - 4 result brackets
   - Component malfunction (random component loss)

6. **3-Pile System** (~100 lines)
   - HP Draw Deck (active)
   - Discard Pile (reshuffles)
   - Damage Graveyard (permanent loss)
   - Reshuffle logic (exclude Graveyard)
   - DAMAGED card insertion (on reshuffle vs on Major Wound)

7. **Cascading Failures** (~80 lines)
   - Detect DAMAGED cards in damage discard
   - Trigger Damage Die rolls
   - Chain reactions (malfunction → more damage → more DAMAGED)

8. **Major Wound Thresholds** (~40 lines)
   - Varies by Casket class (Scout 3+, Warden 5+, Vanguard 7+, Colossus 9+)
   - Add DAMAGED to Discard Pile (not Graveyard!)
   - Track total Major Wounds

9. **Statistics Tracking** (~80 lines)
   - DAMAGED cards created/removed
   - Pilot Wounds taken
   - Component damage by zone
   - Strain rolls and results
   - Cascading failure count

10. **Simulator Integration** (~60 lines)
    - Update execute_turn logic
    - Update damage resolution
    - Update defense dice handling
    - Update combat loop

**Total: ~820 lines of new/modified code**

**Testing Requirements**:
- Unit tests for each subsystem
- Integration tests for cascading failures
- Balance tests with complete rules
- Performance testing (complex state tracking)

**Time Estimate**: 8-12 hours of development

---

## Recommendation

**Given Current Findings**:

1. **Dice mechanics alone proved previous 675-battle analysis invalid**
2. **Church is already unbeatable (100% WR) with partial mechanics**
3. **Complete damage system would make Church even more dominant**
4. **Elves are catastrophically broken (0% WR) and complete system makes it worse**

**Next Steps** (Priority Order):

### IMMEDIATE (Before Adding Complete Mechanics):

1. **Fix Church "Cannot Miss"**:
   - Remove from Righteous Wrath
   - Change to "Advantage on attack roll" (3d6 take 2 highest)
   - Reduce Divine Judgment from 8 → 6 damage
   - **Test with dice sim**: Does this drop Church to ~60% WR?

2. **Fix Elf Bleed Application**:
   - Change from "On Hit" to "On Attack"
   - "Apply 1 Bleed, then if attack hits, deal X damage"
   - Reduce cap from 6 → 4 stacks (compensate for guaranteed application)
   - **Test with dice sim**: Does this bring Elves to ~40% WR?

3. **Fix Crucible Forge Generation**:
   - Change from "On Hit" to "On Attack"
   - "Gain 1 Forge, then deal X damage"
   - **Test with dice sim**: Does this bring Crucible to ~45% WR?

4. **Rerun 225-battle test with fixes**:
   - Target: 7-10 factions in 45-55% WR range
   - If achieved → THEN add complete damage system

### MEDIUM-TERM (After Basic Balance Achieved):

5. **Implement Complete Damage System**:
   - DAMAGED cards + Damage Die
   - Component zones (AP/Structure/Exposure)
   - Pilot Wound deck
   - Strain system
   - 3-pile system
   - **Test impact on balance**

6. **Rebalance with Complete System**:
   - Adjust damage values based on DAMAGED card pressure
   - Adjust Major Wound thresholds by Casket class
   - Add Wound removal/healing mechanics
   - Test focus fire vs spread damage strategies

### LONG-TERM (Post-Balance):

7. **Implement Advantage/Disadvantage** (v3.0 Dice Pool):
   - 3d6 take 2 highest (Advantage)
   - 3d6 take 2 lowest (Disadvantage)
   - Tactical positioning depth
   - Test impact on balance

8. **Faction-Specific Mechanics**:
   - Ossuarium Damage Graveyard resurrection
   - Nomads scavenging SCRAP cards
   - Church Suffering Dice (replace auto-discard)
   - Wyrd Taint exploitation

---

## Conclusion

**The complete damage system implementation is important for realism**, but:

1. **Fix the broken factions FIRST** (Church, Elves, Crucible)
2. **Use simplified dice sim** to test fixes quickly
3. **Only add complete mechanics AFTER basic balance achieved**

**Why?**
- Complete system is 800+ lines of code
- Takes 8-12 hours to implement
- Makes rebalancing slower (more state to track)
- **Balance is currently catastrophic** (Church 100%, Elves 0%)
- Need quick iteration, not complex simulation

**Once basic balance is 7-10 factions in 45-55% range**:
- THEN add complete damage system
- THEN test how DAMAGED cards/Pilot Wounds affect meta
- THEN fine-tune for complete ruleset

---

**Status**: Dice simulator complete and validated. Complete damage system deferred until basic balance achieved.

---

**[← Dice vs Optimal Comparison](DICE-VS-OPTIMAL-COMPARISON.md)** | **[Next: Immediate Balance Fixes →](DICE-BALANCE-FIXES-NEEDED.md)**
