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
- **[CONTRADICTION-AUDIT-2025-10-13.md](CONTRADICTION-AUDIT-2025-10-13.md)** - Latest contradiction audit
  - Fixed "Resonance Engine" → "The Engine" naming inconsistency (43+ instances across 23 files)
  - Verified faction naming consistency
  - Verified equipment system consistency

- **[REPOSITORY-AUDIT-2025-10-13.md](REPOSITORY-AUDIT-2025-10-13.md)** - Repository structure audit

- **[COMPREHENSIVE-CONTRADICTION-AUDIT.md](COMPREHENSIVE-CONTRADICTION-AUDIT.md)** - Earlier comprehensive audit

- **[AUDIT-REPORT.md](AUDIT-REPORT.md)** - General audit report

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
