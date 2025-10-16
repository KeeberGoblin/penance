# Implementation TODO — Repository Cleanup and Index
Last updated: 2025-10-16

This file tracks the documentation integration work and related follow-ups.

## Status Summary

- Vestige Bloodlines — ✅ Implemented (docs/factions/vestige-bloodlines/)
- Emergent Syndicate — ✅ Implemented (docs/factions/emergent/)
- The Soulstone Exchange — ✅ Implemented (docs/factions/exchange/)
- Crucible Packs — ✅ Implemented (docs/factions/crucible-packs/)
- Faction index — ✅ Added (docs/factions/README.md)
- Archive source designs from utilities/ — ⏳ Pending move (see Archive section below)

## Done (Content Added)

- Vestige Bloodlines
  - 7 files: main deck/equipment, 5 bloodline pages, origin story
- Emergent Syndicate
  - 4 files: main deck/equipment, metamorph mechanics, hive-mind coordination, Sibarian lore
- The Exchange
  - 5 files: main deck/equipment, credit economy, mercenary hiring, orthodox vs rational, concordat lore
- Crucible Packs
  - 5 files: main deck/equipment, forge tokens, honor duel system, ancestral iron, forge worship lore
- Factions index (this is the central navigator)
  - docs/factions/README.md

## Next Actions

1) Archive the design sources from utilities/
- See “Archive Moves” below for exact commands.
- Commit message suggestion: chore(archive): move design source docs into utilities/archive/designs

2) Optional follow-ups
- Cards DB
  - [ ] Add new faction cards to docs/cards/complete-card-data.json (if maintained)
- Codex HTML (optional site)
  - [ ] Generate lightweight HTML codex pages for the new factions (docs/codex/)
- Cross-links
  - [ ] Add “Relationships” sections in existing factions referencing the newly added factions (if not already present)
- Lint/Links
  - [ ] Run a link check over docs/ to catch broken references
- Status page (optional)
  - [ ] Create or update utilities/CURRENT-STATUS.md as a living summary

## Archive Moves

Use git mv to keep history.

Required directories:
- utilities/archive/designs/

Commands:
- git mv utilities/Bloodlines_Suggestion.md utilities/archive/designs/vestige-bloodlines-2025-10-16.md
- git mv utilities/deck-complete-design_Collective.md utilities/archive/designs/emergent-syndicate-2025-10-15.md
- git mv utilities/deck-complete-design_Merchant.md utilities/archive/designs/exchange-merchant-2025-10-16.md
- git mv utilities/Exchange_Suggestion.md utilities/archive/designs/exchange-suggestion-2025-10-16.md
- git mv utilities/CruciblePact_Suggestion.md utilities/archive/designs/crucible-packs-2025-10-16.md

Then:
- git add -A
- git commit -m "chore(archive): move design source docs into utilities/archive/designs"
- git push

## Verification Checklist

- [ ] All four factions present under docs/factions/
- [ ] docs/factions/README.md exists and links resolve
- [ ] utilities/archive/designs/ contains archived originals with date-stamped names
- [ ] No broken links within newly added docs (run a link checker if available)
- [ ] Optional: Cards DB updated
- [ ] Optional: Codex HTML updated

Notes:
- Dates in archive filenames match the design’s version date where known (Emergent v1.0 on 2025-10-15).
- If any source file paths differ in your repo, adjust the git mv commands accordingly.
