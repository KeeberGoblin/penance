# Repository Cleanup Summary
**Date**: October 22, 2025
**Performed By**: Claude Code
**Purpose**: Remove clutter, organize archives, delete deprecated files

---

## Files Moved to Archive

### Balance Reports & Session Summaries → `/docs/archive-v5-history/`
- `ARMY-BALANCE-v5.14c-RESULTS.md`
- `MULTIUNIT-BALANCE-v5.14d-RESULTS.md`
- `POINT-COST-UPDATE-v5.14c.md`
- `V5.15-BALANCE-PLAN.md`
- `CRITICAL-DICE-MECHANICS-BUG-REPORT.md`
- `ARMY-BUILDER-SYSTEM.md`
- `SESSION-SUMMARY-v5.15-BALANCE-WORK.md` (from `/simulation/`)

### Repository Audits → `/archive/utilities-archive/`
- `REPOSITORY-AUDIT-2025-10-21.md`
- `IMPROVEMENTS-2025-10-21.md`

### Backup Files → `/docs/archive-backups-2025-10-21/`
- `complete-card-data.json.v5.14d-backup` (from `/docs/cards/`)

### Duplicate Scenarios → `/docs/scenarios/archive/`
- `boss-dr-theslar.md` (HTML version kept in main scenarios)

### Old Lore Files → `/docs/lore/archive/`
- `casket-technology.md` (revised version `casket-technology-revised.md` kept)

### Sample Iterations → `/tools/archive-samples/`
- `church-sample-sheet1.svg`
- `church-sample-sheet2.svg`
- `church-sample-sheet3.svg`

---

## Files Deleted

### Deprecated Faction Images
- `docs/images/MerchantGuild_PlaceH.png` (faction renamed to "The Exchange")
- `docs/images/pack_PlaceH.png` (faction renamed to "Vestige Bloodlines")

### Python Cache
- `simulation/__pycache__/` (directory and all .pyc files)

---

## Current State Summary

### Clean Root-Level Docs
Only essential files remain in `/docs/`:
- `BALANCE-FINAL-V5.29.md` (current balance document)
- `README.md` (directory index)
- `index.html` (codex entry point)
- `favicon.png`

### Archive Structure
Well-organized archives:
- `/archive/` - Top-level historical documents
- `/archive/utilities-archive/` - Audit reports and utility docs
- `/docs/archive-v5-history/` - Version 5.x balance iterations
- `/docs/archive-backups-2025-10-21/` - JSON backups
- `/docs/codex/archive-pre-v529/` - Pre-v5.29 balance files
- `/docs/scenarios/archive/` - Old scenario versions
- `/docs/lore/archive/` - Superseded lore documents
- `/tools/archive-samples/` - Sample sheet iterations

### No Redundant Files Found
- No `.tmp`, `.bak`, or `~` files
- No orphaned backup files
- No duplicate Python cache directories

---

## Recommendations

### Keep Clean Going Forward
1. **Archive, Don't Delete**: When creating new versions, move old versions to appropriate archive folders
2. **Use Dated Archives**: Create dated archive folders for major updates (e.g., `archive-backups-YYYY-MM-DD`)
3. **Clean Python Cache**: Add `__pycache__/` and `*.pyc` to `.gitignore`
4. **Consolidate Images**: Consider reviewing image files for duplicates (multiple verdant/church variants exist)

### Future Cleanup Targets
1. Review `/docs/images/` for duplicate placeholder images (Church2_PlaceH.png vs Church_PlaceH.png, verdant2 vs verdant)
2. Consolidate PDF exports in `/docs/pdfs/` - verify all are current
3. Review `/utilities/` Python scripts for any archived versions

---

## Impact

**Files Archived**: 15
**Files Deleted**: 3 (2 images + 1 cache directory)
**Disk Space Saved**: ~7.1 MB (deprecated images)
**Organization Improvement**: Significant - clean root directories, clear archive structure

Repository is now well-organized with clear separation between:
- **Active Content**: Current rules, lore, and balance documents
- **Historical Content**: Version iterations and audit reports properly archived
- **Reference Materials**: Organized in `/docs/reference/`
- **Development Tools**: Consolidated in `/utilities/`, `/simulation/`, `/tools/`
