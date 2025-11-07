# Ossuarium Balance Analysis

## Current Performance
- **Multi-Unit Win Rate:** 68.9% (Target: 45-55%)
- **Status:** OVERPOWERED (+13.9% above target)
- **Rank:** #1 out of 10 factions

## Card Analysis (21 total faction cards)

### Attack Cards (9 cards)

| Card | Cost | Damage | Effect | Notes |
|------|------|--------|--------|-------|
| Siphon Essence | 2 | 2 | Recover cards = half damage dealt | Efficient |
| Death Grasp | 2 | 3 | Recover 1 card | Good value |
| Necrotic Touch | 2 | 2 | Recover 1 card (3 if kills) | Conditional |
| Bone Scythe Swing | 3 | 4 | Recover 1 card | Standard |
| Soul Harvest | 3 | 4 | Recover up to 3 cards | VERY STRONG |
| Corpse Explosion | 3 | 3 AoE | Recover 1/enemy (max 3) | Multi-target |
| Grave Pact | 3 | 6 | Discard 3, recover 2 next turn | Net -1 cards |
| Soul Rend | 4 | 5 | Recover up to 3 cards | Strong |
| Bone Scythe Reap | 4 | 3+2 AoE | Recover 1/enemy (max 3) | AoE value |
| Drain Life | 5 | 6 | Recover 4 cards | Massive heal |

**Average Attack Cost:** 3.0 SP
**Average Attack Damage:** 2.89 (middle-of-pack)

### Utility/Passive Cards (12 cards)

**Passives (4 cards):**
- **Phylactery** (0 SP): Auto-revive to 3 HP once per mission
- **Necrotic Surge** (0 SP): +1 card when recovering 3+
- **Vampiric Rune** (0 SP): +1 card when dealing 5+ damage
- **Soul Well** (0 SP): Recover 1 card if hand ≤5 at turn start

**Utility (8 cards):**
- **Corpse Fuel** (2 SP): Recover 3 cards when enemy dies nearby
- **Death Mark** (2 SP): +1 card per damage to marked target
- **Death Shroud** (2 SP): +1 card to ALL recovery this turn
- **Deathless Advance** (2 SP): Move 3, cap damage at 5
- **Reanimate** (4 SP): Summon skeleton minion (3 HP, 2 dmg)

**Reactive (2 cards):**
- **Bone Armor** (1 SP): Block 2 damage, recover 1 if blocked 2+
- **Corpse Shield** (1 SP): +3 Defense when nearby enemy dies

## Problem Identification

### ⚠️ Issue #1: Excessive Lifesteal/Recovery
**18 out of 21 cards** (86%) have card recovery effects:
- 9/9 attacks have lifesteal
- 4 passive multipliers
- 5 utility recovery cards

**Problem:** Even without simulation implementing lifesteal, the CARD TEXT promises players constant healing. This creates design expectations that are overpowered.

### ⚠️ Issue #2: Stacking Multipliers
Multiple cards stack recovery bonuses:
- **Death Mark** + **Soul Rend** = 5 damage → recover 3+1 = 4 cards
- **Death Shroud** + **Soul Harvest** = 4 damage → recover 3+1 = 4 cards
- **Necrotic Surge** triggers on most attacks (recover 3+ is common)
- **Vampiric Rune** triggers on 5+ damage attacks

**Example combo:** Death Mark + Death Shroud + Soul Rend (5 damage) + Vampiric Rune
= Recover 3 (base) +1 (Death Mark) +1 (Death Shroud) +1 (Vampiric Rune) = **6 cards from one attack**

### ⚠️ Issue #3: No Trade-offs
Most lifesteal cards have **no downside:**
- Soul Harvest: 3 SP, 4 damage, recover 3 cards (net +1 card advantage)
- Death Grasp: 2 SP, 3 damage, recover 1 card
- Bone Scythe Swing: 3 SP, 4 damage, recover 1 card

Compare to **Grave Pact** (the only one with a cost):
- 3 SP, 6 damage, but discard 3 cards first, recover 2 later (net -1 cards)

### ⚠️ Issue #4: Safety Nets
**Phylactery** + **Soul Well** create extreme durability:
- Phylactery: Auto-revive to 3 HP once per mission
- Soul Well: Passive card draw when hand is low

### Issue #5: Simulation Disconnect
**v5.23 removed lifesteal** from simulation, but Ossuarium still 68.9% WR:
- Cards promise lifesteal, simulation doesn't deliver
- Yet they're STILL overpowered
- This suggests the problem might be elsewhere (damage efficiency, passives, or Taint system less punishing than intended)

## Comparison to Other Factions

| Faction | Avg Attack Damage | Win Rate | Status |
|---------|-------------------|----------|--------|
| Church | 3.50 | 48.9% | Balanced |
| Ossuarium | 2.89 | 68.9% | Overpowered |
| Dwarves | 2.86 | 22.2% | Underpowered |
| Elves | 2.67 | 66.7% | Overpowered |
| Nomads | 2.25 | 35.6% | Underpowered |

**Ossuarium has middle-tier damage but highest win rate** - this suggests:
- Sustain/durability is more valuable than raw damage
- Passive abilities are very strong
- Multi-unit combat favors attrition strategies

## Recommended Balance Changes

### Option A: Reduce Recovery Amounts (Conservative)
1. **Cap all lifesteal at 2 cards maximum** (down from 3-4)
2. **Soul Harvest:** Recover up to 2 cards (down from 3)
3. **Soul Rend:** Recover up to 2 cards (down from 3)
4. **Drain Life:** Recover 3 cards (down from 4)
5. **Necrotic Surge:** Triggers only on recovering 4+ cards (not 3+)

### Option B: Add Costs/Trade-offs (Moderate)
1. **Add Taint costs to lifesteal:**
   - Recovering cards generates 1 Taint per 2 cards recovered
   - High Taint causes penalties (damage reduction, SP loss)
2. **Nerf passive stacking:**
   - Multiplier bonuses don't stack (only highest applies)
3. **Phylactery nerf:**
   - Revive to 2 HP (down from 3)
   - OR make it cost 2 SP to activate

### Option C: Fundamental Redesign (Aggressive)
1. **Limit lifesteal to HALF of attacks** (4-5 cards instead of 9)
2. **Remove stacking multipliers entirely:**
   - Delete Necrotic Surge OR Vampiric Rune
   - Death Shroud becomes "next recovery +1" not "all recovery +1"
3. **Make lifesteal conditional:**
   - "Recover 1 card if you dealt 4+ damage"
   - "Recover 1 card if target was marked"
4. **Add cooldowns:**
   - "Once per turn: Recover 1 card when dealing damage"

### Option D: Taint System Overhaul (Alternative)
Since simulation uses Taint instead of lifesteal:
1. **Implement Taint in card text:**
   - All lifesteal cards gain "Gain 1 Taint" clause
   - High Taint (6+) causes penalties:
     - All damage -1
     - SP costs +1
     - Heat +1 per turn
2. **Make Phylactery cost 3 Taint** to activate
3. **Add Taint purge mechanic** to other factions (counterplay)

## Recommended Changes (My Suggestion)

**Tier 1 - Immediate Nerfs:**
1. **Soul Harvest:** 3 SP, 4 damage, recover 2 cards (down from 3)
2. **Soul Rend:** 4 SP, 5 damage, recover 2 cards (down from 3)
3. **Drain Life:** 5 SP, 6 damage, recover 3 cards (down from 4)
4. **Phylactery:** Revive to 2 HP (down from 3)
5. **Necrotic Surge:** Triggers on recovering 4+ cards (down from 3+)

**Tier 2 - Add Costs:**
6. **All lifesteal attacks:** Add "Gain 1 Taint" to cards that recover 2+ cards
7. **Death Shroud:** Change to "Your next card recovery this turn +1" (not all recoveries)

**Tier 3 - Fix Simulation:**
8. **Implement Taint penalties** in simulation at 6+ Taint:
   - 6-8 Taint: All damage -1
   - 9-10 Taint: All damage -2, all costs +1

This should bring Ossuarium from 68.9% down to ~50-55% win rate.

## Testing Plan

1. Apply Tier 1 nerfs
2. Run simulation: `python3 faction_balance_MULTIUNIT.py`
3. If still >60% WR, apply Tier 2
4. If still >55% WR, apply Tier 3
5. Target: 48-52% win rate

---

**Analysis Date:** November 7, 2025
**Current Version:** v5.23 (lifesteal removed, Taint system)
**Data Source:** complete-card-data.json, equipment_simulator_dice.py
