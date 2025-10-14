# CLAUDE.md
## AI Assistant Context Document for Penance: Absolution Through Steel

**Last Updated**: October 14, 2025
**Project Status**: PLAYTEST READY (Campaign Systems + Bestiary Complete)
**Purpose**: This document provides complete context for AI assistants working on Penance

---

## Quick Start for AI Assistants

### What is Penance?

**Penance: Absolution Through Steel** is a tactical hex-based card game combining:
- **GKR: Heavy Hitters** (deck-as-HP system, SP economy)
- **Kingdom Death: Monster** (brutal progression, component destruction, event tables)
- **BattleTech** (component targeting, heat management)

**Setting**: Grimdark medieval fantasy 437 years after an apocalypse caused by the Resonance Engine. Dead pilots are bound to mechanical armored suits called **Caskets** to fight for redemption.

**Core Mechanic**: Your 30-card deck IS your HP. Take damage → discard cards. Deck empty → reshuffle + add blank "Damage" cards (death spiral).

### Terminology Note: "Codex" = "wiki"

**IMPORTANT**: When the user says "Codex", they mean the `docs/wiki/` directory (HTML reference pages). The directory is called `wiki` for pathing simplicity, but thematically it's referred to as "The Codex" in the UI and conversation.

- **User says**: "Update the Codex navigation"
- **You update**: `docs/wiki/index.html` navigation
- **Directory path**: `docs/wiki/` (for technical file operations)
- **Thematic name**: "The Codex" (for user-facing communication)

---

## Critical Context: System Overhaul v2.0

### IMPORTANT: Equipment System Changed (October 11, 2025)

**OLD SYSTEM (Deprecated)**:
- Fixed 30-card decks
- 12 Primary Weapon cards (locked to Casket)
- 6 Secondary Equipment (choose 1 of 4)

**NEW SYSTEM (Current)**:
- Variable deck size (26-50 cards)
- Modular equipment: Weapon + Shield/Offhand + Accessories (1-4 slots)
- 60+ craftable/lootable equipment items
- Deck composition: 10 Universal + 6 Faction Core + X Equipment + 2 Tactics

**Why It Changed**:
- User requested KDM-style crafting and salvage economy
- Wanted equipment variety and deck customization
- Previous fixed decks lacked replayability

### Current Playable Factions (4 Total)

1. **Church of Absolution** - Aggressive martyrdom (self-harm for burst damage)
2. **Dwarven Forge-Guilds** - Defensive tank (armor-piercing + rune stacking)
3. **The Ossuarium** - Lifesteal vampire (Soul Harvest, resurrections, Decay cards)
4. **Elven Verdant Covenant** - Hit-and-run assassin (Bleed stacking, mobility, regeneration)

**Files**:
- Church: `docs/factions/church/deck-equipment-system.md`
- Dwarves: `docs/factions/dwarves/deck-equipment-system.md`
- Ossuarium: `docs/factions/ossuarium/deck-equipment-system.md`
- Elves: `docs/factions/elves/deck-equipment-system.md`

---

## Faction Name Corrections (CRITICAL)

**User has corrected these faction names multiple times. DO NOT use old names:**

| ❌ NEVER USE | ✅ ALWAYS USE |
|-------------|--------------|
| "Undead Court" | **The Ossuarium** |
| "Bone-Courts" | **The Ossuarium** |
| "Twilight Courts" | **The Wyrd Conclave** |
| "Fae Courts" | **The Wyrd Conclave** |

**Note**: The word "court" is fine for other uses (e.g., "throne room court"), just not as a faction name.

---

## Core Game Systems

### Deck-as-HP System
```
30 cards = 30 HP
Take 6 damage → Discard top 6 cards from deck
Deck empty → Reshuffle discard pile + add 1 Damage card (blank dead draw)
Multiple reshuffles → Multiple Damage cards → Death spiral
```

**Exception**: Ossuarium uses **Decay cards** instead of Damage cards (have negative effects when drawn).

### Component Damage (KDM-Inspired)
```
When you discard Primary Weapon cards from damage:
1 Primary Weapon card = 1 Component Damage to specific location
Track by: Right Arm, Left Arm, Legs, Head, Chassis
3 Component Damage = Component DESTROYED

Destroyed Right Arm → Lose all Primary Weapon cards from hand (permanent)
Destroyed Legs → Movement costs +1 SP per hex
Destroyed Head → -1 to ranged attacks, no sensors
```

### SP Economy (Soul Points)
```
Each turn: Refresh SP to maximum
Light Caskets: 6 SP
Medium Caskets: 5 SP
Heavy Caskets: 4 SP
Fortress Caskets: 3 SP

Actions cost SP: Move (1 SP/hex), Play cards (variable), Attacks (built into cards)
```

### Heat System
```
Safe Zone (0-4 Heat): No penalties
Danger Zone (5+ Heat): Roll Strain at turn start
Strain failures: Lose SP, take damage, component malfunctions
```

### Equipment Slots by Casket Class
| Casket | SP | Weapon | Shield/Offhand | Accessories | Total Equipment |
|--------|----|----|---|---|---|
| Scout (Light) | 6 | 1 | 1 | 1 | 8-12 cards |
| Assault (Medium) | 5 | 1 | 1 | 2 | 12-18 cards |
| Heavy | 4 | 1 | 1 | 3 | 15-24 cards |
| Fortress | 3 | 1 (2-handed) | 1 | 4 | 18-30 cards |

### Smelting & Salvage
```
Smelting: Remove equipment from deck → Gain 1 Scrap per 2 cards
Salvage: After defeating enemy, roll 1d20 → 15+ = Loot 1 equipment card
Crafting: Costs 2-6 Scrap per item depending on complexity
```

---

## Campaign Systems

### Event Tables (KDM-Style)
**File**: `docs/campaigns/event-tables-kdm-style.md`

**Mechanics**:
- Roll 2d6 separately (3+4 = "34" NOT "7")
- 132 total events (66 Departure + 66 Arrival)
- Doubles (11, 22, 33, 44, 55, 66) = Catastrophic or Legendary
- Examples:
  - **11**: "The Offering" (sacrifice) or "Hero's Welcome"
  - **66**: "The End Times" (catastrophe) or "The Miracle"

### Anomalous Events (SCP-Style)
**File**: `docs/campaigns/anomalous-events-scp-style.md`

**Containment Breach Table (1d20)**:
- Safe (1-6): Minor anomalies
- Euclid (7-12): Moderate threats
- Keter (13-17): Major breaches
- Apollyon (18-19): Extinction-level
- Thaumiel (20): Reality-altering (double-edged)

**Artifact Discovery Table (1d100)**:
- 100 unique anomalous artifacts
- Classifications: Safe → Euclid → Keter → Apollyon → Thaumiel
- Examples:
  - "The Soulstone of Nikolas Theslar" (+10 SP, user absorbed into Engine)
  - "The Weeping Casket" (grows organic tissue, painful mutations)
  - "The Doppelganger Soulstone" (quantum superposition, user dies in alternate timelines)

### Pilot Generation Tables
**File**: `docs/campaigns/pilot-generation-tables.md`

**5 Generation Tables**:
- **Background (d20)**: 20 origins (Soldier, Criminal, Priest, Noble, etc.)
- **Starting Traits (d20)**: 40 traits total (20 simple +1/-1, 20 complex unique abilities)
- **Motivation (d20)**: 20 narrative hooks (Redemption, Revenge, Duty, Greed, etc.)
- **Quirks (d100)**: 100 roleplay flavor traits (Prays before missions, Collects trinkets, etc.)
- **Physical Appearance (d20)**: 20 descriptors (Scarred, Tattooed, Missing eye, etc.)

**Hybrid Trait System (RimWorld-Inspired)**:
- Roll twice on trait table for contradictory characters
- Example: Reckless + Cautious = aggressive opener with defensive retreat
- Creates depth and narrative hooks

**Probability**: 1 in 320 million for exact combination (every pilot is statistically unique)

**Interactive Tool**: `docs/tools/pilot-generator.html`
- Random Roll mode (instant generation)
- Manual Select mode (pick-and-choose with probability display)
- Copy to clipboard functionality
- Gothic red/gold aesthetic

### Settlement Phase Procedure
**File**: `docs/campaigns/settlement-phase-procedure.md`

**6-Step Process**:
1. **Return**: Casualties, salvage, loot distribution
2. **Income**: Building income, upkeep costs, debt
3. **Leg-Skimming**: Permanent sacrifices for power
4. **Pilot Care**: Medical treatment, injuries
5. **Settlement Events**: Roll on event tables
6. **Preparation**: Build, craft, recruit, depart

**Tracking**: Settlement sheet, pilot roster, treasury, building roster

### Core Bestiary
**File**: `docs/enemies/bestiary-core.md`

**15 Enemies Total**:
- **3 Swarm (3-5 HP)**: Tainted Rat Swarm, Corrupted Villager, Scrap Drone
- **11 Elite/Boss (15-60 HP)**: Bandit Raider, Bandit Captain, Tainted Ogre, Scrap Golem, Engine Wraith, Tainted Leviathan, Rogue Casket, Bonelord Thresh, Church Zealot, Dwarven Ironclad, Elven Verdant Stalker
- **1 Special**: Tainted Wolf Pack (pack tactics)

**KDM-Style If-Then AI**:
- "If X, do Y. Else, do Z" behavior cards
- Example: "If within melee range, attack. Else, move closer."
- Easy to execute, no GM interpretation needed

**Player-like Mechanics**:
- HP deck system (enemies use decks like players)
- SP economy (3-6 SP depending on enemy type)
- Component Damage (enemies can have limbs destroyed)
- Death spiral (reshuffle adds Damage cards)

**Mission Templates**:
- Swarm Mission: 8-12 low-HP enemies
- Elite Mission: 2-3 mid-HP enemies
- Boss Mission: 1 high-HP enemy with phase-based AI
- Settlement Defense: Waves of mixed enemies

**Loot Tables**: Credits, Scrap, Equipment rolls per enemy defeated

---

## Version 3.0 Optional Mechanics (October 14, 2025)

**IMPORTANT**: v3.0 mechanics are **OPTIONAL ENHANCEMENTS** to the v2.0 base rules. All v3.0 systems can be used independently or ignored entirely. The base game works perfectly without them.

### Dice Pool Advantage (Trench Crusade-Inspired)
**File**: `docs/rules/dice-pool-advantage.md`

**Purpose**: Replace static +1/+2 modifiers with roll-more-dice system for more dramatic swing potential.

**Mechanics**:
- **Advantage**: Roll 3d6, take 2 highest (+17% hit chance, more dramatic crits)
- **Critical Advantage**: Roll 4d6, take 2 highest (triple EXECUTION chance)
- **Disadvantage**: Roll 3d6, take 2 lowest (-17% hit chance)
- **Critical Disadvantage**: Roll 4d6, take 2 lowest (severe penalty)

**When to Use**:
- Replace long range penalties (+2) with Disadvantage
- Replace flanking bonuses (-1) with Advantage
- Works with existing Attack Dice symbols (STRIKE, DOUBLE STRIKE, EXECUTION)

**Integration**:
- `combat-system.md` mentions Dice Pool as optional in Step 2 (attack resolution)
- `range-and-los.md` mentions Dice Pool for range modifiers
- `quick-reference.md` has Dice Pool conversion table

### Taint Exploitation (Tactical Resource System)
**File**: `docs/rules/taint-exploitation.md`

**Purpose**: Make Taint a tactical offensive/defensive resource instead of just a corruption threshold.

**Mechanics**:
- **Offensive Exploits** (spend enemy Taint to debuff them):
  - 1 Taint: Force enemy to reroll 1 die
  - 2 Taint: Give enemy Disadvantage on next roll
  - 3 Taint: Cancel enemy card (costs 1 SP to play)
  - 4 Taint: Stun enemy (lose 1 SP next turn)
  - 5 Taint: Enemy skips next activation

- **Desperate Power** (spend your own Taint for emergency boosts):
  - 2 Taint: +2 damage to next attack
  - 3 Taint: Reduce incoming damage by 4
  - 4 Taint: Resurrect at 5 HP (once per mission)
  - 5 Taint: Gain +3 SP this turn

- **Corruption Threshold**: Still exists (10+ Taint = roll Corruption Save)
- **Taint Accumulation**: Still gain Taint from damage (3 damage = 1 Taint)

**Faction Interactions**:
- **Church**: Embrace Taint for martyrdom, Corruption Save 3+ (zealotry protects)
- **Dwarves**: Gain Taint at half rate (runic protection), cannot use Desperate Power
- **Ossuarium**: Thrive on Taint, "Soul Harvest" spends 2 Taint to recover 3 cards, Corruption Save 5+
- **Elves**: Gain Taint at double rate (fragile), Corruption Save 5+ only in Forest terrain

**Integration**:
- All 4 faction files have "VERSION 3.0 OPTIONAL: Taint Interactions" sections
- `combat-system.md` mentions Taint Exploitation in Pilot Wound section
- `turn-structure.md` should mention Taint Marker tracking in Refresh Phase

### Pilot Grit (Campaign Stat 0-3)
**File**: `docs/campaigns/pilot-grit-system.md`

**Purpose**: Represent pilot mental toughness and experience growth through campaign play.

**Mechanics**:
- **Grit Stat**: 0 (rookie) to 3 (legendary veteran)
- **Starting Grit**: 0 for new pilots, 1 for veterans
- **Grit Progression**: +1 per 5 missions survived, OR +1 when surviving Severe Injury
- **Grit Benefits**: Roll 1d6 + Grit to resist Pilot Wounds. On 5+, ignore 1 Wound.
- **Veteran Resilience**: Grit 3 pilots have 50% chance to ignore Wounds (roll 4-6 = ignore)

**Faction Modifiers**:
- **Church**: Start with Grit 1 (hardened by faith), +1 to Wound saves
- **Dwarves**: +1 Grit when resisting Severe Injuries (stoic endurance)
- **Elves**: -1 Grit (fragile, easily traumatized), PTSD more common
- **Ossuarium**: Immune to Grit (already undead, no mental resilience mechanic)

**Campaign Integration**:
- **Soul Sacrifice** (leg-skimming) grants +1 Grit permanently (trauma survived)
- **Support Units** gain +1 Morale when commanded by Grit 2+ pilots (veterans inspire confidence)
- **Pilot Progression**: Grit tracks on pilot sheet (checkboxes 0-1-2-3)

**Integration**:
- `pilot-progression.md` has v3.0 Grit System section at top, renamed "Survivor's Grit" scar to "Survivor's Tenacity"
- `soul-sacrifice-variants.md` includes "+1 Grit" in Universal Benefits
- `support-units.md` mentions Grit synergy (Morale bonus, effective commands)
- `combat-system.md` mentions Grit for Wound saves

### Design Philosophy: Why v3.0 Exists

**Inspiration**: Trench Crusade's Blood Marker system and resilience mechanics

**Goals**:
1. **More Dramatic Swings** - Dice Pool Advantage creates exciting crits and fumbles
2. **Tactical Depth** - Taint Exploitation adds resource management layer
3. **Veteran Recognition** - Pilot Grit mechanically rewards survival

**User Can Choose**:
- Use all 3 systems together
- Use only 1-2 systems (mix and match)
- Ignore v3.0 entirely (v2.0 base rules work perfectly)

---

## Complete Equipment Pool

**File**: `docs/reference/equipment-pool-complete.md`

**60+ Equipment Items**:

### Weapons (15+)
- **Light**: Dagger (3 cards), Pistol (3), Hand Axe (4)
- **Medium**: Longsword (6), Spear (5), Mace (5), Crossbow (5)
- **Heavy**: Greatsword (8), Warhammer (6), Halberd (7), Rifle (6)
- **Exotic**: Chain Whip (6), Flail (5)

### Shields/Offhand (6+)
- Buckler (2), Kite Shield (3), Tower Shield (4)
- Dueling Dagger (2), Repair Kit (3)

### Plating (4+)
- Ablative (3), Spike (2), Reinforced (3), Stealth (3)

### Sigils (12+)
- Universal: Repair (2), Heat Sink (2), Targeting (3)
- Faction-Exclusive: 8 unique sigils

**Equipment Card Counts Matter**:
- Light weapon (3 cards) = fast cycle, frequent access
- Heavy weapon (8 cards) = slow cycle, but dominates deck when drawn

---

## World Lore & Setting

### Timeline: 437 Years Since The Sundering

**Year 0**: The Theslar Engine activates. Dr. Nikolas Theslar's final transmission: "It's singing."
**Year 52**: First Casket prototype. Engineer Gareth volunteers: "I feel hollow without it."
**Year 78**: Bonelord Thresh opens The Ledger (soul contracts).
**Year 134**: The Great Schism (Church civil war, 80 years).
**Year 223**: Betrayal at Roothold (Church burns elven forests).
**Year 437**: **Present Day** - 9 factions war across a shattered world.

### The Engine (Official Naming)
**File**: `docs/lore/resonance-engine-names.md`

**Player-Facing Name**: **The Engine** (universal, simple - use in all rules/gameplay)
**Full Technical Name**: The Theslar Engine (T.E.)
**Historical Term**: The Resonance Engine (pre-Sundering scientific jargon)

**Faction-Specific Names** (for flavor text and NPC dialogue):
- Church: "The Theslar Sin" (divine punishment)
- Dwarves: "Theslar's Folly" (engineering failure)
- Ossuarium: "The Ledger's Opening" (their genesis moment)
- Elves: "The Withering" (ecological catastrophe)
- Wyrd Conclave: "The Unmaking" (reality rupture)
- Nomads: "The Break" / "Old Nik's Bomb" (irreverent)
- Merchants: "The Theslar Recession" (economic collapse)
- Blighted: "The Mutation Dawn" (evolutionary awakening)
- Chitinous: "The Emergence" (hive-mind birth)

**Players don't need to memorize faction names** - just say "The Engine" during gameplay.

### Cosmology & Species Origins
**File**: `docs/lore/cosmology-and-origins.md`

**Three-Layered Cosmos**:
1. **The Material Realm** - Physical world where the game takes place
2. **The Veil** - Space between worlds, source of magic/ley lines
3. **The Deep** - Unknowable void, origin of eldritch entities

**The Cataclysm Cycle**: Has happened **three times total** (including the current one):
- 1st Ending (50,000 BCE): Flood - Survivors: primitive humans, nascent elves
- 2nd Ending (10,000 BCE): Fire - Volcanic superchains, ley line destabilization
- 3rd Ending (Year 0): Void - The Theslar Engine activation (current state)

**Species Origins**:
- **Humans**: Natural evolution (identical to real Earth), magic-blind (1 in 10,000 sensitive)
- **Elves**: Ley line incarnations from The Veil, immortal but sterile (cannot reproduce)
- **Dwarves**: Stone given consciousness by The Deep, earth-based hivemind
- **Fae**: Reality-benders from The Veil, ageless tricksters with no true form
- **Draconids** (extinct): Ancient species that predicted the Cataclysm cycle, vanished

### 9 Factions (5 Unplayable, Design-Only)

**Playable**:
1. Church of Absolution
2. Dwarven Forge-Guilds
3. The Ossuarium
4. Elven Verdant Covenant

**Design-Only** (not yet implemented):
5. The Wyrd Conclave (fae reality-benders)
6. Nomadic Scrap-Takers (improvised salvage engineers)
7. Merchant Guilds (economic warfare)
8. Blighted Packs (mutation weaponization)
9. Chitinous Horde (hive-mind arthropods)

### The Puppeteer Capsule (Control Interface)
**File**: `docs/reference/casket-control-system.md`

- Pilot sits in gel-filled capsule
- Neural threads pierce spine (12 connection points)
- Soulstone embedded in pilot's chest
- Disconnection causes permanent nerve damage
- Body horror aesthetic: pilot becomes part of machine

### Leg-Skimming (Permanent Sacrifice)
**File**: `docs/campaigns/leg-skimming.md`

- Pilots can burn parts of their soul for immediate power
- Permanent consequences (reduce max HP, SP, etc.)
- 80+ unique pilot scars
- Once skimmed, cannot be undone

---

## Repository Structure

```
penance/
├── README.md                          # Main project overview
├── CLAUDE.md                          # THIS FILE (AI assistant context)
├── SYSTEM-OVERHAUL-SUMMARY.md         # Oct 11, 2025 equipment system changes
├── PLAYTEST-READY.md                  # Playtest package overview
│
├── docs/
│   ├── index.html                     # Interactive website (timeline, factions)
│   │
│   ├── rules/                         # Core mechanics
│   │   ├── turn-structure.md          # 4-phase SP system
│   │   ├── combat-system.md           # Deck-as-HP, component damage
│   │   ├── deck-construction.md       # How to build decks
│   │   ├── range-and-los.md           # Hex movement, facing, LOS
│   │   ├── terrain.md                 # Elevation, cover
│   │   └── quick-reference.md         # 1-page printable
│   │
│   ├── factions/                      # Faction decks
│   │   ├── church/
│   │   │   └── deck-equipment-system.md       # Church v2.0 (NEW)
│   │   ├── dwarves/
│   │   │   └── deck-equipment-system.md       # Dwarves v2.0 (NEW)
│   │   ├── ossuarium/
│   │   │   └── deck-equipment-system.md       # Ossuarium (NEW - Oct 11)
│   │   └── elves/
│   │       └── deck-equipment-system.md       # Elves (NEW - Oct 11)
│   │
│   ├── cards/                         # Card database
│   │   ├── index.html                 # Interactive card browser
│   │   ├── universal.md               # 10 Universal Core cards
│   │   ├── masterlist.md              # Complete card list
│   │   └── anatomy.md                 # How to read cards
│   │
│   ├── scenarios/                     # Playtest scenarios
│   │   ├── 01-proving-grounds.md      # Deathmatch (beginner)
│   │   ├── 02-reliquary-ruins.md      # Objective Control (intermediate)
│   │   ├── example-of-play.md         # 5-turn walkthrough
│   │   └── boss-iron-saint.md         # Boss encounter (HP deck system)
│   │
│   ├── lore/                          # World & story
│   │   ├── world-overview.md          # The Sundering, 9 factions
│   │   ├── chronicle.md               # 437-year timeline
│   │   ├── iconic-npcs.md             # 5 legendary pilots
│   │   ├── resonance-engine.md        # The artifact that ended the world
│   │   ├── resonance-engine-names.md  # Faction-specific Engine names
│   │   └── cosmology-and-origins.md   # Three-layered cosmos, species origins
│   │
│   ├── campaigns/                     # Long-term progression
│   │   ├── settlements.md             # Base building
│   │   ├── settlement-phase-procedure.md  # 6-step settlement phase (NEW - Oct 14)
│   │   ├── pilot-progression.md       # Scars, traits, death
│   │   ├── pilot-generation-tables.md # 5 tables, hybrid traits (NEW - Oct 14)
│   │   ├── leg-skimming.md            # Permanent sacrifice mechanics
│   │   ├── loot-tables.md             # Post-mission rewards
│   │   ├── event-tables-kdm-style.md  # 132 KDM-style events
│   │   └── anomalous-events-scp-style.md  # SCP-style anomalies
│   │
│   ├── enemies/                       # Bestiary (NEW - Oct 14)
│   │   └── bestiary-core.md           # 15 enemies, KDM-style If-Then AI
│   │
│   ├── tools/                         # Interactive tools (NEW - Oct 14)
│   │   └── pilot-generator.html       # JavaScript character generator
│   │
│   ├── reference/                     # Design docs
│   │   ├── core-design.md             # Design philosophy
│   │   ├── playtest-assessment.md     # Development progress
│   │   ├── equipment-pool-complete.md # 60+ equipment items (NEW)
│   │   ├── faction-comparison-playtest.md  # Faction comparison (NEW)
│   │   ├── casket-control-system.md   # Puppeteer capsule (body horror)
│   │   ├── ai-art-prompts.md          # Baroque-romanticist-brutalist aesthetic
│   │   └── PLAYTEST-READY.md          # Detailed playtest package
│   │
│   └── wiki/                          # THE CODEX - Interactive reference (HTML)
│       ├── index.html                 # Codex homepage (iframe navigation)
│       ├── content-home.html          # Codex main content page
│       ├── manuscript-style.css       # Gothic manuscript stylesheet
│       │
│       ├── cosmology.html             # Cosmology page
│       ├── lore-sundering.html        # The Sundering lore
│       ├── lore-engine.html           # Resonance Engine
│       ├── lore-chronicle.html        # 437-year chronicle
│       ├── lore-npcs.html             # Iconic pilots
│       │
│       ├── rules-turn-structure.html  # Turn structure
│       ├── rules-combat.html          # Combat & damage system
│       ├── rules-range-los.html       # Range & line of sight
│       ├── rules-dice.html            # Dice reference
│       ├── rules-quick-ref.html       # Quick reference
│       │
│       ├── faction-church.html        # Church of Absolution
│       ├── faction-dwarves.html       # Dwarven Forge-Guilds
│       ├── faction-undead.html        # The Ossuarium
│       ├── faction-elves.html         # Elven Verdant Covenant
│       ├── faction-fae.html           # The Wyrd Conclave (unplayable)
│       ├── faction-nomads.html        # Nomad Collective (unplayable)
│       ├── faction-merchants.html     # Merchant Guilds (unplayable)
│       ├── faction-blighted.html      # Blighted Packs (unplayable)
│       ├── faction-chitinous.html     # Chitinous Ascendancy (unplayable)
│       │
│       ├── equipment-decks.html       # Equipment & deck building
│       ├── support-units.html         # Support units system
│       │
│       ├── scenarios.html             # Scenario overview
│       ├── scenario-proving-grounds.html      # 1v1 deathmatch scenario (NEW - Oct 13)
│       ├── scenario-reliquary-ruins.html      # Objective control scenario (NEW - Oct 13)
│       ├── scenario-boss-iron-saint.html      # Boss encounter (NEW - Oct 13)
│       ├── scenario-example-of-play.html      # 5-turn walkthrough (NEW - Oct 13)
│       │
│       ├── campaign-settlement-phase.html     # 6-step settlement phase (NEW - Oct 14)
│       ├── campaign-settlements.html          # Settlement building (NEW - Oct 13)
│       ├── campaign-pilot-generation.html     # Pilot generation tables (NEW - Oct 14)
│       ├── campaign-pilot-progression.html    # Pilot scars & traits (NEW - Oct 13)
│       ├── campaign-leg-skimming.html         # Permanent sacrifice (NEW - Oct 13)
│       ├── campaign-event-tables.html         # 132 KDM-style events (NEW - Oct 13)
│       ├── campaign-anomalous-events.html     # 100 SCP-style artifacts (NEW - Oct 13)
│       ├── campaign-loot-tables.html          # Complete loot system (NEW - Oct 13)
│       └── enemies-bestiary.html              # Core bestiary overview (NEW - Oct 14)
│
└── tools/                             # Development utilities
    ├── card-generator/                # Card template generator
    └── generate-tts-deck.py           # Tabletop Simulator integration
```

---

## Key Design Files to Read First

When starting work on Penance, read these files in order:

### Phase 1: Understand Core Systems (30 min)
1. `README.md` - Project overview
2. `docs/rules/turn-structure.md` - How turns work
3. `docs/rules/combat-system.md` - Deck-as-HP, component damage
4. `docs/reference/equipment-pool-complete.md` - Equipment system

### Phase 2: Study Faction Asymmetry (20 min)
5. `docs/factions/church/deck-equipment-system.md` - Church faction
6. `docs/factions/dwarves/deck-equipment-system.md` - Dwarves faction
7. `docs/reference/faction-comparison-playtest.md` - Faction balance

### Phase 3: Campaign & Progression (15 min)
8. `docs/campaigns/event-tables-kdm-style.md` - Event tables
9. `docs/campaigns/leg-skimming.md` - Permanent sacrifice
10. `docs/campaigns/anomalous-events-scp-style.md` - SCP-style horror

### Phase 4: World & Lore (15 min)
11. `docs/lore/world-overview.md` - 437-year history
12. `docs/reference/casket-control-system.md` - Puppeteer capsule (body horror)

---

## User Preferences & Tone Guidelines

### Writing Style
- **NO EMOTICONS** - User has explicitly requested no emojis/emoticons
- **Stay in-theme** - Grimdark medieval fantasy tone
- **Concise** - User prefers brief, direct communication
- **Technical accuracy** - User catches mechanical inconsistencies

### Content Approach
- User wants **brutal, unforgiving mechanics** (KDM-inspired)
- Permanent consequences matter (pilot death, component destruction, scars)
- Asymmetric faction design is critical (each faction plays completely differently)
- Replayability through randomness (event tables, loot, artifacts)

### Communication Style Examples

**Good**:
> "The Church faction gains +1 damage per enemy killed (permanent). This scales infinitely."

**Bad**:
> "The Church faction is super cool! 😊 They get stronger as they kill enemies, which is awesome! 🔥"

**Good**:
> "Component Destruction occurs when 3 Primary Weapon cards are discarded from damage. This is permanent."

**Bad**:
> "Oh no! If you take too much damage to your weapon, it breaks! 😱 Be careful!"

---

## Recent Conversation History (October 11, 2025)

### What Was Changed Today

**User's Request**:
"Can you make a claude.md or update the current one with all up to date materials that would help out"

**Context**: User wants a comprehensive context document for future AI assistants working on Penance. This document (CLAUDE.md) is the result.

### Previous Session Summary

**Major Work Completed (October 11, 2025)**:
1. Equipment system overhaul (fixed → modular, 60+ items)
2. Faction name corrections (Ossuarium, Wyrd Conclave)
3. Event tables created (132 KDM-style events)
4. SCP-style anomalous events (100 artifacts)
5. Two new faction decks (Ossuarium, Elves)
6. Documentation index updated (fixed sticky header, added DATABASE link)

**User Explicitly Corrected**:
- Faction names ("Undead Court" → "The Ossuarium")
- Equipment should be for Caskets (machines), not traditional armor → Use "Plating" and "Sigils"
- Wanted KDM-style crafting economy, not fixed decks

---

## Common Mistakes to Avoid

### 1. Using Old Faction Names
❌ "The Bone-Courts attack..."
✅ "The Ossuarium attacks..."

### 2. Referring to Deprecated Fixed Deck System
❌ "Each Casket has 12 fixed Primary Weapon cards..."
✅ "Each Casket equips a weapon (3-9 cards depending on weapon type)..."

### 3. Using Traditional Armor Terminology
❌ "Equip Plate Armor for +3 Defense"
✅ "Equip Reinforced Plating for +3 Defense"

### 4. Forgetting Deck-as-HP is Core Mechanic
❌ "When you take damage, reduce your HP counter..."
✅ "When you take damage, discard cards from the top of your deck..."

### 5. Not Specifying Equipment Card Counts
❌ "Equip the Longsword"
✅ "Equip the Longsword (6 cards)"

---

## Balance & Design Philosophy

### Faction Win Conditions

**Church of Absolution**: Alpha strike burst (self-harm → massive damage → kill fast)
**Dwarven Forge-Guilds**: Attrition tank (outlast, armor-pierce, stack runes)
**The Ossuarium**: Lifesteal vampire (sustain, resurrections, drain HP)
**Elven Verdant Covenant**: Hit-and-run DoT (stack Bleed infinitely, kite)

### Difficulty Ranking
1. **Easiest**: Dwarves (straightforward tank, forgiving)
2. **Medium**: Church (requires timing Blood Offering correctly)
3. **Medium**: Ossuarium (resource management, resurrection timing)
4. **Hardest**: Elves (requires precise positioning, Bleed stacking)

### Expected Win Rates (1v1 Matchups)
- Church vs Dwarves: 55/45 Church favor (burst vs tank)
- Ossuarium vs Elves: 60/40 Ossuarium favor (sustain vs DoT)
- Church vs Ossuarium: 50/50 (burst vs lifesteal)
- Dwarves vs Elves: 45/55 Elves favor (slow vs mobile)

---

## Technical Details: Deck Composition Formula

### Standard Deck Composition
```
Total Deck Size = 10 Universal + 6 Faction Core + X Equipment + 2 Tactics

Where X Equipment = Weapon + Shield/Offhand + Accessories
```

### Examples

**Light Striker (Scout, 26 cards)**:
- 10 Universal Core
- 6 Faction Core (e.g., Church)
- 8 Equipment (Dagger 3 + Buckler 2 + Sigil 3)
- 2 Tactics (choose 2 from 5 available)
- **Total: 26 cards**

**Heavy Tank (Heavy Casket, 38 cards)**:
- 10 Universal Core
- 6 Faction Core (e.g., Dwarves)
- 20 Equipment (Warhammer 6 + Tower Shield 4 + 3 Sigils 10)
- 2 Tactics
- **Total: 38 cards**

**Dwarven Exception**: Stone Endurance adds +2 cards (passive)
- Dwarf Heavy Tank = 40 cards instead of 38

---

## Card Anatomy & Structure

### Universal Core (10 Cards - Everyone Has These)
1. **MOVE** (×3): 1 SP, Move 2 hexes
2. **SPRINT** (×2): 2 SP, Move 4 hexes, +1 Heat
3. **BRACE** (×2): 1 SP, +2 Defense until next turn
4. **DISENGAGE** (×1): 1 SP, Move 2 hexes, ignore attacks of opportunity
5. **FOCUS** (×1): 0 SP, Draw 1 card
6. **EMERGENCY REPAIR** (×1): 3 SP, Recover 3 cards from discard

### Faction Core (6 Cards - Faction-Specific)
Each faction has 6 unique Core cards that define their playstyle.

**Example - Church Faction Core**:
1. **BLOOD OFFERING**: 0 SP, Discard 2 cards (self-harm), next attack +3 damage
2. **MARTYRDOM PROTOCOL**: 2 SP, Redirect damage from ally to yourself
3. **RIGHTEOUS FURY**: Passive, +1 damage per enemy killed (permanent)
4. **DIVINE JUDGMENT**: 4 SP, Deal 8 damage, ignore Defense
5. **CONSECRATED GROUND**: 3 SP, Create 3-hex zone (allies heal 1 card/turn)
6. **LAST RITES**: 0 SP, When reduced to 0 HP, deal 10 damage to killer

### Equipment Cards (Variable)
Each equipment item has 3-9 unique cards.

**Example - Longsword (6 cards)**:
1. **SLASH**: 2 SP, Melee, Deal 4 damage
2. **THRUST**: 2 SP, Melee, Deal 3 damage, +2 if attacking front arc
3. **PARRY**: 0 SP, Reactive, Reduce damage by 2, next attack +1 damage
4. **RIPOSTE**: 1 SP, Reactive, When attacked in melee, deal 3 damage to attacker
5. **POMMEL STRIKE**: 1 SP, Melee, Deal 2 damage, target loses 1 SP next turn
6. **GUARD STANCE**: 2 SP, Defense, +2 Defense until next turn

### Tactics (Choose 2 from 5)
Each faction has 5 available Tactics. Players choose 2 before each mission.

**Example - Church Tactics**:
1. **FORCED MARCH** (×1): 1 SP, All allies gain +1 Movement this turn
2. **ZEALOUS ASSAULT** (×1): 3 SP, All allies gain +2 damage this turn, +1 Heat
3. **SHIELD WALL** (×1): 2 SP, All adjacent allies gain +2 Defense this turn
4. **BLOOD PACT** (×1): 0 SP, Discard 3 cards, recover 3 ally cards
5. **SECOND WIND** (×1): 2 SP, Recover 4 cards from discard

---

## Aesthetic & Art Direction

**Visual Style**: Baroque-Romanticist-Brutalist Fusion

### Key Influences
- **Baroque**: Ornate religious iconography, dramatic lighting
- **Romanticist**: Emotional intensity, sublime horror
- **Brutalist**: Raw concrete and steel, functional geometry

### Casket Designs (from `ai-art-prompts.md`)
- Church Caskets: Gothic cathedrals in motion, stained glass cockpits, religious martyrdom
- Dwarven Caskets: Fortress-tanks, layered stone armor, rune etchings
- Ossuarium Caskets: Bone architecture, exposed ribcages, necrotic green glow
- Elven Caskets: Living wood and thorns, asymmetric organic growth

### Color Palettes
- **Church**: Crimson blood-red, gold, white marble
- **Dwarves**: Iron gray, forge-orange, deep earth brown
- **Ossuarium**: Bone white, necrotic green, shadow black
- **Elves**: Forest green, thorn-black, bioluminescent blue

---

## Playtesting & Feedback

### Current Playtest Status
**Status**: PLAYTEST READY (v2.0 Equipment System)

**What's Ready**:
- 4 complete faction decks
- 60+ equipment items
- 2 scenarios (Deathmatch, Objective Control)
- Quick reference sheet
- Example of Play (5-turn walkthrough)

**What Needs Testing**:
- Equipment system balance (deck size variance)
- Event table frequency
- Faction matchup win rates
- Casket class balance (Scout vs Fortress)

### Expected Playtest Duration
- First game (learning rules): 90-120 minutes
- Second game (familiar): 60-75 minutes
- Experienced players: 45-60 minutes

---

## Future Development Roadmap

### Short-Term (Next 1-2 Months)
- [ ] Playtest feedback integration
- [ ] Balance adjustments (equipment costs, SP economy)
- [ ] Visual card templates (printable)
- [ ] Additional scenarios (3-4 more)

### Medium-Term (3-6 Months)
- [ ] Campaign scenario chain (10-mission arc)
- [ ] 5 additional faction decks (Wyrd Conclave, Nomads, Merchants, Blighted, Horde)
- [ ] Boss AI behavior decks
- [ ] 3D printable Casket models (STL files)

### Long-Term (6-12 Months)
- [ ] Art commissioning (baroque-romanticist-brutalist style)
- [ ] Full campaign rulebook
- [ ] Monster bestiary (non-Casket enemies)
- [ ] Kickstarter campaign materials
- [ ] Tabletop Simulator mod (official)

---

## Useful Commands & Scripts

### Generate TTS Deck
```bash
python3 tools/generate-tts-deck.py --faction church --output tts_deck.json
```

### Search for Faction References
```bash
grep -r "Bone-Courts\|Twilight Courts" docs/
```

### Validate Card Counts
```bash
# Count total cards in a faction deck
grep "^###" docs/factions/church/deck-equipment-system.md | wc -l
```

### Update Index HTML
```bash
# Location of main documentation page
docs/index.html
```

---

## Contact & Repository Info

- **GitHub**: [@KeeberGoblin](https://github.com/KeeberGoblin)
- **Repository**: https://github.com/KeeberGoblin/penance
- **Website**: https://keebergoblin.github.io/penance/
- **License**: CC BY-NC-SA 4.0 (Creative Commons, Non-Commercial)

---

## Quick Reference: Important Numbers

```
Default Deck Size: 30 cards (26-50 variable with equipment)
Default Hand Size: 6 cards
Default SP: 5 (varies by Casket class: 3-6)
Heat Safe Zone: 0-4 (5+ = Danger Zone)
Component Destruction Threshold: 3 Component Damage
Salvage Success: 15+ on 1d20
Smelting Ratio: 1 Scrap per 2 cards
Reshuffles Add: 1 Damage card per reshuffle (death spiral)
```

---

## Final Notes for AI Assistants

### When Working on Penance

1. **Always check faction names** - Use Ossuarium and Wyrd Conclave
2. **Reference equipment by card count** - "Longsword (6 cards)"
3. **Remember the equipment system is NEW** - Don't refer to old fixed decks
4. **Stay grimdark** - This is brutal fantasy, not heroic
5. **No emoticons** - User dislikes them
6. **Check SYSTEM-OVERHAUL-SUMMARY.md** - For recent changes

### When User Asks About...

**"How do I build a deck?"**
→ Point to `docs/rules/deck-construction.md` and equipment system formula

**"What factions are playable?"**
→ 4 factions: Church, Dwarves, Ossuarium, Elves (see faction-comparison-playtest.md)

**"How does combat work?"**
→ Point to `docs/rules/combat-system.md` (deck-as-HP core mechanic)

**"What's changed recently?"**
→ Point to `SYSTEM-OVERHAUL-SUMMARY.md` (Oct 11, 2025 equipment overhaul)

**"Can I playtest this?"**
→ Yes! Point to `PLAYTEST-READY.md` and scenarios in `docs/scenarios/`

---

## Changelog for This Document

**October 14, 2025** - Pilot Generation System, Core Bestiary, Interactive Tools
- **Pilot Generation Tables Created**: Comprehensive 5-table system (Background, Traits, Motivation, Quirks, Appearance)
  - docs/campaigns/pilot-generation-tables.md (15+ pages)
  - 40 total traits (20 simple +1/-1, 20 complex unique abilities)
  - Hybrid trait system: Roll twice for contradictory characters (RimWorld-inspired)
  - Probability calculations: 1 in 320 million for exact combination
  - Example pilot generation walkthrough (Brother Tomas "The Zealot")
- **Interactive Pilot Generator Tool**: JavaScript-powered HTML tool
  - docs/tools/pilot-generator.html
  - Random Roll mode (instant pilot generation)
  - Manual Select mode (pick-and-choose with probability calculator)
  - Copy to clipboard functionality
  - Gothic red/gold aesthetic matching Codex theme
- **Core Bestiary System Created**: 15 enemies with KDM-style If-Then AI
  - docs/enemies/bestiary-core.md (20+ pages)
  - 3 Swarm enemies (3-5 HP): Tainted Rat Swarm, Corrupted Villager, Scrap Drone
  - 11 Elite/Boss enemies (15-60 HP): Bandit Raider, Bandit Captain, Tainted Ogre, Scrap Golem, Engine Wraith, Tainted Leviathan, Rogue Casket, Bonelord Thresh, Church Zealot, Dwarven Ironclad, Elven Verdant Stalker
  - 1 Special enemy: Tainted Wolf Pack (pack tactics)
  - Player-like mechanics (HP deck, SP economy, Component Damage)
  - Mission templates (Swarm, Elite, Boss, Settlement Defense)
  - Loot tables per enemy type
- **Settlement Phase Procedure**: 6-step settlement process between missions
  - docs/campaigns/settlement-phase-procedure.md
  - Return → Income → Leg-Skimming → Pilot Care → Events → Preparation
  - Tracking sheets for settlement, pilots, treasury, buildings
  - Example playthrough walkthrough
- **Codex HTML Pages Created**: Manuscript-styled overview pages
  - docs/wiki/campaign-settlement-phase.html (flowchart visualization)
  - docs/wiki/campaign-pilot-generation.html (compact tables, probability display)
  - docs/wiki/enemies-bestiary.html (enemy cards, mission templates)
- **Codex Navigation Updated**: Added 3 new pages to Campaign section
  - Settlement Phase Procedure (first item in Campaign section)
  - Pilot Generation Tables (after Settlements)
  - Core Bestiary (after Leg-Skimming)
- **Hidden Boss Encounter Created**: Dr. Teslar boss battle (before this session)
- **Terminology Clarification**: Added to utilities/CLAUDE.md
  - "Codex" = "wiki" directory (thematic name vs technical path)
  - Directory: docs/wiki/ (for file operations)
  - UI name: "The Codex" (for user communication)

**October 13, 2025** - The Codex (Wiki Renamed), Campaign & Scenario Pages, Navigation Reorganization
- **Wiki Renamed to "The Codex"**: More thematic name, updated throughout site (main nav, footer)
- **Campaign Pages Created (6 files)**: All comprehensive HTML iframe pages with manuscript theme
  - campaign-settlements.html (Settlement building system, 14 buildings across 3 tiers)
  - campaign-pilot-progression.html (Pilot scars, 4 categories + faction-specific)
  - campaign-leg-skimming.html (Permanent sacrifice mechanics)
  - campaign-event-tables.html (132 KDM-style events, 2d6 system)
  - campaign-anomalous-events.html (100 SCP-style artifacts, 1d20 + 1d100 tables)
  - campaign-loot-tables.html (Complete loot system, rarity tiers, crafting)
- **Scenario Pages Created (4 files)**: All internal iframe pages (no more GitHub links)
  - scenario-proving-grounds.html (1v1 deathmatch)
  - scenario-reliquary-ruins.html (Objective control)
  - scenario-boss-iron-saint.html (Boss encounter with HP deck system)
  - scenario-example-of-play.html (Complete 5-turn walkthrough)
- **Emoticon Removal (95+ instances)**: All emoticons replaced with text labels
  - Buildings: [FORGE], [MILITARY], [MEDICAL], [ECONOMIC], [SHRINE], [ARSENAL], [WORKSHOP], [REFINERY], [ARCHIVE], [WATCH], [RELIC], [FOUNDRY], [SANCTUARY], [COUNCIL]
  - Dice: [SHIELD], [BLOOD], [CRITICAL], [PIERCE], [HEAT], [STRIKE], [DOUBLE STRIKE], [GLANCE], [JAM], [ABSORB], [DEATH BLOW]
- **Theme Consistency Fixed**: All campaign pages now use manuscript-style.css (was incorrectly using manuscript-content.css)
- **Navigation Reorganized (10 → 8 sections)**:
  - OLD: 1.Lore 2.Rules 3.Playable Factions 4.Equipment 5.Support Units 6.Scenarios 7.Campaign 8.Design Only 9.Playtest 10.External
  - NEW: 1.Lore 2.Rules 3.Playable Factions 4.Equipment & Building 5.Scenarios 6.Campaign 7.Unplayable Factions 8.Resources
  - Support Units merged into Equipment & Building (better organization)
  - Scenarios now all internal iframe pages (no external GitHub links)
  - "Design Only" renamed to "Unplayable Factions" (clearer naming)
  - Playtest + External consolidated into "Resources"
- **Godray Effect Archived**: Performance issues, removed from main page, archived to utilities/archived-effects/
- **Current Codex Status**: 30+ comprehensive HTML pages, all internal, consistent manuscript theme

**October 13, 2025** - Main index manuscript theme overhaul and UI enhancements
- **Manuscript Theme Made Default**: Removed brutalist theme entirely, gothic manuscript is now the only theme
- **Theme Toggle Removed**: Simplified UI by removing theme switching button and JavaScript
- **Dripping Oil/Ink Border**: Replaced geometric border with organic dripping effect from top edge (13 drips)
- **PenanceBG.png Opacity**: Set to 15% for subtle background texture without overwhelming content
- **Scroll-to-Top Button**: Added fixed bottom-right button (appears after 500px scroll)
- **Gothic Typography**: Cinzel Decorative for headings, Crimson Pro for body text (now default)
- **Enhanced Buttons & Cards**: Aged gold borders, gradient backgrounds, manuscript styling throughout
- **Color Palette Unified**: All elements use parchment (#d4c5b0), aged gold (#b8956a), blood-red (#4a0e0e)
- **Footer Updated**: Changed from "brutalist conviction" to "forged in gothic manuscript tradition"
- **Repository Structure Updated**: Wiki pages now include equipment-decks.html, support-units.html, scenarios.html

**October 12, 2025** - Equipment, Support Units, and Scenarios wiki pages
- **Equipment & Decks Wiki Page**: Complete equipment pool (60+ items), crafting costs, smelting/salvage system
- **Support Units Wiki Page**: 6 support unit types (Penitent Squad, Ironclad Sentinel, Bone Thralls, Verdant Stalker, Forge Golem, Scrap Hauler)
- **Scenarios Wiki Page**: Complete walkthroughs of Proving Grounds and Reliquary Ruins scenarios, dice combat examples
- **Navigation Updated**: All Equipment, Support Units, and Scenarios links now use iframe loading instead of GitHub external links
- **Manuscript Styling**: All new pages use consistent gothic parchment aesthetic with centered content

**October 12, 2025** - Wiki completion, cosmology integration, Engine naming
- **Wiki System Complete**: All 9 faction pages converted to manuscript styling (gothic parchment aesthetic)
- **Iframe Navigation Fixed**: Full-height matching eliminates scrolling issues
- **Cosmology & Origins Created**: Three-layered cosmos (Material/Veil/Deep), species origins, Cataclysm cycle
- **Engine Naming System**: "The Engine" for gameplay, faction-specific names for flavor (9 variations)
- **Drop-cap Fix**: Centered quote text no longer misaligned
- **Cross-Platform Responsive**: Wiki pages now work on mobile/tablet (3 breakpoints added)
- **Design-Only Factions Styled**: Wyrd Conclave, Nomads, Merchants, Blighted, Chitinous now have manuscript pages
- **Project Genesis Timeline**: Added 2005-2024 development history to wiki home page

**October 12, 2025** - Contradiction fixes and repository cleanup
- Fixed "Elven Remnants" → "Elven Verdant Covenant" in 7 files
- Added deprecation notices to `deck-complete.md` files (legacy fixed-deck system)
- Corrected pilot physical states in manuscript prompts (Church/Elves NOT skeletons)
- Created comprehensive contradiction report (CONTRADICTION-REPORT.md)
- Note: `deck-complete.md` files are kept for historical reference but marked deprecated

**October 11, 2025** - Initial creation
- Comprehensive context document for AI assistants
- Covers equipment system v2.0, event tables, faction decks
- Includes user preferences, tone guidelines, common mistakes
- Repository structure, design philosophy, balance notes

---

**END OF DOCUMENT**

*"In iron we seek forgiveness. Through blood, absolution."*

*"The deck is your life. When it's empty, so are you."*
