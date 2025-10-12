# Dice Reference (Custom Dice System)
## Penance: Absolution Through Steel

**Version**: 1.0 (Dice System Implementation)
**Last Updated**: October 11, 2025

---

## Overview

Penance uses **3 types of custom d6 dice** to add brutal randomness to combat:

1. **Attack Dice** (2d6) - Roll to-hit, determines if attack lands
2. **Defense Dice** (Xd6) - Roll per damage point, chance to block/mitigate
3. **Suffering Dice** (1d6) - Church faction & event self-harm mechanics

**Design Philosophy**:
- GKR-style to-hit rolls (2d6 target numbers)
- BattleTech modifier stacking (range, movement, terrain)
- Kingdom Death save dice (block damage, critical effects)

---

## 1. Attack Dice (2d6)

### Die Face Symbols

| Face | Symbol | Value | Name |
|------|--------|-------|------|
| 1 | 🛡️ | 1 | GLANCE |
| 2 | 🩸 | 2 | BLOOD |
| 3 | ⚔️ | 3 | STRIKE |
| 4 | ⚔️⚔️ | 4 | DOUBLE STRIKE |
| 5 | 💀 | 5 | DEATH BLOW |
| 6 | ⚙️ | 0 | JAM (critical fail face) |

**Note**: Face 6 (⚙️ JAM) = 0 value for tactical unpredictability

---

### How to Roll Attack Dice

1. **Calculate To-Hit Target Number** (see Section 3 below)
2. **Roll 2 Attack Dice**
3. **Add both values together**
4. **Compare total to target number**

---

### Hit Result Table

| Total | Result | Effect |
|-------|--------|--------|
| **2** (double ⚙️) | **CATASTROPHIC FAILURE** | Weapon jams: discard all Primary Weapon cards from hand, +2 Heat, next attack -2 damage |
| **3-4** | **Miss** (if target 5+) | No damage, attack wasted |
| **5-6** | **Hit** | Standard damage from attack card |
| **7-8** | **Strong Hit** | Standard damage **+1** |
| **9** | **Critical Hit** | Standard damage **+2**, bypass 1 Defense |
| **10** (double 💀) | **EXECUTION** | Auto-destroy 1 Component, bypass ALL Defense |

**Example Rolls**:
- ⚔️ (3) + 💀 (5) = **8 total** → Strong Hit (+1 damage)
- 💀 (5) + 💀 (5) = **10 total** → **EXECUTION** (instant component destruction)
- ⚙️ (0) + ⚙️ (0) = **2 total** → **CATASTROPHIC FAILURE** (weapon jams)

---

### Special Roll Outcomes

**EXECUTION (Double 💀, total 10)**:
- Automatically destroy 1 targeted component (even if <3 Component Damage)
- Bypass ALL Defense (shields, armor, reactive cards don't work)
- Still deal standard damage from attack card
- Defender cannot choose to discard from hand (must discard from deck)
- **Brutality**: Even a 1-damage attack with EXECUTION destroys a component

**CATASTROPHIC FAILURE (Double ⚙️, total 2)**:
- Your weapon critically malfunctions
- Discard all Primary Weapon cards from hand immediately
- Gain +2 Heat (weapon overheats from malfunction)
- Next attack this turn or next turn: -2 damage
- **Does NOT end your turn** (can still move, use Universal cards)

**Example**:
- Church Confessor attacks with Faithful Thrust (4 damage)
- Rolls: ⚙️ (0) + ⚙️ (0) = **2 total** (Catastrophic Failure)
- Must discard all Penitent Blade cards from hand
- Gains 2 Heat
- Next attack -2 damage
- **Can still move, use Buckler Shield, or pass turn**

---

## 2. Defense Dice (Variable, 1d6 per damage)

### Die Face Symbols

| Face | Symbol | Effect |
|------|--------|--------|
| 1 | 🛡️ | **SHIELD** - Block 1 damage |
| 2 | ⚙️ | **ABSORB** - Block 1 damage |
| 3 | 🩸 | **FLESH WOUND** - Take damage (discard 1 card) |
| 4 | 💀 | **CRITICAL** - Take damage + 1 Component Damage |
| 5 | ⚔️ | **PIERCE** - Take damage, cannot use reactive cards |
| 6 | 🔥 | **HEAT** - Take damage + 1 Heat |

---

### How to Roll Defense Dice

1. **Attacker's attack hits** → Determine damage amount
2. **Defender rolls 1 Defense Die per damage point**
   - Example: 6 damage = roll 6 Defense Dice
3. **Count 🛡️ SHIELD and ⚙️ ABSORB symbols**
   - Each blocks 1 damage
4. **Apply special effects** from other symbols
5. **Final damage = Original damage - Total blocks**

**Block Probability**: 2/6 faces block (🛡️, ⚙️) = **33% chance per die**

---

### Defense Die Effects

**🛡️ SHIELD (Face 1)**:
- Blocks 1 damage
- No side effects
- Most reliable defense

**⚙️ ABSORB (Face 2)**:
- Blocks 1 damage
- Represents armor plating absorbing hit
- No side effects

**🩸 FLESH WOUND (Face 3)**:
- Take 1 damage (no block)
- Standard hit, no special effects

**💀 CRITICAL (Face 4)**:
- Take 1 damage (no block)
- **+1 Component Damage to targeted component**
- Stacks with Component Damage from discarding Primary Weapon cards
- **Example**: Roll 3 Defense Dice, get 💀💀💀 = +3 Component Damage (instant destruction)

**⚔️ PIERCE (Face 5)**:
- Take 1 damage (no block)
- **Cannot use reactive defense cards** (shield blocks, parries, etc.)
- Represents armor-piercing hit
- Disable reactive cards for THIS damage instance only

**🔥 HEAT (Face 6)**:
- Take 1 damage (no block)
- **+1 Heat**
- Can trigger Strain roll if pushed into Danger Zone (5+ Heat)

---

### Defense Dice Example

**Setup**: Dwarven Heavy takes **8 damage** from Church attack

**Step 1**: Roll 8 Defense Dice
- Result: 🛡️ 🛡️ 🛡️ 🩸 💀 💀 🔥 ⚔️

**Step 2**: Count Blocks
- **3 Shield symbols (🛡️🛡️🛡️)** = Block 3 damage
- Reduced from 8 → **5 damage**

**Step 3**: Apply Special Effects
- **2 Critical symbols (💀💀)** = +2 Component Damage to targeted component
- **1 Heat symbol (🔥)** = +1 Heat
- **1 Pierce symbol (⚔️)** = Cannot use reactive defense cards

**Step 4**: Defender Chooses Discard
- Must discard 5 cards (chooses 3 from hand, 2 from deck)
- If any Primary Weapon cards discarded → Add to Component Damage

**Step 5**: Final Component Damage
- 2 (from 💀💀) + 1 (from 1 Primary Weapon card discarded) = **3 Component Damage**
- **Component DESTROYED** (reached threshold)

---

### Statistical Breakdown

**Defense Die Probabilities**:
- Block (🛡️ or ⚙️): 2/6 = **33.3%**
- Standard damage (🩸): 1/6 = **16.7%**
- Critical damage (💀): 1/6 = **16.7%**
- Pierce (⚔️): 1/6 = **16.7%**
- Heat (🔥): 1/6 = **16.7%**

**Expected Blocks per Damage**:
- 3 damage = ~1 block (33%)
- 6 damage = ~2 blocks (33%)
- 9 damage = ~3 blocks (33%)

**Variance**:
- Lucky roll: 6 damage, roll 6 blocks (all 🛡️/⚙️) = **0 damage taken**
- Unlucky roll: 6 damage, roll 0 blocks (all 🩸💀⚔️🔥) = **6 damage + penalties**

---

## 3. To-Hit Modifier System

### Base To-Hit Number

**Default**: **5+** (roll 2d6 Attack Dice, total must equal or exceed 5)

---

### Range Modifiers

| Range | Modifier | Final Target |
|-------|----------|--------------|
| **Short (0-3 hexes)** | +0 | 5+ |
| **Medium (4-6 hexes)** | +1 | 6+ |
| **Long (7-10 hexes)** | +2 | 7+ |
| **Extreme (11+ hexes)** | +3 | 8+ |

---

### Movement Modifiers (Attacker)

| Hexes Moved This Turn | Modifier |
|-----------------------|----------|
| **0 (Stationary)** | +0 |
| **1-3** | +1 |
| **4-6** | +2 |
| **7+ (Sprint)** | +3 |

**Note**: Applies to attacker's movement during their current turn

---

### Movement Modifiers (Defender)

| Hexes Moved Last Turn | Modifier |
|-----------------------|----------|
| **0 (Stationary)** | +0 |
| **1-3** | +1 |
| **4-6** | +2 |
| **7+ (Sprint)** | +3 |

**Note**: Applies to defender's movement during their previous turn

---

### Hex-Side Facing Modifiers

| Hex Side | Arc Name | Modifier | Notes |
|----------|----------|----------|-------|
| **1** (Front) | Front Arc | +0 | Standard defense |
| **2** (Front-Right) | Weapon Side | +0 | +1 damage if hit (vulnerable) |
| **3** (Rear-Right) | Flank (Weapon) | -1 (easier) | Exposed flank |
| **4** (Rear) | Rear Arc | -2 (easier) | Blind spot, +3 damage if hit |
| **5** (Rear-Left) | Flank (Shield) | -1 (easier) | Rear flank |
| **6** (Front-Left) | Shield Side | +1 (harder) | Shield protection, +1 Defense if hit |

**Facing Diagram**:
```
         [1]          1 = FRONT (hardest to hit)
      [6] [X] [2]     2 = WEAPON SIDE (vulnerable, +1 damage)
      [5]   [3]       3-5 = FLANKS (easier to hit)
         [4]          4 = REAR (easiest, +3 damage)
                      6 = SHIELD SIDE (harder, +1 Defense)
X = Your Casket
```

---

### Terrain Modifiers

| Terrain | Modifier | Effect |
|---------|----------|--------|
| **Open Ground** | +0 | No cover |
| **Light Cover** (rubble, low walls) | +1 | Partial concealment |
| **Heavy Cover** (fortress walls, forest) | +2 | Significant obstruction |
| **Obscured** (smoke, darkness) | +2 | Limited visibility |
| **Elevated** (attacker on high ground) | -1 (easier) | Height advantage |

**Stacking**: Multiple terrain modifiers can apply
- Example: Target in forest (+2) AND obscured by smoke (+2) = **+4 total**

---

### Complete To-Hit Calculation Example

**Scenario**:
- Church Scout (attacker) shoots Dwarven Heavy (defender) with pistol
- Range: 5 hexes (Medium)
- Scout moved 4 hexes this turn (aggressive advance)
- Dwarf moved 2 hexes last turn (repositioning)
- Attacking Dwarf's **shield-side (hex 6)**
- Dwarf is behind light cover (rubble)

**Calculation**:
1. Base: 5+
2. Range (Medium, 5 hexes): +1 → **6+**
3. Attacker moved 4 hexes: +1 → **7+**
4. Defender moved 2 hexes: +1 → **8+**
5. Shield-side facing: +1 → **9+**
6. Light cover: +1 → **10+**

**Final To-Hit**: **10+** (only possible with double 💀 EXECUTION roll)

**Attack Roll**: 💀 (5) + ⚔️ (3) = **8 total**
**Result**: **MISS** (needed 10+, got 8)

---

### Modifier Quick Reference Table

| Situation | Modifier |
|-----------|----------|
| Short range (0-3) | +0 |
| Medium range (4-6) | +1 |
| Long range (7-10) | +2 |
| Extreme range (11+) | +3 |
| Attacker stationary | +0 |
| Attacker moved 1-3 | +1 |
| Attacker moved 4-6 | +2 |
| Attacker sprinted 7+ | +3 |
| Defender stationary | +0 |
| Defender moved 1-3 | +1 |
| Defender moved 4-6 | +2 |
| Defender sprinted 7+ | +3 |
| Front arc (hex 1) | +0 |
| Weapon-side (hex 2) | +0 |
| Flanks (hex 3, 5) | -1 |
| Rear (hex 4) | -2 |
| Shield-side (hex 6) | +1 |
| Light cover | +1 |
| Heavy cover | +2 |
| Obscured | +2 |
| Elevated (attacker) | -1 |

**Total Modifier Range**: -3 (rear arc + elevated) to +13 (extreme range + sprint + defender sprint + shield-side + heavy cover)

---

## 4. Suffering Dice (1d6, Church & Events)

**Used for**: Church of Absolution self-harm mechanics and campaign events

### Die Face Symbols

| Face | Symbol | Effect |
|------|--------|--------|
| 1 | 🛡️ | **DIVINE MERCY** - No self-harm |
| 2 | 🩸 | **BLOOD PRICE** - Discard 2 cards (self-harm) |
| 3 | ⚔️ | **ZEALOT'S FURY** - Discard 1 card, +1 damage to all attacks this turn |
| 4 | 🔥 | **PENANCE** - Discard 1 card, +1 Heat, +2 damage next attack |
| 5 | 💀 | **MARTYRDOM** - Discard 3 cards, +3 damage to next attack |
| 6 | ⚙️ | **ABSOLUTION** - Discard 1 card, recover 1 card from discard |

---

### When to Roll Suffering Dice

**Church Faction Cards**:
- **BLOOD OFFERING**: Roll 1 Suffering Die instead of auto-discarding 2 cards
- **Flagellant's Zeal**: Roll 2 Suffering Dice, apply both effects
- **Martyrdom Protocol**: When redirecting damage, roll 1 Suffering Die per 3 damage redirected

**Campaign Events**:
- **Penance Rituals** (settlement event)
- **Taint Purging** (when Taint reaches 8+)
- **Soul Bargains** (desperate deals with Bonelord Thresh)
- **Leg-Skimming** (voluntary soul sacrifice)

---

### Suffering Die Effects

**🛡️ DIVINE MERCY (Face 1)**:
- No self-harm
- **Rare blessing** (16.7% chance)
- Church pilot prays: "The Resonance spares me this time."

**🩸 BLOOD PRICE (Face 2)**:
- Discard 2 cards (self-harm)
- Standard Church sacrifice
- Expected outcome for BLOOD OFFERING

**⚔️ ZEALOT'S FURY (Face 3)**:
- Discard 1 card
- +1 damage to ALL attacks this turn
- **Tactical choice**: Less self-harm, sustained damage boost

**🔥 PENANCE (Face 4)**:
- Discard 1 card
- +1 Heat
- +2 damage to **next attack only**
- Risk/reward: Heat buildup for burst damage

**💀 MARTYRDOM (Face 5)**:
- Discard 3 cards (brutal self-harm)
- +3 damage to **next attack only**
- **High risk, high reward**: Sacrifice for lethal strike

**⚙️ ABSOLUTION (Face 6)**:
- Discard 1 card
- Recover 1 card from discard pile
- **Net cost**: 0 cards (discard 1, recover 1)
- Allows card cycling (discard weak card, recover strong card)

---

### Suffering Dice Strategy

**BLOOD OFFERING Card** (Church Faction):
- **Old mechanic**: Auto-discard 2 cards
- **New mechanic**: Roll 1 Suffering Die
- **Expected value**: ~2 cards discarded (same as before)
- **Variance**:
  - Best case: 🛡️ DIVINE MERCY (0 cards)
  - Worst case: 💀 MARTYRDOM (3 cards)

**Risk/Reward Analysis**:
- 1/6 chance (16.7%) to avoid all self-harm (🛡️)
- 1/6 chance (16.7%) to get +3 damage burst (💀)
- 2/6 chance (33.3%) to get sustained +1 damage (⚔️ or 🔥)
- **Trade consistency for unpredictability**

**Multiple Suffering Dice** (Flagellant's Zeal):
- Roll 2 Suffering Dice, apply both
- **Example**: 🩸 + 💀 = Discard 5 cards total, +3 damage next attack
- **Example**: 🛡️ + ⚙️ = Discard 1, recover 1 (net 0 cards, no bonus)
- **Example**: ⚔️ + 🔥 = Discard 2, +1 Heat, +1 damage all attacks + +2 damage next

---

## 5. Dice Probability Tables

### Attack Dice (2d6) Probability

| Total | Probability | Cumulative | Result |
|-------|-------------|------------|--------|
| 2 (⚙️⚙️) | 2.78% | 2.78% | Catastrophic Failure |
| 3 | 5.56% | 8.33% | Likely miss |
| 4 | 8.33% | 16.67% | Likely miss |
| 5 | 11.11% | 27.78% | Hit (if target 5+) |
| 6 | 13.89% | 41.67% | Hit |
| 7 | 16.67% | 58.33% | Strong Hit |
| 8 | 13.89% | 72.22% | Strong Hit |
| 9 | 11.11% | 83.33% | Critical Hit |
| 10 (💀💀) | 2.78% | 86.11% | EXECUTION |

**Note**: Totals above 10 impossible (max die value = 5)

**Hit Chances by Target Number**:
- **5+**: 72.22% (accounting for JAM face)
- **6+**: 58.33%
- **7+**: 41.67%
- **8+**: 27.78%
- **9+**: 13.89%
- **10+**: 2.78% (EXECUTION only)

---

### Defense Dice Block Probability

**Single Die**:
- Block: 33.3% (🛡️ or ⚙️)
- Standard damage: 16.7% (🩸)
- Critical: 16.7% (💀)
- Pierce: 16.7% (⚔️)
- Heat: 16.7% (🔥)

**Expected Blocks**:
| Damage | Expected Blocks | Expected Damage |
|--------|-----------------|-----------------|
| 3 | 1 | 2 |
| 6 | 2 | 4 |
| 9 | 3 | 6 |
| 12 | 4 | 8 |

**Variance Examples**:
- **6 damage, 0 blocks** (all 🩸💀⚔️🔥): 11.6% chance
- **6 damage, 6 blocks** (all 🛡️⚙️): 0.14% chance (very rare)
- **6 damage, 2 blocks** (expected): ~29% chance

---

### Suffering Dice Probability

| Face | Symbol | Effect | Probability |
|------|--------|--------|-------------|
| 1 | 🛡️ | Divine Mercy (0 cards) | 16.7% |
| 2 | 🩸 | Blood Price (2 cards) | 16.7% |
| 3 | ⚔️ | Zealot's Fury (1 card, +1 dmg) | 16.7% |
| 4 | 🔥 | Penance (1 card, +1 Heat, +2 dmg) | 16.7% |
| 5 | 💀 | Martyrdom (3 cards, +3 dmg) | 16.7% |
| 6 | ⚙️ | Absolution (1 card, recover 1) | 16.7% |

**Expected Cards Discarded** (single die):
- (0×1 + 2×1 + 1×1 + 1×1 + 3×1 + 0×1) / 6 = **1.17 cards average**

**Comparison to Fixed Cost**:
- Old BLOOD OFFERING: Always 2 cards
- New BLOOD OFFERING: ~1.17 cards average (but high variance)

---

## 6. Dice Manufacturing Specifications

### Attack Dice (2d6)

**Material**: 16mm standard d6, custom engraved
**Colors**: Black dice, silver/white symbols

**Face Layout**:
1. 🛡️ GLANCE (value 1) - Shield symbol
2. 🩸 BLOOD (value 2) - Blood droplet
3. ⚔️ STRIKE (value 3) - Single crossed swords
4. ⚔️⚔️ DOUBLE STRIKE (value 4) - Double crossed swords
5. 💀 DEATH BLOW (value 5) - Skull
6. ⚙️ JAM (value 0) - Broken gear

**Value markings**: Small number in corner (1-5, 0 for JAM)

---

### Defense Dice (Variable)

**Material**: 16mm standard d6, custom engraved
**Colors**: Red dice, white symbols

**Face Layout**:
1. 🛡️ SHIELD - Shield icon
2. ⚙️ ABSORB - Gear/armor icon
3. 🩸 FLESH WOUND - Blood droplet
4. 💀 CRITICAL - Skull
5. ⚔️ PIERCE - Piercing arrow
6. 🔥 HEAT - Flame

**No value markings** (effect-based, not numeric)

---

### Suffering Dice (1d6)

**Material**: 16mm standard d6, custom engraved
**Colors**: Crimson/dark red dice, gold symbols

**Face Layout**:
1. 🛡️ DIVINE MERCY - Holy shield
2. 🩸 BLOOD PRICE - Blood droplets
3. ⚔️ ZEALOT'S FURY - Flaming sword
4. 🔥 PENANCE - Sacred flame
5. 💀 MARTYRDOM - Crowned skull
6. ⚙️ ABSOLUTION - Halo/holy gear

**Aesthetic**: Church of Absolution theme (religious martyrdom)

---

## 7. Quick Reference: What Dice to Roll When

### During Attack

1. **Declare attack** → Calculate To-Hit target number
2. **Roll 2 Attack Dice** → Add values, compare to target
3. **If hit** → Defender rolls Defense Dice (1 per damage)
4. **Apply damage** → Defender discards cards

### During Defense

1. **Attack hits** → Determine damage amount
2. **Roll X Defense Dice** (X = damage)
3. **Count blocks** (🛡️ and ⚙️)
4. **Apply special effects** (💀 💀⚔️🔥)
5. **Discard final damage** (original - blocks)

### Church Self-Harm

1. **Play BLOOD OFFERING** card
2. **Roll 1 Suffering Die**
3. **Apply effect** (discard cards, gain damage bonus)
4. **Make next attack** (with bonus if applicable)

---

**END OF DOCUMENT**

---

*"The dice are the will of the Resonance. You cannot control fate—only face it."*

*"Every roll is a prayer. Every result, divine judgment."*
