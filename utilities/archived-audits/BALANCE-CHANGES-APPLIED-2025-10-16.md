# Balance Changes Applied - October 16, 2025
## Penance: Absolution Through Steel

**Implementation Date**: October 16, 2025
**Source Audit**: `BALANCE-ANALYSIS-2025-10-16.md`
**Changes Applied**: 9 balance nerfs + 1 new limb HP threshold system

---

## Executive Summary

All 9 recommended balance nerfs from the October 16, 2025 audit have been successfully implemented across 4 faction files. Additionally, a new limb-specific HP threshold system has been integrated into the Component Damage mechanics.

**Expected Meta Impact**:
- Dwarves: More vulnerable to sustained pressure (no +2 HP passive)
- Elves: Conditional regeneration prevents infinite sustain
- Ossuarium: 2 resurrections in casual (down from 3), 75% lifesteal (down from 100%)
- Church: Burst damage capped (no turn-1 alpha strike cheese)
- All Factions: Component targeting now strategic (limbs have varying durability)

---

## PART 1: FACTION BALANCE NERFS (9 Changes)

### 1. Dwarves - Stone Endurance (CRITICAL NERF)

**File**: `docs/factions/dwarves/deck-equipment-system.md`

**Before**:
```
Stone Endurance: Your maximum HP is 32 instead of 30. Add 2 extra "Breathe the Core" cards to deck at start.
```

**After**:
```
Stone Endurance: Once per mission, when you reshuffle your deck, add only 1 Damage card instead of 2 (half death spiral penalty). Does NOT increase maximum HP.
```

**Balance Reason**: Original +2 HP passive combined with Rune Counters made Dwarves nearly unkillable (32 HP + -3 damage per hit = 6.7% more HP + effective damage reduction). New version maintains thematic resilience through slower deck degradation instead of raw HP inflation.

**Meta Impact**: Dwarves lose 6.7% base tankiness but retain attrition advantage through slower death spiral. Expected win rate shift: -5% vs burst damage factions (Church), +0% vs sustained damage (Ossuarium).

---

### 2. Dwarves - Armor-Piercing (MODERATE NERF)

**File**: `docs/factions/dwarves/deck-equipment-system.md`

**Before**:
```
All Dwarven attacks gain Armor-Piercing (faction bonus ignores defenses)
```

**After**:
```
ONLY Crushing Blow (faction card) + equipment-based weapons (Warhammer, War Pick) have Armor-Piercing. Other faction cards do NOT have blanket Armor-Piercing.
```

**Balance Reason**: Universal Armor-Piercing invalidated entire defensive archetypes (Tower Shield builds, Guardian builds, Unyielding Bulwark). Selective Armor-Piercing maintains faction identity without oppressing defensive play.

**Meta Impact**: Defensive builds now viable against Dwarves. Guardian Church builds gain +10-15% survivability. Dwarves must choose specific weapons for Armor-Piercing.

---

### 3. Elves - Photosynthesis (CRITICAL NERF)

**File**: `docs/factions/elves/deck-equipment-system.md`

**Before**:
```
Photosynthesis: At end of your turn, if you did NOT attack this turn, recover 1 card from discard pile and remove 1 Heat.
```

**After**:
```
Photosynthesis: At end of your turn, if you did NOT attack this turn AND did NOT take damage this turn, recover 1 card from discard pile and remove 1 Heat.
```

**Balance Reason**: Original version triggered even when taking damage (too consistent in combat). Elves could kite and heal passively while under fire. New version requires NO DAMAGE TAKEN, making it a true defensive positioning reward.

**Meta Impact**: Passive regeneration reduced from 3 cards/round to 1-2 cards/round (conditional). Expected win rate shift: -10% vs sustained pressure, +0% vs burst.

---

### 4. Elves - Living Seal Equipment (CRITICAL NERF)

**File**: `docs/factions/elves/deck-equipment-system.md`

**Before**:
```
Living Seal - Regeneration (Passive): At start of each round, recover 1 card from discard (stacks with Verdant Regeneration = 2 cards)
```

**After**:
```
Living Seal - Regeneration (Passive): When you use a healing effect (Photosynthesis, Verdant Regeneration, Repair cards), recover +1 additional card. Does NOT grant passive card recovery per round.
```

**Balance Reason**: Original "Regeneration" card granted +1 card per round passively (stacked with Verdant Regeneration for 2 cards/round passive). Elves recovered entire deck size over 10 rounds passively. New version triggers conditionally when OTHER healing effects activate, preventing passive infinite sustain.

**Meta Impact**: Total passive regeneration reduced from 3 cards/round to 1 card/round baseline (Verdant Regeneration only). Living Seal now amplifies active healing instead of providing free sustain.

---

### 5. Elves - Bleed Stacks Cap (MODERATE NERF)

**File**: `docs/factions/elves/deck-equipment-system.md`

**Before**:
```
Bleed Counters: Stack infinitely (Bleed 1 + Bleed 2 = Bleed 3 total on target)
```

**After**:
```
Bleed Counters: Stack up to MAX 10 Bleed counters per target. Bleed damage cannot exceed 10 per turn.
```

**Balance Reason**: Original infinite stacking was oppressive in long games (20+ Bleed stacks after 10 rounds = automatic win). Cap of 10 maintains lethality (10 damage per turn is still 33% of average HP per round) while preventing degenerate scaling.

**Meta Impact**: Elves retain strong DoT identity but can no longer win through infinite scaling in long games. Expected win rate shift: -5% in games lasting 10+ rounds, +0% in short games.

---

### 6. Ossuarium - Phylactery Relic (CRITICAL NERF)

**File**: `docs/factions/ossuarium/deck-equipment-system.md`

**Before**:
```
Phylactery Relic (Accessory - 3 cards): Third resurrection (campaign/casual)
```

**After**:
```
Phylactery Relic (Accessory - 3 cards): CAMPAIGN-ONLY ITEM - Cannot be used in casual/arena play
```

**Balance Reason**: Phylactery Relic provides third resurrection (Phylactery faction card + Undying Resilience tactic + Phylactery Relic = 3 resurrections total = 4 lives). Church must deal lethal damage 4 times to win. Balanced for campaign progression but breaks casual play.

**Meta Impact**: Ossuarium limited to 2 resurrections in casual (Phylactery faction card + Undying Resilience tactic). Expected win rate shift: -10% vs burst damage (Church), -5% vs sustained pressure.

---

### 7. Ossuarium - Soul Harvest Lifesteal (MODERATE NERF)

**File**: `docs/factions/ossuarium/deck-equipment-system.md`

**Before**:
```
Soul Harvest: Deal 4 damage. Recover cards equal to damage dealt from your discard pile (max 4 cards). [100% lifesteal]
```

**After**:
```
Soul Harvest: Deal 4 damage. Recover 3 cards from your discard pile (75% lifesteal, not 100%).
```

**Balance Reason**: Original 100% lifesteal (4 damage = 4 cards recovered) was too oppressive in attrition matchups. Dwarves could not out-damage recovery rate. Reduced to 75% lifesteal (4 damage = 3 cards) maintains faction identity while preventing infinite sustain loops.

**Meta Impact**: Ossuarium sustain reduced by 25% per Soul Harvest. Expected healing over 10-round game: -10 cards recovered (30 vs 40). Expected win rate shift: -5% vs attrition factions (Dwarves).

---

### 8. Church - Blood Offering Limit (CRITICAL NERF)

**File**: `docs/factions/church/deck-equipment-system.md`

**Before**:
```
Blood Offering: Discard 2 cards from deck. Your next attack this turn: +3 damage, ignores 1 Defense, -1 to target number. [NO LIMIT]
```

**After**:
```
Blood Offering: Discard 2 cards from deck. Your next attack this turn: +3 damage, ignores 1 Defense, -1 to target number. LIMIT: You can only play 1 Blood Offering per turn.
```

**Balance Reason**: Original allowed stacking multiple Blood Offerings in one turn (discard 4-6 cards for +6-9 damage). Church could turn-1 alpha strike: Divine Judgment (8 damage) + 2x Blood Offering (+6 damage) = 14 damage guaranteed hit = instant win. Limit maintains power while preventing burst cheese.

**Meta Impact**: Turn-1 alpha strike reduced from 14+ damage to 8-10 damage. Expected win rate shift: -10% vs high-HP targets (Dwarves, Ossuarium), +0% vs low-HP targets.

---

### 9. Church - Righteous Fury Cap (MINOR NERF)

**File**: `docs/factions/church/deck-equipment-system.md`

**Before**:
```
Righteous Fury (Passive): Each time an allied Casket is destroyed this mission, gain +1 damage to all attacks permanently for the rest of the mission (stacks infinitely).
```

**After**:
```
Righteous Fury (Passive): Each time an allied Casket is destroyed this mission, gain +1 damage to all attacks permanently for the rest of the mission (stacks). LIMIT: Max +3 damage from this effect.
```

**Balance Reason**: Original infinite scaling broke multiplayer (5+ allies destroyed in 4-player game = +5 damage permanently). Capped at +3 damage (still 60% increase on 5-damage attacks) to maintain power while preventing runaway scaling.

**Meta Impact**: Multiplayer balance restored. Expected win rate shift in 4-player games: -15% vs defensive factions. 1v1 impact: +0% (rarely reaches cap).

---

## PART 2: LIMB HP THRESHOLD SYSTEM (NEW MECHANIC)

### Component Damage Thresholds (by Location)

**Files Updated**:
- `docs/rules/combat-system.md`
- `docs/codex/rules-combat.html`

**Old System**:
```
All components: 3 Component Damage = Component DESTROYED (universal threshold)
```

**New System**:
```
Head: 3 Component Damage → destroyed (fragile sensors/targeting)
Right Arm: 4 Component Damage → destroyed (moderate weapon mount durability)
Left Arm: 4 Component Damage → destroyed (moderate offhand durability)
Chassis: 5 Component Damage → destroyed (heavily armored core)
Legs: 6 Component Damage → destroyed (redundant locomotion systems)
```

**Design Rationale**:
- Creates **defensive layer** - arms and legs can absorb more punishment before reaching pilot
- **Tactical targeting** - opponents must choose: destroy Head fast (3 HP, -1 ranged attacks) vs destroy Legs slow (6 HP, +1 SP movement cost)
- **Thematic consistency** - sensors are fragile (glass optics), legs are durable (redundant actuators, heavy plating)

**Mechanical Impact**:

| Component | Old Threshold | New Threshold | Delta | Tactical Change |
|-----------|---------------|---------------|-------|----------------|
| **Head** | 3 HP | 3 HP | +0% | No change (still fragile) |
| **Right Arm** | 3 HP | 4 HP | +33% | Weapon mount more durable |
| **Left Arm** | 3 HP | 4 HP | +33% | Offhand mount more durable |
| **Chassis** | 3 HP | 5 HP | +67% | Core heavily armored |
| **Legs** | 3 HP | 6 HP | +100% | Locomotion most durable |

**Expected Gameplay Changes**:

1. **Targeting Priority Shift**:
   - Before: All components equally fragile (3 HP), players targeted randomly or by effect priority
   - After: Head is priority target (3 HP, easy to destroy, -1 ranged attacks), Legs are tank bait (6 HP, hard to destroy)

2. **Time-to-Disable (TTD) Increase**:
   - Average Component Damage per turn: 2-3 (from attacks + CRITICAL symbols)
   - Old TTD (all components): 1-2 turns to destroy any component
   - New TTD:
     - Head: 1-2 turns (unchanged)
     - Arms: 2 turns (+33% slower)
     - Chassis: 2-3 turns (+67% slower)
     - Legs: 2-3 turns (+100% slower)

3. **Defensive Viability**:
   - Caskets now have **natural damage soak** through limbs
   - Arms/Legs absorb 1-3 extra Component Damage before destruction
   - Pilot Wound risk reduced (Neural Feedback triggers at 5+ Component Damage, harder to accumulate)

4. **Meta Impact by Faction**:
   - **Dwarves**: Benefit most (tanky builds absorb more limb damage before core damage)
   - **Elves**: Neutral (rely on mobility, rarely take Component Damage)
   - **Ossuarium**: Benefit moderately (lifesteal buys time for limb damage to accumulate)
   - **Church**: Slight nerf (burst damage must now overcome higher thresholds to disable components)

---

## FILES MODIFIED (Summary)

### Faction Deck Files (4 files):
1. `docs/factions/dwarves/deck-equipment-system.md`
   - Stone Endurance revised (no +2 HP, slower death spiral)
   - Armor-Piercing limited (Crushing Blow + equipment only)
   - Faction Strengths updated with balance notes

2. `docs/factions/elves/deck-equipment-system.md`
   - Photosynthesis revised (requires no damage taken)
   - Living Seal revised (conditional trigger, not passive)
   - Bleed Mechanic capped at 10 stacks
   - Faction Strengths updated with balance notes

3. `docs/factions/ossuarium/deck-equipment-system.md`
   - Soul Harvest revised (75% lifesteal, down from 100%)
   - Phylactery Relic marked CAMPAIGN-ONLY
   - Faction Strengths updated with balance notes

4. `docs/factions/church/deck-equipment-system.md`
   - Blood Offering limited to 1 per turn
   - Righteous Fury capped at +3 damage
   - Faction Strengths updated with balance notes

### Rules Files (2 files):
5. `docs/rules/combat-system.md`
   - Component Damage section revised with limb-specific HP thresholds
   - Component Destroyed Effects reordered by HP threshold
   - Balance change notes added

6. `docs/codex/rules-combat.html`
   - Component Damage HTML table updated with HP column
   - Component Destroyed Effects table reordered by HP threshold
   - Balance change notes added to HTML

### Utility Files (1 file):
7. `utilities/BALANCE-CHANGES-APPLIED-2025-10-16.md` (THIS FILE)

---

## EXPECTED TIER LIST (POST-NERF)

### S-Tier (Best)
- **Church of Absolution** (burst alpha strike still strong, limited to 1 Blood Offering/turn)
- **Dwarven Forge-Guilds** (selective Armor-Piercing, high survivability through Rune Counters + slower death spiral)

### A-Tier (Strong)
- **The Ossuarium** (2 resurrections in casual, 75% lifesteal, grinding sustain)
- **Elven Verdant Covenant** (conditional regeneration, Bleed capped at 10, hit-and-run mobility)

### Pre-Nerf Tier List (for comparison):
1. **Elves** (3 cards/round passive = unkillable)
2. **Ossuarium** (3 resurrections = 4 lives)
3. **Dwarves** (32 HP + Rune Counters = too tanky)
4. **Church** (self-destructive, fragile)

---

## PLAYTESTING PRIORITIES

### High Priority (Critical Balance):
1. Test Dwarven Stone Endurance removal (30 HP vs old 32 HP)
2. Test Elven passive regeneration nerf (1-2 cards/round conditional vs 3 cards/round passive)
3. Test Ossuarium with 2 resurrections (Phylactery + Undying Resilience vs old 3 resurrections)

### Medium Priority (Tuning):
4. Test Church Blood Offering 1/turn limit (can still burst, but no turn-1 cheese)
5. Test Elven Bleed cap at 10 stacks (still lethal, not infinite)
6. Test Ossuarium Soul Harvest 75% lifesteal (still strong, not oppressive)

### Low Priority (Edge Cases):
7. Test Church Righteous Fury +3 cap (multiplayer only)
8. Test Dwarven selective Armor-Piercing (defensive builds now viable)
9. Test new limb HP thresholds (tactical targeting, TTD increase)

---

## ROLLBACK PLAN (if nerfs too harsh)

### Dwarves - Stone Endurance:
**Rollback Trigger**: If Dwarven win rate drops below 45% in playtests
**Rollback Option 1**: Restore +2 HP passive but add "Stone Endurance cards are dead draws (cannot be played)"
**Rollback Option 2**: Change to "Add 2 cards to deck, but reshuffles add 0 Damage cards (once per mission)"

### Elves - Regeneration:
**Rollback Trigger**: If Elven win rate drops below 40% in playtests
**Rollback Option 1**: Photosynthesis triggers if no damage OR no attack (either/or, not both)
**Rollback Option 2**: Living Seal grants +1 card/round passive, but only if you took damage this round (sustain through combat, not kiting)

### Ossuarium - Lifesteal:
**Rollback Trigger**: If Ossuarium win rate drops below 45% in playtests
**Rollback Option 1**: Soul Harvest 85% lifesteal (4 damage = 3.4 cards, round up to 4 cards 40% of the time)
**Rollback Option 2**: Phylactery Relic allowed in casual, but costs 5 SP to activate (high-cost resurrection)

### Church - Blood Offering:
**Rollback Trigger**: If Church win rate drops below 40% in playtests
**Rollback Option 1**: Allow 2 Blood Offerings per turn (limit 2 instead of 1)
**Rollback Option 2**: Remove limit, but each Blood Offering after the first costs +1 Heat

---

## CONCLUSION

All 9 recommended balance nerfs from the October 16, 2025 audit have been successfully implemented. The new limb HP threshold system has been integrated into Component Damage mechanics across all relevant files.

**Expected Meta**: Balanced 50/50 matchups across all factions (Church vs Dwarves, Elves vs Ossuarium, etc.)

**Next Steps**:
1. Playtest with new values (target: 10 games per faction matchup = 60 total games)
2. Collect win rate data (target: 48-52% per faction)
3. Iterate based on feedback (use rollback plan if nerfs too harsh)
4. Update faction-comparison-playtest.md with post-nerf analysis

---

**END OF DOCUMENT**

*"Balance is a lie we tell ourselves at night. But we applied the nerfs anyway."*
