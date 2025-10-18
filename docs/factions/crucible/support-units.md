# Crucible Packs - Support Units
## Penance: Absolution Through Steel

**Version**: 2.0 Equipment System
**Status**: ✅ **COMPLETE** - Full Framework with Behavior Decks
**Date**: October 17, 2025

The Crucible Packs field tribal warriors bound by honor, wielding ancestral weapons forged in volcanic fire.

---

## CRUCIBLE SUPPORT UNITS OVERVIEW

**Starting Units** (Available immediately):
1. **Honor Guard** - Defensive duelist who protects allies
2. **Forge Apprentice** - Support smith who generates Forge tokens
3. **Tribal Hunter** - Scout/skirmisher with tracking abilities

**Unlockable Units** (Require campaign progression):
4. **Duelist Champion** - Elite 1v1 fighter (Unlock: Win 5 Honor Duels)
5. **Forge Master** - Tactical commander (Unlock: Forge 3 Ancestral Weapons)
6. **Ancestral Spirit** - Legendary ghost warrior (Unlock: Defeat Ashen-King Torrak)

**Limit**: Choose 1-3 support units (based on Casket Equipment Slots available)

**Design Philosophy**: Crucible units emphasize honor duels, Forge token economy, ancestral legacy, and volcanic terrain control. They thrive in fire, respect strength, and punish cowardice.

---

## 1. HONOR GUARD ⭐ STARTER UNIT
**Category**: Defender / Duelist
**HP**: 12 | **Movement**: 4 | **Defense**: 3
**Equipment Slots**: 2
**Theme**: Sworn protector who intercepts attacks and fights duels on behalf of allies

### Visual Description
Warrior in ancestral plate armor (passed down 6 generations), carrying tower shield emblazoned with Pack symbol (volcanic hammer). Face scarred from ritual trials. Wears ash-braided hair as honor cord.

### Core Mechanics
- **Bodyguard**: Can intercept attacks targeting allies within 3 hexes
- **Duelist Training**: Can accept Honor Duels on behalf of allies
- **Shield Wall**: Adjacent allies gain +1 Defense
- **Forge Generation**: Gains 1 Forge token when protecting ally from damage
- **Unbreakable**: When reduced to 0 HP, survive with 1 HP once per battle (honor won't permit fall)

### Behavior Deck (6 Cards)

#### 🛡️ PROTECTIVE STANCE
**Type**: Reactive / Defense
**Priority**: Critical (when ally within 3 hexes takes damage)

**Effect**:
- Intercept attack targeting ally within 3 hexes
- Honor Guard takes damage instead of ally
- Reduce damage by 2 (minimum 1, shield absorbs)
- Gain 1 Forge token (honor in protection)
- Move 3 hexes toward ally if needed

**Flavor**: "No harm shall reach those under my shield."

---

#### ⚔️ CHALLENGE ACCEPTED
**Type**: Duel / Attack
**Priority**: High (when ally threatened or Honor Duel issued)

**Effect**:
- Can accept Honor Duel on behalf of ally (take their place)
- If in active duel: Attack for 5 damage
- If duel victory: Gain 2 Forge tokens + draw 2 cards
- If enemy refuses to duel Guard: Enemy gains Coward's Mark

**Flavor**: "Your quarrel is with me now."

---

#### 🏰 SHIELD WALL FORMATION
**Type**: Buff / Area Defense
**Priority**: High (when 2+ allies within 3 hexes)

**Effect**:
- Plant shield (cannot move this turn)
- All allies within 3 hexes gain +2 Defense
- Honor Guard gains +1 Defense (total Defense 4)
- Enemies attacking allies within area take 2 damage (shield spikes)
- Generate 1 Forge token

**Flavor**: "Behind this shield, we fear nothing."

---

#### 🔥 LAVA STANCE
**Type**: Utility / Positioning
**Priority**: Medium (when lava terrain within 4 hexes)

**Effect**:
- Move up to 4 hexes toward lava terrain
- If ending in lava: Gain 2 Forge tokens (instead of 1)
- Take no damage from lava (honor tempers flesh)
- Next attack deals +2 damage (volcanic fury)

**Flavor**: "Fire tests us. We do not burn."

---

#### 💢 RETRIBUTION STRIKE
**Type**: Attack / Revenge
**Priority**: High (when ally was damaged this round)

**Effect**:
- Move toward enemy who damaged ally (up to 4 hexes)
- Attack for 6 damage
- If ally was reduced to ≤50% HP: Deal 8 damage instead
- Gain 1 Forge token per ally protected this battle

**Flavor**: "You hurt mine. Now face the consequences."

---

#### 🏆 LAST STAND
**Type**: Reactive / Survival
**Priority**: Critical (when Honor Guard HP ≤ 4)

**Effect**:
- Trigger Unbreakable (survive at 1 HP, once per battle)
- Gain +3 damage to all attacks for 2 turns
- Cannot move (rooted to spot, "here I stand")
- Allies within 3 hexes gain +1 damage (inspired by courage)
- Generate 2 Forge tokens

**Flavor**: "I fall only when my brothers are safe."

---

### Strategic Use
- **Bodyguard Role**: Intercept high-damage attacks targeting fragile allies
- **Duel Proxy**: Accept duels on behalf of allies who can't win
- **Shield Wall**: Create defensive zone for Casket to operate safely
- **Token Battery**: Generates Forge tokens by protecting allies

---

## 2. FORGE APPRENTICE ⭐ STARTER UNIT
**Category**: Support / Crafter
**HP**: 8 | **Movement**: 5 | **Defense**: 1
**Equipment Slots**: 2
**Theme**: Young smith who tends mobile forge, generates tokens, buffs weapons

### Visual Description
Young warrior (late teens) carrying portable forge (backpack-sized brazier burning with volcanic coal). Wears leather apron over light armor. Carries smith's hammer and tongs. Face smudged with ash, eyes bright with devotion.

### Core Mechanics
- **Mobile Forge**: Generates 2 Forge tokens per turn when standing in lava (1 otherwise)
- **Weapon Blessing**: Can spend 1 Forge token to give ally +1 damage for 1 turn
- **Repair**: Can spend 2 Forge tokens to restore 3 cards to ally
- **Lava Creation**: Can spend 3 Forge tokens to create 1 lava terrain hex
- **Fragile**: Low HP and Defense (must be protected)

### Behavior Deck (6 Cards)

#### 🔨 FORGE TENDING
**Type**: Utility / Token Generation
**Priority**: High (start of turn, if not in lava)

**Effect**:
- Move toward nearest lava terrain (up to 5 hexes)
- If in lava: Generate 2 Forge tokens (mobile forge ignites)
- If not in lava: Generate 1 Forge token (embers suffice)
- Allied Crucible within 3 hexes gain 1 Forge token

**Flavor**: "The forge never sleeps. Neither do I."

---

#### ⚡ EMBER BLESSING
**Type**: Buff / Support
**Priority**: High (when ally about to attack)

**Effect**:
- Target allied Crucible Casket within 4 hexes
- Spend 1 Forge token
- Ally's next attack deals +2 damage (weapon blessed with fire)
- If ally in lava: +3 damage instead
- Ally's weapon glows with volcanic heat (visual)

**Flavor**: "May the First Forge guide your strike."

---

#### 🔧 FIELD REPAIR
**Type**: Healing / Support
**Priority**: Medium (when ally HP ≤ 50%)

**Effect**:
- Target allied Crucible Casket within 3 hexes
- Spend 2 Forge tokens
- Ally recovers 4 cards (emergency repairs)
- Remove 1 debuff from ally (burn away impurity)
- Apprentice cannot act again this turn (exhausted)

**Flavor**: "Hold still. I can fix this."

---

#### 🌋 CREATE LAVA TERRAIN
**Type**: Utility / Terrain Control
**Priority**: Medium (when no lava within 4 hexes)

**Effect**:
- Spend 3 Forge tokens
- Create 1 lava terrain hex within 3 hexes (volcanic eruption)
- Enemies in hex take 3 damage immediately
- Lava hex lasts 3 turns
- Apprentice generates 1 Heat

**Flavor**: "The mountain answers the forge."

---

#### 🏃 EVASIVE MANEUVERS
**Type**: Movement / Survival
**Priority**: Critical (when enemy within 2 hexes or Apprentice HP ≤ 4)

**Effect**:
- Move up to 5 hexes away from nearest enemy
- Cannot be targeted by reactions during movement (too fast)
- If ending adjacent to ally: Hide behind them (cannot be targeted until Apprentice moves)
- Drop 1 lava flask (create 1 lava hex at starting position)

**Flavor**: "I am smith, not warrior! Protect me!"

---

#### 🔥 FORGE OVERLOAD
**Type**: Attack / Desperation
**Priority**: Low (when ally destroyed or Apprentice cornered)

**Effect**:
- Spend all Forge tokens (minimum 3 required)
- Deal 2 damage per token spent to all enemies within 3 hexes
- Create lava terrain at Apprentice's location
- Apprentice takes 2 damage (forge overheats)
- Forge goes dormant (no token generation next turn)

**Flavor**: "If I fall, I take you with me!"

---

### Strategic Use
- **Token Economy**: Primary Forge token generator for team
- **Buff Bot**: Use Ember Blessing to amplify Casket attacks
- **Terrain Control**: Create lava hexes for positioning
- **Fragile**: Must be protected (dies easily to focused fire)

---

## 3. TRIBAL HUNTER ⭐ STARTER UNIT
**Category**: Scout / Skirmisher
**HP**: 10 | **Movement**: 6 | **Defense**: 1
**Equipment Slots**: 2
**Theme**: Fast-moving tracker who harasses, scouts, and marks targets

### Visual Description
Lean warrior in light leather armor, carrying volcanic glass spear and throwing axes. Face painted with ash tribal markings. Moves with predatory grace, constantly scanning environment. Wears trophy teeth from hunted prey.

### Core Mechanics
- **Tracking**: Can mark 1 enemy per turn (Hunter's Mark = +1 damage from all Crucible)
- **Hit-and-Run**: Can move before AND after attacking (split movement)
- **Scout Vision**: Reveals hidden enemies within 8 hexes
- **Pack Tactics**: Deals +1 damage for each ally adjacent to same target
- **Outnumbered Bonus**: Gains +1 damage for each enemy within 6 hexes (desperate strength)

### Behavior Deck (6 Cards)

#### 🎯 HUNTER'S MARK
**Type**: Utility / Mark
**Priority**: High (when priority target identified)

**Effect**:
- Mark 1 visible enemy within 8 hexes (Hunter's Mark)
- All Crucible units deal +1 damage to marked enemy
- Mark lasts until enemy dies or Hunter marks new target
- Reveal hidden enemies within 8 hexes
- Move up to 3 hexes

**Flavor**: "I see you. The pack sees you. Run."

---

#### 🏹 HARASSING STRIKE
**Type**: Attack / Mobility
**Priority**: High (when opportunity for hit-and-run)

**Effect**:
- Move up to 3 hexes toward enemy
- Throw volcanic axe for 3 damage (range 4 hexes)
- Move up to 3 hexes away from enemy (hit-and-run)
- If enemy is marked: Deal 4 damage instead
- Cannot be targeted by reactions during movement

**Flavor**: "Strike fast. Vanish faster."

---

#### 🐺 PACK COORDINATION
**Type**: Attack / Synergy
**Priority**: High (when ally adjacent to enemy)

**Effect**:
- Move toward enemy adjacent to ally (up to 6 hexes)
- If Hunter and ally both adjacent to same enemy:
  - Hunter attacks for 5 damage (volcanic spear)
  - Ally gains +2 damage on their next attack (coordinated strike)
- Generate 1 Forge token (honor in coordination)

**Flavor**: "The pack hunts as one."

---

#### 🔍 SCOUTING RUN
**Type**: Movement / Information
**Priority**: Medium (when battlefield unexplored or objectives present)

**Effect**:
- Move up to 8 hexes (running)
- Reveal all hidden enemies, traps, objectives within 6 hexes
- Mark 1 enemy encountered
- Can move through enemy-occupied hexes (too fast to intercept)
- Report to Casket: Casket draws 1 card (intel value)

**Flavor**: "The terrain is mine. I know every path."

---

#### 💪 DESPERATE FURY
**Type**: Attack / Buff
**Priority**: High (when outnumbered: 2+ enemies within 6 hexes)

**Effect**:
- Gain +1 damage per enemy within 6 hexes (max +3)
- Attack nearest enemy for 4 + bonus damage
- If enemy is marked: Deal additional +2 damage
- Move 3 hexes after attack (retreat or reposition)

**Flavor**: "Cornered prey is deadliest. I am no prey."

---

#### 🔥 VOLCANIC AMBUSH
**Type**: Attack / Terrain
**Priority**: Medium (when lava terrain nearby or enemy isolated)

**Effect**:
- If standing in lava: Leap out to attack enemy within 4 hexes (8 damage)
- If not in lava: Move to lava hex (up to 6 hexes), prepare ambush
- Marked enemies take +3 damage from ambush
- Create 1 lava hex at landing spot (volcanic splash)
- Hunter takes 1 damage (lava exposure, worth it)

**Flavor**: "From fire I strike. To ash you return."

---

### Strategic Use
- **Marking**: Mark priority targets (heaviest enemy, support units)
- **Hit-and-Run**: Harass enemies, never get pinned down
- **Scouting**: Reveal objectives, hidden enemies, traps
- **Pack Synergy**: Coordinate with Casket for bonus damage

---

## 4. DUELIST CHAMPION 🔒 UNLOCKABLE
**Unlock Condition**: Win 5 Honor Duels in campaign
**Category**: Elite 1v1 Fighter
**HP**: 15 | **Movement**: 5 | **Defense**: 2
**Equipment Slots**: 2
**Theme**: Undefeated duelist who lives for single combat

### Visual Description
Scarred veteran covered in duel marks (23 scars, one per duel won). Dual-wields ancestral blades (curved volcanic steel, glowing with heat). Moves with predatory confidence. Eyes cold, assessing every opponent.

### Core Mechanics
- **Duel Master**: Automatically wins initiative in Honor Duels
- **Executioner**: Deals double damage to enemies below 50% HP
- **Riposte**: When attacked in duel, counterattack for 3 damage
- **Coward Slayer**: Deals +4 damage to enemies with Coward's Mark
- **Victory Rush**: Killing enemy in duel recovers 5 HP + 3 Forge tokens

### Key Abilities
1. **Force Duel** (2 SP): Challenge enemy, they cannot refuse (overrides Coward's Mark)
2. **Dual Strike** (3 SP): Attack twice in same turn (4 damage each)
3. **Perfect Parry** (0 SP, Reactive): Negate 1 attack completely, counterattack for 5 damage
4. **Blood Price** (5 Forge tokens): Execute enemy below 50% HP instantly (no defense, guaranteed kill)

### Behavior Pattern
1. Challenge strongest enemy to Honor Duel
2. Use Dual Strike for burst damage
3. Perfect Parry when enemy attacks
4. Blood Price to finish wounded enemies
5. Victory Rush snowballs into next duel

---

## 5. FORGE MASTER 🔒 UNLOCKABLE
**Unlock Condition**: Forge 3 Ancestral Weapons in campaign
**Category**: Tactical Commander / Support
**HP**: 12 | **Movement**: 4 | **Defense**: 3
**Equipment Slots**: 3
**Theme**: Master smith who commands battlefield through forge mastery

### Visual Description
Grizzled elder (60+ years old) carrying massive forge-hammer (head size of anvil). Wears ancestral plate armor adorned with Forge tokens (ceremonial). Gray beard braided with volcanic glass beads. Presence commands respect.

### Core Mechanics
- **Forge Authority**: Generates 3 Forge tokens per turn (master's blessing)
- **Mass Blessing**: Can distribute Forge tokens to all Crucible units within 6 hexes
- **Ancestral Weapon Mastery**: Crucible units with Ancestral Weapons gain +1 to all stats
- **Volcanic Command**: Can create 2 lava hexes per turn (no cost)
- **Inspire**: Allies within 6 hexes have +1 to all actions

### Key Abilities
1. **Forge of War** (4 Forge tokens): All Crucible units gain +2 damage for 2 turns
2. **Ancestral Summon** (6 Forge tokens): Summon spectral ancestor warrior (10 HP, 5 damage, lasts 3 turns)
3. **Volcanic Eruption** (8 Forge tokens): Create 5 lava hexes in area, 6 damage to enemies (ultimate)
4. **Master's Wisdom** (0 SP): All Crucible units draw 1 card (once per round)

### Behavior Pattern
1. Generate and distribute Forge tokens
2. Position near Casket (maximize Inspire aura)
3. Create lava terrain for positioning
4. Use Forge of War when engaging enemies
5. Volcanic Eruption as finisher

---

## 6. ANCESTRAL SPIRIT 🔒 UNLOCKABLE
**Unlock Condition**: Defeat Ashen-King Torrak in Honor Duel
**Category**: Legendary Ghost Warrior
**HP**: 20 | **Movement**: 6 (Flying) | **Defense**: 4
**Equipment Slots**: 3
**Theme**: Spirit of ancient Crucible hero, returned to aid worthy descendants

### Visual Description
Translucent warrior wreathed in volcanic flame and ash. Wears ghostly plate armor from pre-Sundering era. Wields spectral forge-hammer crackling with lightning. Eyes burn with amber fire. Moves without touching ground (floating).

### Core Mechanics
- **Incorporeal**: Takes 50% damage from all sources (ghost form)
- **Phase Walk**: Can move through enemies and terrain (Flying, ignore everything)
- **Ancestral Wrath**: All attacks deal fire damage (ignores armor, affects components)
- **Undying**: When reduced to 0 HP, return to ancestral realm (can be re-summoned after 3 turns)
- **Legacy Aura**: All Crucible units within 8 hexes have +2 to all stats (ancestors watch over us)

### Key Abilities
1. **Hammer of Ages** (4 SP): Attack for 8 fire damage, create 2 lava hexes at impact
2. **Ancestral Judgment** (6 Forge tokens): Enemy with Coward's Mark takes 12 damage and is Feared (skip 2 turns)
3. **Spirit Walk** (2 SP): Teleport up to 8 hexes, pass through enemies (deal 2 damage to each)
4. **Call of the Forge** (Ultimate, once per battle): All dead Crucible units return for 1 turn (spectral forms, 50% HP, fight alongside Spirit)

### Behavior Pattern
1. Hunt enemies with Coward's Mark (Ancestral Judgment)
2. Phase Walk through enemy lines (disruptive)
3. Hammer of Ages for terrain control
4. Call of the Forge when desperate (resurrect fallen)
5. Tank damage with Incorporeal (50% reduction)

---

## STRATEGIC BUILDS

### Honor Guard Fortress (Defensive)
- **Units**: Honor Guard + Forge Apprentice
- **Strategy**: Guard protects Apprentice, Apprentice generates tokens, Guard uses tokens for defense
- **Strength**: Extreme durability, constant token generation, synergistic
- **Weakness**: Low offensive pressure, struggles vs kiting

### Duelist Rush (Aggressive)
- **Units**: Duelist Champion + Tribal Hunter
- **Strategy**: Hunter marks targets, Champion forces duels, executes wounded
- **Strength**: Extreme single-target damage, mark synergy, snowballs victories
- **Weakness**: Vulnerable to AOE, weak vs multiple threats

### Forge Economy (Token Battery)
- **Units**: Forge Apprentice + Forge Master
- **Strategy**: Generate massive Forge tokens (5 per turn), fund expensive abilities
- **Strength**: Infinite resources, powerful abilities always available
- **Weakness**: Low combat power, needs protection

### Ancestral Legacy (Endgame)
- **Units**: Ancestral Spirit + Honor Guard
- **Strategy**: Spirit leads offense, Guard defends, Legacy Aura buffs Casket
- **Strength**: Unstoppable combination, +2 all stats to Casket, incorporeal tank
- **Weakness**: Expensive (6 equipment slots), overkill vs weak enemies

---

## PROGRESSION SYSTEM

### Early Campaign (Missions 1-5)
- **Available**: Honor Guard, Forge Apprentice, Tribal Hunter
- **Focus**: Learn Honor Duel mechanics, Forge token economy, marking targets
- **Playstyle**: Defensive with Honor Guard, token generation with Apprentice, scouting with Hunter

### Mid Campaign (Missions 6-15)
- **Unlock**: Duelist Champion (after 5 duel wins)
- **Unlock**: Forge Master (after forging 3 Ancestral Weapons)
- **Focus**: Specialized dueling or token economy
- **Playstyle**: Aggressive duelist or support-heavy token spam

### Late Campaign (Missions 16+)
- **Unlock**: Ancestral Spirit (after defeating Torrak)
- **Focus**: Deploy legendary unit, maximum power level
- **Playstyle**: Ancestral Spirit dominates battlefield, Casket supports

---

## FACTION SYNERGIES

| Allied Faction | Synergy | Anti-Synergy |
|----------------|---------|--------------|
| **Church** | Honor Guard protects self-harming Church pilots | Compete for melee range |
| **Dwarves** | Both defensive, Shield Wall + Bulwark = fortress | Both slow, lack mobility |
| **Ossuarium** | Tribal Hunter scouts for undead thralls | Honor code conflicts with necromancy |
| **Elves** | Forge Master creates lava, Elves avoid (no synergy) | Lava burns forests (Elves hate) |
| **Vestige** | Both pack-focused, Pack Tactics stack | None |
| **Emergent** | Tribal Hunter marks, Emergent swarm focuses | None |
| **Exchange** | Can hire Crucible mercenaries with Credits | None |
| **Nomads** | Both nomadic, mutual respect, Honor Guard + Nomad scouts = intelligence network | None |

---

## DESIGN PHILOSOPHY

### Identity: Honor Through Fire
- **Honor Code**: Duels are sacred, cowardice is unforgivable
- **Forge Worship**: Fire is holy, lava terrain empowers
- **Ancestral Legacy**: Weapons and warriors persist beyond death
- **Pack Structure**: Fight together, protect each other, honor lineage

### Gameplay Pattern
- **Forge Token Economy**: Generate tokens in lava, spend for powerful effects
- **Honor Duels**: Challenge enemies, punish cowards
- **Volcanic Terrain**: Create and control lava hexes
- **Ancestral Equipment**: Permanent upgrades across missions

### Counterplay
- **Refuse Duels**: Accept Coward's Mark, avoid 1v1 combat
- **Kill Token Generators**: Focus Forge Apprentice, Forge Master
- **Kiting**: Avoid melee range, use ranged attacks
- **AOE Damage**: Punish clustering around lava terrain
- **Destroy Lava Terrain**: Remove Forge token sources

---

## DESIGN NOTES

**Balance Targets**:
- Starter units: ~65% power of Casket (supportive, reliable)
- Unlockable units: ~75% power of Casket (specialized, powerful)
- Elite unit (Ancestral Spirit): ~85% power of Casket (legendary, game-changing)

**Core Fantasy**: "Honorable warriors who worship fire, forge legendary weapons, and never break oaths."

**Unique Mechanics**:
- **Honor Duel System**: Units can accept duels on behalf of Casket
- **Forge Token Sharing**: Units generate tokens for entire team
- **Ancestral Spirit**: Undying unit that returns after death
- **Coward's Mark Punishment**: Units specifically counter dishonorable enemies

**Next Steps**:
1. Playtest Honor Duel mechanics with support units
2. Balance Forge token generation (ensure not overpowered)
3. Test Ancestral Spirit survivability (50% damage reduction might be too strong)
4. Create visual reference cards for Tabletop Simulator

---

**"Fire conquers all. Honor binds us. Steel defines us."**

*Support units document version 1.0 (COMPLETE) - Crucible Packs*

---

[← Back to Crucible](deck-equipment-system.md) | [All Factions](../index.md) | [Rules: Support Units](../../rules/support-units.md)
