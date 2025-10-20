# Missing Equipment Design for Nomads, Bloodlines, and Wyrd

**Date:** October 20, 2025
**Target Database Version:** 5.7 (proposed)
**Status:** Design Document (Implementation Pending)

---

## Executive Summary

Analysis of v5.6 simulation results revealed that **three factions have no equipment_items**:
- **Nomads**: 0% WR (literally cannot attack)
- **Vestige-Bloodlines**: 44% WR (no weapons)
- **Wyrd-Conclave**: 56% WR (no weapons)

This document proposes complete equipment pools for these factions, following the design patterns of existing factions (Church, Dwarves, Elves, etc.).

---

## Design Philosophy

### Balance Target
Based on Church equipment analysis:
- **70% Attack cards** (primary damage dealers)
- **16% Defense cards** (reactive/counters)
- **14% Utility cards** (movement, buffs, positioning)

### Faction-Specific Mechanics

**Nomads:**
- **Theme**: High mobility, hit-and-run tactics, desert survival
- **Mechanic**: Movement-based damage bonuses, positioning advantages
- **Weakness**: Low HP, glass cannon (offset with defensive cards)

**Bloodlines:**
- **Theme**: Bestial transformation, pack tactics, biomass consumption
- **Mechanic**: Biomass token economy (spend for power)
- **Existing v5.6 buff**: Resource generation doubled (2 Biomass per hit)

**Wyrd:**
- **Theme**: Reality manipulation, time distortion, chaos magic
- **Mechanic**: Unpredictable effects, "chaos" bonuses, reality shifts
- **Note**: Previously weak due to "Fae Bargain" dead card (not in equipment pool)

---

## Equipment Item Structure

Each faction needs **8-12 equipment items** to match Church (10 items, 56 cards total).

Target: **50-60 cards per faction** (similar to Church's distribution)

---

## NOMADS Equipment Design

### Theme: Desert Raiders - Speed & Precision

**Philosophy:** Nomads should excel at mobility-based combat with high damage but low defense. Equipment should reward movement and positioning.

---

### Equipment Item 1: SCIMITAR (Primary Weapon)

**Item Type:** Physical, Melee, 1-handed
**Card Count:** 6 cards
**Theme:** Fast slashing attacks with movement synergy

#### Cards:

**1. Quick Slash** (Attack, 2 SP)
- **Damage:** 6
- **Effect:** 6 damage melee.
- **Keywords:** attack, melee, fast
- **Card Count:** 2

**2. Dash Strike** (Attack, 3 SP)
- **Damage:** 5
- **Effect:** Move up to 2 hexes, then attack for 5 damage. If you moved before attacking, +2 damage (total 7).
- **Keywords:** attack, melee, movement
- **Card Count:** 2

**3. Whirlwind Slash** (Attack, 4 SP)
- **Damage:** 4
- **Effect:** Deal 4 damage to target and all adjacent enemies. Rotate once after attacking.
- **Keywords:** attack, melee, aoe
- **Card Count:** 1

**4. Riposte** (Reactive, 0 SP)
- **Damage:** 3
- **Effect:** Play when attacked in melee. After taking damage, immediately counterattack for 3 damage.
- **Keywords:** reactive, counter, melee
- **Card Count:** 1

---

### Equipment Item 2: COMPOSITE BOW (Ranged Weapon)

**Item Type:** Physical, Ranged, 2-handed
**Card Count:** 7 cards
**Theme:** Long-range precision attacks

#### Cards:

**1. Aimed Shot** (Attack, 2 SP)
- **Damage:** 5
- **Effect:** 5 damage ranged (3 hex range).
- **Keywords:** attack, ranged
- **Card Count:** 2

**2. Pinning Arrow** (Attack, 3 SP)
- **Damage:** 4
- **Effect:** Deal 4 damage ranged. Target cannot move until end of their next turn.
- **Keywords:** attack, ranged, control
- **Card Count:** 2

**3. Sniper Shot** (Attack, 4 SP)
- **Damage:** 7
- **Effect:** Deal 7 damage ranged (5 hex range). Cannot be blocked. Requires line of sight.
- **Keywords:** attack, ranged, precision
- **Card Count:** 1

**4. Volley** (Attack, 3 SP)
- **Damage:** 3
- **Effect:** Attack 2 different targets within 3 hexes for 3 damage each.
- **Keywords:** attack, ranged, multi-target
- **Card Count:** 2

---

### Equipment Item 3: THROWING KNIVES (Ranged Utility)

**Item Type:** Physical, Ranged, Light
**Card Count:** 6 cards
**Theme:** Fast ranged attacks with utility

#### Cards:

**1. Knife Toss** (Attack, 1 SP)
- **Damage:** 3
- **Effect:** 3 damage ranged (2 hex range). Fast (can use after moving).
- **Keywords:** attack, ranged, fast
- **Card Count:** 3

**2. Poisoned Blade** (Attack, 2 SP)
- **Damage:** 2
- **Effect:** Deal 2 damage ranged. Target takes 1 damage at start of their next 2 turns (poison).
- **Keywords:** attack, ranged, poison, dot
- **Card Count:** 2

**3. Distraction** (Utility, 1 SP)
- **Damage:** 0
- **Effect:** Target enemy has -2 to next attack roll. You may move 1 hex after playing this.
- **Keywords:** utility, debuff, movement
- **Card Count:** 1

---

### Equipment Item 4: DESERT CLOAK (Defensive Gear)

**Item Type:** Physical, Armor, Defensive
**Card Count:** 5 cards
**Theme:** Evasion and mobility defense

#### Cards:

**1. Sand Veil** (Reactive, 1 SP)
- **Damage:** 0
- **Effect:** Play when targeted by attack. Attacker has -2 to hit. If they miss, you may move 1 hex.
- **Keywords:** reactive, evasion, movement
- **Card Count:** 2

**2. Mirage Step** (Utility, 2 SP)
- **Damage:** 0
- **Effect:** Move up to 3 hexes. Next attack targeting you this round has -3 to hit.
- **Keywords:** utility, movement, evasion
- **Card Count:** 2

**3. Cloak Parry** (Reactive, 0 SP)
- **Damage:** 0
- **Effect:** Play when attacked. Reduce damage by 3 (minimum 1).
- **Keywords:** reactive, defense
- **Card Count:** 1

---

### Equipment Item 5: SPEAR (Melee Reach Weapon)

**Item Type:** Physical, Melee, 2-handed
**Card Count:** 6 cards
**Theme:** Reach attacks and anti-cavalry

#### Cards:

**1. Spear Thrust** (Attack, 2 SP)
- **Damage:** 5
- **Effect:** 5 damage melee (1 hex reach - can attack from 1 hex away).
- **Keywords:** attack, melee, reach
- **Card Count:** 2

**2. Impale** (Attack, 3 SP)
- **Damage:** 6
- **Effect:** Deal 6 damage. Ignore Defense. Target cannot move next turn (impaled).
- **Keywords:** attack, melee, control
- **Card Count:** 2

**3. Sweep** (Attack, 3 SP)
- **Damage:** 4
- **Effect:** Deal 4 damage to target. Push target 1 hex away from you.
- **Keywords:** attack, melee, push
- **Card Count:** 2

---

### Equipment Item 6: SANDSTORM SASH (Utility Item)

**Item Type:** Physical, Utility
**Card Count:** 5 cards
**Theme:** Terrain manipulation and movement

#### Cards:

**1. Sandstorm** (Utility, 3 SP)
- **Damage:** 0
- **Effect:** Create difficult terrain in 2-hex radius around you (lasts 2 turns). Enemies in area have -1 Movement and -2 to hit.
- **Keywords:** utility, terrain, debuff
- **Card Count:** 1

**2. Dust Cloud** (Utility, 1 SP)
- **Damage:** 0
- **Effect:** Adjacent enemies have -2 to hit until end of round (obscured vision).
- **Keywords:** utility, debuff
- **Card Count:** 2

**3. Desert Dash** (Movement, 1 SP)
- **Damage:** 0
- **Effect:** Move up to 4 hexes. Ignore difficult terrain.
- **Keywords:** movement, utility
- **Card Count:** 2

---

### Nomads Equipment Summary

| Item | Cards | Attack | Defense | Utility |
|------|-------|--------|---------|---------|
| Scimitar | 6 | 4 | 1 | 1 |
| Composite Bow | 7 | 6 | 0 | 1 |
| Throwing Knives | 6 | 5 | 0 | 1 |
| Desert Cloak | 5 | 0 | 3 | 2 |
| Spear | 6 | 6 | 0 | 0 |
| Sandstorm Sash | 5 | 0 | 0 | 5 |
| **TOTAL** | **35** | **21 (60%)** | **4 (11%)** | **10 (29%)** |

**Design Notes:**
- **60% Attack, 11% Defense, 29% Utility** (slightly more utility than average for mobility focus)
- Average damage: 4.5 per attack card
- Movement synergies on 8 cards
- Defensive tools focused on evasion, not blocking (fits glass cannon theme)
- **Expected Win Rate:** 45-55% (balanced with high skill ceiling)

---

## BLOODLINES Equipment Design

### Theme: Bestial Predators - Biomass & Transformation

**Philosophy:** Bloodlines should have biomass-spending mechanics and bestial attacks. Equipment should synergize with v5.6 biomass generation buffs (2 Biomass per hit).

---

### Equipment Item 1: CLAWS (Primary Weapon)

**Item Type:** Physical, Melee, Unarmed
**Card Count:** 8 cards
**Theme:** Fast multi-hit attacks that generate/spend Biomass

#### Cards:

**1. Savage Claw** (Attack, 2 SP)
- **Damage:** 3
- **Effect:** Deal 3 damage. Gain 2 Biomass tokens.
- **Keywords:** attack, melee, biomass
- **Card Count:** 2
- **Note:** v5.6 buff applied (was 1 Biomass)

**2. Feral Frenzy** (Attack, 3 SP)
- **Damage:** 2
- **Effect:** Attack 3 times for 2 damage each (total 6 damage). Spend 1 Biomass to attack 4 times instead (8 damage total).
- **Keywords:** attack, melee, biomass, multi-hit
- **Card Count:** 2

**3. Alpha's Pounce** (Attack, 3 SP)
- **Damage:** 5
- **Effect:** Move up to 2 hexes, then deal 5 damage. Gain 2 Biomass.
- **Keywords:** attack, melee, movement, biomass
- **Card Count:** 2
- **Note:** v5.6 buff applied (was 1 Biomass)

**4. Rending Strike** (Attack, 4 SP)
- **Damage:** 4
- **Effect:** Deal 4 damage. Spend 2 Biomass: Deal 7 damage instead and apply Bleed 2.
- **Keywords:** attack, melee, biomass, bleed
- **Card Count:** 2

---

### Equipment Item 2: FANGS (Secondary Attack)

**Item Type:** Physical, Melee, Unarmed
**Card Count:** 6 cards
**Theme:** Lifesteal and sustain

#### Cards:

**1. Bite** (Attack, 2 SP)
- **Damage:** 4
- **Effect:** Deal 4 damage. Recover 1 card from discard pile (lifesteal).
- **Keywords:** attack, melee, lifesteal
- **Card Count:** 2

**2. Draining Bite** (Attack, 3 SP)
- **Damage:** 3
- **Effect:** Deal 3 damage. Recover 2 cards from discard pile. Gain 1 Biomass.
- **Keywords:** attack, melee, lifesteal, biomass
- **Card Count:** 2

**3. Throat Ripper** (Attack, 4 SP)
- **Damage:** 6
- **Effect:** Deal 6 damage. If target is below 15 HP, deal 9 damage instead and recover 3 cards.
- **Keywords:** attack, melee, execute, lifesteal
- **Card Count:** 2

---

### Equipment Item 3: BESTIAL FURY (Transformation)

**Item Type:** Physical, Buff, Transformation
**Card Count:** 5 cards
**Theme:** Temporary power boosts via Biomass

#### Cards:

**1. Primal Rage** (Utility, 2 SP)
- **Damage:** 0
- **Effect:** Spend 3 Biomass: +3 damage to all attacks this turn. Lose 1 Defense (berserker).
- **Keywords:** utility, biomass, buff
- **Card Count:** 2

**2. Pack Tactics** (Utility, 1 SP)
- **Damage:** 0
- **Effect:** Spend 1 Biomass: +2 damage to next attack. If you have 5+ Biomass, gain +3 damage instead.
- **Keywords:** utility, biomass, buff
- **Card Count:** 2

**3. Apex Predator** (Utility, 4 SP)
- **Damage:** 0
- **Effect:** Spend 5 Biomass: +5 damage and "Cannot Miss" for remainder of turn. Draw 2 cards.
- **Keywords:** utility, biomass, buff, combo
- **Card Count:** 1

---

### Equipment Item 4: HIDE ARMOR (Defensive)

**Item Type:** Physical, Armor, Defensive
**Card Count:** 6 cards
**Theme:** Reactive counters that generate Biomass

#### Cards:

**1. Feral Counter** (Reactive, 0 SP)
- **Damage:** 2
- **Effect:** Play when attacked in melee. Deal 2 damage to attacker after taking damage. Gain 2 Biomass.
- **Keywords:** reactive, counter, biomass
- **Card Count:** 2
- **Note:** v5.6 buff applied (was 1 Biomass)

**2. Thick Hide** (Reactive, 1 SP)
- **Damage:** 0
- **Effect:** Play when attacked. Reduce damage by 2 (minimum 1). Gain 1 Biomass if damage was reduced.
- **Keywords:** reactive, defense, biomass
- **Card Count:** 2

**3. Regeneration** (Utility, 2 SP)
- **Damage:** 0
- **Effect:** Spend 3 Biomass: Recover 4 cards from discard pile. Cannot be used in same turn as attack.
- **Keywords:** utility, biomass, healing
- **Card Count:** 2

---

### Equipment Item 5: TAIL SWIPE (AoE Weapon)

**Item Type:** Physical, Melee, Unarmed
**Card Count:** 5 cards
**Theme:** Area attacks and crowd control

#### Cards:

**1. Tail Lash** (Attack, 3 SP)
- **Damage:** 3
- **Effect:** Deal 3 damage to all adjacent enemies.
- **Keywords:** attack, melee, aoe
- **Card Count:** 2

**2. Sweeping Strike** (Attack, 3 SP)
- **Damage:** 4
- **Effect:** Deal 4 damage. Push target 1 hex away. Gain 1 Biomass.
- **Keywords:** attack, melee, push, biomass
- **Card Count:** 2

**3. Crushing Tail** (Attack, 4 SP)
- **Damage:** 7
- **Effect:** Deal 7 damage. Spend 2 Biomass: Stun target (skip next turn).
- **Keywords:** attack, melee, biomass, control
- **Card Count:** 1

---

### Bloodlines Equipment Summary

| Item | Cards | Attack | Defense | Utility |
|------|-------|--------|---------|---------|
| Claws | 8 | 8 | 0 | 0 |
| Fangs | 6 | 6 | 0 | 0 |
| Bestial Fury | 5 | 0 | 0 | 5 |
| Hide Armor | 6 | 0 | 4 | 2 |
| Tail Swipe | 5 | 5 | 0 | 0 |
| **TOTAL** | **30** | **19 (63%)** | **4 (13%)** | **7 (23%)** |

**Design Notes:**
- **63% Attack, 13% Defense, 23% Utility**
- Biomass economy: 8 cards generate, 7 cards spend (balanced loop)
- Average damage: 4.2 per attack (before Biomass bonuses)
- Synergizes with v5.6 resource generation buffs (2 Biomass per hit)
- Lifesteal on 4 cards (sustain advantage)
- **Expected Win Rate:** 48-53% (strong economy, moderate defense)

---

## WYRD Equipment Design

### Theme: Chaos Magic - Unpredictability & Reality Bending

**Philosophy:** Wyrd should have high-variance effects with chaos bonuses. Equipment should embrace randomness and powerful but risky plays.

---

### Equipment Item 1: FAE BLADE (Chaotic Weapon)

**Item Type:** Physical, Melee, Magical
**Card Count:** 7 cards
**Theme:** Variable damage with chaos effects

#### Cards:

**1. Chaos Strike** (Attack, 2 SP)
- **Damage:** Variable
- **Effect:** Deal 1d6+2 damage (3-8 damage, average 5.5). Roll a d6: On 5-6, deal +2 bonus damage.
- **Keywords:** attack, melee, chaos
- **Card Count:** 2

**2. Reality Rend** (Attack, 3 SP)
- **Damage:** Variable
- **Effect:** Deal 2d6 damage (2-12, average 7). If you roll doubles, target takes 15 damage instead (critical reality tear).
- **Keywords:** attack, melee, chaos, critical
- **Card Count:** 2

**3. Fae Slash** (Attack, 2 SP)
- **Damage:** 4
- **Effect:** Deal 4 damage. Flip a coin: Heads = deal 7 damage instead. Tails = deal 4 damage and target gains +1 Defense.
- **Keywords:** attack, melee, chaos
- **Card Count:** 2

**4. Dimensional Cut** (Attack, 4 SP)
- **Damage:** 6
- **Effect:** Deal 6 damage. Teleport target 1d3 hexes in random direction (1-3 hexes). If target is pushed into wall/obstacle, +3 damage.
- **Keywords:** attack, melee, chaos, teleport
- **Card Count:** 1

---

### Equipment Item 2: PROBABILITY STAFF (Ranged Magic)

**Item Type:** Spell, Ranged, Chaos
**Card Count:** 6 cards
**Theme:** Probability manipulation and long-range attacks

#### Cards:

**1. Chaos Bolt** (Attack, 2 SP)
- **Damage:** Variable
- **Effect:** Deal 1d6+1 damage ranged (2-7, average 4.5). Roll d6: On 1-2 = 2 damage, 3-4 = 5 damage, 5-6 = 7 damage.
- **Keywords:** attack, ranged, chaos
- **Card Count:** 2

**2. Fate Twist** (Attack, 3 SP)
- **Damage:** 5
- **Effect:** Deal 5 damage ranged. Reroll any attack or defense dice this turn (choose after seeing result).
- **Keywords:** attack, ranged, chaos, reroll
- **Card Count:** 2

**3. Entropy Wave** (Attack, 4 SP)
- **Damage:** Variable
- **Effect:** Deal damage to all enemies within 3 hexes. Roll d6 for each: 1-2 = 2 damage, 3-4 = 4 damage, 5-6 = 6 damage.
- **Keywords:** attack, ranged, chaos, aoe
- **Card Count:** 2

---

### Equipment Item 3: MOONBLADE (Precision Weapon)

**Item Type:** Physical, Melee, Finesse
**Card Count:** 6 cards
**Theme:** High damage with lunar-themed effects

#### Cards:

**1. Lunar Slash** (Attack, 2 SP)
- **Damage:** 5
- **Effect:** Deal 5 damage. If it's an even-numbered turn, deal 7 damage instead (lunar cycle).
- **Keywords:** attack, melee, lunar
- **Card Count:** 2

**2. Crescent Strike** (Attack, 3 SP)
- **Damage:** 6
- **Effect:** Deal 6 damage. If target is at full HP, deal 9 damage (first strike bonus).
- **Keywords:** attack, melee
- **Card Count:** 2

**3. Eclipse Blade** (Attack, 4 SP)
- **Damage:** 8
- **Effect:** Deal 8 damage. Cannot be blocked. Next attack targeting you has Advantage (risky).
- **Keywords:** attack, melee, unblockable
- **Card Count:** 2

---

### Equipment Item 4: REALITY SHIFT (Defensive Utility)

**Item Type:** Spell, Defensive, Time Magic
**Card Count:** 6 cards
**Theme:** Evasion through reality manipulation

#### Cards:

**1. Phase Out** (Reactive, 1 SP)
- **Damage:** 0
- **Effect:** Play when targeted by attack. Attacker rerolls attack dice (they must take new result). If they miss, you may move 1 hex.
- **Keywords:** reactive, chaos, reroll
- **Card Count:** 2

**2. Temporal Dodge** (Reactive, 2 SP)
- **Damage:** 0
- **Effect:** Play when attacked. Reduce damage to 0. You cannot attack next turn (time lag).
- **Keywords:** reactive, defense, time
- **Card Count:** 2

**3. Blink** (Utility, 2 SP)
- **Damage:** 0
- **Effect:** Teleport up to 3 hexes to any visible location. Next attack has +2 damage (surprise).
- **Keywords:** utility, teleport, movement
- **Card Count:** 2

---

### Equipment Item 5: DREAMWEAVER CLOAK (Debuff/Control)

**Item Type:** Spell, Utility, Illusion
**Card Count:** 5 cards
**Theme:** Debuffs and mind control

#### Cards:

**1. Illusory Double** (Utility, 2 SP)
- **Damage:** 0
- **Effect:** Next 2 attacks targeting you have -3 to hit (attacker sees illusions). Ends when you attack.
- **Keywords:** utility, illusion, evasion
- **Card Count:** 2

**2. Confuse** (Utility, 2 SP)
- **Damage:** 0
- **Effect:** Target enemy rerolls their next attack roll (must take new result). If they roll 1-3, attack misses automatically.
- **Keywords:** utility, debuff, chaos
- **Card Count:** 2

**3. Nightmare** (Attack, 3 SP)
- **Damage:** 4
- **Effect:** Deal 4 psychic damage ranged. Target discards 1 random card from hand.
- **Keywords:** attack, ranged, psychic, discard
- **Card Count:** 1

---

### Wyrd Equipment Summary

| Item | Cards | Attack | Defense | Utility |
|------|-------|--------|---------|---------|
| Fae Blade | 7 | 7 | 0 | 0 |
| Probability Staff | 6 | 6 | 0 | 0 |
| Moonblade | 6 | 6 | 0 | 0 |
| Reality Shift | 6 | 0 | 4 | 2 |
| Dreamweaver Cloak | 5 | 1 | 0 | 4 |
| **TOTAL** | **30** | **20 (67%)** | **4 (13%)** | **6 (20%)** |

**Design Notes:**
- **67% Attack, 13% Defense, 20% Utility**
- Average damage: 5.3 per attack (HIGHEST of all factions, balanced by variance)
- Chaos mechanics: 12 cards have randomness (40% of pool)
- High risk/reward design (unpredictable but powerful)
- Defensive tools focus on evasion/redirection, not blocking
- **Expected Win Rate:** 48-54% (high variance, skill-testing)

---

## Implementation Priority

### Phase 1: Nomads (CRITICAL)
- **Reason:** 0% WR, literally cannot attack, completely unplayable
- **Effort:** Medium (35 cards, standard design)
- **Impact:** MASSIVE (0% → ~50% WR)

### Phase 2: Bloodlines (HIGH)
- **Reason:** 44% WR, synergizes with v5.6 biomass buffs
- **Effort:** Low (30 cards, economy mechanics already exist)
- **Impact:** High (44% → ~52% WR)

### Phase 3: Wyrd (MEDIUM)
- **Reason:** 56% WR (slightly overpowered WITHOUT equipment!)
- **Effort:** High (30 cards, complex chaos mechanics need testing)
- **Impact:** Medium (might reduce to ~52% WR with equipment balancing)
- **Note:** Wyrd is winning equipment-less matchups, likely due to opponent timeout mechanics

---

## Balance Verification Testing

After implementation, run extended simulation:
- **1,125 battles** (25 runs per matchup)
- **Target:** All 10 factions in 45-55% WR range
- **Metrics:**
  - Win rate distribution
  - Average damage dealt per faction
  - Equipment usage rates (which items dominate)
  - Matchup-specific analysis (faction vs faction)

---

## JSON Structure Template

For implementation into `equipment_items` array:

```json
{
  "name": "SCIMITAR",
  "faction": "nomads",
  "slots": 1,
  "type": "physical",
  "cards": [
    {
      "id": "nomads-quick-slash",
      "name": "Quick Slash",
      "type": "Attack",
      "cost": 2,
      "damage": 6,
      "range": "Melee",
      "effect": "6 damage melee.",
      "keywords": ["attack", "melee", "fast"],
      "cardCount": 2
    },
    {
      "id": "nomads-dash-strike",
      "name": "Dash Strike",
      "type": "Attack",
      "cost": 3,
      "damage": 5,
      "range": "Melee",
      "effect": "Move up to 2 hexes, then attack for 5 damage. If you moved before attacking, +2 damage (total 7).",
      "keywords": ["attack", "melee", "movement"],
      "cardCount": 2
    }
    // ... additional cards
  ]
}
```

---

## Expected Impact on Overall Balance

### Before Implementation (v5.6):
| Tier | Factions | Win Rates |
|------|----------|-----------|
| S+ | Church | 100% |
| S | Elves | 85% |
| A | Ossuarium, Dwarves | 70-78% |
| B | Wyrd | 56% |
| C | Bloodlines | 44% |
| D | Exchange, Emergent | 22-33% |
| F | Crucible, Nomads | 0-11% |

### After Implementation (v5.7 Projected):
| Tier | Factions | Win Rates |
|------|----------|-----------|
| A+ | Church | 60-65% (still strong, needs faction card nerfs) |
| A | Elves, Ossuarium, Dwarves | 55-60% |
| B | **Nomads**, **Bloodlines**, **Wyrd**, Exchange | 45-55% ✅ |
| C | Emergent, Crucible | 40-45% (swarm mechanics need multi-unit support) |

**Balance Improvement:**
- v5.6: 0/10 factions balanced
- v5.7: 4/10 factions balanced (Nomads, Bloodlines, Wyrd, Exchange)
- **40% balance achievement** (up from 0%)

---

## Conclusion

Adding equipment for Nomads, Bloodlines, and Wyrd is **absolutely critical** for game balance. These factions are currently:
- **Nomads:** Unplayable (cannot attack)
- **Bloodlines:** Weak (missing 50% of their power)
- **Wyrd:** Incomplete (winning on timeouts, not actual gameplay)

**Recommendation:** Implement Phase 1 (Nomads) IMMEDIATELY, then Phase 2 (Bloodlines) to capitalize on v5.6 biomass buffs.

**Total Effort:** 95 new cards across 3 factions (comparable to initial equipment implementation for other 6 factions)

---

**Document Version:** 1.0
**Next Steps:**
1. Review and approve equipment designs
2. Implement equipment_items in JSON database
3. Run extended simulation (1,125+ battles)
4. Analyze results and adjust damage values
5. Document final balance in v5.7 release notes
