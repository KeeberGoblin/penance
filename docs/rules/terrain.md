# Terrain & Environmental Rules
## Penance: Absolution Through Steel

**Version**: 1.0
**Last Updated**: October 9, 2025
**Status**: Playtest Ready

---

## Overview

Terrain adds tactical depth to combat. Positioning matters—high ground, cover, hazards all affect battles.

---

## Terrain Types

### 1. Clear Terrain (Baseline)

**Movement**: 1 SP per hex
**Combat**: No modifiers
**Special**: None

**Examples**: Flat ground, paved roads, open fields

---

### 2. Difficult Terrain

**Movement**: Each hex costs +1 SP (2 SP total per hex)
**Combat**: No penalties
**Special**: Certain abilities ignore difficult terrain (Ironstrider's Rush, Aerial Leap)

**Examples**: Rubble, shallow water, mud, dense vegetation

**Note**: Difficult terrain slows movement but doesn't block LOS.

---

### 3. Impassable Terrain

**Movement**: Cannot enter
**Combat**: Blocks line of sight completely (Full Cover)
**Special**: Flying units can pass over (Jump Jets)

**Examples**: Walls, solid buildings, deep chasms, collapsed structures

---

### 4. Elevated Terrain (+1 Level)

**Movement**: Costs +1 SP to move UP one level (free to move DOWN)
**Combat**:
- Attacking target below: +1 to hit (ranged), +1 damage (melee if charging down)
- Defending from above: +1 Defense

**Examples**: Hills, rubble piles, platforms, stairs

**Stacking**: Terrain can have multiple elevation levels (+1, +2, +3)

---

### 5. Cover Terrain (Partial Cover)

**Movement**: Normal (1 SP per hex)
**Combat**:
- Defender in cover: +1 Defense
- Attacker shooting at target in cover: -1 to hit
- Melee attacks ignore cover (you're adjacent)

**Examples**: Barricades, low walls, scattered rubble, tree trunks

**Line of Sight**: Does not block LOS, provides partial cover

---

### 6. Hazard Terrain (Fire/Lava)

**Movement**: Normal (but dangerous)
**Combat**: No modifiers
**Special**:
- At end of your turn, if standing in Fire hex: Take 1 damage, gain 2 Heat
- At end of round, Fire spreads to 1 random adjacent hex (roll 1d6 for direction)

**Examples**: Burning buildings, lava flows, chemical spills

**Interaction**: Water hexes extinguish adjacent Fire hexes

---

### 7. Cooling Terrain (Water/Ice)

**Movement**: Water = Normal, Ice = Difficult (+1 SP)
**Combat**: No modifiers
**Special**:
- At end of your turn in Water hex: Remove 1 Heat
- At end of your turn in Ice hex: Remove 1 Heat, but must pass stability check (roll 4+ or rotate 1 random facing)

**Examples**: Shallow ponds, ice fields, snow drifts

**Interaction**: Fire damage to water hex creates steam (blocks LOS for 1 round)

---

### 8. Obscuring Terrain (Smoke/Mist)

**Movement**: Normal
**Combat**:
- All ranged attacks INTO or OUT OF this hex: -2 to hit
- Melee attacks unaffected (you're too close to miss)
**Special**: Smoke dissipates at end of round (1/3 chance per smoke hex, roll 5+ to clear)

**Examples**: Smoke grenades, mist, fog, chemical clouds

**Line of Sight**: Blocks LOS through the hex (can't shoot through smoke to target beyond)

---

## Terrain Interaction Examples

### Example 1: Shooting from High Ground

**Attacker**: Scout on +1 Elevation hill
**Defender**: Heavy on ground level, 4 hexes away (Medium range)

**Combat**:
- Medium range: 1d6, 4+ to hit (baseline)
- High ground: +1 to hit
- **Total**: 1d6, 3+ to hit

**If hit**: Base damage + 0 (elevation bonus is to-hit only, not damage)

---

### Example 2: Charging Through Fire

**Scout**: Wants to move 3 hexes to reach enemy
- Hex 1: Clear (1 SP)
- Hex 2: Fire hazard (1 SP to enter, but will take damage at end of turn)
- Hex 3: Clear, adjacent to enemy (1 SP)

**Cost**: 3 SP total

**At end of turn**:
- Scout is in Hex 3 (clear)
- But Scout WAS in Fire hex during turn
- **Take 1 damage, gain 2 Heat** (Fire hex penalty)

**Decision**: Worth it to close distance? Or go around?

---

### Example 3: Fighting in Cover

**Attacker**: Heavy with Warhammer, 5 hexes away (Medium range)
**Defender**: Scout behind barricade (Partial Cover)

**Ranged Option** (if Heavy had bow):
- Medium range: 1d6, 4+ to hit
- Partial cover: -1 to hit
- **Total**: 1d6, 5+ to hit
- Defender gets +1 Defense from cover

**Melee Option** (if Heavy closes distance):
- Move adjacent (ignores cover penalty)
- Melee auto-hits
- Defender does NOT get +1 Defense (melee ignores cover)

**Lesson**: Cover is stronger against ranged attacks.

---

## Environmental Effects

### Weather (Optional)

**Can add weather effects to scenarios**:

**Rain**:
- All Fire hexes extinguished at start of scenario
- All ranged attacks: -1 to hit
- Water hexes increase to cover more area

**Sandstorm**:
- All hexes count as Obscuring (ranged -2 to hit)
- Scout class loses +1 initiative bonus (can't see far ahead)

**Extreme Heat**:
- All Caskets start with 2 Heat
- No passive cooling (water hexes don't remove Heat)

---

### Destructible Terrain

**Some terrain can be destroyed**:

**Barricades** (Cover):
- 5 HP
- When destroyed: Becomes rubble (Difficult Terrain)

**Walls** (Impassable):
- 10 HP
- Assault class siege weapons can damage
- When destroyed: Becomes rubble pile (Difficult + Partial Cover)

**How to Attack Terrain**:
- Declare terrain hex as target
- Attack resolves normally (hits automatically, no Defense)
- Track HP, destroy when reduced to 0

---

## Hex Board Setup

### Standard Arena Board (7x7)

```
   1  2  3  4  5  6  7
 ┌──┬──┬──┬──┬──┬──┬──┐
1│  │  │▓▓│  │▓▓│  │  │  ▓▓ = Impassable (walls)
 ├──┼──┼──┼──┼──┼──┼──┤
2│  │░░│  │  │  │░░│  │  ░░ = Difficult (rubble)
 ├──┼──┼──┼──┼──┼──┼──┤
3│▓▓│  │  │△△│  │  │▓▓│  △△ = Elevated (+1)
 ├──┼──┼──┼──┼──┼──┼──┤
4│  │  │△△│  │△△│  │  │  ▒▒ = Partial Cover
 ├──┼──┼──┼──┼──┼──┼──┤
5│▓▓│  │  │▒▒│  │  │▓▓│
 ├──┼──┼──┼──┼──┼──┼──┤
6│  │░░│  │  │  │░░│  │  Deployment Zones:
 ├──┼──┼──┼──┼──┼──┼──┤  P1 = Row 1-2
7│  │  │▓▓│  │▓▓│  │  │  P2 = Row 6-7
 └──┴──┴──┴──┴──┴──┴──┘
```

**Features**:
- 4 Impassable wall hexes (corners + center sides)
- 4 Difficult terrain rubble hexes (flanks)
- 4 Elevated hexes (center cluster + sides)
- 1 Partial Cover hex (center)

**Deployment**:
- Player 1: Rows 1-2 (any hex)
- Player 2: Rows 6-7 (any hex)

---

## Terrain Strategy Tips

### For Scouts
- **Use elevation**: High ground negates your low defense with +1 Defense bonus
- **Avoid hazards**: Low HP means 1 damage from Fire is significant (1/22 of your deck!)
- **Jump over impassable**: Jump Jets let you ignore walls

### For Heavy/Assault
- **Claim high ground early**: Slow movement means you won't get there later
- **Use cover when bracing**: Partial cover + Shield Wall = nearly immune to ranged
- **Smash destructible terrain**: Clear path for allies

### For Support
- **Stay near allies but use cover**: Buff from behind barricades
- **Control chokepoints**: Stand in difficult terrain to slow enemies (you can repair the SP cost with buffs)

### For Aberrant
- **Teleport ignores terrain**: Warp Anchor bypasses everything
- **Use hazards offensively**: Teleport enemies into Fire hexes

---

## Common Terrain Questions

### Q: Can I move through allies?
**A**: Yes, but you cannot end your movement in an occupied hex.

### Q: Can I move through enemies?
**A**: No, unless you have special ability (Void Walk for Aberrant).

### Q: Does flying ignore all terrain?
**A**: Yes. Jump Jets, Aerial Leap, and similar abilities ignore terrain penalties and can pass over Impassable hexes.

### Q: Can I destroy terrain on purpose?
**A**: Yes. Attack the terrain hex. It has HP but no Defense.

### Q: Do I take Fire damage if I move through a Fire hex but don't end there?
**A**: No. Only if you END YOUR TURN in the Fire hex.

### Q: Can I push enemies into hazards?
**A**: Yes! Shield Bash, knockback effects, etc. can push into Fire/hazards. They take damage at end of their turn.

### Q: Does partial cover stack with shields?
**A**: Yes. Partial Cover (+1 Defense) + Tower Shield (+2 Defense) = +3 Defense total.

---

## Terrain Setup Recommendations

### For New Players (Simple)
- 2 Impassable walls
- 2 Partial Cover hexes
- 1 Elevated hex
- Rest Clear terrain

**Goal**: Learn basics without overwhelming terrain complexity

---

### For Experienced Players (Complex)
- 4-6 Impassable walls (create chokepoints)
- 3-4 Partial Cover hexes (reward positioning)
- 2-3 Elevated hexes (high ground battles)
- 2-3 Difficult terrain hexes (slow movement)
- 1-2 Hazard hexes (Fire or Ice)

**Goal**: Tactical depth, multiple approach vectors

---

### For Narrative Scenarios
- **Ruined City**: Lots of rubble (Difficult), broken walls (Partial Cover), collapsed buildings (Impassable)
- **Volcano Arena**: Lava hexes (Fire Hazard), elevated rock outcrops, smoke vents (Obscuring)
- **Frozen Wastes**: Ice hexes (Difficult + Cooling), snow drifts (Partial Cover), crevasses (Impassable)
- **Overgrown Temple**: Dense vegetation (Difficult), crumbling pillars (Partial Cover), temple walls (Impassable)

---

## Next Steps

- See [combat-resolution.md](combat-resolution.md) for attack mechanics
- See [arena-scenarios.md](arena-scenarios.md) for pre-made maps
- See [turn-structure.md](turn-structure.md) for movement rules

---

*"Terrain is your ally or your tomb. Choose where you stand."*
