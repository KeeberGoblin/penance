# Penance Repository Audit
**Date**: October 17, 2025
**Auditor**: Claude Code
**Scope**: Full repository analysis for redundancies, inconsistencies, and improvements

---

## Executive Summary

**Repository Health**: 🟢 **GOOD** - Well-organized with some cleanup needed
**Total Files Audited**: 154 markdown/HTML files
**Repository Size**: 60MB (docs) + 540KB (archive) + 136KB (utilities)

**Key Findings**:
- ✅ Strong faction documentation with consistent structure
- ✅ Comprehensive combat system (GKR + KDM hybrid)
- ⚠️ Moderate HTML/markdown duplication in codex (45 HTML files)
- ⚠️ Naming inconsistencies across factions
- ⚠️ Two competing index files (readme.md vs index.md)
- ⚠️ Orphaned faction references (crucible-packs vs crucible)

---

## 🔴 HIGH PRIORITY Issues

### 1. Faction Naming Inconsistency: "Crucible Packs" vs "Crucible"

**Issue**: Directory is named `crucible/` but documentation references `crucible-packs/`

**Evidence**:
- Actual directory: `docs/factions/crucible/`
- References in [readme.md](../docs/factions/readme.md:28-30):
  ```
  - ✅ Crucible Packs
    - Path: docs/factions/crucible-packs/
    - Start here: docs/factions/crucible-packs/deck-equipment-system.md
  ```

**Impact**: Broken links, confusion for contributors

**Recommendation**:
- **Option A**: Rename directory `crucible/` → `crucible-packs/`
- **Option B**: Update all references to use `crucible/` (simpler)

---

### 2. Boss File Name Typo: "Theslar" vs "Teslar"

**Issue**: Boss character has inconsistent name spelling

**Evidence**:
- Markdown file: [boss-dr-theslar.md](../docs/scenarios/boss-dr-theslar.md)
- HTML file: [boss-dr-teslar.html](../docs/scenarios/boss-dr-teslar.html)
- Engine references: "Theslar Engine" in lore files

**Impact**: Broken cross-references, confusion in naming

**Recommendation**: Standardize to "Theslar" (appears more frequently in lore)
- Rename `boss-dr-teslar.html` → `boss-dr-theslar.html`

---

### 3. Duplicate Index Files in Factions

**Issue**: Two competing faction index files with different content

**Files**:
- [docs/factions/index.md](../docs/factions/index.md) (57 lines, detailed with playstyles)
- [docs/factions/readme.md](../docs/factions/readme.md) (45 lines, simple list)

**Differences**:
- `index.md`: Rich content with faction playstyles, mechanics, support unit links
- `readme.md`: Basic list with paths, references non-existent `crucible-packs/`

**Impact**: Confusion about canonical source, maintenance burden

**Recommendation**:
- **Keep**: `index.md` (richer, more useful)
- **Delete or convert**: `readme.md` → simple redirect to index.md

---

## 🟡 MEDIUM PRIORITY Issues

### 4. HTML/Markdown Duplication in Codex

**Issue**: 45 HTML files in `docs/codex/` duplicate markdown content

**Scope**:
- Faction pages: 9 HTML files (church, dwarves, elves, etc.)
- Rules pages: 8 HTML files (combat, turn-structure, dice, etc.)
- Campaign pages: 10 HTML files
- Scenarios: 7 HTML files
- Lore pages: 4 HTML files

**Evidence**:
- `docs/rules/taint-exploitation.md` → `docs/codex/rules-taint-exploitation.html`
- `docs/rules/turn-structure.md` → `docs/codex/rules-turn-structure.html`
- Similar pattern for scenarios, campaigns, etc.

**Impact**:
- Maintenance burden (updates must be synced)
- Risk of content drift (HTML becomes outdated)
- Increased repository size

**Recommendation**:
- **Option A**: Keep HTML as compiled/generated output (add build script)
- **Option B**: Delete HTML files, serve markdown directly
- **Option C**: Add clear note that HTML is auto-generated (don't edit manually)

**Note**: If HTMLs are generated from markdown, consider:
- Adding `.gitignore` entry for `docs/codex/*.html`
- Documenting build process in utilities/README.md

---

### 5. Faction HTML Files Use Old Names

**Issue**: Codex HTML uses different faction names than current docs

**Evidence**:
```
docs/codex/faction-undead.html    → should be "ossuarium"
docs/codex/faction-blighted.html  → should be "vestige-bloodlines"
docs/codex/faction-chitinous.html → should be "emergent"
docs/codex/faction-merchants.html → should be "exchange"
docs/codex/faction-fae.html       → "wyrd" (not yet implemented)
```

**Current Markdown Factions**:
- ✅ Church of Absolution
- ✅ Dwarven Forge-Guilds
- ✅ The Ossuarium (not "undead")
- ✅ Elven Verdant Covenant
- ✅ Vestige Bloodlines (not "blighted")
- ✅ Emergent Syndicate (not "chitinous")
- ✅ Soulstone Exchange (not "merchants")
- ✅ Crucible Packs
- 🚧 Nomad Collective
- 🚧 Wyrd Conclave (not "fae")

**Impact**: Outdated HTML content, broken mental model for users

**Recommendation**:
- Update HTML faction files to match current naming
- Or delete and regenerate from current markdown

---

### 6. Deck-Equipment-System Files Vary Significantly in Size

**Issue**: Similar files have vastly different line counts (inconsistent depth)

**Evidence**:
```
church/deck-equipment-system.md:     490 lines
crucible/deck-equipment-system.md:   529 lines
dwarves/deck-equipment-system.md:    457 lines
elves/deck-equipment-system.md:      530 lines
exchange/deck-equipment-system.md:   523 lines
ossuarium/deck-equipment-system.md:  487 lines
vestige-bloodlines/deck-equipment-system.md: 459 lines

BUT:
emergent/deck-complete-design.md:    408 lines (different filename!)
nomads/deck-complete-design.md:      451 lines (different filename!)
```

**Impact**:
- Inconsistent naming (`deck-equipment-system.md` vs `deck-complete-design.md`)
- Harder to compare factions side-by-side
- Potential content gaps in shorter files

**Recommendation**:
- Standardize all to `deck-equipment-system.md`
- Audit shorter files to ensure no missing sections
- Consider template/checklist for faction documentation

---

### 7. Missing Faction Index Link in Some Lore Files

**Issue**: Faction lore files don't consistently link back to main faction page

**Examples**:
- `emergent/lore-sibarian-origin.md` - no index link
- `exchange/lore-concordat.md` - no index link
- `crucible/lore-forge-worship.md` - no index link

**Impact**: Poor navigation, harder to explore related content

**Recommendation**: Add standard footer to all faction lore files:
```markdown
---
[← Back to [Faction] Index](deck-equipment-system.md) | [View All Factions](../index.md)
```

---

## 🟢 LOW PRIORITY Issues (Polish & Organization)

### 8. Support Units Files Inconsistently Present

**Current State**:
- ✅ Church: [support-units.md](../docs/factions/church/support-units.md) (801 lines)
- ✅ Dwarves: [support-units.md](../docs/factions/dwarves/support-units.md) (763 lines)
- ✅ Ossuarium: [support-units.md](../docs/factions/ossuarium/support-units.md) (822 lines)
- ✅ Elves: [support-units.md](../docs/factions/elves/support-units.md) (853 lines)
- ❌ Vestige Bloodlines: **MISSING**
- ❌ Emergent Syndicate: **MISSING**
- ❌ Exchange: **MISSING**
- ❌ Crucible: **MISSING**

**Impact**: Incomplete faction design (support units are optional but useful)

**Recommendation**:
- Mark as "TODO" in faction documentation
- OR document that some factions don't use support units (if intentional)

---

### 9. Archive Directory Needs Cleanup

**Current State**:
```
archive/
  card-generator-old/        (old HTML tools)
  wiki-index-old.html       (orphaned wiki)
utilities/archive/audits/
  AUDIT-2025-10-15.md
  COMPREHENSIVE-V3-AUDIT-2025-10-14.md
```

**Issues**:
- Unclear what's in `archive/card-generator-old/` (540KB)
- Two recent audits in utilities/archive (good!)
- Old wiki HTML files still present

**Recommendation**:
- Add `archive/README.md` explaining what's archived and why
- Consider deleting truly obsolete files (pre-v2.0 card generators)
- Keep recent audits (good historical record)

---

### 10. Inconsistent Mechanics Documentation Depth

**Observation**: Some faction-specific mechanics are deeply documented, others less so

**Well-Documented**:
- ✅ Emergent: [metamorph-mechanics.md](../docs/factions/emergent/metamorph-mechanics.md), [hive-mind-coordination.md](../docs/factions/emergent/hive-mind-coordination.md)
- ✅ Exchange: [credit-economy.md](../docs/factions/exchange/credit-economy.md), [mercenary-hiring.md](../docs/factions/exchange/mercenary-hiring.md)
- ✅ Crucible: [forge-token-mechanics.md](../docs/factions/crucible/forge-token-mechanics.md), [honor-duel-system.md](../docs/factions/crucible/honor-duel-system.md)

**Less Documented**:
- ⚠️ Church: Only deck-equipment-system.md (no deep dive on Blood Offering mechanics)
- ⚠️ Dwarves: Only deck-equipment-system.md (no deep dive on Rune Counter mechanics)
- ⚠️ Ossuarium: Only deck-equipment-system.md (no deep dive on Soul Harvest triggers)

**Impact**: Harder for players to master older factions

**Recommendation**: Consider adding mechanics deep-dives for Church, Dwarves, Ossuarium:
- `church/blood-offering-combos.md`
- `dwarves/rune-counter-tactics.md`
- `ossuarium/soul-harvest-guide.md`

---

## ✅ STRENGTHS (Things Done Well)

### Excellent Documentation Structure
- ✅ Clear faction folders with consistent layouts
- ✅ Comprehensive [casket-types.md](../docs/factions/casket-types.md) (1140 lines!)
- ✅ Detailed [tactics-overview.md](../docs/factions/tactics-overview.md) (638 lines)
- ✅ Strong [relationships.md](../docs/factions/relationships.md) (421 lines)

### Combat System is Well-Documented
- ✅ [combat-system.md](../docs/rules/combat-system.md) clearly explains GKR + KDM hybrid
- ✅ Deck-as-HP system fully documented
- ✅ Component damage rules clear
- ✅ Pilot Wound Deck system explained

### Lore is Rich and Consistent
- ✅ 437-year timeline well-established
- ✅ Origin stories for factions (Emergent, Exchange, Vestige)
- ✅ [chronicle.md](../docs/lore/chronicle.md) and [chronicle-enhanced.md](../docs/lore/chronicle-enhanced.md)
- ✅ [iconic-npcs.md](../docs/lore/iconic-npcs.md)

### Reference Materials are Strong
- ✅ [playtest-assessment.md](../docs/reference/playtest-assessment.md) (realistic status)
- ✅ [equipment-pool-complete.md](../docs/reference/equipment-pool-complete.md)
- ✅ [ai-art-prompts.md](../docs/reference/ai-art-prompts.md) (very detailed)
- ✅ [card-template-specification.md](../docs/reference/card-template-specification.md)

---

## 📋 RECOMMENDATIONS SUMMARY

### Immediate Actions (1-2 hours)
1. ✅ **Fix crucible naming**: Rename folder OR update readme.md references
2. ✅ **Fix Theslar/Teslar**: Rename `boss-dr-teslar.html` → `boss-dr-theslar.html`
3. ✅ **Consolidate faction indexes**: Keep index.md, delete or redirect readme.md
4. ✅ **Standardize deck file names**: Rename `deck-complete-design.md` → `deck-equipment-system.md`

### Short-Term Improvements (4-6 hours)
5. ✅ **Document HTML generation**: Add note to codex/README explaining HTML build process
6. ✅ **Update faction HTML files**: Match current faction names (undead→ossuarium, etc.)
7. ✅ **Add navigation footers**: Standardize back-links in faction lore files
8. ✅ **Archive cleanup**: Add archive/README.md explaining contents

### Long-Term Enhancements (Optional)
9. ⚠️ **Support units**: Complete for remaining 4 factions (Vestige, Emergent, Exchange, Crucible)
10. ⚠️ **Mechanics deep-dives**: Add detailed guides for Church, Dwarves, Ossuarium
11. ⚠️ **Faction balance audit**: Ensure all 8 playable factions have similar documentation depth

---

## 📊 METRICS

### Documentation Completeness by Faction

| Faction | Deck System | Support Units | Lore Files | Mechanics Docs | Status |
|---------|-------------|---------------|------------|----------------|--------|
| Church | ✅ (490L) | ✅ (801L) | ⚠️ Basic | ❌ Missing | 75% |
| Dwarves | ✅ (457L) | ✅ (763L) | ⚠️ Basic | ❌ Missing | 75% |
| Ossuarium | ✅ (487L) | ✅ (822L) | ⚠️ Basic | ❌ Missing | 75% |
| Elves | ✅ (530L) | ✅ (853L) | ⚠️ Basic | ❌ Missing | 75% |
| Vestige | ✅ (459L) | ❌ Missing | ✅ Excellent | ⚠️ Basic | 70% |
| Emergent | ✅ (408L) | ❌ Missing | ✅ Excellent | ✅ Excellent | 90% |
| Exchange | ✅ (523L) | ❌ Missing | ✅ Excellent | ✅ Excellent | 90% |
| Crucible | ✅ (529L) | ❌ Missing | ✅ Excellent | ✅ Excellent | 90% |
| Nomads | 🚧 (451L) | ❌ Missing | ⚠️ Basic | ❌ Missing | 50% |
| Wyrd | ❌ Missing | ❌ Missing | ❌ Missing | ❌ Missing | 0% |

**Average Completeness**: 75% (for 8 playable factions)

### File Type Distribution
- Markdown files: ~100 (65%)
- HTML files: ~54 (35%)
- Total: 154 files

### Largest Documentation Files (Top 10)
1. `casket-types.md` - 1,140 lines
2. `elves/support-units.md` - 853 lines
3. `ossuarium/support-units.md` - 822 lines
4. `church/support-units.md` - 801 lines
5. `dwarves/support-units.md` - 763 lines
6. `tactics-overview.md` - 638 lines
7. `elves/deck-equipment-system.md` - 530 lines
8. `crucible/deck-equipment-system.md` - 529 lines
9. `exchange/deck-equipment-system.md` - 523 lines
10. `crucible/lore-forge-worship.md` - 496 lines

---

## 🎯 CONCLUSION

**Overall Assessment**: **🟢 HEALTHY REPOSITORY**

The Penance repository is well-organized with strong foundational documentation. The combat system is clearly explained, faction designs are comprehensive, and lore is rich. Main issues are minor inconsistencies (naming, duplication) rather than fundamental problems.

**Priority**: Focus on fixing the 4 immediate naming/consistency issues first. The HTML duplication is manageable if it's part of a build process. Support units and mechanics deep-dives are nice-to-have enhancements.

**Playtest Readiness**: ✅ Confirmed - Core systems are documented and complete per [playtest-assessment.md](../docs/reference/playtest-assessment.md)

---

**Audit Generated**: October 17, 2025
**Next Audit Recommended**: After major version update (v3.0) or 3 months
