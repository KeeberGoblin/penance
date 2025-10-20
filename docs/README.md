# Penance Documentation Hub

Welcome to the complete documentation for **Penance: Absolution Through Steel**.

---

## Quick Start

**[PLAYTEST-READY Package](reference/PLAYTEST-READY.md)** - Everything you need for your first game

**New to Penance?** Start here:
1. Read the [Playtest Package](reference/PLAYTEST-READY.md)
2. Choose a faction: [Church](factions/church/deck-equipment-system.md), [Dwarves](factions/dwarves/deck-equipment-system.md), [Ossuarium](factions/ossuarium/deck-equipment-system.md), or [Elves](factions/elves/deck-equipment-system.md)
3. Play [The Proving Grounds](scenarios/01-proving-grounds.md) scenario
4. Reference the [Quick Sheet](rules/quick-reference.md) during play

---

## Documentation Sections

### [Rules](rules/)
Core game mechanics - turn structure, combat, deck building, terrain
- [Turn Structure](rules/turn-structure.md)
- [Combat System](rules/combat-system.md) (Deck-as-HP + Component Damage)
- [Deck Construction](rules/deck-construction.md)
- [Range & Line of Sight](rules/range-and-los.md)
- [Support Units](rules/support-units.md) (GKR-inspired AI companions)
- [Terrain Rules](rules/terrain.md)
- [Quick Reference](rules/quick-reference.md)

### [Factions](factions/)
Playable factions with complete deck lists and lore
- [Church of Absolution](factions/church/deck-equipment-system.md) - Aggressive martyrdom
  - [Church Support Units](factions/church/support-units.md) - 6 units with behavior decks
- [Dwarven Forge-Guilds](factions/dwarves/deck-equipment-system.md) - Fortress defender
  - [Dwarven Support Units](factions/dwarves/support-units.md) - 6 units with behavior decks
- [The Ossuarium](factions/ossuarium/deck-equipment-system.md) - Lifesteal vampire
  - [Ossuarium Support Units](factions/ossuarium/support-units.md) - 6 units with behavior decks
- [Elven Verdant Covenant](factions/elves/deck-equipment-system.md) - Hit-and-run assassin
  - [Elven Support Units](factions/elves/support-units.md) - 6 units with behavior decks
- [Faction Relationships](factions/relationships.md)
- [Casket Types](factions/casket-types.md) - 36 unique designs

### [Cards](cards/)
Complete card database and references
- [Interactive Card Browser](cards/index.html) - Color-coded, filterable
- [Universal Core Cards](cards/universal.md) - 10 cards everyone has
- [Master Card List](cards/masterlist.md)
- [Card Anatomy](cards/anatomy.md)

### [Scenarios](scenarios/)
Playtest scenarios and example games
- [01: The Proving Grounds](scenarios/01-proving-grounds.md) - Deathmatch (beginner)
- [02: Reliquary Ruins](scenarios/02-reliquary-ruins.md) - Objective Control (intermediate)
- [Example of Play](scenarios/example-of-play.md) - 5-turn walkthrough
- [Boss: The Iron Saint](scenarios/boss-iron-saint.md) - Co-op boss fight

### [Lore](lore/)
World-building, history, and narrative
- [World Overview](lore/world-overview.md) - The Sundering and the Remnants
- [Chronicle](lore/chronicle.md) - 437-year timeline
- [Iconic NPCs](lore/iconic-npcs.md) - 5 legendary pilots
- [Theslar Engine](lore/theslar-engine-mechanics.md) - The artifact that ended the world

### [Campaigns](campaigns/)
Long-term progression systems
- [Settlements](campaigns/settlements.md) - Base building between missions
- [Pilot Progression](campaigns/pilot-progression.md) - Scars, traits, death
- [Leg Skimming](campaigns/leg-skimming.md) - Sacrifice HP for power
- [Loot Tables](campaigns/loot-tables.md) - Post-mission rewards

### [Reference](reference/)
Design documents and creator tools
- [PLAYTEST-READY.md](reference/PLAYTEST-READY.md) - Detailed playtest guide
- [Core Design](reference/core-design.md) - Game philosophy
- [Playtest Assessment](reference/playtest-assessment.md) - Development progress
- [AI Art Prompts](reference/ai-art-prompts.md) - Visual generation guide
- [Tabletop Simulator Guide](reference/tabletop-simulator-guide.md)
- [3D Printable System](reference/3d-printable-system.md)

### [Simulation](../simulation/)
Combat simulator and balance testing tools
- [Combat Simulator (v5.14)](../simulation/README.md) - Complete deck combat with dice mechanics
- [V5.14 Implementation Results](V5.14-COMPLETE-DECK-IMPLEMENTATION.md) - Latest balance analysis
- **Features:**
  - Custom 2d6 attack dice + 1d6 defense dice system
  - Resource economy tracking (Credits, Biomass, Faith, Forge, Bleed)
  - All 10 factions with complete deck system (faction + universal + equipment cards)
  - 225-battle test suite (~3 minutes runtime)
- **Current Status:** 1/10 factions balanced (45-55% WR range)

---

## Interactive Sites

- **[Main Website](index.html)** - Timeline, faction overview, playtest section
- **[Card Database](cards/index.html)** - Interactive, filterable, color-coded cards
- **[Codex](codex/index.html)** - Comprehensive game reference

---

## Game At A Glance

**Penance** is a tactical hex-based card game combining:
- **GKR: Heavy Hitters** - Deck-as-HP, SP economy
- **Kingdom Death: Monster** - Component destruction, brutal progression
- **BattleTech** - Heat management, mech customization
- **Grimdark Medieval Fantasy** - 437 years after the apocalypse

**Core Loop**: Build 30-card deck → Fight in hex arena → Take damage = discard cards → Component destruction → Death spiral → Campaign progression

---

[← Back to Repository](https://github.com/KeeberGoblin/penance)
