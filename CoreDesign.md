# Penance: Absolution Through Steel
## Core Design Document v0.1

**Last Updated**: October 8, 2025  
**Status**: Early Development / Concept Phase

---

## Table of Contents
1. [Concept Overview](#concept-overview)
2. [Casket Weight Classes](#casket-weight-classes)
3. [Soul-Point Action Economy](#soul-point-action-economy)
4. [Soulstone Power System](#soulstone-power-system)
5. [Game Modes](#game-modes)
6. [Mission Deck System](#mission-deck-system)
7. [Monster AI System](#monster-ai-system)
8. [Combat & Positioning](#combat--positioning)

---

## Concept Overview

### The Pitch
A tactical hex-based card game where players pilot massive armored suits called **Caskets** in brutal medieval fantasy combat. Your deck IS your Casket - cards represent equipment, actions, and battle damage. Power comes from corrupting Soulstones that grant strength at the cost of your humanity.

### Core Loop
1. **Deploy** - Build your Casket deck based on weight class and equipment
2. **Fight** - Tactical hex-based combat using Soul-Points for actions
3. **Survive** - Manage heat, corruption, and damage
4. **Progress** - Upgrade in the Workshop, but carry permanent scars

### Inspirations
- **GKR: Heavy Hitters** - Hex positioning, facing matters
- **Kingdom Death: Monster** - Brutal progression, AI behavior decks, permanent consequences
- **MechWarrior/BattleTech** - Weight classes, component damage
- **Deck-builders** - Your Casket is constructed from cards
- **Escaflowne** - Mystical power cores in mechanical armor

---

## Casket Weight Classes

### Scout (500-800 lbs)
**Soul-Points**: 5 SP (Safe Zone)  
**Movement Focus**: Speed & Evasion  
**Deck Size**: 20-25 cards

**Philosophy**: Minimize armor, maximize agility. Scouts survive by not getting hit.

**Strengths**:
- Highest movement range
- Superior evasion abilities
- Sensor/reconnaissance capabilities
- Can disengage from combat easily

**Weaknesses**:
- Fragile - few hits will disable systems
- Low firepower
- Limited equipment slots

**Unique Mechanic**: **Sensor Sweep** - Reveal enemy cards or AI behavior

**Example Loadouts**:
- Dual pistols, jump jets, active camouflage
- Light rifle, grappling hook, smoke launchers
- Recon drone, EMP pulse, escape thrusters

**Strain Table** (Roll 1d6 + Heat when pushing into Danger Zone):
- 1-3: **Servo Whine** - Gain 1 Heat token
- 4-5: **Gyro Slip** - Rotate 1 random facing
- 6-7: **Structural Stress** - Take 1 damage to random limb
- 8+: **Critical Failure** - Lose 1 SP next turn + 1 Heat

---

### Support (900-1,200 lbs)
**Soul-Points**: 4 SP (Safe Zone)  
**Movement Focus**: Balanced  
**Deck Size**: 25-30 cards

**Philosophy**: Force multiplier. Weaker alone, devastating with allies.

**Strengths**:
- Buff and heal allies
- Area control abilities
- Moderate armor and firepower
- Versatile equipment options

**Weaknesses**:
- Vulnerable when isolated
- Jack-of-all-trades, master of none
- Relies on team positioning

**Unique Mechanic**: **Field Repairs** - Remove damage cards from allies' decks

**Example Loadouts**:
- Medical rig, shield projector, support cannon
- Repair drone, smoke screen, flare gun
- Ammo resupply, portable cover, rally beacon

**Strain Table**:
- 1-4: **Power Fluctuation** - Gain 1 Heat token
- 5-6: **System Lag** - Discard 1 random card
- 7-8: **Overload** - Cannot use Support abilities next turn
- 9+: **Cascade Failure** - All adjacent allies gain 1 Heat

---

### Heavy (1,300-1,800 lbs)
**Soul-Points**: 3 SP (Safe Zone)  
**Movement Focus**: Frontline Anchor  
**Deck Size**: 30-35 cards

**Philosophy**: Built to last. Heavies control space through sheer presence.

**Strengths**:
- Thick armor plating
- Sustained firepower
- Can "hold the line" in defensive positions
- Difficult to disable

**Weaknesses**:
- Slow movement
- Cannot disengage easily once committed
- Predictable - enemies know where you'll be

**Unique Mechanic**: **Brace Protocols** - Root in place for massive defensive bonus

**Example Loadouts**:
- Tower shield, battle rifle, reactive armor
- Heavy autocannon, ablative plating, anchor system
- Fortress shield, heavy sword, redundant systems

**Strain Table**:
- 1-5: **Engine Strain** - Gain 1 Heat token
- 6-7: **Hydraulic Lock** - -1 Movement next turn
- 8-9: **Armor Fatigue** - -1 Defense until end of round
- 10+: **Pressure Breach** - Take 2 damage to Chassis

---

### Assault (1,900-2,500 lbs)
**Soul-Points**: 2 SP (Safe Zone)  
**Movement Focus**: Mobile Fortress  
**Deck Size**: 35-40 cards

**Philosophy**: Walking apocalypse. When an Assault arrives, the battlefield changes.

**Strengths**:
- Devastating firepower
- Nearly indestructible
- Environmental impact (tremors, terrain destruction)
- Psychological intimidation

**Weaknesses**:
- Extremely slow
- High heat generation
- Resource intensive (deployment cost in campaigns)
- Cannot navigate tight spaces

**Unique Mechanic**: **Siege Mode** - Multi-turn attacks that reshape the battlefield

**Example Loadouts**:
- Siege cannon, fortress armor, seismic anchors
- Dual heavy weapons, ablative plating, reactor overdrive
- Wrecking blade, bunker shield, tremor generators

**Strain Table**:
- 1-6: **Reactor Spike** - Gain 2 Heat tokens
- 7-8: **Immobilization** - Cannot move next turn
- 9-10: **Meltdown Warning** - Must spend next turn venting or take 3 damage
- 11+: **Catastrophic Breach** - Take 3 damage to Chassis, gain 1 Taint

---

### Aberrant (600-1,500 lbs Variable)
**Soul-Points**: 3 SP (Safe Zone)  
**Movement Focus**: Unpredictable  
**Deck Size**: 25-30 cards (asymmetric)

**Philosophy**: Rules are optional. Reality is negotiable.

**Strengths**:
- Breaks normal game rules
- Unpredictable abilities
- Can bypass standard defenses
- Unique movement (teleport, phase, crawl on walls)

**Weaknesses**:
- High corruption cost
- Unstable - side effects are common
- Difficult to master
- Weight fluctuates (affects terrain interactions)

**Unique Mechanic**: **Warp Flux** - Reality-bending effects with unpredictable outcomes

**Example Loadouts**:
- Living weapon grafts, void shield, mutation cards
- Phase cannon, dimensional anchor, chaos field
- Bone blades, corruption aura, reality tear

**Strain Table** (Weird effects):
- 1-3: **Whispers** - Gain 1 Taint token
- 4-5: **Reality Slip** - Teleport 1d3 hexes in random direction
- 6-7: **Mutation** - Gain random buff/debuff until next turn
- 8-9: **Possession** - AI controls your next action
- 10+: **Void Touch** - Adjacent enemies gain 1 Taint, you gain 2

---

## Soul-Point Action Economy

### Core Concept
Each Casket has a **Strain Dial** tracking their operational capacity. Pilots can operate safely within their Casket's limits or push into dangerous territory for more actions.

### Safe Zone vs Danger Zone

**Safe Zone (Green)**:
- Scout: 5 SP
- Support: 4 SP
- Heavy: 3 SP
- Assault: 2 SP
- Aberrant: 3 SP

**Danger Zone (Red)**:
- ALL classes: +2 SP beyond safe zone
- Must roll on Strain Table at end of turn
- Risk increases with accumulated Heat

### Soul-Point Costs

**Movement**:
- 1 SP: Move 1 hex forward/backward
- 1 SP: Rotate 1 hex-facing (60°)
- 2 SP: Sidestep 1 hex (no rotation change)

**Combat**:
- 1 SP: Light weapon (pistol, knife, light rifle)
- 2 SP: Medium weapon (rifle, sword, standard cannon)
- 3 SP: Heavy weapon (siege cannon, greatsword, rocket launcher)

**Other Actions**:
- 1 SP: Brace (increase defense until next turn)
- 2 SP: Interact with objective/environment
- 1 SP: Emergency system activation (varies by card)
- 2 SP: Vent Heat (remove 1d3 Heat tokens)

### Example Turn (Heavy Casket)

"I have 3 SP safely. I'll move forward 2 hexes (2 SP), then attack with my medium autocannon (2 SP). That's 4 SP total - I'm 1 into the Danger Zone."

*End of turn: Roll 1d6 = 5. Current Heat is 1, so 5+1 = 6. Check Heavy Strain Table: Result 6-7 = "Hydraulic Lock" - -1 Movement next turn.*

---

## Soulstone Power System

### The Heart Cores

**Lore**: Ancient crystalline organs pulsing with corrupted life energy. No one knows their true origin - some say they're fossilized dragon hearts, others claim they're fragments of fallen gods. What's certain: they grant immense power at terrible cost.

### Corruption Track (0-10 Taint)

**Clean Stone (0-2 Taint)**:
- Standard Safe Zone SP
- Stable, predictable operation
- Access to basic equipment only

**Tainted Stone (3-6 Taint)**:
- Safe Zone +1 SP (more power!)
- All Strain rolls +1 (more dangerous)
- Unlock "Tainted" keyword cards
- Pilot suffers nightmares, paranoia

**Corrupted Stone (7-9 Taint)**:
- Safe Zone +2 SP (incredible power!)
- All Strain rolls +2 (very dangerous)
- Unlock "Forbidden" keyword cards
- Pilot's body begins mutating

**Abomination (10 Taint)**:
- Transformation event triggered
- Player-controlled Casket becomes AI-controlled boss
- Gains monstrous abilities
- Becomes enemy to ALL players
- Can only be stopped by destruction

### Gaining Taint

**During Combat**:
- Using "Corruption" keyword cards
- Pushing Strain Table rolls of 10+
- Taking critical damage to Soulstone chamber
- Exposure to enemy corruption effects

**Between Missions**:
- Choosing high-risk, high-reward campaign options
- Installing forbidden equipment
- Accepting dark bargains

### Purification

**Rare and Costly**:
- Specific campaign missions
- Workshop rituals (expensive resources)
- Sacrifice of powerful equipment
- Not guaranteed to work

### Mechanical Benefits of Corruption

**Tainted Cards** (3+ Taint required):
- More efficient SP costs
- Powerful effects with drawbacks
- Example: *"Hungering Blade"* - Deals +2 damage, gain 1 Taint per kill

**Forbidden Cards** (7+ Taint required):
- Game-breaking abilities
- Severe side effects
- Example: *"Void Rend"* - Ignore all armor, teleport target, gain 2 Taint, -1 to all rolls next turn

---

## Heat Management

### Heat Accumulation
Heat represents your Casket's thermal load, system stress, and pilot exhaustion.

**Gain Heat from**:
- Entering Danger Zone (via Strain Table)
- Using high-output weapons
- Environmental factors (standing in fire, etc.)
- Corruption effects

### Heat Thresholds

| Heat | Effects |
|------|---------|
| 0-2 | Normal operations |
| 3-4 | All Strain rolls +1 |
| 5-6 | All Strain rolls +2, -1 Defense |
| 7-8 | All Strain rolls +3, weapon costs +1 SP |
| 9+ | **Emergency Shutdown** - Skip entire next turn to vent all Heat |

### Venting Heat
- **Manual Vent**: 2 SP to remove 1d3 Heat
- **Passive Cooling**: Some equipment provides end-of-turn Heat removal
- **Support Allies**: Support Caskets can vent allies' Heat
- **Environmental**: Water hexes, ice terrain, etc.

---

## Game Modes

### Arena (PvP)
**Setup**: Fixed point value for Casket + loadout  
**Duration**: 30-45 minutes  
**Board**: Small (7x7 hexes)  
**Objective**: Last Casket standing or points-based victory  
**Format**: Best of 3 rounds

**Ideal for**: Competitive play, tournament format, quick games

---

### Campaign (Co-op PvE)
**Setup**: Persistent pilot and Casket across 10-15 missions  
**Duration**: 2-3 hours per session  
**Board**: Variable based on mission  
**Objective**: Story-driven goals, unlock new equipment  
**Progression**: Workshop upgrades, pilot experience, permanent consequences

**Features**:
- Persistent injuries
- Settlement building (forge/workshop)
- Resource management
- Branching narrative based on corruption levels
- Permadeath or severe setbacks

**Ideal for**: Long-term play groups, narrative experience

---

### Raid (Boss Fight)
**Setup**: 1-4 players vs massive AI monster  
**Duration**: 60-90 minutes  
**Board**: Large (12x12+ hexes) with terrain features  
**Objective**: Defeat the boss or survive X turns  
**Rewards**: Legendary equipment drops

**Boss Mechanics**:
- Multiple phases
- Environmental hazards
- Minion spawns
- Weak point targeting

**Ideal for**: Special events, one-shot sessions

---

### Skirmish (Mixed PvP/PvE)
**Setup**: Teams or FFA with objective deck  
**Duration**: 60-90 minutes  
**Board**: Medium (10x10 hexes)  
**Objective**: Variable based on Mission Deck  
**Format**: Points-based victory

**Features**:
- Primary and secondary objectives
- Hidden agendas
- Environmental hazards
- Possible NPC monsters

**Ideal for**: Varied gameplay, replayability

---

## Mission Deck System

### Purpose
Creates dynamic objectives beyond "kill everything." Adds replayability and tactical variety.

### Deck Structure
- 10-12 objective cards shuffled face-down
- Reveal 1-3 at game start (scenario dependent)
- New objectives trigger at specific events or turn counts

### Objective Categories

#### Primary Objectives (Win Condition)
- **Annihilation**: Destroy all enemy Caskets
- **Extraction**: Reach designated hex zone, survive 2 turns
- **Relic Recovery**: Secure central artifact, return to deployment
- **Assassination**: Kill specific high-value target (worth double VP)
- **Hold the Line**: Control key hexes for X consecutive turns
- **Escort**: Protect non-combatant unit to extraction

#### Secondary Objectives (Bonus Rewards)
- **Scavenge**: Collect resource tokens scattered on battlefield
- **No Casualties**: Complete mission without losing a pilot
- **Swift Victory**: Win in under 6 turns
- **Brutal Efficiency**: Kill with overkill damage
- **Corruption Resistance**: Complete with less than 3 Taint
- **Precision Strike**: Disable specific components without destroying Casket

#### Hidden Agendas (Secret Personal Goals)
Each player draws one secretly:
- **Betrayal**: Deal X damage to ally (team games only)
- **Field Test**: Use specific weapon type 3 times
- **Salvage Priority**: Destroy specific Casket component
- **Glory Hound**: Land killing blow on target
- **Survival Instinct**: End mission with full health

### Rewards Structure

**Primary Completion**:
- 100 Workshop Credits
- 1 Standard equipment card
- Progress campaign story

**Secondary Completion**:
- 50 Credits per objective
- Rare component
- Soulstone fragment (purification material)

**Hidden Agenda Completion**:
- 25 Credits
- Personal upgrade (doesn't share with team)
- Pilot experience point

---

## Monster AI System

### Behavior Deck Structure

Each monster type has 15-20 card AI deck:
- **Basic Attacks** (50%): Standard moves and attacks
- **Special Moves** (30%): Unique abilities
- **Mood Shifts** (15%): Changes behavior pattern mid-fight
- **Trap Cards** (5%): Triggered by player actions

### AI Turn Sequence

1. **Draw AI Card** from behavior deck
2. **Check Positioning Triggers**: "If closest enemy in front arc..."
3. **Execute Movement**: Based on card instructions
4. **Execute Attack/Ability**: Resolve damage and effects
5. **Check Wound Threshold**: Has monster taken enough damage to trigger phase change?

### Example: The Shrieking Colossus

**Size**: Occupies 3 hexes (large creature)  
**Health**: 50 HP  
**Armor**: 5  
**Special**: AOE attacks cause tremors

**Phase 1 Behavior** (50-51 HP):
- Cautious attacks
- Maintains distance
- Tests defenses

**Phase 2 Behavior** (25-49 HP):
- Aggressive closing
- More special abilities
- Targets weakest Casket

**Phase 3 Behavior** (1-24 HP):
- **Berserker Mode**: Reshuffle deck with ONLY attack cards
- Ignores defense
- All attacks deal +2 damage
- No self-preservation

**Sample AI Cards**:

*"Seismic Slam"*
- Move toward closest enemy
- If adjacent: Deal 4 damage, all adjacent hexes take 1 damage
- All affected Caskets must pass stability check or fall prone

*"Piercing Shriek"*
- No movement
- All enemies on board: Discard 1 random card
- Gain 1 armor until next turn

*"Cornered Rage" (Mood Shift)*
- If below 50% health: Add +1 to all attack damage
- Movement increased by 1 hex
- Reshuffle this card back into deck

---

### Example: Carrion Swarm

**Size**: 5-8 individual 1-hex units acting as swarm  
**Health**: 5 HP each  
**Special**: When one dies, others gain +1 movement

**Swarm Tactics**:
- Always attempts to surround targets
- Coordinates attacks on single target
- When reduced to 3 or fewer: Attempts to flee and regroup

**Sample AI Card**:

*"Envelop"*
- All swarm units move toward single target
- If 3+ units adjacent to same target: Target takes 6 damage
- Target must discard equipment card (swarmed and damaged)

---

### Example: Corrupted Casket (Fallen Pilot)

**Special**: Uses player-style deck, but drawn randomly  
**Corruption**: Starts at 8 Taint (Corrupted Stone benefits)  
**Unpredictable**: Draw 2 AI cards, execute both if possible

**Loot**:
- High-tier equipment drops
- Corrupted versions of standard cards
- Cursed relics (powerful but dangerous)

---

## Combat & Positioning

### Hex Facings

Each Casket occupies 1 hex and has 6 facings:
1. **Front** (0°)
2. **Front-Right** (60°)
3. **Back-Right** (120°)
4. **Back** (180°)
5. **Back-Left** (240°)
6. **Front-Left** (300°)

### Equipment Arcs

Equipment cards specify which facings they affect:

**Example: Tower Shield (Left Arm)**
- **Protection Arcs**: Front-Left, Front, Front-Right
- **Effect**: +2 Defense when attacked from these facings
- **Weakness**: Rear and right side vulnerable

**Example: Shoulder Cannon (Chassis)**
- **Firing Arc**: Front-Right only
- **Effect**: Can attack without turning to face
- **Limitation**: Cannot fire to left side

### Attack Resolution

1. **Declare Target**: Choose enemy in range and line of sight
2. **Check Facing**: Determine which facing of target you're attacking
3. **Play Attack Card**: Spend SP, play weapon card
4. **Target Declares Defense**: May play defense cards, check armor
5. **Apply Modifiers**: Facing bonuses/penalties, terrain, etc.
6. **Roll Dice** (if applicable): Some attacks require hit rolls
7. **Resolve Damage**: Apply to target, potentially to specific components

### Facing Modifiers

**Attacking from Front**:
- Standard defense
- Shield arcs active
- Target aware of attack

**Attacking from Sides**:
- Standard defense
- Shield arcs may not apply
- Moderate vulnerability

**Attacking from Rear**:
- -2 Defense for target
- Critical hits more likely
- Shield/armor less effective
- Most devastating position

### Range Bands

**Adjacent (Melee)**:
- 0 hexes away
- Melee weapons only
- Can be "locked in combat" (harder to disengage)

**Close (2-3 hexes)**:
- Short-range weapons optimal
- Shotguns, SMGs, thrown weapons
- Still within charge range

**Medium (4-6 hexes)**:
- Standard engagement range
- Rifles, standard cannons
- Most combat happens here

**Long (7+ hexes)**:
- Sniper rifles, artillery
- Penalties for small targets
- Scouts excel here

### Line of Sight

**Clear LOS**: No obstructions, normal attack  
**Partial Cover**: Terrain/obstacles between, -1 to hit, +1 Defense  
**Full Cover**: Cannot target directly, must use indirect fire

---

## Next Steps in Development

### Immediate Priorities
1. **Card Anatomy**: Design card layout and information hierarchy
2. **Damage System**: How components break and affect gameplay
3. **Deck Construction**: Rules for building legal decks
4. **Complete Card Set**: Design initial equipment and action cards

### Future Development
- Workshop/progression system details
- Campaign structure and story beats
- Terrain and environmental rules
- Full monster bestiary
- Playtesting protocols

---

*This is a living document. Updates will be tracked via version numbers.*

**Version History**:
- v0.1 (Oct 8, 2025): Initial design document capturing core systems
