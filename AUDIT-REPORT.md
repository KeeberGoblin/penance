# Repository Audit Report - 2025-10-12

## Overview
Comprehensive audit of Penance repository to identify and fix outdated references, broken links, and legacy content.

## Status: IN PROGRESS

---

## Completed Updates

### ✅ Wiki Index (docs/wiki/index.html)
**Status**: COMPLETE
**Changes Made**:
- Updated from "2 factions (30/32 cards)" → "4 factions (26-50 cards variable)"
- Removed references to deck-complete.md
- Added Equipment System section (60+ items)
- Added Dice Reference link
- Updated sidebar navigation (separated playable vs design-only factions)
- Changed "Elven Remnants" → "Elven Verdant Covenant"
- Changed "Dwarven Clans" → "Dwarven Forge-Guilds"
- Updated Recent Updates section with v2.0 changelog
- Added Faction Overview table with all 9 factions
- Added PDF download link for PLAYTEST-READY.pdf
- Updated dates (2024 → 2025)

---

## Files Requiring Updates

### 🔴 HIGH PRIORITY - Wiki Faction Pages

#### docs/wiki/faction-church.html
**Issues Found**:
- References deck-complete.md (line 327)
- Shows "30 cards" (needs to show "variable 26-50 cards")
- Lacks equipment system information
- Missing v2.0 deck composition

#### docs/wiki/faction-dwarves.html
**Issues Found**:
- References deck-complete.md (multiple locations)
- Shows "32 cards" (needs to show "variable 28-52 cards")
- Name "Dwarven Clans" → should be "Dwarven Forge-Guilds"
- Lacks equipment system information

#### docs/wiki/faction-undead.html (The Ossuarium)
**Issues Found**:
- Likely outdated or empty (need to check)
- Needs v2.0 deck system information
- Needs Soul Harvest, Decay cards information

#### docs/wiki/faction-elves.html
**Issues Found**:
- Name "Elven Remnants" → should be "Elven Verdant Covenant"
- Likely outdated or empty (need to check)
- Needs v2.0 deck system, Bleed stacking information

---

### 🟡 MEDIUM PRIORITY - Scenario Files

#### docs/scenarios/example-of-play.md
**Issues**: References old deck system (30/32 cards fixed)
**Fix Needed**: Update to reflect equipment system (note this is just an example, can stay simplified)

#### docs/scenarios/boss-iron-saint.md
**Issues**: May reference old deck system
**Fix Needed**: Verify and update if needed

---

### 🟡 MEDIUM PRIORITY - Reference Files

#### docs/reference/playtest-assessment.md
**Issues**: May reference "2 factions" or old deck counts
**Fix Needed**: Update to reflect 4 factions, v2.0 system

#### docs/reference/design-roadmap.md
**Issues**: Likely shows old roadmap
**Fix Needed**: Update to reflect current state (v2.0 complete)

#### docs/reference/tabletop-simulator-guide.md
**Issues**: May reference old deck system
**Fix Needed**: Update if needed

#### docs/reference/core-design.md
**Issues**: May reference 30-card fixed decks
**Fix Needed**: Update design philosophy section if needed

---

### 🟢 LOW PRIORITY - Card Files

#### docs/cards/universal.md
**Issues**: May say "30 cards = 30 HP"
**Fix Needed**: Update to "deck size varies (26-50 cards)"

#### docs/cards/masterlist.md
**Issues**: May reference old faction organization
**Fix Needed**: Update to reflect equipment system

#### docs/cards/new-cards-dice-system.md
**Issues**: Unknown - needs review
**Fix Needed**: Verify and update if needed

---

## Recommended Actions

### Immediate (Today)
1. ✅ Update wiki index - DONE
2. 🔴 Update 4 wiki faction pages (church, dwarves, ossuarium, elves)
3. 🔴 Verify and fix any broken links in main documentation

### Next Session
4. 🟡 Update scenario files (example-of-play, boss encounters)
5. 🟡 Update reference files (playtest-assessment, design-roadmap)
6. 🟢 Update card database files (universal, masterlist)

### Long-term
7. Create visual diagrams for complex rules (hex movement, facing, etc.)
8. Generate printable hex maps for scenarios
9. Create quick-start video tutorial

---

## Search Patterns Used

```bash
# Find deck-complete references
grep -r "deck-complete" docs/ --include="*.md" --include="*.html"

# Find fixed card count references
grep -r "30 cards\|32 cards" docs/ --include="*.md" --include="*.html"

# Find old faction names
grep -r "Elven Remnants\|Dwarven Clans\|Bone-Courts\|Twilight Courts" docs/
```

---

## Files Modified So Far

1. ✅ docs/wiki/index.html - Updated to v2.0
2. ✅ docs/reference/PLAYTEST-READY.md - Completely rewritten for v2.0
3. ✅ docs/reference/PLAYTEST-READY.pdf - Regenerated
4. ✅ docs/README.md - Fixed broken links
5. ✅ docs/factions/index.md - Updated to 4 factions
6. ✅ docs/cards/index.md - Fixed deck composition
7. ✅ README.md (root) - Fixed all broken links

---

## Next Steps

Continue updating wiki faction pages (faction-church.html, faction-dwarves.html, faction-undead.html, faction-elves.html).

---

## Estimated Time Remaining

- Wiki faction pages: 30 minutes
- Scenario files: 15 minutes
- Reference files: 20 minutes
- Card database files: 10 minutes

**Total**: ~75 minutes of work remaining

---

## Notes

- All PDFs are now in git and accessible (fixed earlier)
- Equipment system is well-documented (equipment-pool-complete.md)
- Main website (index.html) may also need updates (check separately)
- Archive folder is well-organized

---

**Last Updated**: 2025-10-12
**Auditor**: Claude Code
**Status**: 40% complete (7 of ~15-20 files updated)
