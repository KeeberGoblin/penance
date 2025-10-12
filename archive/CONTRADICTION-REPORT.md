# Repository Contradiction Report

**Date**: October 12, 2025
**Scan Scope**: All `/docs` folder markdown and HTML files
**Purpose**: Identify lore, mechanics, and naming inconsistencies

---

## CRITICAL CONTRADICTIONS

### 1. Deck System Confusion (HIGH PRIORITY)

**Issue**: Two conflicting deck systems coexist in the repository

**Evidence**:

**System A: OLD - Fixed 30-Card Decks**
- Location: `docs/factions/*/deck-complete.md`
- Church: "Total Deck Size: 30 cards" (line 12)
- Dwarves: "Deck Size: 30 cards total" (line 5)
- States: 12 Primary Weapon cards (locked to Casket)
- States: 6 Secondary Equipment (choose 1 of 4 options)

**System B: NEW - Variable Equipment System**
- Location: `docs/factions/*/deck-equipment-system.md`
- Church: "Total Deck Size: 26-30 cards" (line 171)
- Dwarves: "Total Equipment Cards: 18-30 cards" (line 107)
- States: Modular equipment (Weapon + Shield/Offhand + Accessories 1-4 slots)
- States: 60+ craftable/lootable equipment items

**CLAUDE.md Statement** (line 647):
> "Remember the equipment system is NEW - Don't refer to old fixed decks"

**Problem**:
- `deck-complete.md` files are deprecated but still present
- No clear indication which system is canonical
- New players/AI assistants will be confused

**Recommendation**:
- [ ] **Option A**: Delete all `deck-complete.md` files (clean slate)
- [ ] **Option B**: Move `deck-complete.md` to `docs/factions/archive/` folder with deprecation notice
- [ ] **Option C**: Add prominent deprecation warning at top of each `deck-complete.md`:
  ```markdown
  # ⚠️ DEPRECATED - This file uses the OLD fixed-deck system
  **Current System**: See `deck-equipment-system.md` for variable equipment system
  **Date Deprecated**: October 11, 2025
  ```

---

### 2. Faction Name Inconsistency (MEDIUM PRIORITY)

**Issue**: "Elven Remnants" vs "Elven Verdant Covenant" used interchangeably

**Evidence**:

**Correct Name** (per CLAUDE.md line 50):
- "Elven Verdant Covenant"

**Files Using WRONG Name "Elven Remnants"**:
1. `docs/reference/design-roadmap.md:392` - "Elven Remnants (regeneration/nature theme)"
2. `docs/reference/ai-art-prompts.md:103` - "## Elven Remnants Caskets"
3. `docs/reference/PLAYTEST-READY.md:198` - "Add Elven Remnants or The Ossuarium"
4. `docs/reference/casket-control-system.md:152` - "### Elven Remnants: The Root Interface"
5. `docs/factions/dwarves/deck-complete.md:521` - "### Playing Against Elven Remnants"
6. `docs/factions/index.md:38` - "**Elven Remnants**: Thorn barriers..."
7. `docs/campaigns/leg-skimming.md:143` - "### Elven Remnants: **Tragic Necessity**"

**Files Using CORRECT Name**:
- All `docs/factions/elves/deck-equipment-system.md` files
- `docs/reference/equipment-pool-complete.md`
- `docs/reference/illuminated-manuscript-prompts.md`
- `CLAUDE.md` (master document)

**Recommendation**:
- [ ] Global find-and-replace "Elven Remnants" → "Elven Verdant Covenant" in 7 files
- [ ] Note: "Remnants" IS correct when referring to ALL dead pilots (not just Elves)

---

## MINOR CONTRADICTIONS

### 3. Pilot Physical State (RESOLVED in latest commit)

**Issue**: Manuscript prompts incorrectly showed all pilots as skeletons

**Status**: ✅ **FIXED** in commit `2b021ab` (October 12, 2025)

**Correction Applied**:
- Church: Changed to "pale corpse with flesh intact"
- Dwarves: Confirmed as skeleton (correct)
- Ossuarium: Confirmed as preserved corpse (correct)
- Elves: Changed to "semi-mummified in amber sap"

---

### 4. HTML Wiki Uses "Elven Remnants" (LOW PRIORITY)

**Issue**: HTML wiki pages use "Elven Remnants" in navigation

**Evidence**:
- All `docs/wiki/*.html` files have navigation link:
  ```html
  <a href="faction-elves.html" class="nav-link">Elven Remnants</a>
  ```

**Impact**: Low (HTML wiki may be outdated/deprecated)

**Recommendation**:
- [ ] Update all HTML navigation to "Elven Verdant Covenant" if wiki is still active
- [ ] OR mark entire `/docs/wiki/` folder as deprecated if it's no longer maintained

---

## POTENTIAL CONTRADICTIONS (Requires User Clarification)

### 5. Casket Class SP Values

**Question**: Are SP values consistent across all documentation?

**Found in Multiple Files**:
- Scout (Light): 6 SP ✅ Consistent
- Assault (Medium): 5 SP ✅ Consistent
- Heavy: 4 SP ✅ Consistent
- Fortress: 3 SP ✅ Consistent

**Status**: ✅ **NO CONTRADICTION FOUND**

---

### 6. Universal Core Cards Count

**Question**: How many Universal Core cards exist?

**Found Values**:
- CLAUDE.md line 79: "10 Universal + 6 Faction Core"
- `docs/cards/universal.md`: States "10 Universal Core cards"
- `docs/factions/dwarves/deck-complete.md`: Lists 10 Universal cards (lines 26-88)

**Status**: ✅ **NO CONTRADICTION FOUND** (10 is correct)

---

### 7. Timeline Dates

**Spot Check**: Verifying major historical events

| Event | File | Date | Consistent? |
|-------|------|------|-------------|
| The Sundering | world-overview.md | Year 0 | ✅ Yes |
| First Casket | world-overview.md | Year 50-150 | ✅ Yes |
| Great Schism | world-overview.md | Year 134 | ✅ Yes |
| Present Day | world-overview.md | Year 437 | ✅ Yes |

**Status**: ✅ **NO CONTRADICTION FOUND**

---

### 8. Faction Count

**Question**: How many factions exist total?

**CLAUDE.md states** (line 136):
- 4 Playable: Church, Dwarves, Ossuarium, Elves
- 5 Design-Only: Wyrd Conclave, Nomads, Merchants, Blighted, Chitinous
- **Total: 9 factions**

**Cross-Reference**:
- `docs/lore/world-overview.md` line 82: "Nine major factions locked in endless cycles"

**Status**: ✅ **NO CONTRADICTION FOUND**

---

## DEPRECATED FILES (Require Action)

### Files Identified as Potentially Obsolete:

1. **`docs/factions/*/deck-complete.md`** (4 files)
   - Status: Uses OLD fixed-deck system
   - Action: Archive or deprecate

2. **`docs/wiki/*.html`** (unknown number)
   - Status: May be outdated (uses "Elven Remnants")
   - Action: Verify if wiki is still maintained

3. **`docs/reference/FACTION-NAME-IDEAS.md`**
   - Status: Brainstorming document (shows old "Undead Court" name)
   - Action: Safe to keep (historical reference), but add note that names are finalized

---

## SUMMARY STATISTICS

| Category | Count | Priority |
|----------|-------|----------|
| Critical Contradictions | 2 | HIGH |
| Minor Contradictions | 2 | MEDIUM |
| Resolved Issues | 1 | N/A |
| Potential Issues (No Contradiction Found) | 4 | N/A |

---

## RECOMMENDED ACTION PLAN

### Immediate (Do Now):

1. **Fix Elven Faction Name** (7 files)
   ```bash
   # Find and replace in these files:
   docs/reference/design-roadmap.md
   docs/reference/ai-art-prompts.md
   docs/reference/PLAYTEST-READY.md
   docs/reference/casket-control-system.md
   docs/factions/dwarves/deck-complete.md
   docs/factions/index.md
   docs/campaigns/leg-skimming.md
   ```

2. **Resolve Deck System Confusion**
   - Add deprecation notice to all `deck-complete.md` files
   - OR move to `/docs/factions/archive/` folder
   - Update CLAUDE.md to explicitly state `deck-complete.md` is deprecated

### Short-Term (Next Session):

3. **Update HTML Wiki** (if still active)
   - Replace "Elven Remnants" with "Elven Verdant Covenant" in navigation
   - Verify wiki is still maintained or mark as deprecated

4. **Create Migration Guide**
   - Document transition from fixed-deck to equipment system
   - Explain why old `deck-complete.md` files exist

### Long-Term (Optional):

5. **Audit All Documentation**
   - Systematic review of every markdown file
   - Cross-reference all game mechanics (SP costs, damage values, Heat)
   - Verify all lore dates and events

---

## FILES REQUIRING UPDATES

### High Priority (Contradictions):

1. `docs/reference/design-roadmap.md` - Line 392
2. `docs/reference/ai-art-prompts.md` - Line 103
3. `docs/reference/PLAYTEST-READY.md` - Line 198
4. `docs/reference/casket-control-system.md` - Line 152
5. `docs/factions/dwarves/deck-complete.md` - Line 521
6. `docs/factions/index.md` - Line 38
7. `docs/campaigns/leg-skimming.md` - Line 143

### Medium Priority (Deprecation):

8. `docs/factions/church/deck-complete.md` - Add deprecation notice
9. `docs/factions/dwarves/deck-complete.md` - Add deprecation notice
10. `docs/factions/ossuarium/deck-complete.md` - Add deprecation notice (if exists)
11. `docs/factions/elves/deck-complete.md` - Add deprecation notice (if exists)

### Low Priority (HTML Wiki):

12. All `docs/wiki/*.html` files - Update navigation links

---

## NOTES

- ✅ Pilot state contradictions were already resolved (commit 2b021ab)
- ✅ Faction name corrections were previously applied to FACTION-NAME-IDEAS.md
- ✅ Core game mechanics (SP, Heat, dice) appear consistent across documentation
- ⚠️ Main issues are legacy files (`deck-complete.md`) and incomplete name migration

---

**END OF REPORT**

**Next Action**: Await user decision on:
1. Should `deck-complete.md` files be deleted, archived, or marked deprecated?
2. Should "Elven Remnants" → "Elven Verdant Covenant" be globally replaced?
3. Is HTML wiki still maintained?
