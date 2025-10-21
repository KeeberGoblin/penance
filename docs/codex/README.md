# Penance Codex - HTML Documentation

This directory contains HTML versions of the Penance game documentation, formatted with an illuminated manuscript aesthetic.

## Purpose

The HTML files in this directory provide a styled, browsable version of the game rules and lore:

- **Beautiful Presentation**: Styled with medieval manuscript aesthetics (gold borders, parchment backgrounds, ornamental breaks)
- **Easy Navigation**: Sidebar navigation system with iframe content loading
- **Printable Format**: Optimized for browser printing and PDF generation
- **Standalone Viewing**: Can be opened directly in a browser without a server

## Structure

```
docs/codex/
├── index.html              # Main entry point with navigation sidebar
├── manuscript-style.css    # Shared CSS for manuscript aesthetic
├── content-home.html       # Landing page
│
├── rules-*.html           # Combat system, turn structure, dice, etc.
├── faction-*.html         # Faction overviews and mechanics
├── scenario-*.html        # Playtest scenarios and boss fights
├── campaign-*.html        # Campaign systems (settlements, events, loot)
├── lore-*.html           # World lore, chronicle, NPCs
└── images/               # Shared images and assets
```

## Relationship to Markdown Files

**IMPORTANT**: These HTML files are **compiled/generated** from the markdown source files in other directories:

- Source: `docs/rules/*.md` → Compiled: `docs/codex/rules-*.html`
- Source: `docs/scenarios/*.md` → Compiled: `docs/codex/scenario-*.html`
- Source: `docs/campaigns/*.md` → Compiled: `docs/codex/campaign-*.html`
- Source: `docs/lore/*.md` → Compiled: `docs/codex/lore-*.html`

### Content Update Guidelines

1. **Always edit the markdown source files**, not the HTML directly
2. HTML files should be regenerated after markdown changes
3. If you edit HTML directly, changes will be lost on next build
4. For new content, create markdown first, then generate HTML

## Faction HTML Files

The faction HTML files use **current faction names** (as of October 2025):

| HTML File | Faction Name | Source Directory |
|-----------|--------------|------------------|
| `faction-church.html` | Church of Absolution | `docs/factions/church/` |
| `faction-dwarves.html` | Dwarven Forge-Guilds | `docs/factions/dwarves/` |
| `faction-undead.html` | The Ossuarium | `docs/factions/ossuarium/` |
| `faction-elves.html` | Elven Verdant Covenant | `docs/factions/elves/` |
| `faction-blighted.html` | Vestige Bloodlines | `docs/factions/vestige-bloodlines/` |
| `faction-chitinous.html` | Emergent Syndicate | `docs/factions/emergent/` |
| `faction-merchants.html` | The Exchange | `docs/factions/exchange/` |
| `faction-nomads.html` | Nomad Collective | `docs/factions/nomads/` |
| `faction-fae.html` | Wyrd Conclave | *(Not yet implemented)* |

**Note**: Some HTML **filenames** use older working names (undead, blighted, chitinous, merchants), but the **content inside** uses the current canonical faction names. This is a legacy naming convention and does not affect functionality.

## Build Process

*TO DO*: Document the build process for regenerating HTML from markdown.

If you're maintaining this repository:
- Consider adding a build script (e.g., `scripts/build-codex.sh`)
- Or use a static site generator (Pandoc, Jekyll, etc.)
- Add `.gitignore` entries if HTML is fully auto-generated

## Viewing the Codex

To view the codex:

1. **Local viewing**: Open `docs/codex/index.html` in your browser
2. **Live server**: Use a local HTTP server for better navigation
   ```bash
   cd docs/codex
   python3 -m http.server 8000
   # Then open http://localhost:8000
   ```

## Contributing

When adding new content:

1. Write the markdown source in the appropriate directory
2. Generate the HTML version using the build process
3. Update the sidebar navigation in `index.html` if needed
4. Test that links work and styling renders correctly

---

**Last Updated**: October 17, 2025
**Maintained by**: Penance Development Team
