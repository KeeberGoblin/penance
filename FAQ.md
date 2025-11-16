# Frequently Asked Questions (FAQ)

## General Questions

### What is Penance: Absolution Through Steel?

Penance is a tactical hex-based card game set in a grimdark medieval fantasy world. Players pilot massive war machines called Caskets in brutal combat, using cards to represent attacks, defenses, and maneuvers.

### Is this a physical card game or digital?

Penance is designed as a **tabletop game** with printable components. The repository contains:
- Complete rules and lore
- Card database with 278 cards
- Interactive web tools for deck building
- Printable card sheets for physical play
- Tabletop Simulator integration

### Is Penance free to play?

Yes! Penance is licensed under **CC BY-NC-SA 4.0**, meaning you can:
- ✅ Download and play for free
- ✅ Print cards for personal use
- ✅ Modify and remix content
- ❌ Sell or use commercially without permission

---

## Getting Started

### How do I start playing?

1. **Read the rules:** Start with [QUICKSTART.md](/QUICKSTART.md)
2. **Choose a faction:** Review [faction summaries](README.md#playable-factions)
3. **Get cards:** Use the [Deck Builder](/docs/cards/deck-builder.html) or pre-built decks in [playtest-kit](/playtest-kit/)
4. **Try a scenario:** Play [Scenario 01: Proving Grounds](/docs/scenarios/01-proving-grounds.md)

### What do I need to play?

**Minimum:**
- 2 players
- 1 deck per player (26-50 cards)
- Hex grid or map (pencil and paper works)
- Dice: 6d6 (attack) and 3d6 (defense)
- Tokens for tracking HP, SP, heat

**Optional:**
- Miniatures for Caskets
- Terrain pieces
- Printed reference sheets

### Which faction should I play first?

**For beginners:**
- **Church:** Straightforward offense, good healing
- **Dwarves:** Tanky and forgiving, armor-focused
- **Nomads:** Mobile and flexible

**Avoid as first faction:**
- **Emergent Syndicate:** Complex resource management
- **Wyrd-Conclave:** Requires understanding Taint mechanics

---

## Rules & Gameplay

### How does the deck-as-HP system work?

Your deck is your health. When you take damage:
1. Discard cards equal to damage taken
2. Discarded cards go to your graveyard
3. When your deck + hand is empty, you're defeated

This creates tension as you burn through powerful cards to survive.

### What happens when I run out of cards?

If your deck is empty at the start of your turn, **you lose**. Plan carefully!

### Can I mix factions in my deck?

Sort of:
- Your deck must have **10 Universal Core cards** (same for everyone)
- **6 Faction Core cards** from one faction (defines your Casket)
- Remaining slots can be **Equipment** (faction-neutral)

You cannot mix faction-specific cards from different factions.

### How does component damage work?

Cards can be **DAMAGED** during play. When you draw a DAMAGED card:
- It goes **directly to your graveyard** (not your hand)
- This represents permanent injuries to your Casket

Think of it like Kingdom Death: Monster's injury system.

---

## Webtools & Digital

### Where can I view all cards?

Use the [Interactive Card Browser](/docs/cards/index.html). Features:
- Search by name, type, or effect
- Filter by faction or cost
- Detailed card view with stats

### How do I build a deck online?

Use the [Deck Builder](/docs/cards/deck-builder.html). It validates deck construction rules and lets you save/load decks as JSON files.

### Can I play on Tabletop Simulator?

Yes! See [TTS-IMPORT-GUIDE.md](/tools/TTS-IMPORT-GUIDE.md) for instructions on importing cards.

### The web tools aren't loading. What's wrong?

Common issues:
1. **CORS errors:** Use a local web server instead of opening files directly
   ```bash
   cd docs/cards
   python3 -m http.server 8000
   # Visit http://localhost:8000
   ```
2. **Missing card data:** Ensure `complete-card-data.json` is in the same directory
3. **Browser compatibility:** Use a modern browser (Chrome, Firefox, Edge)

---

## Development & Contributing

### Can I contribute to the project?

Absolutely! See [CONTRIBUTING.md](/CONTRIBUTING.md) for guidelines. We welcome:
- Playtesting feedback
- Card balance suggestions
- Lore contributions
- Bug fixes
- New features

### How do I report a bug?

1. Check if it's already reported in [Issues](https://github.com/KeeberGoblin/penance/issues)
2. If not, open a new issue with the **Bug** template
3. Include:
   - What you expected
   - What actually happened
   - Steps to reproduce

### How do I suggest a new card or mechanic?

Open an issue with the **Feature Request** template and include:
- Card name, cost, and effect
- Faction it belongs to
- Why it's needed (fills a gap, creates synergy, etc.)
- Balance considerations

### Where can I discuss the game?

- **GitHub Issues:** For bugs and features
- **GitHub Discussions:** For general talk (if enabled)
- **Pull Requests:** For proposing specific changes

---

## Balance & Design

### Is the game balanced?

The game undergoes continuous playtesting. Current balance status (v6.0):
- **7/10 factions** have win rates between 44-58% (acceptable)
- **3 factions** need adjustment (Elves, Crucible, Emergent)

See [BALANCE-FINAL-V5.29.md](/docs/BALANCE-FINAL-V5.29.md) for detailed analysis.

### Why is [faction] so weak/strong?

Balance is iterative. If you've playtested and found issues:
1. Provide **specific examples** (not just "feels weak")
2. Include **battle reports** with card usage
3. Suggest **numerical adjustments** (e.g., "increase damage from 3 to 4")

See the combat simulator in `/simulation/` to test changes statistically.

### Can I create my own faction?

Yes! Follow the structure in `/docs/factions/` and:
- Create 6 unique Faction Core cards
- Design 3-4 Support Units
- Write lore and faction identity
- Submit via Pull Request for review

---

## Lore & Setting

### What is the Sundering?

The apocalyptic event (Year 0) when the Theslar Engine detonated, reshaping reality and creating the current world.

### What are Caskets?

Massive war machines piloted by humans. They're powered by Soulstones (crystallized human souls) and Neural Thread interfaces that link pilot to machine.

### What's the deal with Taint?

Taint represents corruption from the Theslar Engine's remnants. Some factions (Wyrd-Conclave, Elves) exploit it for power, but it costs sanity.

### Where can I read more lore?

- [World Overview](/docs/lore/world-overview.md)
- [Chronicle](/docs/lore/chronicle.md) - 437-year timeline
- [Cosmology](/docs/lore/cosmology-and-origins.md)
- [Interactive Codex](/docs/codex/index.html)

---

## Technical

### What version of the game is this?

Current version: **v6.0** (Soul Shard Update - November 2025)

Major changes in v6.0:
- Replaced lifesteal with Soul Shard economy
- Adjusted Ossuarium mechanics
- Balance adjustments across factions

### Where's the changelog?

See [CHANGELOG.md](/utilities/CHANGELOG.md) for version history.

### Can I use this project's code?

Yes! The code is under CC BY-NC-SA 4.0. You can:
- Fork and modify
- Use for your own projects (non-commercial)
- Learn from the implementation

Just attribute the original project.

---

## Troubleshooting

### The card database says "Error loading cards"

Check:
1. File path is correct (`complete-card-data.json` in same folder)
2. JSON is valid (use a validator like jsonlint.com)
3. No CORS errors (serve via HTTP, not file://)

### My custom deck won't validate

Common errors:
- Missing 10 Universal Core cards
- Missing 6 Faction Core cards
- Too many/few total cards (must be 26-50)
- Mixing faction-specific cards from different factions

### Dice probabilities seem off

The game uses **2d6 for attacks** (7 is most likely) and **1d6 for defense** (3-4 most common). This creates:
- ~58% hit rate on target 7
- ~42% chance to roll 3-4 defense

If it feels swingy, that's intentional. Grimdark games punish bad luck.

---

## Still have questions?

- **Open an issue** with the "Question" label
- **Check existing issues** - someone may have asked already
- **Read the docs** - comprehensive guides in `/docs/`

---

**Last Updated:** November 2025
