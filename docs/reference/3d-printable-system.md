# 3D Printable Modular Casket System
## Penance: Absolution Through Steel

**Version**: 0.1
**Last Updated**: October 8, 2025

---

## Vision

Create an open, modular 3D printable system where:
- Players download a **standardized Core Casket frame**
- Community designs and shares **custom weapons, armor, and equipment**
- All parts use **universal attachment points** (like LEGO compatibility)
- Anyone can print, customize, and share their unique builds
- Official repository curates balanced, tournament-legal designs

**Goal**: Make Penance accessible, customizable, and community-driven.

---

## Core Casket Frame (Official Release)

### Included Components

**Chassis Parts** (Standardized):
1. **Torso/Body** - Central piece with visible Soulstone chamber
2. **Legs** (2 pieces) - Multiple pose variants:
   - Standing (neutral)
   - Walking/striding (dynamic)
   - Charging (aggressive)
   - Bracing (defensive)
3. **Hip Joint** - Connection between torso and legs
4. **Hex Base** - 28mm hex base with weight class markings

**Attachment Points** (Standardized Sockets):
1. **Right Arm Socket** - Universal ball joint or peg system
2. **Left Arm Socket** - Matching universal connection
3. **Back Mount** - For wings, jetpacks, banners, weapon racks
4. **Head Socket** - Swappable heads for races/aesthetics
5. **Relic Mounts** (3 small points) - Chest, shoulders, hips for equipment

**Design Principle**:
All attachment points use **standardized connectors** so any community-created part fits any core frame.

---

## Universal Connector Standards

### Primary Weapon Sockets (Arms)

**Option A: Ball Joint System**
- **Socket**: 5mm diameter spherical cavity in shoulder
- **Peg**: 5mm ball on weapon attachment
- **Benefit**: Posable, adjustable angles
- **Drawback**: May need friction fit or glue

**Option B: Peg & Hole System**
- **Socket**: 3mm cylindrical hole in shoulder
- **Peg**: 3mm cylinder on weapon (with key/tab for rotation lock)
- **Benefit**: Sturdy, easy to print, friction holds
- **Drawback**: Fixed angles (but can include multiple peg positions)

**Recommended**: **Option B (Peg System)** for ease of printing and sturdiness.

### Relic Micro-Mounts

**Magnet System** (Preferred):
- **Socket**: 2mm x 1mm circular cavity
- **Peg**: 2mm x 1mm neodymium magnet embedded
- **Benefit**: Swappable equipment, no glue needed
- **Use Cases**: Pouches, sensors, badges, small details

**Alternative Peg System**:
- **Socket**: 1.5mm cylindrical hole
- **Peg**: 1.5mm cylinder
- **Benefit**: No magnets required, fully printable

### Head Socket

**Standard**: 3mm peg with key tab (prevents rotation)
- Allows race-specific heads, helmets, variants

### Back Mount

**Standard**: Dual 2mm pegs (5mm apart)
- For banners, backpacks, wings, weapon racks

---

## Scale & Dimensions

**Model Scale**: 28mm heroic scale (compatible with common tabletop miniatures)

**Dimensions**:
- **Height**: 60-80mm (torso to top of head, not including back mounts)
- **Width**: 30-40mm (shoulder to shoulder)
- **Base**: 28mm hex (fits standard hex grid boards)
- **Weight** (printed): ~15-25g depending on material and infill

**Hex Board Scale**:
- 1 hex = 28mm flat-to-flat
- Caskets fit comfortably on 1 hex with room for facing orientation

---

## File Structure & Organization

### Official Core Release

```
/core-casket-v1/
├── README.md                    # Assembly instructions
├── LICENSE.txt                  # CC BY-NC-SA 4.0
├── /torso/
│   ├── human_torso.stl
│   ├── elven_torso.stl          # Optional race variants
│   ├── dwarven_torso.stl
│   └── orcish_torso.stl
├── /legs/
│   ├── legs_standing.stl
│   ├── legs_walking.stl
│   ├── legs_charging.stl
│   └── legs_bracing.stl
├── /heads/
│   ├── human_knight_helm.stl
│   ├── elven_ranger_helm.stl
│   ├── dwarven_beard_helm.stl
│   └── orcish_spiked_helm.stl
├── /bases/
│   ├── hex_base_scout.stl       # Marked with weight class
│   ├── hex_base_heavy.stl
│   └── hex_base_assault.stl
└── /test_pieces/
    ├── connector_test.stl       # Print this first to verify fit
    └── assembly_guide.pdf
```

### Community Weapon Submission Structure

```
/weapon-longsword-faithkeeper/
├── faithkeeper_arm_right.stl    # Right arm attachment
├── faithkeeper_cards.pdf        # 4 card designs
├── balance_notes.txt            # Playtesting data, SP costs
├── preview_image.png            # Render or photo of printed model
└── README.md                    # Designer notes, paint tips
```

---

## Community Creation Guidelines

### Submission Requirements

**STL Files**:
- Clean, manifold geometry (no holes or inverted normals)
- Proper scale (test against connector_test.stl)
- Printable on both FDM and Resin (design for 0.4mm nozzle minimum)
- Pre-supported version recommended (but not required)

**Card Data**:
- PDF or image of card designs (use official template)
- Stats: SP cost, initiative, range, heat, keywords
- Balanced according to guidelines (see below)

**Documentation**:
- Designer name/credit
- Playtesting notes (if available)
- Recommended paint schemes (optional)
- Print settings used for test print

**Preview Image**:
- Photo of painted/printed model OR 3D render
- Shows attachment to core frame
- Ideally shown in context (on hex base, with cards)

### Balance Guidelines

**Weapon Design Targets**:

| Weight Class | Card Count | SP Range | Initiative Range | Special Notes |
|--------------|-----------|----------|------------------|---------------|
| Scout | 3-4 cards | 1-2 SP | 1-4 | Fast, low damage |
| Support | 3-4 cards | 1-3 SP | 2-5 | Utility focus |
| Heavy | 4-5 cards | 2-3 SP | 4-7 | High damage/defense |
| Assault | 4-5 cards | 2-4 SP | 5-9 | Devastating, slow |
| Universal | Any class | Any | Any | Available to all |

**Damage Guidelines**:
- Light weapons: 2-3 damage
- Medium weapons: 3-5 damage
- Heavy weapons: 5-7 damage
- Siege weapons: 7-9 damage (with drawbacks)

**Heat Guidelines**:
- Most weapons: 0 Heat
- High-output weapons: +1 Heat
- Sustained fire/AOE: +2 Heat
- Overcharged/corruption: +3 Heat

**Relic Tech** (Ammo/Charges):
- 3-5 uses per mission
- Higher damage than equivalent non-tech
- Limited availability (justifies power)

---

## Licensing & Distribution

### Official Core License

**License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)

**You MAY**:
- Download and print for personal use
- Remix and modify the core
- Share modifications (under same license)
- Use in non-commercial playtesting/events

**You MAY NOT**:
- Sell prints of the official core (without permission)
- Remove attribution
- Use for commercial purposes without license

### Community Submission License

**Recommended**: CC BY-NC-SA 4.0 (same as core)

**Designer retains**:
- Credit for design
- Right to sell pre-supported or premium versions
- Copyright on original artistic elements

**Community receives**:
- Right to print for personal use
- Right to remix (with attribution)

---

## Community Repository System

### Repository Structure (Future Site/GitHub)

**Categories**:
- `/weapons/melee/`
- `/weapons/ranged/`
- `/weapons/magic/`
- `/shields/`
- `/relics/`
- `/cosmetics/` (heads, armor plates, decorations)
- `/terrain/` (hex terrain for boards)
- `/monsters/` (AI enemies)

**Submission Process**:
1. Designer creates weapon + cards
2. Uploads to community repository (GitHub, Thingiverse, or dedicated site)
3. Community playtests and votes
4. If balanced and popular: Approved for "tournament legal" tag
5. Designer credited, files hosted officially

**Curation**:
- **Homebrew**: Fun, experimental, unbalanced (use at own risk)
- **Community Tested**: Playtested, seems balanced
- **Tournament Legal**: Officially approved for competitive play

---

## Production & Release Strategy

### Phase 1: Free Core Release
- Core Casket STL files (all races)
- 10 universal card PDFs
- 5 basic weapons (longsword, shield, bow, hammer, spear)
- Design standards document
- Connector test print file

**License**: CC BY-NC-SA 4.0 (free for personal use)

### Phase 2: Premium Packs (Optional Paid Content)
- High-detail sculpted variants
- Pre-supported files (optimized for printing)
- Full race cosmetic kits (Human Penitent, Elven Verdant, etc.)
- Professional card art packs
- Official tournament equipment sets
- Physical card decks (print-on-demand or Kickstarter)

### Phase 3: Community Marketplace
- Approved designers can sell premium versions
- Revenue share model (70% designer, 30% platform)
- Official stamp of approval for quality/balance

---

## Kickstarter Potential

**Campaign Concept**: "Penance: Core Set"

**Pledge Tiers**:

**$0 - Digital Core** (Free Forever):
- Core Casket STL files
- 10 universal cards PDF
- 5 basic weapons STL
- Rulebook PDF

**$15 - Starter Pack**:
- Digital Core (above)
- Pre-supported STL files
- Full race pack (Human Penitent cosmetics)
- Basic card deck (printed, shipped)
- Player mat PDF

**$35 - Deluxe Pack**:
- Everything in Starter
- All 7 race cosmetic packs
- 20 weapon STL files
- Monster AI pack (3 enemies)
- Hex terrain STL files
- Printed card decks (universal + 3 weapon sets)

**$75 - Complete Set**:
- Everything in Deluxe
- Physical printed & painted core Casket model
- All card decks (printed, premium quality)
- Hex board (neoprene mat)
- Token set (heat, taint, ammo)

**Stretch Goals**:
- Unlock new races (Fae, Draconid, Undead)
- Monster bestiary expansions
- Terrain packs (ruins, forests, lava fields)
- Community design contest (winning designs added officially)

---

## Technical Print Testing

### Recommended Print Settings

**FDM (Filament) Printing**:
- **Layer Height**: 0.2mm (0.15mm for high detail)
- **Nozzle**: 0.4mm standard
- **Infill**: 15-20% (gyroid or cubic)
- **Material**: PLA, PLA+, or PETG
- **Supports**: Minimal (design for printability)

**Resin Printing**:
- **Layer Height**: 0.05mm
- **Exposure**: Standard resin settings
- **Supports**: Light supports, pre-supported version available
- **Material**: Standard resin (ABS-like or tough resin for durability)

**Post-Processing**:
- Sand connection points for smooth fit
- Prime before painting (spray primer recommended)
- Acrylic paints work well (Citadel, Vallejo, Army Painter)

### Connector Fit Testing

**Important**: Print `connector_test.stl` FIRST to verify fit on your printer.

- Tests all socket types (arm, relic, head, back)
- Verifies tolerances (0.2mm clearance standard)
- Adjust scale if needed (+/- 1-2% to tighten/loosen fit)

---

## Community Design Contests (Future)

**Monthly Theme Contests**:
- "Best Scout Weapon" - Lightweight, fast designs
- "Most Creative Relic" - Unique mechanics
- "Coolest Monster" - AI enemy designs
- "Best Terrain Piece" - Hex-based environmental hazards

**Prizes**:
- Feature on official site
- Tournament legal approval
- Physical printed version (if Kickstarter funded)
- Revenue share on sales (if marketplace exists)

---

## Next Steps for Development

### Immediate (Pre-Release)
- [ ] Finalize connector dimensions (print tests)
- [ ] Model core Casket frame (human variant first)
- [ ] Design 5 basic weapons (longsword, shield, bow, hammer, spear)
- [ ] Create connector test print file
- [ ] Write assembly instructions

### Short-Term (Alpha Release)
- [ ] Release core STL files (free download)
- [ ] Create submission template for community
- [ ] Set up repository (GitHub or dedicated site)
- [ ] Playtest with printed models
- [ ] Iterate based on feedback

### Long-Term (Community Growth)
- [ ] Approve first community submissions
- [ ] Launch Kickstarter (if desired)
- [ ] Develop marketplace system
- [ ] Expand to all 7 races
- [ ] Create monster/terrain packs

---

## Example: Community Submission

**Weapon: "Anvilfall" (Dwarven Warhammer)**

**Designer**: RuneSmith42

**Files**:
- `anvilfall_right_arm.stl` (7.2 MB)
- `anvilfall_cards.pdf` (4 cards)
- `balance_notes.txt`
- `preview_painted.jpg`

**Stats**:
- **Type**: Weapon (Right Arm)
- **Weight Class**: Heavy/Assault only (too heavy for Scout/Support)
- **Deck Addition**: 4 cards
  - "Crushing Descent" (Init 6, 5 dmg, 2 SP)
  - "Earthshaker Smash" (Init 7, 4 dmg AOE, 3 SP, +1 Heat)
  - "Anvil's Echo" (Init 5, 3 dmg, stun on 6+, 2 SP)
  - "Hammerfall" (Init 8, 6 dmg, cannot move next turn, 3 SP)

**Playtesting Notes**:
- Tested in 5 games (3 wins, 2 losses)
- High damage balanced by slow initiative
- AOE makes it valuable vs swarms
- "Hammerfall" self-root feels thematic and balanced

**Community Rating**: 4.7/5 (89 downloads, 23 votes)

**Status**: ✅ **Tournament Legal** (approved by official team)

---

*This system is designed to grow with the community. As more designers contribute, Penance becomes a living, evolving game.*
