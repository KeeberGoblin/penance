# Recommendations Summary
## Penance: Absolution Through Steel

**Version**: 0.1
**Last Updated**: October 9, 2025

---

## Executive Summary

You have an **excellent foundation** with strong thematic cohesion and innovative mechanics. The Tesla-inspired Cataclysm lore ("The Sundering") adds depth and gives each faction distinct motivations.

**What's Working:**
- ✅ Soul-Point push-your-luck economy
- ✅ Deck-as-health system
- ✅ Corruption/Taint progression
- ✅ Asymmetric racial abilities
- ✅ 3D printable modular Casket system
- ✅ Strong world-building foundation

**What's Missing:**
- ❌ Combat resolution mechanics (how do attacks actually work?)
- ❌ Deck construction rules (how do I build a legal deck?)
- ❌ Turn structure clarity (do I play 1 card or multiple per turn?)
- ❌ Equipment catalog (what can I actually equip?)
- ❌ Campaign progression system (how do I upgrade between missions?)

---

## Critical Decisions You Must Make (Before Playtesting)

### 1. Turn Structure: Card-Based vs SP-Based ⚠️ CRITICAL

**The Problem**: Your current docs are inconsistent.

**Option A: Card-Based (GKR-style)**
- Each player plays 1 card per turn
- Reveal simultaneously, resolve by initiative order
- Multiple rounds until game ends or someone passes
- SP is a "budget" limiting how many cards you can play across multiple turns

**Option B: SP-Based (Deck-builder style)** ⭐ RECOMMENDED
- Each player gets 1 turn per round
- On your turn, play cards spending SP until you're out or choose to stop
- Allows combos, chaining, strategic sequencing
- More in line with deck-building identity

**Recommendation**: **SP-Based Turns**
- Better fits deck-building genre
- Allows for tactical combo plays
- Simpler to teach ("you have X SP, spend it however you want")
- Supports "build your own turn" agency

---

### 2. Combat Resolution: Auto-Hit vs Dice Rolls ⚠️ CRITICAL

**The Problem**: Attack resolution isn't defined.

**Recommendation**: **Hybrid System**
```
MELEE ATTACKS: Auto-hit (adjacent = hard to miss)
RANGED ATTACKS: Roll 1d6, 4+ to hit
  - Modifiers: Long range -1, Cover -1, Rear attack +1
MAGIC SPELLS: Auto-hit (magic seeks target)
```

**Defense = Damage Reduction**
- Base Defense: 0 for all classes
- Shields/abilities add Defense
- Defense reduces incoming damage (minimum 1 damage always dealt)

**Why**: Fast resolution, minimal dice, tension where it matters (ranged combat).

---

### 3. Deck Size: Fixed or Variable? ⚠️ HIGH PRIORITY

**The Problem**: "Scout: 20-25 cards" - is that player choice or equipment variance?

**Recommendation**: **Fixed Base + Equipment Adds Cards**

**Example: Scout Deck Construction**
```
Base Deck: 20 cards
├─ Universal Cards: 10 (mandatory)
└─ Equipment Cards: 10 (starting pool)

Equipped Gear Adds Cards:
├─ Right Arm (Longsword): +4 cards
├─ Left Arm (Buckler): +2 cards
└─ Relic (Jump Jets): +3 cards

Final Deck Size: 20 + 9 = 29 cards
```

**Limits**:
- Scout can equip max 10-12 equipment cards (ends up 20-25 final size) ✓
- Heavy can equip max 25-30 equipment cards (ends up 30-35 final size) ✓
- No more than 2 copies of any single card

---

### 4. Campaign Progression: Gear Only or Pilot XP? ⚠️ MEDIUM PRIORITY

**Recommendation**: **Hybrid (Gear + Scars)**

**Workshop System** (Gear Progression):
- Earn Credits per mission (100 primary, 50 secondary, 25 hidden agenda)
- Spend Credits at Workshop:
  - New equipment: 100-500 Credits
  - Repairs: 50/150/500 Credits (minor/major/full)
  - Soulstone purification: 200 Credits per Taint removed

**Pilot Scars System** (Character Progression):
- Earn 1 Scar every 3 missions completed
- Scars are permanent traits (good, bad, or mixed)
  - **Veteran's Instinct**: +1 hand size
  - **Shattered Leg**: -1 movement permanently
  - **Voidtouched**: +1 SP Safe Zone, start missions at 1 Taint
- Max 5 Scars per pilot (retire or die after that)

**Why**: Gear provides power curve, Scars tell emergent stories.

---

## Lore Integration: The Sundering

### What You Now Have (Added in world-lore.md)

**The Cataclysm Event**:
- Nikolas Theslar's Resonance Engine (Tesla-inspired experiment)
- Attempted wireless energy broadcast
- Accidentally tore open Void rift
- EMP-like pulse destroyed all technology
- Magical radiation flooded world
- 100 years later: fragmented realms, Casket warfare

**Why It's Great**:
- Explains Soulstones (crystallized Void energy)
- Explains Taint/Corruption (Void exposure)
- Explains lack of advanced tech (Cataclysm destroyed it)
- Explains medieval-fantasy aesthetic (rebuilt from ruins)
- Explains faction conflict (no central authority post-collapse)

**Each Faction Has Different Interpretation**:
- Humans (Church): Divine punishment, seek absolution
- Elves: Ecological murder, heal the world
- Dwarves: Engineering failure, fix what broke
- Orcs: Who cares, world's always broken
- Undead: Death boundary shattered, we evolved
- Fae: Dimensions merged, opportunity for us
- Draconids: This happened before, cycle repeats

**Central Mystery**: What are Soulstones really? (Each theory is partially true - the Void doesn't follow singular rules)

---

## Priority Action Items

### **THIS WEEK** (Critical Path to Playtest)

1. **Decide and document turn structure** ⚠️ CRITICAL
   - Recommendation: SP-based turns
   - Write 1-page "Turn Structure" section for CoreDesign.md

2. **Write combat resolution rules** ⚠️ CRITICAL
   - Hit rolls (melee auto, ranged 4+, magic auto)
   - Defense = damage reduction
   - Step-by-step flowchart
   - Add to CoreDesign.md (2-3 pages)

3. **Create deck construction rules** ⚠️ CRITICAL
   - Fixed base + equipment variance
   - Max 2 copies per card
   - Template for each weight class
   - New doc: `deck-construction.md`

4. **Design 5 starter weapons** ⚠️ HIGH PRIORITY
   - Longsword (4 cards), Greatsword (5 cards), Bow (4 cards), Shield (3 cards), Hammer (4 cards)
   - Full card stats (SP cost, initiative, damage, heat, range)
   - Add to Equipment Catalog doc (start it)

5. **Create 1 Arena scenario** ⚠️ HIGH PRIORITY
   - 7x7 hex map layout
   - 2-3 terrain features (ruins, water hex, elevation)
   - Deployment zones marked
   - Victory: First to 10 VP or last standing
   - New doc: `arena-scenarios.md`

### **NEXT WEEK** (Playtest Prep)

6. **Write example of play** ⚠️ HIGH PRIORITY
   - Full combat example (2-3 turns)
   - Show deck, hand, board state, decisions
   - Walk through damage resolution and card cycling
   - Add to CoreDesign.md or separate `example-play.md`

7. **Create quick reference sheet** ⚠️ MEDIUM PRIORITY
   - 1-page combat flowchart
   - SP costs (movement, attacks, utilities)
   - Heat thresholds, Taint track
   - Printable PDF

8. **First playtest** ⚠️ CRITICAL
   - You + 1 friend
   - Scout vs Heavy, Arena 1v1
   - Take notes on:
     - Confusing rules
     - Pacing (too fast/slow?)
     - Balance (one side dominate?)
     - Fun factor (exciting decisions?)

### **MONTH 1** (Expand & Iterate)

9. Expand equipment catalog to 15 items
10. Design terrain system (6-8 types)
11. Create 3 monster AI decks (Shrieking Colossus, Carrion Swarm, Corrupted Casket)
12. Write Campaign mission 1 (tutorial scenario)
13. Design Workshop system (full price list, upgrade tree)

---

## Balance Tweaks (From Previous Analysis)

### **Racial Abilities** (Balance Issues)

**Undead: Too Strong**
- Current: Start at 3 Taint (stable), Death's Door (extra life), immune to healing restrictions
- **Fix**: Death's Door triggers only ONCE per campaign, costs 2 Taint when used

**Fae Bargain: Too Swingy**
- Current: +2 SP for 3 turns (Scout gets 7 SP safe zone!)
- **Fix**: +1 SP for 3 turns (still strong, not broken)

**Human Vows: Too Weak**
- Current: Restrictions too minor for bonuses
- **Fix**: Steepen penalties
  - Vow of Wrath: Must attack if able, +1 damage, **-1 Defense**
  - Vow of Poverty: No Relic Tech, -1 Taint gain, **+1 Heat per turn** (struggling without tech)

### **Heat System** (Too Forgiving)

**Current**: 3-4 Heat = +1 Strain, 5-6 Heat = +2 Strain, -1 Defense

**Problem**: Players will sit comfortably at 4-5 Heat

**Fix**: Steeper escalation
```
| Heat | Effects |
|------|---------|
| 0-1  | Normal |
| 2-3  | Strain +1 |
| 4-5  | Strain +2, -1 Defense, weapons +1 SP |
| 6-7  | Strain +3, weapons +1 SP, movement -1 hex |
| 8+   | MELTDOWN: Take 2 Chassis damage OR vent all Heat (skip next turn) |
```

Now Heat 6+ is genuinely scary.

### **Universal Cards** (Minor Fixes)

**Unyielding Bulwark vs Second Skin**
- Current: Bulwark reduces 2 damage (strictly better than Second Skin's 1)
- **Fix**: Bulwark reduces 3 damage, but discard 1 random card from hand after use (risk/reward)

**Soul's Recall**
- Current: Draw 2 for 1 SP (very efficient, speeds deck cycling too much)
- **Fix**: Draw 2, discard 1 (net +1 card, forces choice)

---

## What Makes This Game Unique (Your Selling Points)

### 1. **Deck-As-Health + Equipment-As-Deck**
- Your deck IS your Casket
- Taking damage shrinks your options
- Equipment damage adds injury cards that clog your deck
- **Death spiral with mitigation** (Support can remove injuries)
- Kingdom Death meets deck-building

### 2. **Push-Your-Luck Action Economy**
- Safe Zone vs Danger Zone SP
- Risk heat/strain for more actions
- Corruption gives power but transforms you into a boss
- **Every turn is a gamble**

### 3. **Asymmetric Faction Gameplay**
- 7 races, each with unique mechanics
- Not just flavor—mechanically distinct
- Humans: Vow restrictions, Elves: Self-healing, Orcs: Anger stacking, Undead: Death's Door

### 4. **Grimdark Medieval Mech Fantasy**
- Not space marines, not anime, not steampunk
- **Gothic knights piloting magic-powered iron giants**
- Escaflowne meets Warhammer meets Kingdom Death

### 5. **Community-Driven 3D Printable System**
- Free core STLs
- Standardized connectors (like LEGO)
- Community designs weapons, shares files
- Repository of player-created content
- **Accessible and infinitely expandable**

### 6. **Rich Lore With No "Canon Answer"**
- The Sundering has 7 different interpretations (all partially true)
- Soulstones are divine fragments AND dragon hearts AND radiation byproduct
- Players can believe what they want
- **Mystery > definitive answer**

---

## Long-Term Vision

### **Year 1: Core Release**
- Free digital release (PDFs + STLs)
- Core rulebook, 20 equipment cards, 5 scenarios
- Community playtest feedback
- Iterate and refine

### **Year 2: Kickstarter**
- Physical card decks (print-on-demand or Kickstarter fulfillment)
- Professional art
- Pre-supported STL packs (all 7 races)
- Campaign book (15 missions with narrative)
- Stretch goals: Monster packs, terrain sets, NPC pilots

### **Year 3: Community Growth**
- Marketplace for community designs (70/30 revenue share)
- Tournament scene (official balanced equipment list)
- Expansion packs (new races, new factions, new threats)
- Living campaign (online narrative events)

---

## Final Thoughts

Your game has **huge potential**. The core mechanics are innovative, the theme is compelling, and the 3D printable angle is brilliant for accessibility and community engagement.

**The biggest risk right now**: Not playtesting soon enough.

**My recommendation**:
1. Make the 3 critical decisions (turn structure, combat resolution, deck construction)
2. Design 5 weapons
3. Create 1 scenario
4. Playtest THIS WEEK with minimal rules (write down questions as they come up)
5. Iterate based on what breaks

Don't wait for perfection. Get something playable, break it, fix it, repeat.

**You're 2-3 weeks away from a testable prototype.** The hard work (theme, core systems, world-building) is done. Now it's execution and iteration.

---

*"In iron we seek forgiveness. Through blood, absolution."*

Let me know which systems you want to tackle first. I'm happy to help design:
- Combat resolution rules
- Deck construction templates
- Equipment catalog (5-10 weapons to start)
- Arena scenario
- Example of play walkthrough
- Quick reference sheet

You're doing great work. Let's get this playable.
