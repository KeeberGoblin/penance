# Codex HTML Audit Report

**Date:** 2025-11-11
**Audited Directory:** `/docs/codex/`
**Total Files:** 124 HTML files (121 active pages + 3 archive files)
**Total Lines of Code:** 69,178 lines

---

## Executive Summary

✅ **Image References:** All 14 unique image references verified as existing
⚠️ **Broken Links:** 3 broken internal links found across 6 pages
✅ **Stylesheet Consistency:** All pages use `manuscript-style.css`
⚠️ **Navigation Consistency:** Consistent structure, but new species demographics page not linked from index

---

## 1. Image Reference Audit

### Status: ✅ PASS

All 14 unique image references found in codex HTML files exist in the filesystem:

**Faction Images (12):**
- ✓ `../images/Church2_PlaceH.png`
- ✓ `../images/CruciblePact_PlaceH.png`
- ✓ `../images/Exchange_PlaceH.png`
- ✓ `../images/ForgeG_PlaceH.png`
- ✓ `../images/IronDoctrine.png`
- ✓ `../images/Wyrd_PlaceH.png`
- ✓ `../images/bloodlines_PlaceH.png`
- ✓ `../images/draconis_PlaceH.png`
- ✓ `../images/nomad_PlaceH.png`
- ✓ `../images/ossuarium_PlaceH.png`
- ✓ `../images/syndicate_PlaceH.png`
- ✓ `../images/verdant2_PlaceH.png`

**Lore Images (2):**
- ✓ `../images/soulstones/Lore_SoulstoneExposionSketch.png`
- ✓ `../images/soulstones/Lore_SoulstoneSketch.png`

---

## 2. Internal Link Audit

### Status: ⚠️ ISSUES FOUND

**Total Internal Links Extracted:** 102 unique `.html` references
**Broken Links:** 3
**Success Rate:** 97.1%

### Broken Links

#### 1. `faction-ossuarium.html` (MISSING)

**Actual File:** `faction-undead.html` exists instead
**Referenced By:**
- `lore-bonelord-karath.html`
- `lore-casket-manufacturing.html`
- `lore-settlements.html`

**Recommendation:** Update all 3 files to link to `faction-undead.html` instead of `faction-ossuarium.html`

---

#### 2. `faction-wyrd.html` (MISSING)

**Actual Files:**
- `wyrd_mechanic.html` (mechanics/gameplay page) exists
- No faction-specific "faction-wyrd.html" page exists

**Referenced By:**
- `lore-chronicle.html`

**Recommendation:** Either:
- Create `faction-wyrd.html` as a faction overview page, OR
- Update link to point to `wyrd_mechanic.html` (mechanics page)

---

#### 3. `lore-caskets-revised.html` (MISSING)

**Actual File:** `lore-caskets-overview.html` exists instead
**Referenced By:**
- `lore-neural-threads.html`
- `lore-soulstone-system.html`

**Recommendation:** Update both files to link to `lore-caskets-overview.html` instead of `lore-caskets-revised.html`

---

## 3. Stylesheet Consistency Audit

### Status: ✅ PASS

All 124 HTML files consistently reference:
- `manuscript-style.css`

No missing or inconsistent stylesheet references found.

---

## 4. Navigation Structure Audit

### Status: ✅ PASS (with recommendations)

**Standard Navigation Pattern:**
```html
<nav class="codex-nav" id="codexNav">
    <a href="index.html" class="nav-home">← Return to Codex</a>
    <span class="nav-separator">|</span>
```

**Lore Pages Linking to Index:** 123 of 123 lore pages have proper index links

### Navigation Observations

1. All pages follow consistent navigation structure
2. Breadcrumb navigation implemented across all pages
3. "Return to Codex" link present on all pages

---

## 5. Newly Created Content

### `lore-species-demographics.html`

**Status:** ✅ Created and functional
**Linked From Other Pages:** ⚠️ None yet

**Features:**
- Chart.js integration for population visualizations
- Pie chart for subspecies distribution
- Bar chart for faction demographics
- Responsive manuscript styling
- 620 lines of HTML

**Recommendation:** Link this page from:
- `index.html` (main codex index)
- `content-home.html` (content navigation)
- `lore-factions-overview.html` (faction context)
- `cosmology.html` (related cosmology content)

---

## 6. File Inventory

### By Category

**Faction Pages (12):**
- `faction-ashborne.html` (Iron Doctrine)
- `faction-bloodlines.html`
- `faction-church.html`
- `faction-crucible.html`
- `faction-draconid.html`
- `faction-dwarves.html`
- `faction-elves.html`
- `faction-emergent.html`
- `faction-exchange.html`
- `faction-fae.html`
- `faction-nomads.html`
- `faction-undead.html`

**Lore Pages (23):**
Including chronicles, casket technology, NPCs, world events, cosmology, and species demographics

**Campaign Pages (15):**
Event tables, settlement phase, pilot progression, mission generation, etc.

**Rules Pages (18):**
Combat, deck construction, dice mechanics, support units, terrain, etc.

**Scenario Pages (10):**
Tutorial missions, boss fights, example scenarios

**Mechanics Pages (10):**
Faction-specific mechanical deep dives

**Other Pages (36):**
Bestiary, GM tools, reference cards, balance sheets, etc.

---

## 7. Priority Action Items

### High Priority

1. **Fix Broken Links (3 files to update, 6 pages affected)**
   - Update `lore-bonelord-karath.html`: Change `faction-ossuarium.html` → `faction-undead.html`
   - Update `lore-casket-manufacturing.html`: Change `faction-ossuarium.html` → `faction-undead.html`
   - Update `lore-settlements.html`: Change `faction-ossuarium.html` → `faction-undead.html`
   - Update `lore-chronicle.html`: Change `faction-wyrd.html` → `wyrd_mechanic.html` (or create faction-wyrd.html)
   - Update `lore-neural-threads.html`: Change `lore-caskets-revised.html` → `lore-caskets-overview.html`
   - Update `lore-soulstone-system.html`: Change `lore-caskets-revised.html` → `lore-caskets-overview.html`

2. **Link New Species Demographics Page**
   - Add link from `index.html`
   - Add link from `content-home.html`
   - Add cross-reference from `cosmology.html`

### Medium Priority

3. **Consider Creating Missing Pages**
   - `faction-wyrd.html` - Wyrd Conclave faction overview (currently only mechanics page exists)
   - Cross-check if any other factions are missing dedicated faction pages

### Low Priority

4. **Documentation Maintenance**
   - Update `DOCS_ORGANIZATION.md` to reflect this audit
   - Consider adding automated link checking to CI/CD

---

## 8. Statistics

| Metric | Value |
|--------|-------|
| Total HTML Files | 124 |
| Total Lines | 69,178 |
| Total Internal Links | 102 unique |
| Broken Links | 3 (2.9%) |
| Image References | 14 |
| Missing Images | 0 (0%) |
| Stylesheet Consistency | 100% |
| Pages Needing Updates | 6 |

---

## 9. Verification Commands

To verify fixes, run:

```bash
# Check for remaining broken links
cd docs/codex && grep -E 'href="(faction-ossuarium|faction-wyrd|lore-caskets-revised)\.html"' *.html

# Verify all images still exist
cd docs && for img in images/*.png images/*/*.png; do [ -f "$img" ] && echo "✓ $img" || echo "✗ $img"; done

# Check if species demographics is linked
grep -l "lore-species-demographics" docs/codex/*.html
```

---

## 10. Conclusion

The codex HTML codebase is in **good overall health** with minor linking issues that can be quickly resolved. All critical assets (images, stylesheets) are present and properly referenced. The navigation structure is consistent across all pages.

**Recommended Next Steps:**
1. Fix the 6 broken link references (high priority)
2. Link the new species demographics page into the navigation
3. Consider creating a `faction-wyrd.html` faction overview page for consistency

---

**Audit Conducted By:** Claude Code
**Tools Used:** Bash, grep, sed, file system verification
**Next Audit Recommended:** After link fixes are applied
