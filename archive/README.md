# Archive

This folder contains historical development documents and status reports that are no longer actively referenced but provide valuable context for the project's evolution.

## Contents

### System Update Reports
- `SYSTEM-OVERHAUL-SUMMARY.md` - October 11, 2025 equipment system overhaul (v2.0)
- `DICE-SYSTEM-IMPLEMENTATION-COMPLETE.md` - Custom dice system implementation
- `INDEX-HTML-DICE-SYSTEM-UPDATE.md` - Main page dice system integration

### Correction & Analysis Documents
- `CONTRADICTION-REPORT.md` - Lore and mechanics consistency review
- `PILOT-STATE-CORRECTIONS.md` - Pilot wound deck system corrections
- `SITE-REDESIGN-ANALYSIS.md` - Website redesign planning document

### Infrastructure
- `GITHUB-PAGES-SETUP.md` - GitHub Pages deployment guide

### Historical Versions
- `PLAYTEST-READY-v1.md` - Original playtest package (October 9, 2025)
- `church-deck-complete-legacy.md` - Church fixed-deck system (pre-v2.0)
- `dwarves-deck-complete-legacy.md` - Dwarven fixed-deck system (pre-v2.0)

### Old Tools & Assets
- `church-sample-sheet.svg` - Sample TTS sheet (Church faction)
- `dwarven-sample-sheet.svg` - Sample TTS sheet (Dwarven faction)
- `utilities-archive/` - Old utility scripts and audits (moved from utilities/)

## Why Archive?

These documents were moved from the project root and tools directory to reduce clutter and improve navigation. They remain in version control for historical reference but are no longer actively maintained.

### Current Locations
- Playtest package: `docs/reference/PLAYTEST-READY.md`
- Faction decks: `docs/factions/{faction}/deck-equipment-system.md`
- Card system: `docs/cards/` (index.html, deck-builder.html, print-deck.html)
- Codex (wiki): `docs/codex/index.html`
- PDF generation: `tools/generate-pdfs.py` (if exists)

## Cleanup History

### October 17, 2025 - Archive Cleanup
Removed obsolete files that were fully replaced by current systems:
- ❌ `card-generator-old/` (252KB) - Replaced by `docs/cards/`
- ❌ `wiki-index-old.html` (23KB) - Replaced by `docs/codex/index.html`
- ❌ `timeline-replacement.txt` (12KB) - One-time content, already integrated
- ❌ `update_timeline.py` (4KB) - One-time script, no longer needed
- ❌ `generate-dwarven-deck.py` (4KB) - Obsolete deck generator

**Result**: Archive reduced from 540KB to 244KB (54% reduction)

---

**Last Updated**: October 17, 2025
