# Utilities Folder

This folder contains AI assistant context documents, audit reports, and diagnostic files used for repository maintenance and development.

---

## Contents

### AI Assistant Context
- **[CLAUDE.md](CLAUDE.md)** - Comprehensive context document for AI assistants working on Penance
  - Contains project overview, system mechanics, lore, faction details, and user preferences
  - Updated regularly with new content and design changes
  - Essential reading for any AI assistant starting work on the project

### Change History
- **[CHANGELOG.md](CHANGELOG.md)** - Project change history and version log
  - Documents major system changes, additions, and fixes
  - Organized by date and version

### Python Tools
- **[rebuild-card-database-v3.py](rebuild-card-database-v3.py)** - Card database generation script
  - Rebuilds card index from source markdown files
  - Used for maintaining card catalog consistency

### Archived Audits
All completed audit reports have been moved to **[archived-audits/](archived-audits/)** for historical reference:
- audit_1030_1016 - October 16 comprehensive audit
- AUDIT-2025-10-15.md - October 15 repository audit
- BALANCE-ANALYSIS-2025-10-16.md - Balance analysis report
- BALANCE-CHANGES-APPLIED-2025-10-16.md - Balance change implementation log
- COMPREHENSIVE-V3-AUDIT-2025-10-14.md - v3.0 integration audit
- HTML-AUDIT-2025-10-16.md - HTML codex page audit
- HTML-RENOVATION-SUMMARY.md - HTML renovation summary
- Implementation-todo.md - Completed implementation checklist

These files remain available for historical tracking but are no longer actively referenced.

---

## Purpose

These files serve several purposes:

1. **AI Context** - Help AI assistants understand the project quickly and accurately
2. **Quality Assurance** - Track contradictions, inconsistencies, and technical debt
3. **Documentation** - Record major changes and design decisions
4. **Maintenance** - Enable systematic repository cleanup and consistency checks

---

## For Developers

### When to Update CLAUDE.md
- After major system changes (e.g., equipment system overhaul)
- When adding new factions or mechanics
- When correcting naming conventions
- After significant lore additions

### When to Create Audit Reports
- Before major releases or playtests
- After large refactors or system changes
- When users report inconsistencies
- Quarterly maintenance cycles

### Audit Checklist
When creating new audit reports, check for:
- [ ] Naming convention consistency (Engine, faction names)
- [ ] System version consistency (equipment, deck construction)
- [ ] Cross-references between documents
- [ ] Deprecated terminology in active docs
- [ ] Broken links in codex/docs
- [ ] README accuracy

---

## File Maintenance

### Active Files (Update Regularly)
- `CLAUDE.md` - Keep synchronized with latest design changes
- `CHANGELOG.md` - Add entries for all significant changes
- `rebuild-card-database-v3.py` - Update when card structure changes
- `validate-card-database.py` - Run before major releases

### Archived Files
- **`archived-audits/2025-10-17-18/`** - 19 audit reports from Oct 17-18 (superseded by Oct 19 cleanup)
- **`archived-scripts/`** - 7 Python extraction scripts (work complete, data in main database)
- **`archived-effects/`** - Deprecated visual effects
- **`archived-audits/`** - Historical audit reports (pre-Oct 17)

### Recent Cleanup (October 19, 2025)
Moved ~381K of redundant files to archives:
- 19 completed audit reports (all issues addressed in Oct 19 cleanup)
- 7 one-time extraction scripts (Wyrd cards, equipment, faction cards)
- 2 extracted JSON files (data now in `docs/cards/complete-card-data.json`)

### Current Utilities Directory
```
utilities/
├── CLAUDE.md (26K) - AI assistant context (ACTIVE)
├── CHANGELOG.md (7K) - Project history (ACTIVE)
├── README.md (this file) - Utilities documentation (ACTIVE)
├── rebuild-card-database-v3.py (17K) - Card database tool (ACTIVE)
├── validate-card-database.py (5K) - Validation tool (ACTIVE)
├── archived-audits/ - Historical audit reports
│   ├── 2025-10-17-18/ - Recent audits (superseded)
│   └── [older audits]
├── archived-scripts/ - Completed extraction tools
└── archived-effects/ - Deprecated visual effects
```

---

**Last Updated**: October 19, 2025
