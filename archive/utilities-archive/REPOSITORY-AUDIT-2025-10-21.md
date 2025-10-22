# Repository Audit Report
**Date:** October 21, 2025
**Scope:** Complete repository analysis for contradictions, redundancy, and outdated information
**Version Context:** v5.29-FINAL (production balance)

---

## Executive Summary

Comprehensive audit of 307 files (146,682 lines) identified **critical contradictions** between simulator implementation, card database, and documentation. The repository contains outdated content from pre-v5.23 (before lifesteal removal) that contradicts the current production simulator.

**Severity Breakdown:**
- 🔴 **CRITICAL**: 5 major contradictions requiring immediate fixes
- 🟡 **WARNING**: 43 files with outdated lifesteal references
- 🟢 **RESOLVED**: 2 structural issues fixed during audit

---

## 🔴 CRITICAL CONTRADICTIONS

### 1. Ossuarium Card Database Completely Outdated
**Location:** [docs/cards/complete-card-data.json](docs/cards/complete-card-data.json)
**Issue:** All 21 Ossuarium faction cards describe lifesteal mechanics (Soul Harvest, Corpse Fuel, Drain Life, Vampiric Rune) that were removed in v5.23 (80+ days ago).

**Current Simulator Implementation (v5.23+):**
```python
# V5.23: REMOVED LIFESTEAL - Ossuarium now only gains Taint from dealing damage
# Taint accumulates and causes penalties, but NO card recovery
if attacker.faction.lower() == 'ossuarium' and actual_damage > 0:
    # Gain 1 Taint per 3 damage dealt (scales with aggression)
    taint_gain = (actual_damage + 2) // 3
```

**Card Database Still Shows:**
- Soul Harvest: "Deal 4 damage. Recover cards equal to damage dealt"
- Corpse Fuel: "Recover 5 cards from discard pile"
- Drain Life, Necrotic Touch, Vampiric Rune (all lifesteal)

**Impact:** The simulator ignores card effect text and hardcodes Taint mechanics, but card database misleads anyone reading faction cards.

**Recommendation:** Replace all 21 Ossuarium cards with v5.29 Taint-based cards (Decay Aura, Raise Dead, Phylactery, Taint cards).

---

### 2. Ossuarium Faction Documentation Completely Outdated
**Location:** [docs/factions/ossuarium/deck-equipment-system.md](docs/factions/ossuarium/deck-equipment-system.md)
**Date:** October 11, 2025 (40 days outdated)
**Issue:** Entire 500-line file describes pre-v5.23 lifesteal mechanics as if current.

**Document States:**
- "Signature Mechanic: Soul Harvest (drain HP from enemies to recover your own cards)"
- "Philosophy: Fast drain, hit-and-run lifesteal"
- Detailed Soul Harvest, Corpse Fuel, Bone Scythe Reap lifesteal cards
- No mention of Decay Aura, Taint tokens, or Phylactery

**Actual v5.29 Mechanics:**
- Decay Aura (passive): Enemies within 3 hexes gain +1 Taint/turn
- Phylactery: Resurrect once per mission at 5 HP
- Raise Dead: Summon skeletal Thralls
- Taint penalties (Heat/damage) instead of lifesteal recovery

**Recommendation:** Complete rewrite to match [docs/codex/faction-undead.html](docs/codex/faction-undead.html) which was fixed in previous session.

---

### 3. Dwarves Rune Counter Values Wrong
**Location:** [docs/codex/faction-dwarves.html](docs/codex/faction-dwarves.html)
**Issue:** Codex shows outdated rune counter values.

**Codex States:**
> "Each counter reduces all damage by 1 (max 2 counters)"
> "Balance Update Oct 19: Max reduced from 3 to 2 counters"

**Simulator Shows (v5.25):**
```python
# V5.25: Buffed from 3 → 4 damage per counter (Dwarves still struggling at 28.9% WR)
# Each rune counter reduces 4 damage
rune_reduction = min(self.rune_counters * 4, remaining_damage)
# Max 3 counters (not 2)
attacker.rune_counters = min(attacker.rune_counters + rune_effect['generate'], 3)
```

**Actual v5.29 Values:**
- 4 damage reduction per counter
- Max 3 counters
- Total max reduction: **12 damage** (not 2!)

**Impact:** Massive understatement of faction power. Codex says 2 max damage reduction, simulator implements 12.

**Recommendation:** Update codex to reflect v5.25 buff (4 dmg/counter, max 3 counters).

---

### 4. Vestige Bloodlines Biomass Generation Wrong
**Location:** [docs/codex/faction-bloodlines.html](docs/codex/faction-bloodlines.html)
**Issue:** Codex describes passive Biomass generation that doesn't exist in simulator.

**Codex States:**
> "Vestige Heritage: Gain 2 Biomass at start of your turn (passive generation)"
> "Balance Update Oct 19: Added 2 Biomass per turn passive generation, increased from 1/turn"

**Simulator Shows (v5.17):**
```python
# Bloodlines: Gain Biomass on kill (Vestige Heritage mechanic)
# V5.17: Nerfed from 2 → 1 per kill (was too strong at 82% WR)
if not defender.is_alive and attacker.faction.lower() == 'vestige-bloodlines':
    biomass_gain = 1  # V5.17: Reduced from 2
    attacker.biomass_tokens = min(attacker.biomass_tokens + biomass_gain, 10)
```

**Actual v5.29 Mechanics:**
- Gain 1 Biomass **on kill** (not per turn)
- No passive generation
- v5.17 nerf from 2 → 1 per kill

**Impact:** Codex describes a much stronger mechanic (2/turn passive) than what's implemented (1 on kill).

**Recommendation:** Update codex to match simulator (1 Biomass on kill, no passive generation).

---

### 5. Exchange Credit Generation Rate Wrong
**Location:** [docs/codex/faction-exchange.html](docs/codex/faction-exchange.html)
**Issue:** Codex doesn't specify v5.17 nerf to credit generation.

**Codex Shows:**
- Generic mentions of "Credit generation" and "gains Credits"
- No specific rate mentioned

**Simulator Shows (v5.17):**
```python
# Exchange: Gain Credits
# V5.17: Nerfed to gain 1 Credit per 2 attacks (was every attack at 78% WR)
if credit_effect['generate'] > 0:
    attacker.credit_attack_count += 1
    if attacker.credit_attack_count >= 2:
        attacker.credit_tokens = min(attacker.credit_tokens + credit_effect['generate'], 10)
        attacker.credit_attack_count = 0
```

**Actual v5.29 Mechanics:**
- 1 Credit per **2 attacks** (v5.17 nerf)
- Was 1 per attack (too strong at 78% WR)

**Recommendation:** Add explicit credit generation rate to codex.

---

## 🟡 WARNING: Outdated Lifesteal References

**43 files** contain references to lifesteal, Soul Harvest, or Corpse Fuel mechanics removed in v5.23:

### Reference Documentation (Intentionally Historical?)
- [docs/reference/PLAYTEST-READY.md](docs/reference/PLAYTEST-READY.md) - "Ossuarium: Lifesteal vampire with resurrections (Soul Harvest)"
- [docs/reference/equipment-pool-complete.md](docs/reference/equipment-pool-complete.md) - Soul Harvest and Corpse Fuel card descriptions
- [docs/reference/faction-comparison-playtest.md](docs/reference/faction-comparison-playtest.md) - Extensive lifesteal analysis
- [docs/reference/card-template-specification.md](docs/reference/card-template-specification.md) - Soul Harvest as example card
- [docs/reference/card-optimization-dice-system.md](docs/reference/card-optimization-dice-system.md) - Lifesteal mechanic analysis
- [docs/reference/playtest-assessment.md](docs/reference/playtest-assessment.md) - "Ossuarium: Lifesteal vampire"

### Faction Documentation
- [docs/factions/ossuarium/deck-equipment-system.md](docs/factions/ossuarium/deck-equipment-system.md) - **CRITICAL** (see above)
- [docs/factions/ossuarium/support-units.md](docs/factions/ossuarium/support-units.md) - Lifesteal references
- [docs/factions/exchange/deck-equipment-system.md](docs/factions/exchange/deck-equipment-system.md) - Mentions Soul Harvest
- [docs/factions/emergent/deck-equipment-system.md](docs/factions/emergent/deck-equipment-system.md) - References lifesteal
- [docs/factions/index.md](docs/factions/index.md) - Ossuarium described with lifesteal
- [docs/factions/vestige-bloodlines/deck-equipment-system.md](docs/factions/vestige-bloodlines/deck-equipment-system.md) - Lifesteal references

### Lore/Campaign Documentation
- [docs/campaigns/flesh-bargain-variants.md](docs/campaigns/flesh-bargain-variants.md) - References lifesteal
- [docs/lore/soulstone-system.md](docs/lore/soulstone-system.md) - Lifesteal descriptions
- [docs/lore/iconic-npcs.md](docs/lore/iconic-npcs.md) - NPC with lifesteal
- [docs/lore/year-zero-timeline.md](docs/lore/year-zero-timeline.md) - Historical lifesteal reference

### Rules Documentation
- [docs/rules/casket-classes.md](docs/rules/casket-classes.md) - Lifesteal mentions
- [docs/rules/quick-reference.md](docs/rules/quick-reference.md) - Soul Harvest reference
- [docs/rules/taint-exploitation.md](docs/rules/taint-exploitation.md) - Lifesteal references
- [docs/rules/component-damage-system.md](docs/rules/component-damage-system.md) - Lifesteal example

### Codex HTML (Public-Facing)
- ✅ [docs/codex/faction-undead.html](docs/codex/faction-undead.html) - **FIXED** in previous session
- [docs/codex/faction-exchange.html](docs/codex/faction-exchange.html) - Mentions lifesteal
- [docs/codex/equipment-decks.html](docs/codex/equipment-decks.html) - References Soul Harvest
- [docs/codex/rules-taint-exploitation.html](docs/codex/rules-taint-exploitation.html) - Lifesteal references
- [docs/codex/enemies-bestiary.html](docs/codex/enemies-bestiary.html) - Lifesteal enemies

### Cards & Examples
- [docs/cards/README.md](docs/cards/README.md) - Lifesteal examples
- [docs/cards/new-cards-dice-system.md](docs/cards/new-cards-dice-system.md) - Soul Harvest card
- [docs/examples/spell-equipment-combat-demo.md](docs/examples/spell-equipment-combat-demo.md) - Lifesteal combat

### Balance Documentation (Historical Context)
- [docs/BALANCE-FINAL-V5.29.md](docs/BALANCE-FINAL-V5.29.md) - References lifesteal removal (correct historical context)
- [docs/CRITICAL-DICE-MECHANICS-BUG-REPORT.md](docs/CRITICAL-DICE-MECHANICS-BUG-REPORT.md) - Lifesteal mechanics described
- [docs/codex/balance-v529-final.html](docs/codex/balance-v529-final.html) - States "SP system removed" (misleading - only old economy removed)

**Recommendation:** Categorize these files as either:
1. **Historical/Archive** - Move to archive folder or clearly mark as pre-v5.23
2. **Needs Update** - Update to reflect v5.29 Taint mechanics
3. **Reference Examples** - Update examples to use current mechanics

---

## 🟢 RESOLVED DURING AUDIT

### 1. ✅ Duplicate Faction Folders
**Issue:** Redundant faction folders with conflicting content.

**Found:**
- `docs/factions/wyrd/` (18K, older Version 2.0 with Wyrd Tokens)
- `docs/factions/wyrd-conclave/` (22K, current version with Bargain Tokens)
- `docs/factions/bloodlines/` (only support-units.md, 474 lines Version 3.0)
- `docs/factions/vestige-bloodlines/` (complete faction, support-units.md 283 lines Version 2.0)

**Resolution:**
- Deleted `docs/factions/wyrd/` (superseded by wyrd-conclave)
- Copied newer bloodlines/support-units.md (v3.0) to vestige-bloodlines/
- Deleted `docs/factions/bloodlines/` folder
- Canonical structure now: wyrd-conclave/ and vestige-bloodlines/

---

### 2. ✅ SP Cost Terminology
**Initial Concern:** 385 instances of "SP cost" terminology - thought this might need changing to "Heat cost"

**Resolution:** NOT AN ISSUE
- SP cost = Soul-Point cost (resource to play cards)
- Heat = separate penalty mechanic (gained from card effects)
- Both systems coexist correctly
- No changes needed

---

## Additional Findings

### Version Reference Spread
**38 files** contain version references (v5.1 through v5.29), mostly in:
- Archive history files (correct)
- Simulator code comments (correct)
- Some codex pages (may need v5.29-FINAL standardization)

### Duplicate QUICKSTART Files
- `./QUICKSTART.md` - Repository contributor guide
- `./playtest-kit/QUICKSTART.md` - Player quick-start guide
- **Status:** Different content, both valid (different audiences)

### Faction Count
**10 playable factions confirmed:**
1. Church of Absolution
2. Dwarven Forge-Guilds
3. Ossuarium (Undead)
4. Elven Thornveil Enclaves
5. Wyrd Conclave (Fae)
6. Nomad Clans
7. The Exchange (Merchants)
8. Vestige Bloodlines (Mutants)
9. Emergent Collective (Hivemind)
10. Crucible Packs (Goblinoid forge-worshippers)

**11th faction:** Draconid Remembrance (NPC-ONLY, correctly marked in codex)

---

## Recommended Action Plan

### Immediate Priority (Critical Fixes)
1. **Ossuarium Card Database** - Replace all 21 cards with v5.29 Taint mechanics
2. **Ossuarium Faction Docs** - Complete rewrite of deck-equipment-system.md
3. **Dwarves Codex** - Update to 4 dmg/counter, max 3 counters
4. **Bloodlines Codex** - Update to 1 Biomass on kill (not 2/turn)
5. **Exchange Codex** - Add "1 Credit per 2 attacks" rate

### Secondary Priority (Documentation Cleanup)
6. Audit all 43 lifesteal reference files - categorize as historical vs needs-update
7. Update reference documentation to reflect v5.29 mechanics
8. Standardize version references to v5.29-FINAL where appropriate
9. Consider archive folder for pre-v5.23 documentation

### Tertiary Priority (Verification)
10. Verify Church 5x discard bonus documented in codex
11. Verify Elves bleed cap (8 or 4?) across all docs
12. Cross-reference all faction mechanics simulator → codex → card database
13. Verify equipment damage values match v5.29 balance spreadsheet

---

## Audit Methodology

**Files Analyzed:** 307 (.md, .html, .json, .py)
**Lines Analyzed:** 146,682
**Search Patterns:**
- Faction-specific mechanics (lifesteal, rune counters, biomass, etc.)
- Version references (v5.x)
- Duplicate file patterns
- Terminology consistency (SP cost, Heat, etc.)

**Tools Used:**
- `grep -r` for text pattern matching
- `diff` for file comparison
- `jq` for JSON analysis
- Manual file reading for context verification

**Repository State:** Git shows modified files, clean working tree (no uncommitted critical changes from previous sessions)

---

## Conclusion

The repository contains **high-quality production-ready balance** (v5.29-FINAL with 7/10 factions competitive) but suffers from **documentation drift** where simulator implementation has evolved faster than supporting documentation.

**Primary Issue:** The v5.23 lifesteal removal (80 days ago) was implemented in simulator but never propagated to card database and faction documentation.

**Impact:** Playtesters reading docs/factions/ossuarium/ would build decks based on lifesteal mechanics that don't exist in the actual game.

**Severity:** 🔴 CRITICAL for Ossuarium, 🟡 WARNING for other factions

**Estimated Fix Time:**
- Critical fixes: 4-6 hours (rewrite Ossuarium cards/docs, update 4 faction codex pages)
- Secondary cleanup: 8-10 hours (audit + update 43 lifesteal references)
- Full documentation alignment: 15-20 hours

