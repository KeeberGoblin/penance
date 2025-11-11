# Documentation Organization Guide

This document explains the structure of the `/docs` folder to help contributors navigate and maintain the Penance documentation.

---

## Folder Structure

```
docs/
├── README.md                    # Main documentation entry point
├── DOCS_ORGANIZATION.md         # This file
├── BALANCE-FINAL-V5.29.md       # Latest balance snapshot
│
├── codex/                       # ⚠️ WEBSITE FILES - HTML pages (don't edit structure)
│   ├── index.html              # Main codex website
│   ├── manuscript-style.css    # Codex styling
│   ├── lore-*.html            # Lore HTML pages
│   ├── faction-*.html         # Faction HTML pages
│   └── ...                    # Other codex pages
│
├── lore/                       # 📖 World-building & narrative
│   ├── index.md               # Lore navigation
│   ├── species-demographics.md # NEW! Subspecies & population data
│   ├── casket-technology-revised.md
│   ├── neural-thread-system.md
│   ├── soulstone-system.md
│   ├── theslar-event-ground-zero.md
│   └── ...
│
├── factions/                   # ⚔️ Faction-specific content
│   ├── index.md
│   ├── church/
│   ├── dwarves/
│   ├── elves/
│   ├── ossuarium/
│   ├── nomads/
│   ├── crucible/
│   ├── exchange/
│   ├── wyrd-conclave/
│   ├── vestige-bloodlines/
│   ├── emergent/
│   ├── iron-doctrine/          # NEW! Train-bound immortals
│   └── draconid/
│
├── rules/                      # 🎲 Game mechanics & rules
│   ├── index.md
│   ├── combat-system.md
│   ├── deck-construction.md
│   ├── support-units.md
│   └── ...
│
├── campaigns/                  # 🗺️ Campaign content & settlement rules
│   ├── index.md
│   ├── event-tables-kdm-style.md
│   ├── settlement-phase-procedure.md
│   ├── pilot-progression.md
│   └── ...
│
├── scenarios/                  # 📍 Individual mission scenarios
│   ├── index.md
│   ├── 01-proving-grounds.md
│   ├── 02-reliquary-ruins.md
│   └── ...
│
├── cards/                      # 🃏 Card system documentation
│   ├── index.md
│   ├── masterlist.md
│   ├── anatomy.md
│   └── ...
│
├── enemies/                    # 👹 Bestiary & enemy stats
│   └── bestiary-core.md
│
├── reference/                  # 🛠️ Design docs, balance sheets, dev notes
│   ├── index.md
│   ├── core-design.md
│   ├── faction-image-prompts.md
│   ├── playtest-assessment.md
│   └── ...
│
├── balance/                    # 📊 Balance analysis & reports
│   ├── ossuarium-balance-analysis.md
│   └── ossuarium-paradox.md
│
├── mechanics/                  # ⚙️ Specific game systems
│   └── soul-shard-system.md
│
├── images/                     # 🖼️ Image assets
│   ├── README.md
│   ├── IronDoctrine.png       # NEW! Faction images
│   ├── Church_PlaceH.png
│   └── ...
│
├── archive-v5-history/         # 📦 Historical balance records
│   └── (v5.x balance iterations)
│
└── archive-backups-2025-10-21/ # 📦 Old file backups
    └── (archived content)
```

---

## Content Guidelines

### Where to Put New Content

| Content Type | Location | Example |
|--------------|----------|---------|
| **Lore/Worldbuilding** | `docs/lore/` | Species demographics, Theslar Event, cosmology |
| **Faction Mechanics** | `docs/factions/{faction-name}/` | Deck equipment, support units, lore |
| **Game Rules** | `docs/rules/` | Combat system, deck construction, turn structure |
| **Campaign Content** | `docs/campaigns/` | Settlement phase, event tables, pilot progression |
| **Missions** | `docs/scenarios/` | Individual playable scenarios |
| **Balance Data** | `docs/balance/` | Faction analysis, statistical reports |
| **Design Notes** | `docs/reference/` | Dev documentation, prompts, technical specs |
| **Website Pages** | `docs/codex/` | HTML pages for the codex website |

### File Naming Conventions

- **Markdown files**: `kebab-case-names.md` (e.g., `species-demographics.md`)
- **HTML files**: `kebab-case-names.html` (e.g., `lore-species-demographics.html`)
- **Faction folders**: lowercase (e.g., `church/`, `iron-doctrine/`)
- **Index files**: Always `index.md` for navigation

---

## Codex Website (docs/codex/)

⚠️ **IMPORTANT**: The `docs/codex/` folder contains the **website HTML files**. These are:
- Hand-coded HTML with manuscript styling
- Served as the official Penance Codex website
- Should NOT have their structure changed without coordinating with website deployment

**Relationship to Markdown Files**:
- Markdown files in `docs/lore/`, `docs/factions/`, etc. are **source content**
- HTML files in `docs/codex/` are **formatted web pages** (may be manually created or generated)
- Some content exists in BOTH formats (markdown for editing, HTML for display)

---

## Navigation Files (index.md)

Each major folder should have an `index.md` file that provides:
1. Overview of the folder's contents
2. Links to major files
3. Organization/categorization

**Example**: `docs/lore/index.md` should link to:
- Species Demographics
- Theslar Event
- Casket Technology
- Soulstone System
- etc.

---

## Working with Lore Content

### Adding New Lore

1. Create markdown file in `docs/lore/{topic}.md`
2. Add entry to `docs/lore/index.md`
3. (Optional) Create HTML version in `docs/codex/lore-{topic}.html` if web display needed
4. Cross-link to related content

### Example: Adding Species Demographics

✅ **Done**:
- Created `docs/lore/species-demographics.md` (source content)
- Created `docs/codex/lore-species-demographics.html` (web display with charts)
- TODO: Update `docs/lore/index.md` to link to new file

---

## Working with Faction Content

Each faction folder should contain:
```
docs/factions/{faction-name}/
├── faction-overview.md          # Main faction description
├── deck-equipment-system.md     # Cards & equipment
├── support-units.md             # Support unit mechanics
├── lore-*.md                    # Additional lore documents
└── ...
```

**Example**: Iron Doctrine
```
docs/factions/iron-doctrine/
└── faction-overview.md          # NEW! Train-bound immortals
```

---

## Archive Folders

### `archive-v5-history/`
Contains historical balance iteration documents from v5.x development. **Do not delete** - these are development history records.

### `archive-backups-2025-10-21/`
Contains old file backups. May be cleaned up after confirming nothing critical was lost.

---

## Image Assets

All images go in `docs/images/`:
- Faction images: `{FactionName}_PlaceH.png` or `{FactionName}.png`
- Concept art: `Concept_{Description}.jpg`
- Soulstone visuals: `images/soulstones/`

---

## Cross-Referencing

When linking between documents:
- **Within same folder**: `[Link Text](./other-file.md)`
- **To other folder**: `[Link Text](../other-folder/file.md)`
- **To codex HTML**: `[Link Text](../../codex/lore-topic.html)`

**Example**:
```markdown
See [Species Demographics](./species-demographics.md) for evolutionary biology.
See [Codex Version](../../codex/lore-species-demographics.html) for web display.
```

---

## Maintenance Tasks

### Regular Updates
- [ ] Update `index.md` files when adding new content
- [ ] Keep codex HTML in sync with markdown source (when applicable)
- [ ] Archive old balance data to `archive-v5-history/`
- [ ] Update this DOCS_ORGANIZATION.md when structure changes

### Cleanup Tasks (As Needed)
- [ ] Review `archive-backups-2025-10-21/` for deletion
- [ ] Consolidate duplicate content
- [ ] Verify all internal links work

---

## Quick Reference

| Need to find... | Look in... |
|-----------------|------------|
| How Caskets work | `docs/lore/casket-technology-revised.md` |
| Faction equipment | `docs/factions/{name}/deck-equipment-system.md` |
| Combat rules | `docs/rules/combat-system.md` |
| Population data | `docs/lore/species-demographics.md` |
| Mission scenarios | `docs/scenarios/` |
| Balance analysis | `docs/balance/` or `docs/reference/` |
| Website content | `docs/codex/` |

---

## Contributing

When adding new documentation:
1. Choose appropriate folder (see "Where to Put New Content" table above)
2. Follow naming conventions
3. Update relevant `index.md` files
4. Add cross-references to related documents
5. If creating web content, add both `.md` (source) and `.html` (display) versions where appropriate

---

**Last Updated**: 2025-01-XX (Update this when modifying structure)
