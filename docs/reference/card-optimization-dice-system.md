# Card Optimization for Dice System
## Penance: Absolution Through Steel

**Version**: 1.0 (Dice System Integration)
**Last Updated**: October 11, 2025

---

## Overview

The introduction of **Attack Dice (to-hit rolls)** and **Defense Dice (damage mitigation)** fundamentally changes card design philosophy. This document analyzes how existing cards interact with the new dice system and recommends optimizations.

---

## Key Changes from Dice System

### Before Dice System
- **Guaranteed hits**: All attacks always hit (no miss chance)
- **Deterministic damage**: Damage = Base - Defense (exact math)
- **No variance**: Same attack always dealt same damage

### After Dice System
- **To-hit rolls**: Attacks can miss (5+ base, modifiers stack)
- **Defense Dice variance**: Same damage can be blocked 0-100% of time
- **Critical effects**:
  - Strong Hits (+1 dmg on 7-8)
  - Critical Hits (+2 dmg on 9, bypass 1 Defense)
  - EXECUTION (10, auto-destroy component)
  - Catastrophic Failures (2, weapon jams)
- **Defense Dice effects**:
  - 💀 CRITICAL (+1 Component Damage per symbol, 17% chance)
  - 🔥 HEAT (+1 Heat, 17% chance)
  - ⚔️ PIERCE (no reactives, 17% chance)

---

## Card Type Analysis

### 1. HIGH-DAMAGE SINGLE-HIT ATTACKS

**Examples**:
- Divine Judgment (4 SP, 8 damage)
- Overhead Slash (3 SP, 8 damage, +1 Heat)
- Executioner's Blow (4 SP, 10 damage, must be <50% HP)

**How Dice Affect Them**:
- ✅ **Benefit from Strong Hits**: 8 damage → 9 on Strong Hit (7-8 roll)
- ✅ **Benefit from Critical Hits**: 8 damage → 10 on Critical (9 roll)
- ✅ **High damage = more Defense Dice rolled**: 8 damage = roll 8 Defense Dice = higher chance of blocks
- ❌ **Single big hit can miss**: Wasting 4 SP on a miss is devastating

**Recommendation**:
- **KEEP AS-IS**, but add rider effects to make misses less punishing
- **NEW DESIGN**: Add "On Miss: Gain +2 damage to next attack" or "On Miss: Recover 2 SP"

**Optimized Version**:
```
Divine Judgment (Church)
Cost: 4 SP
Range: Melee
Effect: Deal 8 damage, ignore Defense
On Miss: Recover 2 SP (you gather divine wrath for next strike)
```

---

### 2. MULTI-HIT ATTACKS

**Examples**:
- Whirlwind (3 SP, Deal 4 damage to all adjacent enemies)
- Earthshaker (3 SP, Deal 3 damage to all adjacent, push 1 hex)

**How Dice Affect Them**:
- ✅ **Spread risk**: Instead of 1 attack with 10 damage, 3 attacks with 3 damage each
- ✅ **Multiple to-hit rolls**: If one misses, others may still hit
- ❌ **Lower damage per hit = less likely to trigger Strong/Critical**: 3 damage attacks rarely hit 7-8-9 on dice
- ✅ **AoE bypasses positioning**: Don't need to flank, just be adjacent

**Recommendation**:
- **BUFF AoE ATTACKS** slightly to compensate for multiple to-hit rolls
- **NEW DESIGN**: AoE attacks get -1 to target number (easier to hit) OR "Cannot miss" rider

**Optimized Version**:
```
Earthshaker (Dwarves)
Cost: 3 SP
Range: Melee (all adjacent)
Effect: Deal 3 damage to all adjacent enemies, push 1 hex
Special: Attacks cannot miss (ground eruption guaranteed)
```

---

### 3. DEFENSIVE/REACTIVE CARDS

**Examples**:
- Brace for Impact (0 SP, Reactive, reduce damage by 2)
- Deflect (1 SP, Reactive, reduce damage by 2)
- Unbreakable (1 SP, Reactive, reduce damage by 3)
- Shield Wall (2 SP, +3 Defense until next turn)

**How Dice Affect Them**:
- ✅ **Synergize with Defense Dice**: Defense bonuses + Defense Dice blocks stack
- ❌ **Less valuable** now that Defense Dice provide 33% block chance baseline
- ⚔️ **PIERCE symbols** (Defense Die face) disable reactive cards (17% chance)
- ✅ **Still necessary** for guaranteed damage reduction (Defense Dice are RNG)

**Recommendation**:
- **BUFF REACTIVE CARDS** to be more powerful than Defense Dice alone
- **NEW DESIGN**: Add rider effects to compete with natural Defense Dice variance

**Optimized Versions**:
```
Brace for Impact (Universal)
Cost: 0 SP, Reactive
Effect: Reduce damage by 2 AND reroll all 💀 CRITICAL symbols on Defense Dice
(Prevents Component Damage spikes)

Deflect (Buckler Shield)
Cost: 1 SP, Reactive
Effect: Reduce damage by 2 AND reroll up to 3 Defense Dice
(Gives control over RNG)

Unbreakable (Dwarves)
Cost: 1 SP, Reactive
Effect: Reduce damage by 3 AND ignore all ⚔️ PIERCE symbols (can still use other reactives)
(Counterplay to Pierce)
```

---

### 4. ACCURACY-BOOSTING CARDS

**Currently Missing** - These should exist now that to-hit matters!

**New Card Type Needed**: Cards that improve to-hit rolls

**Design Examples**:
```
Precision Strike (Universal - NEW)
Cost: 1 SP
Range: Melee or Ranged
Effect: Next attack gains -2 to target number (easier to hit)
"Aim carefully. Strike true."

Targeting Systems (Equipment Sigil - NEW)
Cost: 2 SP
Effect: Passive - All ranged attacks gain -1 to target number
"Advanced optics compensate for distance."

Focus Fire (Tactic - NEW)
Cost: 0 SP
Effect: Once per turn, reroll 1 Attack Die
"When it matters, concentrate."
```

**Recommendation**: **ADD 3-5 ACCURACY CARDS PER FACTION**

---

### 5. GUARANTEED-HIT EFFECTS

**Examples** (none currently exist, but should):
- Currently: ALL attacks roll to-hit

**New Design Philosophy**: Some attacks should auto-hit to reduce RNG frustration

**Design Examples**:
```
Point-Blank Shot (Pistol)
Cost: 2 SP
Range: 1 hex (adjacent only)
Effect: Deal 4 damage. This attack cannot miss (muzzle pressed against target).
"At this range, even corpses don't miss."

Grapple Strike (Melee)
Cost: 2 SP
Range: Melee
Effect: Deal 3 damage. This attack cannot miss. Target cannot move next turn.
"You grabbed them. They're not going anywhere."

Area Denial (Tactic)
Cost: 3 SP
Range: Aura 2
Effect: Deal 2 damage to all enemies in range. This attack cannot miss (explosive payload).
```

**Recommendation**: **ADD 2-3 AUTO-HIT CARDS PER FACTION** (premium cost, lower damage)

---

### 6. CARDS THAT MANIPULATE TO-HIT

**Currently Missing** - These should exist!

**Design Examples**:
```
Smoke Grenade (Universal - NEW)
Cost: 1 SP
Range: 3 hexes
Effect: Create 3-hex smoke cloud. All attacks through this hex get +2 to target number.
Duration: 2 Rounds
"Obscure the battlefield."

Blinding Light (Church)
Cost: 2 SP
Range: 3 hexes
Effect: Target gets +2 to all their attack to-hit numbers until their next turn (harder for them to hit).
"The light of judgment blinds the wicked."

Tremor (Dwarves)
Cost: 2 SP
Range: Self
Effect: All adjacent enemies get +1 to target number on attacks this turn (ground shakes, harder to aim).
```

**Recommendation**: **ADD TERRAIN/STATUS CARDS** that affect to-hit modifiers

---

### 7. CARDS THAT INTERACT WITH DEFENSE DICE

**Currently Missing** - These should exist!

**Design Examples**:
```
Lucky Charm (Equipment Accessory - NEW)
Cost: Passive
Effect: Once per turn, reroll up to 2 Defense Dice
"Fortune favors the prepared."

Armor-Piercing Rounds (Ammunition - NEW)
Cost: 2 SP
Effect: Your next ranged attack: All defender's Defense Dice showing 🛡️ SHIELD become 🩸 FLESH WOUND instead.
"Hardened tips punch through plating."

Runic Warding (Dwarves)
Cost: 2 SP
Effect: Until your next turn, convert all 💀 CRITICAL symbols to 🛡️ SHIELD symbols on Defense Dice.
"Ancient runes deflect fate itself."

Heat-Seeking Munitions (Tech - NEW)
Cost: 3 SP
Effect: Your next attack: For each 🔥 HEAT symbol on Defense Dice, deal +1 additional damage.
"Their own heat betrays them."
```

**Recommendation**: **ADD DEFENSE DICE MANIPULATION CARDS**

---

## Specific Card Revisions

### Church Faction

**Blood Offering (Current)**:
```
Cost: 0 SP
Effect: Discard 2 cards, next attack +3 damage, ignore 1 Armor
```

**Blood Offering (Optimized for Dice)**:
```
Cost: 0 SP
Effect: Discard 2 cards, next attack:
  - +3 damage
  - Ignore 1 Defense
  - Gain -1 to target number (easier to hit, blood sacrifice improves aim)
Reasoning: Self-harm should guarantee the attack lands
```

---

**Righteous Fury (Current)**:
```
Passive: +1 damage per enemy killed (permanent)
```

**Righteous Fury (Optimized)**:
```
Passive:
  - +1 damage per enemy killed (permanent)
  - For each kill, gain -1 to target number on your next attack (max -3)
Reasoning: Killing spree improves confidence = better aim
```

---

### Dwarven Faction

**Crushing Blow (Current)**:
```
Cost: 2 SP
Effect: Deal 4 damage, ARMOR PIERCING - ignore all Defense
```

**Crushing Blow (Optimized for Dice)**:
```
Cost: 2 SP
Effect: Deal 4 damage
Special: ARMOR PIERCING - ignore all Defense bonuses
Improved: On Strong Hit (7-8) or Critical (9+), deal double damage (8-12 dmg)
Reasoning: Armor-piercing attacks should capitalize on good rolls
```

---

**Rune of Protection (Current)**:
```
Cost: 2 SP
Effect: Gain 1 Rune Counter (max 3), reduce all damage by 1 per counter
```

**Rune of Protection (Optimized)**:
```
Cost: 2 SP
Effect: Gain 1 Rune Counter (max 3)
  - Reduce all damage by 1 per counter
  - For each Rune Counter, reroll 1 Defense Die showing 💀 CRITICAL
Reasoning: Runes should protect against critical failures
```

---

### Universal Cards

**Move (Current)**:
```
Cost: 1 SP
Effect: Move 2 hexes
```

**Move (Optimized - NO CHANGE)**:
```
Cost: 1 SP
Effect: Move 2 hexes
Reasoning: Movement doesn't need dice interaction
```

---

**Sprint (Current)**:
```
Cost: 2 SP
Effect: Move 4 hexes, +1 Heat
```

**Sprint (Optimized)**:
```
Cost: 2 SP
Effect: Move 4 hexes, +1 Heat
Penalty: Next attack this turn gets +1 to target number (harder to hit while sprinting)
Reasoning: Sprinting should have accuracy penalty
```

---

**Focus (Current)**:
```
Cost: 0 SP
Effect: Draw 1 card
```

**Focus (Optimized)**:
```
Cost: 0 SP
Effect: Draw 1 card OR Reroll 1 Attack Die on your next attack
Reasoning: "Focus" should improve accuracy, not just card draw
```

---

## Card Design Principles for Dice System

### 1. Mitigate Whiff Risk
**Problem**: Missing a 4 SP attack feels terrible
**Solution**: High-cost attacks should have miss compensation
- "On Miss: Recover 2 SP"
- "On Miss: Gain +2 damage to next attack"
- "Reroll 1 Attack Die" rider effects

### 2. Reward Good Rolls
**Problem**: Rolling 9-10 should feel amazing
**Solution**: Cards that synergize with Strong Hits/Criticals
- "On Critical Hit: Push target 2 hexes"
- "On Strong Hit: Draw 1 card"
- "On EXECUTION: Recover all SP"

### 3. Punish Bad Rolls (For Opponent)
**Problem**: Defender rolling all 💀 CRITICAL should feel devastating
**Solution**: Cards that exploit bad Defense Dice
- "For each 💀 CRITICAL on Defense Dice, deal +1 damage"
- "If defender rolls 3+ 🩸 FLESH WOUND, gain +1 SP"

### 4. Manipulate Probability
**Problem**: Pure RNG can feel unfair
**Solution**: Cards that give control over dice
- "Reroll up to 2 Defense Dice"
- "Reroll 1 Attack Die"
- "Convert 💀 CRITICAL to 🛡️ SHIELD"

### 5. Auto-Hit for Consistency
**Problem**: Some tactics need guaranteed damage
**Solution**: Premium-cost attacks that can't miss
- Point-blank attacks (adjacent only, cannot miss)
- AoE attacks (cannot miss, lower damage)
- Grapple/melee clinch (cannot miss, utility effect)

---

## Recommended New Card Types

### 1. Accuracy Cards (5-8 per faction)
- Reduce to-hit target number by 1-2
- Reroll Attack Dice
- "Cannot miss" riders on specific conditions

### 2. Defense Dice Manipulation (5-8 per faction)
- Reroll Defense Dice
- Convert symbols (💀 → 🛡️)
- Block-all cards (expensive, block all damage regardless of Defense Dice)

### 3. Punisher Cards (3-5 per faction)
- Trigger on opponent's bad rolls
- "If defender rolls 3+ 🩸, draw 1 card"
- "For each 💀 rolled, gain +1 Heat on opponent"

### 4. Gambler Cards (2-3 per faction)
- High risk, high reward
- "Roll 1 Attack Die. If 💀, deal 10 damage. Otherwise, miss."
- "Discard top 5 Defense Dice results, apply only the best 3"

### 5. Terrain Manipulation (3-4 per faction)
- Create smoke (+2 to target number through it)
- Tremors (+1 to target number for enemies)
- Blinding effects

---

## Balance Considerations

### Expected Hit Rates

**Base To-Hit (5+ on 2d6)**:
- Stationary, short range, no modifiers: **72% hit rate**
- Medium range (4-6 hexes): **58% hit rate** (+1)
- Long range (7-10 hexes), moved 4 hexes: **42% hit rate** (+2+1)
- Long range, moved, defender moved, cover: **28% hit rate** (+2+1+1+1)

**Design Implications**:
- **Low-cost attacks (1-2 SP)**: Accept 50-70% hit rate
- **High-cost attacks (3-4 SP)**: Should have accuracy buffs or miss compensation to hit 70-80%
- **Premium attacks (4+ SP)**: Should be near-guaranteed (auto-hit OR -2 to target number)

### Expected Defense Dice Blocks

**Per Die**: 33% block chance (🛡️ or ⚙️)

**Expected Blocks by Damage**:
- 3 damage = 1 block (33%) → 2 final damage
- 6 damage = 2 blocks (33%) → 4 final damage
- 9 damage = 3 blocks (33%) → 6 final damage
- 12 damage = 4 blocks (33%) → 8 final damage

**Design Implications**:
- **Burst damage (8-10)** is now **less reliable** (can be blocked to 5-7)
- **Sustained damage (multiple 3-4 dmg attacks)** is now **more consistent**
- **Auto-hit low-damage** may be better than **high-damage miss-risk**

---

## Faction-Specific Recommendations

### Church of Absolution (Aggressive Burst)

**Current Identity**: Self-harm for massive burst damage

**Dice System Problems**:
- Blood Offering (discard 2 cards) + big attack can **MISS** (feels terrible)
- Divine Judgment (4 SP, 8 dmg) can whiff

**Optimizations**:
1. **Blood Offering**: Add "-1 to target number" (sacrifice ensures aim)
2. **Divine Judgment**: Add "On Miss: Recover 2 SP and gain +3 damage to next attack"
3. **NEW CARD**: "Zealot's Focus" (1 SP, Reroll 1 Attack Die on next attack)
4. **NEW CARD**: "Martyr's Certainty" (2 SP, Next attack cannot miss but deals -2 damage)

---

### Dwarven Forge-Guilds (Defensive Tank)

**Current Identity**: Outlast with Rune Counters and armor

**Dice System Problems**:
- Rune Counters reduce damage, but Defense Dice ALSO reduce damage (redundant)
- Defense Dice provide 33% block baseline, diminishing value of +3 Defense from Shield Wall

**Optimizations**:
1. **Rune of Protection**: Add "Reroll 1 Defense Die showing 💀 per Rune Counter"
2. **Shield Wall**: Change to "+3 Defense AND convert all 🩸 to 🛡️ on Defense Dice"
3. **NEW CARD**: "Runic Fate" (2 SP, Reroll all Defense Dice once)
4. **NEW CARD**: "Stone Certainty" (Passive, 💀 CRITICAL symbols cannot destroy components)

---

### The Ossuarium (Lifesteal Vampire)

**Current Identity**: Soul Harvest (heal when dealing damage)

**Dice System Problems**:
- Lifesteal triggers on damage dealt, but Defense Dice reduce damage → less healing
- Missing attacks = no Soul Harvest

**Optimizations**:
1. **Soul Harvest**: Change to "Gain 1 HP per Attack Die showing 💀 DEATH BLOW (even if miss)"
2. **NEW CARD**: "Vampiric Precision" (1 SP, Next attack -1 to target number, heal 2 HP if hit)
3. **NEW CARD**: "Draining Touch" (2 SP, Cannot miss, deal 3 damage, heal 3 HP)
4. **NEW CARD**: "Death's Certainty" (Passive, Reroll 1 Attack Die per Decay card in deck)

---

### Elven Verdant Covenant (Bleed Stacking)

**Current Identity**: Stack Bleed counters, kite and poke

**Dice System Problems**:
- Bleed stacks require hitting multiple times → to-hit variance reduces reliability
- Low-damage attacks (2-3) are easier to fully block with Defense Dice

**Optimizations**:
1. **Thorn Strike**: Add "If this attack misses, apply 1 Bleed anyway" (thorns cut regardless)
2. **NEW CARD**: "Inevitable Decay" (2 SP, Cannot miss, deal 2 damage, apply 2 Bleed)
3. **NEW CARD**: "Poisoned Precision" (1 SP, Next attack -1 to target number and applies +1 Bleed)
4. **NEW CARD**: "Nature's Wrath" (Passive, For each Bleed on target, your attacks gain -1 to target number vs that target)

---

## Summary of Changes Needed

### HIGH PRIORITY (Do First)
1. **Add 5-8 Accuracy Cards** (Reroll Attack Dice, -1 to target number)
2. **Buff Reactive Cards** (Reroll Defense Dice, convert symbols)
3. **Add "On Miss" compensation** to high-cost attacks (4+ SP)
4. **Add 2-3 Auto-Hit cards** per faction (point-blank, grapple, AoE)

### MEDIUM PRIORITY (Do Second)
5. **Add Defense Dice manipulation** cards (Reroll, convert 💀 → 🛡️)
6. **Buff self-harm cards** (Blood Offering should guarantee hit)
7. **Add Strong Hit/Critical synergy** cards ("On Critical, do X")
8. **Add terrain manipulation** (smoke, tremors, blinding)

### LOW PRIORITY (Playtesting First)
9. **Gambler cards** (high-risk, high-reward)
10. **Punisher cards** (trigger on opponent's bad rolls)
11. **Rebalance AoE** (maybe make them auto-hit OR -1 to target number)

---

## Testing Checklist

After implementing changes, playtest for:
- [ ] Do high-cost attacks (4+ SP) feel worth the risk? (Target: 70-80% expected hit rate with buffs)
- [ ] Do reactive cards feel valuable? (Should feel better than relying on Defense Dice alone)
- [ ] Do self-harm mechanics feel fair? (Blood Offering shouldn't miss after sacrificing 2 cards)
- [ ] Do accuracy cards create meaningful choices? (Spend 1 SP for -1 to target number vs save SP)
- [ ] Does Defense Dice variance feel fair? (Target: Not TOO swingy, not too predictable)

---

**END OF DOCUMENT**

---

*"The dice giveth, and the dice taketh away. But the wise Pilot stacks the odds."*
