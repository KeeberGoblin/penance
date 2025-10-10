# Turn Structure & Action Resolution
## Penance: Absolution Through Steel

**Version**: 1.0
**Last Updated**: October 9, 2025
**Status**: Playtest Ready

---

## Overview

Penance uses **SP-based turns** where each player spends their Soul-Point pool to play multiple cards per turn. Turns are taken sequentially in initiative order, creating a dynamic tactical flow.

---

## Round Structure

### Round Flow

1. **Initiative Phase** - Determine turn order
2. **Action Phase** - Players take turns in order
3. **End Phase** - Resolve end-of-round effects

---

## Initiative Phase

### Determining Initiative

**At the start of each round:**

1. All players roll **1d6 + Corruption modifier**
   - **Clean Stone (0-2 Taint)**: +0
   - **Tainted Stone (3-6 Taint)**: +1
   - **Corrupted Stone (7-9 Taint)**: +2
   - **Abomination (10 Taint)**: +3

2. **Highest roll goes first**, then descending order
3. **Ties**: Re-roll tied players only

**Initiative order remains fixed for the entire round.**

### Initiative Modifiers

**Bonuses**:
- Scout class: +1 to initiative roll
- Fae Bargain active: +2 to initiative roll
- Certain equipment/relics: Variable

**Penalties**:
- Assault class: -1 to initiative roll
- Heat 7+: -1 to initiative roll
- Legs degraded (6+ damage): -1 to initiative roll

---

## Action Phase (Your Turn)

### Turn Overview

**On your turn, you:**

1. **Spend Soul-Points (SP)** to play cards from your hand
2. **Execute card effects** in the order you play them
3. **Track Heat** and risk entering the Danger Zone
4. **Pass** when you're done or out of SP

**You may play as many cards as your SP allows.**

---

### Soul-Point Budget

**Your Safe Zone** (varies by weight class):
- Scout: 5 SP
- Support: 4 SP
- Heavy: 3 SP
- Assault: 2 SP
- Aberrant: 3 SP

**Modified by**:
- **Taint 3-6**: +1 SP (Tainted Stone bonus)
- **Taint 7-9**: +2 SP (Corrupted Stone bonus)
- **Chassis degraded**: -1 SP
- **Certain relics/abilities**: Variable

---

### Safe Zone vs Danger Zone

**Safe Zone** (Green):
- Spend up to your Safe Zone SP with no risk
- No Strain roll required
- Recommended for cautious play

**Danger Zone** (Red):
- Spend beyond your Safe Zone for **+2 SP** (one-time)
- **Maximum total SP per turn = Safe Zone + 2**
  - Scout: 5 + 2 = 7 SP max
  - Assault: 2 + 2 = 4 SP max
- **At end of turn**: Roll on Strain Table (see below)

**Example**:
- Heavy Casket has 3 SP Safe Zone
- Spends 4 SP total (1 into Danger Zone)
- Must roll on Strain Table at end of turn

---

### Playing Cards

**Step 1: Choose Card**
- Select card from your hand
- Check SP cost
- Verify you have enough SP remaining this turn

**Step 2: Pay SP Cost**
- Reduce your available SP by the card's cost
- Track on Strain Dial or paper

**Step 3: Declare Targets/Effects**
- Announce what the card does
- Choose targets (if applicable)
- Check range and line of sight

**Step 4: Resolve Card**
- Execute effect immediately
- Apply damage, movement, buffs, etc.
- Discard card to your discard pile

**Step 5: Track Heat**
- If card generates Heat, add tokens
- Note Heat total (affects Strain roll later)

**Repeat** until you pass or run out of SP.

---

### Free Actions (0 SP)

**Cards with SP Cost: 0** do not count toward your SP limit.

**Examples**:
- Warden's Pivot (rotate to any facing)
- Reactive cards (played on opponent's turn)

**You may play unlimited free actions** during your turn, but each card can only be played once per turn.

---

### Passing Your Turn

**When you pass**:
- You may have unspent SP remaining (it's lost)
- You cannot take more actions this round
- Turn passes to next player in initiative order

**You must pass if**:
- You have no cards in hand
- You have no SP remaining
- You choose to pass

---

## Reactive Cards (Interrupts)

### When Can You Play Reactive Cards?

**Reactive cards** have Initiative **[—]** and can be played **on an opponent's turn**.

**Triggers**:
- "When targeted by attack" (Unyielding Bulwark, Second Skin)
- "When enemy enters adjacent hex" (trap effects)
- "When ally takes damage" (protective abilities)

**Timing**:
1. Opponent declares action (attack, movement, etc.)
2. **Before resolving**, you may play 1 reactive card
3. Reactive effect resolves first
4. Then opponent's action resolves (modified by your reactive)

**SP Cost**:
- Most reactive cards cost **0 SP**
- They do NOT count against your turn's SP limit
- You can play them even if you've already passed your turn

**Limit**: **1 reactive card per trigger** (you can't stack multiple reactive defenses against the same attack)

---

## Strain Table (Danger Zone Risk)

### When to Roll

**If you entered the Danger Zone** (spent more than Safe Zone SP), roll at the **end of your turn**.

### How to Roll

**Roll 1d6 + Current Heat**

Compare total to your weight class's Strain Table:

---

### Scout Strain Table (5 SP Safe Zone)

| Roll Total | Effect |
|------------|--------|
| 1-3 | **Servo Whine** - Gain 1 Heat token |
| 4-5 | **Gyro Slip** - Rotate 1 random facing (roll 1d6: 1-2 left, 3-4 right, 5-6 no change) |
| 6-7 | **Structural Stress** - Take 1 damage to random limb (roll: 1-2 Right Arm, 3-4 Left Arm, 5-6 Legs) |
| 8+ | **Critical Failure** - Lose 1 SP Safe Zone next turn + Gain 1 Heat |

---

### Support Strain Table (4 SP Safe Zone)

| Roll Total | Effect |
|------------|--------|
| 1-4 | **Power Fluctuation** - Gain 1 Heat token |
| 5-6 | **System Lag** - Discard 1 random card from hand |
| 7-8 | **Overload** - Cannot use Support abilities next turn |
| 9+ | **Cascade Failure** - All adjacent allies gain 1 Heat |

---

### Heavy Strain Table (3 SP Safe Zone)

| Roll Total | Effect |
|------------|--------|
| 1-5 | **Engine Strain** - Gain 1 Heat token |
| 6-7 | **Hydraulic Lock** - Movement costs +1 SP next turn |
| 8-9 | **Armor Fatigue** - -1 Defense until end of next round |
| 10+ | **Pressure Breach** - Take 2 damage to Chassis |

---

### Assault Strain Table (2 SP Safe Zone)

| Roll Total | Effect |
|------------|--------|
| 1-6 | **Reactor Spike** - Gain 2 Heat tokens |
| 7-8 | **Immobilization** - Cannot move next turn (can still rotate and attack) |
| 9-10 | **Meltdown Warning** - Must spend next turn venting (play no other cards) or take 3 damage |
| 11+ | **Catastrophic Breach** - Take 3 damage to Chassis + Gain 1 Taint |

---

### Aberrant Strain Table (3 SP Safe Zone - Weird Effects)

| Roll Total | Effect |
|------------|--------|
| 1-3 | **Whispers** - Gain 1 Taint token |
| 4-5 | **Reality Slip** - Teleport 1d3 hexes in random direction (roll 1d6 for facing) |
| 6-7 | **Mutation** - Roll 1d6: 1-3 = +1 damage all attacks next turn, 4-6 = -1 Defense next turn |
| 8-9 | **Possession** - Opponent to your left controls your next action (must spend 1 SP minimum) |
| 10+ | **Void Touch** - All adjacent enemies gain 1 Taint, you gain 2 Taint |

---

## Heat Management

### Heat Thresholds (Revised for Balance)

| Heat | Effects |
|------|---------|
| 0-1 | **Normal operations** - No penalties |
| 2-3 | **Warm** - All Strain rolls +1 |
| 4-5 | **Hot** - Strain +2, -1 Defense, weapon SP costs +1 |
| 6-7 | **Critical** - Strain +3, weapon SP costs +1, movement costs +1 SP |
| 8+ | **MELTDOWN** - At start of your turn, choose: (A) Skip entire turn to vent all Heat, OR (B) Take 2 Chassis damage and continue |

### Gaining Heat

**Sources**:
- Playing cards with "Heat: +X" keyword
- Danger Zone Strain Table results
- Environmental hazards (standing in lava, fire hexes)
- Corruption effects

### Removing Heat

**Methods**:
- **Breathe the Core** (Universal card): 2 SP, remove 1d3 Heat
- **Support class abilities**: Can vent allies' Heat
- **Environmental**: Water hexes, ice terrain (remove 1 Heat at end of turn)
- **Passive cooling relics**: Specific equipment
- **Emergency venting**: Skip entire turn to remove all Heat (when at 8+ Heat)

**Note**: Heat does NOT reduce automatically at end of round. You must actively manage it.

---

## End Phase

### End of Round Cleanup

**After all players have passed**:

1. **Remove temporary effects**
   - "Until end of round" buffs/debuffs expire
   - Temporary Defense bonuses reset

2. **Check environmental effects**
   - Standing in hazard hexes (lava, ice, etc.)
   - Terrain-based healing/damage

3. **Resolve end-of-round abilities**
   - Elven Symbiosis (remove 1 Damage card from discard)
   - Passive cooling effects
   - Certain relic triggers

4. **Check victory conditions**
   - Any Casket disabled?
   - Objective completed?
   - VP threshold reached?

5. **Start new round** - Roll initiative again

---

## Card Draw & Deck Management

### Drawing Cards

**When you draw**:
- At **start of game**: Draw 6 cards (default hand size)
- **After playing card**: Immediately draw 1 card to replace it
- **End of your turn**: Draw back up to hand size (6 cards)
- **Special effects**: Some cards allow extra draws

### Hand Size

**Base**: 6 cards

**Modified by**:
- **Source Conduit Arm**: +1 (total 7)
- **Tome of Echoes** (Relic): +1 (total 7)
- **Berserker Implant** (Relic): -1 (total 5)
- **Veteran's Instinct** (Pilot Scar): +1 (total 7)

### Deck Empty (Reshuffle)

**When you need to draw but deck is empty**:

1. **Shuffle discard pile** to form new deck
2. **Add Damage cards** based on component injuries (see Damage System)
3. **Continue drawing** from new deck

**Deck composition worsens** each reshuffle as Damage cards accumulate.

### Hand Empty

**If your hand is empty during your turn**:
- You must pass (cannot play cards)
- Draw back up to hand size at end of turn

**If hand AND deck are both empty**:
- Your Casket is **disabled** (defeated)

---

## Taking Damage

### Damage Resolution (During Opponent's Turn)

**When you take damage**:

1. **Announce damage total** (after defense/armor)
2. **Choose how to discard** cards equal to damage:
   - **From Hand**: Lose tactical options now
   - **From Deck**: Mill from top without looking
   - **Mixed**: Combination of both

3. **Track component damage** (if specific location targeted)
4. **Continue playing** (if you still have cards)

**See [damage-system.md](damage-system.md) for full details on component damage, injuries, and reshuffling.**

---

## Complete Turn Example

### Scout Turn (5 SP Safe Zone, 2 Heat currently)

**Hand**: Desperate Lunge, Faithful Thrust (longsword), Warden's Pivot, Unyielding Bulwark, Breathe the Core, Soul's Recall

**Board State**:
- 4 hexes from enemy Heavy Casket
- Currently facing north
- Heat: 2 (Strain +1 if entering Danger Zone)

**Plan**: Close distance and attack

---

**Action 1**: Play **Desperate Lunge** (1 SP, +1 Heat)
- Move 2 hexes toward enemy
- Now 2 hexes away
- SP spent: 1/5
- Heat: 3

**Action 2**: Play **Warden's Pivot** (0 SP, free action)
- Rotate to face enemy
- SP spent: 1/5 (no change)
- Heat: 3

**Action 3**: Play **Faithful Thrust** (2 SP, longsword attack)
- Still 2 hexes away (not adjacent = out of melee range)
- **Realizes mistake** - can't attack, card wasted?
- **DM ruling**: Can take back action if realized immediately (friendly playtest rule)

**Revised Action 3**: Play **Soul's Recall** (1 SP)
- Draw 2 cards
- Now hand has: Faithful Thrust, Unyielding Bulwark, Breathe the Core, + 2 new cards
- SP spent: 2/5
- Heat: 3

**Action 4**: Play **Breathe the Core** (2 SP, remove 1d3 Heat)
- Roll 1d3 = 2
- Remove 2 Heat
- SP spent: 4/5
- Heat: 1

**Action 5**: Play **Desperate Lunge** again?
- **Wait**: Already discarded it. Can't play same card twice per turn.

**Pass turn**
- Spent 4 SP (stayed in Safe Zone, no Strain roll)
- Heat reduced from 3 → 1
- Draw back up to 6 cards

---

## Common Mistakes (First-Time Players)

### ❌ Playing Multiple Copies
**Wrong**: "I play Desperate Lunge twice to move 4 hexes"
**Right**: Each card can only be played once per turn (unless you have duplicates from equipping 2 of the same weapon)

### ❌ Forgetting Heat
**Wrong**: Playing multiple Heat-generating cards without tracking
**Right**: Track Heat on dial/paper, check thresholds after each card

### ❌ Overspending SP
**Wrong**: Scout tries to spend 8 SP in one turn
**Right**: Max SP = Safe Zone + 2 (Scout max = 7 SP total)

### ❌ Reactive Timing
**Wrong**: Playing Unyielding Bulwark after damage is resolved
**Right**: Declare reactive card before damage calculation

### ❌ Not Drawing Cards
**Wrong**: Ending turn with 3 cards in hand, not drawing
**Right**: Always draw back to hand size (6) at end of turn

---

## Quick Reference: Turn Sequence

### Your Turn Checklist

1. ☐ Roll initiative (start of round only)
2. ☐ Check Heat threshold penalties
3. ☐ Play cards, spending SP
4. ☐ Track Heat after each card
5. ☐ Pass when done
6. ☐ Roll Strain Table (if entered Danger Zone)
7. ☐ Draw back to hand size
8. ☐ Check if reshuffle needed

---

## Next Steps

- See [combat-resolution.md](combat-resolution.md) for attack mechanics
- See [damage-system.md](damage-system.md) for injury rules
- See [deck-construction.md](deck-construction.md) for building legal decks

---

*"Know your limits. Then decide if they're worth breaking."*
