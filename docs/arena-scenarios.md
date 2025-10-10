# Arena Scenarios - Playtest Missions
## Penance: Absolution Through Steel

**Version**: 1.0
**Last Updated**: October 9, 2025
**Status**: Playtest Ready

---

## Scenario 1: First Blood (1v1 Tutorial)

**Type**: Arena PvP
**Players**: 2
**Duration**: 20-30 minutes
**Difficulty**: Beginner

---

### Setup

**Board Size**: 7x7 hex grid

**Terrain**:
```
   A  B  C  D  E  F  G
 ┌──┬──┬──┬──┬──┬──┬──┐
1│P1│P1│  │  │  │P2│P2│  P1/P2 = Deployment
 ├──┼──┼──┼──┼──┼──┼──┤  ▓▓ = Impassable Wall
2│P1│P1│  │  │  │P2│P2│  ░░ = Difficult (Rubble)
 ├──┼──┼──┼──┼──┼──┼──┤  △△ = Elevated (+1)
3│  │  │░░│  │░░│  │  │  ▒▒ = Partial Cover
 ├──┼──┼──┼──┼──┼──┼──┤
4│  │  │  │△△│  │  │  │
 ├──┼──┼──┼──┼──┼──┼──┤
5│  │  │░░│  │░░│  │  │
 ├──┼──┼──┼──┼──┼──┼──┤
6│P2│P2│  │  │  │P1│P1│
 ├──┼──┼──┼──┼──┼──┼──┤
7│P2│P2│  │  │  │P1│P1│
 └──┴──┴──┴──┴──┴──┴──┘

Center Hex: D4 (Elevated +1)
Rubble Hexes: C3, E3, C5, E5
```

**Deployment Zones**:
- **Player 1**: Any hex in rows 1-2, columns A-B
- **Player 2**: Any hex in rows 6-7, columns F-G

---

### Victory Conditions

**Primary**: Disable enemy Casket (reduce to 0 cards in hand AND deck)

**Alternate**: First to 10 Victory Points (VP)
- Kill enemy Casket: 10 VP (instant win)
- Deal 5+ damage in one attack: 1 VP
- Control center hex (D4) for 2 consecutive turns: 2 VP
- End turn with 0 Heat: 1 VP

**Time Limit**: 10 rounds. If time expires, highest VP wins (ties = draw).

---

### Recommended Builds

**Player 1 - Scout "First Timer"**:
- Right Arm: Swiftstrike Dagger (3 cards)
- Left Arm: Ironwall Buckler (3 cards)
- Relic: Drake's Wing Jump Jets (3 cards)
- Universal: 10 cards
- **Total**: 19 cards (add +3 more equipment or use different dagger)

**Suggested Fix**: Add second dagger to Left Arm (dual wield)
- Right Arm: Swiftstrike Dagger (3 cards)
- Left Arm: Swiftstrike Dagger (3 cards, DUPLICATES!)
- Relic: Jump Jets (3 cards)
- **Total**: 10 + 3 + 3 + 3 = 19 cards (still light—add 1 more relic)

**Final Build**:
- Dual Daggers: 6 cards (with duplicates)
- Jump Jets: 3 cards
- Emergency Vents: 3 cards
- Universal: 10 cards
- **Total**: 22 cards ✓

---

**Player 2 - Heavy "Tank"**:
- Right Arm: Anvilfall Warhammer (4 cards)
- Left Arm: Stalwart Tower Shield (3 cards)
- Relic 1: Ablative Plating (3 cards)
- Relic 2: Emergency Vents (3 cards)
- Relic 3: Repair Kit (3 cards)
- Universal: 10 cards
- **Total**: 26 cards ✓

---

### Special Rules

**Tutorial Mode**:
- First 2 rounds: No Danger Zone allowed (practice Safe Zone SP management)
- Round 3+: Danger Zone unlocked

**Highlight Mechanics**:
- **Facing**: Scout tries rear attacks for +2 damage
- **Terrain**: Heavy claims center elevated hex for +1 Defense
- **Heat Management**: Scout generates Heat with Jump Jets
- **Reactive Defense**: Heavy uses Shield Wall and Unyielding Bulwark

---

### Suggested Play Flow

**Round 1**: Players deploy, move toward center
**Round 2**: Scout reaches center first (5 SP mobility), Heavy advances slowly
**Round 3**: Scout attacks from range (daggers are melee—must close!), Heavy counter-attacks
**Round 4-6**: Scout tries flanking (rear attacks), Heavy turtles on elevated hex
**Round 7-10**: Attrition battle. Scout's speed vs Heavy's durability.

---

### Learning Goals

**By end of scenario, players should understand**:
1. ✓ SP economy (Safe Zone vs Danger Zone)
2. ✓ Initiative and turn order
3. ✓ Melee vs Ranged attacks
4. ✓ Facing and rear attacks (+2 damage)
5. ✓ Terrain benefits (elevation, rubble)
6. ✓ Heat management (Jump Jets generate Heat, Vents remove it)
7. ✓ Reactive defense cards (Bulwark, Shield Wall)
8. ✓ Deck-as-health (damage = discard cards)

---

## Scenario 2: King of the Hill (1v1 Objective)

**Type**: Arena PvP (Objective-based)
**Players**: 2
**Duration**: 30-45 minutes
**Difficulty**: Intermediate

---

### Setup

**Board Size**: 9x9 hex grid

**Terrain**:
```
   A  B  C  D  E  F  G  H  I
 ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
1│P1│P1│  │▓▓│  │▓▓│  │P2│P2│
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
2│P1│P1│░░│  │  │  │░░│P2│P2│
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
3│  │  │  │▒▒│  │▒▒│  │  │  │
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
4│▓▓│  │▒▒│  │△△│  │▒▒│  │▓▓│
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
5│  │  │  │△△│★★│△△│  │  │  │  ★★ = Objective (Hill)
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤  Elevation +2
6│▓▓│  │▒▒│  │△△│  │▒▒│  │▓▓│
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
7│  │  │  │▒▒│  │▒▒│  │  │  │
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
8│P2│P2│░░│  │  │  │░░│P1│P1│
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┤
9│P2│P2│  │▓▓│  │▓▓│  │P1│P1│
 └──┴──┴──┴──┴──┴──┴──┴──┴──┘

Objective: E5 (Elevated +2, "The Hill")
Elevated Ring: D4, F4, D5, F5, D6, F6 (Elevation +1)
Partial Cover: D3, F3, C4, G4, C6, G6, D7, F7
Rubble: C2, G2, C8, G8
Walls: D1, F1, A4, I4, A6, I6, D9, F9
```

---

### Victory Conditions

**Primary**: Control the Hill (E5) for **3 consecutive turns** (instant win)

**Secondary**: First to 15 Victory Points
- Control Hill for 1 turn: 2 VP
- Disable enemy Casket: 10 VP
- Deal 7+ damage in one attack: 2 VP
- Knock enemy off the Hill: 3 VP

**Time Limit**: 12 rounds. Highest VP wins.

---

### Special Rules

**The Hill (E5)**:
- Elevation +2 (costs 2 SP to climb from ground level)
- **While on Hill**: +2 Defense, +1 to all ranged attacks
- **Only 1 Casket can occupy the Hill hex**

**Knockback**:
- Shield Bash, certain attacks can push enemies
- If knocked off Hill, lose control (VP clock resets)

---

### Recommended Builds

**Build 1 - Scout "Hill Runner"**:
- Longsword + Buckler + Jump Jets + Vents
- **Strategy**: Jump to Hill (ignore climb cost), defend with speed
- **Risk**: Low HP, will be primaried

**Build 2 - Heavy "Fortress"**:
- Warhammer + Tower Shield + Ablative Plating + Vents + Repair Kit
- **Strategy**: Claim Hill, turtle, outlast
- **Risk**: Slow to get there, vulnerable to flanking

**Balanced Option - Support "Controller"**:
- Longsword + Tower Shield + Repair Kit + Smoke Launchers
- **Strategy**: Claim Hill, heal self, drop smoke to block ranged attacks

---

### Tactical Notes

**Elevation Stacking**:
- Ground → +1 Ring (+1 SP)
- +1 Ring → Hill (+1 SP)
- **Total from ground: 2 SP to reach Hill**

**Defensive Positioning**:
- Stand on Hill = +2 Defense
- Partial Cover ring at +1 elevation = +1 Defense
- **Total**: +3 Defense (nearly immune to basic attacks)

**Offensive Positioning**:
- Shoot from Hill = +1 to hit, +2 elevation bonus
- Target below at ground level = additional +1 to hit
- **Very hard to miss**

---

## Scenario 3: Gauntlet Run (Solo/Co-op)

**Type**: Campaign/Solo
**Players**: 1 (or 2 co-op)
**Duration**: 30-45 minutes
**Difficulty**: Hard

---

### Setup

**Board Size**: 12 hexes long x 5 hexes wide (linear gauntlet)

**Terrain**:
```
START                              EXIT
  1  2  3  4  5  6  7  8  9 10 11 12
 ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
A│P1│  │░░│▓▓│  │🔥│  │▓▓│░░│  │  │  │  🔥 = Fire Hazard
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤  ▓▓ = Impassable
B│  │▒▒│  │  │▒▒│  │▒▒│  │  │▒▒│  │🏁│  ░░ = Difficult
 ├──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┼──┤  ▒▒ = Partial Cover
C│P1│  │░░│▓▓│  │🔥│  │▓▓│░░│  │  │  │  🏁 = Exit
 └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘

Deploy: A1 or C1
Exit: B12 (must reach this hex)
Fire Hazards: A6, C6
```

---

### Victory Conditions

**Primary**: Reach Exit hex (B12) with at least 10 cards remaining in deck+hand

**Secondary Objectives** (bonus rewards):
- Reach Exit in under 8 turns: +50 Credits
- Take less than 5 damage total: +30 Credits
- Never enter Danger Zone: +20 Credits

**Failure**: Reduced to 0 cards before reaching Exit

---

### Enemies (AI)

**3 Stationary Turrets** (automated defenses):
- **Turret 1**: Hex B4 (shoots at anyone in hexes 3-5)
- **Turret 2**: Hex B7 (shoots at anyone in hexes 6-8)
- **Turret 3**: Hex B10 (shoots at anyone in hexes 9-11)

**Turret Stats**:
- HP: 8
- Attack: 3 damage, Medium range, auto-hit (1 attack per round at closest target in range)
- Defense: 2
- Cannot move

**Turret Activation**:
- At end of each round, each Turret attacks closest Casket in range
- If multiple targets equidistant, attacks randomly

---

### Special Rules

**Time Pressure**:
- Each round, Fire spreads 1 hex toward starting zone (hexes become unusable)
- Round 1: Fire at A6, C6
- Round 2: Fire spreads to A5, C5
- Round 3: Fire spreads to A4, C4
- etc.

**Strategy**: Move fast or get burned!

---

### Recommended Build

**Scout "Runner"**:
- Dagger + Buckler + Jump Jets + Vents
- **Plan**: Jump over obstacles, ignore turrets, sprint to Exit
- **Challenge**: Can you avoid all damage?

**Heavy "Brawler"**:
- Warhammer + Tower Shield + Ablative Plating + Vents
- **Plan**: Smash through Turrets, tank damage, walk to Exit
- **Challenge**: Can you reach Exit before Fire catches you?

---

### Solo Campaign Variant

**Use this as Mission 1** of a campaign:

**Rewards**:
- Victory: 100 Credits
- Secondary objectives: +20-50 Credits each
- **Total possible**: 200 Credits

**Use Credits to buy new equipment** before next mission (see [equipment-catalog.md](equipment-catalog.md))

---

## Scenario 4: Duel at Dawn (Honorable 1v1)

**Type**: Arena PvP (Honor Rules)
**Players**: 2
**Duration**: 15-30 minutes
**Difficulty**: Intermediate

---

### Setup

**Board Size**: 5x5 hex grid (small, intense)

**Terrain**:
```
   A  B  C  D  E
 ┌──┬──┬──┬──┬──┐
1│P1│  │  │  │P2│  P1/P2 = Deployment (corners)
 ├──┼──┼──┼──┼──┤  No terrain (flat arena)
2│  │  │  │  │  │
 ├──┼──┼──┼──┼──┤
3│  │  │★ │  │  │  ★ = Center Hex
 ├──┼──┼──┼──┼──┤
4│  │  │  │  │  │
 ├──┼──┼──┼──┼──┤
5│P2│  │  │  │P1│
 └──┴──┴──┴──┴──┘

Deploy: P1 = A1, P2 = E1 (or swap)
Center: C3
```

---

### Victory Conditions

**Primary**: Disable enemy Casket

**Honor Rules** (optional but encouraged):
- No attacking until Round 2 (Round 1 = positioning only)
- No rear attacks (fight face-to-face, honor duel)
- No Danger Zone (stay in Safe Zone limits)

**Breaking Honor**: If you break any Honor Rule, opponent gains +2 SP for rest of mission

---

### Special Rules

**Sudden Death**: If both Caskets survive 8 rounds, both enter **Berserk Mode**:
- +1 damage on all attacks
- +2 SP Safe Zone
- Must attack if able (cannot pass without attacking)

**First Blood**: First Casket to deal damage gains +1 initiative for rest of match

---

### Recommended Builds

**Equal Weight Classes** (for fairness):
- Both players use Scout OR both use Heavy
- Both start with same equipment budget (200 Credits)

**Example**: Both use Longsword + Shield + 1 Relic of choice

---

## Quick Reference: Scenario Difficulty

| Scenario | Difficulty | Best For | Duration |
|----------|------------|----------|----------|
| First Blood | Beginner | Learning rules | 20-30 min |
| King of the Hill | Intermediate | Objectives practice | 30-45 min |
| Gauntlet Run | Hard | Solo/Campaign | 30-45 min |
| Duel at Dawn | Intermediate | Quick matches | 15-30 min |

---

## Scenario Creation Guidelines

**For your own scenarios**:

1. **Define Win Condition** (kill, objectives, VP, survival)
2. **Set Board Size** (7x7 standard, 9x9 large, 5x5 small)
3. **Place Terrain** (cover, elevation, hazards)
4. **Add Special Rules** (time limits, environmental effects)
5. **Balance Deployment** (equal distance to objectives)

---

## Next Steps

- See [combat-resolution.md](combat-resolution.md) for attack rules
- See [terrain-rules.md](terrain-rules.md) for terrain details
- See [deck-construction.md](deck-construction.md) for building decks

---

*"The arena awaits. Prove your worth in blood and steel."*
