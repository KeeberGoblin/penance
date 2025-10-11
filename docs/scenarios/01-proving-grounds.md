# ARENA SCENARIO #1: THE PROVING GROUNDS

**Type**: 1v1 Deathmatch
**Factions**: Church of Absolution vs Dwarven Clans
**Estimated Playtime**: 45-60 minutes
**Difficulty**: Beginner-friendly (tests core mechanics)
**Victory Condition**: Reduce opponent to 0 HP OR force 4+ reshuffles

---

## SCENARIO SETUP

### Map: The Proving Grounds (12×12 Hexes)

```
     [F ][F ][  ][  ][  ][  ][  ][  ][  ][  ][F ][F ]
    [F ][F ][R ][  ][  ][  ][  ][  ][  ][R ][F ][F ]
   [  ][R ][R ][  ][  ][W ][W ][  ][  ][R ][R ][  ]
  [  ][  ][  ][  ][W ][W ][W ][W ][  ][  ][  ][  ]
 [  ][  ][  ][W ][W ][E1][E1][W ][W ][  ][  ][  ]
[  ][  ][W ][W ][E1][  ][  ][E1][W ][W ][  ][  ]
[  ][  ][W ][W ][E2][  ][  ][E2][W ][W ][  ][  ]
 [  ][  ][  ][W ][W ][E2][E2][W ][W ][  ][  ][  ]
  [  ][  ][  ][  ][W ][W ][W ][W ][  ][  ][  ][  ]
   [  ][R ][R ][  ][  ][W ][W ][  ][  ][R ][R ][  ]
    [F ][F ][R ][  ][  ][  ][  ][  ][  ][R ][F ][F ]
     [F ][F ][  ][  ][  ][  ][  ][  ][  ][  ][F ][F ]
```

### Terrain Legend

**[F] - Forest** (8 hexes)
- **Effect**: +1 Defense when standing in this hex
- **Movement**: Normal (1 SP per hex)
- **LOS**: Blocks LOS through multiple forest hexes

**[R] - Rubble** (8 hexes)
- **Effect**: +1 Defense when standing in this hex
- **Movement**: Difficult Terrain (2 SP per hex)
- **LOS**: Does not block LOS

**[W] - Water/Mud** (20 hexes)
- **Effect**: No defensive bonus
- **Movement**: Difficult Terrain (2 SP per hex)
- **LOS**: Does not block LOS
- **Special**: If you end turn in Water, remove 1 Heat

**[E1] - Elevation 1** (4 hexes, ring 1)
- **Effect**: +1 damage to attacks FROM this hex
- **Effect**: Ignore cover when attacking FROM this hex
- **Movement**: Costs 2 SP to enter from lower elevation
- **LOS**: Can see over non-elevated terrain

**[E2] - Elevation 2** (4 hexes, ring 2)
- **Effect**: +2 damage to attacks FROM this hex
- **Effect**: Ignore cover when attacking FROM this hex
- **Movement**: Costs 3 SP to enter from Elevation 1, 5 SP from ground
- **LOS**: Can see over all terrain except Elevation 2
- **Special**: Attacks FROM Elevation 2 gain +1 Range

**[  ] - Clear Ground** (All other hexes)
- **Effect**: No modifiers
- **Movement**: Normal (1 SP per hex)

---

## DEPLOYMENT

### Church of Absolution Deployment Zone
**Hexes**: Top-left quadrant (rows 1-3, columns 1-3)
```
  [F ][F ][  ]
 [F ][F ][R ]
[  ][R ][R ]
```
**Starting Position**: Player chooses any hex in this zone
**Facing**: Player chooses initial facing

### Dwarven Clans Deployment Zone
**Hexes**: Bottom-right quadrant (rows 10-12, columns 10-12)
```
       [R ][R ][  ]
        [R ][F ][F ]
         [  ][F ][F ]
```
**Starting Position**: Player chooses any hex in this zone
**Facing**: Player chooses initial facing

### Deployment Order
1. **Roll 1d6**: Higher roll chooses who deploys first
2. **First player**: Places Casket in their deployment zone
3. **Second player**: Places Casket in their deployment zone
4. **First player begins** Turn 1

---

## PRE-BUILT DECKS

### CHURCH DECK: "MARTYR'S FURY"

**Casket Class**: Assault (Medium Frame - 5 SP)

**Build**:
- 10 Universal Core (mandatory)
- 6 Church Faction Core (mandatory)
- Equipment: Longsword (6 cards) + Buckler Shield (2 cards) + Martyr's Brand Sigil (3 cards) = 11 cards
- 2 Tactics: Righteous Fury + Blood Pact

**Total**: 29 cards (10 Universal + 6 Faction + 11 Equipment + 2 Tactics)

**Deck Composition**:

**Universal Core (10 cards)**:
1. Move ×3 (1 SP, Move 2 hexes)
2. Sprint ×2 (2 SP, Move 4 hexes, +1 Heat)
3. Brace ×2 (1 SP, +2 Defense until next turn)
4. Disengage ×1 (1 SP, Move 2 hexes, ignore attacks of opportunity)
5. Focus ×1 (0 SP, Draw 1 card)
6. Emergency Repair ×1 (3 SP, Recover 3 cards from discard)

**Church Faction Core (6 cards)**:
7. Blood Offering ×1 (0 SP, Discard 2 cards, next attack +3 damage)
8. Martyrdom Protocol ×1 (2 SP, Redirect damage from ally to yourself)
9. Righteous Fury ×1 (Passive, +1 damage per enemy killed - permanent)
10. Divine Judgment ×1 (4 SP, Deal 8 damage, ignore Defense)
11. Consecrated Ground ×1 (3 SP, Create 3-hex zone, allies heal 1 card/turn)
12. Last Rites ×1 (0 SP, When reduced to 0 HP, deal 10 damage to killer)

**Equipment - Longsword (6 cards)**:
13. Slash ×2 (2 SP, Melee, Deal 4 damage)
14. Thrust ×1 (2 SP, Melee, Deal 3 damage, +2 if attacking front arc)
15. Parry ×1 (0 SP, Reactive, Reduce damage by 2, next attack +1 damage)
16. Riposte ×1 (1 SP, Reactive, When attacked in melee, deal 3 damage to attacker)
17. Guard Stance ×1 (2 SP, Defense, +2 Defense until next turn)

**Equipment - Buckler Shield (2 cards)**:
18. Deflect ×1 (1 SP, Reactive, Reduce damage by 2)
19. Shield Bash ×1 (2 SP, Melee, Deal 2 damage, push 1 hex)

**Equipment - Martyr's Brand Sigil (3 cards - Church-Exclusive)**:
20. Martyr's Blessing ×1 (Passive, When you discard cards via Blood Offering, gain +1 Defense until next turn)
21. Sacred Wound ×1 (2 SP, Self-harm: discard 1 card, all allies gain +1 damage this turn)
22. Zealot's Fervor ×1 (Passive, When below 15 HP, all attacks deal +1 damage)

**Tactics (2 cards)**:
23. Righteous Fury Tactic ×1 (0 SP, Once per game: Next attack deals double damage)
24. Blood Pact ×1 (0 SP, Discard 3 cards, recover 3 ally cards)

**Opening Hand** (6 cards, drawn randomly):
- Shuffle deck, draw top 6 cards

**Playstyle**:
- Aggressive martyr striker
- Use Blood Offering for burst damage (+3 dmg at cost of 2 HP)
- Longsword provides versatile melee options
- Buckler Shield gives reactive defense without slowing movement
- Martyr's Brand Sigil rewards self-harm with defensive buffs
- Scales with component destruction (Righteous Fury passive)

**Win Condition**: Burst opponent down with Blood Offering combos before death spiral begins

---

### DWARVEN DECK: "IMMOVABLE WALL"

**Casket Class**: Heavy (Heavy Frame - 4 SP)

**Build**:
- 10 Universal Core (mandatory)
- 6 Dwarven Faction Core (mandatory)
- Equipment: Warhammer (6 cards) + Tower Shield (4 cards) + Forge-Rune Sigil (3 cards) = 13 cards
- 2 Tactics: Stone Endurance + Runic Overcharge
- **Stone Endurance Bonus**: +2 Universal Core cards (32 total HP)

**Total**: 33 cards (12 Universal + 6 Faction + 13 Equipment + 2 Tactics)

**Deck Composition**:

**Universal Core (12 cards - includes Stone Endurance bonus)**:
1. Move ×4 (1 SP, Move 2 hexes) - +1 extra from Stone Endurance
2. Sprint ×3 (2 SP, Move 4 hexes, +1 Heat) - +1 extra from Stone Endurance
3. Brace ×2 (1 SP, +2 Defense until next turn)
4. Disengage ×1 (1 SP, Move 2 hexes, ignore attacks of opportunity)
5. Focus ×1 (0 SP, Draw 1 card)
6. Emergency Repair ×1 (3 SP, Recover 3 cards from discard)

**Dwarven Faction Core (6 cards)**:
7. Crushing Blow ×1 (2 SP, Melee, Deal 4 damage, ARMOR PIERCING - ignore all Defense)
8. Forge Fury ×1 (2 SP, Convert all Heat to damage, deal X damage where X = current Heat)
9. Rune of Protection ×1 (2 SP, Gain 1 Rune Counter, reduce damage by 1 per counter - max 3, lasts until end of mission)
10. Unbreakable ×1 (1 SP, Reactive, Reduce damage by 3)
11. Earthshaker ×1 (3 SP, Melee AOE, Deal 3 damage to all adjacent enemies, push 1 hex)
12. Clan Vengeance ×1 (Passive, +2 damage per Component Damage taken - permanent)

**Equipment - Warhammer (6 cards)**:
13. Hammer Strike ×2 (2 SP, Melee, Deal 5 damage)
14. Overhead Smash ×1 (3 SP, Melee, Deal 7 damage, +1 Heat)
15. Hammer Block ×1 (1 SP, Reactive, Reduce damage by 2, next attack +2 damage)
16. Pommel Bash ×1 (1 SP, Melee, Deal 3 damage, target loses 1 SP next turn)
17. Crushing Sweep ×1 (2 SP, Melee, Deal 4 damage to target + 2 damage to 1 adjacent enemy)

**Equipment - Tower Shield (4 cards)**:
18. Shield Wall ×1 (2 SP, +4 Defense until next turn, cannot move)
19. Tower Defense ×1 (1 SP, Reactive, Reduce damage by 3)
20. Shield Advance ×1 (2 SP, Move 2 hexes, gain +2 Defense this turn)
21. Bulwark Stance ×1 (1 SP, +2 Defense until next turn)

**Equipment - Forge-Rune Sigil (3 cards - Dwarven-Exclusive)**:
22. Runic Regeneration ×1 (Passive, When you gain a Rune Counter, recover 1 card from discard)
23. Forge Heat ×1 (1 SP, Gain 2 Heat, +1 damage to next attack)
24. Rune of Endurance ×1 (Passive, Max Rune Counters increased from 3 to 4)

**Tactics (2 cards)**:
25. Stone Endurance ×1 (Passive, +2 Universal Core cards, deck starts at 33 cards instead of 31)
26. Runic Overcharge ×1 (2 SP, Once per game: Gain 3 Rune Counters immediately)

**Opening Hand** (6 cards, drawn randomly):
- Shuffle deck, draw top 6 cards

**Playstyle**:
- Defensive fortress tank
- Stack Rune Counters (Rune of Protection + Runic Overcharge = 4 counters with Rune of Endurance)
- Use Tower Shield + Rune Counters for massive damage reduction (-7 total)
- Crushing Blow ignores all Defense (counters Church's defensive buffs)
- 33 HP deck (Stone Endurance) = superior durability
- Outlast opponent through attrition

**Win Condition**: Survive until opponent's death spiral (4+ Damage cards) collapses their deck

---

## TURN STRUCTURE REMINDER

### 4 Phases Per Turn

#### PHASE 1: REFRESH
1. Restore SP to maximum
   - Church: 5 SP (Medium Frame)
   - Dwarves: 5 SP (Medium Frame)
2. If Heat 5+: Roll Strain (1d6 + current Heat)
   - 1-5: +1 Heat
   - 6-8: -1 SP this turn
   - 9-11: Take 2 damage
   - 12+: Component malfunction (lose 1 random card type for turn)

#### PHASE 2: ACTION PHASE
- Play cards from hand (costs SP)
- Move (1 SP per hex, 2 SP for difficult terrain)
- Continue until out of SP or pass turn

#### PHASE 3: DRAW PHASE
1. Draw cards until hand size = 6
2. If deck is empty:
   - Shuffle discard pile
   - Add 1 "Damage" card (blank, dead draw)
   - This is your new deck

#### PHASE 4: END TURN
- Resolve end-of-turn effects
- Remove temporary buffs (e.g., Shield Wall)
- Opponent begins their turn

---

## COMBAT RESOLUTION

### Attack Steps
1. **Declare attack**: Play attack card, spend SP
2. **Check range**: Is target in range?
   - Melee: 1 hex
   - Close: 2-3 hexes
   - Medium: 4-6 hexes
   - Long: 7+ hexes
3. **Check LOS**: Can you see target? (forest blocks LOS)
4. **Calculate damage**:
   - Base damage (from card)
   - + Facing modifier (Rear +2, Side +1, Front +0)
   - + Elevation modifier (E1 +1, E2 +2)
   - - Defense modifiers (cover, buffs)
5. **Apply damage**: Defender discards X cards from top of deck

### Damage Example
Church plays **Faithful Thrust** (4 damage, Melee) against Dwarven Casket:
- Church is attacking from **Rear arc**: +2 damage
- Church is on **Elevation 1**: +1 damage
- Dwarf has **1 Rune Counter**: -1 damage
- Total: 4 + 2 + 1 - 1 = **6 damage**
- Dwarf discards top 6 cards from deck

### Component Damage
When you discard cards from damage:
1. Count how many **Primary Weapon cards** were discarded
2. Each Primary Weapon card = 1 **Component Damage**
3. Track Component Damage by location:
   - Arms (weapon systems)
   - Legs (movement systems)
   - Head (sensors)
   - Chassis (core systems)
4. When **3 Component Damage** to same location = **Component Destroyed**

#### Component Destruction Effects
- **Right Arm Destroyed**: Lose all Primary Weapon cards from hand (discard them)
- **Left Arm Destroyed**: Lose all Secondary Equipment cards from hand
- **Legs Destroyed**: Movement costs +1 SP per hex
- **Head Destroyed**: -1 damage to ranged attacks, no sensor abilities
- **Chassis Destroyed**: -1 SP maximum permanently

---

## VICTORY CONDITIONS

### Primary Victory: Reduce Opponent to 0 HP
When opponent's deck is empty AND they cannot reshuffle (discard pile also empty), they are defeated.

### Secondary Victory: Death Spiral (4+ Reshuffles)
After 4 reshuffles, opponent's deck contains:
- 26 real cards
- 4 Damage cards (13% of deck is dead draws)

At this point, most players concede. You can declare victory if opponent agrees.

### Tertiary Victory: Concession
Either player may concede at any time.

---

## SCENARIO OBJECTIVES (Optional Victory Points)

These are OPTIONAL goals for learning/practice. Not required for victory.

### Church Objectives
- [ ] **Aggressive Martyr**: Deal 20+ damage in a single turn using Blood Offering combo
- [ ] **Righteous Fury**: Trigger Righteous Fury (+1 dmg per kill) - destroy 1 component
- [ ] **Faithful Execution**: Kill opponent with Divine Judgment (6-8 dmg execute)

### Dwarven Objectives
- [ ] **Immovable Object**: Survive 5+ turns with 3 Rune Counters active
- [ ] **Armor Piercer**: Deal 15+ damage with armor-piercing attacks in one turn
- [ ] **Forge Eruption**: Use Forge Fury with 5+ Heat (8+ damage total)

---

## SPECIAL RULES FOR THIS SCENARIO

### 1. Simplified Component Damage
For beginner learning, track Component Damage as a **single pool** (not by location).
- 3 Component Damage total = Destroy **1 random component** (roll 1d4: 1=Arms, 2=Legs, 3=Head, 4=Chassis)

Advanced players should track by location.

### 2. No Pilot Wounds (Optional)
For faster learning games, ignore Pilot Wound Decks.
- Casket destruction = immediate defeat
- No capsule breach, no neural feedback

Once comfortable, add Pilot Wounds for full brutality.

### 3. Terrain Interaction Encouraged
The map is designed to teach terrain usage:
- **Forest corners**: Defensive positions (+1 Defense)
- **Central elevation**: High-risk, high-reward positioning (+2 dmg)
- **Water/Mud ring**: Heat management and mobility challenge
- **Rubble lines**: Cover without mobility penalty

Players should experiment with terrain advantages.

---

## EXPECTED GAME FLOW

### Turns 1-3: Positioning
- Both players navigate terrain toward center
- Church moves faster (Desperate Lunge, Overextend)
- Dwarves set up defensive buffs (Rune of Protection)
- Minimal damage, mostly movement and setup

### Turns 4-6: First Engagement
- Church closes to Melee range
- Dwarves activate Shield Wall
- First attacks land (4-6 damage each)
- Heat begins building (especially Dwarves)
- First Component Damage tracked

### Turns 7-10: Brutal Exchange
- Both sides trading heavy blows
- Church using Blood Offering for burst (discard 2 cards for +3 dmg)
- Dwarves stacking Rune Counters (reducing damage)
- First reshuffle likely (add 1 Damage card)
- Heat Strain checks begin (5+ Heat)

### Turns 11-15: Death Spiral
- Decks contain Damage cards (dead draws)
- Component destruction occurs (3+ Component Damage)
- Players desperate, using ultimate cards (Hammerfall, Divine Judgment)
- One side collapses

### Expected Winner
**51/49 Church favor** - slightly more aggressive, can burst down Dwarves before attrition matters.

However, if Dwarves survive to Turn 12+, attrition favors them (32 HP vs 30 HP).

---

## LEARNING OBJECTIVES

This scenario teaches:
1. **SP economy**: When to spend, when to save
2. **Heat management**: Risk/reward of high-Heat cards
3. **Deck cycling**: When to reshuffle, when to delay
4. **Component damage**: Tracking and destruction effects
5. **Facing modifiers**: Importance of positioning (rear arc +2 dmg)
6. **Terrain usage**: Cover, elevation, difficult terrain
7. **Reactive cards**: 0 SP interrupts (Brace for Impact, Unbreakable)
8. **Death spiral**: How Damage cards accumulate

After playing this scenario 2-3 times, players should understand all core mechanics.

---

## POST-GAME DEBRIEF

### Questions to Consider
1. When did you feel most powerful? Most vulnerable?
2. How many reshuffles occurred? (Track Damage card accumulation)
3. Did Component Destruction happen? Which component?
4. How did terrain affect positioning choices?
5. Did Heat Strain matter? (5+ Heat rolls)
6. Which cards felt most/least useful?

### Balance Observations
- Did armor-piercing (Dwarven Crushing Blow) feel oppressive?
- Did Church's burst damage (Blood Offering) feel fair?
- Did 32 HP (Stone Endurance) make Dwarves too tanky?
- Did Reactive cards (0 SP) disrupt gameplay positively or negatively?

### Suggested Variations
- **Swap Tactics**: Try different Tactic combinations
- **Swap Secondary**: Church uses Tower Shield, Dwarves use Siege Cannon
- **Full Pilot Wounds**: Add Pilot Wound Decks for maximum brutality
- **Component Tracking**: Track Component Damage by specific location

---

## MAP STRATEGY GUIDE

### For Church (Aggressive Striker)
1. **Opening**: Deploy in Forest hex (top-left) for initial cover
2. **Turn 1-2**: Rush toward center elevation using Desperate Lunge + Overextend
3. **Turn 3**: Reach Elevation 1 (E1), use Quick Shot to harass
4. **Turn 4+**: Close to Melee, attack from elevated rear arc (4 base + 2 rear + 1 elevation = 7 dmg)
5. **Heat**: Use Water hexes to cool down if overheating
6. **Win**: Burst damage from favorable position before Dwarves stabilize

**Key Hexes**: Elevation 1 (center ring), Forest corners (fallback)

### For Dwarves (Defensive Anchor)
1. **Opening**: Deploy in Rubble hex (bottom-right) for +1 Defense
2. **Turn 1-2**: Advance slowly, play Rune of Protection (stack counters)
3. **Turn 3**: Activate Shield Wall, position near Water (Heat management)
4. **Turn 4+**: Let Church come to you, counter-attack with Crushing Blow
5. **Heat**: High Heat generation, use Water hexes frequently
6. **Win**: Outlast Church through superior HP and damage reduction

**Key Hexes**: Rubble (defensive positions), Water (Heat cooling), Elevation 2 (if safe)

---

## QUICK REFERENCE

### Movement Costs
- Clear Ground: 1 SP per hex
- Difficult Terrain (Water/Rubble): 2 SP per hex
- Entering Elevation 1: 2 SP
- Entering Elevation 2: 3 SP (from E1), 5 SP (from ground)

### Damage Modifiers
- Rear Arc: +2 dmg (attacker), -2 Defense (defender)
- Side Arc: +1 dmg (attacker), -1 Defense (defender)
- Front Arc: +0 dmg (attacker), Full Defense (defender)
- Elevation 1: +1 dmg from this hex
- Elevation 2: +2 dmg from this hex
- Cover (Forest/Rubble): +1 Defense when standing in hex

### Heat Strain Table (Roll at 5+ Heat)
| 1d6 + Heat | Effect |
|------------|--------|
| 1-5 | +1 Heat |
| 6-8 | -1 SP this turn |
| 9-11 | Take 2 damage |
| 12+ | Component malfunction |

### Component Destruction Effects
| Component | Effect |
|-----------|--------|
| Right Arm | Lose Primary Weapon cards from hand |
| Left Arm | Lose Secondary Equipment cards from hand |
| Legs | Movement +1 SP per hex |
| Head | -1 dmg to ranged attacks |
| Chassis | -1 SP maximum |

---

## SETUP CHECKLIST

Before starting:
- [ ] Print Quick Reference Sheet
- [ ] Print or draw 12×12 hex map
- [ ] Prepare Church deck (30 cards shuffled)
- [ ] Prepare Dwarven deck (32 cards shuffled)
- [ ] Prepare 2d6 for Strain checks
- [ ] Prepare tokens for:
  - Heat tracking (0-10+)
  - SP tracking (current SP)
  - Rune Counters (Dwarves)
  - Component Damage markers
  - Facing indicator (arrow or die)
- [ ] Prepare paper for tracking:
  - Current HP (cards remaining in deck)
  - Damage cards in deck (reshuffle count)
  - Component Damage by location (optional)

---

**STATUS**: PLAYTEST READY
**NEXT STEP**: Example of Play (4-5 turn walkthrough)
**ESTIMATED TIME**: 45-60 minutes first game, 30-45 minutes experienced players
