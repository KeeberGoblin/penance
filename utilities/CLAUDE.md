# CLAUDE.md
## AI Assistant Context Document for Penance: Absolution Through Steel

**Last Updated**: October 14, 2025
**Project Status**: PLAYTEST READY (v3.0 Optional Mechanics Complete)
**Purpose**: Complete context for AI assistants working on Penance

---

## Quick Start for AI Assistants

### What is Penance?

**Penance: Absolution Through Steel** is a tactical hex-based card game combining:
- **GKR: Heavy Hitters** (deck-as-HP system, SP economy)
- **Kingdom Death: Monster** (brutal progression, component destruction, event tables)
- **BattleTech** (component targeting, heat management)

**Setting**: Grimdark medieval fantasy 437 years after an apocalypse caused by the Theslar Engine. Dead pilots are bound to mechanical armored suits called **Caskets** to fight for redemption.

**Core Mechanic**: Your deck IS your HP (26-50 cards variable). Take damage → discard cards. Deck empty → reshuffle + add blank "Damage" cards (death spiral).

### Terminology Note: "Codex" = "codex"

**IMPORTANT**: When the user says "Codex", they mean the `docs/codex/` directory (HTML reference pages).

- **User says**: "Update the Codex navigation"
- **You update**: `docs/codex/index.html` navigation
- **Directory path**: `docs/codex/` (for technical file operations)
- **Thematic name**: "The Codex" (for user-facing communication)

---

## Critical Context: v2.0 Equipment System (October 11, 2025)

### Equipment System Changed

**OLD SYSTEM (Deprecated)**:
- Fixed 30-card decks
- 12 Primary Weapon cards (locked to Casket)
- 6 Secondary Equipment (choose 1 of 4)

**NEW SYSTEM (Current v2.0)**:
- **Variable deck size (26-50 cards)**
- Modular equipment: Weapon + Shield/Offhand + Accessories (1-4 slots)
- 60+ craftable/lootable equipment items
- **Deck composition**: `10 Universal + 6 Faction Core + X Equipment + 2 Tactics`

**Why It Changed**: User requested KDM-style crafting and salvage economy with equipment variety

### Current Playable Factions (4 Total)

1. **Church of Absolution** - Aggressive martyrdom (self-harm for burst damage)
2. **Dwarven Forge-Guilds** - Defensive tank (armor-piercing + rune stacking)
3. **The Ossuarium** - Lifesteal vampire (Soul Harvest, resurrections, Decay cards)
4. **Elven Verdant Covenant** - Hit-and-run assassin (Bleed stacking, mobility, regeneration)

**Files**: `docs/factions/{church,dwarves,ossuarium,elves}/deck-equipment-system.md`

---

## Faction Name Corrections (CRITICAL)

**User has corrected these faction names multiple times. DO NOT use old names:**

| ❌ NEVER USE | ✅ ALWAYS USE |
|-------------|--------------|
| "Undead Court" | **The Ossuarium** |
| "Bone-Courts" | **The Ossuarium** |
| "Twilight Courts" | **The Wyrd Conclave** |
| "Fae Courts" | **The Wyrd Conclave** |

---

## Core Game Systems

### Deck-as-HP System
```
Variable Deck Size: 26-50 cards (depends on equipment)
Take 6 damage → Discard top 6 cards from deck
Deck empty → Reshuffle discard + add 1 Damage card (blank dead draw)
Multiple reshuffles → Multiple Damage cards → Death spiral
```

**Exception**: Ossuarium uses **Decay cards** instead of Damage cards (have negative effects when drawn).

### Deck Composition Formula
```
Total = 10 Universal + 6 Faction Core + X Equipment + 2 Tactics

Where X Equipment = Weapon cards + Shield/Offhand cards + Accessory cards

Examples:
- Light Scout (26 cards): 10+6+8+2 = 26 (Dagger 3, Buckler 2, Sigil 3)
- Heavy Tank (38 cards): 10+6+20+2 = 38 (Warhammer 6, Tower Shield 4, 3 Sigils 10)
```

**Dwarven Exception**: Stone Endurance adds +2 cards (passive racial ability)

### Component Damage (KDM-Inspired)
```
When you discard Primary Weapon equipment cards from damage:
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
Light Caskets (Scout): 6 SP
Medium Caskets (Assault): 5 SP
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

---

## Version 3.0 Optional Mechanics (October 14, 2025)

**IMPORTANT**: v3.0 mechanics are **OPTIONAL ENHANCEMENTS** to the v2.0 base rules. All v3.0 systems can be used independently or ignored entirely. The base game works perfectly without them.

### Dice Pool Advantage (Trench Crusade-Inspired)
**File**: `docs/rules/dice-pool-advantage.md`

**Mechanics**:
- **Advantage**: Roll 3d6, take 2 highest (+17% hit chance, more dramatic crits)
- **Critical Advantage**: Roll 4d6, take 2 highest (triple EXECUTION chance)
- **Disadvantage**: Roll 3d6, take 2 lowest (-17% hit chance)
- **Critical Disadvantage**: Roll 4d6, take 2 lowest (severe penalty)

**When to Use**: Replace static +1/+2 modifiers with Advantage/Disadvantage for more dramatic swing potential

### Taint Exploitation (Tactical Resource System)
**File**: `docs/rules/taint-exploitation.md`

**Mechanics**:
- **Offensive Exploits** (spend enemy Taint): Force rerolls, give Disadvantage, cancel cards, stun (1-5 costs)
- **Desperate Power** (spend own Taint): +2 damage, reduce incoming damage, resurrect, gain SP (2-5 costs)
- **Corruption Threshold**: Still exists (10+ Taint = roll Corruption Save)

**Faction Interactions**:
- **Church**: Embrace Taint for martyrdom, Corruption Save 3+
- **Dwarves**: Gain Taint at half rate, cannot use Desperate Power
- **Ossuarium**: Thrive on Taint, "Soul Harvest" spends 2 Taint to recover 3 cards
- **Elves**: Gain Taint at double rate, Corruption Save 5+ in Forest only

### Pilot Grit (Campaign Stat 0-3)
**File**: `docs/campaigns/pilot-grit-system.md`

**Mechanics**:
- **Grit Stat**: 0 (rookie) to 3 (legendary veteran)
- **Grit Progression**: +1 per 5 missions survived, OR +1 when surviving Severe Injury
- **Grit Benefits**: Roll 1d6 + Grit to resist Pilot Wounds. On 5+, ignore 1 Wound.

**Faction Modifiers**:
- **Church**: Start with Grit 1, +1 to Wound saves
- **Dwarves**: +1 Grit when resisting Severe Injuries
- **Elves**: -1 Grit (fragile, easily traumatized)
- **Ossuarium**: Immune to Grit (already undead)

**Campaign Integration**: Soul Sacrifice grants +1 Grit permanently, Support Units gain +1 Morale when commanded by Grit 2+ pilots

---

## Campaign Systems

### Pilot Generation Tables
**File**: `docs/campaigns/pilot-generation-tables.md`

**5 Generation Tables**:
- Background (d20), Starting Traits (d20 - 40 total), Motivation (d20), Quirks (d100), Physical Appearance (d20)
- **Hybrid Trait System**: Roll twice on trait table for contradictory characters (RimWorld-inspired)
- **Probability**: 1 in 320 million for exact combination
- **Interactive Tool**: `docs/tools/pilot-generator.html` (JavaScript character generator)

### Settlement Phase Procedure
**File**: `docs/campaigns/settlement-phase-procedure.md`

**6-Step Process**:
1. **Return**: Casualties, salvage, loot distribution
2. **Income**: Building income, upkeep costs
3. **Event Roll**: d100 settlement event table
4. **Settlement Actions**: Build, craft, trade
5. **Pilot Care**: Medical treatment, injuries, Soul Sacrifice (optional)
6. **Preparation**: Assign pilots, build decks, depart

### Core Bestiary
**File**: `docs/enemies/bestiary-core.md`

**15 Enemies Total**:
- **3 Swarm (3-5 HP)**: Tainted Rat Swarm, Corrupted Villager, Scrap Drone
- **11 Elite/Boss (15-60 HP)**: Bandit Raider, Bandit Captain, Tainted Ogre, Scrap Golem, Engine Wraith, Tainted Leviathan, Rogue Casket, Bonelord Thresh, Church Zealot, Dwarven Ironclad, Elven Verdant Stalker
- **1 Special**: Tainted Wolf Pack (pack tactics)

**KDM-Style If-Then AI**: "If X, do Y. Else, do Z" behavior cards (no GM interpretation needed)
**Player-like Mechanics**: HP deck system, SP economy, Component Damage, death spiral

### Event Tables
**KDM-Style** (`docs/campaigns/event-tables-kdm-style.md`): 132 events, roll 2d6 separately (3+4 = "34" NOT "7")
**Anomalous/SCP-Style** (`docs/campaigns/anomalous-events-scp-style.md`): 100 artifacts, classifications Safe → Apollyon

---

## World Lore & Setting

### Timeline: 437 Years Since The Sundering

**Year 0**: The Theslar Engine activates. Dr. Nikolas Theslar's final transmission: "It's singing."
**Year 52**: First Casket prototype. Engineer Gareth volunteers: "I feel hollow without it."
**Year 437**: **Present Day** - 9 factions war across a shattered world.

### The Engine (Official Naming)

**Player-Facing Name**: **The Engine** (universal, simple - use in all rules/gameplay)
**Full Technical Name**: The Theslar Engine (T.E.)

**Faction-Specific Names** (for flavor text only):
- Church: "The Theslar Sin" | Dwarves: "Theslar's Folly" | Ossuarium: "The Ledger's Opening"
- Elves: "The Withering" | Wyrd Conclave: "The Unmaking" | Nomads: "The Break"

**Players don't need to memorize faction names** - just say "The Engine" during gameplay.

### Cosmology
**File**: `docs/lore/cosmology-and-origins.md`

**Three-Layered Cosmos**:
1. **The Material Realm** - Physical world where the game takes place
2. **The Veil** - Space between worlds, source of magic/ley lines
3. **The Deep** - Unknowable void, origin of eldritch entities

**Species Origins**:
- **Humans**: Natural evolution (magic-blind, 1 in 10,000 sensitive)
- **Elves**: Ley line incarnations from The Veil (immortal but sterile)
- **Dwarves**: Stone given consciousness by The Deep (earth-based hivemind)
- **Fae**: Reality-benders from The Veil (ageless tricksters)

### 9 Factions

**Playable**: Church of Absolution, Dwarven Forge-Guilds, The Ossuarium, Elven Verdant Covenant

**Design-Only** (not yet implemented): The Wyrd Conclave, Nomadic Scrap-Takers, Merchant Guilds, Blighted Packs, Chitinous Horde

---

## Repository Structure (Key Directories)

```
penance/
├── README.md                          # Main project overview
├── utilities/CLAUDE.md                # THIS FILE (AI assistant context)
│
├── docs/
│   ├── index.html                     # Interactive website (timeline, factions)
│   │
│   ├── rules/                         # Core mechanics
│   │   ├── turn-structure.md, combat-system.md, dice-reference.md
│   │   ├── dice-pool-advantage.md (v3.0), taint-exploitation.md (v3.0)
│   │   └── quick-reference.md
│   │
│   ├── factions/                      # Faction decks
│   │   ├── church/, dwarves/, ossuarium/, elves/
│   │   └── (each has deck-equipment-system.md)
│   │
│   ├── campaigns/                     # Long-term progression
│   │   ├── pilot-generation-tables.md, settlement-phase-procedure.md
│   │   ├── pilot-grit-system.md (v3.0), soul-sacrifice-variants.md
│   │   ├── event-tables-kdm-style.md, anomalous-events-scp-style.md
│   │   └── loot-tables.md
│   │
│   ├── enemies/                       # Bestiary
│   │   └── bestiary-core.md (15 enemies, KDM-style If-Then AI)
│   │
│   ├── tools/                         # Interactive tools
│   │   └── pilot-generator.html (JavaScript character generator)
│   │
│   ├── codex/                          # THE CODEX - Interactive reference (HTML)
│   │   ├── index.html (iframe navigation), manuscript-style.css
│   │   ├── rules-dice-pool.html (v3.0), rules-taint-exploitation.html (v3.0)
│   │   ├── campaign-pilot-grit.html (v3.0)
│   │   ├── faction-church.html, faction-dwarves.html, etc. (all have v3.0 sections)
│   │   └── (30+ total HTML pages)
│   │
│   └── reference/                     # Design docs
│       ├── equipment-pool-complete.md, faction-comparison-playtest.md
│       ├── casket-control-system.md (puppeteer capsule, body horror)
│       └── PLAYTEST-READY.md
```

---

## Key Design Files to Read First

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
9. `docs/campaigns/pilot-generation-tables.md` - Pilot generation
10. `docs/campaigns/bestiary-core.md` - Enemies

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

---

## Aesthetic & Art Direction

**Visual Style**: Baroque-Romanticist-Brutalist Fusion

### Key Influences
- **Baroque**: Ornate religious iconography, dramatic lighting
- **Romanticist**: Emotional intensity, sublime horror
- **Brutalist**: Raw concrete and steel, functional geometry

### Casket Designs
- Church Caskets: Gothic cathedrals in motion, stained glass cockpits
- Dwarven Caskets: Fortress-tanks, layered stone armor, rune etchings
- Ossuarium Caskets: Bone architecture, exposed ribcages, necrotic green glow
- Elven Caskets: Living wood and thorns, asymmetric organic growth

---

## Playtesting & Current Status

### Current Playtest Status
**Status**: PLAYTEST READY (v2.0 + v3.0 Optional Mechanics)

**What's Ready**:
- 4 complete faction decks with v3.0 modifiers
- 60+ equipment items
- 3 v3.0 optional systems (Dice Pool, Taint, Grit)
- 15-enemy bestiary with KDM-style AI
- Pilot generation system (5 tables, 320M combinations)
- 2 scenarios (Deathmatch, Objective Control)
- Quick reference sheet
- Interactive pilot generator tool
- 30+ HTML Codex pages

**What Needs Testing**:
- v3.0 optional mechanics balance
- Equipment system balance (deck size variance)
- Faction matchup win rates
- Enemy AI difficulty

---

## Quick Reference: Important Numbers

```
Default Deck Size: 26-50 cards (variable with equipment)
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
3. **Remember the equipment system is v2.0** - Variable decks, not fixed
4. **v3.0 is OPTIONAL** - All v3.0 mechanics are enhancements, not requirements
5. **Stay grimdark** - This is brutal fantasy, not heroic
6. **No emoticons** - User dislikes them

### When User Asks About...

**"How do I build a deck?"**
→ Point to faction deck-equipment-system.md files (show formula: 10+6+X+2)

**"What factions are playable?"**
→ 4 factions: Church, Dwarves, Ossuarium, Elves

**"How does combat work?"**
→ Point to `docs/rules/combat-system.md` (deck-as-HP core mechanic)

**"What's v3.0?"**
→ Optional enhancements: Dice Pool Advantage, Taint Exploitation, Pilot Grit

**"Can I playtest this?"**
→ Yes! Point to `docs/reference/PLAYTEST-READY.md` and scenarios

---

## Changelog for This Document

**October 14, 2025** - v3.0 Integration Complete
- Added Version 3.0 Optional Mechanics section (Dice Pool, Taint, Grit)
- All 23 files from audit updated with v3.0 cross-references
- Created 3 new HTML codex pages for v3.0 (rules-dice-pool, rules-taint-exploitation, campaign-pilot-grit)
- Updated all 4 faction HTML pages with v3.0 Taint/Grit modifiers
- Updated main website with v3.0 announcement
- Streamlined CLAUDE.md (removed redundant sections, consolidated deck composition)

**October 14, 2025** - Campaign Systems (In Progress - need scenario chains)
- Pilot Generation Tables (5 tables, 320M combinations, interactive tool)
- Core Bestiary (15 enemies, KDM-style If-Then AI)
- Settlement Phase Procedure (6 steps)
- 3 new Codex HTML pages (pilot generation, bestiary, settlement phase)
- Fixed terminology: "leg-skimming" → "Soul Sacrifice" (faction-specific variants)
- Fixed deck formula contradictions (30-card fixed → 26-50 variable)

**October 13, 2025** - The Codex Expansion
- Codex renamed to "The Codex" (thematic consistency)
- Campaign pages created (6 files: settlements, pilot progression, leg-skimming, events, anomalous, loot)
- Scenario pages created (4 files: all internal iframe pages)
- Emoticon removal (95+ instances replaced with text labels)
- Navigation reorganized (10 → 8 sections)

**October 12, 2025** - Codex System Complete
- All 9 faction pages manuscript-styled
- Cosmology & Origins created (three-layered cosmos)
- Engine naming system (universal "The Engine" + 9 faction-specific names)
- Equipment, Support Units, Scenarios codex pages
- Cross-platform responsive design

**October 11, 2025** - Initial Creation
- Comprehensive context document for AI assistants
- Covers equipment system v2.0, event tables, faction decks
- Includes user preferences, tone guidelines, common mistakes

---

**END OF DOCUMENT**

*"In iron we seek forgiveness. Through blood, absolution."*

*"The deck is your life. When it's empty, so are you."*
