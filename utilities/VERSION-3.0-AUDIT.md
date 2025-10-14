# Version 3.0 System Audit
## Penance: Absolution Through Steel

**Date**: October 14, 2025
**Auditor**: Claude
**Purpose**: Identify all files needing updates for Version 3.0 mechanics

---

## What Changed in Version 3.0

### Three New Mechanics Systems

1. **Dice Pool Advantage/Disadvantage** (Trench Crusade-inspired)
   - File: `docs/rules/dice-pool-advantage.md`
   - Replaces static to-hit modifiers with roll-more-dice system
   - Affects: Combat, range/LOS, quick reference

2. **Taint Exploitation** (Trench Crusade Blood Marker-inspired)
   - File: `docs/rules/taint-exploitation.md`
   - Makes Taint a tactical resource (offensive + defensive uses)
   - Affects: Combat, factions, campaign rules

3. **Pilot Grit System** (Campaign progression)
   - File: `docs/campaigns/pilot-grit-system.md`
   - Pilot stat that grows with survival, resists Wound cards
   - Affects: Pilot progression, faction balance, campaign

---

## Files Requiring Updates

### HIGH PRIORITY (Core Rules)

**1. `/docs/rules/combat-system.md`**
- Status: Version 2.0 (October 10, 2025)
- Changes Needed:
  - Add reference to Dice Pool Advantage in Attack Resolution section
  - Add reference to Taint Exploitation in damage effects
  - Update "To-Hit" section to mention optional Dice Pool system
  - Add version note: "See dice-pool-advantage.md for optional modifier system"
- Action: UPDATE with 3.0 references

**2. `/docs/rules/turn-structure.md`**
- Status: Version 2.0 (October 10, 2025)
- Changes Needed:
  - Add Taint Marker tracking to Refresh Phase
  - Add Grit Check procedure to FAQ/Special Rules section
  - Reference Taint Exploitation as optional advanced rule
- Action: UPDATE with 3.0 references

**3. `/docs/rules/quick-reference.md`**
- Status: No version (October 10, 2025)
- Changes Needed:
  - Add Dice Pool Advantage quick table
  - Add Taint Exploitation costs table
  - Add Grit Check results table
  - Mark as "v3.0 Optional Rules" section
- Action: UPDATE with 3.0 optional rules section

**4. `/docs/rules/range-and-los.md`**
- Status: Version 2.0 (October 10, 2025)
- Changes Needed:
  - Update to-hit modifier sections to reference Dice Pool Advantage
  - Add note: "Using Dice Pool system? See dice-pool-advantage.md"
  - Convert static modifiers to Advantage/Disadvantage equivalents
- Action: UPDATE with 3.0 references

**5. `/docs/rules/dice-reference.md`**
- Status: Version 2.0 (October 10, 2025)
- Changes Needed:
  - Add Dice Pool Advantage section
  - Explain rolling 3d6 or 4d6 variants
  - Add probability tables for Advantage/Disadvantage
- Action: UPDATE with 3.0 dice mechanics

**6. `/docs/rules/index.md`**
- Status: No version
- Changes Needed:
  - Add links to three new 3.0 mechanics files
  - Add "Version 3.0 Optional Rules" section
  - Update Key Concepts to mention Dice Pool, Taint, Grit
- Action: UPDATE with 3.0 navigation

---

### MEDIUM PRIORITY (Campaign Rules)

**7. `/docs/campaigns/pilot-progression.md`**
- Status: No version (October 10, 2025)
- Changes Needed:
  - Add reference to Pilot Grit system
  - Integrate Grit as part of pilot stat progression
  - Add Grit to pilot sheet template
- Action: UPDATE with Grit integration

**8. `/docs/campaigns/index.md`**
- Status: No version
- Changes Needed:
  - Add link to pilot-grit-system.md
  - Update campaign overview to mention Grit progression
- Action: UPDATE with 3.0 navigation

**9. `/docs/campaigns/leg-skimming.md`**
- Status: No version (October 10, 2025)
- Changes Needed:
  - Add note: Leg-Skimming grants +1 Grit (see pilot-grit-system.md)
  - Cross-reference with Grit system
- Action: UPDATE with Grit cross-reference

---

### LOW PRIORITY (Supplemental)

**10. `/docs/rules/deck-construction.md`**
- Status: Version 2.0 (October 10, 2025)
- Changes Needed: None (3.0 mechanics don't affect deck building)
- Action: LEAVE AS-IS (add version note only)

**11. `/docs/rules/terrain.md`**
- Status: No version (October 10, 2025)
- Changes Needed:
  - Update cover rules to reference Dice Pool Advantage
  - Add note: "Heavy cover grants Disadvantage (see dice-pool-advantage.md)"
- Action: UPDATE with 3.0 references

**12. `/docs/rules/support-units.md`**
- Status: No version (October 10, 2025)
- Changes Needed:
  - Add note: Support Units gain +1 Morale if commanded by Grit 2+ pilot
  - Cross-reference pilot-grit-system.md
- Action: UPDATE with Grit synergy

---

## Faction-Specific Files

### Faction Deck Files

**ALL FACTION DECKS** (church, dwarves, ossuarium, elves):
- Status: Version 2.0 (Equipment System)
- Changes Needed:
  - Add "Faction Interactions with Taint" section to each
  - Add "Faction Grit Modifiers" section to each
  - Church: +1 Starting Grit, embraces Taint
  - Dwarves: +1 Grit vs Severe, resists Taint
  - Ossuarium: Immune to Grit (uses Decay), thrives on Taint
  - Elves: -1 Grit always, vulnerable to Taint
- Action: UPDATE with faction 3.0 modifiers

Files to update:
- `/docs/factions/church/deck-equipment-system.md`
- `/docs/factions/dwarves/deck-equipment-system.md`
- `/docs/factions/ossuarium/deck-equipment-system.md`
- `/docs/factions/elves/deck-equipment-system.md`

---

## HTML/Wiki Files

**Codex Pages** (docs/wiki/*.html):
- Files affected: 30+ HTML pages
- Changes Needed:
  - Add navigation links to 3.0 mechanics (dice-pool, taint, grit)
  - Create 3 new HTML pages for new mechanics
  - Update faction pages with Taint/Grit modifiers
- Action: CREATE new pages + UPDATE navigation

Priority HTML files:
1. `/docs/wiki/rules-combat.html` - Add Dice Pool reference
2. `/docs/wiki/rules-turn-structure.html` - Add Taint/Grit references
3. `/docs/wiki/rules-quick-ref.html` - Add 3.0 optional rules table
4. `/docs/wiki/faction-church.html` - Add Grit +1, Taint synergy
5. `/docs/wiki/faction-dwarves.html` - Add Grit +1 vs Severe, Taint resist
6. `/docs/wiki/faction-undead.html` - Add Grit immune, Taint thrive
7. `/docs/wiki/faction-elves.html` - Add Grit -1, Taint vulnerable

New HTML pages needed:
- `/docs/wiki/rules-dice-pool.html`
- `/docs/wiki/rules-taint-exploitation.html`
- `/docs/wiki/campaign-pilot-grit.html`

---

## Files to Archive

### None (3.0 is additive, not replacement)

All Version 2.0 files remain valid. Version 3.0 mechanics are OPTIONAL enhancements.

**Approach**: Add "Optional v3.0 Rules" sections rather than replace v2.0 content.

---

## Main Website (docs/index.html)

**Changes Needed**:
- Add "Version 3.0 Update" announcement section
- Link to new mechanics in navigation
- Update "Recent Updates" section

---

## README.md

**Changes Needed**:
- Update version from 2.0 to 3.0
- Add bullet points for three new mechanics
- Update "Playtest Status" to "v3.0 Ready"

---

## Implementation Plan

### Phase 1: Core Rules Updates (1 hour)
1. Update combat-system.md with Dice Pool + Taint references
2. Update turn-structure.md with Taint + Grit references
3. Update quick-reference.md with 3.0 optional rules table
4. Update range-and-los.md with Dice Pool references
5. Update dice-reference.md with Advantage/Disadvantage mechanics
6. Update rules/index.md with 3.0 navigation

### Phase 2: Campaign Rules Updates (30 min)
7. Update pilot-progression.md with Grit integration
8. Update leg-skimming.md with Grit bonus
9. Update campaigns/index.md with Grit navigation
10. Update support-units.md with Grit synergy

### Phase 3: Faction Updates (30 min)
11. Update church/deck-equipment-system.md (Grit +1, Taint embrace)
12. Update dwarves/deck-equipment-system.md (Grit +1 Severe, Taint resist)
13. Update ossuarium/deck-equipment-system.md (Grit immune, Taint thrive)
14. Update elves/deck-equipment-system.md (Grit -1, Taint vulnerable)

### Phase 4: HTML/Wiki Updates (2 hours)
15. Create 3 new HTML pages for new mechanics
16. Update faction HTML pages with Taint/Grit modifiers
17. Update rules HTML pages with 3.0 references
18. Update navigation to link to new pages

### Phase 5: Top-Level Updates (15 min)
19. Update README.md to v3.0
20. Update docs/index.html with v3.0 announcement
21. Update CLAUDE.md with v3.0 system notes

---

## Total Estimated Time: 4-5 hours

---

## Priority Order

1. **Core Rules** (combat, turn, quick-ref, range) - CRITICAL
2. **Rules Index** (add navigation) - CRITICAL
3. **README** (announce v3.0) - HIGH
4. **Faction Files** (Taint/Grit modifiers) - HIGH
5. **Campaign Files** (Grit integration) - MEDIUM
6. **HTML/Wiki** (new pages + updates) - MEDIUM
7. **Main Website** (index.html announcement) - LOW

---

**END OF AUDIT**

---

*"Version 3.0: More dice. More tactics. More grit."*
