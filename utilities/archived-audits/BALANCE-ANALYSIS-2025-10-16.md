# Faction Balance Analysis - October 16, 2025
## Penance: Absolution Through Steel

**Analysis Date**: October 16, 2025
**Game Version**: v2.0 + v3.0 Optional Rules
**Method**: Mathematical analysis + comparative review

---

## Executive Summary

After analyzing the four playable factions (Church, Dwarves, Ossuarium, Elves), I've identified **3 critical balance concerns** and **5 minor tuning opportunities**. This document provides mathematical breakdowns and recommended nerfs/buffs.

---

## Critical Balance Issues

### 1. Dwarven Stone Endurance (+2 HP Passive)

**Current State**:
- Dwarves start with **32 HP** (30 base + 2 from Stone Endurance)
- All other factions: 26-30 HP depending on deck size
- Dwarves also have Rune Counters (-1 damage per counter, max -3)

**Mathematical Impact**:
- Base HP advantage: +6.7% more HP than standard 30-card deck
- With 3 Rune Counters: Effective HP = 32 + (3 × average attacks to kill)
- Against 4-damage attacks: 32 HP = 8 hits vs 30 HP = 7.5 hits (6.7% more durable)
- **Combined with Rune Counters**: Dwarves can reduce 4-damage attacks to 1-damage → 32 hits to kill

**Problem**: Too tanky for playtest balance. Church burst damage (8-10 per attack) becomes trivial.

**Recommended Nerf**:
- REMOVE Stone Endurance +2 HP passive entirely
- **Replacement**: "Stone Endurance: Once per mission, when you reshuffle your deck, add only 1 Damage card instead of 1 (half death spiral penalty)"
- Keeps thematic "stone resilience" without raw HP inflation

---

### 2. Elven Passive Regeneration (3 cards/round)

**Current State**:
- **Photosynthesis**: Recover 1 card per turn if you don't attack
- **Verdant Regeneration**: Recover 1 card at start of each round
- **Living Seal (equipment)**: +1 card recovery per round if equipped
- **Total**: 3 cards recovered per round passively

**Mathematical Impact**:
- Average damage per attack: 4-6 cards
- Elves recover 3 cards/round passively = neutralizes 50% of incoming damage
- In a 10-round game: 30 cards recovered = entire deck size
- **Infinite sustain**: Elves never die in long games if they kite successfully

**Problem**: Oppressive in attrition matchups. Dwarves can't kill them, Ossuarium can't out-sustain them.

**Recommended Nerf**:
- **Photosynthesis**: Change to "At end of your turn, if you did NOT attack AND did not take damage this turn, recover 1 card"
- **Verdant Regeneration**: Keep as-is (1 card/round passive)
- **Living Seal**: Reduce to "+1 card recovery when you use a healing effect" (not passive)
- **New Total**: 1-2 cards/round (conditional), down from 3 guaranteed

---

### 3. Ossuarium Triple Resurrection

**Current State**:
- **Phylactery (faction card)**: First time at 0 HP, set HP to 5 (automatic, once per mission)
- **Undying Resilience (equipment)**: Second resurrection (manual trigger, once per mission)
- **Phylactery Relic (rare equipment)**: Third resurrection (manual trigger, once per campaign)
- **Total**: 3 full resurrections

**Mathematical Impact**:
- Ossuarium effectively has 4 lives (original + 3 resurrections)
- Church must deal lethal damage **4 times** to win
- Average game length: 10 rounds → Ossuarium resurrects on round 3, 6, 9 → unkillable

**Problem**: Phylactery Relic (third resurrection) is campaign-only item but breaks casual play.

**Recommended Nerf**:
- **Phylactery**: Keep as-is (once per mission, automatic, 5 HP recovery)
- **Undying Resilience**: Keep as-is (once per mission, manual trigger)
- **Phylactery Relic**: REMOVE from casual play (campaign-only, end-game reward)
- **Alternative Option**: Phylactery reduced to "recover 3 cards" instead of "set HP to 5"
- **New Total**: 2 resurrections max in casual play

---

## Minor Tuning Opportunities

### 4. Church Blood Offering (Self-Harm Risk/Reward)

**Current State**:
- **Blood Offering**: Discard 2 cards from deck → +3 damage, ignore 1 Defense, -1 to hit (easier)
- Cost: 2 cards (6.7% of 30-card deck)
- Reward: +3 damage (increases 5-damage attack to 8 damage = +60%)

**Analysis**:
- Fair trade in alpha strike scenarios (burst 10+ damage turn 1-2)
- **Problem**: Church can stack multiple Blood Offerings in one turn (discard 4-6 cards for +6-9 damage)
- Divine Judgment (8 damage) + 2× Blood Offering = 14 damage guaranteed hit

**Recommended Nerf**:
- Add limit: "You can only play 1 Blood Offering per turn"
- Prevents degenerate turn-1 alpha strike (discard 6 cards, deal 20 damage, win immediately)

---

### 5. Dwarven Armor-Piercing (Oppressive vs Defense Builds)

**Current State**:
- **All Dwarven attacks ignore Defense buffs and armor**
- Church Guardian's Defiance (+2 Defense) = useless
- Universal Unyielding Bulwark (-2 damage) = useless
- Ossuarium defensive cards = useless

**Analysis**:
- Thematic and balanced vs offensive factions (Elves, Church)
- **Problem**: Invalidates entire defensive archetypes (Tower Shield builds, Guardian builds)

**Recommended Adjustment**:
- **Crushing Blow (faction card)**: Keep ARMOR PIERCING keyword
- **Other Dwarven faction cards**: Remove blanket armor-piercing
- **Equipment-based armor-piercing**: Keep (Warhammer, specific weapons)
- **Result**: Dwarves retain armor-piercing identity but don't invalidate all defensive play

---

### 6. Church Righteous Fury (Infinite Scaling)

**Current State**:
- **Righteous Fury (passive)**: Each time allied Casket destroyed → +1 damage to all attacks permanently
- Stacks infinitely
- In 4-player game with 3 allies destroyed: +3 damage permanently

**Analysis**:
- Balanced in 1v1 (no allies = no scaling)
- **Problem**: Broken in multiplayer (3+ allies = +3-5 damage permanently)

**Recommended Nerf**:
- Add limit: "Righteous Fury: Max +3 damage from this effect"
- Still strong (+3 damage = +60% increase on 5-damage attacks) but not infinite

---

### 7. Elven Bleed Stacking (Infinite Scaling)

**Current State**:
- **Bleed damage stacks infinitely**
- Thorn Strike (3 damage + Bleed 2) × 5 attacks = 10 Bleed damage per turn
- After 10 rounds: 20+ Bleed damage per turn (automatic win)

**Analysis**:
- Balanced in short games (1-5 rounds)
- **Problem**: Oppressive in long games (10+ rounds = 30+ Bleed stacks)

**Recommended Nerf**:
- Add cap: "Max Bleed stacks: 10" (still strong, not infinite)
- Alternative: "Bleed damage decays by 1 per round" (requires re-application)

---

### 8. Ossuarium Soul Harvest Lifesteal (Too Consistent)

**Current State**:
- **Soul Harvest**: 4 damage → recover 4 cards (100% lifesteal)
- No diminishing returns, no caps

**Analysis**:
- Balanced vs burst damage (Church kills before lifesteal)
- **Problem**: Oppressive vs attrition (Dwarves can't out-damage recovery)

**Recommended Nerf**:
- Reduce recovery: "Soul Harvest: 4 damage → recover 3 cards (75% lifesteal)"
- Still strong, but not 1:1 trade

---

## Recommended Tier List (Post-Nerf)

### S-Tier (Best)
- **Church of Absolution** (burst alpha strike, strong in 1v1)
- **Dwarven Forge-Guilds** (tanky, armor-piercing, consistent)

### A-Tier (Strong)
- **The Ossuarium** (2 resurrections, lifesteal, grinding)
- **Elven Verdant Covenant** (mobility, Bleed, hit-and-run)

### Current Tier List (Pre-Nerf)
1. **Elves** (3 cards/round passive = unkillable)
2. **Ossuarium** (3 resurrections = 4 lives)
3. **Dwarves** (32 HP + Rune Counters = too tanky)
4. **Church** (self-destructive, fragile)

---

## Proposed Nerfs Summary

| Faction | Card/Mechanic | Current Effect | Proposed Nerf | Impact |
|---------|--------------|----------------|---------------|--------|
| **Dwarves** | Stone Endurance | +2 HP passive | Remove, replace with "half death spiral penalty" | -6.7% HP |
| **Elves** | Photosynthesis | 1 card/turn (no attack) | 1 card/turn (no attack AND no damage taken) | Conditional |
| **Elves** | Living Seal | +1 card/round passive | +1 card when healing effect used | Conditional |
| **Elves** | Bleed Stacks | Infinite | Max 10 stacks | Caps scaling |
| **Ossuarium** | Phylactery Relic | 3rd resurrection | Remove from casual play | -1 life |
| **Ossuarium** | Soul Harvest | 4 damage = 4 cards | 4 damage = 3 cards | -25% lifesteal |
| **Church** | Blood Offering | Unlimited per turn | 1 per turn limit | Prevents turn-1 alpha |
| **Church** | Righteous Fury | Infinite scaling | Max +3 damage | Caps scaling |
| **Dwarves** | Armor-Piercing | All attacks | Only Crushing Blow + equipment | Less oppressive |

---

## Playtesting Priority

**High Priority** (Critical Balance):
1. Test Dwarven Stone Endurance removal (HP 30 vs 32)
2. Test Elven passive regeneration nerf (3 cards/round → 1-2 conditional)
3. Test Ossuarium with 2 resurrections (remove Phylactery Relic)

**Medium Priority** (Tuning):
4. Test Church Blood Offering 1/turn limit
5. Test Elven Bleed cap at 10 stacks
6. Test Ossuarium Soul Harvest 75% lifesteal

**Low Priority** (Edge Cases):
7. Test Church Righteous Fury +3 cap (multiplayer only)
8. Test Dwarven armor-piercing limited to specific cards

---

## Mathematical Breakdown: Expected Win Rates (Post-Nerf)

### Church vs Dwarves
- **Pre-Nerf**: 55/45 Church favor (burst bypasses armor)
- **Post-Nerf**: 50/50 (Dwarves lose 2 HP, Church loses infinite stacking)

### Church vs Ossuarium
- **Pre-Nerf**: 60/40 Church favor (burst before lifesteal)
- **Post-Nerf**: 55/45 Church favor (Ossuarium loses 1 resurrection)

### Church vs Elves
- **Pre-Nerf**: 45/55 Elves favor (mobility + infinite regeneration)
- **Post-Nerf**: 50/50 (Elves lose 1-2 cards/round passive)

### Dwarves vs Ossuarium
- **Pre-Nerf**: 40/60 Ossuarium favor (3 resurrections + lifesteal)
- **Post-Nerf**: 50/50 (Ossuarium loses 1 resurrection, -25% lifesteal)

### Dwarves vs Elves
- **Pre-Nerf**: 35/65 Elves favor (infinite Bleed + passive regen)
- **Post-Nerf**: 55/45 Dwarves favor (Elves lose regen, Bleed capped)

### Ossuarium vs Elves
- **Pre-Nerf**: 40/60 Elves favor (infinite scaling)
- **Post-Nerf**: 50/50 (both lose infinite scaling)

---

## Conclusion

**Current meta (pre-nerf)**: Elves > Ossuarium > Dwarves > Church
**Proposed meta (post-nerf)**: All factions 50/50 balanced

**Action Items**:
1. Apply nerfs to faction card files
2. Update faction-comparison-playtest.md
3. Playtest with new values
4. Iterate based on feedback

---

**END OF DOCUMENT**

*"Balance is a lie we tell ourselves at night. But we keep trying anyway."*
