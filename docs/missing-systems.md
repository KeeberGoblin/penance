# Missing Systems & Design Gaps
## Penance: Absolution Through Steel

**Version**: 0.1
**Last Updated**: October 9, 2025

---

## Critical Missing Systems (Blocks Playtesting)

### 1. **Deck Construction Rules** ⚠️ CRITICAL

**Status**: Not defined
**Needed for**: Building legal decks for any game mode

**What's Missing**:
- Deck size ranges per weight class (mentioned but not enforced)
  - Scout: 20-25 cards (which is correct? 20? 25? Player choice?)
  - Support: 25-30 cards
  - Heavy: 30-35 cards
  - Assault: 35-40 cards
  - Aberrant: 25-30 cards

**Must Define**:
- [ ] **Exact deck sizes** (fixed or range with min/max?)
- [ ] **Card copy limits** (can I have 3 copies of "Faithful Thrust"?)
- [ ] **Equipment card quantity rules**
  - Longsword adds how many cards? (mentioned as 3-5 in card-anatomy.md)
  - Shield adds how many?
  - Source Conduit arm adds exactly 5 spell cards (stated)
- [ ] **Mandatory cards**
  - 10 Universal cards (stated) ✓
  - Racial unique cards? (Undead get "Soul Reserve" deck—how many cards?)
- [ ] **Relic slot allocation**
  - Each Relic adds how many cards to deck?
  - Do Relics with ammo/charges add cards at all?
- [ ] **Starting hand size** (default 6, stated) ✓
- [ ] **Mulligan rules** (can you redraw starting hand?)

**Example Template Needed**:
```
SCOUT DECK CONSTRUCTION:
- Total Deck Size: 22 cards (fixed)
- Universal Cards: 10 (mandatory)
- Equipment Cards: 12 total
  - Right Arm Weapon: 3-4 cards
  - Left Arm Weapon/Shield: 3-4 cards
  - Relic Slot: 3-4 cards
- Racial Bonus: 0-1 cards (optional, race-specific)
- No card may appear more than 2 times
```

---

### 2. **Combat Resolution Mechanics** ⚠️ CRITICAL

**Status**: Vaguely described in CoreDesign.md
**Needed for**: Resolving any attack

**What's Missing**:
- [ ] **Attack resolution flowchart**
  - Declare target → Check range/LOS → Play card → Defender response → Damage?
  - Current description (CoreDesign.md:762-771) is incomplete
- [ ] **Hit rolls vs automatic hits**
  - Do attacks always hit, or do you roll dice?
  - "Some attacks require hit rolls" (line 769) - which ones?
- [ ] **Defense stat**
  - What's base Defense for each weight class?
  - Shields add "+2 Defense" - defense against what?
  - Is Defense a target number? Damage reduction? Evasion chance?
- [ ] **Armor system**
  - Separate from Defense?
  - Damage reduction? Ablative?
  - Weight class affects armor?
- [ ] **Critical hits**
  - "Rear attacks: critical hits more likely" - what's the crit system?
  - Natural 6 on d6? Doubles on 2d6? Automatic?
- [ ] **Damage types**
  - Physical, Fire, Ice, Lightning, Poison, Acid mentioned for Draconid breath
  - Do damage types interact with armor differently?
  - Resistance/vulnerability system?

**Needs Entire Section**:
```
### Combat Resolution (Detailed)

1. DECLARE ATTACK
   - Choose target in range and LOS
   - Check facing (front/side/rear)
   - Play attack card, spend SP

2. DEFENDER DECLARES DEFENSE
   - May play reactive defense cards (Unyielding Bulwark, etc.)
   - Apply Defense stat from facing/shields

3. ROLL TO HIT (if applicable)
   - Melee weapons: Auto-hit
   - Ranged weapons: Roll 1d6, 3+ hits (modified by range/cover)
   - Magic spells: Auto-hit unless specified

4. CALCULATE DAMAGE
   - Base damage from card
   - +/- modifiers (facing, buffs, debuffs)
   - Apply Defense reduction
   - Apply Armor (if any)
   - Minimum 1 damage (always deal at least 1)

5. RESOLVE DAMAGE
   - Defender discards cards equal to damage
   - If specific component targeted, track component damage
```

---

### 3. **Range & Line of Sight Rules** ⚠️ CRITICAL

**Status**: Range bands mentioned, LOS vague
**Needed for**: Any ranged combat

**What's Missing**:
- [ ] **Hex counting**
  - Range 1 = adjacent only?
  - Range 2-3 = Close (stated)
  - Do you count the hex you're on? (No, standard hex rules)
- [ ] **Line of Sight blocking**
  - What terrain blocks LOS completely?
  - What provides partial cover?
  - Elevated terrain advantage?
- [ ] **Firing arcs**
  - Can you shoot in any direction, or only front-facing?
  - Shoulder cannons have "Front-Right only" arc (example given)
  - Need standard rules
- [ ] **Height/Elevation**
  - Flying units? (Jump jets mentioned)
  - Shooting up/down hills?
  - Does height grant bonuses?

**Needs Diagram + Rules**:
- Visual hex map showing range counting
- Visual showing LOS blocking (terrain examples)
- Firing arc diagram (6 hex facings, which can you shoot?)

---

### 4. **Terrain System** ⚠️ HIGH PRIORITY

**Status**: Mentioned but not defined
**Needed for**: Any game with a map

**What's Missing**:
- [ ] **Terrain types**
  - Clear terrain (baseline)
  - Difficult terrain (Ironstrider's Rush ignores it - what is it?)
  - Water hexes (cooling, Heat removal mentioned)
  - Lava/Fire hexes (damage? Heat gain?)
  - Ice terrain (slippery? Movement penalty?)
  - Rubble/Ruins (cover?)
  - Forest (blocks LOS?)
  - Elevated hexes (height advantage?)
- [ ] **Terrain effects on movement**
  - Difficult terrain: +1 SP per hex? Half movement? Stop when entering?
- [ ] **Terrain effects on combat**
  - Cover bonuses (+1 Defense? -1 to hit?)
  - Hazard damage (lava = 1 damage per turn standing in it?)
- [ ] **Destructible terrain**
  - Can Assault Caskets destroy walls/forests?
  - Environmental attacks ("Seismic Slam" creates rubble?)

**Needs Entire Section**: "Terrain & Environmental Rules"

---

### 5. **Turn Structure & Action Economy** ⚠️ HIGH PRIORITY

**Status**: Partially described (card-anatomy.md:265-289)
**Needed for**: Playing a single turn

**What's Missing**:
- [ ] **Simultaneous vs Sequential play**
  - Planning Phase: "All players secretly choose 1 card" (line 266)
  - Do you play ONLY 1 card per turn? Or multiple?
  - Current description says "choose 1 card, reveal, resolve"
  - But SP system implies you play multiple cards (Scout has 5 SP, most cards cost 1-3 SP)
- [ ] **Free actions**
  - Warden's Pivot is "free action" (0 SP)
  - Can you play multiple free actions per turn?
  - Can you play free action + SP actions?
- [ ] **Reactive/Interrupt timing**
  - Defensive cards have Initiative [—] (reactive)
  - When exactly can you play them?
  - Opponent declares attack → You respond before resolution?
- [ ] **Round vs Turn terminology**
  - Is a "round" = all players act once?
  - Is a "turn" = one player's activation?
  - Inconsistent usage in docs
- [ ] **End of round effects**
  - "Remove temporary effects, reduce Heat (if applicable)" - when does Heat reduce naturally?
  - Passive cooling rules?

**MAJOR CLARIFICATION NEEDED**:

**Option A: Card-Based Turns** (current description)
- Each player plays 1 card per turn
- Reveal simultaneously, resolve by initiative
- Repeat until round ends (6 turns per round? Until SP exhausted?)

**Option B: SP-Based Turns** (implied by SP system)
- Each player has 1 turn per round
- On your turn, spend SP to play multiple cards until you're out of SP or choose to stop
- Play proceeds clockwise/initiative order

**These are COMPLETELY DIFFERENT GAMES.** Must choose one.

---

### 6. **Campaign Progression System** ✅ COMPLETE (with gaps)

**Status**: Core systems complete — see [settlement-mechanics.md](settlement-mechanics.md)
**Needed for**: Campaign mode

**What's Complete**:
- [x] **Workshop/Upgrade System** — See settlement-mechanics.md:44-69
  - Credits earn rate (100 for primary objective, 50 for secondary) ✅
  - Building costs, equipment prices, repair costs defined ✅
  - 14 buildings across 3 tiers + 6 faction-specific buildings ✅
  - Starting credits: Implied as 100-150 (1-2 missions worth)
- [x] **Settlement/Base Building** — See settlement-mechanics.md:70-275
  - Full building system with progression tiers ✅
  - Buildings provide passive bonuses, special actions, and unlocks ✅
  - Resource management (Credits, Scrap, Population, Morale) ✅
- [x] **Story Beats/Narrative Structure** — Partial
  - Settlement Event table (d20 random events) ✅
  - Faction reputation system — See [faction-relationships.md](faction-relationships.md) ✅
  - Resonance Engine doomsday clock — See [resonance-engine-mechanics.md](resonance-engine-mechanics.md) ✅
  - Multiple ending variations based on faction/Engine choices ✅

**What's Still Missing**:
- [x] **Pilot Experience/Leveling** — ✅ COMPLETE — **See [pilot-scars-traits.md](pilot-scars-traits.md)**
  - 80+ Scar entries across 4 categories (Physical, Corruption, Trauma, Combat) ✅
  - Acquisition rules defined (1 per 3 missions + traumatic events) ✅
  - Trauma/disorder system implemented (Kingdom Death-style) ✅
  - Faction-specific Scar tables included ✅
- [x] **Injury/Scarring Tables** — ✅ COMPLETE — **See [pilot-scars-traits.md](pilot-scars-traits.md)**
  - Full Physical Scars table with mechanical effects ✅
  - Example: "Shattered Leg" = permanent -1 movement ✅
  - Mixed with temporary injuries from damage-system.md ✅
- [x] **Loot System** — ✅ COMPLETE — **See [loot-tables.md](loot-tables.md)**
  - 4 rarity tiers with full item lists ✅
  - Specialized tables (Abominations, NPCs, Sibarian Wastes) ✅
  - Faction trade goods and crafting recipes ✅
- [ ] **Campaign Map/Mission Selection** — Not designed
  - Linear missions 1→15? Branching paths? Open map?
  - Mission unlock conditions?
  - Story gating vs player choice?

**Recommended Next Steps**:
1. Create "Pilot Scar & Injury Tables" document (HIGH PRIORITY)
2. Design campaign mission structure (MEDIUM PRIORITY)

---

### 7. **Equipment Catalog** ⚠️ MEDIUM PRIORITY

**Status**: Examples given, full catalog missing
**Needed for**: Deck construction, gear choices

**What's Missing**:
- [ ] **Baseline equipment list**
  - At least 10-15 weapons for playtest
  - Melee: Longsword, Greatsword, Hammer, Axe, Spear, Dagger
  - Ranged: Bow, Crossbow, Rifle (relic tech), Pistol
  - Shields: Buckler, Tower Shield, Great Shield
  - Relic examples: Jump Jets, Repair Kit, Ammo Pouch
- [ ] **Equipment stats table**
  | Equipment | Type | Cards Added | SP Range | Weight Classes | Cost (Campaign) |
  |-----------|------|-------------|----------|----------------|-----------------|
  | Faithkeeper Longsword | Right Arm | 4 | 1-2 | Any | 100 Credits |
- [ ] **Source Conduit spell schools**
  - Fire school (example given)
  - Ice, Lightning, Void, Nature schools?
  - 5 cards per school
- [ ] **Racial unique equipment**
  - Elven living weapons
  - Dwarven runeforged gear
  - Orcish scrap variants
  - Undead necrotech
  - Fae glamour items

**Needs Document**: "Equipment Catalog & Card Database"

---

### 8. **Monster/AI Bestiary** ⚠️ MEDIUM PRIORITY

**Status**: 3 examples given (Shrieking Colossus, Carrion Swarm, Corrupted Casket)
**Needed for**: Campaign/Raid modes

**What's Missing**:
- [ ] **Monster stat blocks**
  - HP, Armor, Movement, Deck Size
  - Special abilities
  - Weak points (for targeting)
- [ ] **AI Behavior Decks**
  - 15-20 cards per monster (stated)
  - Need full decks for at least 5 monsters
- [ ] **Monster difficulty ratings**
  - Minion (1-2 players can handle)
  - Elite (challenging for full party)
  - Boss (raid-level threat)
- [ ] **Loot tables**
  - What do monsters drop when defeated?
  - Credits, equipment, Soulstone fragments?
- [ ] **Void-spawn variants**
  - Abominations from different Void rifts
  - Taint-corrupted wildlife
  - Rogue Caskets (fallen pilots)

**Needs Document**: "Monster Bestiary & AI System"

---

### 9. **Mission Deck Templates** ⚠️ LOW PRIORITY

**Status**: Concept described, no actual mission cards
**Needed for**: Skirmish mode, Campaign variety

**What's Missing**:
- [ ] **Mission objective cards** (10-12 per deck, stated)
  - Primary objectives (examples given)
  - Secondary objectives (examples given)
  - Hidden agendas (examples given)
  - Need 30-50 actual cards designed
- [ ] **Event cards** (environmental hazards, twists)
  - "Sudden Sandstorm" - all ranged attacks -1 to hit
  - "Void Rift Opens" - spawn 1d3 Abominations
  - "Soulstone Cache Discovered" - control objective for bonus loot
- [ ] **Map layouts**
  - 5-10 pre-designed hex maps for common scenarios
  - Deployment zones marked
  - Terrain features placed
  - Objective locations

**Needs Document**: "Mission Deck & Scenario System"

---

### 10. **Victory Point System (Arena/Skirmish)** ⚠️ LOW PRIORITY

**Status**: Mentioned but not detailed
**Needed for**: Non-elimination victory

**What's Missing**:
- [ ] **VP values**
  - Kill enemy Casket: 5 VP (stated)
  - Destroy component: 2 VP (stated)
  - Control objective hex: 3 VP (stated)
  - Other VP sources?
- [ ] **VP tracking**
  - Public or hidden?
  - Announced when earned or counted at end?
- [ ] **VP victory threshold**
  - Arena: First to 10-15 VP (stated)
  - Skirmish: First to 20 VP (stated)
- [ ] **Tiebreakers** (listed in CoreDesign.md:942-948) ✓

**Minor issue, but needs clarity.**

---

## Missing Polish/Flavor Elements

### 11. **Component Breakdown Visuals**

**Status**: Text descriptions only
**Needed for**: New player onboarding

**What's Missing**:
- [ ] Player mat layout diagram
- [ ] Casket component diagram (where is Right Arm? Chassis? Legs?)
- [ ] Hex facing diagram (which facings are "front arc"? "rear"?)
- [ ] Card layout visual (currently ASCII art only)

**Needs**: Graphic design, even simple diagrams

---

### 12. **Quick Reference Sheet**

**Status**: Doesn't exist
**Needed for**: Table reference during play

**What's Missing**:
- [ ] One-page combat resolution flowchart
- [ ] SP cost quick reference (Movement: 1 SP per hex, Attack: varies, Vent Heat: 2 SP)
- [ ] Heat threshold effects table
- [ ] Taint corruption track
- [ ] Strain table summary (per weight class)

**Needs**: 1-2 page printable reference

---

### 13. **Glossary/Index**

**Status**: Doesn't exist
**Needed for**: Rules clarity

**What's Missing**:
- [ ] Alphabetical term definitions
  - Casket, Soulstone, SP, Heat, Taint, Strain, Initiative, etc.
- [ ] Keyword index
  - Universal, Tainted, Forbidden, Corruption, Relic, Tech, Reactive, etc.

**Needs**: 2-3 page glossary

---

### 14. **Example of Play**

**Status**: Doesn't exist
**Needed for**: Teaching new players

**What's Missing**:
- [ ] Complete turn example (Player A vs Player B)
  - Show deck, hand, board state
  - Walk through Planning → Reveal → Resolution → Damage → Draw
  - Show decision-making process
- [ ] Example combat resolution
  - Attack from rear, defender plays Unyielding Bulwark, calculate final damage
- [ ] Example reshuffle with Damage cards
  - Show before/after deck composition

**Needs**: 2-4 page walkthrough with visuals

---

## Design Decisions That Need To Be Made

### A. Turn Structure Clarification (CRITICAL)
**Decision**: Card-based turns (1 card/turn, GKR-style) OR SP-based turns (spend pool, deck-builder-style)?

**Recommendation**: **SP-based turns**
- Play multiple cards per turn until you run out of SP or pass
- Better supports deck-building identity
- Allows "combo turns" and strategic chaining
- Simultaneous reveal would be clunky with multiple cards

---

### B. Hit Roll System (CRITICAL)
**Decision**: Automatic hits OR dice-based resolution?

**Recommendation**: **Hybrid**
- Melee: Auto-hit (you're adjacent, hard to miss)
- Ranged: Roll 1d6, 4+ hits (modified by range/cover)
- Magic: Auto-hit (magic seeks target)
- Keeps resolution fast but adds tension to ranged attacks

---

### C. Defense/Armor Distinction (CRITICAL)
**Decision**: One stat or two separate systems?

**Recommendation**: **Defense as damage reduction**
- Base Defense = 0 for all classes
- Shields add Defense (Tower Shield: +2 Defense)
- Defense reduces incoming damage (min 1)
- Simple, intuitive, no separate armor stat needed

---

### D. Deck Size: Fixed or Range? (HIGH PRIORITY)
**Decision**: Scout is 20-25 cards - is that player choice or variance based on equipment?

**Recommendation**: **Fixed base + equipment variance**
- Scout base: 20 cards (10 Universal + 10 equipment)
- Each piece of equipment adds fixed cards (Longsword: +4, Shield: +3, Relic: +3)
- Final deck size = base 20 + equipment (usually 23-25)
- Predictable, easy to balance

---

### E. Card Copy Limits (HIGH PRIORITY)
**Decision**: Can I have multiple copies of the same card?

**Recommendation**: **Max 2 copies per card**
- Weapons add 3-4 unique cards (no duplicates within the weapon)
- You can equip 2 longswords (one in each hand) = 2 copies of "Faithful Thrust"
- Prevents deck from being 15 copies of best card
- Encourages variety

---

### F. Passive Heat Reduction (MEDIUM PRIORITY)
**Decision**: Does Heat reduce at end of round automatically?

**Recommendation**: **No passive cooling**
- Heat persists until you actively vent it
- Creates tension (Heat is a real threat)
- Manual venting (Breathe the Core, Support allies, water hexes) is meaningful choice
- Exception: End of mission, all Heat clears

---

### G. Campaign XP System (MEDIUM PRIORITY)
**Decision**: Do pilots level up, or is progression purely gear?

**Recommendation**: **Hybrid: Gear + Pilot Traits**
- Progression is mostly gear (Workshop purchases)
- Pilots earn 1 "Scar" per 3 missions (permanent trait)
  - Positive scars: "Veteran Instincts" (+1 hand size)
  - Negative scars: "Shattered Leg" (-1 movement)
  - Mixed scars: "Voidtouched" (+1 SP, start at 1 Taint)
- Max 5 scars per pilot
- Tells a story through mechanical changes

---

## Priority Roadmap

### **Phase 1: Minimum Viable Playtest** (CRITICAL - DO FIRST)
1. ✅ Finalize turn structure (SP-based turns)
2. ✅ Define combat resolution (hit rolls, defense, damage)
3. ✅ Create deck construction rules
4. ✅ Design 10 basic weapons (catalog start)
5. ✅ Create 1 example scenario (Arena 1v1)
6. ✅ Write example of play
7. ✅ Create quick reference sheet

**Goal**: Playable prototype for testing core loop

---

### **Phase 2: Expansion & Variety** (HIGH PRIORITY)
8. ✅ Terrain system (6-8 terrain types)
9. ✅ Range/LOS rules (diagrams + examples)
10. ✅ Equipment catalog (30+ items)
11. ✅ Monster bestiary (10 enemies with AI decks)
12. ✅ Mission deck (30 objective/event cards)

**Goal**: Full game modes playable (Arena, Campaign, Raid, Skirmish)

---

### **Phase 3: Campaign & Progression** (MEDIUM PRIORITY)
13. ✅ Workshop system (prices, upgrade tree)
14. ✅ Pilot traits/scars system
15. ✅ Campaign map/mission structure (15 missions)
16. ✅ Settlement building rules
17. ✅ Story beats & narrative events

**Goal**: Full campaign experience (10-15 sessions)

---

### **Phase 4: Polish & Production** (LOW PRIORITY)
18. ✅ Graphic design (player mats, card templates)
19. ✅ 3D models (core Casket + 5 weapons)
20. ✅ Final art direction
21. ✅ Kickstarter prep materials
22. ✅ Community submission guidelines

**Goal**: Production-ready game

---

## Immediate Next Steps (Prioritized)

### THIS WEEK:
1. **Decide turn structure** (card-based vs SP-based) - CRITICAL
2. **Write combat resolution rules** (2-3 pages, detailed)
3. **Create deck construction template** (1 page per weight class)
4. **Design 5 weapons** (Longsword, Greatsword, Bow, Shield, Hammer)

### NEXT WEEK:
5. **Design 1 Arena scenario** (map layout, deployment, victory condition)
6. **Write example of play** (2-3 turns, full walkthrough)
7. **Create quick reference sheet** (1-2 pages)
8. **First playtest** (you + 1 friend, 1v1 Arena match)

### MONTH 1:
9. Iterate based on playtest feedback
10. Expand equipment catalog to 15 items
11. Design terrain system
12. Create 3 monster AI decks

---

*Once Phase 1 is complete, you'll have a playable prototype. Everything else builds on that foundation.*
