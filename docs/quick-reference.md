# Quick Reference Sheet
## Penance: Absolution Through Steel

**Version**: 1.0 - Playtest Edition
**Print this page for table reference!**

---

## Round Structure

1. **Initiative Phase** - Roll 1d6 + Corruption modifier, highest goes first
2. **Action Phase** - Players take turns in initiative order
3. **End Phase** - Clear temporary effects, check victory

---

## Your Turn (Action Phase)

1. **Play cards** - Spend SP on cards from hand
2. **Track Heat** - Note Heat gained from cards
3. **Pass** - When done or out of SP
4. **Strain Roll** - If entered Danger Zone (1d6 + Heat)
5. **Draw** - Back to hand size (6 cards default)

---

## Soul-Point (SP) Safe Zones

| Weight Class | Safe Zone SP | Danger Zone SP |
|--------------|--------------|----------------|
| Scout | 5 SP | +2 (max 7 SP) |
| Support | 4 SP | +2 (max 6 SP) |
| Heavy | 3 SP | +2 (max 5 SP) |
| Assault | 2 SP | +2 (max 4 SP) |
| Aberrant | 3 SP | +2 (max 5 SP) |

**Modified by**: Taint 3-6 (+1 SP), Taint 7-9 (+2 SP), Chassis degraded (-1 SP)

---

## SP Costs (Common Actions)

| Action | SP Cost |
|--------|---------|
| Move 1 hex forward/back | 1 SP |
| Move 1 hex sidestep | 2 SP |
| Rotate 1 facing (60°) | 1 SP |
| Rotate any facing (Warden's Pivot) | 0 SP (free) |
| Light weapon attack | 1 SP |
| Medium weapon attack | 2 SP |
| Heavy weapon attack | 3 SP |
| Vent Heat (Breathe the Core) | 2 SP |
| Draw 2 cards (Soul's Recall) | 1 SP |
| Brace (Guardian's Defiance) | 1 SP |

**Note**: Equipment cards list their own SP costs!

---

## Heat Thresholds

| Heat | Effects |
|------|---------|
| 0-1 | **Normal** - No penalties |
| 2-3 | **Warm** - Strain rolls +1 |
| 4-5 | **Hot** - Strain +2, -1 Defense, weapon SP +1 |
| 6-7 | **Critical** - Strain +3, weapon SP +1, movement SP +1 |
| 8+ | **MELTDOWN** - Skip turn to vent all Heat OR take 2 Chassis damage |

---

## Strain Tables (If Entered Danger Zone)

**Roll 1d6 + Current Heat, check your weight class table:**

### Scout (5 SP)
- 1-3: Gain 1 Heat
- 4-5: Rotate 1 random facing
- 6-7: Take 1 damage to random limb
- 8+: Lose 1 SP next turn + Gain 1 Heat

### Heavy (3 SP)
- 1-5: Gain 1 Heat
- 6-7: Movement +1 SP next turn
- 8-9: -1 Defense until next round
- 10+: Take 2 Chassis damage

### Assault (2 SP)
- 1-6: Gain 2 Heat
- 7-8: Cannot move next turn
- 9-10: Must vent next turn or take 3 damage
- 11+: Take 3 Chassis damage + Gain 1 Taint

**See [turn-structure.md](turn-structure.md) for Support/Aberrant tables**

---

## Combat Resolution

### Attack Steps

1. **Declare** - Choose target, play attack card, pay SP
2. **Defender Response** - May play 1 reactive defense card
3. **Hit Roll** (if applicable):
   - **Melee**: Auto-hit
   - **Ranged**: 1d6, 4+ hits (modified)
   - **Magic**: Auto-hit
4. **Calculate Damage** - Base damage + modifiers - Defense
5. **Resolve** - Defender discards cards equal to damage

---

## Range Categories

| Range | Hexes | To-Hit Modifier |
|-------|-------|-----------------|
| Melee | Adjacent (1) | Auto-hit |
| Close | 2-3 | +1 to hit |
| Medium | 4-6 | +0 to hit |
| Long | 7+ | -1 to hit |

---

## Combat Modifiers

### To-Hit (Ranged Only)

| Condition | Modifier |
|-----------|----------|
| Close range | +1 |
| Long range | -1 |
| Partial cover | -1 |
| Rear attack | +1 |
| Called shot | -1 |
| Target Heat 6+ | +1 |

### Damage

| Condition | Modifier |
|-----------|----------|
| Rear attack | +2 damage |
| Critical hit (natural 6) | +2 damage |
| Partial cover (defender) | -1 damage |
| Tainted weapon | +1 damage |
| Arm degraded | -1 damage |

**Minimum damage**: Always 1 (even if Defense exceeds damage)

---

## Defense Modifiers

| Source | Modifier |
|--------|----------|
| Buckler (front arc) | +1 Defense |
| Tower Shield (front arc) | +2 Defense |
| Great Shield (front arc) | +3 Defense |
| Guardian's Defiance | +2 Defense |
| **Rear attack (defender)** | **-2 Defense** |
| Heat 4-5 | -1 Defense |
| Shattered Plating (Damage card) | -2 Defense |
| Partial Cover terrain | +1 Defense |
| Elevated +1 (defender) | +1 Defense |

---

## Terrain Types

| Terrain | Movement | Combat Effect |
|---------|----------|---------------|
| **Clear** | 1 SP/hex | None |
| **Difficult** (rubble) | 2 SP/hex | None |
| **Impassable** (walls) | Cannot enter | Blocks LOS |
| **Elevated +1** | +1 SP to climb | +1 to-hit/Defense |
| **Partial Cover** | Normal | +1 Defense, -1 to-hit |
| **Fire Hazard** | Normal | 1 dmg + 2 Heat at end of turn |
| **Water/Ice** | Normal/2 SP | Remove 1 Heat at end of turn |
| **Obscuring** (smoke) | Normal | -2 to-hit ranged |

---

## Component Damage Thresholds

| Damage | Effect |
|--------|--------|
| 0-2 | Minor - 1 Damage card on reshuffle |
| 3-5 | Moderate - 2 Damage cards on reshuffle |
| 6-8 | Major - 3 Damage cards + component degraded |
| 9+ | **Critical** - Component disabled |

### Degraded Penalties

- **Arm**: -1 damage on attacks from that arm
- **Chassis**: -1 SP Safe Zone
- **Legs**: Movement +1 SP

---

## Taint Corruption Track

| Taint | Status | Effects |
|-------|--------|---------|
| 0-2 | **Clean Stone** | Normal operation |
| 3-6 | **Tainted Stone** | +1 SP Safe Zone, Strain +1 |
| 7-9 | **Corrupted Stone** | +2 SP Safe Zone, Strain +2 |
| 10 | **ABOMINATION** | Transform into AI boss (game over) |

---

## Common Card Keywords

- **Universal** - Base card, always in deck (10 cards)
- **Tainted** - Requires 3+ Taint to use
- **Forbidden** - Requires 7+ Taint to use
- **Corruption** - Causes Taint gain when played
- **Relic** - Special equipment
- **Tech** - Uses ammo/charges
- **Reactive** - Play on opponent's turn (Initiative [—])
- **Passive** - Always active (not played, stays in deck)
- **Injury** - Damage card (cannot be played, clogs hand)

---

## Hand & Deck Management

- **Starting Hand**: 6 cards (modified by Source Conduit, relics)
- **Draw after playing**: Immediately draw 1 after playing each card
- **End of turn**: Draw back to hand size
- **Deck empty**: Shuffle discard + add Damage cards (based on component damage)
- **Hand + Deck = 0**: Casket disabled (defeat)

---

## Facing Diagram

```
      [1]
  [6]  ▲  [2]
       █       Your Casket
  [5]     [3]
      [4]

[1] Front
[2] Front-Right
[3] Back-Right
[4] REAR (-2 Defense!)
[5] Back-Left
[6] Front-Left

Shields cover [1][2][6] (front arc)
```

---

## Victory Conditions (Arena)

**Last Casket Standing**: Disable all enemy Caskets

**Victory Points**: First to 10-15 VP (scenario dependent)
- Kill: 5 VP
- Destroy component: 2 VP
- Control objective 2 turns: 3 VP

**Time Limit**: Highest VP when timer expires

---

## Common Mistakes (Avoid!)

1. ❌ **Playing same card twice** - Each card can only be played once per turn (unless you have duplicates)
2. ❌ **Forgetting Heat tracking** - Always note Heat gained!
3. ❌ **Overspending SP** - Max SP = Safe Zone + 2
4. ❌ **Not drawing cards** - Draw after each card played!
5. ❌ **Reactive timing wrong** - Play reactive BEFORE damage resolves
6. ❌ **Shields on rear** - Shields don't protect rear attacks!

---

## Turn Checklist

☐ Roll initiative (start of round only)
☐ Play cards, spending SP
☐ Track Heat after each card
☐ Pass when done
☐ Roll Strain Table (if Danger Zone)
☐ Draw back to hand size
☐ Check if reshuffle needed

---

## Emergency Reference

**Disabled**: Hand + Deck = 0 OR Chassis 9+ damage
**Reshuffle**: Shuffle discard + add Damage cards (1 per 2 component damage)
**Rear Attack**: +2 damage, -2 Defense (devastating!)
**Critical Hit**: Natural 6 on ranged = +2 damage, defender can't use reactives
**Meltdown**: 8+ Heat = skip turn to vent OR take 2 Chassis damage

---

**For full rules, see:**
- [turn-structure.md](turn-structure.md) - Complete turn sequence
- [combat-resolution.md](combat-resolution.md) - Attack mechanics
- [deck-construction.md](deck-construction.md) - Building decks
- [equipment-catalog.md](equipment-catalog.md) - Weapon stats
- [terrain-rules.md](terrain-rules.md) - Terrain details

---

*"Know the rules. Break the enemy."*
