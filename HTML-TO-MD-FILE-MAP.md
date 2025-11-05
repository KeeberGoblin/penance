# HTML to Markdown File Mapping

**Purpose**: Map each HTML file in `docs/codex/` to corresponding MD file(s) in `docs/` tree
**Total HTML Files**: 85
**Last Updated**: 2025-11-05

**Legend**:
- ✅ = MD equivalent exists and is current
- ⚠️ = MD equivalent exists but has differences/issues
- ❌ = No MD equivalent found
- 🔀 = Content split across multiple MD files
- 📝 = Needs creation/update

---

## Balance & Versioning

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `balance-v529-final.html` | ⚠️ | `BALANCE-FINAL-V5.29.md` | Root level file exists |

---

## Campaign Files

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `campaign-anomalous-events.html` | ⚠️ | `campaigns/anomalous-events-scp-style.md` | Check alignment |
| `campaign-event-tables.html` | ⚠️ | `campaigns/event-tables-kdm-style.md` | Check alignment |
| `campaign-flesh-bargains.html` | ⚠️ | `campaigns/flesh-bargains.md` | Different structure/focus |
| `campaign-loot-tables.html` | ⚠️ | `campaigns/loot-tables.md` | Check alignment |
| `campaign-mission-generation.html` | ❌ | NOT FOUND | 📝 Needs creation |
| `campaign-pilot-generation.html` | ⚠️ | `campaigns/pilot-generation-tables.md` | Check alignment |
| `campaign-pilot-grit.html` | ⚠️ | `campaigns/pilot-grit-system.md` | Check alignment |
| `campaign-pilot-progression.html` | ⚠️ | `campaigns/pilot-progression.md` | Check alignment |
| `campaign-pilot-skills.html` | ✅ | `campaign/pilot-skills.md` | Well-aligned! |
| `campaign-scavengers-crusade.html` | ⚠️ | `campaigns/campaign-scavengers-crusade.md` | Check alignment |
| `campaign-settlement-phase.html` | ⚠️ | `campaigns/settlement-phase-procedure.md` | Check alignment |
| `campaign-settlements.html` | ⚠️ | `campaigns/settlements.md` | Check alignment |

---

## Card System

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `card-anatomy.html` | ⚠️ | `cards/anatomy.md` | Check alignment |
| `equipment-decks.html` | 🔀 | Multiple in `factions/*/deck-equipment-system.md` | Faction-specific |
| `support-equipment.html` | 🔀 | Multiple in `factions/*/support-units.md` | Faction-specific |
| `support-units.html` | 🔀 | Multiple in `factions/*/support-units.md` | Faction-specific |

---

## Content/Navigation

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `content-home.html` | ❌ | NOT NEEDED | Navigation page only |
| `index.html` | ❌ | NOT NEEDED | Index page only |

---

## Cosmology & Lore Core

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `cosmology.html` | ⚠️ | `lore/cosmology-and-origins.md` | MD has more tech detail |

---

## Enemies

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `enemies-anomalous.html` | ❌ | NOT FOUND | 📝 Needs creation |
| `enemies-bestiary.html` | ⚠️ | `enemies/bestiary-core.md` | Check alignment |

---

## Factions

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `faction-ashborne.html` | 🔀 | `factions/crucible/` | Ashborne = Crucible faction |
| `faction-bloodlines.html` | 🔀 | `factions/vestige-bloodlines/` multiple files | Split across bloodline files |
| `faction-church.html` | 🔀 | `factions/church/deck-equipment-system.md` + `support-units.md` | Split content |
| `faction-crucible.html` | 🔀 | `factions/crucible/deck-equipment-system.md` + others | Split content |
| `faction-draconid.html` | ⚠️ | `factions/draconid/faction-overview.md` | Check alignment |
| `faction-dwarves.html` | 🔀 | `factions/dwarves/deck-equipment-system.md` + `support-units.md` | Split content |
| `faction-elves.html` | ⚠️ | `factions/elves/deck-equipment-system.md` | **OUTDATED BALANCE** |
| `faction-emergent.html` | 🔀 | `factions/emergent/` multiple files | Split content |
| `faction-exchange.html` | 🔀 | `factions/exchange/` multiple files | Split content |
| `faction-fae.html` | ❌ | NOT FOUND | 📝 Check for Wyrd Conclave files |
| `faction-nomads.html` | 🔀 | `factions/nomads/deck-equipment-system.md` + `support-units.md` | Split content |
| `faction-undead.html` | 🔀 | `factions/ossuarium/` multiple files | Undead = Ossuarium |

---

## GM Tools

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `gm-helper.html` | ❌ | NOT FOUND | 📝 Needs creation |
| `gm-reference-combat.html` | ⚠️ | `rules/combat-system.md`? | Check alignment |
| `player-aid-reference-card.html` | ❌ | NOT FOUND | 📝 Likely player handout only |

---

## Lore: Casket Technology

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-casket-manufacturing.html` | ⚠️ | `lore/casket-technology-revised.md`? | Check alignment |
| `lore-casket-origins.html` | ⚠️ | `lore/casket-technology-revised.md`? | Check alignment |
| `lore-caskets-overview.html` | ⚠️ | `lore/casket-technology-revised.md` | Check alignment |
| `lore-neural-threads.html` | ✅ | `lore/neural-thread-system.md` | Likely aligned |

---

## Lore: Characters & NPCs

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-bonelord-karath.html` | ⚠️ | `lore/iconic-npcs.md`? | **NAME CONFLICT: Karath vs Thresh** |
| `lore-npcs.html` | ⚠️ | `lore/iconic-npcs.md` | Check alignment |

---

## Lore: Chronicle & History

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-chronicle.html` | ⚠️ | `lore/chronicle.md` or `chronicle-enhanced.md` | Check which is current |
| `lore-year-zero.html` | ✅ | `lore/year-zero-timeline.md` | Likely aligned |
| `lore-pre-sundering.html` | 🔀 | Integrated in `lore/cosmology-and-origins.md` | Part of larger file |
| `lore-sundering.html` | 🔀 | Integrated in `lore/cosmology-and-origins.md` | Part of larger file |

---

## Lore: Engine & Technology

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-engine.html` | ⚠️ | `lore/theslar-engine-mechanics.md` | Check alignment |
| `lore-ground-zero.html` | ⚠️ | `lore/theslar-event-ground-zero.md` | Check alignment |

---

## Lore: Factions Overview

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-factions-overview.html` | ⚠️ | `factions/index.md` or `factions/readme.md` | Check alignment |

---

## Lore: Geography & Environment

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-climate.html` | ❌ | NOT FOUND | 📝 May be in world-overview.md |
| `lore-settlements.html` | ⚠️ | `campaigns/settlements.md`? | Check alignment |
| `lore-theslar-overview.html` | ⚠️ | Multiple files in `lore/` | Check alignment |

---

## Lore: Soul & Soulstone System

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-soul-binding.html` | ⚠️ | Integrated in `lore/soulstone-system.md`? | Check coverage |
| `lore-soul-economics.html` | ⚠️ | Integrated in `lore/soulstone-system.md`? | Check coverage |
| `lore-soulstone-system.html` | ⚠️ | `lore/soulstone-system.md` | Different focus/structure |
| `lore-soulstone-volatility.html` | ✅ | `lore/soulstone-volatility.md` | Likely aligned |

---

## Lore: The Void

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `lore-void.html` | ❌ | **NO STANDALONE FILE** | 📝 **CRITICAL: Needs creation** |

**Issue**: 530+ lines of void lore in HTML, only ~18 lines in cosmology.md
**Action**: Extract to new `/docs/lore/void.md`

---

## Rules: Combat & Gameplay

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `rules-combat.html` | ⚠️ | `rules/combat-system.md` | Check alignment |
| `rules-combat-flowchart.html` | ❌ | NOT FOUND | 📝 Likely visual aid only |
| `rules-turn-structure.html` | ⚠️ | `rules/turn-structure.md` | Check alignment |

---

## Rules: Casket Systems

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `rules-casket-classes.html` | ⚠️ | `rules/casket-classes.md` | Check alignment |
| `rules-component-damage.html` | ⚠️ | `rules/component-damage-system.md` | Check alignment |

---

## Rules: Deck & Cards

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `rules-deck-construction.html` | ⚠️ | `rules/deck-construction.md` | Check alignment |
| `rules-scrap-cards.html` | ❌ | NOT FOUND | 📝 May be in combat-system.md |

---

## Rules: Dice & Mechanics

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `rules-dice.html` | ⚠️ | `rules/dice-reference.md` | Check alignment |
| `rules-dice-pool.html` | ✅ | `rules/dice-pool-advantage.md` | Likely aligned |

---

## Rules: Optional Systems (V3.0)

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `rules-taint-exploitation.html` | ✅ | `rules/taint-exploitation.md` | Likely aligned |
| `rules-thread-snap.html` | ❌ | NOT FOUND | 📝 May be in neural-thread-system.md |
| `rules-v3-optional.html` | ❌ | NOT FOUND | 📝 Needs creation or split |

---

## Rules: Specialized Mechanics

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `rules-common-mistakes.html` | ❌ | NOT FOUND | 📝 Needs creation |
| `rules-range-los.html` | ⚠️ | `rules/range-and-los.md` | Check alignment |
| `rules-soulstone-energy.html` | 🔀 | Integrated in `lore/soulstone-system.md` | Rules vs Lore split |
| `rules-support-as-main.html` | ⚠️ | `rules/support-as-main.md` | Check alignment |
| `rules-terrain.html` | ⚠️ | `rules/terrain.md` | Check alignment |

---

## Rules: Quick Reference

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `rules-quick-ref.html` | ⚠️ | `rules/quick-reference.md` | Check alignment |

---

## Scenarios

| HTML File | Status | MD File(s) | Notes |
|-----------|--------|------------|-------|
| `scenario-boss-iron-saint.html` | ❌ | NOT FOUND | 📝 Check scenarios/ dir |
| `scenario-escort-duty.html` | ❌ | NOT FOUND | 📝 Check scenarios/ dir |
| `scenario-example-of-play.html` | ⚠️ | `rules/example-of-play.md` | Check alignment |
| `scenario-king-of-the-hill.html` | ❌ | NOT FOUND | 📝 Check scenarios/ dir |
| `scenario-proving-grounds.html` | ❌ | NOT FOUND | 📝 Check scenarios/ dir |
| `scenario-reliquary-ruins.html` | ❌ | NOT FOUND | 📝 Check scenarios/ dir |
| `scenario-sabotage-mission.html` | ❌ | NOT FOUND | 📝 Check scenarios/ dir |
| `scenario-tutorial-energy-threads.html` | ❌ | NOT FOUND | 📝 Check scenarios/ dir |
| `scenarios.html` | ❌ | NOT FOUND | 📝 Scenario index |

---

## Summary Statistics

### Status Breakdown
- ✅ **Well-Aligned**: ~10 files (12%)
- ⚠️ **Needs Review**: ~40 files (47%)
- ❌ **Missing**: ~25 files (29%)
- 🔀 **Content Split**: ~10 files (12%)

### Priority Files Needing Creation
1. `lore/void.md` - **CRITICAL**
2. `scenarios/` directory files - Multiple missing
3. `rules/common-mistakes.md`
4. `rules/v3-optional.md` or split into components
5. `enemies/anomalous.md`
6. `gm-tools/` directory with helper content

### Files Needing Update
1. `factions/elves/deck-equipment-system.md` - Balance v5.29
2. All files with "Bonelord Thresh" → "Bonelord Karath" (or vice versa)
3. Any files referencing outdated mechanics

---

## Maintenance Protocol

When updating content:

1. **Check this map** to find all affected files
2. **Update both HTML and MD** versions
3. **Note version/date** in both files
4. **Update this map** if file locations change
5. **Add to changelog** if balance changes

---

## Notes

- **Faction content** is heavily split: HTML has unified faction pages, MD splits into deck-equipment, support-units, lore, etc.
- **Lore content** varies: HTML has detailed narrative, MD has mechanics
- **Campaign vs Campaigns**: Note directory name difference (`campaign/` vs `campaigns/`)
- **Scenarios**: Appears to be a gap - many scenario HTML files, possibly no MD equivalents

---

*This map will be updated as files are created, renamed, or reorganized.*

Last updated: 2025-11-05
