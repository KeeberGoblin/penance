# PENANCE: QUICK REFERENCE
## Absolution Through Steel

---

## TURN STRUCTURE

### Player Turn (4 Phases)

**1. REFRESH**
- Restore SP to maximum
- If Heat 5+: Roll Strain (1d6 + Heat)

**2. ACTION PHASE**
- Play cards (costs SP)
- Move (1 SP per hex)
- Rotate facing (free, once per turn)
- Continue until out of SP or pass

**3. DRAW PHASE**
- Draw to hand size 6
- If deck empty: Reshuffle + add 1 Damage card

**4. END TURN**
- Resolve end-of-turn effects
- Next player goes

---

## SP MAXIMUM (by Casket Type)

| Casket Type | SP Max |
|-------------|--------|
| Light | 6 SP |
| Medium | 5 SP |
| Heavy | 4 SP |
| Assault | 3 SP |

Modified by destroyed Chassis (-1 SP) or Leg-Skimming (+1 SP)

---

## COMBAT RESOLUTION (WITH DICE)

### Attack Sequence
1. **Play attack card** (spend SP), declare target component
2. **Calculate To-Hit Number**:
 - Base: **5+** (roll 2d6 Attack Dice)
 - \+ Range (Short +0, Medium +1, Long +2, Extreme +3)
 - \+ Attacker movement (1-3 hexes +1, 4-6 +2, 7+ +3)
 - \+ Defender movement (1-3 hexes +1, 4-6 +2, 7+ +3)
 - \+ Hex-side (Front +0, Weapon +0, Flank -1, Rear -2, Shield +1)
 - \+ Cover (Light +1, Heavy +2)
 - \+ Elevation (Higher -1, Lower +1)
3. **Roll 2 Attack Dice**, add values:
 - **5-6** = Hit | **7-8** = Strong Hit (+1 dmg)
 - **9** = Critical (+2 dmg, bypass 1 Def) | **10** = EXECUTION (destroy component)
 - **<5** = Miss | **2** = Catastrophic Failure (weapon jams)
4. **If hit**, Defender plays reactive card (optional, 0 SP)
5. **Defender rolls Defense Dice** (1d6 per damage):
 - Count blocks: SHIELD, ABSORB (each blocks 1 dmg)
 - Apply effects: CRITICAL (+1 Component Dmg), HEAT (+1 Heat), PIERCE (no reactives)
6. **Defender discards** final damage (original - blocks) from hand/deck

### Component Damage
- Primary Weapon cards discarded → +1 Component Damage
- Defense Dice CRITICAL → +1 Component Damage
- **3 Component Damage = Component Destroyed**

---

## COMPONENT DESTRUCTION EFFECTS

| Component | Effect |
|-----------|--------|
| **Right Arm** | Lose all Primary Weapon cards from hand |
| **Left Arm** | Lose all Secondary Equipment cards |
| **Legs** | Movement costs +1 SP per hex |
| **Head** | -1 to ranged attacks, no Sensor Sweep |
| **Chassis** | -1 SP maximum (permanent) |

---

## RANGE & LINE OF SIGHT

### Range Bands
- **Melee**: Range 1 (adjacent only)
- **Close**: Range 2-3
- **Medium**: Range 4-6
- **Long**: Range 7+

### LOS Blocked By
- Walls
- Large terrain (buildings)
- Dense forests (marked)

### Cover (To-Hit Penalty)
- Light cover (forest, rubble): +1 to target number
- Heavy cover (fortress walls): +2 to target number
- Behind other Caskets: +1 to target number

---

## FACING MODIFIERS (6-HEX SYSTEM)

| Hex-Side | To-Hit Mod | Damage Bonus | Def Penalty | Shield Blocks? |
|----------|------------|--------------|-------------|----------------|
| **1 (Front)** | +0 | +0 | 0 | Yes |
| **2 (Weapon)** | +0 | +1 | -1 | No |
| **3 (Flank-R)** | -1 | +2 | -2 | No |
| **4 (Rear)** | -2 | +3 | -3 | No |
| **5 (Flank-L)** | -1 | +2 | -2 | No |
| **6 (Shield)** | +1 | +0 | +1 | Yes |

**Rotating**: Free action, once per turn. 1 SP per additional rotation.

---

## HEAT SYSTEM

### Heat Zones
| Heat | Zone | Effect |
|------|------|--------|
| 0-4 | Safe | None |
| 5-9 | Danger | Roll Strain at start of turn |
| 10+ | Critical | Auto-fail Strain |

### Strain Table (1d6 + Heat)
| Roll | Effect |
|------|--------|
| 1-5 | +1 Heat |
| 6-8 | -1 SP this turn |
| 9-11 | Take 2 damage |
| 12+ | Component malfunction |

### Removing Heat
- Emergency Vent card (2 SP): Remove 3 Heat
- Water hexes: Remove 2 Heat per turn
- Pass entire turn: Remove 1 Heat

---

## MOVEMENT

| Action | SP Cost |
|--------|---------|
| Move 1 hex (clear) | 1 SP |
| Move 1 hex (difficult) | 2 SP |
| Climb up 1 level | 2 SP |
| Climb down 1 level | 1 SP |
| Rotate facing | Free |

**Cannot move through**: Enemies, walls, obstacles

---

## PILOT WOUNDS

### When Pilot Takes Damage
- Capsule breach
- Neural feedback (5+ Component Damage total)
- Thread snap
- Taint overload (10 Taint)
- Casket destruction (roll save)

### Wound Types
- **Minor Injury** (5 cards): Temporary debuff
- **Severe Injury** (3 cards): PERMANENT effect
- **Trauma** (2 cards): Mental breakdown

**10 Wounds = Pilot Death**

---

## COMMON ACTIONS

| Action | SP Cost | Notes |
|--------|---------|-------|
| Play attack card | Varies | 1-5 SP typically |
| Play reactive defense | 0 SP | During enemy turn |
| Move 1 hex | 1 SP | +1 SP if difficult terrain |
| Vent Heat | 2 SP | Remove 3 Heat (card) |
| Rotate | Free | Once per turn |
| Draw extra card | Varies | Some cards grant this |

---

## DECK & HAND

### Starting Hand
- **6 cards**
- **Mulligan**: Once at start, shuffle hand & redraw 6

### Hand Size
- **Maximum 6** (discard down at end of turn)
- Draw to 6 every Draw Phase

### Deck Depletion
- Deck empty → **Reshuffle** discard pile
- **Add 1 Damage card** when reshuffling
- Damage cards do nothing (dead draws)

### Defeat
- Deck AND discard both empty → **Casket destroyed**

---

## REACTIVE CARDS

### Timing
- Played during **opponent's turn**
- Must have **[—] Initiative** keyword
- Cost **0 SP** (doesn't use your pool)

### Limits
- **1 reactive per attack**
- Must be in hand
- Played BEFORE damage is calculated

### Examples
- Brace for Impact: Reduce damage by 2
- Deflect: Reduce damage by 1
- Unyielding Bulwark: Reduce damage by 3, gain 1 Heat

---

## VICTORY CONDITIONS

### Arena
- Reduce enemy Casket to 0 HP (deck empty)
- Kill enemy pilot (10 Wounds)
- Scenario-specific objectives

### Campaign
- Complete primary objective
- At least 1 pilot survives

---

## KEYWORDS

| Keyword | Meaning |
|---------|---------|
| **Melee** | Range 1 only |
| **Reactive** | Play during enemy turn |
| **[—] Initiative** | Reactive card |
| **Aura X** | Affects X-hex radius |
| **Ignore Armor** | Bypass Defense entirely |
| **Self-Harm** | Discard from your deck |
| **Component Target** | Choose which component to damage |

---

## TERRAIN TYPES

| Terrain | Movement | LOS | Cover | Special |
|---------|----------|-----|-------|---------|
| Clear | 1 SP | Yes | No | — |
| Forest | 2 SP | Yes | +1 Def | — |
| Rubble | 2 SP | Yes | +1 Def | — |
| Wall | Impassable | BLOCKED | N/A | — |
| Water | 1 SP | Yes | No | Remove 2 Heat/turn |
| Elevated | 2 SP (up) | Yes | No | +1 dmg if higher |

---

## CASKET DECK COMPOSITION (30 cards)

- **10 Universal Core** (mandatory, everyone has)
- **12 Primary Weapon** (faction-specific, cannot change)
- **6 Secondary Equipment** (player choice)
- **2 Faction Tactics** (choose 2 from 5 available)

---

## DICE QUICK REFERENCE

### Attack Dice (2d6)
| Symbol | Value | Name |
|--------|-------|------|
| | 1 | GLANCE |
| | 2 | BLOOD |
| | 3 | STRIKE |
| | 4 | DOUBLE STRIKE |
| | 5 | DEATH BLOW |
| | 0 | JAM |

**Results**: 5-6 Hit | 7-8 Strong Hit (+1) | 9 Critical (+2) | 10 EXECUTION | 2 Catastrophic Failure

### Defense Dice (1d6 per damage)
| Symbol | Effect |
|--------|--------|
| | SHIELD - Block 1 dmg |
| | ABSORB - Block 1 dmg |
| | FLESH WOUND - Take dmg |
| | CRITICAL - Take dmg + 1 Component Dmg |
| | PIERCE - Take dmg, no reactives |
| | HEAT - Take dmg + 1 Heat |

### Suffering Dice (Church/Events, 1d6)
| Symbol | Effect |
|--------|--------|
| | DIVINE MERCY - No harm |
| | BLOOD PRICE - Discard 2 |
| | ZEALOT'S FURY - Discard 1, +1 dmg all attacks |
| | PENANCE - Discard 1, +1 Heat, +2 dmg next |
| | MARTYRDOM - Discard 3, +3 dmg next |
| | ABSOLUTION - Discard 1, recover 1 |

---

## COMMON MISTAKES

❌ **Don't**: Draw cards during Action Phase (only Draw Phase)
❌ **Don't**: Discard from hand when damaged (discard from DECK)
❌ **Don't**: Stack cover bonuses (max +1 Defense from cover)
❌ **Don't**: Attack targets outside your front 180° arc
❌ **Don't**: Forget to roll Strain at 5+ Heat

✅ **Do**: Rotate before attacking rear targets (free action)
✅ **Do**: Use reactive cards to mitigate damage
✅ **Do**: Track Component Damage separately per component
✅ **Do**: Add Damage card when reshuffling deck

---

## SAMPLE TURN (WITH DICE)

**Church Confessor (6 SP, 2 Heat, 24 HP)**

1. **REFRESH**: 6 SP, Heat check = Safe Zone (skip)
2. **ACTION**:
 - Rotate (free) → Face enemy
 - Move 2 hexes (2 SP)
 - Play Blood Offering (0 SP) → Discard 2 cards, buff active (+3 dmg)
 - Play Faithful Thrust (2 SP) → Attack for 4 dmg + 3 buff = 7 dmg
 - **To-Hit**: Base 5+ | Moved 2 hexes +1 = Need 6+
 - **Roll**: (3) + (5) = 8 → Strong Hit (+1 dmg) = 8 total dmg
 - **Enemy rolls 8 Defense Dice**: = 2 blocks, 1 Critical, 1 Heat
 - Final: 6 damage + 1 Component Damage to enemy
 - Pass (2 SP unused)
3. **DRAW**: Draw 2 cards (hand back to 6)
4. **END**: Next player's turn

**Result**: 22 HP remaining, enemy took 6 dmg + 1 Component Dmg + 1 Heat

---

---

## VERSION 3.0 OPTIONAL RULES

**These are OPTIONAL enhancements. Base v2.0 rules work perfectly without them.**

### Dice Pool Advantage (Instead of Static Modifiers)

**ADVANTAGE** (flanking, higher ground, aiming):
- Roll **3d6 Attack Dice**
- **Discard lowest**, add 2 highest
- +17% hit chance, +2.3% crit chance

**CRITICAL ADVANTAGE** (2+ advantages):
- Roll **4d6 Attack Dice**
- **Discard 2 lowest**, add 2 highest
- Triple EXECUTION chance!

**DISADVANTAGE** (heavy cover, long range, high Heat):
- Roll **3d6 Attack Dice**
- **Discard highest**, add 2 lowest
- -16% hit chance, harder crits

**CRITICAL DISADVANTAGE** (2+ disadvantages):
- Roll **4d6 Attack Dice**
- **Discard 2 highest**, add 2 lowest
- Very likely to miss/jam

**Cancellation**: 1 Advantage + 1 Disadvantage = straight 2d6 roll

---

### Taint Exploitation (Tactical Resource)

**GAINING TAINT**:
- 1 Taint per 3 damage taken
- Event cards (Taint Pulse, Void Embrace)
- Church self-harm cards

**SPEND ENEMY TAINT** (offensive):
- **[1 Taint]** Exposed Weakness → Advantage on attack
- **[2 Taint]** Force Reroll → Reroll up to 2 Defense blocks
- **[1 Taint]** Heat Spike → Target gains +1 Heat
- **[3 Taint]** Component Vulnerability → +1 Component Dmg
- **[4 Taint]** Neural Disruption → No Reactive cards
- **[5 Taint]** Taint Overload → Flip 1 Pilot Wound

**SPEND YOUR TAINT** (defensive/desperate):
- **[2 Taint]** Tainted Fury → +2 damage, gain 1 Heat
- **[3 Taint]** Ignore Pain → Reduce damage by 3, gain 1 Heat
- **[1 Taint]** Void Step → Move 2 hexes (0 SP), gain 1 Heat
- **[4 Taint]** Thermal Purge → Remove all Heat, -1 SP max
- **[5 Taint]** Resurrection → Reshuffle when defeated (once), flip 2 Wounds

**CORRUPTION THRESHOLD**:
- 10+ Taint: Roll 1d6, need 4+ or become Corrupted
- Corrupted: Mind control, explosion, or mutation (1d6 table)

---

### Pilot Grit (Campaign Progression)

**GRIT STAT** (0-3, grows with experience):
- **Grit 0**: Untested (0-4 missions)
- **Grit 1**: Seasoned (5 missions OR 1 Severe Injury survived)
- **Grit 2**: Hardened (10 missions OR 3 Severe Injuries)
- **Grit 3**: Iron Will (20 missions OR 5 Severe Injuries)

**GRIT CHECK** (when Pilot takes damage):
- Roll **1d6 + Grit**
- Compare to table:

| Roll | Effect |
|------|--------|
| **1-3** | Full Wound (flip normally) |
| **4-5** | Tough It Out (Severe → Minor) |
| **6-7** | Shrug It Off (no flip, +1 Heat) |
| **8+** | Iron Will (no flip, no penalty) |

**FACTION MODIFIERS**:
- Church: +1 Starting Grit (zealot training)
- Dwarves: +1 Grit vs Severe only (stoic endurance)
- Ossuarium: Immune (already dead)
- Elves: -1 Grit always (fragile immortals)

**BONUSES**:
- Leg-Skimmed: +1 Grit permanent
- Trauma Wound: -1 Grit per Trauma

---

**PRINT THIS PAGE FOR TABLE REFERENCE**

---

*"Refresh. Fight. Draw. Endure. Adapt."*
