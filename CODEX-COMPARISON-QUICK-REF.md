# Codex HTML↔MD Comparison - Quick Reference

## Critical Issues Requiring Immediate Action

### 🔴 CRITICAL: Naming Conflict
**Bonelord Name Inconsistency**
- **HTML files**: "Bonelord Karath"
- **MD files**: "Bonelord Thresh"
- **MD files**: "Bonelord Karath"
- **Files affected**: cosmology.html/.md, pilot-skills.html/.md, potentially more
- **ACTION NEEDED**: Choose canonical name and update ALL files

---

### 🔴 CRITICAL: Balance Outdated in MD

**Elven Verdant Covenant** (`docs/factions/elves/deck-equipment-system.md`)

| Mechanic | HTML (Current v5.29) | MD (Outdated) | Status |
|----------|----------------------|---------------|--------|
| **Bleed Cap** | 8 stacks (reduced Oct 19) | 10 stacks | ❌ OUTDATED |
| **Photosynthesis** | REMOVED (line 433) | REVISED (still active) | ❌ OUTDATED |
| **Leaf Dance** | 2 hexes | 3 hexes | ❌ OUTDATED |
| **Living Seal** | No passive regen | Conditional regen | ⚠️ UNCLEAR |
| **Verdant Regen** | 2 cards unconditional | 1 card (+1 with Living Seal) | ⚠️ CONFLICT |

**ACTION NEEDED**: Update `deck-equipment-system.md` to match v5.29 balance

---

### 🔴 CRITICAL: Missing MD File

**Void Lore** - No standalone `/docs/lore/void.md`
- HTML file: 530+ lines of detailed void lore
- MD equivalent: ~18 lines in cosmology.md
- **ACTION NEEDED**: Extract void.html content to new void.md

---

## File Mapping Reference

### ✅ Well-Aligned Files
- `campaign-pilot-skills.html` ↔ `campaign/pilot-skills.md` (95% match)

### ⚠️ Partial Coverage
- `faction-elves.html` ↔ `factions/elves/deck-equipment-system.md` (complementary)
- `cosmology.html` ↔ `lore/cosmology-and-origins.md` (complementary)
- `lore-soulstone-system.html` ↔ `lore/soulstone-system.md` (different focus)

### ❌ No MD Equivalent Found
- `lore-void.html` - NO STANDALONE MD
- `lore-bonelord-karath.html` - likely missing
- `lore-ground-zero.html` - likely missing
- `lore-npcs.html` - likely missing
- Multiple scenario files - check needed
- `gm-helper.html` - likely missing

---

## Content Patterns

### HTML Files Tend to Have:
- ✅ More lore exposition
- ✅ Visual presentation (CSS, images)
- ✅ Recent balance updates
- ✅ Faction relationships tables
- ✅ Schisms and mirror match lore
- ✅ V3.0 optional rules integration
- ✅ Support unit stat blocks

### MD Files Tend to Have:
- ✅ Equipment card lists with SP costs
- ✅ Build examples with deck breakdowns
- ✅ Tactics lists
- ✅ Counter-play sections
- ✅ Campaign progression paths
- ✅ Technology timeline details
- ✅ Detailed procedure mechanics

---

## Quick Fix Checklist

- [ ] **Decide: Bonelord name** (Karath or Thresh?)
- [ ] **Find-replace** chosen name across ALL files
- [ ] **Update** `factions/elves/deck-equipment-system.md`:
  - [ ] Bleed cap 10 → 8
  - [ ] Remove Photosynthesis card
  - [ ] Leaf Dance 3 → 2 hexes
- [ ] **Create** `lore/void.md` from void.html
- [ ] **Create** `HTML_TO_MD_FILE_MAP.md`
- [ ] **Create** `BALANCE-CHANGELOG.md`
- [ ] **Add** tech level section to cosmology.html

---

## Statistics

- **HTML files**: 85 in `docs/codex/`
- **MD files**: 170+ across all `docs/` subdirectories
- **Files compared**: 6 pairs in depth
- **Critical issues**: 3 (naming, balance, missing void)
- **Alignment score**: 6.5/10

---

## For Full Details

See: `/home/user/penance/CODEX-MARKDOWN-COMPARISON-REPORT.md`

Last updated: 2025-11-05
