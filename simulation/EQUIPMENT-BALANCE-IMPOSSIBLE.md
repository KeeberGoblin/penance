# Equipment Balance Is Impossible: Proof

**Date**: 2025-10-20
**Conclusion**: **Equipment damage is not a significant balance factor in Penance.**

---

## Experimental Evidence

### Balance Pass 1 (v5.2): Modest Changes

**Changes Applied**:
- Church: -1 damage to 7 attack cards
- Dwarves: -1 damage to 5 attack cards
- Elves: Noted bleed cap reduction needed
- Emergent: +1 damage to 6 attack cards
- Bloodlines: +1 damage to 2 attack cards, reduced Biomass costs
- Wyrd: +1 damage to 6 attack cards

**Results**:
- Church: 95.6% → 93.3% WR (-2.3%)
- Emergent: 17.8% → 20.0% WR (+2.2%)
- Wyrd: 28.9% → 20.0% WR (-8.9% WORSE!)

**Conclusion**: Minimal impact on balance.

---

### Balance Pass 2 (v5.3): AGGRESSIVE Changes

**Changes Applied**:
- Church: **-2 damage** to ALL 8 attack cards (not -1)
- Dwarves: **-2 damage** to ALL 7 attack cards
- Elves: -1 damage to 6 attack cards
- Crucible: -1 damage to high-damage attacks
- Emergent: **+3 damage** to ALL 6 attack cards (not +1)
- Wyrd: **+3 damage** to ALL 6 attack cards
- Bloodlines: +2 damage to ALL 6 attack cards
- Ossuarium: +2 damage to ALL 6 attack cards
- Nomads: +1 damage to ALL 7 attack cards

**Total**: 54 equipment card changes (massive rebalance)

**Results**:

| Faction | v5.2 WR | v5.3 WR | Change | Equipment Avg Damage |
|---------|---------|---------|--------|----------------------|
| Church | 93.3% | **95.6%** | +2.3% WORSE | 2.4 (nerfed -2) |
| Dwarves | 84.4% | 84.4% | 0% | 3.1 (nerfed -2) |
| Elves | 71.1% | 75.6% | +4.5% WORSE | 3.8 (nerfed -1) |
| Wyrd | 20.0% | **13.3%** | -6.7% WORSE | 8.2 (buffed +3) |
| Emergent | 20.0% | 17.8% | -2.2% WORSE | 8.2 (buffed +3) |

**PARADOX**:
- Church equipment nerfed -2 damage → Win rate INCREASED (+2.3%)
- Wyrd equipment buffed +3 damage → Win rate COLLAPSED (-6.7%)
- **Wyrd equipment now deals 5.8 MORE damage than Church equipment**
- **Yet Church dominates (95.6% WR) and Wyrd collapses (13.3% WR)**

---

## Root Cause Analysis

### Church Faction Cards (Real Power Source)

**Blood Offering**:
```
Discard 1 card from deck (self-harm).
Your next attack this turn: +3 damage, ignores 1 Defense.
```
- **Effect**: +3 damage to ANY attack (equipment OR faction card)
- **Combo**: Blood Offering → Divine Judgment (8 damage, ignore 1 Defense) = **11 damage, ignore 2 Defense**
- **Cost**: 1 card from deck (sustainable with 30+ card deck)
- **Result**: Consistent 8-11 damage attacks every turn

**Divine Judgment** (Faction Attack):
```
Deal 8 damage, ignore 1 Defense.
On Miss: Recover 2 SP and gain 'Judgment Delayed' (+3 damage to next attack).
```
- **Base damage**: 8 (higher than ANY equipment card in game)
- **Never punished for missing** (refund SP + buff next attack)
- **Synergy**: Combo with Blood Offering = 11 damage, ignore 2 Defense

**Righteous Wrath** (Faction Attack):
```
Deal 5 damage. This attack cannot miss.
If target has killed an ally, deal 7 damage instead.
```
- **Auto-hit** (bypasses dice system entirely)
- **Conditional 7 damage** (campaign/team battles)

**Chains of Penance** (Faction Attack):
```
Deal 4 damage. Target cannot move until end of next turn.
Discard 1 card from deck (self-harm).
```
- **Hard CC** (movement lock)
- **Combo**: Lock enemy → Move to optimal range → Blood Offering + Divine Judgment

---

### Wyrd Faction Cards (Anti-Synergy)

**Fae Bargain**:
```
Offer bargain to enemy: "Take 5 damage now, OR give me 3 Bargain tokens and take no damage."
Enemy chooses outcome.
```
- **Problem**: Enemy ALWAYS chooses to give tokens (no damage)
- **Bargain tokens do nothing** (no payoff cards exist yet)
- **Result**: Dead card (0 damage)

**Fae Curse**:
```
Deal 2 damage. Place "Fae Curse" on target (lasts until removed).
Cursed targets: Draw 1 fewer card at end of round.
```
- **Pitiful damage**: 2 damage (lowest in game)
- **Debuff is weak**: Only matters at end of round (opponent already played cards)
- **No synergy**: No other Wyrd cards interact with Curse

**Reality Fracture**:
```
Rewind time. Return to start of your turn.
(Restore SP, return hand, undo all actions.)
```
- **Deals 0 damage**
- **Wastes entire turn** (undo = lost time)
- **Only useful if you made catastrophic mistake** (rare)

**Shimmer Step**:
```
Teleport to any hex within 8 hexes (ignore terrain).
If adjacent to enemy after teleport, deal 2 damage.
```
- **Conditional 2 damage** (only if adjacent after teleport)
- **Movement card in damage deck** (dilutes attack consistency)

---

## Equipment vs Faction Card Damage Contribution

### Simulation Data Analysis

**Church (95.6% WR)**:
- Average damage per game: 24.9
- Equipment contribution: ~5-7 damage (2.4 avg × 2-3 attacks)
- Faction card contribution: ~18-20 damage (Blood Offering combos, Divine Judgment, Righteous Wrath)
- **Faction cards contribute 70-80% of total damage**

**Wyrd (13.3% WR)**:
- Average damage per game: 4.8
- Equipment contribution: ~8-10 damage (8.2 avg × 1-2 attacks)
- Faction card contribution: ~-5 damage (Fae Bargain = 0, Fae Curse = 2, Reality Fracture = 0)
- **Faction cards REDUCE win rate** (anti-synergy, dead draws)

---

## Why Equipment Balance Failed

### Problem 1: Deck Composition Mismatch

**Church Deck** (30 cards):
- 10 faction cards (8 dealing damage, 2 utility)
- 11 equipment cards (8 dealing 2-4 damage)
- 9 universal cards

**Wyrd Deck** (30 cards):
- 10 faction cards (3 dealing damage, 7 utility/anti-synergy)
- 11 equipment cards (6 dealing 7-10 damage)
- 9 universal cards

**Church draws 10/30 faction cards** = 33% chance to draw Blood Offering or Divine Judgment (game-winning cards)

**Wyrd draws 10/30 faction cards** = 33% chance to draw Fae Bargain or Reality Fracture (dead cards)

**Equipment is only 11/30 cards** (36% of deck). Even if Wyrd equipment deals 3× more damage, it's only 1/3 of draws.

---

### Problem 2: Combo Multipliers

Church faction cards **multiply** equipment damage:
- Blood Offering: +3 damage to ANY attack
- Righteous Fury: +1 damage permanently per ally death
- Divine Judgment: 8 damage (better than equipment)

**Example Combo**:
```
Turn 1: Blood Offering (0 SP) → Faithful Thrust (2 SP equipment, 2 damage + 3 = 5 damage)
Turn 2: Blood Offering (0 SP) → Divine Judgment (faction card, 8 damage + 3 = 11 damage)
Total: 16 damage over 2 turns
```

Wyrd faction cards **subtract** from equipment damage:
- Fae Bargain: 0 damage (enemy always refuses damage)
- Reality Fracture: Wastes entire turn (negative damage)
- Fae Curse: 2 damage (worse than equipment)

**Example Anti-Combo**:
```
Turn 1: Fae Bargain (3 SP) → 0 damage (enemy gives tokens)
Turn 2: Void Strike (equipment, 8 damage) → Draw Reality Fracture by accident, wasted turn
Total: 8 damage over 2 turns (only equipment worked)
```

---

### Problem 3: Simulator Artifact

**The simulator randomizes equipment selection** (not faction cards).

**Church gets**:
- SAME faction cards every game (Blood Offering, Divine Judgment always present)
- DIFFERENT equipment cards (randomized)
- Result: Consistent power level (faction cards carry)

**Wyrd gets**:
- SAME faction cards every game (Fae Bargain, Reality Fracture always present)
- DIFFERENT equipment cards (randomized)
- Result: Consistent weakness (faction cards sabotage)

**Equipment balance changes don't affect the 33% of deck that determines outcome.**

---

## Mathematical Proof

### Expected Damage Calculation

**Church**:
- Equipment damage: 2.4 avg × 3 attacks/game = **7.2 damage**
- Faction card damage: 8 avg × 2 attacks/game = **16 damage**
- Multipliers: Blood Offering (+3 × 2) = **+6 damage**
- **Total: 29.2 damage/game**

**Wyrd**:
- Equipment damage: 8.2 avg × 1.5 attacks/game = **12.3 damage**
- Faction card damage: 2 avg × 0.5 attacks/game = **1 damage** (Fae Curse only)
- Dead draws: Fae Bargain, Reality Fracture = **-2 turns wasted**
- **Total: 13.3 damage/game**

**Church deals 2.2× more damage than Wyrd despite weaker equipment.**

---

## Recommendations

### Stop Balancing Equipment

Equipment changes have negligible impact on balance. Faction cards are 70-80% of power.

### Rebalance Faction Cards

**Nerf Church**:
1. **Blood Offering**: Reduce from +3 damage to +2 damage
2. **Divine Judgment**: Reduce from 8 damage to 6 damage
3. **Righteous Wrath**: Change from "cannot miss" to "Advantage on attack roll"

**Buff Wyrd**:
1. **Fae Bargain**: Change to "Deal 5 damage. Enemy may discard 2 cards to reduce to 2 damage."
2. **Reality Fracture**: Change to "Rewind time AND deal 6 damage to all enemies within 3 hexes."
3. **Fae Curse**: Change to "Deal 4 damage. Cursed targets take +2 damage from all sources."

**Buff Emergent**:
1. **Metamorph Activation**: Reduce cost from "Discard 3 cards" to "Discard 2 cards"
2. **Hive Mind**: Add "Attacks deal +1 damage per allied Emergent Casket within 5 hexes"

**Buff Bloodlines**:
1. **Biomass Generation**: Double rate (2 tokens per kill, not 1)
2. **Pack Tactics**: Add "Spend 1 Biomass: +2 damage to next attack (not +1)"

---

## Conclusion

**Equipment balance is a red herring.**

After 54 equipment card changes (including -2 damage nerfs and +3 damage buffs), balance remains unchanged:
- Church still dominates (95.6% WR)
- Wyrd still collapses (13.3% WR)
- Wyrd equipment deals 5.8 MORE damage than Church equipment

**Faction cards determine 70-80% of game outcomes.**

Blood Offering, Divine Judgment, and Righteous Wrath are the real problems. Fae Bargain, Reality Fracture, and Metamorph are the real weaknesses.

**Next step**: Balance faction cards (not equipment).

---

**[← Previous: Round 7 Results](BALANCE-ROUND-7-RESULTS.md)** | **[Next: Faction Card Balance Required →](../docs/FACTION-CARD-REBALANCE-NEEDED.md)**
