# Wyrd Conclave - Support Units
## Penance: Absolution Through Steel

**Version**: 2.0 Equipment System
**Status**: ✅ **COMPLETE** - Full Framework with Behavior Decks
**Date**: October 17, 2025

The Wyrd Conclave deploys reality-bending illusions, stolen identities, and incomprehensible entities that break the rules of war.

---

## WYRD SUPPORT UNITS OVERVIEW

**Starting Units** (Available immediately):
1. **Shimmer Phantom** - Illusion decoy that confuses enemies
2. **Bargain Broker** - Generates Bargain tokens through deals
3. **Stolen Soldier** - Doppelganger wearing enemy's stolen face

**Unlockable Units** (Require campaign progression):
4. **Mirror Legion** - Self-replicating illusion army (Unlock: Make 10 bargains)
5. **Temporal Echo** - Time-displaced version of yourself (Unlock: Use Reality Fracture)
6. **The Un-Thing** - Incomprehensible entity from Feywild (Unlock: Defeat Lady Whisper)

**Limit**: Choose 1-3 support units (based on Casket Equipment Slots available)

**Design Philosophy**: Wyrd units defy logic. They create illusions, break game rules, force bargains, and manipulate reality in ways that shouldn't be possible.

---

## 1. SHIMMER PHANTOM ⭐ STARTER UNIT
**Category**: Illusion / Decoy
**HP**: 1 (Illusion - dies in one hit) | **Movement**: 8 | **Defense**: 0
**Equipment Slots**: 1
**Theme**: Perfect illusion of Casket that draws fire and confuses enemies

### Visual Description
Shimmer Phantom appears identical to your Casket, but ripples faintly (like heat mirage). Moves identically, attacks (but deals 0 damage), and even "takes damage" convincingly (fake sparks, fake screams). Only reveals it's an illusion when destroyed (dissolves into shimmer).

### Core Mechanics
- **Perfect Illusion**: Enemies cannot tell Phantom from real Casket (50/50 guess)
- **Decoy**: Draws enemy attacks (waste their SP)
- **0 Damage Attacks**: Phantom attacks but deals 0 damage (enemies don't know until hit)
- **Disposable**: Only 1 HP, but cheap to recreate (2 Bargain tokens)
- **Shimmer Death**: When destroyed, teleport real Casket to Phantom's location (swap positions)

### Behavior Deck (6 Cards)

#### 👥 MIMIC MOVEMENT
**Type**: Movement / Deception
**Priority**: High (when Casket moves)

**Effect**:
- Phantom copies Casket's last movement exactly (same hexes, same path)
- If Casket didn't move, Phantom moves toward nearest enemy (bait)
- Enemies targeting "you" have 50% chance to hit Phantom instead
- Phantom acts exactly like Casket (same animations, sounds)

**Flavor**: "Can you tell which one is real? Neither can they."

---

#### ⚔️ FALSE ASSAULT
**Type**: Attack / Deception
**Priority**: Medium (when adjacent to enemy)

**Effect**:
- Phantom attacks enemy for 0 damage (but enemy doesn't know yet)
- Phantom plays attack animation convincingly (swings weapon, yells)
- Enemy sees "you" attack (thinks it's real Casket)
- If enemy retaliates, destroys Phantom (reveals it was fake all along)

**Flavor**: "The blade passes through. Nothing was there."

---

#### 🔄 SHIMMER SWAP
**Type**: Utility / Teleport
**Priority**: Critical (when Phantom destroyed or Casket in danger)

**Effect**:
- Swap positions: Real Casket teleports to Phantom's hex, Phantom teleports to Casket's hex
- Then destroy Phantom (illusion ends)
- Enemies lose track of real you (confusion)
- Generate 1 Bargain token (successful deception)

**Flavor**: "Which one died? Neither. Both. You'll never know."

---

#### 🎭 MULTIPLY ILLUSION
**Type**: Utility / Duplication
**Priority**: Low (when no enemies adjacent)

**Effect**:
- Spend 2 Bargain tokens: Create 2nd Shimmer Phantom (now have 2 illusions)
- Both act independently (double deception)
- Enemies must guess which of 3 targets is real (33% chance)
- Illusions last until both destroyed

**Flavor**: "One becomes two. Two become legion. Legion becomes nightmare."

---

#### 🎯 BAIT AND PUNISH
**Type**: Tactical / Trap
**Priority**: High (when enemy targets Phantom)

**Effect**:
- If enemy attacks Phantom this turn:
  - Phantom is destroyed (reveals fake)
  - Real Casket immediately attacks that enemy (free attack, 4 damage)
  - Gain 1 Bargain token (they fell for it)
- Otherwise: Phantom moves to flank enemy

**Flavor**: "Strike the shadow. Face the blade."

---

#### 💨 PHASE THROUGH
**Type**: Movement / Evasion
**Priority**: Medium (when enemies block path)

**Effect**:
- Phantom moves through enemy-occupied hexes (illusion, no collision)
- Can pass through walls, terrain, anything (not real)
- Ends movement behind enemy lines (deep infiltration)
- Enemies waste SP chasing "you" (actually chasing nothing)

**Flavor**: "You cannot touch what isn't there."

---

### Strategic Use
- **Early Game**: Create confusion (enemies waste attacks on Phantom)
- **Mid Game**: Use Shimmer Swap for emergency escapes
- **Late Game**: Multiply Illusion for maximum chaos (3 targets = analysis paralysis)

---

## 2. BARGAIN BROKER ⭐ STARTER UNIT
**Category**: Support / Token Generator
**HP**: 10 | **Movement**: 4 | **Defense**: 2
**Equipment Slots**: 2
**Theme**: Fae merchant who makes deals with EVERYONE (allies, enemies, neutrals)

### Visual Description
Unsettling humanoid wearing mismatched stolen clothes (10 different eras). Face shifts constantly (never same twice). Carries ledger of debts (written in incomprehensible Fae script). Speaks in overlapping voices (sounds like 3 people talking at once).

### Core Mechanics
- **Deal Maker**: Offers bargains to allies AND enemies (both can accept)
- **Token Economy**: Generates 1-2 Bargain tokens per turn (passive)
- **Merchant's Protection**: Cannot be attacked by anyone who owes Bargain tokens
- **Debt Collector**: When units with debts die, collect their tokens (steal from corpses)
- **Walking Bank**: Stores up to 10 Bargain tokens, can transfer to Casket

### Behavior Deck (6 Cards)

#### 💰 OFFER BARGAIN (Ally)
**Type**: Support / Token Generation
**Priority**: High (when ally within 4 hexes needs help)

**Effect**:
- Offer bargain to ally: "I give you +2 damage this turn, you give me 1 Bargain token next turn."
- Ally AI automatically accepts if beneficial
- Ally gains buff, Broker marks them as "Debtor"
- Next turn, collect 1 token from that ally (debt paid)

**Flavor**: "Power now. Payment later. Always."

---

#### 🤝 OFFER BARGAIN (Enemy)
**Type**: Debuff / Coercion
**Priority**: High (when enemy within 6 hexes is wounded)

**Effect**:
- Offer bargain to enemy: "Stop attacking for 1 turn, I won't attack you. OR fight and take 3 damage from me."
- Enemy AI accepts if below 50% HP (self-preservation)
- If accepted: Enemy skips turn, Broker gains 2 Bargain tokens
- If refused: Broker attacks enemy for 3 damage

**Flavor**: "Survival or pride? Choose wisely."

---

#### 📊 DEBT COLLECTION
**Type**: Passive / Token Generation
**Priority**: Always active

**Effect**:
- Whenever any unit (ally or enemy) with Bargain debt dies:
  - Broker collects their debt (gain 2 Bargain tokens)
  - Transfer tokens to Casket immediately
- Whenever ally or enemy pays debt:
  - Broker gains +1 additional token (interest)

**Flavor**: "Death pays all debts. To me."

---

#### 🛡️ MERCHANT'S IMMUNITY
**Type**: Passive / Defense
**Priority**: Always active

**Effect**:
- Broker cannot be targeted by any unit that owes Bargain tokens
- This includes allies AND enemies (debts protect)
- If Casket has 5+ Bargain tokens, Broker gains +2 Defense (wealth = power)
- Immune to Fae Curse (fellow Fae, professional courtesy)

**Flavor**: "You owe me. You cannot harm your creditor."

---

#### 💸 FIRE SALE
**Type**: Utility / Discount
**Priority**: Low (when Casket has 0 Bargain tokens)

**Effect**:
- Broker offers "discount": All Bargain costs reduced by 1 (minimum 1) this turn
- Casket can play expensive cards cheaply (Stolen Face 3 → 2 tokens)
- After turn ends, Broker gains 1 Bargain token per discounted card played (profit)
- Once per mission (Fae generosity has limits)

**Flavor**: "Special offer. Today only. Terms apply."

---

#### 📜 BINDING CONTRACT
**Type**: Gambit / Control
**Priority**: Critical (when enemy is powerful threat)

**Effect**:
- Spend 5 Bargain tokens
- Force enemy into binding contract: "You cannot attack Casket for 2 turns."
- Enemy must obey (Fae magic binds)
- If enemy tries to attack, they take 5 damage (contract violation)
- Lasts 2 turns or until Broker dies (contract breaks)

**Flavor**: "Sign here. In blood. Metaphorically. Mostly."

---

### Strategic Use
- **Token Battery**: Broker generates tokens passively (1-2 per turn via bargains)
- **Ally Buffs**: Trade tokens for temporary power spikes
- **Enemy Control**: Force enemies into bad bargains (skip turns or die)
- **Protected Asset**: Cannot be killed while enemies owe debts (immune)

---

## 3. STOLEN SOLDIER ⭐ STARTER UNIT
**Category**: Infiltrator / Identity Thief
**HP**: 12 | **Movement**: 5 | **Defense**: 2
**Equipment Slots**: 2
**Theme**: Doppelganger wearing stolen face, fights using victim's own abilities

### Visual Description
Appears as perfect copy of enemy unit (face, voice, mannerisms). Only flaw: Eyes don't blink correctly (too slow, uncanny valley effect). Wears stolen clothes, wields stolen weapons. Occasionally "glitches" (face ripples, voice distorts).

### Core Mechanics
- **Stolen Identity**: Copies 1 enemy's appearance and abilities (choose at start of battle)
- **Perfect Disguise**: Enemies cannot tell Stolen Soldier from real unit (until attacked)
- **Ability Theft**: Can use copied enemy's cards (draw from their deck)
- **Betrayal Strike**: Deals bonus damage to units matching stolen identity (self-hatred)
- **Face Swap**: Can change stolen identity mid-battle (spend 3 Bargain tokens)

### Behavior Deck (6 Cards)

#### 🎭 STEAL FACE
**Type**: Utility / Theft
**Priority**: Critical (start of battle or when current face dies)

**Effect**:
- Choose 1 enemy within 8 hexes
- Copy their appearance perfectly (face, armor, weapon)
- Draw 2 random cards from their deck (add to Soldier's hand)
- Soldier can use those cards as if they were their own
- Lasts until Soldier changes face or battle ends

**Flavor**: "I am you now. Better than you."

---

#### ⚔️ BETRAYAL STRIKE
**Type**: Attack / Bonus Damage
**Priority**: High (when adjacent to enemy matching stolen face)

**Effect**:
- Attack enemy matching stolen identity (same faction/unit type)
- Deal 6 damage (traitor's blade cuts deep)
- That enemy takes -2 Defense this turn (confused by seeing "self")
- Gain 1 Bargain token (successful deception)

**Flavor**: "Look in the mirror. Die by your own hand."

---

#### 🤫 INFILTRATE
**Type**: Movement / Stealth
**Priority**: High (when no enemies adjacent)

**Effect**:
- Move up to 5 hexes toward enemy lines
- Enemies do not recognize Soldier as threat (looks like ally)
- Can move through enemy-occupied hexes (they think you're friendly)
- Once adjacent to target, reveal true nature (attack surprise)

**Flavor**: "I was always among you. You never noticed."

---

#### 🔄 FACE SWAP
**Type**: Utility / Transformation
**Priority**: Medium (when current face is ineffective or dead)

**Effect**:
- Spend 3 Bargain tokens
- Choose new enemy to copy (within 8 hexes)
- Discard old stolen cards, draw 2 new cards from new target's deck
- Change appearance to match new target
- All enemies lose track of "which one is the fake" (reset confusion)

**Flavor**: "That face bores me. I'll take yours."

---

#### 🎯 SOW DISCORD
**Type**: Debuff / Confusion
**Priority**: Medium (when 2+ enemies adjacent to each other)

**Effect**:
- Soldier positions between 2 enemies (looks like their ally)
- Both enemies have 50% chance to attack each other instead of Soldier (friendly fire)
- If enemies attack each other, Soldier gains 2 Bargain tokens (chaos profiteering)
- If they realize trick, Soldier takes damage normally

**Flavor**: "Aim carefully. That's your friend. Or is it?"

---

#### 💀 DEAD MAN'S HAND
**Type**: Passive / Theft
**Priority**: Always active

**Effect**:
- When enemy matching stolen face dies:
  - Permanently steal 1 random card from their deck
  - Add it to Soldier's deck (keep between missions)
  - Can use that card forever (stolen power)
- Soldier's deck grows with each kill (identity collection)

**Flavor**: "You're dead. I'll take your name, your face, your life. All mine."

---

### Strategic Use
- **Confusion Warfare**: Enemies can't tell friend from foe (waste attacks)
- **Ability Theft**: Use enemy's own cards against them (poetic justice)
- **Infiltration**: Get behind enemy lines disguised as "ally"
- **Permanent Growth**: Deck expands with each kill (scaling power)

---

## 4. MIRROR LEGION 🔒 UNLOCKABLE
**Unlock Condition**: Make 10 successful bargains in campaign
**Category**: Swarm / Self-Replication
**HP**: 5 each (but there are many) | **Movement**: 6 | **Defense**: 1
**Equipment Slots**: 2
**Theme**: Illusion army that duplicates itself endlessly

### Visual Description
Starts as 1 shimmering humanoid silhouette. Each turn, splits into 2 identical copies. By turn 5, there are 16 copies (exponential growth). All move in perfect sync, attack simultaneously, dissolve when hit (1 HP each).

### Core Mechanics
- **Self-Replication**: Splits into 2 copies each turn (1 becomes 2, 2 becomes 4, 4 becomes 8)
- **Exponential Growth**: By turn 5, there are 16+ Mirror Soldiers
- **Hive Mind**: All copies act simultaneously (move together, attack together)
- **Fragile**: Each copy has only 5 HP (die easily)
- **Illusion**: Enemies cannot tell which is "original" (all are equally real/fake)

### Key Abilities
1. **Mirror Split** (Passive): At start of each turn, each Mirror creates 1 duplicate at adjacent hex
2. **Swarm Attack** (2 SP): All Mirrors attack same target simultaneously (3 damage each × number of Mirrors)
3. **Fracture** (3 Bargain tokens): Create 4 Mirrors instantly (emergency reinforcement)
4. **Shatter** (Ultimate): Sacrifice all Mirrors, deal 2 damage per Mirror to all enemies in 6-hex radius (suicide bomb)

### Behavior Pattern
1. Split every turn (exponential growth)
2. Surround enemies (swarm tactics)
3. Attack in unison (overwhelm with numbers)
4. If reduced to 1 Mirror, retreat and rebuild (restart growth)

---

## 5. TEMPORAL ECHO 🔒 UNLOCKABLE
**Unlock Condition**: Use Reality Fracture ability
**Category**: Time Clone / Paradox
**HP**: Equal to Casket's current HP | **Movement**: Equal to Casket | **Defense**: Equal to Casket
**Equipment Slots**: 2
**Theme**: You from 3 turns ago, displaced through time

### Visual Description
Perfect copy of your Casket, but flickering (unstable temporal existence). Speaks in reverse (audio played backwards). Moves jerkily (skips frames like corrupted video). Attacks land "before" being thrown (time delay).

### Core Mechanics
- **Time Displaced**: Echo acts 1 turn in the past (resolves before Casket's turn)
- **Mirror Stats**: Has exact same HP, SP, deck as Casket had 3 turns ago (snapshot)
- **Paradox**: Echo and Casket cannot occupy same hex (temporal violation)
- **Unstable**: Each turn, roll 1d6. On 1, Echo vanishes (time corrects itself)
- **Doubled Actions**: Casket + Echo = 2 full turns per round (massive advantage)

### Key Abilities
1. **Temporal Duplicate** (Passive): Echo acts immediately before Casket's turn (free extra turn)
2. **Paradox Strike** (3 SP): If Echo and Casket attack same target, deal combined damage +4 (temporal echo)
3. **Time Collapse** (5 Bargain tokens): Merge Echo into Casket, heal 10 HP, gain all Echo's unspent SP (absorption)
4. **Rewind** (Ultimate, once): If Casket dies, Echo becomes "new" Casket (temporal replacement, survive death)

### Behavior Pattern
1. Echo acts before Casket (scout ahead, test enemy responses)
2. Casket exploits Echo's intel (attack weaknesses Echo revealed)
3. If Echo dies, no penalty (was already dead in original timeline)
4. If Casket dies, Echo continues (time paradox saves you)

---

## 6. THE UN-THING 🔒 UNLOCKABLE
**Unlock Condition**: Defeat Lady Whisper in campaign boss fight
**Category**: Eldritch Horror / Reality Violation
**HP**: 30 | **Movement**: 4 (floats) | **Defense**: 5
**Equipment Slots**: 3
**Theme**: Incomprehensible entity from Feywild that shouldn't exist in this dimension

### Visual Description
Cannot be accurately described (human perception fails). Appears as shifting mass of impossible geometry - too many angles, too few dimensions, colors that don't exist. Looking at it causes headaches. Smells like nostalgia and dread. Sounds like whispers in dead language.

### Core Mechanics
- **Incomprehensible**: Enemies have -2 to hit Un-Thing (cannot perceive correctly)
- **Reality Breach**: Un-Thing ignores all game rules (can move through walls, attack at any range, etc.)
- **Sanity Damage**: Enemies within 6 hexes lose 1 card per turn (mental strain from witnessing it)
- **Unkillable**: When reduced to 0 HP, returns to Feywild, comes back in 3 turns (banishment, not death)
- **Fae Pact**: Requires 10 Bargain tokens to summon (expensive, but devastating)

### Key Abilities
1. **Violation of Physics** (Passive): Un-Thing can move through terrain, units, obstacles (no collision)
2. **Madness Aura** (Passive): Enemies within 6 hexes draw 1 fewer card each turn (insanity)
3. **Unnatural Strike** (4 SP): Attack any enemy on map (infinite range, ignores line of sight)
4. **Reality Collapse** (Ultimate, 15 Bargain tokens): All enemies take 10 damage, terrain destroyed, game rules suspended for 1 turn (apocalypse)

### Behavior Pattern
1. Float toward densest enemy cluster (maximize Madness Aura)
2. Attack strongest enemy (Unnatural Strike ignores range)
3. Absorb attacks with high Defense (tank damage)
4. If banished, return in 3 turns (inevitable)

---

## STRATEGIC BUILDS

### Illusion Swarm (Maximum Confusion)
- **Units**: Shimmer Phantom + Mirror Legion
- **Strategy**: Flood battlefield with illusions (Phantom × 2 + Legion × 16 = 18 fake targets)
- **Strength**: Enemies paralyzed by indecision, waste all attacks
- **Weakness**: Vulnerable to AOE (clears illusions fast)

### Bargain Economy (Token Battery)
- **Units**: Bargain Broker + Temporal Echo
- **Strategy**: Broker generates tokens, Echo doubles actions (2 turns per round)
- **Strength**: Infinite resources, double action economy
- **Weakness**: Expensive (needs tokens to function)

### Identity Theft (Infiltration)
- **Units**: Stolen Soldier + Shimmer Phantom
- **Strategy**: Soldier infiltrates disguised as enemy, Phantom distracts
- **Strength**: Perfect deception, backstab potential
- **Weakness**: Weak if disguise blown early

### Eldritch Horror (Overwhelming Power)
- **Units**: The Un-Thing (solo, requires 3 equipment slots)
- **Strategy**: Summon Un-Thing, let it devastate battlefield alone
- **Strength**: Unstoppable single unit, ignores rules
- **Weakness**: Expensive (10 tokens to summon), fills all slots

---

## PROGRESSION SYSTEM

### Early Campaign (Missions 1-5)
- **Available**: Shimmer Phantom, Bargain Broker, Stolen Soldier
- **Focus**: Learn bargain economy, illusion tactics
- **Playstyle**: Defensive with deception

### Mid Campaign (Missions 6-15)
- **Unlock**: Mirror Legion (10 bargains), Temporal Echo (use Reality Fracture)
- **Focus**: Exponential growth (Legion swarm) or action economy (Echo double turns)
- **Playstyle**: Aggressive swarm or tactical doubling

### Late Campaign (Missions 16+)
- **Unlock**: The Un-Thing (defeat Lady Whisper)
- **Focus**: Deploy ultimate horror or maintain deception army
- **Playstyle**: Choose between Un-Thing solo or coordinated illusion swarm

---

## FACTION SYNERGIES

| Allied Faction | Synergy | Anti-Synergy |
|----------------|---------|--------------|
| **Church** | None (Church hates Fae) | Ideological incompatibility |
| **Dwarves** | None (Dwarves distrust bargains) | Contractual disputes |
| **Ossuarium** | Both exist "between" states | None |
| **Elves** | Shared dimensional interest | None |
| **Crucible** | None (honor vs. trickery clash) | Philosophical conflict |
| **Exchange** | Both value contracts/bargains | Fae exploit loopholes (Exchange dislikes) |
| **Nomads** | Fae find Nomad ingenuity amusing | Fae occasionally trick Nomads |
| **Vestige** | Fae fascinated by mutations | None |
| **Emergent** | Both manipulate reality/biology | None |

---

## DESIGN PHILOSOPHY

### Identity: Reality Merchants
- **Not evil, not good**: Fae are alien (human morality doesn't apply)
- **Bargains are compulsion**: Cannot resist making deals
- **Trickery is nature**: Deception is how they interact with world
- **Trapped**: Desperate to return to Feywild (drives all actions)

### Gameplay Pattern
- **Bargain Economy**: Generate and spend tokens for reality-warping effects
- **Illusion Warfare**: Create fake threats, confuse enemies
- **Identity Theft**: Steal faces, abilities, cards from enemies
- **Rule Breaking**: Cards that violate normal game mechanics (by design)

### Counterplay
- **AOE Attacks**: Clears illusions instantly (Mirror Legion, Shimmer Phantom vulnerable)
- **Burst Damage**: Kill before bargains stack (prevent token economy)
- **Refuse Bargains**: Don't accept deals (deny token generation)
- **High Intelligence**: See through illusions (some units ignore fakes)

---

**"We are the bargain. We are the price. We are inevitable."**

*Support units document version 1.0 (COMPLETE) - Wyrd Conclave*

---

[← Back to Wyrd Conclave](deck-equipment-system.md) | [All Factions](../index.md) | [Rules: Support Units](../../rules/support-units.md)
