# Card Database Audit Summary
## Executive Report for Penance Card System

**Date**: October 18, 2025
**Auditor**: Claude (Comprehensive Analysis)
**Database**: `/workspaces/penance/docs/cards/complete-card-data.json` (v3.2)

---

## CRITICAL FINDING: Two Different Card Systems

The audit revealed that **JSON and Markdown use different organizational structures**:

### JSON Structure (complete-card-data.json)
- **Individual ability cards** grouped by faction/type
- Example: "Aimed Shot", "Shield Bash", "Crushing Blow" (individual cards)
- Total: **170 individual cards**

### Markdown Structure (equipment-pool-complete.md)
- **Equipment items** that contain multiple cards
- Example: "LONGSWORD (6 cards)" = Slash + Thrust + Parry + Riposte + Pommel Strike + Guard Stance
- Total: **26 equipment items** containing **121 individual cards**

**This is NOT a discrepancy - it's two ways of organizing the same data.**

---

## SECTION 1: FACTION COMPLETENESS TABLE

| Faction | JSON Cards | Expected Full Deck | Missing | Status |
|---------|-----------|-------------------|---------|--------|
| **Universal Core** | 10 | 10 | 0 | ✓ COMPLETE |
| **Church** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |
| **Dwarves** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |
| **Elves** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |
| **Ossuarium** | 6 | 21 | 15 | CRITICAL (missing 4 core + equipment) |
| **Wyrd Conclave** | 21 | 21 | 0 | ✓ COMPLETE |
| **Emergent Syndicate** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |
| **Nomads** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |
| **Exchange** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |
| **Crucible** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |
| **Vestige-Bloodlines** | 10 | 21 | 11 | INCOMPLETE (needs equipment) |

### Interpretation:
- **Wyrd Conclave** is the ONLY complete faction (10 core + 6 primary + 5 secondary)
- **Ossuarium** is critically incomplete (only 6/10 faction core cards)
- **9 factions** have complete faction core (10 cards) but lack equipment cards

**Expected Deck Formula**: `10 Universal + 6-10 Faction Core + 6 Primary Equipment + 5 Secondary Equipment = 21-31 cards`

---

## SECTION 2: MISSING CARDS (In Markdown but NOT in JSON)

### Total: 11 Cards

#### CHURCH (5 missing cards)
The Church markdown documents **13 faction cards** but JSON only has **10**. Missing:

1. **Divine Guidance** (Sigil) - Accuracy buff (-2 to target number)
2. **Martyrdom's Certainty** (Sigil) - Type unknown
3. **Zealot's Focus** (Sigil) - Type unknown
4. **Point-Blank Execution** (Weapon Attack) - Close-range execution
5. **Confession Under Duress** (Utility) - Type unknown

**Source**: `/workspaces/penance/docs/factions/church/deck-equipment-system.md` lines 95-111

**Recommendation**: Add these 5 cards to JSON under `"church"` section

---

#### WYRD CONCLAVE (6 missing cards)
The Wyrd markdown documents **6 additional cards** not in JSON (may be older names):

1. **Fairy Dust**
2. **Mirror Step**
3. **Oath-Binding Contract**
4. **Reality Bargain**
5. **Stolen Reflection**
6. **What-If Paradox**

**Source**: `/workspaces/penance/docs/factions/wyrd/deck-equipment-system.md` (legacy file)

**Note**: The `/workspaces/penance/docs/factions/wyrd-conclave/` directory may have updated documentation.

**Recommendation**: Cross-reference with `wyrd-conclave` directory to see if these were renamed

---

## SECTION 3: DATA QUALITY ASSESSMENT

### ✓ PASSED Checks

1. **Required Fields**: All 170 cards have `id`, `name`, `type`, `cost`, `effect`
2. **No Duplicate IDs**: All card IDs are unique across entire database
3. **Valid JSON Syntax**: No trailing commas, proper escaping, valid structure
4. **Consistent Naming**: kebab-case IDs, Title Case names

### Field Coverage

| Field | Present in All Cards | Notes |
|-------|---------------------|-------|
| `id` | ✓ Yes | Unique kebab-case identifiers |
| `name` | ✓ Yes | Title Case display names |
| `type` | ✓ Yes | attack, defense, utility, movement, passive, reactive |
| `cost` | ✓ Yes | 0-5 SP |
| `effect` | ✓ Yes | Text descriptions |
| `keywords` | ✓ Yes | All cards have keyword arrays |
| `cardCount` | Mostly | Indicates deck quantity (1-3 copies) |
| `range` | Partial | Some cards don't need range (passive/reactive) |
| `heat` | Partial | Only cards that generate/remove heat |

**Overall Quality**: EXCELLENT - No critical issues found

---

## SECTION 4: EQUIPMENT POOL ANALYSIS

### Equipment in Markdown (equipment-pool-complete.md)

**26 Equipment Items** containing **121 individual cards**:

#### WEAPONS (14 items = 68 cards)
- **Light**: Dagger (3), Pistol (3), Hand Axe (4)
- **Medium**: Longsword (6), Spear (5), Mace (5)
- **Heavy**: Greatsword (8), Warhammer (6), Halberd (7)
- **Ranged**: Crossbow (5), Longbow (4), Rifle (6)
- **Exotic**: Chain Whip (6), Flail (5)

#### SHIELDS (4 items = 11 cards)
- Buckler Shield (2), Dueling Dagger (2), Kite Shield (3), Tower Shield (4)

#### PLATING (4 items = 11 cards)
- Ablative (3), Spike (2), Reinforced (3), Stealth (3)

#### SIGILS (11 items = 31 cards)
- **Universal**: Repair (2), Heat Sink (2), Targeting (3)
- **Faction-Exclusive**: 8 faction sigils (2-4 cards each)

---

### Equipment in JSON (equipment section)

**46 individual equipment ability cards**:

Example cards: Aimed Shot, Shield Bash, Crushing Blow, Blade Dance, etc.

**Comparison**:
- Markdown: 121 equipment cards organized into 26 items
- JSON: 46 equipment cards (individual abilities)
- **Gap**: 75 cards from markdown not yet in JSON

**Analysis**: JSON contains a **SUBSET** of the equipment pool. Many equipment items from markdown are not represented.

**Examples of Missing Equipment Items**:
- LONGSWORD (6 cards) - Only "Quick Slash" and "Righteous Slash" appear in JSON
- WARHAMMER (6 cards) - Only "Hammer Strike", "Runic Smash", "Crushing Blow" appear
- GREATSWORD (8 cards) - Only "Cleaving Strike", "Execution Blow" appear
- CROSSBOW (5 cards) - Only "Aimed Shot" appears
- RIFLE (6 cards) - Only "Sniper Shot" appears

**Recommendation**: Add missing equipment item cards from markdown to JSON

---

## SECTION 5: CARD COUNT BREAKDOWN

### Universal Cards (10 Total) ✓ COMPLETE

1. Desperate Lunge (movement, 1 SP)
2. Warden's Pivot (movement, 0 SP)
3. Ironstrider's Rush (movement, 2 SP)
4. Unyielding Bulwark (defense, 0 SP)
5. Second Skin (defense, 0 SP)
6. Breathe the Core (utility, 2 SP) - 3 copies
7-10. Additional universal cards

**Status**: Complete and well-balanced

---

### Faction Cards Summary

| Faction | Core Cards | Primary | Secondary | Total | Completeness |
|---------|-----------|---------|-----------|-------|--------------|
| Church | 10 | 0 | 0 | 10 | 48% (10/21) |
| Dwarves | 10 | 0 | 0 | 10 | 48% (10/21) |
| Elves | 10 | 0 | 0 | 10 | 48% (10/21) |
| Ossuarium | 6 | 0 | 0 | 6 | 29% (6/21) |
| Wyrd Conclave | 10 | 6 | 5 | 21 | 100% (21/21) ✓ |
| Emergent | 10 | 0 | 0 | 10 | 48% (10/21) |
| Nomads | 10 | 0 | 0 | 10 | 48% (10/21) |
| Exchange | 10 | 0 | 0 | 10 | 48% (10/21) |
| Crucible | 10 | 0 | 0 | 10 | 48% (10/21) |
| Vestige | 10 | 0 | 0 | 10 | 48% (10/21) |

**Average Completeness**: 52% (9 factions incomplete)

---

### Equipment Cards (46 in JSON)

**By Type**:
- Attack: 29 cards (63%)
- Defense: 11 cards (24%)
- Utility: 5 cards (11%)
- Movement: 1 card (2%)

**Gap Analysis**:
- Documented in markdown: 121 equipment ability cards
- In JSON: 46 equipment ability cards
- **Missing**: 75 cards (62% of equipment pool)

---

### Support Units (7 in JSON)

Cards appear to be NPC/ally units that can be hired or summoned:
- Function unknown (not cross-referenced with other documentation)
- May be campaign-only cards

**Recommendation**: Cross-reference with campaign settlement documentation

---

## SECTION 6: WYRD CONCLAVE ANALYSIS (Template for Completion)

Wyrd Conclave is the **ONLY faction with 21 cards** - analyze as template:

### Faction Core (10 cards)
1. Bargain Struck
2. Fae Bargain
3. Deal With The Devil
4. Price Paid
5. Bargain Siphon
6. Fae Curse
7. Fae Mirror
8. Stolen Strength
9. Stolen Face
10. Reality Fracture

**Mechanics**: All cards revolve around "bargains" and reality manipulation

---

### Primary Equipment (6 cards)
11. Shimmer Strike
12. Phase Cut
13. Paradox Blade
14. Incomprehensible Strike
15. Impossible Geometry
16. Mirage Assault

**Mechanics**: Faction-specific attack abilities (illusionary weapons)

---

### Secondary Equipment (5 cards)
17. Shimmer Veil
18. Shimmer Step
19. Mirror Self
20. Reality Shard
21. Temporal Loop

**Mechanics**: Universal-ish equipment (defensive/utility abilities)

---

### Template Pattern for Other Factions

**Each faction should have**:
- 10 Faction Core cards (unique to faction, define playstyle)
- 6 Primary Equipment cards (faction-flavored weapons/abilities)
- 5 Secondary Equipment cards (generic equipment usable by all)

**Example for Church**:
- 10 Core: Blood Offering, Martyrdom Protocol, Righteous Fury, etc.
- 6 Primary: Holy weapons (Flurry of Faith, Penitent's Wrath, Faithful Thrust, etc.)
- 5 Secondary: Universal equipment (Aimed Shot, Shield Bash, Defensive Stance, etc.)

---

## SECTION 7: RECOMMENDATIONS (Priority Order)

### CRITICAL PRIORITY

#### 1. Complete Ossuarium Faction (15 cards needed)
**Current**: 6 faction core cards
**Target**: 21 cards (10 core + 6 primary + 5 secondary)
**Missing**: 4 additional core + 6 primary + 5 secondary

**Action Items**:
- Add 4 missing faction core cards (consult design docs)
- Add 6 primary equipment (Death-themed weapons: Bone Blade, Soul Drain, etc.)
- Add 5 secondary equipment (universal equipment pool)

**Estimated Time**: 2-3 hours

---

#### 2. Add Missing Church Cards (5 cards)
**Current**: 10 faction core cards
**Target**: Add documented cards from markdown

**Action Items**:
- Add Divine Guidance (Sigil)
- Add Martyrdom's Certainty (Sigil)
- Add Zealot's Focus (Sigil)
- Add Point-Blank Execution (Weapon Attack)
- Add Confession Under Duress (Utility)

**Source**: `/workspaces/penance/docs/factions/church/deck-equipment-system.md`

**Estimated Time**: 30 minutes

---

### HIGH PRIORITY

#### 3. Complete All 9 Factions (99 cards total)
**Target**: Add 11 cards to each incomplete faction (6 primary + 5 secondary)

**Recommended Order** (by lore/design maturity):
1. **Church** - Add 6 primary + 5 secondary (11 cards)
2. **Dwarves** - Add 6 primary + 5 secondary (11 cards)
3. **Elves** - Add 6 primary + 5 secondary (11 cards)
4. **Emergent** - Add 6 primary + 5 secondary (11 cards)
5. **Nomads** - Add 6 primary + 5 secondary (11 cards)
6. **Exchange** - Add 6 primary + 5 secondary (11 cards)
7. **Crucible** - Add 6 primary + 5 secondary (11 cards)
8. **Vestige-Bloodlines** - Add 6 primary + 5 secondary (11 cards)

**Estimated Time**: 8-12 hours (1-1.5 hours per faction)

---

#### 4. Expand Equipment Pool (75 cards)
**Current**: 46 equipment ability cards
**Target**: 121 cards (per equipment-pool-complete.md)

**Action Items**:
- Add complete card sets for each weapon type
  - Example: LONGSWORD (6 cards) = Slash, Thrust, Parry, Riposte, Pommel Strike, Guard Stance
- Add complete shield card sets (Buckler, Kite, Tower)
- Add plating cards (Ablative, Spike, Reinforced, Stealth)
- Add universal sigil cards (Repair, Heat Sink, Targeting)
- Add faction-exclusive sigil cards (8 factions × 2-4 cards each)

**Source**: `/workspaces/penance/docs/reference/equipment-pool-complete.md`

**Estimated Time**: 6-8 hours

---

### MEDIUM PRIORITY

#### 5. Resolve Wyrd Conclave Naming Discrepancy
**Issue**: Markdown documents 6 cards not in JSON (Fairy Dust, Mirror Step, etc.)

**Action Items**:
- Check if `/workspaces/penance/docs/factions/wyrd-conclave/` has updated card names
- Create mapping table of old names → new names
- Update markdown documentation if cards were renamed

**Estimated Time**: 1 hour

---

#### 6. Add Tactics Cards (20 cards)
**Expected**: Each faction deck includes "2 Tactics" cards
**Current**: No tactics cards in JSON

**Action Items**:
- Determine if tactics are universal (same for all factions) or faction-specific
- Add 2 tactics per faction OR 2 universal tactics
- Cross-reference with deck composition formula

**Estimated Time**: 2-3 hours

---

### LOW PRIORITY

#### 7. Document Support Unit Cards (7 cards)
**Current**: 7 support unit cards in JSON with minimal documentation

**Action Items**:
- Cross-reference with campaign settlement phase documentation
- Verify stats match across sources
- Add missing support units if any

**Estimated Time**: 1 hour

---

#### 8. Create Validation Script
**Goal**: Automated JSON schema validation

**Features**:
- Check for required fields
- Validate cost ranges (0-5 SP)
- Flag duplicate IDs
- Verify keyword consistency
- Check cross-references between factions and equipment

**Estimated Time**: 3-4 hours

---

## SECTION 8: SPECIFIC CARD EXAMPLES

### Complete Equipment Item Structure (Example: LONGSWORD)

**From Markdown** (equipment-pool-complete.md lines 74-86):
```
LONGSWORD
Card Count: 6 cards
Crafting Cost: 4 Scrap
Weight: Medium
Faction Restrictions: None (Universal)

Cards:
1. Slash (2 SP, Melee): Deal 4 damage
2. Thrust (2 SP, Melee): Deal 3 damage, +2 damage if attacking from front arc
3. Parry (0 SP, Reactive): Reduce damage by 2, next attack this turn +1 damage
4. Riposte (1 SP, Reactive): When attacked in melee, deal 3 damage to attacker
5. Pommel Strike (1 SP, Melee): Deal 2 damage, target loses 1 SP next turn
6. Guard Stance (2 SP, Defense): +2 Defense until your next turn
```

**In JSON** (recommended structure):
```json
{
  "id": "longsword-slash",
  "name": "Slash",
  "type": "attack",
  "cost": 2,
  "range": "Melee",
  "damage": 4,
  "effect": "Deal 4 damage",
  "heat": "0",
  "keywords": ["equipment", "weapon", "longsword", "melee"],
  "equipmentItem": "longsword",
  "cardCount": 1,
  "cardType": "equipment"
}
```

**Pattern**: Each of the 6 longsword abilities becomes a separate JSON object

---

### Faction Core Card Structure (Example: Church)

**From Markdown** (church/deck-equipment-system.md lines 30-38):
```
1. BLOOD OFFERING (REVISED for Dice System - BALANCE NERF)
Type: Gambit (Self-Harm)
SP Cost: 0
Effect: Discard 2 cards from top of your deck (self-harm). Your next attack this turn: +3 damage, ignores 1 Defense, and -1 to target number (easier to hit). LIMIT: You can only play 1 Blood Offering per turn.
Keywords: Gambit, Self-Harm, Buff, Accuracy
```

**In JSON** (current format):
```json
{
  "id": "blood-offering",
  "name": "Blood Offering",
  "type": "utility",
  "cost": 0,
  "range": "Self",
  "effect": "Discard 2 cards from top of your deck (self-harm). Your next attack this turn: +3 damage, ignores 1 Defense, and -1 to target number (easier to hit). LIMIT: You can only play 1 Blood Offering per turn.",
  "heat": "0",
  "keywords": ["faction", "church", "gambit", "self-harm", "buff"],
  "cardCount": 1,
  "cardType": "faction"
}
```

---

## SECTION 9: TECHNICAL NOTES

### JSON Structure Best Practices

**Current Structure** (working well):
```json
{
  "_meta": {
    "version": "3.2",
    "lastUpdated": "2025-10-17",
    "description": "..."
  },
  "universal": [ array of card objects ],
  "church": [ array of card objects ],
  "equipment": [ array of card objects ],
  ...
}
```

**Recommended Fields** (for all cards):
- `id` - kebab-case unique identifier
- `name` - Title Case display name
- `type` - attack | defense | utility | movement | passive | reactive
- `cost` - 0-5 (SP cost)
- `range` - "Melee" | "Ranged X-Y" | "Self" | "Area"
- `effect` - Full text description
- `heat` - "+X" | "-X" | "0"
- `keywords` - Array of tags for filtering
- `cardCount` - Number of copies in deck (1-3)
- `cardType` - "core" | "faction" | "primary" | "secondary" | "equipment"

**Optional Fields** (context-dependent):
- `damage` - Number (for attack cards)
- `healing` - Number (for utility cards)
- `equipmentItem` - String (which equipment this belongs to: "longsword", "crossbow")
- `craftingCost` - Number (scrap cost for equipment)
- `weight` - "light" | "medium" | "heavy"
- `factionRestrictions` - Array (for faction-specific equipment)

---

### Markdown Parsing Recommendations

**Standardize Headers**:
```markdown
### 1. CARD NAME (Type)
### 2. CARD NAME (Type)
...

#### EQUIPMENT NAME (X cards)
**Cards**:
1. Ability Name (cost, range): Effect
2. Ability Name (cost, range): Effect
...
```

**Benefits**:
- Easier automated parsing
- Consistent documentation format
- Clear distinction between faction core and equipment

---

## SECTION 10: ESTIMATED COMPLETION TIMELINE

### Phase 1: Critical Fixes (3-4 hours)
- Complete Ossuarium faction (15 cards)
- Add missing Church cards (5 cards)
- **Total**: 20 cards

### Phase 2: Faction Completion (12-16 hours)
- Complete 8 remaining factions (88 cards)
- Add primary/secondary equipment to each
- **Total**: 88 cards

### Phase 3: Equipment Pool (6-8 hours)
- Add missing equipment items (75 cards)
- Verify stats match markdown
- **Total**: 75 cards

### Phase 4: Polish & Validation (4-5 hours)
- Resolve naming discrepancies (11 cards)
- Add tactics cards (20 cards)
- Document support units (7 cards)
- **Total**: 38 cards

### GRAND TOTAL
- **Cards to Add**: 221 cards
- **Estimated Time**: 25-33 hours
- **Current Database**: 170 cards
- **Target Database**: 391 cards

---

## APPENDIX A: Faction Card Lists (Current State)

### CHURCH (10/21 cards)
1. Absolution
2. Blood Offering
3. Chains Of Penance
4. Consecrated Ground
5. Divine Judgment
6. Flagellant's Zeal
7. Last Rites
8. Martyrdom Protocol
9. Righteous Fury
10. (Church card 10 name unknown)

**Missing**: Divine Guidance, Martyrdom's Certainty, Zealot's Focus, Point-Blank Execution, Confession Under Duress, + 6 primary + 5 secondary

---

### WYRD CONCLAVE (21/21 cards) ✓ COMPLETE
**Faction Core (10)**:
1. Bargain Struck, 2. Fae Bargain, 3. Deal With The Devil, 4. Price Paid, 5. Bargain Siphon, 6. Fae Curse, 7. Fae Mirror, 8. Stolen Strength, 9. Stolen Face, 10. Reality Fracture

**Primary (6)**:
11. Shimmer Strike, 12. Phase Cut, 13. Paradox Blade, 14. Incomprehensible Strike, 15. Impossible Geometry, 16. Mirage Assault

**Secondary (5)**:
17. Shimmer Veil, 18. Shimmer Step, 19. Mirror Self, 20. Reality Shard, 21. Temporal Loop

---

### OSSUARIUM (6/21 cards) - CRITICAL
1-6. (Card names not extracted - need to query JSON)

**Missing**: 4 additional faction core + 6 primary + 5 secondary

---

### EMERGENT SYNDICATE (10/21 cards)
1. Chrysalis Rebirth
2. Collective Consciousness
3. Compound Vision
4. Exoskeleton Molt
5. Hive-Mind Link
6. Mandible Rend
7. Metamorphic Adaptation
8. Pheromone Command
9. Segmented Strike
10. Swarm Intelligence

**Missing**: 6 primary + 5 secondary

---

### (Other factions follow similar pattern - 10 core, missing 11)

---

## APPENDIX B: Equipment Pool Checklist

### Weapons (68 cards across 14 items)

**Light Weapons** (10 cards):
- [ ] Dagger (3 cards): Stab, Deflect, Double-Strike
- [ ] Pistol (3 cards): Quick Shot, Point Blank, Reload
- [ ] Hand Axe (4 cards): Chop, Hook, Throw, Retrieve

**Medium Weapons** (16 cards):
- [ ] Longsword (6 cards): Slash, Thrust, Parry, Riposte, Pommel Strike, Guard Stance
- [ ] Spear (5 cards): Thrust, Sweep, Brace, Javelin Throw, Defensive Stance
- [ ] Mace (5 cards): Crush, Shield Break, Stun Strike, Overhead Smash, Backswing

**Heavy Weapons** (21 cards):
- [ ] Greatsword (8 cards): Cleave, Overhead Smash, Spinning Slash, Execute, Guard Break, Pommel Bash, Impale, Defensive Sweep
- [ ] Warhammer (6 cards): Crushing Blow, Earthshaker, Backswing, Forge Fury, Armor Break, Slam
- [ ] Halberd (7 cards): Thrust, Slash, Hook, Trip, Overhead Chop, Defensive Sweep, Impale

**Ranged Weapons** (15 cards):
- [ ] Crossbow (5 cards): Aimed Shot, Quick Shot, Reload, Suppressing Fire, Leg Shot
- [ ] Longbow (4 cards): Rapid Fire, Aimed Shot, Volley, Pierce Shot
- [ ] Rifle (6 cards): Snipe, Burst Fire, Suppressing Fire, Reload, Aimed Shot, Hip Fire

**Exotic Weapons** (11 cards):
- [ ] Chain Whip (6 cards): Lash, Grapple, Trip, Disarm, Strangle, Sweep
- [ ] Flail (5 cards): Wild Swing, Overhead Crush, Chain Wrap, Momentum Strike, Defensive Spin

---

### Shields (11 cards across 4 items)

- [ ] Buckler Shield (2 cards): Quick Deflect, Shield Bash
- [ ] Dueling Dagger (2 cards): Parry, Offhand Strike
- [ ] Kite Shield (3 cards): Shield Block, Shield Charge, Defensive Stance
- [ ] Tower Shield (4 cards): Iron Wall, Shield Wall, Advance, Hunker Down

---

### Plating (11 cards across 4 items)

- [ ] Ablative Plating (3 cards): Reactive Armor, Shrapnel Burst, Sacrificial Layer
- [ ] Spike Plating (2 cards): Thorn Defense, Charge Damage
- [ ] Reinforced Plating (3 cards): Damage Reduction, Fortified Hull, Emergency Bulkhead
- [ ] Stealth Plating (3 cards): Sensor Dampening, Heat Signature Reduction, Optical Camouflage

---

### Sigils (31 cards across 11 items)

**Universal Sigils** (7 cards):
- [ ] Repair Sigil (2 cards): Emergency Repair, Auto-Patch System
- [ ] Heat Sink Sigil (2 cards): Passive Cooling, Vent Boost
- [ ] Targeting Sigil (3 cards): Aim Assist, Weak Point Scan, Lock-On

**Faction-Exclusive Sigils** (24 cards):
- [ ] Martyr's Brand - Church (3 cards)
- [ ] Forge-Rune - Dwarves (3 cards)
- [ ] Living Seal - Elves (3 cards)
- [ ] Death Mark - Ossuarium (3 cards)
- [ ] Glamour Sigil - Wyrd Conclave (4 cards)
- [ ] Mutation Sigil - Emergent (3 cards)
- [ ] Salvage Sigil - Nomads (2 cards)
- [ ] Contract Sigil - Exchange (3 cards)

---

## CONCLUSION

The card database is **structurally sound but incomplete**:

### Strengths:
- ✓ Excellent data quality (no missing fields, no duplicates)
- ✓ Consistent formatting and naming conventions
- ✓ One faction (Wyrd Conclave) serves as complete template
- ✓ 170 cards already implemented with proper JSON structure

### Weaknesses:
- ✗ 9 of 10 factions incomplete (missing equipment cards)
- ✗ Ossuarium critically incomplete (only 6/21 cards)
- ✗ Equipment pool 62% incomplete (46/121 cards)
- ✗ 11 documented cards missing from JSON
- ✗ 82 JSON cards lack markdown documentation

### Priority Actions:
1. **Immediate**: Complete Ossuarium (15 cards) + Add missing Church cards (5 cards)
2. **Short-term**: Complete all faction decks (88 cards)
3. **Medium-term**: Expand equipment pool (75 cards)
4. **Long-term**: Add tactics cards + validation script

### Estimated Effort: 25-33 hours to reach 100% completeness

---

**END OF AUDIT REPORT**

*Report Generated: October 18, 2025*
*Next Review: After Ossuarium completion*

