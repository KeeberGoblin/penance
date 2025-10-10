# Penance: Absolution Through Steel
## Core Design Document v0.1

**Last Updated**: October 8, 2025  
**Status**: Early Development / Concept Phase

---

## Table of Contents
1. [Concept Overview](#concept-overview)
2. [Casket Control System](#casket-control-system)
3. [Casket Weight Classes](#casket-weight-classes)
4. [Racial Casket Variants](#racial-casket-variants)
5. [Soul-Point Action Economy](#soul-point-action-economy)
6. [Soulstone Power System](#soulstone-power-system)
7. [Game Modes](#game-modes)
8. [Mission Deck System](#mission-deck-system)
9. [Monster AI System](#monster-ai-system)
10. [Combat & Positioning](#combat--positioning)

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

## Casket Control System

### The Puppeteer Interface

**Caskets are not worn like suits. They are piloted like puppets from inside.**

Each Casket contains a **Control Capsule**—a coffin-sized chamber filled with Neural Fluid where the pilot floats in total darkness, arms bound across their chest in a death pose. From each fingertip extends a **Neural Thread** (bio-mechanical "puppet string") that connects to the Casket's motor control nodes.

**Key Features**:
- **10 Neural Threads** (one per finger) control all Casket movement
- **Mummy binding pose** prevents pilot movement (protects threads)
- **Viscous Neural Fluid** provides sensory deprivation and thread medium
- **Total immersion** - pilot sees through Casket sensors, not human eyes
- **Pain feedback** - Casket damage translates to finger/nerve pain

**Why This System?**
- Remnants are dead—degraded nervous systems can't operate traditional controls
- Neural Threads bypass body, connecting consciousness directly to machine
- Horrifying by design: piloting is suffering, not empowerment
- Reinforces themes of imprisonment, sacrifice, and body horror

For complete technical specifications, see **[casket-control-system.md](casket-control-system.md)**.

---

## Casket Weight Classes

**IMPORTANT**: The generic weight classes below are deprecated as of v1.0. See [faction-casket-types.md](faction-casket-types.md) for the new asymmetric faction-specific Casket system.

The following sections are kept for reference during transition and playtesting.

---

### Scout (500-800 lbs) [DEPRECATED - See Faction Caskets]
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
- Only 1 Relic slot (focused, specialized builds)

**Unique Mechanic**: **Sensor Sweep** - Reveal enemy cards or AI behavior

**Equipment Slots**: Right Arm, Left Arm, 1 Relic slot

**Example Loadouts**:
- Rapier blade, buckler shield, jump jets (relic)
- Longbow, dagger, grappling hook (relic)
- Dual daggers, smoke launchers (relic)

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

**Equipment Slots**: Right Arm, Left Arm, 2 Relic slots

**Example Loadouts**:
- Mace, tower shield, repair kit (relic), banner (relic)
- Spear, buckler, smoke launcher (relic), medical supplies (relic)
- Crossbow, shield, field toolkit (relic), flare gun (relic)

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

**Equipment Slots**: Right Arm, Left Arm, 3 Relic slots

**Example Loadouts**:
- Great shield, warhammer, ablative plating (relic), gyro-stabilizers (relic), emergency vents (relic)
- Ballista arm, tower shield, reinforced joints (relic), auto-loader (relic), relic plating (relic)
- Greatsword (two-hand), fortress armor (relic), anchor system (relic), repair kit (relic)

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

**Equipment Slots**: Right Arm, Left Arm, 3 Relic slots

**Example Loadouts**:
- Siege ballista arm, great shield, reinforced frame (relic), seismic anchors (relic), coolant system (relic)
- Giant maul (two-hand), ablative plating (relic), tremor generator (relic), reactor overdrive (relic)
- Flameheart cannon (relic tech), bunker shield, emergency vents (relic), relic armor (relic)

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

**Equipment Slots**: Right Arm, Left Arm, 2 Relic slots

**Example Loadouts**:
- Blade arm (corruption-grafted), void shield, warp anchor (relic), mutation catalyst (relic)
- Source conduit arm (void school), bone claws, dimensional tether (relic), chaos field (relic)
- Morphing weapon graft, living armor, reality shard (relic), hunger relic (relic)

**Strain Table** (Weird effects):
- 1-3: **Whispers** - Gain 1 Taint token
- 4-5: **Reality Slip** - Teleport 1d3 hexes in random direction
- 6-7: **Mutation** - Gain random buff/debuff until next turn
- 8-9: **Possession** - AI controls your next action
- 10+: **Void Touch** - Adjacent enemies gain 1 Taint, you gain 2

---

## Racial Casket Variants

All weight classes are available to all races, but each race brings unique mechanics and aesthetics to their Caskets.

### 1. Human - "Penitent Frames"

**Philosophy**: Redemption through suffering, religious devotion, modular pragmatism

**Aesthetic**: Gothic knight armor, chains, prayer scrolls, religious iconography, heavy plate

**Unique Mechanic: Vow System**
- Choose 1 Vow at mission start (restriction + bonus)
- **Vow of Mercy**: Cannot kill disabled enemies, +1 SP Safe Zone
- **Vow of Poverty**: Cannot use Relic Tech (firearms/ancient tech), -1 Taint gain
- **Vow of Wrath**: Must attack each turn if able, +1 damage on all attacks
- **Vow of Penance**: Start at 1 Taint, but can purge 1 Taint per mission if objective completed
- **Vow of Protection**: Must shield allies when adjacent, gain +1 Defense when protecting

**Equipment Naming**:
- Weapons: "Faithkeeper Blade", "Godstrike Maul", "Absolution's Edge"
- Armor: "Martyr's Burden", "Penitent's Wall"
- Tech Relics: "Thunderspeaker" (rifle), "Stormwhisper Lance"

---

### 2. Elven - "Verdant Walkers"

**Philosophy**: Nature integrated with machinery, elegant biomechanics, harmony over domination

**Aesthetic**: Wood grain, living vines, crystal power cores, flowing organic lines, leaf motifs

**Unique Mechanic: Symbiosis**
- Casket "heals" naturally over time
- At end of each round: Remove 1 Damage card from discard pile (shuffle it out)
- BUT: Vulnerable to fire (all fire damage +1)
- Living components require sunlight (penalty in underground/dark missions)

**Equipment Naming**:
- Weapons: "Willowstrike Blade", "Ironbark Greatbow", "Thornwhisper Glaive"
- Armor: "Rootbound Aegis", "Dreamwood Shell"
- Living Relics: "Vinegrasp Tendrils", "Moonshard Arrows"

---

### 3. Dwarven - "Forge Titans"

**Philosophy**: Overengineered masterworks, stone and steel, brutal efficiency, ancestral craftsmanship

**Aesthetic**: Riveted plates, runic engravings, steam vents, anvil-shaped armor, industrial brutality

**Unique Mechanic: Runic Overcharge**
- Can inscribe Runes on equipment cards (once per campaign, permanent)
- Rune effect triggers once per mission, then goes dormant (recharges between missions)
- **Rune of Stone**: Ignore next 3 damage
- **Rune of Flame**: Next attack deals double damage
- **Rune of Iron**: Ignore forced movement/rotation for 1 round
- **Rune of Warding**: +2 Defense against magic/corruption attacks for 1 round

**Equipment Naming**:
- Weapons: "Anvilfall Hammer", "Mountainsplitter Axe", "Grudgebearer Ballista"
- Armor: "Ironheart Bulwark", "Stonebreaker Plate"
- Tech Relics: "Flameheart Cannon", "Runescribed Mechanism"

---

### 4. Orcish - "War Hulks"

**Philosophy**: Scrap metal monsters, brutal and loud, intimidation over elegance, more is better

**Aesthetic**: Jagged edges, war paint, trophies (skulls, banners), asymmetrical design, crude welds

**Unique Mechanic: Scrap Fury**
- When you reshuffle deck, gain +1 damage on all attacks until end of mission (stacks)
- More cycles = more damage (getting angrier as fight continues)
- At 3+ reshuffles: Gain "Berserk" status:
  - Must attack if able (cannot use support/defensive actions)
  - +2 damage on all attacks
  - Ignore pain (first damage card each round doesn't count toward hand clog)

**Equipment Naming**:
- Weapons: "Choppaklaw", "Bashablade", "Skullkrusha Maul", "Dakka-Ballista"
- Armor: "Spikey Bitz", "Scrap Plating"
- Crude Relics: "More Dakka Module", "Grot-Patched Armor"

---

### 5. Draconid - "Dragonborn Shells"

**Philosophy**: Ancient draconic power, crystalline cores, scales and fire, pride and honor

**Aesthetic**: Dragon-scale plating, horn decorations, breath weapon vents, gem inlays, reptilian

**Unique Mechanic: Draconic Breath**
- Built-in breath weapon (doesn't take equipment slot or add cards to deck)
- Choose element at Casket creation: Fire/Ice/Lightning/Poison/Acid
- **Once per mission**: Spend 3 SP, AOE attack in front arc (3 hexes, cone shape)
  - Fire: 3 damage, targets gain 2 Heat
  - Ice: 2 damage, targets slowed (movement -1 next turn)
  - Lightning: 4 damage to primary target, 1 damage to adjacent enemies
  - Poison: 2 damage, ongoing damage (1 damage per turn for 2 turns)
  - Acid: 3 damage, ignores armor
- Generates 3 Heat when used

**Equipment Naming**:
- Weapons: "Clawrend Talons", "Fanged Glaive", "Tailblade Scythe"
- Armor: "Scaleheart Guardian", "Wyrmforged Plate"
- Draconic Relics: "Hoarded Soulstone" (ancient dragon heart)

---

### 6. Undead - "Bonecage Sentinels"

**Philosophy**: Death-powered machinery, necromantic engines, cursed relics, no fear

**Aesthetic**: Bone grafts, tattered banners, ghostly energy, ossified armor, decay aesthetic

**Unique Mechanic: Unliving Resilience**
- Start at 3 Taint (already corrupted, but stable)
- Immune to morale/fear effects
- Immune to poison/disease
- **Death's Door**: When reduced to 0 cards in deck AND hand (normally defeated):
  - Don't die immediately
  - Roll 1d6: 4+ = Continue fighting
  - Draw 5 cards from "Soul Reserve" (special emergency deck)
  - Last stand for 1 more round, then collapse
- Cannot be healed by normal means (requires necromantic repair)

**Equipment Naming**:
- Weapons: "Soulreaver Blade", "Boneshatter Maul", "Cryptkeeper's Staff"
- Armor: "Gravewarden Frame", "Deathmarch Plate"
- Necrotech: "Wraith-Engine Heart", "Phylactery Core", "Lifestealer Grafts"

---

### 7. Fae/Fey - "Glamour Suits"

**Philosophy**: Illusion and trickery, impossible geometry, dreamlike, bargains and prices

**Aesthetic**: Butterfly wings, mirror surfaces, shifting colors, ethereal glow, delicate but deadly

**Unique Mechanic: Fae Bargain**
- **Once per mission**: Activate "Deal" mode (declare at start of turn)
- For 3 turns:
  - +2 SP Safe Zone (Scout gets 7 SP!)
  - Ignore terrain penalties
  - +2 initiative on all cards (act faster)
  - Attacks ignore partial cover
- **After 3 turns, payment due**:
  - Gain 2 Taint
  - -1 SP Safe Zone for rest of mission
  - All Strain rolls +1 for rest of mission
- Risk/reward: Powerful burst, but consequences linger

**Equipment Naming**:
- Weapons: "Starfall Rapier", "Dreamthorn Daggers", "Gossamer Lance"
- Armor: "Twilight Vestment", "Moonveil Cloak"
- Fae Relics: "Trickster's Mirror", "True Name Seal", "Glamour Veil"

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
- Persistent injuries (see [damage-system.md](damage-system.md))
- Settlement building — **See [settlement-mechanics.md](settlement-mechanics.md)** for full system
- Resource management (Credits, Scrap, Population, Morale)
- Branching narrative based on corruption levels and faction relationships
- Permadeath or severe setbacks
- **World Threat**: The Resonance Engine's Instability Track acts as a doomsday clock — **See [resonance-engine-mechanics.md](resonance-engine-mechanics.md)**
- **Political Web**: Faction relationships shift based on player actions — **See [faction-relationships.md](faction-relationships.md)**

**Ideal for**: Long-term play groups, narrative experience

**Campaign Resources**: For world lore, NPCs, and historical context, see:
- [world-lore.md](world-lore.md) — Setting, factions, and Cataclysm history
- [iconic-npcs.md](iconic-npcs.md) — 5 major NPC pilots (potential allies, rivals, or bosses)
- [chronicle-entries.md](chronicle-entries.md) — Historical flavor and storytelling hooks

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

**Note**: This AI system applies to **both** Abominations (Void-spawn monsters) and intelligent NPC enemies (rival pilots). For detailed NPC pilot designs with full mechanics, see **[iconic-npcs.md](iconic-npcs.md)**.

### Behavior Deck Structure

Each monster type has 15-20 card AI deck:
- **Basic Attacks** (50%): Standard moves and attacks
- **Special Moves** (30%): Unique abilities
- **Mood Shifts** (15%): Changes behavior pattern mid-fight
- **Trap Cards** (5%): Triggered by player actions

**NPC Pilots**: Instead of random AI cards, NPCs have strategic decks with signature abilities (e.g., Sister Vex's "Penitent's Burden," Thresh's "Predatory Pact"). They follow similar activation patterns but make "intelligent" tactical decisions.

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

## Victory & Defeat Conditions

### Arena (PvP) Mode

**Victory Conditions**:
- **Last Casket Standing**: Disable all enemy Caskets (deck + hand = 0)
- **Points Victory**: Reach X Victory Points first (typically 10-15 VP)
  - Kill enemy Casket: 5 VP
  - Destroy specific component: 2 VP
  - Control objective hex for 2 turns: 3 VP
- **Time Limit**: Most VP when timer expires (typically 8-10 rounds)

**Defeat Conditions**:
- Your Casket is disabled (deck + hand = 0)
- Chassis takes 9+ damage (core destroyed)
- Opponent reaches victory threshold first

**Between Matches**: Caskets reset to full health, no permanent damage

---

### Campaign (Co-op) Mode

**Mission Victory Conditions** (varies by scenario):
- **Objective Completion**: Secure artifact, reach extraction, hold position
- **Elimination**: Destroy all enemy units
- **Survival**: Last X rounds against overwhelming odds
- **Escort**: Protect NPC/target to destination
- **Timed**: Complete objective before timer expires

**Mission Defeat Conditions**:
- All players' Caskets disabled
- Primary objective fails (VIP dies, artifact destroyed, etc.)
- Time limit expires

**Campaign Consequences**:
- **Victory**: Earn credits, experience, loot
  - Advance story
  - Unlock new equipment/missions
  - Reduce settlement threat level
- **Defeat**:
  - Pilot may die (permadeath if enabled)
  - Expensive repairs needed
  - Story consequences (locked paths, penalties)
  - Settlement may be raided

---

### Raid (Boss Fight) Mode

**Victory Conditions**:
- Reduce boss to 0 HP
- Destroy specific boss components (some bosses have multi-stage defeat)
- Survive X rounds (some boss missions are about endurance, not killing)

**Defeat Conditions**:
- All players' Caskets disabled
- Boss completes its objective (destroys settlement, escapes, etc.)
- Time limit expires

**Rewards**:
- Legendary equipment drops
- Rare Soulstone fragments
- Unique relic tech
- Campaign story advancement

---

### Skirmish (Mixed) Mode

**Victory Conditions** (multiple objectives active):
- **Primary Objective**: Worth 10 VP (e.g., control center hex for 3 turns)
- **Secondary Objectives**: Worth 3-5 VP each (e.g., eliminate enemy leader, scavenge resources)
- **Hidden Agendas**: Worth 2 VP (secret personal goals)
- **Eliminations**: 5 VP per enemy Casket destroyed

**First to 20 VP wins** (or highest VP when time expires)

**Defeat Condition**:
- Your Casket is disabled (but you still score VP for objectives completed before death)

---

### Casket Disabled State

**What "Disabled" Means**:
1. **Deck empty AND hand empty**: Cannot draw or play cards
2. **Chassis component at 9+ damage**: Core destroyed, catastrophic failure
3. **Mission-specific**: Some scenarios have unique disable conditions

**When Disabled**:
- **Arena/Skirmish**: You lose the match, opponent scores VP
- **Campaign/Raid (Solo)**: Mission failure, campaign consequences
- **Campaign/Raid (Co-op)**:
  - You are out of combat (cannot act)
  - Mission continues if allies survive
  - You can be "revived" if allies use repair abilities (variant rule)
  - If all players disabled = mission failure

---

### Special Victory Conditions

**Corruption Victory** (Variant Rule):
- If a player reaches 10 Taint and transforms into Abomination
- They become AI-controlled boss enemy
- Other players must destroy them
- If Abomination wins, campaign ends (dark ending)

**Survival Victory** (Some Campaign Missions):
- Hold out for X rounds against waves
- Victory = surviving, not killing everything
- Rewards based on rounds survived

**Extraction Victory** (Arena/Campaign):
- Reach designated hex zone
- Survive 2 turns in extraction zone
- Exit battlefield (Casket intact = bonus rewards)

---

### Tiebreakers

**If multiple players/teams have same VP**:
1. Least damage taken (component damage totals)
2. Least Heat accumulated
3. Lowest Taint level
4. Fewest turns to complete objective
5. Sudden death round (first to score next VP wins)

---

### Campaign Permadeath (Optional Rule)

**When Pilot Dies**:
- Casket is disabled in critical mission (story-critical loss)
- Chassis destroyed (9+ damage to Chassis)
- Execution (captured in mission, failed rescue)

**Consequences**:
- Pilot is permanently dead (cannot be used again)
- Create new pilot (lose experience, keep some equipment)
- Campaign continues with new character
- Story acknowledges death (memorial, consequences)

**Resurrection** (Rare):
- Specific campaign missions can revive dead pilots (necromancy, rare tech)
- High cost (corruption, permanent debuff, story cost)
- Limited uses

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