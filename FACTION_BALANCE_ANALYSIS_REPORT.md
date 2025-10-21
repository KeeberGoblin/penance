# Comprehensive Faction Balance Analysis Report

**Date:** October 20, 2025
**Scope:** Analysis of 10 faction card data sets
**Data Source:** `/workspaces/penance/docs/cards/complete-card-data.json` (v5.20)
**Simulation Data:** 30,600+ battles across 17 balance rounds

---

## Executive Summary

### Current Balance State (v5.20)

| Faction | Win Rate | Status | Key Issue |
|---------|----------|--------|-----------|
| **Vestige-Bloodlines** | 82.2% | 🚨 Critical OP | Biomass economy too strong |
| **Ossuarium** | 77.8% | ⚠️ Very OP | Lifesteal + low Taint penalties |
| **Emergent Syndicate** | 60.0% | ⚠️ OP | Consistent high damage |
| **Wyrd Conclave** | 55.6% | ⚠️ Slightly OP | Strong token economy |
| **Crucible Packs** | 51.1% | ✅ Balanced | Reference point |
| **Exchange** | 48.9% | ✅ Balanced | Credit economy scaled well |
| **Elves** | 42.2% | ⚠️ Weak | Low damage, bleed too slow |
| **Church** | 33.3% | ⚠️ Very Weak | Self-harm without payoff |
| **Nomads** | 28.9% | 🚨 Critical Weak | No economy, low damage |
| **Dwarves** | 20.0% | 🚨 Critical Weak | Rune system too slow |

**Balanced Factions:** 2/10 (Crucible, Exchange)
**Target:** 7-8/10 factions in 45-55% WR range

---

## Faction Card Data Analysis

### 1. DAMAGE EFFICIENCY COMPARISON

| Faction | Avg Dmg | Attack Cards | Avg Efficiency | Top Efficiency |
|---------|---------|--------------|----------------|----------------|
| Church | 5.25 | 17 | 1.79 | 2.00 |
| Dwarves | 5.00 | 19 | 1.71 | 2.00 |
| Emergent | 4.50 | 15 | **N/A** | **N/A** |
| Exchange | 4.17 | 15 | **N/A** | **N/A** |
| Crucible | 4.00 | 17 | **N/A** | **N/A** |
| Ossuarium | 4.00 | 15 | 1.33 | 2.00 |
| Vestige-Bloodlines | 3.88 | 17 | 1.50 | 2.00 |
| Wyrd Conclave | 3.73 | 15 | **N/A** | **N/A** |
| Nomads | 3.60 | 13 | **N/A** | **N/A** |
| Elves | 3.00 | 16 | **N/A** | **N/A** |

**Key Finding:** Base damage does NOT correlate with win rate. Church has highest average damage (5.25) but lowest WR (33.3%). Bloodlines has low average damage (3.88) but highest WR (82.2%).

**Conclusion:** **Resource economies dominate balance, not base damage.**

---

### 2. RESOURCE ECONOMY ANALYSIS

| Faction | Token Economy | Card Advantage | Damage Buffs | On-Kill Synergies | Passives |
|---------|--------------|----------------|--------------|-------------------|----------|
| **Vestige-Bloodlines** | **15 cards** | 5 cards | **9 cards** | 4 cards | 3 cards |
| **Ossuarium** | 2 cards | **12 cards** | 2 cards | **5 cards** | 0 cards |
| **Wyrd Conclave** | **15 cards** | **15 cards** | **N/A** | **N/A** | **N/A** |
| Church | 6 cards | 5 cards | 4 cards | 4 cards | 0 cards |
| Dwarves | 6 cards | 0 cards | 6 cards | 2 cards | 2 cards |
| Crucible | **N/A** | 8 cards | **N/A** | 2 cards | **N/A** |
| Emergent | **N/A** | 7 cards | **N/A** | 2 cards | **N/A** |
| Exchange | **N/A** | 7 cards | **N/A** | 3 cards | **N/A** |
| Nomads | **N/A** | 6 cards | **N/A** | 1 card | **N/A** |
| Elves | **N/A** | 1 card | **N/A** | 2 cards | **N/A** |

**Critical Insight:**

- **Top 4 factions (77-82% WR):** All have extensive token economies (12-15 cards)
- **Bottom 3 factions (20-33% WR):** Weak or broken token economies (0-6 cards)

**Pattern:** Token economy size directly correlates with win rate.

---

### 3. EQUIPMENT DAMAGE ANALYSIS

| Faction | Equipment Cards | Damage Cards | Avg Equipment Damage | Notes |
|---------|----------------|--------------|---------------------|-------|
| **Emergent** | 11 | 6 | **8.17** | Highest by far |
| **Nomads** | 11 | 7 | **6.29** | High but WR still low |
| **Elves** | 11 | 6 | 4.83 | Ranged advantage |
| **Dwarves** | 11 | 7 | 4.86 | Solid but WR 20% |
| **Ossuarium** | 11 | 6 | 4.67 | Paired with lifesteal |
| **Crucible** | 11 | 6 | 4.67 | Balanced |
| **Church** | 13 | 9 | 4.44 | Most cards, lowest WR |
| **Exchange** | 11 | 6 | 4.17 | Economy compensates |
| **Universal** | 22 | 12 | **7.42** | Mixed faction cards |

**Key Finding:** Emergent has 8.17 average equipment damage (94% higher than Church's 4.44), yet Church has more total damage cards (9 vs 6).

**Imbalance Identified:** Emergent equipment is severely overstatted compared to other factions.

---

## Problem Faction Deep Dive

### 🚨 OSSUARIUM (64% → 77.8% WR)

**Why Still Strong After Lifesteal "Nerf"?**

#### Card Economy
- **Deck Recovery:** 12 cards (highest of any faction)
- **On-Kill Synergies:** 5 cards (tied for highest)
- **Equipment Damage:** 4.67 average (middle of pack)

#### The Lifesteal Paradox
In v5.20, **fixing the broken lifesteal mechanic actually NERFED Ossuarium** by 11.1%:

- **v5.19 (broken):** 88.9% WR - Lifesteal didn't work (empty discard pile)
- **v5.20 (working):** 77.8% WR - Lifesteal works but generates Taint penalties

**How It Works:**
1. Lifesteal recovers 50% of damage dealt (e.g., 4 damage = 2 cards)
2. Each recovery generates Taint tokens
3. 3+ Taint = +1 Heat + 1 damage per turn
4. 5+ Taint = +2 Heat + 1 damage per turn

**Net Effect:** 50% lifesteal with penalties < 100% lifesteal without penalties

#### Why Still Overpowered?
1. **12 deck recovery cards** provide sustainability beyond lifesteal
2. **5 on-kill synergies** create snowball effect
3. **Low-cost lifesteal cards** (Soul Reaper 3 SP) provide efficient sustain
4. Taint penalties not harsh enough (only 2-4 damage per battle)

#### Solution
- Increase Taint penalties: 3+ Taint = +2 damage (not +1), 5+ Taint = +3 damage
- OR reduce equipment damage by -1 across the board
- OR reduce lifesteal to 33% (1/3 damage recovered)

---

### 🚨 VESTIGE-BLOODLINES (69% → 82.2% WR)

**Why Consistently Overpowered?**

#### Card Economy - THE PROBLEM
- **Token Economy:** 15 cards (highest in game)
- **Damage Buffs:** 9 cards (more than any other faction)
- **Card Advantage:** 5 cards
- **On-Kill Synergies:** 4 cards
- **Passives:** 3 cards (strongest passive suite)

#### The Biomass Problem
**Key Card: Vestige Heritage (Passive)**
> "When ANY Casket (enemy, ally, or neutral) is destroyed within 6 hexes of you, gain 2 Biomass tokens"

**Snowball Effect:**
1. Every kill = 2 Biomass tokens
2. Biomass spends at 1-2 per card
3. By mid-game, 6-10 Biomass tokens accumulated
4. Cards like "Devouring Maw" (3 Biomass cost, 5 damage + 3 Biomass gain on kill + recover 2 cards) create infinite loops

**Historical Data (30,600 battles):**
- Biomass 8/10/12 damage: **73-82% WR** (tested 3 separate times)
- Biomass 7/9/11 damage: **40-48% WR** (current v5.16 data)
- **Current v5.20:** 82.2% WR (reverted to broken values?)

#### Synergistic Overload
Bloodlines has:
- **Pack Instinct (Passive):** +1 damage when attacking adjacent to allies
- **Predator's Mark:** +2 damage against marked Prey
- **Alpha's Command:** All allies +1 damage and +1 movement
- **Feral Rage:** +3 damage (but can't use defense/movement)
- **Adaptive Evolution:** Gain mutation counters on damage taken

**Problem:** Too many stacking damage buffs. A single attack can have:
- Base: 4 damage
- Pack Instinct: +1
- Predator's Mark: +2
- Feral Rage: +3
- **Total: 10 damage** (250% of base)

#### Solution
1. **Nerf Biomass generation:** 2 → 1 Biomass per kill
2. **Cap damage buffs:** Maximum +4 from all sources (not unlimited stacking)
3. **Reduce equipment damage:** -1 across the board
4. **Nerf Predator's Mark:** +1 damage (not +2)

---

### 🚨 CHURCH OF ABSOLUTION (27% → 33.3% WR)

**Why Did It Collapse?**

#### Card Economy - BROKEN
- **Token Economy:** 6 cards (weak)
- **Damage Buffs:** 4 cards (weak)
- **Card Advantage:** 5 cards (average)
- **On-Kill Synergies:** 4 cards (average)
- **Passives:** 0 cards (none!)

#### The Self-Harm Trap
**Design Intent:** Trade HP (cards) for damage bonuses
**Reality:** Self-harm costs without payoff

**Example Cards:**
1. **Blood Offering (0 SP):** Discard 1 card, next attack +2 damage, -1 target number
2. **Martyrdom Protocol (0 SP):** Redirect damage to yourself, gain 1 Heat
3. **Righteous Fury (Passive):** Each ally death = +1 damage permanently

**Problem:** Self-harm costs are IMMEDIATE, payoffs are DELAYED/CONDITIONAL

**Math:**
- Blood Offering: Discard 1 card to gain +2 damage on next attack
- If attack misses (43% chance in v5.20), you wasted 1 card for nothing
- If attack hits for base 4 + 2 = 6 damage, you traded 1 HP for 2 HP damage (net +1)
- **Break-even scenario requires 100% hit rate**

#### Why v5.16 Made It Worse
**v5.15 → v5.16 Changes:**
- Ossuarium nerfed -1 damage → fights end faster
- Faster fights = less time to accumulate self-harm bonuses
- Church went from 24.4% → 15.6% WR (-8.8%)

**v5.19 → v5.20 Recovery:**
- Card cycling fixed → discard bonuses actually work
- Church went from 20.0% → 33.3% WR (+13.3%)
- Still 17% below target WR

#### The Equipment Problem
Church has:
- **Most equipment cards:** 13 (vs 11 average)
- **Most damage-dealing cards:** 9 (vs 6 average)
- **Lowest average damage:** 4.44 (vs 5.63 overall average)

**Problem:** Quantity without quality. More cards but each card is weaker.

#### Solution
1. **Increase self-harm payoffs:** Blood Offering +2 → +4 damage
2. **Add card recovery:** "Discard 2 cards → Recover 3 cards" mechanic
3. **Remove self-harm costs on defensive cards:** Martyrdom Protocol shouldn't cost Heat
4. **Buff equipment damage:** +1 across the board (4.44 → 5.44 average)

---

### 🚨 DWARVES (29% → 47% → 20% WR)

**What Changed? A Rollercoaster Story**

#### Win Rate Timeline
- **v5.14-v5.15:** 29% WR (very weak)
- **v5.16:** 47% WR (balanced!) - +18% improvement
- **v5.17-v5.19:** 31% WR (weak again) - -16% drop
- **v5.20:** 20% WR (critical weak) - -11% drop

**Question:** What happened in v5.16 that worked, then broke?

#### Card Economy
- **Token Economy:** 6 cards (Rune Counters)
- **Damage Buffs:** 6 cards (average)
- **Card Advantage:** 0 cards (lowest in game!)
- **Passives:** 2 cards (weak)

#### The Rune Counter Problem
**Design:** Defensive scaling via Rune Counters
- Max 3 counters
- Each counter: -1 damage taken (minimum 1 damage)
- Acquire via specific cards (slow generation)

**Problem:** Rune Counter economy is too slow and defensive-only

**Example Battle:**
- Turn 1-3: No runes (taking full damage)
- Turn 4: Gain 1 rune (-1 damage reduction)
- Turn 7: Gain 2 runes (-2 damage reduction)
- Turn 10: Gain 3 runes (-3 damage reduction)
- **But the enemy has been hitting you for 4-6 damage the entire time**

**Math:**
- Runes reduce incoming damage by 1-3 per hit
- Typical battle: 8-12 enemy attacks
- Runes active for ~50% of battle
- Total damage prevented: 4-6 cards
- **Meanwhile, you're dealing normal damage with no offensive scaling**

#### What Worked in v5.16?
**Hypothesis:** Unknown changes to equipment or simulator mechanics temporarily benefited Dwarves.

**Evidence:**
- v5.16 notes mention "Equipment changes were faction-neutral"
- Dwarves have 4.86 average equipment damage (2nd highest for faction cards)
- Possible that meta shifts (Ossuarium weaker) helped Dwarves

**What Broke After v5.16?**
- v5.17: "Catastrophic multi-buff" - buffed 4 factions at once
- Dwarves not among buffed factions → relatively weaker
- v5.20: Card cycling bug fixed → faster battles → less time to stack runes

#### Equipment Analysis
Dwarves have:
- **Equipment damage:** 4.86 average (3rd highest)
- **Damage cards:** 7 (tied for most)
- **Top damage:** Anvil Breaker (7), Runic Smash (6)

**Not the problem.** Equipment is fine.

#### Solution
1. **Increase rune generation:** Gain 1 rune per attack (not just specific cards)
2. **Increase rune cap:** 3 → 5 counters
3. **Add offensive scaling:** Each rune counter also grants +1 damage OR -1 SP cost
4. **Add card draw:** Dwarves have 0 card advantage mechanics (worst in game)

---

## Key Imbalances Identified

### 1. Resource Economy Dominance

**Data:**
- Factions with 12-15 token economy cards: 77-82% WR
- Factions with 0-6 token economy cards: 20-33% WR
- **Gap: 47-62% WR difference**

**Root Cause:** Token economies provide:
1. Damage scaling (Biomass, Credits, Forge tokens)
2. Defensive scaling (Rune Counters, Taint resistance)
3. Card advantage (Bargain tokens, discard recovery)

**Imbalance:** Factions without strong economies can't compete.

---

### 2. Equipment Damage Variance

**Data:**
- Emergent: 8.17 average damage
- Church: 4.44 average damage
- **Gap: 84% higher damage for Emergent**

**Problem:** Equipment is supposed to be balanced across factions, but some factions have 2x the damage of others.

**Impact:**
- Emergent 60% WR despite no token economy
- Church 33% WR despite most equipment cards

---

### 3. Damage Efficiency vs Win Rate Mismatch

**Expected:** Higher damage efficiency → higher win rate
**Reality:**
- Church: 1.79 efficiency, 33.3% WR
- Bloodlines: 1.50 efficiency, 82.2% WR

**Conclusion:** Damage efficiency is MEANINGLESS when economies exist.

---

### 4. Card Advantage Imbalance

**Data:**
- Ossuarium: 12 deck recovery cards
- Dwarves: 0 card advantage cards
- **Gap: Infinite vs zero**

**Impact:**
- Ossuarium can sustain 30+ turn battles
- Dwarves run out of cards by turn 20-25
- Win rate gap: 57.8% (77.8% vs 20%)

---

### 5. Passive Ability Inequality

**Data:**
- Bloodlines: 3 passives (Vestige Heritage, Pack Instinct, Scent of Blood)
- Church: 0 passives
- Dwarves: 2 passives (weak)

**Impact:** Passives provide "free" value every turn. Bloodlines gains 2 Biomass per kill passively, while Church has to actively self-harm for bonuses.

---

## Missing Mechanics & Broken Synergies

### 1. Church - Missing Self-Harm Payoff
**Cards:** 8 self-harm or ally-death cards
**Payoff:** 4 cards that reward self-harm
**Problem:** 2:1 cost-to-reward ratio

**Examples:**
- Blood Offering: Cost 1 card → gain +2 damage once
- Martyrdom Protocol: Cost HP → gain 1 Heat (not a benefit)
- Righteous Fury: Requires ally deaths (unreliable)

**Solution:** Add "Discard 2 → Recover 3" loop mechanic

---

### 2. Dwarves - Missing Card Draw
**Cards:** 0 card draw mechanics
**Problem:** Cannot sustain long battles, Rune Counter scaling never reaches full potential

**Solution:** Add "Gain 1 Rune → Draw 1 card" mechanic

---

### 3. Nomads - Missing Everything
**Cards:** 6 resource economy cards (below average)
**Problem:** No token economy, no card advantage, average damage

**Toolkit:**
- Movement: Doesn't work in simulator
- Hit-and-run: Requires positioning (doesn't work in simulator)
- Scavenging: Only 3 cards

**Solution:** Add passive sustain (+1 HP per attack) or token economy (Momentum tokens)

---

### 4. Bloodlines - Snowball Loop
**Cards:** 15 token economy cards, 9 damage buffs, 4 on-kill synergies
**Problem:** Too many synergies create exponential scaling

**Example Combo:**
1. Vestige Heritage: Kill enemy → gain 2 Biomass (passive)
2. Devouring Maw: Spend 3 Biomass → deal 5 damage → if kill, gain 3 Biomass + recover 2 cards
3. Net result: 0 Biomass cost, deal 5 damage, recover 2 cards, repeatable

**Solution:** Cap Biomass generation at 1 per kill OR remove on-kill recovery loops

---

### 5. Ossuarium - Infinite Sustain
**Cards:** 12 deck recovery cards, 5 on-kill synergies
**Problem:** Too many ways to recover cards

**Example Cards:**
- Soul Harvest: Deal 4 damage, recover 4 cards (50% lifesteal)
- Corpse Fuel: Enemy dies → recover 5 cards
- Phylactery: When deck reaches 5 → recover 8 cards
- Grave Pact: Deal 6 damage, recover 6 cards (100% lifesteal on this card)

**Solution:** Reduce recovery amounts by 50% OR increase Taint penalties

---

## Comparative Economy Analysis

### Token Generation Rates (per battle)

| Faction | Token Type | Generation Rate | Spending Rate | Net Accumulation |
|---------|-----------|-----------------|---------------|------------------|
| **Bloodlines** | Biomass | 2 per kill (6-12 total) | 1-3 per card | +4-8 surplus |
| **Ossuarium** | Taint | 1 per lifesteal (4-8 total) | Penalty only | N/A |
| **Wyrd** | Bargain | 1 per turn (15-25 total) | 2-4 per card | +5-10 surplus |
| **Exchange** | Credits | 1 per 2 attacks (5-8 total) | 3-4 per card | Break-even |
| **Crucible** | Forge | 1 per lava hex (3-6 total) | 2-3 per card | Break-even |
| **Dwarves** | Rune | 1 per 3 turns (3-5 total) | Passive (defense) | N/A |
| **Church** | Heat | Penalty only | N/A | N/A |
| **Nomads** | None | N/A | N/A | N/A |
| **Elves** | Bleed | 1-2 per attack (6-12 total) | Passive (DoT) | N/A |
| **Emergent** | Metamorph | 1 per turn (15-25 total) | 5 per transform | +5-10 surplus |

**Key Insight:**
- **Surplus economies (Bloodlines, Wyrd, Emergent):** 70%+ WR
- **Break-even economies (Exchange, Crucible):** 48-51% WR
- **Penalty/no economies (Church, Dwarves, Nomads, Ossuarium):** 20-77% WR (wide variance)

**Ossuarium Exception:** 77.8% WR despite penalty economy because lifesteal + deck recovery compensate.

---

## Recommendations

### Critical Priority (Fix First)

#### 1. Nerf Vestige-Bloodlines (82.2% → 50%)
- **Biomass generation:** 2 → 1 per kill
- **Damage buff cap:** Maximum +4 from all sources
- **Equipment damage:** -1 across the board
- **Expected Impact:** 82.2% → 50-55% WR

#### 2. Nerf Ossuarium (77.8% → 50%)
- **Taint penalties:** 3+ Taint = +2 damage, 5+ Taint = +3 damage
- **Lifesteal:** 50% → 33% recovery
- **Deck recovery cap:** Maximum 4 cards per activation (already implemented)
- **Expected Impact:** 77.8% → 50-55% WR

#### 3. Buff Dwarves (20% → 45%)
- **Rune generation:** Gain 1 rune per attack (not per specific card)
- **Rune cap:** 3 → 5 counters
- **Add offensive scaling:** Each rune = +1 damage OR -1 SP cost
- **Add card draw:** "Gain rune → draw 1 card" mechanic
- **Expected Impact:** 20% → 40-45% WR

#### 4. Buff Nomads (28.9% → 45%)
- **Add passive sustain:** +1 HP per attack
- **Equipment damage:** +1 across the board
- **Add token economy:** Momentum tokens (gain 1 per movement, spend for +damage)
- **Expected Impact:** 28.9% → 40-45% WR

#### 5. Buff Church (33.3% → 45%)
- **Self-harm payoffs:** Double all bonuses (Blood Offering +2 → +4 damage)
- **Add recovery loop:** "Discard 2 → Recover 3" mechanic
- **Remove defensive costs:** Martyrdom Protocol no Heat cost
- **Equipment damage:** +1 across the board
- **Expected Impact:** 33.3% → 40-45% WR

---

### Secondary Priority (After Critical Fixes)

#### 6. Minor Nerf Emergent (60% → 50%)
- **Equipment damage:** -1 on highest cards (8-10 → 7-9)
- **Expected Impact:** 60% → 52-55% WR

#### 7. Minor Nerf Wyrd (55.6% → 50%)
- **Bargain spending costs:** +1 across the board
- **Expected Impact:** 55.6% → 50-52% WR

#### 8. Buff Elves (42.2% → 48%)
- **Bleed damage:** 1 → 2 per stack per turn
- **Bleed application:** +1 stack on all attacks (not just specific cards)
- **Expected Impact:** 42.2% → 46-50% WR

---

## Balance Philosophy Insights

### What We've Learned

1. **Resource economies dominate balance** - Token generation/spending is 10x more important than base damage
2. **Equipment variance is massive** - 84% damage gap between factions (Emergent vs Church)
3. **Lifesteal is multiplicatively powerful** - Damage + recovery = 2x value per attack
4. **Self-harm requires 2:1 payoff ratio** - Church needs double rewards for costs
5. **Defensive scaling is weak** - Dwarves' rune counters can't keep up with offensive scaling
6. **Passive abilities are "free wins"** - Bloodlines' 3 passives vs Church's 0 = 49% WR gap

### Design Principles (Updated)

1. **All factions need a token economy** - Minimum 8-10 cards
2. **Token generation should be consistent** - Not kill-dependent (RNG)
3. **Damage buffs should cap** - Maximum +4-5 from all sources
4. **Equipment should be normalized** - ±10% variance max (not 84%)
5. **Self-harm needs 2:1 payoff** - Every 1 card cost = 2 cards value
6. **Defensive scaling needs offense** - Pure defense doesn't win games

---

## Conclusion

**Current State:** 2/10 factions balanced (20% success rate)

**Root Causes:**
1. **Resource economy imbalance** - 12-15 card economies vs 0-6 card economies
2. **Equipment damage variance** - 84% gap between highest and lowest
3. **Missing core mechanics** - Church/Dwarves/Nomads lack functional economies
4. **Snowball loops** - Bloodlines/Ossuarium have infinite scaling
5. **Passive inequality** - 0-3 passives per faction creates "free value" gaps

**Path to Balance:**
1. **Nerf top 2 (Bloodlines, Ossuarium)** - Cap economies and reduce recovery
2. **Buff bottom 3 (Dwarves, Nomads, Church)** - Add functional economies
3. **Normalize equipment** - ±10% variance maximum
4. **Test iteratively** - One faction per patch, 225 battles minimum
5. **Target 7-8/10 balanced** - 45-55% WR range

**Estimated Patches to Balance:** 3-4 iterations (v5.21-v5.24)

---

**Document Version:** 1.0
**Analysis Date:** October 20, 2025
**Data Sources:**
- `/workspaces/penance/docs/cards/complete-card-data.json` (v5.20)
- 30,600+ simulated battles (Rounds 1-17)
- Session summaries v5.15, v5.16, v5.20

**Next Steps:** Implement v5.21 balance changes targeting Bloodlines and Ossuarium nerfs.
