# Comprehensive Faction Balance Audit - Penance RPG
**Date**: October 18, 2025
**Auditor**: AI Analysis
**Scope**: All 10 playable factions

---

## Executive Summary

This audit analyzes all 10 factions across five key dimensions:
1. **Card Count Balance** - Verify each faction has adequate cards
2. **Mechanical Power Level** - Identify overpowered/underpowered mechanics
3. **Support Unit Balance** - Compare HP, movement, and abilities
4. **Deck Composition Structure** - Ensure consistent framework
5. **Win Condition Uniqueness** - Verify distinct playstyles

**Critical Findings**:
- **9 out of 10 factions** are missing equipment cards in the JSON database
- **Elves** have infinite Bleed scaling (no cap defined)
- **Ossuarium** was previously overpowered (fixed via Soul Harvest nerf)
- **All 10 factions are mechanically distinct** - excellent design diversity

---

## Section 1: CARD COUNT ISSUES

### Current State

| Faction | Faction Cards | Equipment Cards | Tactics | Total |
|---------|---------------|-----------------|---------|-------|
| Church | 10 | 0* | 3 | 13 |
| Dwarves | 10 | 0* | 0 | 10 |
| Ossuarium | 6 | 0* | 0 | 6 |
| Elves | 10 | 0* | 0 | 10 |
| Crucible | 10 | 0* | 0 | 10 |
| Exchange | 10 | 0* | 0 | 10 |
| Nomads | 10 | 0* | 0 | 10 |
| Vestige-Bloodlines | 10 | 0* | 0 | 10 |
| Emergent | 10 | 0* | 0 | 10 |
| Wyrd-Conclave | 10 | 11 | 0 | 21 |

*Note: Equipment cards exist in markdown documentation but are missing from `complete-card-data.json`

### Expected vs. Actual

**Expected per faction**:
- 10 Faction Core cards
- 12-18 Equipment cards (12 Primary Weapon + 6 Secondary Equipment)
- 3-5 Tactics cards (player chooses 2)
- **Total: 25-33 cards per faction**

**Actual**: Only Wyrd-Conclave approaches expected count (21 cards with embedded equipment)

### Critical Issues

**BLOCKER: JSON Database Incomplete**
- Equipment cards are documented in `/docs/factions/*/deck-equipment-system.md`
- Equipment cards are NOT in `/docs/cards/complete-card-data.json` (except for legacy 46-card "equipment" array)
- This creates a disconnect between documentation and game data

**Missing Faction Content**:
- **Ossuarium**: Only 6 faction cards (should be 10)
- **All factions except Wyrd**: Missing equipment cards in JSON
- **9 factions**: Missing Tactics cards in JSON

### Recommendations

**HIGH PRIORITY**:
1. Add equipment cards to `complete-card-data.json` for all 9 factions
2. Add 4 missing Ossuarium faction cards (currently at 6/10)
3. Add Tactics cards to JSON database (currently only Church has 3)

**STRUCTURE DECISION NEEDED**:
- Should equipment cards be in top-level "equipment" array (current legacy format)?
- Should equipment cards be embedded in faction sections (Wyrd-Conclave approach)?
- Recommend: **Faction-specific equipment in faction sections** (cleaner organization)

---

## Section 2: MECHANICAL POWER LEVEL

### Power Tier Rankings

**S-Tier (Strongest)**:
- **Wyrd-Conclave**: Reality manipulation (time rewind, card theft, bargain mechanics)
- **Ossuarium** (Campaign): 3 resurrections is excessive (Phylactery Relic marked campaign-only)

**A-Tier (Strong)**:
- **Elves**: Infinite Bleed scaling (needs cap)
- **Church**: High-risk/high-reward martyrdom (balanced)
- **Crucible**: Permanent upgrades via Ancestral Iron

**B-Tier (Balanced)**:
- **Dwarves**: Slow but unkillable (low movement balances high defense)
- **Exchange**: Economy-dependent (strong if Credits generated)
- **Emergent**: Form-shifting adaptability

**C-Tier (Needs Testing)**:
- **Nomads**: Scavenger mechanics (power unclear without full card data)
- **Vestige-Bloodlines**: Pack tactics (power unclear without full card data)

### Infinite Loops & Broken Combos

**PATCHED: Ossuarium Infinite Sustain**
- **Original**: Soul Harvest 4 damage = 4 cards recovered (100% lifesteal)
- **Fixed**: Soul Harvest 4 damage = 3 cards recovered (75% lifesteal)
- **Status**: BALANCED (nerf documented in `/docs/factions/ossuarium/deck-equipment-system.md`)

**ISSUE: Elves Infinite Bleed**
- **Combo**: Thorn Strike + Pruning Cut + Shadowleaf Assassin + Thorn Stalkers
- **Result**: 10+ Bleed counters per turn = 10+ damage/turn (exponential scaling)
- **Problem**: No cap on Bleed stacking mentioned in documentation
- **Fix Needed**: Implement Bleed cap (recommend 10-12 counters per target)
- **Balance Note**: Docs mention "Consider capping Bleed at 10 counters" but not enforced

**CONCERN: Wyrd-Conclave Time Manipulation**
- **Reality Fracture**: Rewind entire turn once per mission (no counterplay)
- **Between Moments**: Take 2 turns in a row (action economy advantage)
- **Stolen Face**: Permanently gain enemy cards on kill (deck expansion)
- **Assessment**: High skill ceiling, potentially frustrating to play against
- **Counterplay**: Reality Fracture is once per mission, Bargains can be refused

**BALANCED: Church Martyrdom Loop**
- **Combo**: Blood Offering + Martyrdom Protocol + Righteous Fury
- **Result**: Self-harm for +damage, but requires HP management
- **Risk**: Can self-destruct if mismanaged
- **Verdict**: High risk balances high reward

**BALANCED: Dwarves Fortress Defense**
- **Combo**: Shield Wall + Tower Shield + Rune of Protection
- **Result**: 10+ Defense (nearly immune to standard damage)
- **Balance**: Low movement (2 hexes), low SP (3-4), slow kills
- **Counterplay**: Kite, use armor-piercing, bypass via control effects

### Resource Economy Balance

**Forge Tokens (Crucible)**:
- Generation: 1-2/turn in lava, 3 on Honor Duel kill
- Spending: 2-5 tokens per effect
- Cap: Not specified (assume 10 like Bargain Tokens)
- Assessment: BALANCED (terrain-dependent generation)

**Bargain Tokens (Wyrd-Conclave)**:
- Generation: 1/turn passive, 3 from Fae Bargain
- Spending: 1-5 tokens per effect
- Cap: 10 tokens maximum
- Inflation Combo: Bargain Struck + Fae Bargain + Price Multiplier = 5+ tokens/turn
- Assessment: BALANCED (opponents can refuse bargains)

**Credits (Exchange)**:
- Generation: Passive, from economic cards
- Spending: Hire mercenaries mid-battle (2-8 Credits per unit)
- Assessment: Unique economy mechanic, power unclear without full data

**Scrap Tokens (Nomads)**:
- Generation: Salvage from destroyed units
- Spending: Craft equipment, improvise solutions
- Assessment: Reactive mechanic, power unclear without full data

---

## Section 3: SUPPORT UNIT BALANCE

### Statistical Comparison

| Faction | Avg HP | Avg Move | Avg Defense | Assessment |
|---------|--------|----------|-------------|------------|
| Church | 8.0 | 3.0 | 1.0 | Balanced (low HP, martyrdom theme) |
| Dwarves | 11.7 | 2.3 | 3.0 | Overstatted but slow |
| Ossuarium | 11.3 | 3.0 | 1.3 | Balanced (resurrection compensates) |
| Elves | 8.0 | 4.3 | 1.3 | Glass cannons (skill-dependent) |

**Note**: Only 4 factions have complete support unit documentation

### Unit-by-Unit Analysis

**CHURCH (3 units)**:
- Flagellant Pack: 6 HP, 0 Def, self-harm berserker (thematic)
- Penitent Squad: 8 HP, 1 Def, balanced infantry
- Relic Bearers: 10 HP, 2 Def, support aura (Tesla Cross)
- **Verdict**: BALANCED - Diverse roles, fits faction theme

**DWARVES (3 units)**:
- Shield Wall Guard: 12 HP, 4 Def, nearly unkillable tank
- Bombard Battery: 8 HP, 2 Def, long-range artillery (8 damage)
- Rune Sentinel: 15 HP, 3 Def, construct with scaling (Rune Counters)
- **Verdict**: OVERSTATTED - Highest HP and Defense, but balanced by low movement

**OSSUARIUM (3 units)**:
- Bone Thrall Swarm: 12 HP (4x3), 0 Def, infinite resurrection
- Grave Knight: 14 HP, 3 Def, lifesteal + soul counters
- Fleshcrafter: 8 HP, 1 Def, healer/summoner (creates Flesh Abominations)
- **Verdict**: BALANCED - Resurrection theme, medium stats

**ELVES (3 units)**:
- Thorn Stalkers: 6 HP, 5 Move, Bleed application
- Rootweaver Circle: 8 HP, 2 Move, terrain control (Verdant Zones)
- Shadowleaf Assassin: 10 HP, 6 Move, 12 damage assassinate
- **Verdict**: FRAGILE - Lowest HP/Defense, highest mobility, skill-dependent

### Power Tier Rankings (Support Units)

**S-Tier**:
- Dwarven Rune Sentinel (15 HP, 3 Def, Rune scaling, area damage)
- Ossuarium Grave Knight (14 HP, lifesteal, souls, resurrection mechanic)

**A-Tier**:
- Elven Shadowleaf Assassin (12 damage assassinate, 6 move, stealth)
- Dwarven Bombard Battery (8 damage at range 8, splash damage)

**B-Tier**:
- Dwarven Shield Wall Guard (12 HP, 4 Def, static defender)
- Church Relic Bearers (Tesla aura, zone control)
- Ossuarium Fleshcrafter (healer, creates minions)

**C-Tier**:
- Most other units (functional but not exceptional)

### Balance Concerns

**ISSUE: Dwarven Support Units Too Strong?**
- Rune Sentinel: 15 HP + 3 Defense + regeneration + area damage
- Shield Wall Guard: 12 HP + 4 Defense = nearly unkillable
- **Counterpoint**: Low movement (2-3 hexes), can be kited

**ISSUE: Elven Support Units Too Fragile?**
- Shadowleaf Assassin: 10 HP, 1 Defense = dies to burst damage
- Thorn Stalkers: 6 HP, 1 Defense = fragile scout
- **Counterpoint**: High mobility (5-6 hexes), hit-and-run tactics

**VERDICT**: Support units are thematically appropriate but potentially imbalanced
- Dwarves: Tank faction has tank units (consistent)
- Elves: Glass cannon faction has glass cannon units (consistent)
- Recommend: Playtesting to confirm balance

---

## Section 4: DECK COMPOSITION STRUCTURE

### Universal Framework

**Expected Deck Structure**:
```
10 Universal Core (movement, generic attacks)
+ 10 Faction Core (faction-specific abilities)
+ 12 Primary Weapon cards (main attack suite)
+ 6 Secondary Equipment cards (utility/defense)
+ 2 Tactics cards (chosen from 5 available)
= 40 cards total (standard deck)
```

### Faction Variations

**Ossuarium Exception**:
- Only 6 Faction Core cards (instead of 10)
- Uses "Decay" cards instead of "Damage" cards on reshuffle
- Rationale: Already undead, different degradation mechanic

**Wyrd-Conclave Exception**:
- 10 Faction Core + 11 Equipment embedded in faction section
- Total 21 cards in JSON (most complete faction)
- Rationale: Equipment is faction-specific (Folded-Blades, Reality-Shards)

**Scout/Assault/Heavy/Fortress Variations**:
- Scout (6 SP): Smaller deck (26-30 cards)
- Assault (5 SP): Medium deck (30-36 cards)
- Heavy (4 SP): Large deck (33-42 cards)
- Fortress (3 SP): Massive deck (36-48 cards)

### Consistency Analysis

**CONSISTENT ACROSS ALL FACTIONS**:
- 10 Universal Core cards (same for everyone)
- 10 Faction Core cards (unique per faction)* except Ossuarium (6)
- Choose 2 Tactics from 5 available

**INCONSISTENT**:
- Equipment card counts vary wildly in documentation
- JSON database missing most equipment cards
- Support unit slot costs vary (2-5 slots)

### Recommendations

**STANDARDIZE**:
1. All factions should have 10 Faction Core cards (add 4 to Ossuarium)
2. All factions should have 12 Primary + 6 Secondary equipment cards
3. All factions should have 5 Tactics (player chooses 2)

**EXCEPTION: Ossuarium Decay Mechanic**:
- Keep Decay cards instead of Damage cards (thematic, balanced)
- But increase Faction Core to 10 cards (consistency)

---

## Section 5: WIN CONDITION ANALYSIS

### Win Condition Diversity

**AGGRESSIVE BURST**:
- **Church**: Self-sacrifice martyrdom (Blood Offering, Righteous Fury)

**DEFENSIVE ATTRITION**:
- **Dwarves**: Fortress defense (Rune Counters, armor-piercing)
- **Ossuarium**: Lifesteal + resurrections (Soul Harvest, Phylactery)

**HIT-AND-RUN**:
- **Elves**: Bleed stacking + mobility (infinite DoT, kiting)
- **Nomads**: Scavenger survival (Scrap tokens, adaptability)

**TERRAIN CONTROL**:
- **Crucible**: Volcanic duels (Forge tokens, Honor Duels, lava terrain)
- **Elves**: Forest zones (Rootweavers, Verdant Zones)

**UNIQUE MECHANICS**:
- **Exchange**: Economic warfare (Credit economy, hired mercenaries)
- **Vestige-Bloodlines**: Pack tactics (animal mutations, coordination)
- **Emergent**: Bio-evolution (form shifting, metamorphosis)
- **Wyrd-Conclave**: Reality manipulation (bargains, time control, illusions)

### Uniqueness Scores

| Faction | Uniqueness | Primary Mechanic |
|---------|------------|------------------|
| Elves | 5/5 | Infinite Bleed DoT |
| Crucible | 5/5 | Honor Duels 1v1 |
| Exchange | 5/5 | Credit economy |
| Emergent | 5/5 | Form shifting |
| Wyrd-Conclave | 5/5 | Reality manipulation |
| Church | 5/5 | Self-harm martyrdom |
| Ossuarium | 5/5 | Resurrection loops |
| Vestige-Bloodlines | 4/5 | Animal mutations |
| Nomads | 4/5 | Scavenger survival |
| Dwarves | 3/5 | Pure tank |

### Overlap Analysis

**NO SIGNIFICANT OVERLAP DETECTED**
- Every faction has a distinct primary win condition
- Mechanical themes do not overlap significantly
- Elves and Ossuarium both do attrition, but via different mechanics (Bleed vs Lifesteal)
- Crucible and Wyrd both have token economies, but different purposes (Forge vs Bargain)

**VERDICT**: Excellent faction diversity. All 10 factions are mechanically distinct.

---

## Section 6: RECOMMENDATIONS

### HIGH PRIORITY (Critical Fixes)

1. **Complete JSON Database**
   - Add equipment cards for all 9 factions (currently only Wyrd has them)
   - Add 4 missing Ossuarium faction cards (currently 6/10)
   - Add Tactics cards for all 10 factions (currently only Church has 3)

2. **Implement Bleed Cap for Elves**
   - Cap Bleed counters at 10-12 per target (prevent infinite scaling)
   - Document cap explicitly in rules and card text
   - Elves docs already mention "consider capping Bleed" but not enforced

3. **Verify Ossuarium Balance**
   - Confirm Phylactery Relic is campaign-only (docs say yes, but verify in game)
   - 3 resurrections in campaign is overpowered
   - 2 resurrections in casual/arena is balanced

### MEDIUM PRIORITY (Balance Tuning)

4. **Test Dwarven Support Units**
   - Rune Sentinel (15 HP) and Shield Wall (12 HP, 4 Def) may be overstatted
   - Playtest to confirm if low movement (2-3 hexes) balances high durability
   - Consider slight HP/Defense reduction if too strong

5. **Test Elven Support Units**
   - Shadowleaf Assassin (10 HP, 1 Def) may be too fragile
   - Playtest to confirm if mobility (6 hexes) compensates for fragility
   - Consider +1 Defense or +2 HP if too weak

6. **Clarify Wyrd-Conclave Power Level**
   - Reality Fracture (time rewind) has no counterplay
   - Stolen Face (permanent card gain) has no cap
   - Playtest to confirm if once-per-mission limits prevent abuse

7. **Standardize Token Economy Caps**
   - Bargain Tokens: 10 max (documented)
   - Forge Tokens: No cap mentioned (recommend 10 max)
   - Credits: No cap mentioned (recommend no cap, but high costs)
   - Scrap Tokens: No cap mentioned (recommend no cap, reactive resource)

### LOW PRIORITY (Quality of Life)

8. **Standardize Support Unit Count**
   - Church, Dwarves, Ossuarium, Elves: 3 units each (asymmetric design)
   - Crucible, Exchange, Nomads, Vestige, Emergent, Wyrd: 6 units each (docs show 6)
   - Inconsistency is intentional (asymmetric design) but document rationale

9. **Add Support Unit Data to JSON**
   - Currently only in markdown files
   - Add to `complete-card-data.json` under `support_units` section

10. **Document Casket Frame Variations**
    - Scout (6 SP), Assault (5 SP), Heavy (4 SP), Fortress (3 SP)
    - Document deck size variations clearly
    - Explain equipment slot trade-offs

---

## Section 7: FACTION-SPECIFIC BALANCE REPORTS

### Church of Absolution

**Card Count**: 10 Faction + 0 Equipment + 3 Tactics = 13 total
- **ISSUE**: Missing equipment cards in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary equipment cards

**Mechanics**: Self-harm martyrdom
- Blood Offering: Discard cards for burst damage
- Martyrdom Protocol: Redirect damage to self
- Righteous Fury: Gain damage when low HP
- **BALANCE**: High risk/high reward, balanced

**Support Units**: 3 units (Flagellants, Penitents, Relic Bearers)
- **BALANCE**: Diverse, thematic, balanced

**Win Condition**: Kill enemy before self-destructing
- **UNIQUENESS**: 5/5 (only self-harm faction)

**VERDICT**: Balanced mechanically, missing equipment data

---

### Dwarven Forge-Guilds

**Card Count**: 10 Faction + 0 Equipment + 0 Tactics = 10 total
- **ISSUE**: Missing equipment cards and Tactics in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Rune Counter defense fortress
- Rune of Protection: +2 Defense per counter
- Stone Endurance: +2 cards to deck
- Armor-piercing attacks
- **BALANCE**: Slow but unkillable, balanced by low SP/movement

**Support Units**: 3 units (Shield Wall, Bombard Battery, Rune Sentinel)
- **CONCERN**: Overstatted (11.7 avg HP, 3.0 avg Defense)
- **COUNTERPOINT**: Balanced by low movement (2.3 avg)

**Win Condition**: Outlast through extreme defense
- **UNIQUENESS**: 3/5 (pure tank, less unique than others)

**VERDICT**: Mechanically balanced, potentially overstatted support units

---

### The Ossuarium

**Card Count**: 6 Faction + 0 Equipment + 0 Tactics = 6 total
- **CRITICAL ISSUE**: Only 6 faction cards (expected 10)
- **ISSUE**: Missing equipment and Tactics in JSON
- **STATUS**: Needs +4 Faction + 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Lifesteal + resurrection
- Soul Harvest: 75% lifesteal (NERFED from 100%, balanced)
- Phylactery: Resurrect at 5 HP once per mission
- Corpse Fuel: Recover 5 cards per enemy death
- **BALANCE**: Strong in campaign (3 resurrections), balanced in casual (2)

**Support Units**: 3 units (Bone Thralls, Grave Knight, Fleshcrafter)
- **BALANCE**: Medium stats, resurrection compensates

**Win Condition**: Grind enemy down, resurrect multiple times
- **UNIQUENESS**: 5/5 (only resurrection faction)

**VERDICT**: Needs 4 more faction cards, mechanically balanced after nerf

---

### Elven Verdant Covenant

**Card Count**: 10 Faction + 0 Equipment + 0 Tactics = 10 total
- **ISSUE**: Missing equipment and Tactics in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Infinite Bleed scaling + hit-and-run
- Bleed counters: Stack infinitely (1 damage/counter/turn)
- High mobility: 5-6 hexes movement
- Shadowleaf Assassin: 12 damage assassinate
- **CRITICAL ISSUE**: No Bleed cap = infinite scaling

**Support Units**: 3 units (Thorn Stalkers, Rootweavers, Shadowleaf)
- **CONCERN**: Fragile (8.0 avg HP, 1.3 avg Defense)
- **COUNTERPOINT**: Highest mobility (4.3 avg Move)

**Win Condition**: Apply Bleed, kite until enemy dies
- **UNIQUENESS**: 5/5 (infinite DoT scaling)

**VERDICT**: NEEDS BLEED CAP (10-12 counters max), otherwise overpowered

---

### Crucible Packs

**Card Count**: 10 Faction + 0 Equipment + 0 Tactics = 10 total
- **ISSUE**: Missing equipment and Tactics in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Forge tokens + Honor Duels + volcanic terrain
- Forge tokens: Generate in lava (1-2/turn)
- Honor Duel: 1v1 binding combat
- Ancestral Iron: Permanent upgrades (cross-mission)
- **BALANCE**: Terrain-dependent, unique, balanced

**Support Units**: 6 units documented (incomplete data in audit)
- **STATUS**: Need full stats for comparison

**Win Condition**: Win duels, gain permanent power
- **UNIQUENESS**: 5/5 (only duel mechanic)

**VERDICT**: Unique and balanced, missing card data

---

### Soulstone Exchange

**Card Count**: 10 Faction + 0 Equipment + 0 Tactics = 10 total
- **ISSUE**: Missing equipment and Tactics in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Credit economy + hired mercenaries
- Generate Credits mid-battle
- Hire mercenary units (2-8 Credits each)
- Compound Interest: Snowball resources
- **BALANCE**: Unclear without full card data

**Support Units**: 6 units, HIRE-ONLY (unique mechanic)
- **UNIQUE**: Must pay Credits to deploy (not pre-deployed)
- **STATUS**: Need full stats for comparison

**Win Condition**: Generate Credits, hire army, overwhelm
- **UNIQUENESS**: 5/5 (only economy faction)

**VERDICT**: Extremely unique, needs full data for balance assessment

---

### Nomad Collective

**Card Count**: 10 Faction + 0 Equipment + 0 Tactics = 10 total
- **ISSUE**: Missing equipment and Tactics in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Scrap tokens + mobility + survival
- Scrap tokens: Salvage from destroyed units
- High mobility and adaptability
- **BALANCE**: Unclear without full card data

**Support Units**: 3 units (Salvage Crew, Outrider Squadron, Caravan Walker)
- **STATUS**: Partial documentation, need full stats

**Win Condition**: Salvage battlefield, adapt, outlast
- **UNIQUENESS**: 4/5 (scavenger theme)

**VERDICT**: Unique scavenger mechanics, needs full data

---

### Vestige Bloodlines

**Card Count**: 10 Faction + 0 Equipment + 0 Tactics = 10 total
- **ISSUE**: Missing equipment and Tactics in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Pack tactics + animal mutations
- Bloodline powers: Wolf, Bear, Raven, Chitin, Serpent
- Pack coordination buffs
- **BALANCE**: Unclear without full card data

**Support Units**: 6 units (Pack Hunters, Berserker, Murder, Swarmling, Assassin, Alpha)
- **STATUS**: Partial documentation, need full stats

**Win Condition**: Use pack buffs, savage melee
- **UNIQUENESS**: 4/5 (animal mutations)

**VERDICT**: Unique mutation mechanics, needs full data

---

### Emergent Syndicate

**Card Count**: 10 Faction + 0 Equipment + 0 Tactics = 10 total
- **ISSUE**: Missing equipment and Tactics in JSON
- **STATUS**: Needs 12 Primary + 6 Secondary + 5 Tactics

**Mechanics**: Form shifting + bio-evolution
- Metamorph tokens: Transformation resource
- Forms: Assault, Tank, Scout, Support
- Hive-mind coordination
- **BALANCE**: Unclear without full card data

**Support Units**: 6 units (Drone Swarm, Molt Guardian, Adaptation, Hive Spawn, Catalyst, Apex)
- **STATUS**: Partial documentation, need full stats

**Win Condition**: Adapt forms to counter enemy
- **UNIQUENESS**: 5/5 (only transformation faction)

**VERDICT**: Extremely unique, needs full data

---

### Wyrd-Conclave

**Card Count**: 10 Faction + 11 Equipment + 0 Tactics = 21 total
- **STATUS**: MOST COMPLETE FACTION in JSON
- **ISSUE**: Missing Tactics (0/5)

**Mechanics**: Reality manipulation + bargain mechanics
- Bargain tokens: Force deals with costs
- Reality Fracture: Rewind turn (once per mission)
- Stolen Face: Copy enemy cards permanently
- Between Moments: Take 2 turns in a row
- **CONCERN**: Time manipulation may be oppressive
- **BALANCE**: Limited by once-per-mission restrictions

**Support Units**: 6 units (Shimmer Phantom, Bargain Broker, Stolen Soldier, Mirror Legion, Temporal Echo, Un-Thing)
- **STATUS**: Partial documentation, need full stats

**Win Condition**: Force bargains, manipulate reality
- **UNIQUENESS**: 5/5 (only reality-bending faction)

**VERDICT**: Most unique faction, potentially frustrating to play against

---

## Section 8: FINAL BALANCE VERDICT

### Overall Assessment

**STRENGTHS**:
1. Excellent faction diversity (all 10 factions are mechanically distinct)
2. Clear win conditions for each faction
3. Asymmetric design is intentional and well-executed
4. Self-balancing through counterplay (e.g., refuse bargains, kite tanks)

**WEAKNESSES**:
1. **CRITICAL**: JSON database is incomplete (missing equipment/tactics for 9 factions)
2. **CRITICAL**: Elves have infinite Bleed scaling (no cap)
3. Ossuarium missing 4 faction cards (6/10)
4. Dwarven support units may be overstatted (needs playtesting)
5. Elven support units may be too fragile (needs playtesting)

### Balance Tiers (Based on Available Data)

**S-Tier (Potentially Overpowered)**:
- **Elves**: Infinite Bleed scaling (NEEDS CAP)
- **Wyrd-Conclave**: Reality manipulation (high skill ceiling)

**A-Tier (Strong)**:
- **Church**: High burst damage (balanced by self-harm risk)
- **Ossuarium**: Multiple resurrections (campaign-only)
- **Crucible**: Permanent upgrades (long-term scaling)

**B-Tier (Balanced)**:
- **Dwarves**: Unkillable but slow (balanced by mobility)
- **Exchange**: Economy-dependent (balanced by Credit generation)
- **Emergent**: Form-shifting (balanced by reactive play)

**C-Tier (Insufficient Data)**:
- **Nomads**: Scavenger mechanics (need full card data)
- **Vestige-Bloodlines**: Pack tactics (need full card data)

### Recommended Action Items

**IMMEDIATE**:
1. Implement Bleed cap for Elves (10-12 counters per target)
2. Add 4 missing Ossuarium faction cards
3. Complete JSON database (equipment + tactics for all factions)

**SHORT-TERM**:
4. Playtest Dwarven support units (may need stat reduction)
5. Playtest Elven support units (may need stat buff)
6. Playtest Wyrd-Conclave Reality Fracture (may need additional restrictions)

**LONG-TERM**:
7. Standardize token economy caps (Forge, Credits, Scrap)
8. Document support unit design philosophy (asymmetric intentional)
9. Create balance patch notes for future updates

---

## Conclusion

Penance RPG has **excellent faction diversity** with 10 mechanically distinct factions. However, the JSON database is **critically incomplete**, with only 1 out of 10 factions having full equipment cards. The **Elves faction needs an immediate Bleed cap** to prevent infinite scaling. The **Ossuarium needs 4 additional faction cards** to reach the standard 10-card core.

Once the database is complete and the Bleed cap is implemented, the game will be in a strong balance state. Most factions appear well-balanced through asymmetric design and counterplay mechanics.

**Overall Grade**: B+ (would be A+ with complete data and Bleed cap)

---

**END OF AUDIT**

*Next Steps: Address critical issues (JSON completion, Bleed cap, Ossuarium cards), then conduct playtesting for fine-tuning.*
