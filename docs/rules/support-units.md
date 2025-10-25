# Support Units System
## Penance: Absolution Through Steel

**Version**: 3.0 (Pilot Grit Integration)
**Date**: October 14, 2025

Support units are AI-controlled allies that accompany your Casket into battle. These units follow simple behavior cards and can be influenced by your Casket's command abilities.

> **v3.0 OPTIONAL**: Support units gain +1 Morale when commanded by pilots with **Grit 2+**. Veterans inspire confidence. High-Grit pilots' Rally and Command actions are more effective (see [pilot-grit-system.md](../campaigns/pilot-grit-system.md) for details).

---

## Core Concept

**Support Units are NOT controlled directly.** Instead:
- They have a **Behavior Deck** (4-6 cards) that determines their actions
- Each unit type has unique behaviors and specializations
- Players can influence them with **Command cards** and **Rally actions**
- They activate AFTER all Caskets have taken their turns

---

## Support Unit Anatomy

Each support unit has:

### Stats
- **HP**: 5-15 (track with tokens, NOT a deck)
- **Movement**: 2-4 hexes per turn
- **Defense**: 0-2
- **Type**: Infantry, Artillery, Scout, Engineer, Mystic

### Behavior Deck (4-6 Cards)
A small deck of AI behavior cards that determine what the unit does each turn. Shuffle at start of battle, draw 1 per turn, execute action.

### Command Response
How the unit reacts when given a Command by a Casket.

---

## How Support Units Work

### Deployment
- **During Setup**: Deploy support unit within 3 hexes of your Casket
- **Cost**: Varies by unit type (2-4 Equipment Slots when building deck)
- **Limit**: 1 support unit per Casket maximum

### Activation
1. **All Caskets take their turns first**
2. **Support Unit Phase**: Draw 1 Behavior card
3. **Execute Behavior**: Follow card instructions (move, attack, etc.)
4. **Discard Behavior card**: Reshuffles when deck empty

### Command Actions
Casket players can spend SP to influence support units:
- **RALLY** (1 SP): Move support unit up to 3 hexes
- **COMMAND: ATTACK** (2 SP): Support unit attacks target you choose
- **COMMAND: DEFEND** (1 SP): Support unit gains +2 Defense until next turn
- **COMMAND: HOLD** (0 SP): Support unit skips its behavior this turn (stays put)

---

## SUPPORT UNIT TYPES

---

## 1. PENITENT SQUAD (Infantry)
**Category**: Infantry Support
**Faction**: Church of Absolution
**HP**: 8 | **Movement**: 3 | **Defense**: 1
**Equipment Slots**: 2

### Description
Zealous infantry squad armed with sanctified blades and fanatical devotion. They charge into melee and fight until death.

### Behavior Deck (5 Cards)

#### CHARGE FORWARD
- **Action**: Move toward nearest enemy. If adjacent, attack for 3 damage.
- **Priority**: High

#### SURROUND ENEMY
- **Action**: Move to flank nearest enemy (try to position in rear arc). If already flanking, attack for 4 damage.
- **Priority**: Medium

#### PROTECT THE CASKET
- **Action**: If Casket within 4 hexes is under 15 HP, move toward Casket. Attack any enemy adjacent to Casket for 3 damage.
- **Priority**: High

#### DESPERATE STRIKE
- **Action**: If squad HP ≤ 4, move toward nearest enemy and attack for 5 damage (suicidal charge).
- **Priority**: Critical

#### REGROUP
- **Action**: If no enemies within 4 hexes, move toward Casket. Otherwise, attack nearest enemy for 3 damage.
- **Priority**: Low

### Command Response
- **RALLY**: Move up to 3 hexes (ignores behavior)
- **ATTACK**: Attack target for 4 damage (+1 bonus for following orders)
- **DEFEND**: +2 Defense, but cannot attack next turn
- **HOLD**: Stay in place, gain +1 Defense

### Special Ability: MARTYRDOM
If Penitent Squad is destroyed, deal 3 damage to all adjacent enemies (explosive death).

---

## 2. IRONCLAD SENTINEL (Artillery)
**Category**: Artillery Support
**Faction**: Dwarven Forge-Guilds
**HP**: 6 | **Movement**: 2 | **Defense**: 2
**Equipment Slots**: 3

### Description
Mobile artillery platform with a shoulder-mounted siege cannon. Slow but devastating at range.

### Behavior Deck (4 Cards)

#### SIEGE BOMBARDMENT
- **Action**: Attack furthest visible enemy within 8 hexes for 6 damage. Ignore 2 Defense. +1 Heat to self.
- **Priority**: High

#### DEFENSIVE POSITION
- **Action**: If enemy within 3 hexes, move away 2 hexes. Then attack nearest enemy within range for 5 damage.
- **Priority**: High

#### SUPPRESSING FIRE
- **Action**: Attack nearest enemy within 6 hexes for 4 damage. Target cannot move next turn.
- **Priority**: Medium

#### RELOAD
- **Action**: Move 1 hex toward nearest cover. Gain +2 Defense until next turn. Next attack deals +2 damage.
- **Priority**: Low

### Command Response
- **RALLY**: Move up to 2 hexes (slow, heavy unit)
- **ATTACK**: Attack target within 8 hexes for 7 damage (heavy bombardment)
- **DEFEND**: Deploy siege shield (+3 Defense, cannot move next turn)
- **HOLD**: Anchor position, next attack deals +3 damage

### Special Ability: EXPLOSIVE SHELLS
When Ironclad Sentinel attacks, all enemies within 1 hex of target take 2 splash damage.

---

## 3. BONE THRALLS (Swarm Infantry)
**Category**: Swarm Support
**Faction**: The Ossuarium
**HP**: 12 (3 HP per thrall, 4 thralls total) | **Movement**: 4 | **Defense**: 0
**Equipment Slots**: 2

### Description
Four skeletal thralls bound to your will. Individually weak, but they swarm enemies and can be resurrected.

### Behavior Deck (6 Cards)

#### SWARM ATTACK
- **Action**: All thralls move toward nearest enemy. Each thrall adjacent to an enemy attacks for 2 damage (up to 8 damage total if all 4 are adjacent).
- **Priority**: High

#### SCATTER
- **Action**: Each thrall moves in a different direction (spread out around nearest enemy). Attack if adjacent (2 damage per thrall).
- **Priority**: Medium

#### FEAST ON THE FALLEN
- **Action**: If enemy died this round, move toward corpse. Recover 3 HP to swarm (resurrect 1 thrall if any are dead).
- **Priority**: High

#### RECKLESS CHARGE
- **Action**: All thralls move full movement toward nearest enemy. Thralls take 1 damage each, but next attack deals +1 damage per thrall.
- **Priority**: Medium

#### DEFENSIVE CIRCLE
- **Action**: All thralls move adjacent to Casket. Form defensive ring (+1 Defense to Casket until thralls move).
- **Priority**: Low

#### SPLIT ATTACK
- **Action**: Divide thralls between 2 nearest enemies (2 thralls each). Each thrall attacks for 2 damage.
- **Priority**: Medium

### Command Response
- **RALLY**: Move all thralls up to 4 hexes to target location
- **ATTACK**: All thralls focus attack target (2 damage × number of thralls alive)
- **DEFEND**: Thralls form shield wall in front of Casket (block LOS, +1 Defense to Casket)
- **HOLD**: Thralls stay in place, gain +1 Defense each

### Special Ability: RESURRECTION
When thralls are destroyed, place corpse markers. During your Support Unit Phase, if Casket is within 4 hexes of corpse, you may spend 2 SP to resurrect 1 thrall with 3 HP.

---

## 4. VERDANT STALKER (Scout)
**Category**: Scout Support
**Faction**: Elven Verdant Covenant
**HP**: 6 | **Movement**: 5 | **Defense**: 1
**Equipment Slots**: 2

### Description
Elven ranger bonded with your Casket. Fast, mobile, applies Bleed stacks and scouts ahead.

### Behavior Deck (5 Cards)

#### HUNT THE WOUNDED
- **Action**: Move toward enemy with most Bleed counters. Attack for 3 damage + 1 damage per Bleed counter on target (max +5). Apply 1 Bleed.
- **Priority**: High

#### SCOUT AHEAD
- **Action**: Move 5 hexes toward nearest unexplored area or nearest enemy. If adjacent to enemy, attack for 3 damage and apply 1 Bleed.
- **Priority**: Medium

#### HIT AND RUN
- **Action**: Move adjacent to nearest enemy, attack for 3 damage and apply 1 Bleed, then move 3 hexes away.
- **Priority**: High

#### SNIPER SHOT
- **Action**: If no enemy within 3 hexes, attack furthest visible enemy within 6 hexes for 4 damage. Apply 1 Bleed.
- **Priority**: Medium

#### VANISH
- **Action**: If Stalker HP ≤ 3, move 5 hexes away from all enemies. Gain Stealth until next turn (enemies cannot target directly).
- **Priority**: Critical

### Command Response
- **RALLY**: Move up to 5 hexes (very fast)
- **ATTACK**: Attack target for 4 damage and apply 2 Bleed counters
- **DEFEND**: Gain Stealth (cannot be targeted until Stalker attacks)
- **HOLD**: Aim carefully, next attack deals +3 damage

### Special Ability: BLEED MASTERY
All Bleed counters applied by Verdant Stalker last 1 extra turn (ticks 3 times instead of 2).

---

## 5. FORGE GOLEM (Tank)
**Category**: Tank Support
**Faction**: Dwarven Forge-Guilds
**HP**: 15 | **Movement**: 2 | **Defense**: 3
**Equipment Slots**: 4

### Description
Massive animated construct of stone and rune-etched iron. Slow, incredibly durable, draws enemy fire.

### Behavior Deck (4 Cards)

#### TAUNT
- **Action**: Move toward nearest enemy. All enemies within 4 hexes must target Forge Golem next turn if able (taunt effect).
- **Priority**: High

#### CRUSHING SLAM
- **Action**: Attack nearest enemy for 5 damage. Ignore 2 Defense. Target is knocked back 1 hex.
- **Priority**: High

#### DEFENSIVE STANCE
- **Action**: If Golem HP ≤ 8, do not move. Gain +2 Defense until next turn. Counterattack any melee attacker for 3 damage.
- **Priority**: Critical

#### SEISMIC STOMP
- **Action**: Deal 3 damage to all adjacent enemies. Push them 1 hex away. +1 Heat to Golem.
- **Priority**: Medium

### Command Response
- **RALLY**: Move up to 2 hexes (slow but obedient)
- **ATTACK**: Attack target for 7 damage, ignore 3 Defense (massive strike)
- **DEFEND**: Golem becomes immobile, gains +4 Defense, blocks LOS
- **HOLD**: Anchor position, gain Regeneration 2 (recover 2 HP at end of turn)

### Special Ability: RUNIC SHIELDS
When Forge Golem takes damage, roll 1d6. On 5-6, reduce damage by 3 (magical shielding).

---

## 6. WARP FAMILIAR (Mystic)
**Category**: Mystic Support
**Faction**: The Wyrd Conclave
**HP**: 5 | **Movement**: 4 (fly) | **Defense**: 0
**Equipment Slots**: 3

### Description
Fae spirit creature bound to the pilot. Can teleport, phase through terrain, and disrupt enemy actions.

### Behavior Deck (5 Cards)

#### REALITY SHIFT
- **Action**: Teleport to any visible hex within 6 hexes. Deal 3 damage to adjacent enemy.
- **Priority**: Medium

#### PHASE STRIKE
- **Action**: Teleport adjacent to nearest enemy (ignoring terrain/LOS). Attack for 4 damage. Teleport 3 hexes away.
- **Priority**: High

#### CURSE
- **Action**: Move toward nearest enemy. If within 3 hexes, give target 1 Curse counter (target's next card costs +1 SP).
- **Priority**: Medium

#### MIRROR IMAGE
- **Action**: If Familiar HP ≤ 3, teleport 5 hexes away. Create illusory copy (decoy). Enemies attacking Familiar have 50% chance to hit decoy instead (roll 1d6: 1-3 = hit decoy).
- **Priority**: Critical

#### ELDRITCH BLAST
- **Action**: Attack nearest enemy within 5 hexes for 3 damage. Ignore LOS and cover (magic bypasses obstacles).
- **Priority**: Medium

### Command Response
- **RALLY**: Teleport to any visible hex within 8 hexes (incredible mobility)
- **ATTACK**: Attack target for 5 damage and apply 2 Curse counters
- **DEFEND**: Phase out of reality (cannot be targeted until next turn)
- **HOLD**: Channel magic, next attack deals 6 damage and stuns target (loses next turn)

### Special Ability: PHASE SHIFT
Warp Familiar ignores terrain and can pass through walls. Cannot be blocked by obstacles.

---

## 7. SCRAP HAULER (Engineer)
**Category**: Engineer Support
**Faction**: Nomadic Scrap-Takers
**HP**: 10 | **Movement**: 3 | **Defense**: 1
**Equipment Slots**: 3

### Description
Salvage bot cobbled together from scrap metal. Repairs Caskets, builds cover, and scavenges resources.

### Behavior Deck (5 Cards)

#### FIELD REPAIR
- **Action**: Move toward nearest friendly Casket with <20 HP. If adjacent, heal 4 HP (recover 4 cards from discard).
- **Priority**: High

#### BUILD COVER
- **Action**: If no cover within 2 hexes, create 1 hex of cover (blocks LOS, +1 Defense). Otherwise, move toward nearest damaged Casket.
- **Priority**: Medium

#### SCAVENGE
- **Action**: Move toward nearest corpse or destroyed equipment. If adjacent, recover 1 Scrap token (usable after mission).
- **Priority**: Low

#### IMPROVISED ATTACK
- **Action**: If enemy within 3 hexes, throw scrap metal for 3 damage. No special effects (just a desperate attack).
- **Priority**: Low

#### EMERGENCY OVERRIDE
- **Action**: If any friendly Casket has 3+ Component Damage, move toward them. If adjacent, remove 1 Component Damage marker (field repair).
- **Priority**: Critical

### Command Response
- **RALLY**: Move up to 3 hexes
- **ATTACK**: Not applicable (Hauler is not combat unit, cannot be commanded to attack)
- **DEFEND**: Deploy portable shield (blocks LOS for 1 hex, +2 Defense to adjacent allies)
- **HOLD**: Fortify position, build 2 hexes of cover

### Special Ability: SALVAGE
When enemy is destroyed within 4 hexes of Scrap Hauler, automatically gain 1 Scrap token.

---

## 8. BLIGHTED HOUND (Beast)
**Category**: Beast Support
**Faction**: Vestige Bloodlines
**HP**: 10 | **Movement**: 5 | **Defense**: 0
**Equipment Slots**: 2

### Description
Mutated war-hound with grotesque mutations and bestial rage. Fast, vicious, spreads Blight.

### Behavior Deck (6 Cards)

#### FERAL CHARGE
- **Action**: Move full speed toward nearest enemy. If adjacent, attack for 4 damage and apply 1 Blight counter.
- **Priority**: High

#### SAVAGE BITE
- **Action**: Attack nearest enemy for 5 damage. If target has Blight counters, deal +1 damage per counter (max +4).
- **Priority**: High

#### SPREADING INFECTION
- **Action**: Attack nearest enemy for 3 damage. Apply 2 Blight counters. All adjacent enemies gain 1 Blight counter (contagion).
- **Priority**: Medium

#### BLOOD FRENZY
- **Action**: If Hound HP ≤ 5, gain +2 damage to all attacks. Move toward nearest enemy and attack for 6 damage.
- **Priority**: Critical

#### HUNT THE WEAK
- **Action**: Move toward enemy with lowest HP. Attack for 4 damage and apply 1 Blight counter.
- **Priority**: Medium

#### PACK TACTICS
- **Action**: If Casket is adjacent to an enemy, move toward that enemy. Attack for 3 damage with advantage (roll 2d6 for hit, use higher roll if using hit rolls).
- **Priority**: Medium

### Command Response
- **RALLY**: Move up to 5 hexes (very fast beast)
- **ATTACK**: Attack target for 6 damage and apply 2 Blight counters
- **DEFEND**: Hound is too feral to defend (ignores this command, executes normal behavior)
- **HOLD**: Growl menacingly, enemies within 2 hexes have -1 to attacks (intimidation)

### Special Ability: BLIGHT AURA
All enemies starting their turn adjacent to Blighted Hound gain 1 Blight counter automatically.

---

## COMMAND CARDS (For Casket Decks)

Players can add these to their deck to better control support units:

### RALLY CRY (Universal)
- **SP Cost**: 1
- **Type**: Utility
- **Range**: 6 hexes
- **Effect**: Choose 1 support unit within range. Move it up to its full movement distance to any visible hex.
- **Heat**: 0

### COORDINATED STRIKE (Universal)
- **SP Cost**: 2
- **Type**: Attack, Command
- **Range**: Special
- **Effect**: Your support unit and your Casket both attack the same target. Both attacks gain +2 damage.
- **Heat**: 0

### DEFENSIVE FORMATION (Universal)
- **SP Cost**: 1
- **Type**: Utility, Command
- **Range**: 4 hexes
- **Effect**: Move support unit adjacent to you. Both you and support unit gain +2 Defense until start of next turn.
- **Heat**: 0

### FOCUSED ASSAULT (Requires Support Unit)
- **SP Cost**: 3
- **Type**: Attack, Command
- **Range**: 8 hexes
- **Effect**: Command support unit to attack target. Support unit makes 2 attacks instead of 1.
- **Heat**: 1

### EMERGENCY RECALL (Universal)
- **SP Cost**: 0
- **Type**: Reactive, Command
- **Range**: 10 hexes
- **Effect**: When support unit would be destroyed, immediately teleport it adjacent to your Casket and prevent destruction (1 HP remains).
- **Heat**: 0
- **Keywords**: Reactive

### INSPIRE (Universal)
- **SP Cost**: 2
- **Type**: Utility, Command
- **Range**: 6 hexes
- **Effect**: Support unit draws 2 Behavior cards, choose 1 to execute, discard the other.
- **Heat**: 0

---

## EQUIPMENT SLOT COSTS

When building your deck, support units take up Equipment Slots:

| Support Unit | Slots | Justification |
|--------------|-------|---------------|
| Penitent Squad | 2 | Basic infantry |
| Ironclad Sentinel | 3 | Heavy artillery |
| Bone Thralls | 2 | Swarm, individually weak |
| Verdant Stalker | 2 | Fast scout |
| Forge Golem | 4 | Massive tank |
| Warp Familiar | 3 | Powerful mystic |
| Scrap Hauler | 3 | Support specialist |
| Blighted Hound | 2 | Fast beast |

**Trade-off**: Taking a support unit means fewer equipment cards in your deck.

**Example**:
- Scout Casket (Light): 1 Equipment Slot
  - Cannot take support units (not enough slots)
- Assault Casket (Medium): 2 Equipment Slots
  - Can take Penitent Squad, Bone Thralls, Verdant Stalker, or Blighted Hound
- Heavy Casket: 3 Equipment Slots
  - Can take any support except Forge Golem
- Fortress Casket: 4 Equipment Slots
  - Can take any support unit, including Forge Golem

---

## BALANCING SUPPORT UNITS

### Advantages
- Extra actions per turn (support acts after Caskets)
- Tactical flexibility (flanking, drawing fire, objectives)
- Action economy (2 units acting instead of 1)

### Disadvantages
- Uses Equipment Slots (fewer weapons/equipment)
- HP pool separate from deck (can be killed permanently)
- AI behavior can be unpredictable
- Requires SP to command effectively

### Design Philosophy
Support units should feel like **force multipliers**, not replacements for player skill. They:
- Provide tactical options (zoning, flanking, tanking)
- Create interesting decisions (do I command them or let AI handle it?)
- Have weaknesses (low HP, predictable AI, costs equipment slots)

---

## ADVANCED RULES

### Support Unit Death
When support unit reaches 0 HP:
- Remove from battlefield immediately
- Place corpse marker (can be scavenged by Scrap Hauler)
- Cannot be resurrected (except Bone Thralls with special ability)
- Remains dead for rest of mission

### Multiple Support Units
In larger games (3v3, 4v4), you can have 1 support unit per Casket. They activate in initiative order (roll 1d6 per support unit).

### Support-Only Armies (Variant)
For scenario variety, one player can control multiple support units with no Casket:
- 3 support units (total 8 Equipment Slots worth)
- Example: Ironclad Sentinel + Bone Thralls + Verdant Stalker
- Player draws 1 Behavior card per unit, executes all
- Can use Rally/Command actions on any of their units (pool 5 SP total)

---

## EXAMPLE TURN WITH SUPPORT UNIT

**Setup**: You control a Church Casket + Penitent Squad

**Round 1**:

### 1. Casket Turn
- Refresh 5 SP
- Play **MOVE** (1 SP): Move 2 hexes toward enemy
- Play **BLOOD OFFERING** (0 SP): Discard 2 cards, next attack +3 damage
- Play **FAITHFUL THRUST** (2 SP): Attack enemy for 7 damage (4 base + 3 Blood Offering)
- Draw 3 cards
- 2 SP remaining

### 2. Support Unit Phase (Penitent Squad)
- Draw 1 Behavior card: **CHARGE FORWARD**
- Execute: Squad moves 3 hexes toward nearest enemy
- Squad attacks for 3 damage (now adjacent)
- Discard Behavior card

### 3. Decision Point
You have 2 SP left. Do you:
- **Option A**: Save SP for next turn
- **Option B**: Spend 1 SP to RALLY squad into flanking position (rear arc)
- **Option C**: Spend 2 SP to COMMAND: ATTACK for 4 damage instead of 3

You choose **Option B**: Spend 1 SP to Rally squad to enemy's rear arc.

**Next Turn**: Squad will naturally execute behavior from rear position (likely 4 damage due to flanking)

---

## DESIGN NOTES

### Why This System Works
1. **Action Economy**: Gives players more board presence without overwhelming control complexity
2. **Faction Identity**: Each faction's support units reflect their theme (Church = zealots, Dwarves = artillery/golems, Ossuarium = undead thralls)
3. **Strategic Depth**: Choosing equipment vs support unit is meaningful
4. **Emergent Gameplay**: AI behaviors + command system creates dynamic situations

### Playtesting Priorities
- Are support units too powerful for their cost?
- Is the AI behavior system intuitive?
- Do Command cards feel impactful enough?
- Does the Equipment Slot trade-off feel fair?

---

**End of Document**
