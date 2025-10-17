# Penance Card System
**Version**: 3.2
**Last Updated**: October 17, 2025

Complete card database and interactive tools for Penance: Absolution Through Steel.

---

## 📚 What's Here

### Interactive HTML Tools

1. **[index.html](index.html)** - Card Database Browser
   - View all cards in the database
   - Filter by faction, type, cost
   - Search by name or keywords
   - Beautiful manuscript-style interface

2. **[deck-builder.html](deck-builder.html)** - Deck Builder
   - Build custom decks for any faction
   - Drag-and-drop interface
   - Deck validation (30-card limit)
   - Export deck lists

3. **[print-deck.html](print-deck.html)** - Print Sheets
   - Generate printable card sheets
   - Optimized for physical cards
   - Multiple cards per page
   - Print-and-play ready

### Data Files

- **[complete-card-data.json](complete-card-data.json)** (87KB) - Master card database
  - All 10 factions (107 faction cards)
  - 10 universal cards
  - Equipment, tactics, support units
  - JSON format for easy parsing

### Documentation

- **[anatomy.md](anatomy.md)** - Card anatomy and design
- **[masterlist.md](masterlist.md)** - Complete card list
- **[universal.md](universal.md)** - Universal core cards
- **[weapon-cards-detailed.md](weapon-cards-detailed.md)** - Weapon system details

---

## 🃏 Database Contents

### Version 3.2 (Current)

**Factions** (10 complete):
- ✅ Church of Absolution (10 cards)
- ✅ Crucible Packs (10 cards)
- ✅ Dwarven Forge-Guilds (10 cards)
- ✅ Elven Verdant Covenant (10 cards)
- ✅ Emergent Syndicate (10 cards)
- ✅ Nomad Collective (10 cards)
- ✅ The Ossuarium (6 cards)
- ✅ Soulstone Exchange (10 cards)
- ✅ Vestige Bloodlines (10 cards)
- ✅ The Wyrd Conclave (21 cards) ⭐ NEW

**Core Cards**:
- Universal Core: 10 cards (everyone has these)
- Equipment: 46+ items (weapons, shields, accessories)
- Tactics: 5 categories
- Support Units: 7 base units

**Total Cards**: ~170+ unique cards

---

## 🚀 Quick Start

### View Cards in Browser

1. Open `index.html` in your web browser
2. Browse cards by faction
3. Click cards to see details
4. Use filters to find specific cards

### Build a Deck

1. Open `deck-builder.html`
2. Select your faction
3. Add universal cards (10)
4. Choose 6 faction cards from your faction
5. Add equipment cards
6. Choose 2 tactics cards
7. Export your deck list

### Print Cards

1. Open `print-deck.html`
2. Select cards to print
3. Adjust layout (cards per page)
4. Print or save as PDF

---

## 🛠️ For Developers

### Database Structure

```json
{
  "_meta": {
    "version": "3.1",
    "lastUpdated": "2025-10-17",
    "description": "Complete Penance card database"
  },
  "universal": [ /* 10 core cards */ ],
  "church": [ /* 10 faction cards */ ],
  "crucible": [ /* 10 faction cards */ ],
  ...
  "equipment": [ /* Equipment items */ ],
  "tactics": { /* Tactics by faction */ }
}
```

### Card Object Schema

```json
{
  "id": "card-id",
  "name": "Card Name",
  "cardType": "core|faction|equipment|tactic",
  "type": "attack|defense|movement|utility",
  "cost": 2,  // SP cost (or special cost string)
  "range": "4 hexes",
  "effect": "Card effect text",
  "keywords": ["keyword1", "keyword2"],
  "lore": "Flavor text",
  "cardCount": 1  // How many in deck
}
```

### Rebuilding the Database

If faction cards are updated in `docs/factions/*/deck-equipment-system.md`:

```bash
# Extract new cards
python3 utilities/extract-all-faction-cards.py

# Merge into database
python3 utilities/merge-faction-cards.py

# Validate
python3 utilities/validate-card-database.py
```

---

## 📖 Usage Examples

### Example Deck (Church of Absolution)

**Universal Core** (10 cards - mandatory):
- Desperate Lunge, Warden's Pivot, Ironstrider's Rush, etc.

**Faction Cards** (choose 6 from 10):
1. Blood Offering (self-harm buff)
2. Martyrdom Protocol (protect ally)
3. Righteous Fury (vengeance scaling)
4. Consecrated Ground (healing zone)
5. Last Rites (death trigger)
6. Righteous Wrath (auto-hit)

**Equipment** (variable 10-20 cards):
- Primary Weapon: Penitent Blades (12 cards)
- Secondary: Buckler Shield (6 cards)

**Tactics** (choose 2 from 5):
- Divine Guidance
- Martyrdom's Certainty

**Total Deck**: 30-36 cards (depends on equipment)

---

## 🔧 Maintenance

### Adding New Cards

1. Add cards to faction's `deck-equipment-system.md` file
2. Run extraction script: `python3 utilities/extract-all-faction-cards.py`
3. Merge: `python3 utilities/merge-faction-cards.py`
4. Test web interfaces

### Updating Existing Cards

1. Edit `complete-card-data.json` directly, OR
2. Edit source `deck-equipment-system.md` and re-extract

### Version History

- **v3.1** (Oct 17, 2025) - Added Crucible, Emergent, Exchange, Vestige Bloodlines (9 factions total)
- **v3.0** (Oct 14, 2025) - Database restructure, added cardType field
- **v2.0** (Oct 11, 2025) - Equipment system overhaul
- **v1.0** (Oct 9, 2025) - Initial card database (4 factions)

---

## 📝 Notes

### Known Issues
- Ossuarium only has 6 faction cards (design decision - compensated by lifesteal)
- Some special costs (Forge tokens, Credits) stored as strings, not integers
- Equipment cards have nested structure (item → cards array)

### Future Enhancements
- [ ] Card images/illustrations
- [ ] Tabletop Simulator integration
- [ ] Deck validation rules (check slots, equipment limits)
- [ ] Printable PDF generator (automated)
- [ ] Mobile-responsive deck builder

---

## 🆘 Troubleshooting

**Cards not loading in browser?**
- Check browser console for errors
- Ensure `complete-card-data.json` is valid JSON
- Try hard refresh (Ctrl+F5)

**Deck builder not working?**
- Ensure JavaScript is enabled
- Check for JSON syntax errors
- Verify database has all factions

**Print layout broken?**
- Adjust print margins in browser
- Try "Print to PDF" instead of physical printer
- Check page orientation (landscape vs portrait)

---

## 📚 Related Documentation

- [Faction Index](../factions/index.md) - Complete faction documentation
- [Deck Construction Rules](../rules/deck-construction.md) - Deck building rules
- [Equipment Pool](../reference/equipment-pool-complete.md) - All equipment items
- [Card Template Specification](../reference/card-template-specification.md) - Design specs

---

**Maintained by**: Penance Development Team
**Repository**: [github.com/KeeberGoblin/penance](https://github.com/KeeberGoblin/penance)
**License**: See repository for details
