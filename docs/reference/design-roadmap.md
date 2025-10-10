# Design Roadmap: From Here to Playtest
## Penance: Absolution Through Steel

**Current Status**: 85% Ready for Alpha Playtest
**Date**: October 10, 2025

---

## Philosophy: Build Minimum Viable Playtest First

**Goal**: Get to **first playable match** in 3-5 days of focused work.

**Why this matters**:
- Theory vs Practice: Systems that sound good may not play well
- Iteration speed: Fast playtest → Quick feedback → Rapid improvement
- Motivation: Playing your own game is incredibly motivating
- Scope control: Don't design content you'll throw away after testing

**The Plan**: Build **ONE complete game mode** (Arena 1v1) with **TWO complete factions**, then expand.

---

## Phase 1: Minimum Viable Playtest (3-5 Days)

**Goal**: First playable Arena match (Church vs Dwarves, 1v1)

### Day 1: Combat Foundations (4-5 hours)

#### 1.1 Turn Structure Document ✅ CRITICAL
**Time**: 1.5 hours
**File**: `turn-structure-final.md`

**Content**:
```markdown
## Turn Structure (SP-Based)

### Game Round
1. Initiative (all players roll 1d6, highest goes first)
2. Player turns in order
3. Round ends when all players pass

### Player Turn Structure
PHASE 1: Refresh
- Restore SP to maximum
- Check Heat (if 5+, roll Strain)

PHASE 2: Action Phase
- Play cards from hand (costs SP)
- Move (1 SP per hex)
- Attack, defend, utility
- Continue until out of SP or pass

PHASE 3: Draw Phase
- Draw to hand size (6 cards)
- If deck empty: Reshuffle + add 1 Damage card

PHASE 4: End Turn
- Announce "Done"
- Next player goes

### Reactive Cards
- Played during OPPONENT'S turn
- 0 SP cost, [—] Initiative keyword
- Interrupt resolution (defense, counters)
```

**Why this format**: Simple phases, clear timing, no ambiguity.

---

#### 1.2 Range & Line of Sight ✅ CRITICAL
**Time**: 2 hours
**File**: `range-and-los-final.md`

**Content**:
- Hex range counting (visual diagram: Range 1-6 from center)
- LOS blocking rules:
  - **Blocks LOS**: Walls, large terrain
  - **Provides Cover (+1 Defense)**: Forests, rubble, other Caskets
  - **Transparent**: Water, ice, open ground
- Firing arcs:
  - Front 180° (3 front-facing hexes) = can attack
  - Rear 180° (3 rear-facing hexes) = cannot attack (must pivot first)
- Elevation rules:
  - Higher ground: +1 damage
  - Ignore cover if 2+ levels above target

**Include**: 3-4 hex diagrams showing:
1. Range counting (1, 2, 3, 4+ hexes)
2. LOS through forest (cover, not blocked)
3. LOS blocked by wall
4. Firing arc (which hexes you can attack)

**Tools**: ASCII diagrams or simple grid sketches (can upgrade to graphics later)

---

#### 1.3 Quick Reference Sheet ✅ HIGH PRIORITY
**Time**: 1 hour
**File**: `quick-reference-sheet.md`

**Content** (1-page printable):

**Left Column: Turn Structure**
- Refresh → Action → Draw → End
- SP costs: Movement (1/hex), Vent (2)

**Center: Combat Resolution**
```
ATTACK
1. Play card, spend SP
2. Check range/LOS
3. Calculate damage
4. Defender discards cards from deck
5. Check for Component Damage

COMPONENT DAMAGE
- Primary Weapon cards discarded = Component Damage
- 3 Damage = Destroyed
- Right Arm: Lose Primary Weapon cards from hand
- Left Arm: Lose Secondary Equipment
- Legs: +1 SP movement cost
- Head: -1 ranged attacks
- Chassis: -1 SP max
```

**Right Column: Modifiers**
- Facing: Rear +2 dmg/-2 Def, Side +1/-1
- Cover: +1 Defense
- Heat Zones: 0-4 Safe, 5+ Danger (Strain)

**Bottom: Strain Table**
| Roll | Effect |
|------|--------|
| 1-5  | +1 Heat |
| 6-8  | -1 SP this turn |
| 9-11 | Take 2 damage |
| 12+  | Component malfunction |

**Format**: Markdown table format, easy to print/reference

---

### Day 2: First Faction Complete (4-5 hours)

#### 2.1 Church of Absolution - Complete Deck ✅
**Time**: 3 hours
**File**: `faction-deck-church-complete.md`

**Build out the full 30-card deck with EXACT card text**:

**Universal Core** (10 cards) - Write full rules text:
- Desperate Lunge: "1 SP. Move up to 2 hexes."
- Brace for Impact: "0 SP, Reactive. Reduce next damage by 2."
- Emergency Vent: "2 SP. Remove 3 Heat."
- (Continue for all 10)

**Primary Weapon: Penitent Blades** (12 cards):
- Blood Offering × 2: "0 SP. Discard 2 cards from your deck (self-harm). Your next attack this turn: +3 damage, ignore 1 Armor."
- Faithful Thrust × 3: "2 SP. Range: Melee. Deal 4 damage. If attacking from rear: +2 damage."
- (Continue for all 12)

**Secondary Equipment** (design 4 options, 6 cards each):
- Buckler Shield (6 cards)
- Tower Shield (6 cards)
- Repair Kit (6 cards)
- Holy Pistol (6 cards)

**Faction Tactics** (5 options, player chooses 2):
- Righteous Fury: "Passive. Each enemy Casket destroyed this mission: +1 damage to all attacks permanently."
- Flagellant's Zeal: "4 SP. Discard 5 cards. Gain 5 SP immediately."
- Last Rites: "0 SP, Reactive. When ally within 3 hexes is defeated: Recover 5 cards from your discard."
- Absolution: "5 SP. Remove all Heat. Recover 3 cards from discard. Gain 1 Taint."
- Crusader's Vow: "Passive. While you have 20+ cards in deck: All attacks cost -1 SP."

**Pilot Wound Deck** (10 cards):
- Design specific wound effects for Church pilots
- Minor Injuries (5): Cracked rib, concussion, broken finger, internal bleeding, dislocated shoulder
- Severe Injuries (3): Shattered hand (-2 SP permanent), spinal trauma (movement +1 SP permanent), ruptured organ (start missions at -5 HP)
- Trauma (2): PTSD (cannot attack from rear), Martyr Complex (must attack every turn or take 2 damage)

**Why start with Church**: Already have examples, thematically clear, good baseline faction.

---

#### 2.2 Dwarven Clans - Complete Deck ✅
**Time**: 2 hours
**File**: `faction-deck-dwarves-complete.md`

**Same structure as Church, but different playstyle**:

**Primary Weapon: Runic Warhammer** (12 cards):
- Emphasis on armor-piercing, defensive buffs, redundancy
- Example cards:
  - Crushing Blow × 3: "3 SP. Deal 6 damage. Ignore 2 Armor."
  - Rune of Protection × 2: "2 SP. Gain +2 Defense until end of round."
  - Emergency Override × 2: "1 SP. If a Component is destroyed this turn, prevent it (once per mission)."

**Secondary Equipment**:
- Great Shield (heavy defense)
- Backup Hammer (redundancy theme)
- Engineering Kit (repair mid-battle)
- Shoulder Cannon (ranged option)

**Faction Tactics**:
- Runic Shielding: "Passive. When you would take 5+ damage: Reduce by 2."
- Forge Fury: "3 SP. Deal damage equal to your current Heat."
- Unbreakable: "2 SP. Until end of round, Component Damage cannot destroy Components."
- Overclock: "4 SP. Gain +3 SP this turn. Gain 3 Heat."
- Grudge Bearer: "Passive. Each time a Component is destroyed: +2 damage to all attacks vs that enemy."

**Pilot Wound Deck**:
- Dwarven-specific wounds (forge burns, metal shrapnel, ale withdrawal)

**Why Dwarves second**: Contrasting playstyle (defensive tanky vs Church aggressive), easy to balance against.

---

### Day 3: Arena Scenario + Example of Play (4-5 hours)

#### 3.1 Arena Scenario #1: "The Proving Grounds" ✅
**Time**: 2 hours
**File**: `scenario-arena-01-proving-grounds.md`

**Content**:
```markdown
## Scenario: The Proving Grounds

### Map Layout (12×12 hex grid)
- 2 deployment zones (opposite corners, 3 hexes each)
- Center: Raised platform (elevated 1 level, +1 damage from here)
- 4 rubble piles (provide cover, +1 Defense)
- 2 water hexes (remove 2 Heat per turn standing in them)
- 2 walls (block LOS, cannot cross)

### Deployment
- Each player places Casket in deployment zone
- Church deploys first (attacker), Dwarves second (defender)

### Victory Conditions
- Primary: Reduce enemy Casket to 0 HP (deck empty)
- Secondary: Destroy 3+ enemy Components
- Alt: Kill enemy pilot (10 Wounds)

### Special Rules
- Arena match (no reinforcements, no retreat)
- First blood: First Casket to deal damage gains +1 SP for 1 turn
- Crowd favor: Destroying Component from rear grants 1 free card draw

### Pre-Built Decks
- Church Confessor (Light, 6 SP)
  - Primary: Penitent Blades
  - Secondary: Buckler Shield
  - Tactics: Blood Offering + Righteous Fury

- Dwarven Ironclad (Heavy, 4 SP)
  - Primary: Runic Warhammer
  - Secondary: Great Shield
  - Tactics: Runic Shielding + Unbreakable
```

**Include**: ASCII map of arena layout

---

#### 3.2 Example of Play Walkthrough ✅
**Time**: 2-3 hours
**File**: `example-of-play-arena-match.md`

**Content**: Full 4-5 turn walkthrough showing:

**Setup Phase**:
- Both players shuffle 30-card decks
- Draw 6 cards each
- Roll initiative: Church rolls 5, Dwarves roll 3 → Church goes first

**Turn 1 (Church)**:
- REFRESH: 6 SP
- ACTION: Play Desperate Lunge (1 SP) → Move 2 hexes toward center
- ACTION: Play Survey the Field (1 SP) → Draw 1 card
- ACTION: Move 2 hexes (2 SP) → Now at center platform
- DRAW: Draw 2 cards (hand back to 6)
- END TURN (2 SP unused)

**Turn 1 (Dwarves)**:
- REFRESH: 4 SP
- ACTION: Play Advance (2 SP) → Move 2 hexes toward center, +1 Defense this turn
- ACTION: Play Sensor Sweep (1 SP) → Reveal 1 card in enemy hand (sees Blood Offering)
- DRAW: Draw 2 cards
- END TURN (1 SP unused)

**Turn 2 (Church) - FIRST COMBAT**:
- REFRESH: 6 SP
- Heat check: 0 Heat (safe)
- ACTION: Rotate to face Dwarves (free action)
- ACTION: Play Blood Offering (0 SP) → Discard 2 cards from deck (now at 28 HP)
- ACTION: Play Faithful Thrust (2 SP) → Attack, Range: Melee
  - Church is on elevated platform: +1 damage
  - Blood Offering active: +3 damage, ignore 1 Armor
  - Attacking from front: No facing bonus
  - **Total: 4 (base) +1 (elevation) +3 (Blood Offering) = 8 damage**
- RESOLUTION: Dwarves discard top 8 cards
  - Cards discarded: 3 Universal, 3 Primary (Warhammer), 1 Secondary, 1 Tactic
  - **3 Primary Weapon cards → 3 Component Damage on Right Arm**
  - **RIGHT ARM DESTROYED!**
  - Dwarves immediately discard all Runic Warhammer cards from hand (3 cards)
- DRAW: Draw 4 cards
- END TURN

**Turn 2 (Dwarves) - DESPERATE RESPONSE**:
- REFRESH: 4 SP
- Dwarves now at 22 HP (30 - 8)
- Hand: Only 3 cards (lost 3 Primary Weapons)
- Draw Phase happens AFTER actions, so hand is weak
- ACTION: Play Rune of Protection (2 SP) from earlier turn → +2 Defense until end of round
- ACTION: Play Retreat (2 SP) → Move 4 hexes away, cannot attack this turn
- DRAW: Draw 6 cards (hand maxed out)
- END TURN

**Analysis**:
- Church used self-harm (Blood Offering) for massive alpha strike
- Dwarves lost Primary Weapon on Turn 2 → must fight with Secondary + Universal only
- This is the **brutal, desperate combat** we want
- Dwarves now need to rely on defensive play and Secondary Equipment

**Continue for 2-3 more turns** showing:
- Dwarven counterattack using Great Shield bashes
- Church pushing advantage but taking Heat damage
- Component destruction spiral
- Potential pilot damage when Casket HP gets low

**Why this is critical**: Shows players HOW the game actually flows. Theory → Practice.

---

### Day 4: Playtesting & Iteration (3-4 hours)

#### 4.1 First Solo Playtest ✅
**Time**: 2 hours
**Process**:
1. Print quick reference sheet
2. Lay out both decks physically (or use TTS if digital)
3. Play through Arena scenario
4. **Take notes constantly**:
   - What was confusing?
   - What took too long?
   - What was boring?
   - What felt awesome?
5. Record final game state (who won, how many turns, HP remaining)

**Expected issues**:
- SP costs might be unbalanced (too cheap/expensive)
- Component destruction might trigger too fast/slow
- Hand size might feel too small/large
- Damage values might be too high/low

**This is GOOD**: Finding problems early is the goal.

---

#### 4.2 Rules Clarification Pass ✅
**Time**: 1-2 hours
**Process**:
1. Review all questions/confusion from playtest
2. Update documents with clarifications
3. Add FAQ section to quick reference

**Example clarifications**:
- "Can I play multiple 0 SP cards in one turn?" → Yes
- "When exactly does Component Damage trigger?" → When Primary Weapon cards discarded
- "Can I draw cards mid-turn?" → Only from card effects, not automatically

---

### Day 5: Second Playtest (Optional)
**Time**: 2 hours

Play again with updated rules. Should feel smoother.

If it feels good → **You're ready for external playtest** (friend, online community).

---

## Phase 2: Expand Content (Week 2)

**Goal**: Add variety without breaking what works.

### Priority 1: More Factions (Choose 2-3)

**Recommended next factions**:
1. **Undead Court** (unique resurrection mechanic)
2. **Elven Remnants** (regeneration/nature theme)
3. **Fae Courts** (teleportation/trickery)

**Time per faction**: 3-4 hours each

**Process** (repeat for each):
1. Design Primary Weapon (12 cards) with unique mechanic
2. Design 4 Secondary Equipment options (6 cards each)
3. Design 5 Faction Tactics
4. Create Pilot Wound Deck with faction flavor
5. Write faction-specific Component Destruction effects

**Example: Undead Court**
- Primary: Necro-Scythe (drain life, reanimate)
- Unique Mechanic: When defeated, roll 1d6. On 4+, return with 10 HP
- Component Destruction: Undead don't care (missing arm? Fine, use other one)

---

### Priority 2: Equipment Expansion

**Goal**: 15 total Secondary Equipment options (currently have ~8)

**Add**:
- Melee: Spear (reach), Dual Daggers (fast attacks)
- Ranged: Crossbow (armor-piercing), Rifle (long range)
- Shields: Riot Shield (reactive defense)
- Relics: Grappling Hook (mobility), Flare Gun (utility), Smoke Grenades (concealment)

**Time**: 4-5 hours for 7 new equipment sets (6 cards each = 42 cards total)

---

### Priority 3: Terrain System

**Goal**: 6-8 terrain types with clear rules

**Terrain Types**:
1. **Clear** (baseline, no effect)
2. **Difficult** (costs +1 SP per hex, slows movement)
3. **Water** (remove 2 Heat per turn standing here)
4. **Forest** (provides cover +1 Defense, blocks LOS)
5. **Rubble** (provides cover +1 Defense, difficult terrain)
6. **Wall** (blocks LOS, cannot cross)
7. **Elevated** (+1 damage when attacking from here)
8. **Hazard** (lava, acid - take 1 damage per turn)

**File**: `terrain-system-complete.md`

**Time**: 2 hours

---

### Priority 4: More Scenarios

**Goal**: 5 Arena scenarios with different maps/objectives

**Scenario Ideas**:
1. Proving Grounds (already done)
2. King of the Hill (control center hex for 3 turns)
3. Assassination (kill enemy pilot, not Casket)
4. Gauntlet (waves of weak enemies)
5. Tag Team (2v2 battle)

**Time**: 1-2 hours per scenario (design map, write special rules)

---

## Phase 3: Campaign Mode (Week 3-4)

**Goal**: Playable 5-mission campaign with progression

### Priority 1: Mission Structure

**Campaign Flow**:
```
Mission 1: Tutorial (vs easy AI)
→ Workshop (spend credits, repair)
→ Mission 2: First real threat
→ Workshop
→ Mission 3: Boss encounter (Sister Vex)
→ Workshop (unlock new buildings)
→ Mission 4: Faction war mission
→ Workshop
→ Mission 5: Finale (Engine assault)
```

**Time**: 6-8 hours to design 5 missions

---

### Priority 2: Settlement Integration

**Connect existing settlement-mechanics.md to gameplay**:

**After each mission**:
1. Earn Credits (100 for primary, 50 for secondary)
2. Roll on Settlement Event table (d20)
3. Spend Credits:
   - Repair Caskets (10 Credits per 5 HP restored)
   - Buy equipment (weapons, shields, relics)
   - Build settlement buildings (unlock bonuses)
4. Pilot recovery:
   - Roll for Pilot Scars (if took 5+ Wounds)
   - Downtime activities (train, research, socialize)

**Time**: 3-4 hours to write Workshop phase rules

---

### Priority 3: AI Opponents

**Design 3-5 AI behavior decks** (enemies for campaign):

**AI Types**:
1. Abomination (mindless, aggressive)
2. Rogue Casket (uses player cards, but simplified)
3. Boss (Sister Vex - already designed)

**AI Behavior Deck** (15-20 cards):
- Move toward nearest enemy
- Attack if in range
- Defend if attacked
- Special abilities (unique per AI)

**Time**: 2-3 hours per AI type

---

## Phase 4: Polish & Production (Month 2+)

**This is post-playtest refinement, not MVP.**

### Priority 1: Card Templates

**Design printable card layout**:
- Card name
- SP cost
- Type (Attack, Defense, Movement, etc.)
- Effect text
- Flavor text
- Faction symbol
- Card art placeholder

**Tools**: Figma, Canva, or Affinity Designer

**Time**: 4-6 hours for template design

---

### Priority 2: AI Art Generation

**Using ai-art-prompts.md**, generate actual Casket art:

**Priority assets**:
1. 2 Caskets per faction (Light + Heavy)
2. 5 Equipment visuals (Longsword, Shield, Warhammer, Pistol, Repair Kit)
3. Capsule cutaway (show interior)

**Tools**: Midjourney, Stable Diffusion, DALL-E 3

**Time**: 2-3 hours (AI generation is fast, iteration takes time)

---

### Priority 3: Tabletop Simulator Mod

**Export to TTS for online playtesting**:
- Import card images
- Create decks
- Set up hex board
- Add scripting for automated draw/discard

**Time**: 4-6 hours (if familiar with TTS modding)

---

## Critical Path Summary

### To First Playtest (3-5 Days):
1. ✅ Turn structure doc (1.5 hrs)
2. ✅ Range/LOS doc (2 hrs)
3. ✅ Quick reference (1 hr)
4. ✅ Church deck complete (3 hrs)
5. ✅ Dwarves deck complete (2 hrs)
6. ✅ Arena scenario (2 hrs)
7. ✅ Example of play (3 hrs)
8. ✅ First playtest (2 hrs)

**Total: ~16-20 hours** (doable in 1 week)

---

### To Full Game (4-6 Weeks):
**Week 1**: MVP playtest (above)
**Week 2**: Add 3 factions, equipment, terrain
**Week 3**: Campaign mode (5 missions)
**Week 4**: AI opponents, polish, second playtest
**Weeks 5-6**: Iteration, art, TTS mod

---

## Design Principles Moving Forward

### 1. Playtest Early, Playtest Often
- Don't design in a vacuum
- Get cards on table ASAP
- Player feedback > designer assumptions

### 2. Start Asymmetric, Balance Later
- Factions should feel DIFFERENT first
- Balance second
- Better to have 5 unique factions than 9 samey ones

### 3. Embrace Brutality
- Component destruction should hurt
- Pilot Wounds should be scary
- Death spiral should be inevitable (but dramatic)
- "Balanced" doesn't mean "fair" — it means "interesting choices"

### 4. Use What Exists
- You have 437 years of lore
- You have 36 Casket designs
- You have puppeteer capsules + leg-skimming
- **Use this identity in every card**

### 5. Mechanics Reinforce Theme
- Blood Offering = self-harm for power (Church theme)
- Runic Shielding = engineering redundancy (Dwarf theme)
- Every card should feel like that faction

---

## What I'd Do Right Now (Priority Order)

If I were you, here's my exact next steps:

### Tomorrow:
1. Write turn-structure-final.md (1.5 hrs)
2. Write range-and-los-final.md (2 hrs)
3. Start quick-reference-sheet.md (1 hr)

### Day 2:
4. Complete Church faction deck (3 hrs)
   - All 30 cards with exact text
   - 4 Secondary Equipment options
   - 5 Faction Tactics
   - 10 Pilot Wounds

### Day 3:
5. Complete Dwarves faction deck (2 hrs)
6. Write arena-scenario-01.md (2 hrs)

### Day 4:
7. Write example-of-play walkthrough (3 hrs)

### Day 5:
8. **PLAYTEST** (print cards, play it, take notes)
9. Iterate based on what broke

---

## Red Flags to Watch For

**During design**:
- ⚠️ Cards that say "Draw your entire deck" (broken)
- ⚠️ SP costs below 1 for attacks (too spammable)
- ⚠️ Component destruction triggering on first hit (too fast)
- ⚠️ Infinite combos (X card + Y card = repeat forever)

**During playtest**:
- ⚠️ Games ending in 2-3 turns (too fast)
- ⚠️ Games lasting 2+ hours (too slow)
- ⚠️ One faction wins 100% of the time (balance issue)
- ⚠️ Players get decision paralysis every turn (too complex)
- ⚠️ "I don't know what to do" moments (unclear rules)

---

## Success Metrics

**You'll know the game is ready when**:
- ✅ Games last 30-45 minutes (sweet spot)
- ✅ Both players had "oh shit" moments (drama)
- ✅ Component destruction happened 2-3 times (not too rare, not constant)
- ✅ At least 1 reshuffle occurred (deck cycling works)
- ✅ Players had meaningful choices every turn (not obvious optimal move)
- ✅ Someone said "one more game" after finishing (it's fun!)

---

**Final Thought**: You have an incredible foundation (GKR combat + KDM brutality + puppeteer horror). The hard creative work is done. What remains is **execution** — writing the specific cards, testing, iterating.

**You're 1 week away from playing your own game.**

Do it. You've earned this.
