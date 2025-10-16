# Dice Pool Advantage System
## Penance: Absolution Through Steel

**Version**: 3.0 (Trench Crusade-Inspired Enhancement)
**Last Updated**: October 14, 2025

---

## Overview

This system replaces static to-hit modifiers with a **dice pool mechanic** inspired by Trench Crusade's modifier system. Instead of adding +1 or +2 to your target number, you roll extra dice and take the highest or lowest results.

**Why This Is Better**:
- More dramatic swings (chance of rolling double criticals increases)
- Feels more exciting (rolling more dice is fun!)
- Creates more variance at extremes (skilled attackers have higher crit chances)
- Compatible with existing Attack Dice system

---

## Core Mechanic

### Base Roll: 2 Attack Dice

**Standard attack** (no modifiers):
- Roll **2 Attack Dice**
- Add both values together
- Compare to target number (usually 5+)

---

### Advantage: Roll 3, Take Highest 2

**When you have tactical ADVANTAGE**:
- Roll **3 Attack Dice**
- **Discard the LOWEST die**
- Add the 2 highest values together

**Advantage Sources**:
- Flanking attack (hex-sides 3, 5)
- Rear attack (hex-side 4)
- Higher ground (1+ elevation)
- Target is Stunned/Immobilized
- Aiming (spent previous turn stationary, aiming at target)
- Target has 5+ Momentum Tokens

**Example**:
```
You're attacking from higher ground (Advantage)
Roll 3 Attack Dice: (3) + (5) + (0)
Discard lowest (): Keep (3) + (5) = 8 total
Result: Strong Hit! (+1 damage)
```

---

### Disadvantage: Roll 3, Take Lowest 2

**When you have tactical DISADVANTAGE**:
- Roll **3 Attack Dice**
- **Discard the HIGHEST die**
- Add the 2 lowest values together

**Disadvantage Sources**:
- Heavy cover (fortress walls, dense forest)
- Obscured target (smoke, darkness)
- Long range (7-10 hexes)
- Extreme range (11+ hexes)
- Attacker moved 6+ hexes this turn
- Attacker has 5+ Heat (Danger Zone)
- Attacker's Primary Weapon destroyed

**Example**:
```
You're shooting through heavy cover (Disadvantage)
Roll 3 Attack Dice: (3) + (5) + (4)
Discard highest (): Keep (3) + (4) = 7 total
Result: Strong Hit (but you discarded the , missed crit chance)
```

---

### Critical Advantage: Roll 4, Take Highest 2

**When you have MULTIPLE advantages** (2+ sources):
- Roll **4 Attack Dice**
- **Discard the 2 LOWEST dice**
- Add the 2 highest values together

**Critical Advantage Examples**:
- Rear attack (Advantage) + Higher ground (Advantage) = Critical Advantage
- Flanking (Advantage) + Target Stunned (Advantage) = Critical Advantage
- Aiming (Advantage) + Target has 5+ Momentum (Advantage) = Critical Advantage

**Why This Matters**:
- Dramatically increases chance of double (EXECUTION: auto-destroy component)
- Rewards perfect tactical positioning
- Creates "alpha strike" moments

**Example**:
```
You're attacking rear (Advantage) from higher ground (Advantage) = Critical Advantage
Roll 4 Attack Dice: (3) + (5) + (5) + (4)
Discard 2 lowest (, ): Keep (5) + (5) = 10 total
Result: EXECUTION! Auto-destroy component, bypass all Defense!
```

---

### Critical Disadvantage: Roll 4, Take Lowest 2

**When you have MULTIPLE disadvantages** (2+ sources):
- Roll **4 Attack Dice**
- **Discard the 2 HIGHEST dice**
- Add the 2 lowest values together

**Critical Disadvantage Examples**:
- Heavy cover (Disadvantage) + Long range (Disadvantage) = Critical Disadvantage
- Moved 6+ hexes (Disadvantage) + Target in smoke (Disadvantage) = Critical Disadvantage
- Primary Weapon destroyed (Disadvantage) + 5+ Heat (Disadvantage) = Critical Disadvantage

**Why This Hurts**:
- Very high chance of missing or jamming
- Almost impossible to get Strong Hits or Crits
- Forces you to reposition or wait for better opportunity

**Example**:
```
You're shooting through heavy cover (Disadvantage) at long range (Disadvantage) = Critical Disadvantage
Roll 4 Attack Dice: (3) + (5) + (0) + (1)
Discard 2 highest (, ): Keep (0) + (1) = 1 total
Result: CATASTROPHIC FAILURE! Weapon jams, +2 Heat, next attack -2 damage
```

---

## Advantage/Disadvantage Interactions

### If You Have BOTH Advantage and Disadvantage:

**They CANCEL OUT (1-for-1)**:
- 1 Advantage + 1 Disadvantage = **Straight Roll** (2 dice, no change)
- 2 Advantages + 1 Disadvantage = **Advantage** (net +1, roll 3 take highest 2)
- 1 Advantage + 2 Disadvantages = **Disadvantage** (net -1, roll 3 take lowest 2)

**Example**:
```
Attacking from higher ground (Advantage) through heavy cover (Disadvantage)
Net: 0 (cancel out)
Roll 2 Attack Dice normally
```

**Example 2**:
```
Rear attack (Advantage) from higher ground (Advantage) but target in heavy cover (Disadvantage)
Net: +1 Advantage (2 - 1 = 1)
Roll 3 Attack Dice, take highest 2
```

---

## Probability Math (Why This Works)

### Chance of Strong Hit or Better (7+):

**Straight Roll (2d6)**: ~42%
**Advantage (3d6, take 2 highest)**: ~59% (+17% improvement)
**Disadvantage (3d6, take 2 lowest)**: ~26% (-16% penalty)

### Chance of EXECUTION (Double , value 10):

**Straight Roll**: ~2.8%
**Advantage**: ~5.1% (+2.3% improvement, nearly DOUBLE)
**Critical Advantage (4d6)**: ~8.5% (TRIPLE the base chance!)

**This creates dramatic "god roll" moments when perfectly positioned.**

---

## Quick Reference Table

| Situation | Dice Roll | Effect |
|-----------|-----------|--------|
| **Standard** | 2d6, add both | Baseline |
| **Advantage** | 3d6, discard lowest | +17% hit chance, +2.3% crit |
| **Critical Advantage** | 4d6, discard 2 lowest | +8.5% EXECUTION chance |
| **Disadvantage** | 3d6, discard highest | -16% hit chance, harder crits |
| **Critical Disadvantage** | 4d6, discard 2 highest | Very likely to miss/jam |

---

## Integration with Existing To-Hit System

### OLD SYSTEM (Static Modifiers):

```
Base 5+ to hit
Long range: +2 to target number (need 7+)
Heavy cover: +2 to target number (need 9+)
Total: Need 9+ on 2d6 (only 27% chance)
```

### NEW SYSTEM (Dice Pool):

```
Base 5+ to hit
Long range: Disadvantage (3d6, take lowest 2)
Heavy cover: Disadvantage (3d6, take lowest 2)
Total: 2 Disadvantages = Critical Disadvantage (4d6, take 2 lowest)
Chance to hit 5+: ~15% (worse than old system, but more dramatic)
```

**Balancing Note**: The new system is slightly harsher at extremes but more rewarding for perfect setups. Consider adjusting base to-hit from 5+ to 4+ if you want to maintain old success rates.

---

## Advantage/Disadvantage Source List

### ADVANTAGE Sources (Roll 3, Take Highest 2)

**Positioning**:
- Flanking attack (hex-sides 3, 5)
- Rear attack (hex-side 4)
- Higher ground (1+ elevation above target)
- Aiming (spent last turn stationary, aiming at this target)

**Target Status**:
- Target Stunned (cannot move or use Reactive cards)
- Target Immobilized (Chains of Penance, etc.)
- Target has 5+ Momentum Tokens
- Target's Primary Weapon destroyed (easier to hit, less defensive)

**Card Effects**:
- "Targeting Sigil" card: Grants Advantage on next attack
- "Sensor Sweep" card: Reveals enemy hand, grants Advantage
- "Zealot's Fury" (Church Tactic): Grants Advantage to all allies this turn

---

### DISADVANTAGE Sources (Roll 3, Take Lowest 2)

**Range**:
- Long range (7-10 hexes)
- Extreme range (11+ hexes)
- Beyond weapon's maximum range (auto-miss, but listed for clarity)

**Cover**:
- Heavy cover (fortress walls, dense forest, barricades)
- Obscured target (smoke, darkness, fog)
- Target behind other Caskets (if GM rules this grants cover)

**Attacker Status**:
- Moved 6+ hexes this turn (sprinting penalty)
- 5+ Heat (Danger Zone, weapon overheating)
- Primary Weapon destroyed (makeshift attacks)
- Head destroyed (sensor damage, -1 to all ranged attacks)

**Target Status**:
- Target moved 6+ hexes last turn (evasive maneuvers)
- Target using "Evasion Protocol" card (temporary Disadvantage to attackers)

**Environmental**:
- Shooting uphill (target 2+ levels higher)
- Wind/Storm effects (scenario-specific)

---

## Replacing Old Modifiers with Dice Pool

### Conversion Chart:

| Old Modifier | New Dice Pool |
|--------------|---------------|
| +0 (standard) | 2d6, add both |
| +1 (easier to hit) | Advantage (3d6, take 2 highest) |
| +2 (much easier) | Critical Advantage (4d6, take 2 highest) |
| -1 (harder to hit) | Disadvantage (3d6, take 2 lowest) |
| -2 (much harder) | Critical Disadvantage (4d6, take 2 lowest) |

**Example Conversions**:

**Flanking (old: -1 to target number) → Advantage**
**Heavy cover (old: +2 to target number) → Disadvantage**
**Rear + Higher ground (old: -3 to target number) → Critical Advantage**

---

## Playtesting Notes

### If Attacks Feel Too Easy:
- Increase base to-hit from 5+ to 6+
- Reduce Critical Advantage sources (require 3+ advantages instead of 2+)
- Add more Disadvantage sources (light cover now grants Disadvantage)

### If Attacks Feel Too Hard:
- Decrease base to-hit from 5+ to 4+
- Allow "Aiming" as a free action (don't consume full turn)
- Reduce Disadvantage impact (3d6 take highest 1 and lowest 1, add together)

### If EXECUTIONS Happen Too Often:
- Change EXECUTION to require triple (not double)
- Or: EXECUTION requires 10+ AND all dice show or 

### If Dice Pool Feels Too Swingy:
- Revert to static modifiers for competitive play
- Use Dice Pool system for narrative/campaign play only

---

## Example Combat with Dice Pool

### Setup:
- **Attacker**: Church Confessor, 6 cards in hand
- **Defender**: Dwarven Ironclad, in heavy cover (fortress wall)
- **Range**: 5 hexes (medium range)
- **Attacker Facing**: Flanking position (hex-side 3)

### Old System Calculation:
```
Base: 5+
Flanking: -1 (easier, need 4+)
Heavy cover: +2 (harder, need 6+)
Net: Need 6+ to hit
Roll 2d6: (3) + (4) = 7 total
Result: Hit!
```

### New System Calculation:
```
Base: 5+
Flanking: Advantage (3d6, take 2 highest)
Heavy cover: Disadvantage (3d6, take 2 lowest)
Net: 1 Advantage - 1 Disadvantage = Cancel out (straight roll, 2d6)

Roll 2d6: (3) + (4) = 7 total
Result: Hit!
```

**In this case, the systems produce same result. But:**
- If Attacker had higher ground (2 Advantages - 1 Disadvantage = Advantage), they'd roll 3d6 take 2 highest
- Increases chance of Strong Hit/Crit dramatically

---

## Designer's Notes

### Why Dice Pool Over Static Modifiers?

1. **Feels Better**: Rolling more dice is viscerally fun
2. **More Dramatic**: Higher variance at extremes (perfect positioning = god rolls)
3. **Intuitive**: "I have advantage" is easier to understand than "need 7+ instead of 5+"
4. **Compatible**: Works with existing Attack Dice symbols ( etc.)
5. **Rewards Skill**: Perfect setups (Critical Advantage) = triple EXECUTION chance

### Trench Crusade Inspiration

Trench Crusade uses this system with standard d6s:
- Base: 2d6, need 7+
- +1: 3d6, take 2 highest
- -1: 3d6, take 2 lowest

We've adapted it to work with Penance's custom Attack Dice (with symbols) and added Critical Advantage/Disadvantage for more extreme situations.

---

## FAQ

**Q: Can I have more than 2 Advantages or Disadvantages?**
A: No. Maximum is Critical Advantage (2+) or Critical Disadvantage (2+). Additional modifiers beyond that are wasted.

**Q: Do I need to track sources? Or just count net Advantages?**
A: Just count net. 3 Advantages - 1 Disadvantage = net 2 Advantages = Critical Advantage.

**Q: What if I have 5 Advantages and 4 Disadvantages?**
A: Net = 1 Advantage. Roll 3d6, take 2 highest.

**Q: Does this work with Defense Dice?**
A: No. Defense Dice use a different system (1d6 per damage, count symbols). This only applies to Attack Dice.

**Q: Can cards grant Advantage?**
A: Yes! Example: "Targeting Sigil" card: "Next attack gains Advantage."

**Q: Does this replace facing modifiers (weapon-side +1 damage)?**
A: No. Facing modifiers for DAMAGE remain the same. This only affects TO-HIT rolls.

**Q: If I have Advantage, do I still apply range penalties?**
A: No! Advantage/Disadvantage REPLACES all other to-hit modifiers. Just count net Advantage/Disadvantage, roll appropriate dice pool, compare to base target number (5+).

---

**END OF DOCUMENT**

---

*"Three dice. Two kept. One discarded. The difference between glory and a shallow grave."*
