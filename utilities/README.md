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

### Audit Reports
- **[COMPREHENSIVE-V3-AUDIT-2025-10-14.md](COMPREHENSIVE-V3-AUDIT-2025-10-14.md)** - Latest v3.0 integration audit
  - Analyzes v3.0 mechanics integration across 103 files
  - Identifies missing cross-references and integration gaps
  - Provides priority fix list and action plans

**Archived Audits** (see `/archive/utilities-archive/`):
- CONTRADICTION-AUDIT-2025-10-13.md - Engine naming fixes
- REPOSITORY-AUDIT-2025-10-13.md - Structure audit
- COMPREHENSIVE-CONTRADICTION-AUDIT.md - Earlier contradiction analysis
- AUDIT-REPORT.md - v2.0 repository audit
- VERSION-3.0-AUDIT.md - v3.0 planning (superseded by comprehensive)

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

### Historical Files (Keep for Reference)
- Audit reports - Archive but don't delete (useful for tracking change history)
- Old contradiction reports - Show evolution of consistency efforts

---

**Last Updated**: October 13, 2025
