# Penance: Absolution Through Steel - AI Coding Instructions

## Project Architecture

**Penance** is a tactical hex-based card game combining GKR: Heavy Hitters' deck-as-HP system with Kingdom Death: Monster's brutal progression. This is a **documentation-heavy project** with interactive HTML tools, not traditional software.

### Core Components
- **Variable deck system** (26-50 cards): `10 Universal + 6 Faction Core + X Equipment + 2 Tactics`
- **Deck-as-HP mechanic**: Damage = discard cards from top of deck, reshuffles add "Damage" cards (death spiral)
- **Component destruction**: Track damage by body part (Right Arm, Left Arm, etc.), 3 damage = destroyed
- **SP economy**: Turn-based Soul Points system (3-6 SP per turn depending on Casket class)

## Critical File Patterns

### Faction Structure (`docs/factions/`)
Each faction has standardized naming and structure:
- **Correct names**: Church of Absolution, Dwarven Forge-Guilds, The Ossuarium, Elven Verdant Covenant
- **Never use**: "Undead Court", "Bone-Courts", "Twilight Courts", "Fae Courts"
- **Equipment system files**: `{faction}/deck-equipment-system.md` (v2.0+ variable decks, NOT fixed 30-card)

### Dual Documentation System
1. **Markdown source** (`docs/`): Source of truth for rules and content
2. **HTML Codex** (`docs/codex/`): Interactive reference with iframe navigation and manuscript styling
3. **Main website** (`docs/index.html`): Timeline, faction overviews, download links

### Version System
- **v2.0 Base Rules**: Equipment system, variable decks (current standard)
- **v3.0 Optional Mechanics**: Dice Pool Advantage, Taint Exploitation, Pilot Grit (enhancements only)
- Always specify which version when referencing mechanics

## Development Workflow

### Card Database (`docs/cards/complete-card-data.json`)
- **Structure**: `universal`, `church`, `dwarves`, `ossuarium`, `elves`, `equipment`, `tactics`, `support_units`
- **Required fields**: `cardType` ("core", "faction", "equipment", "tactic"), `cardCount`, `cost`, `effect`
- **Update script**: `utilities/rebuild-card-database-v3.py` (maintain JSON structure)

### PDF Generation (`tools/generate-pdfs.py`)
- Uses WeasyPrint for professional styling
- Converts markdown to styled PDFs with headers/footers
- Manuscript aesthetic: Palatino fonts, aged paper colors, ornate borders

### Interactive Tools
- **Pilot Generator** (`docs/tools/pilot-generator.html`): JavaScript character creation using 5 random tables
- **Card Browser** (`docs/cards/index.html`): Searchable database with filters
- **Deck Builder** (`docs/cards/deck-builder.html`): Equipment selection interface

## Content Conventions

### Writing Style
- **No emoticons/emojis** (user explicitly dislikes them)
- **Grimdark medieval fantasy tone**: "Through steel, absolution" not "awesome mechanics!"
- **Specific equipment counts**: "Longsword (6 cards)" not just "Longsword"
- **Kingdom Death terminology**: Component Destruction, Event Tables, Settlement Phase

### Equipment References
When mentioning equipment, always include card count:
```markdown
- Dagger (3 cards)
- Tower Shield (4 cards)  
- Sigil of Warding (3 cards)
```

### Deck Formula Documentation
Always use current v2.0 formula:
```
Total Deck = 10 Universal + 6 Faction Core + X Equipment + 2 Tactics
Where X varies by equipment chosen (8-30 cards typical range)
```

## Integration Points

### HTML Codex System (`docs/codex/`)
- **Navigation**: iframe-based with `manuscript-style.css`
- **Cross-references**: Link between rules, factions, and campaign systems
- **Responsive design**: Mobile-friendly manuscript aesthetic
- **Color scheme**: `--black: #1a1410`, `--accent: #b8956a`, `--blood-red: #8b1a1a`

### Campaign Systems Integration
- **Pilot Generation**: 5 tables (Background, Traits, Motivation, Quirks, Appearance) = 320M combinations
- **Settlement Phase**: 6-step process (Return → Income → Event → Actions → Care → Preparation)
- **Enemy AI**: KDM-style "If-Then" behavior decks requiring no GM interpretation

### External Dependencies
- **Google Fonts**: Cinzel Decorative, Crimson Pro, Libre Baskerville (manuscript theme)
- **WeasyPrint**: PDF generation from HTML/CSS
- **GitHub Pages**: Static site hosting at `keebergoblin.github.io/penance/`

## Common Pitfalls

1. **Using deprecated fixed deck system** - Always reference variable deck sizes (26-50 cards)
2. **Wrong faction names** - Use "The Ossuarium" not "Undead Court"
3. **Missing card counts** - Equipment must specify number of cards it adds to deck
4. **Confusing "Codex" terminology** - User means `docs/codex/` HTML files, not general documentation
5. **Ignoring version context** - Specify whether discussing v2.0 base rules or v3.0 optional mechanics

## Testing and Validation

### Balance Validation
- **Church vs Dwarves**: Expected 55/45 Church favor (alpha strike vs attrition)
- **Equipment variance**: Ensure 26-card scout builds remain viable vs 38-card heavy builds
- **Component destruction**: Verify permanent consequences feel impactful but not game-ending

### Content Cross-Reference
- **Terminology consistency**: Use `utilities/CLAUDE.md` as authoritative source
- **Mechanical accuracy**: Equipment costs must match deck size constraints
- **Lore integration**: Ensure faction equipment matches thematic identity (Church self-harm, Dwarven armor-piercing, etc.)

When working on Penance, prioritize mechanical accuracy and consistency with the variable deck system over rapid feature addition.