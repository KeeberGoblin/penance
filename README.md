# Penance: Absolution Through Steel

A tactical hex-based card game of grimdark medieval fantasy mech combat where redemption is earned through brutal warfare.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue)

---

## Overview

**Penance: Absolution Through Steel** combines the tactical positioning of GKR: Heavy Hitters with the brutal progression and AI systems of Kingdom Death: Monster, wrapped in a deck-building framework. Pilot massive armored suits called **Caskets** powered by corrupting **Soulstones** as you fight for redemption in a dark medieval fantasy world.

### Core Pillars
- **Tactical Hex-Based Combat**: Positioning matters - facing, range, and terrain affect every decision
- **Deck-Building**: Your deck IS your Casket - each card represents equipment, actions, and battle damage
- **Push-Your-Luck Action Economy**: Safe operations or risk everything for more Soul-Points
- **Corruption System**: Power comes at a price - Soulstones grant strength but corrupt your pilot
- **Campaign Progression**: Persistent pilots, permanent injuries, workshop upgrades, and brutal consequences

---

## Game Modes

- **Arena (PvP)**: 1v1, 2v2, or FFA competitive battles
- **Campaign (Co-op)**: Story-driven progression with persistent characters
- **Raid (Boss Fight)**: Team up against massive AI-controlled monsters
- **Skirmish (Mixed)**: Objective-based gameplay with mission decks

---

## Casket Weight Classes

| Class | Weight | Soul-Points | Movement Focus |
|-------|--------|-------------|----------------|
| **Scout** | 500-800 lbs | 5 SP | Speed & Evasion |
| **Support** | 900-1,200 lbs | 4 SP | Team Buffs & Repairs |
| **Heavy** | 1,300-1,800 lbs | 3 SP | Armor & Sustained Fire |
| **Assault** | 1,900-2,500 lbs | 2 SP | Devastating Power |
| **Aberrant** | 600-1,500 lbs | 3 SP | Reality-Breaking Chaos |

---

## Key Mechanics

### Soul-Point (SP) System
Each Casket has a **Safe Zone** of Soul-Points they can spend per turn without consequence. Push into the **Danger Zone** for +2 SP, but risk rolling on the Strain Table - overheating, system failures, or worse.

### Soulstone Corruption
The crystalline hearts that power Caskets grant immense strength but accumulate **Taint**. Higher corruption unlocks forbidden abilities but risks transforming you into an Abomination.

### Directional Combat
Attacks from different hex facings have different effects:
- Shield arcs provide bonus defense
- Rear attacks are devastating
- Positioning is survival

### Monster AI Behavior Decks
Kingdom Death-inspired AI system - monsters have behavior decks that create unpredictable, emergent combat scenarios.

---

## Design Influences

- **GKR: Heavy Hitters** - Hex-based tactical positioning
- **Kingdom Death: Monster** - Brutal progression, AI behavior decks, permanent consequences
- **BattleTech/MechWarrior** - Weight class system, component damage
- **Deck-building games** - Your Casket is your deck
- **Escaflowne** - Mystical power sources in mechanical armor

---

## Project Status

**Early Development** - Core systems being designed

### Completed
- [x] Core concept and theme
- [x] Weight class system (5 classes)
- [x] Racial variants (7 races with unique mechanics)
- [x] Soul-Point action economy
- [x] Corruption/Soulstone mechanics
- [x] Game mode variety
- [x] Card anatomy and types
- [x] Damage and component system
- [x] Deck-as-health mechanics
- [x] Universal cards (10 base cards)
- [x] Victory conditions (all modes)
- [x] Interactive HTML reference site
- [x] Printable card templates

### In Progress
- [ ] Full equipment card catalog
- [ ] 3D printable Casket models

### Planned
- [ ] AI behavior decks (NPC pilots designed, behavior decks in progress)
- [ ] Mission deck system
- [ ] Monster bestiary (bestiary expansion needed)
- [ ] Playtest protocol & feedback system
- [ ] Art direction & final card designs
- [ ] Kickstarter campaign materials

### Recently Completed
- [x] Combat resolution mechanics (detailed) — [combat-resolution.md](docs/combat-resolution.md)
- [x] Workshop/campaign progression — [settlement-mechanics.md](docs/settlement-mechanics.md)
- [x] Terrain & environmental rules — [terrain-rules.md](docs/terrain-rules.md)
- [x] World-building systems (NPCs, factions, lore) — See World-Building section below

---

##  Quick Start

### Play Now
1. **Browse the Interactive Reference**: Open [tools/card-generator/index.html](tools/card-generator/index.html) in your browser
2. **Print & Play**: Open [tools/card-generator/printable-cards.html](tools/card-generator/printable-cards.html) to print test cards
3. **Read the Rules**: Check out [docs/CoreDesign.md](docs/CoreDesign.md) for complete game rules

See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions!

---

## Repository Structure

```
penance/
├── QUICKSTART.md                  # Start here!
├── docs/                          # Complete design documents
│   ├── CoreDesign.md              # Main rulebook
│   ├── world-lore.md              # Setting, factions, history
│   │
│   ├── Core Mechanics/
│   │   ├── card-anatomy.md        # Card design reference
│   │   ├── combat-resolution.md   # Combat & attack rules
│   │   ├── damage-system.md       # Injury & component damage
│   │   ├── deck-construction.md   # How to build legal decks
│   │   ├── turn-structure.md      # Turn-by-turn gameplay
│   │   ├── terrain-rules.md       # Environmental mechanics
│   │   └── universal-cards.md     # 10 base cards
│   │
│   ├── Campaign Systems/
│   │   ├── settlement-mechanics.md        # Base-building & progression
│   │   ├── resonance-engine-mechanics.md  # World threat system
│   │   └── faction-relationships.md       # Political web tracker
│   │
│   ├── World-Building/
│   │   ├── iconic-npcs.md         # 5 faction NPC pilots
│   │   ├── chronicle-entries.md   # 10 historical flavor texts
│   │   └── (more lore docs)
│   │
│   ├── Equipment & Cards/
│   │   ├── equipment-catalog.md   # Weapons & gear stats
│   │   ├── card-masterlist.md     # Complete card database
│   │   └── arena-scenarios.md     # PvP match setups
│   │
│   └── Reference/
│       ├── quick-reference.md     # One-page rules summary
│       ├── example-of-play.md     # Full turn walkthrough
│       └── missing-systems.md     # Development roadmap
│
├── tools/
│   └── card-generator/
│       ├── index.html             #  Interactive reference
│       ├── printable-cards.html   #  Print & play cards
│       └── README.md
├── cards/                         # Card designs (future)
├── assets/                        # Art & visual resources (future)
├── playtesting/                   # Playtest reports (future)
└── examples/                      # Sample decks & scenarios (future)
```

### Documentation Guide

**New Players**: Start with [QUICKSTART.md](QUICKSTART.md) → [CoreDesign.md](docs/CoreDesign.md) → [quick-reference.md](docs/quick-reference.md)

**Game Masters**: Read [world-lore.md](docs/world-lore.md) → [iconic-npcs.md](docs/iconic-npcs.md) → [settlement-mechanics.md](docs/settlement-mechanics.md)

**Campaign Players**: Focus on [settlement-mechanics.md](docs/settlement-mechanics.md) → [faction-relationships.md](docs/faction-relationships.md) → [resonance-engine-mechanics.md](docs/resonance-engine-mechanics.md)

---

## Contributing

This project is in early development. Feedback and playtesting notes are welcome! Please open an issue or discussion to share ideas.

---

## License

This work is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](LICENSE.md).

You are free to share and adapt this material for non-commercial purposes with attribution.

---

## Contact

- **GitHub**: [@KeeberGoblin](https://github.com/KeeberGoblin)
- **Project Repository**: https://github.com/KeeberGoblin/penance

---

*"In iron we seek forgiveness. Through blood, absolution."*
