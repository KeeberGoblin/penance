# System Overhaul Summary
## Penance: Absolution Through Steel - Version 2.0

**Date**: October 11, 2025
**Status**: Equipment System Overhaul Complete

---

## Major Changes Implemented

### 1. Equipment Slot System (Replaces Fixed Decks)

**Old System**:
- Fixed 30-card decks
- 12 Primary Weapon cards (locked)
- 6 Secondary Equipment cards (choose 1 of 4 options)

**New System**:
- Variable deck size (25-50 cards depending on Casket class and loadout)
- Equipment cards add to deck based on item complexity
- Modular: Weapon + Shield/Offhand + Accessories (1-4 slots)

**Equipment Slots by Casket Class**:
| Casket | SP | Weapon | Shield/Offhand | Accessories | Total Equipment |
|--------|----|----|---|---|---|
| Scout | 6 | 1 | 1 | 1 | 8-12 cards |
| Assault | 5 | 1 | 1 | 2 | 12-18 cards |
| Heavy | 4 | 1 | 1 | 3 | 15-24 cards |
| Fortress | 3 | 1 (2-handed) | 1 | 4 | 18-30 cards |

---

### 2. Complete Equipment Pool (40+ Items)

**Created**: [equipment-pool-complete.md](docs/reference/equipment-pool-complete.md)

**Categories**:
- **Weapons**: 15+ weapons (3-9 cards each)
  - Light: Dagger (3), Pistol (3), Hand Axe (4)
  - Medium: Longsword (6), Spear (5), Mace (5), Crossbow (5)
  - Heavy: Greatsword (8), Warhammer (6), Halberd (7), Rifle (6)
  - Exotic: Chain Whip (6), Flail (5)

- **Shields/Offhand**: 6+ options (2-4 cards each)
  - Buckler Shield (2), Kite Shield (3), Tower Shield (4)
  - Dueling Dagger (2), Secondary weapons

- **Plating**: 4+ hull modifications (2-3 cards each)
  - Ablative (3), Spike (2), Reinforced (3), Stealth (3)

- **Sigils**: 12+ enchantments (2-4 cards each)
  - Universal: Repair (2), Heat Sink (2), Targeting (3)
  - Faction-Exclusive: 8 unique sigils (Church, Dwarves, Elves, Ossuarium, Wyrd Conclave, Horde, Nomads, Merchants)

---

### 3. Smelting & Salvage Economy

**Smelting**:
- Remove unwanted equipment from deck
- Gain Scrap: 1 Scrap per 2 cards smelted
- Example: Greatsword (8 cards) → Smelt → Gain 4 Scrap

**Salvage**:
- Loot enemy equipment: Roll 1d20, on 15+ recover 1 equipment
- Can use cross-faction gear (even if you can't craft it)
- Looted gear cannot be repaired/upgraded
- Can be smelted normally

---

### 4. Faction Name Updates

**Changed**:
- "Undead Court" / "Bone-Courts" → **The Ossuarium**
- "Twilight Courts" / "Fae Courts" → **The Wyrd Conclave**

**Files Updated**: 16 markdown files across docs/

---

### 5. Event Tables (Kingdom Death Style)

**Created**: [event-tables-kdm-style.md](docs/campaigns/event-tables-kdm-style.md)

**Departure Events** (2d6 - 66 outcomes):
- Roll 2d6, read individually (3+4 = "34" not "7")
- Doubles trigger catastrophic/legendary events:
  - 11: The Offering (sacrifice) or Hero's Welcome (blessing)
  - 22: The Betrayal (traitor revealed) or The Plague (disease)
  - 33: The Fracture (settlement attacked) or The Revelation (secrets)
  - 44: The Reckoning (debts) or consequences
  - 55: The Ascension (transcendence) or The Awakening (legendary)
  - 66: The End Times (catastrophe) or The Miracle (ultimate blessing)

**Arrival Events** (2d6 - 66 outcomes):
- Post-mission consequences
- Settlement growth, NPC encounters, rewards, disasters

---

### 6. SCP-Style Anomalous Events

**Created**: [anomalous-events-scp-style.md](docs/campaigns/anomalous-events-scp-style.md)

**Containment Breach Table** (1d20):
- Safe: Minor anomalies (The Weeping Casket, compass)
- Euclid: Moderate threats (Recursive Hallway, Doppelganger Soulstone)
- Keter: Major breaches (Consensus Engine, Hungry Workshop)
- Apollyon: Extinction-level (Retroactive Massacre, The Nobody)

**Artifact Discovery Table** (1d100):
- 01-20: Safe artifacts (useful, minor risks)
- 21-50: Euclid artifacts (powerful, significant risks)
- 51-80: Keter artifacts (extremely dangerous)
- 81-95: Apollyon artifacts (world-ending potential)
- 96-100: Thaumiel artifacts (reality-altering, double-edged)

**Anomalous Entities**:
- SCP-PE-088: The Mimic Casket
- SCP-PE-103: The Choir of Sibaria (singing calls pilots to Engine)
- SCP-PE-117: The Empty Ones (humanity-drained pilots)

---

### 7. Rebuilt Faction Decks

**Created**:
- [church/deck-equipment-system.md](docs/factions/church/deck-equipment-system.md)
- [dwarves/deck-equipment-system.md](docs/factions/dwarves/deck-equipment-system.md)

**Church of Absolution**:
- 6 Faction Core cards (Blood Offering, Martyrdom Protocol, Righteous Fury, Divine Judgment, Consecrated Ground, Last Rites)
- 4 sample builds (Aggressive Martyr, Defensive Support, Self-Harm Berserker, Ranged Martyrdom)
- Deck sizes: 26-48 cards depending on Casket and loadout
- Faction-exclusive: Martyr's Brand Sigil (3 cards)

**Dwarven Forge-Guilds**:
- 6 Faction Core cards (Crushing Blow, Forge Fury, Rune of Protection, Unbreakable, Earthshaker, Clan Vengeance)
- 4 sample builds (Immovable Wall, Armor-Piercing Assault, Artillery Platform, Berserker Engineer)
- Deck sizes: 30-50 cards (32-52 with Stone Endurance)
- Faction-exclusive: Forge-Rune Sigil (3 cards), War Pick (6 cards), Battle Axe (6 cards), Siege Cannon (7 cards)

---

## System Philosophy

### Design Goals Achieved

**Kingdom Death: Monster Inspiration**:
- Brutal event tables with permanent consequences
- Equipment crafting and salvage economy
- Permanent pilot scars and trauma
- No pure heroes or villains
- Death spiral mechanics

**GKR: Heavy Hitters Inspiration**:
- Deck-as-HP system
- SP economy (energy refresh)
- Fixed hand size (6 cards)
- Component damage tracking

**SCP Foundation Inspiration**:
- Anomalous artifact system
- Containment procedures
- Reality-bending phenomena
- Classification tiers (Safe/Euclid/Keter/Apollyon/Thaumiel)

---

## Deck Size Balance

### Example Deck Comparisons

**Light Striker (Scout)**:
- 10 Universal + 6 Faction + 8 Equipment (Dagger 3 + Buckler 2 + Sigil 3) + 2 Tactics
- **Total: 26 cards** (fast cycle, 6 SP per turn)

**Balanced Fighter (Assault)**:
- 10 Universal + 6 Faction + 14 Equipment (Longsword 6 + Kite Shield 3 + 2 Sigils 5) + 2 Tactics
- **Total: 32 cards** (balanced, 5 SP per turn)

**Heavy Tank (Heavy)**:
- 10 Universal + 6 Faction + 20 Equipment (Warhammer 6 + Tower Shield 4 + 3 Sigils 10) + 2 Tactics
- **Total: 38 cards** (slow but durable, 4 SP per turn)

**Ultra-Fortress (Fortress with Stone Endurance)**:
- 10 Universal + 6 Faction + 24 Equipment (Greatsword 8 + 4 Sigils 16) + 2 Tactics + 2 Stone Endurance
- **Total: 44 cards** (maximum tank, 3 SP per turn)

---

## Campaign Integration

### Mission 1 (Tutorial)
- Players start with basic equipment (Longsword + Buckler)
- Learn core mechanics (SP, Heat, deck-as-HP)
- Earn 4-6 Scrap from mission rewards

### Mission 5-10 (Mid-Campaign)
- Craft/loot faction-exclusive equipment
- Upgrade to Medium or Heavy Caskets (more accessory slots)
- Begin encountering event table consequences

### Mission 15+ (Late-Campaign)
- Stack multiple accessories (Heavy/Fortress have 3-4 slots)
- Acquire looted cross-faction gear
- Face Anomalous Events (SCP-style)
- Encounter Iconic NPCs (Signature Card opportunities)

---

## Replayability Factors

1. **Equipment Variety**: 40+ items with variable card counts = hundreds of deck combinations
2. **Event Tables**: 132 unique events (66 Departure + 66 Arrival) + 20 Anomalous
3. **Artifact Discovery**: 100 unique artifacts on 1d100 table
4. **NPC Encounters**: 5 Iconic NPCs with Signature Card rewards
5. **Faction Asymmetry**: Each faction has unique Core cards and exclusive equipment
6. **Pilot Scars**: 80+ permanent character traits
7. **Settlement Building**: 20+ buildings with different upgrade paths

---

## Next Steps

### Immediate (Completed)
- Equipment pool documented
- Event tables created
- Faction decks rebuilt
- SCP anomalies catalogued

### Short-Term (Next Session)
- Playtest new equipment system
- Balance equipment crafting costs
- Test event table frequency
- Verify deck size balance

### Long-Term (Future Development)
- Additional faction decks (Elves, Ossuarium, Wyrd Conclave, Horde, Nomads, Merchants)
- Campaign scenario chain
- Boss encounter AI decks
- Visual card templates
- Tabletop Simulator integration

---

## Files Created This Session

1. `docs/reference/equipment-pool-complete.md` (Complete equipment catalog)
2. `docs/campaigns/event-tables-kdm-style.md` (66+66 event tables)
3. `docs/campaigns/anomalous-events-scp-style.md` (SCP-style anomalies)
4. `docs/factions/church/deck-equipment-system.md` (Church v2.0)
5. `docs/factions/dwarves/deck-equipment-system.md` (Dwarves v2.0)
6. `SYSTEM-OVERHAUL-SUMMARY.md` (This document)

**Total New Content**: ~25,000 words

---

## Balance Considerations

### Potential Issues to Monitor

**Deck Size Variance**:
- Scout (26 cards) vs Fortress (44 cards) = 68% difference
- May create imbalance (fast cycle advantage vs durability)
- Solution: Test and adjust SP costs if needed

**Equipment Crafting Costs**:
- Basic weapons: 2-4 Scrap
- Advanced weapons: 5-6 Scrap
- Faction-exclusive: 5-6 Scrap
- May need adjustment based on Scrap generation rates

**Event Table Frequency**:
- Rolling events every mission may be exhausting
- Consider: Every other mission, or player-triggered
- Double rolls (11, 22, etc.) should remain rare

**Anomalous Event Balance**:
- SCP-style events are VERY punishing
- Recommend: 1 per 5-10 missions maximum
- GM discretion critical

---

## System Strengths

**Deep Customization**:
- Equipment slots allow personal expression
- Deck sizes reflect playstyle (fast aggro vs slow tank)
- Faction identity preserved through Core cards

**Narrative Emergence**:
- Event tables create unexpected stories
- Anomalous artifacts drive memorable moments
- NPC Signature Cards reward exploration

**Replayability**:
- Hundreds of equipment combinations
- Random events create unique campaigns
- Permanent scars make each pilot unique

---

**END OF DOCUMENT**

*"The system is complete. The tools are forged. The rules are written. Now comes the blood and iron."*
