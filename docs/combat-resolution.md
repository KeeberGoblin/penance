# Combat Resolution & Attack Mechanics
## Penance: Absolution Through Steel

**Version**: 1.0
**Last Updated**: October 9, 2025
**Status**: Playtest Ready

---

## Combat Overview

Combat in Penance uses a **hybrid system**:
- **Melee attacks**: Auto-hit (adjacent = hard to miss)
- **Ranged attacks**: Roll to hit (1d6, modified by range/cover)
- **Magic/Spells**: Auto-hit (magic seeks target)

**Defense reduces damage** (not evasion).

---

## Attack Resolution Flowchart

```
┌─────────────────────────────────────┐
│ 1. DECLARE ATTACK                   │
│ - Play attack card, pay SP cost     │
│ - Choose target in range & LOS      │
│ - Check facing (front/side/rear)    │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 2. DEFENDER RESPONSE                │
│ - May play 1 reactive defense card  │
│ - Check Defense bonuses (shields)   │
│ - Note facing modifiers             │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 3. HIT ROLL (if applicable)         │
│ - Melee: Auto-hit                   │
│ - Ranged: Roll 1d6, 4+ hits         │
│ - Magic: Auto-hit                   │
│ - Apply modifiers (range, cover)    │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 4. CALCULATE DAMAGE                 │
│ - Base damage from card             │
│ - Add modifiers (rear attack, etc.) │
│ - Subtract Defense                  │
│ - Minimum 1 damage always dealt     │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 5. RESOLVE DAMAGE                   │
│ - Defender discards cards           │
│ - Track component damage            │
│ - Check for disabled status         │
└─────────────────────────────────────┘
```

---

## Step 1: Declare Attack

### Requirements

**To declare attack, you must**:
1. Have an attack card in hand
2. Have enough SP to pay the card's cost
3. Have a valid target in range
4. Have line of sight (LOS) to target

### Choose Target

**Valid targets**:
- Enemy Caskets within range
- Monsters/NPCs (if applicable)
- Objectives (if destructible)

**Check range** (distance in hexes):
- Count hexes from your space to target's space
- Do NOT count your own hex
- Count target's hex

**Check line of sight** (see Range & LOS Rules below)

### Determine Facing

**Critical for damage calculation!**

From **attacker's position**, which hex facing of the target are you attacking?

```
      [1]
  [6]  ▲  [2]
       █       Target Casket
  [5]     [3]
      [4]

Facings:
[1] Front
[2] Front-Right
[3] Back-Right
[4] Back (Rear)
[5] Back-Left
[6] Front-Left
```

**Draw imaginary line** from center of your hex to center of target's hex.
- Which facing does the line enter? That's the facing you're attacking.

**Facing Effects**:
- **Front** (1, 2, 6): Standard Defense, shields may apply
- **Side** (3, 5): Standard Defense, shields may not apply (check shield arc)
- **Rear** (4): **-2 Defense**, critical hits more likely, shields don't apply

---

## Step 2: Defender Response

### Reactive Defense Cards

**Before damage is rolled**, defender may play **1 reactive defense card**.

**Common reactive cards**:
- **Unyielding Bulwark**: Reduce damage by 3, discard 1 random card
- **Second Skin**: Reduce damage by 1
- **Guardian's Defiance**: (Not reactive, must be played earlier)

**Reactive cards**:
- Cost **0 SP** (don't count against turn limit)
- Can be played even if you've already passed your turn
- Resolve **before** hit roll

### Calculate Base Defense

**Base Defense** = 0 for all Caskets

**Add Defense from**:
- **Shields** (if in protected arc)
  - Buckler: +1 Defense (front arc: facings 1, 2, 6)
  - Tower Shield: +2 Defense (front arc + one side)
  - Great Shield: +3 Defense (front arc only)
- **Guardian's Defiance** (Universal card): +2 Defense until next turn
- **Certain relics/abilities**: Variable
- **Bracing** (Heavy class ability): +2 Defense while immobile

**Subtract Defense from**:
- **Rear attack**: -2 Defense (target being attacked from behind)
- **Shattered Plating** (Damage card): -2 Defense
- **Heat 4-5**: -1 Defense
- **Legs degraded**: -1 Defense

**Note**: Defense can go negative! (Rear attack on damaged Casket = -4 Defense = +4 damage)

---

## Step 3: Hit Roll (If Applicable)

### Melee Attacks (Auto-Hit)

**If attack range is "Melee"**:
- Automatically hits
- No roll required
- Proceed to damage calculation

**Melee range** = Adjacent hex only (1 hex away)

---

### Ranged Attacks (Roll to Hit)

**If attack range is "Close/Medium/Long"**:

**Roll 1d6**:
- **1-3**: Miss (no damage)
- **4-6**: Hit (proceed to damage)

**Modifiers**:

| Modifier | Effect |
|----------|--------|
| **Range: Close (2-3 hexes)** | +1 to hit roll |
| **Range: Medium (4-6 hexes)** | +0 to hit roll |
| **Range: Long (7+ hexes)** | -1 to hit roll |
| **Partial cover** | -1 to hit roll |
| **Full cover** | Cannot target (must use indirect fire) |
| **Attacking from rear** | +1 to hit roll |
| **Target has Heat 6+** | +1 to hit roll (predictable movement) |
| **Attacker has Blind Sensors** (Damage card) | -1 to hit roll |

**Examples**:
- Shooting at close range (2 hexes): Roll 1d6+1, need 3+ to hit
- Shooting at long range (8 hexes) with partial cover: Roll 1d6-2, need 6 to hit (4 base + 2 modifier)

---

### Magic/Spells (Auto-Hit)

**If attack type is "SPELL"**:
- Automatically hits
- No roll required
- Magic seeks its target
- Proceed to damage calculation

**Unless**:
- Spell card specifically says "Roll to hit"
- Target has "Magic Resistance" ability

---

## Step 4: Calculate Damage

### Base Damage

**Start with card's damage value** (listed on card)

**Example**: Faithful Thrust = 4 damage

---

### Add Damage Modifiers

**Bonuses**:

| Source | Bonus |
|--------|-------|
| **Attacking from rear** (facing 4) | +2 damage |
| **Critical hit** (natural 6 on ranged attack) | +2 damage |
| **Tainted weapons** (3+ Taint) | +1 damage |
| **Scrap Fury** (Orcish racial, per reshuffle) | +1 damage (stacks) |
| **Berserker Implant** (Relic) | +1 damage all attacks |
| **Certain buffs/abilities** | Variable |

**Penalties**:

| Source | Penalty |
|--------|---------|
| **Attacking through partial cover** | -1 damage |
| **Arm degraded** (6+ damage to weapon arm) | -1 damage |
| **Sundered Servos** (Critical Damage card) | Half damage (round down) |

---

### Subtract Defense

**Defender's total Defense** (calculated in Step 2)

**Example**:
- Faithful Thrust: 4 base damage
- Attacking from rear: +2 = 6 damage
- Target has Tower Shield (+2 Defense) but rear attack (shields don't apply to rear)
- Target has 0 Defense (shield doesn't help)
- **Final damage: 6**

**If Defense is negative**:
- Treat as bonus damage
- Example: -2 Defense from rear attack + -2 from Shattered Plating = +4 damage total

---

### Minimum Damage Rule

**Attacks always deal at least 1 damage**, even if Defense exceeds damage value.

**Example**:
- Attack deals 3 damage
- Defender has +5 Defense (heavy shield + buffs)
- **Final damage: 1** (minimum)

**Exception**: Attack misses entirely (ranged attack rolled 1-3)

---

## Step 5: Resolve Damage

### Discard Cards

**Defender must discard cards equal to damage taken.**

**Choose HOW to discard**:
- **From Hand**: Choose specific cards to discard (lose options now)
- **From Deck**: Mill from top of deck without looking (preserve hand)
- **Mixed**: Combination (2 from hand, 2 from deck, etc.)

**See [damage-system.md](damage-system.md) for full details.**

---

### Component Damage Tracking

**If attack targeted specific component** (Right Arm, Chassis, etc.):

1. Discard cards normally (defender's choice)
2. **Mark component damage** on player mat
3. When you reshuffle, add Damage cards based on component damage

**Component Damage Thresholds**:

| Damage | Effect |
|--------|--------|
| 0-2 | Minor - 1 Damage card on reshuffle |
| 3-5 | Moderate - 2 Damage cards on reshuffle |
| 6-8 | Major - 3 Damage cards + component degraded (penalties) |
| 9+ | Critical - Component disabled, cards unusable |

**Degraded penalties**:
- **Right/Left Arm**: -1 damage on attacks from that arm
- **Chassis**: -1 SP Safe Zone
- **Legs**: Movement costs +1 SP

---

### Check for Disabled

**Casket is disabled if**:
- **Hand AND deck are both empty** (no more cards to play)
- **Chassis takes 9+ damage** (core destroyed)
- **Scenario-specific** (mission objectives)

**When disabled**:
- **PvP/Arena**: You lose, opponent scores VP
- **Co-op/Campaign**: You're out of combat (allies can continue)

---

## Special Attack Types

### Area of Effect (AOE)

**Some attacks hit multiple targets** (e.g., Draconic Breath, artillery)

**Resolution**:
1. Declare AOE shape and targets
2. Roll to hit **separately** for each target (if ranged)
3. Each target calculates Defense separately
4. Resolve damage individually

**Common AOE shapes**:
- **Cone**: 3 hexes in front arc (60° wedge)
- **Line**: 3-5 hexes in straight line
- **Blast**: Target hex + all adjacent hexes

---

### Called Shots (Targeting Components)

**Attacker may declare specific component** (Right Arm, Chassis, Legs, etc.)

**Cost**: -1 to hit roll (ranged only)

**Effect**: Damage applies to that component for tracking purposes

**Example**:
- "I shoot at his Right Arm with my bow"
- Roll to hit at -1 penalty
- If hit, damage goes to Right Arm component

**Benefit**: Disable specific equipment (e.g., destroy weapon arm to prevent attacks)

---

### Overkill Damage

**If damage exceeds defender's remaining cards**:

**Example**:
- Defender has 4 cards total (2 in hand, 2 in deck)
- Takes 7 damage

**Resolution**:
1. Discard all 4 cards (hand + deck empty)
2. Casket is **disabled**
3. Excess damage (3) is wasted

**No "splash" damage** to nearby units (unless AOE attack specifies)

---

## Range & Line of Sight

### Range Categories

| Range | Hexes | Weapons |
|-------|-------|---------|
| **Melee** | Adjacent (1 hex) | Swords, hammers, claws |
| **Close** | 2-3 hexes | Bows, pistols, short rifles |
| **Medium** | 4-6 hexes | Rifles, crossbows, standard cannons |
| **Long** | 7+ hexes | Sniper rifles, artillery, siege weapons |

### Counting Hexes

**Distance** = Number of hexes between you and target

**How to count**:
1. Start from your hex
2. Count shortest path to target's hex
3. **Do NOT count your own hex**
4. **Count target's hex**

**Example**:
```
You → ○ → ○ → Target = 3 hexes (Close range)
```

---

### Line of Sight (LOS)

**To have LOS, draw imaginary line** from center of your hex to center of target's hex.

**Clear LOS**:
- No obstacles between you and target
- Standard attack

**Partial Cover**:
- Low obstacles (rubble, barricades, other Caskets)
- Target gets **+1 Defense**, attacker gets **-1 to hit**

**Full Cover**:
- Solid obstacles (walls, buildings, large terrain)
- **Cannot target directly**
- Must use indirect fire (certain weapons only)

---

### Elevation & Height

**Higher ground grants bonus**:
- Attacking target 1+ elevation levels below: **+1 to hit**
- Defending from 1+ elevation levels above: **+1 Defense**

**Elevation levels**:
- Ground level: 0
- Hill/Rubble: +1
- Building/Tower: +2

**Jumping/Flying**:
- Jump jets, wings, etc. can change elevation temporarily
- Costs extra SP (usually +1 SP per level)

---

## Armor & Damage Types

### Armor (Future Expansion)

**Currently**: Armor is abstracted into Defense

**Future**: Damage types may interact differently:
- **Physical**: Standard damage
- **Fire**: Ignores 1 point of Defense
- **Ice**: Reduces movement next turn
- **Lightning**: Chains to adjacent targets
- **Poison**: Ongoing damage over time
- **Acid**: Ignores all armor

**For now**: All damage is treated as Physical, Defense applies normally.

---

## Critical Hits

### Automatic Criticals

**Rear attacks from melee** (adjacent + facing 4):
- Auto-critical (no roll needed)
- +2 damage bonus
- May trigger component-specific effects

---

### Ranged Criticals

**When you roll natural 6 to hit** (before modifiers):
- Automatic hit (even if modifiers would make you miss)
- **+2 damage bonus**
- Defender cannot use reactive defense cards (too fast to react)

**Example**:
- Shooting at long range with cover: Need 6 to hit
- Roll natural 6 = Critical Hit!
- Damage: Base + 2, defender can't play Unyielding Bulwark

---

## Combat Examples

### Example 1: Melee Attack (Auto-Hit)

**Attacker**: Human Scout with Longsword (Right Arm)
**Defender**: Orcish Heavy with Tower Shield (Left Arm)

**Attacker's turn**:
1. Plays **Faithful Thrust** (2 SP, 4 damage, melee)
2. Declares attack on adjacent Heavy Casket
3. Checks facing: Attacking from front (facing 1)

**Defender's response**:
- Tower Shield provides +2 Defense (front arc active)
- Plays **Unyielding Bulwark** (reactive): +3 Defense, discard 1 card after
- Total Defense: 0 base + 2 shield + 3 Bulwark = **+5 Defense**

**Hit roll**:
- Melee = Auto-hit (no roll needed)

**Damage calculation**:
- Base damage: 4
- Front attack: +0
- Subtract Defense: 4 - 5 = -1
- **Minimum damage: 1**

**Resolution**:
- Defender discards 1 card (from hand or deck)
- Defender discards 1 additional random card (Bulwark cost)
- **Total: 2 cards discarded** (1 from damage, 1 from Bulwark)

---

### Example 2: Ranged Attack (Roll to Hit)

**Attacker**: Elven Scout with Longbow (Right Arm)
**Defender**: Human Heavy at Medium range (5 hexes), partial cover

**Attacker's turn**:
1. Plays **Swift Arrow** (2 SP, 3 damage, Medium range)
2. Declares attack on Heavy 5 hexes away
3. Target is behind rubble (partial cover)

**Defender's response**:
- No shield equipped
- No reactive cards played
- Partial cover: +1 Defense
- **Total Defense: +1**

**Hit roll**:
- Ranged attack: Roll 1d6
- Medium range: +0
- Partial cover: -1 to hit
- **Need 5+ to hit** (4 base + 1 modifier)
- **Rolls 5 = Hit!**

**Damage calculation**:
- Base damage: 3
- Partial cover: -1 damage
- Subtract Defense: 2 - 1 = 1
- **Final damage: 1**

**Resolution**:
- Defender discards 1 card

---

### Example 3: Rear Attack Critical

**Attacker**: Dwarven Heavy with Warhammer (Right Arm)
**Defender**: Scout (low defense, high evasion)

**Attacker's turn**:
1. Flanked Scout, attacking from rear (facing 4)
2. Plays **Crushing Descent** (2 SP, 5 damage, melee)

**Defender's response**:
- No shield (Scouts rarely use shields)
- Plays **Second Skin** (reactive): +1 Defense
- Rear attack: -2 Defense
- **Total Defense: 0 + 1 - 2 = -1** (negative!)

**Hit roll**:
- Melee = Auto-hit
- Rear melee = Auto-critical

**Damage calculation**:
- Base damage: 5
- Rear attack: +2
- Critical (rear melee): Already included
- Subtract Defense: 7 - (-1) = 7 + 1 = **8 damage**

**Resolution**:
- Scout discards 8 cards
- Scout likely has only ~22-25 cards total
- This is **devastating** (1/3 of deck gone in one hit)

**Lesson**: Don't let enemies get behind you!

---

## Common Combat Questions

### Q: Can I attack multiple enemies in one turn?
**A**: Yes, if you have multiple attack cards and enough SP. Play each attack separately.

### Q: Can I attack the same enemy twice?
**A**: Yes, if you have multiple attack cards (or duplicates).

### Q: Do I have to attack?
**A**: No. You can spend SP on movement, utility, or pass without attacking.

### Q: Can I split movement and attacks?
**A**: Yes. Example: Move 2 hexes (play Desperate Lunge), attack (play Faithful Thrust), move again (play another movement card if you have it).

### Q: Can I attack after moving?
**A**: Yes. You can play cards in any order during your turn.

### Q: What if I have no valid targets?
**A**: You cannot play attack cards without valid targets. Choose different cards or pass.

### Q: Can I attack allies?
**A**: Not in standard rules. Some scenarios (Hidden Agendas, Betrayal objectives) may allow it.

### Q: Does damage carry over reshuffles?
**A**: Discarded cards go to discard pile. Component damage persists and adds Damage cards when you reshuffle. See [damage-system.md](damage-system.md).

---

## Quick Reference: Combat Modifiers

### To-Hit Modifiers (Ranged Only)

| Condition | Modifier |
|-----------|----------|
| Close range (2-3 hexes) | +1 to hit |
| Long range (7+ hexes) | -1 to hit |
| Partial cover | -1 to hit |
| Rear attack | +1 to hit |
| Called shot | -1 to hit |
| Target Heat 6+ | +1 to hit |
| Attacker Blind Sensors | -1 to hit |

### Damage Modifiers

| Condition | Modifier |
|-----------|----------|
| Rear attack | +2 damage |
| Critical hit | +2 damage |
| Partial cover (target) | -1 damage |
| Tainted weapon | +1 damage |
| Arm degraded (attacker) | -1 damage |

### Defense Modifiers

| Source | Modifier |
|--------|----------|
| Buckler shield (front arc) | +1 Defense |
| Tower shield (front arc) | +2 Defense |
| Great shield (front arc) | +3 Defense |
| Guardian's Defiance | +2 Defense |
| Rear attack (defender) | -2 Defense |
| Heat 4-5 | -1 Defense |
| Shattered Plating | -2 Defense |

---

## Next Steps

- See [turn-structure.md](turn-structure.md) for full turn sequence
- See [damage-system.md](damage-system.md) for injury mechanics
- See [terrain-rules.md](terrain-rules.md) for environmental effects
- See [equipment-catalog.md](equipment-catalog.md) for weapon stats

---

*"Steel meets steel. Stone cries out. Only one walks away."*
