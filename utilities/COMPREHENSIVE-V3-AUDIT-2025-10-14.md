# Comprehensive Version 3.0 Audit Report
## Penance: Absolution Through Steel

**Audit Date**: October 14, 2025
**Auditor**: Claude
**Repository Status**: Version 3.0 (Partial Integration)

---

## Executive Summary

**Total Files**: 69 markdown files, 34 HTML files
**v3.0 Status**: 3 new mechanics systems created, but minimal integration with existing files
**Contradictions Found**: 0 major contradictions
**Missing Cross-References**: ~40 files could benefit from v3.0 references
**Playability Impact**: **LOW** - v3.0 systems are standalone, v2.0 remains fully functional

### Overall Assessment: ✅ FUNCTIONAL BUT INCOMPLETE INTEGRATION

The v3.0 mechanics systems are complete and playable, but they exist in isolation. Core rules files don't reference them, and faction/campaign files lack integration. This is **acceptable for optional mechanics**, but reduces discoverability.

---

## Detailed Findings

### 1. Core Rules Files (v2.0 Base)

**Files Still Marked v2.0**:
- `docs/rules/combat-system.md` - Version 2.0 (October 10, 2025)
- `docs/rules/turn-structure.md` - Version 2.0 (October 10, 2025)
- `docs/rules/range-and-los.md` - Version 2.0 (October 10, 2025)
- `docs/rules/support-units.md` - Version 2.0 Equipment System
- `docs/campaigns/event-tables-kdm-style.md` - Version 2.0

**Issue**: These files don't mention v3.0 mechanics exist
**Impact**: Players won't discover optional rules unless they read index/quick-ref
**Severity**: MEDIUM (discoverability issue, not functional problem)

---

### 2. Dice Pool Integration

**Current Status**:
- `dice-pool-advantage.md` exists and is complete
- `quick-reference.md` has v3.0 Dice Pool table
- `rules/index.md` links to dice-pool-advantage.md

**Missing Integrations**:
- `combat-system.md` - No mention of Dice Pool as alternative to static modifiers
- `range-and-los.md` - Still uses static +1/+2 modifiers, no Dice Pool mention
- `dice-reference.md` - Doesn't explain Advantage/Disadvantage rolling

**Specific Gaps**:

#### combat-system.md (Line 149-190)
```
Current: "Base To-Hit: 5+ (roll 2d6 Attack Dice)"
Missing: Note that says "OPTIONAL: Use Dice Pool Advantage (see dice-pool-advantage.md)"
```

#### range-and-los.md (Line 44-64)
```
Current: "Medium Range (4-6 hexes): +1 to target number"
Missing: "OPTIONAL: Use Disadvantage instead (see dice-pool-advantage.md)"
```

#### dice-reference.md
```
Missing: Section explaining "Rolling Advantage/Disadvantage (v3.0 Optional)"
Should include: "Roll 3d6, discard lowest/highest, add 2 remaining"
```

**Recommendation**: Add 1-2 sentence notes in these files pointing to dice-pool-advantage.md

---

### 3. Taint Exploitation Integration

**Current Status**:
- `taint-exploitation.md` exists and is complete
- `quick-reference.md` has Taint Exploitation tables
- `rules/index.md` links to taint-exploitation.md

**Existing Taint References** (NOT v3.0 compliant):
- `combat-system.md` mentions "gain 1 Taint" for Church cards
- `turn-structure.md` mentions "Taint Overload (when Taint reaches 10)"
- These are old v2.0 Taint (threshold system), NOT v3.0 Taint Exploitation

**Contradiction Found**:
```
OLD v2.0 System: "Taint reaches 10 → Corrupted"
NEW v3.0 System: "Taint is tactical resource, spend offensively/defensively, 10+ = Corruption Save"
```

**Severity**: LOW (v2.0 Taint still works, v3.0 just adds exploitation)

**Missing Integrations**:
- `combat-system.md` - No mention of spending Taint for offensive exploits
- `turn-structure.md` - No mention of Taint Markers in Refresh Phase
- Faction files - No mention of faction-specific Taint interactions

**Faction-Specific Taint Gaps**:

#### Church Faction (docs/factions/church/deck-equipment-system.md)
```
Missing: "Church pilots start with +1 Grit and embrace Taint for martyrdom"
Missing: "Church Corruption Save is 3+ instead of 4+ (zealotry protects)"
```

#### Dwarven Faction (docs/factions/dwarves/deck-equipment-system.md)
```
Missing: "Dwarves gain Taint at half rate (6 damage = 1 Taint instead of 2)"
Missing: "Cannot spend Taint for Desperate Power (rune-locked)"
```

#### Ossuarium Faction (docs/factions/ossuarium/deck-equipment-system.md)
```
Missing: "Ossuarium thrives on Taint, 'Soul Harvest' spends 2 Taint to recover 3 cards"
Missing: "Corruption Save: 5+ (very resistant, already undead)"
```

#### Elven Faction (docs/factions/elves/deck-equipment-system.md)
```
Missing: "Elves gain Taint at double rate (3 damage = 2 Taint)"
Missing: "Corruption Save: 5+ only in Forest terrain"
```

**Recommendation**: Add "v3.0 Taint Interactions" section to each faction file

---

### 4. Pilot Grit Integration

**Current Status**:
- `pilot-grit-system.md` exists and is complete
- `quick-reference.md` has Grit Check table
- `rules/index.md` links to pilot-grit-system.md (though in wrong directory)

**Missing Integrations**:

#### pilot-progression.md
```
Current: Has "Survivor's Grit" scar (unrelated to v3.0 Grit stat)
Missing: Section explaining "Pilot Grit Stat (0-3)" and how it grows
Missing: Pilot sheet template with Grit field
```

#### leg-skimming.md
```
Current: Lists permanent bonuses (+1 SP, etc.)
Missing: "Leg-Skimming grants +1 Grit permanently (see pilot-grit-system.md)"
```

#### campaigns/index.md
```
Current: Lists campaign systems
Missing: Link to pilot-grit-system.md
```

#### support-units.md
```
Current: Describes Support Unit AI behavior
Missing: "Support Units gain +1 Morale if commanded by Grit 2+ pilot"
```

**Recommendation**: Add Grit cross-references to campaign files

---

### 5. HTML/Codex Pages (The Codex)

**Current Status**: 34 HTML files, NONE reference v3.0 mechanics

**Missing HTML Pages**:
1. `docs/codex/rules-dice-pool.html` - Dice Pool Advantage system
2. `docs/codex/rules-taint-exploitation.html` - Taint as tactical resource
3. `docs/codex/campaign-pilot-grit.html` - Grit stat progression

**HTML Pages Needing Updates** (Faction Modifiers):
1. `docs/codex/faction-church.html` - Add Grit +1, Taint embrace
2. `docs/codex/faction-dwarves.html` - Add Grit +1 vs Severe, Taint resist
3. `docs/codex/faction-undead.html` - Add Grit immune, Taint thrive
4. `docs/codex/faction-elves.html` - Add Grit -1, Taint vulnerable

**HTML Pages Needing Updates** (Rules References):
5. `docs/codex/rules-combat.html` - Add Dice Pool option note
6. `docs/codex/rules-turn-structure.html` - Add Taint Marker tracking
7. `docs/codex/rules-quick-ref.html` - Add v3.0 tables (or link to MD quick-ref)

**Navigation Updates Needed**:
- `docs/codex/index.html` - Add "v3.0 Optional Rules" section to navigation
- Link to 3 new HTML pages from main Codex navigation

**Recommendation**: Create 3 new HTML pages + update faction pages with modifiers

---

### 6. Main Website (docs/index.html)

**Current Status**: Website homepage doesn't mention v3.0

**Missing**:
- No "Version 3.0 Update" announcement banner
- No link to v3.0 mechanics in main navigation
- "Recent Updates" section doesn't list v3.0 (still shows v2.0 dates)

**Recommendation**: Add v3.0 announcement section to homepage

---

### 7. CLAUDE.md Context Document

**Current Status**: CLAUDE.md last updated October 13, 2025 (before v3.0)

**Missing**:
- No mention of v3.0 mechanics systems
- No guidance on Dice Pool Advantage for future AI assistants
- No Taint Exploitation system notes
- No Pilot Grit progression context

**Should Add**:
```markdown
## Version 3.0 Optional Mechanics (October 14, 2025)

### Dice Pool Advantage (Trench Crusade-Inspired)
- Replace static +1/+2 modifiers with roll-more-dice system
- Advantage: 3d6 take 2 highest
- Critical Advantage: 4d6 take 2 highest
- Works with existing Attack Dice symbols
- OPTIONAL enhancement to v2.0 base rules

### Taint Exploitation (Tactical Resource)
- Spend enemy Taint offensively (1-5 Taint costs)
- Spend own Taint for desperate power (2-5 Taint costs)
- Faction interactions: Church embrace, Dwarves resist, etc.
- OPTIONAL enhancement to v2.0 Taint threshold system

### Pilot Grit (Campaign Stat)
- Stat 0-3 that grows with missions/injuries survived
- Roll 1d6+Grit to resist Pilot Wounds
- Faction modifiers: Church +1 start, Dwarves +1 vs Severe, etc.
- OPTIONAL enhancement for campaign play
```

**Recommendation**: Update CLAUDE.md with v3.0 section

---

### 8. Cross-Reference Check

**Broken Links**: None found (all internal links work)

**Weak Cross-References** (files that should link to v3.0 but don't):
- `combat-system.md` → should link to `dice-pool-advantage.md`
- `turn-structure.md` → should link to `taint-exploitation.md`
- `range-and-los.md` → should link to `dice-pool-advantage.md`
- `pilot-progression.md` → should link to `pilot-grit-system.md`
- `leg-skimming.md` → should link to `pilot-grit-system.md`
- All 4 faction files → should link to `taint-exploitation.md` and `pilot-grit-system.md`

**Recommendation**: Add "See also" sections with v3.0 links

---

### 9. Contradiction Analysis

**NONE FOUND** - v3.0 mechanics are additive, not replacement

**Potential Confusion**:
- Old v2.0 "Taint threshold" vs new v3.0 "Taint Exploitation"
  - **Resolution**: v3.0 includes v2.0 threshold (10+ = Corruption), just adds tactical uses
  - No contradiction, but should clarify in docs

**Name Collision**:
- `pilot-progression.md` has "Survivor's Grit" scar (unrelated to v3.0 Grit stat)
  - **Resolution**: Rename scar to "Survivor's Tenacity" to avoid confusion

**Recommendation**: Rename "Survivor's Grit" scar in pilot-progression.md

---

### 10. Version Number Consistency

**README.md**: Version 3.0 ✅
**rules/index.md**: Version 3.0 ✅
**quick-reference.md**: Has v3.0 section ✅

**Still marked v2.0**:
- combat-system.md (should update to "v2.0 base, see v3.0 enhancements")
- turn-structure.md (should update to "v2.0 base, see v3.0 enhancements")
- range-and-los.md (should update to "v2.0 base, see v3.0 enhancements")
- support-units.md (should update to "v2.0 base, see v3.0 enhancements")

**Recommendation**: Add "v3.0 enhancements available" note to v2.0 headers

---

## Priority Fix List

### CRITICAL (Blocks v3.0 Discovery)

1. **combat-system.md** - Add note about Dice Pool option
2. **range-and-los.md** - Add note about Dice Pool option
3. **All 4 faction files** - Add Taint/Grit modifier sections

### HIGH (Improves Integration)

4. **pilot-progression.md** - Add Grit stat section, rename "Survivor's Grit" scar
5. **leg-skimming.md** - Add "+1 Grit" to bonuses list
6. **support-units.md** - Add Grit synergy note
7. **CLAUDE.md** - Add v3.0 section for future AI context

### MEDIUM (Enhances Experience)

8. Create 3 new HTML codex pages (dice-pool, taint, grit)
9. Update 4 faction HTML pages with Taint/Grit modifiers
10. Update docs/index.html with v3.0 announcement
11. **dice-reference.md** - Add Advantage/Disadvantage section

### LOW (Nice to Have)

12. Update turn-structure.md with Taint Marker tracking
13. Update combat-system.md version header
14. Update navigation in codex/index.html

---

## Estimated Work by Priority

**CRITICAL Fixes**: ~2 hours
- 3 core rules files + 4 faction files = 7 files
- Add 1-3 paragraphs per file

**HIGH Fixes**: ~1.5 hours
- 4 campaign files + CLAUDE.md = 5 files
- Add sections or cross-references

**MEDIUM Fixes**: ~3 hours
- Create 3 HTML pages + update 5 existing HTML pages
- Web development work

**LOW Fixes**: ~1 hour
- Minor updates to existing files

**Total Estimated Time**: 7.5 hours for complete integration

---

## Recommended Action Plan

### Option A: Minimal Integration (1 hour)
**Goal**: Make v3.0 discoverable from core rules

1. Add 1-sentence notes to combat/range/turn files: "OPTIONAL v3.0 enhancements available, see quick-reference.md"
2. Add Taint/Grit sections to 4 faction files (2 paragraphs each)
3. Rename "Survivor's Grit" scar in pilot-progression.md

**Result**: v3.0 is discoverable, factions have modifiers, no confusion

---

### Option B: Full Integration (7.5 hours)
**Goal**: Complete v3.0 integration across all files

1. Update all core rules files with v3.0 cross-references
2. Update all campaign files with Grit integration
3. Update all faction files with Taint/Grit modifiers
4. Create 3 new HTML codex pages
5. Update faction HTML pages
6. Update CLAUDE.md
7. Update main website homepage

**Result**: v3.0 fully integrated, all cross-references work, HTML/codex complete

---

### Option C: Current State (0 hours)
**Goal**: Leave as-is, v3.0 remains optional enhancement

**Pros**:
- v3.0 is fully functional as standalone systems
- v2.0 base rules unaffected
- Clear separation between base and optional rules

**Cons**:
- Low discoverability (players must read index/quick-ref)
- Faction modifiers not documented
- HTML/codex incomplete

**Result**: Acceptable for optional mechanics, but incomplete for full release

---

## Conclusion

**Current Status**: Version 3.0 mechanics are **playable and complete**, but **poorly integrated** with existing documentation.

**Recommendation**: **Option A (Minimal Integration)** - 1 hour of work to make v3.0 discoverable and document faction modifiers. This gives the best ROI for playability without requiring extensive HTML/codex work.

**Long-Term**: Consider **Option B (Full Integration)** before v3.0 official release or Kickstarter campaign.

---

## Files Requiring Updates (Summary)

**CRITICAL (7 files)**:
1. docs/rules/combat-system.md
2. docs/rules/range-and-los.md
3. docs/factions/church/deck-equipment-system.md
4. docs/factions/dwarves/deck-equipment-system.md
5. docs/factions/ossuarium/deck-equipment-system.md
6. docs/factions/elves/deck-equipment-system.md
7. docs/campaigns/pilot-progression.md (rename scar)

**HIGH (4 files)**:
8. docs/campaigns/leg-skimming.md
9. docs/campaigns/index.md
10. docs/rules/support-units.md
11. utilities/CLAUDE.md

**MEDIUM (8 files)**:
12-14. Create 3 new HTML files
15-19. Update 5 existing HTML files
20. docs/index.html

**LOW (3 files)**:
21. docs/rules/turn-structure.md
22. docs/rules/dice-reference.md
23. docs/codex/index.html

**Total**: 23 files needing updates (out of 103 total files)

---

**END OF AUDIT**

---

*"The mechanics are sound. The integration is pending. Prioritize discoverability."*
