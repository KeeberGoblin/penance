# Range & Line of Sight Rules
## Penance: Absolution Through Steel

**Version**: 2.0 (Hex-Based Combat)
**Last Updated**: October 10, 2025

---

## Hex Grid Basics

**Penance uses a hex grid for movement and combat.**

### Hex Counting
- **Range 0**: The hex you're standing in
- **Range 1**: The 6 hexes directly adjacent to you
- **Range 2**: The 12 hexes one ring out
- **Range 3+**: Continue counting outward

**Do NOT count the hex you're standing in.**

---

## Range Diagram

```
        [ ][ ][ ][ ][ ]
       [ ][3][3][3][ ]
      [ ][3][2][2][3][ ]
     [ ][3][2][1][2][3][ ]
    [ ][3][2][1][X][1][2][3][ ]
     [ ][3][2][1][2][3][ ]
      [ ][3][2][2][3][ ]
       [ ][3][3][3][ ]
        [ ][ ][ ][ ][ ]

X = Your Casket
1 = Range 1 (adjacent, 6 hexes)
2 = Range 2 (12 hexes)
3 = Range 3 (18 hexes)
```

---

## Range Bands

**Cards specify range as:**

| Range | Distance | Notes |
|-------|----------|-------|
| **Melee** | Range 1 only | Must be adjacent (touching) |
| **Close** | Range 2-3 | Short-ranged weapons, pistols |
| **Medium** | Range 4-6 | Rifles, bows |
| **Long** | Range 7+ | Sniper weapons, artillery |
| **Self** | Range 0 | Affects only you |
| **Aura X** | X hexes radius | Affects all units within X hexes |

**Examples**:
- **Faithful Thrust**: "Range: Melee" (must be adjacent)
- **Quick Shot** (Pistol): "Range 3" (up to 3 hexes away)
- **Sniper Shot**: "Range 8" (long-distance)
- **Consecrated Ground**: "Aura 3" (affects 3-hex radius around you)

---

## Line of Sight (LOS)

**To attack or target an enemy, you must have Line of Sight.**

### LOS Basics

**You have LOS if:**
- You can draw a straight line from center of your hex to center of target hex
- That line does NOT pass through LOS-blocking terrain

**LOS is BLOCKED by:**
- **Walls** (solid obstacles)
- **Large terrain** (buildings, cliffs)
- **Dense forests** (specifically marked as "blocks LOS")

**LOS is NOT blocked by:**
- **Other Caskets** (you can shoot past allies/enemies)
- **Rubble** (provides cover, doesn't block)
- **Light terrain** (water, ice, clear ground)

---

## LOS Diagram

```
BLOCKED LOS (Wall in the way):
    [ ][T][ ]
    [ ][#][ ]   # = Wall
    [ ][A][ ]   A = Attacker, T = Target

    LOS blocked! Cannot attack.
```

```
CLEAR LOS (Rubble provides cover, doesn't block):
    [ ][T][ ]
    [ ][~][ ]   ~ = Rubble
    [ ][A][ ]

    LOS clear! Can attack, but target has +1 Defense (cover).
```

```
CLEAR LOS (Can shoot past other Caskets):
    [ ][T][ ]
    [ ][E][ ]   E = Enemy Casket
    [ ][A][ ]

    LOS clear! Other Caskets don't block.
```

---

## Cover System

**Cover provides defensive bonuses without blocking LOS.**

### Cover Rules

**If target is:**
- In or adjacent to cover terrain (forests, rubble)
- AND attacker's LOS passes through/near that terrain
- **Target gains +1 Defense** against that attack

**Cover Terrain Types**:
- **Forest hexes**: +1 Defense when standing in them
- **Rubble hexes**: +1 Defense when standing in them
- **Other Caskets**: +1 Defense if enemy Casket is between you and attacker

**Cover does NOT stack**:
- Maximum +1 Defense from cover (even if multiple cover sources)

---

## Cover Diagram

```
COVER EXAMPLE:
    [A][ ][ ]
    [ ][~][T]   ~ = Rubble, T = Target

    Target is IN rubble hex.
    Attacker's LOS passes through rubble.
    Target gets +1 Defense.
```

```
NO COVER (Behind rubble, but not in it):
    [A][ ][ ]
    [ ][~][ ]
    [ ][ ][T]

    Target is NOT in rubble hex.
    No cover bonus.
```

---

## Facing & Firing Arcs

**Caskets have a facing (which direction they're pointed).**

### Hex Facing

**Each Casket occupies 1 hex and faces ONE of the 6 hex edges.**

```
Hex Facings (6 possible directions):
       [N]
    [NW] [NE]
    [SW] [SE]
       [S]
```

---

### Firing Arc (Front 180°)

**You can only attack targets in your FRONT ARC (3 front-facing hexes).**

```
Front Arc Diagram (Facing North):
         [F][F][F]   F = Front arc (can attack)
        [S][X][S]    X = Your Casket
         [R][R][R]   R = Rear arc (cannot attack)
                     S = Side hexes (can attack)

If enemy is in F or S hexes, you can attack.
If enemy is in R hexes, you must ROTATE first.
```

**Rotating**:
- **Free action** (once per turn)
- Changes which hexes are in your front arc
- Does not cost SP

---

### Facing Modifiers (Attack Bonuses)

**Attacking from different facings grants bonuses:**

| Facing | Attacker Bonus | Defender Penalty |
|--------|----------------|------------------|
| **Front** (facing you) | +0 damage | Full Defense |
| **Side** (flank) | +1 damage | -1 Defense |
| **Rear** (behind) | +2 damage | -2 Defense |

**Example**:
- Attack deals 5 damage
- Attacking from REAR: 5 + 2 = **7 damage**
- Defender has 2 Defense, but Rear = -2 Defense → **0 Defense**
- Defender takes full 7 damage

**Facing matters!** Flanking is powerful.

---

## Facing Diagram

```
REAR ATTACK (Most vulnerable):
    [ ][A][ ]   A = Attacker
    [ ][T][ ]   T = Target (facing away)
    [ ][↑][ ]   ↑ = Target's facing direction

    Attacker is BEHIND target.
    +2 damage, target's Defense -2
```

```
SIDE ATTACK (Flank):
    [A][ ][ ]
    [ ][T→][ ]   T = Target (facing right)

    Attacker is to the SIDE.
    +1 damage, target's Defense -1
```

```
FRONT ATTACK (Expected):
    [ ][↓][ ]   Target facing attacker
    [ ][T][ ]
    [ ][A][ ]

    No bonuses. Full Defense applies.
```

---

## Elevation & Height

**Some hexes are elevated (hills, platforms, buildings).**

### Elevation Rules

**Higher Ground Advantage**:
- If you are **1+ levels higher** than target:
  - **+1 damage** to attacks
  - Ignore cover (shoot over it)

**Shooting Uphill Penalty**:
- If you are **1+ levels lower** than target:
  - **-1 damage** to attacks

**Levels**:
- Level 0: Ground level (most of map)
- Level 1: Hills, platforms (+1 elevation)
- Level 2: Towers, rooftops (+2 elevation)

**Climbing**:
- Moving UP 1 level: Costs +1 SP (2 SP total)
- Moving DOWN 1 level: Normal cost (1 SP)

---

## Elevation Diagram

```
HIGHER GROUND (+1 damage):
    [A2]        A = Attacker (Level 2)
    [  ]
    [T0]        T = Target (Level 0)

    Attacker 2 levels higher: +1 damage, ignore cover
```

---

## Special LOS Rules

### Aura Effects (Self-Centered Radius)

**Some cards create aura effects:**

**Aura X** = Affects all targets within X hexes of you (including yourself)

```
AURA 2 EXAMPLE:
    [ ][x][x][x][ ]
    [x][x][2][x][x]
    [x][2][A][2][x]   A = You, 2 = Aura range
    [x][x][2][x][x]
    [ ][x][x][x][ ]

    All 'x' and '2' hexes are affected by Aura 2.
```

**Aura ignores LOS** (no need to see targets, just be within range).

---

### Melee Range (Adjacent Only)

**Melee weapons require Range 1 (adjacent).**

**You can melee attack enemies in any of your 6 adjacent hexes**, regardless of facing.

**BUT**: Facing still matters for damage bonuses!
- Front melee: +0 damage
- Side melee: +1 damage
- Rear melee: +2 damage

---

## Quick Reference: Range/LOS Checklist

**Before attacking, check:**

1. ✅ **In range?** (Count hexes from you to target)
2. ✅ **In firing arc?** (Target in front 180° of your facing?)
3. ✅ **Have LOS?** (No walls blocking straight line?)
4. ✅ **Cover?** (Target in/near forest or rubble? +1 Defense)
5. ✅ **Facing modifier?** (Rear +2 dmg, Side +1, Front +0)
6. ✅ **Elevation?** (Higher ground +1 dmg, lower ground -1 dmg)

---

## Common Situations

### "Can I shoot through my ally?"
**Yes.** Other Caskets (ally or enemy) do NOT block LOS.

### "Can I shoot an enemy I can't see?"
**No.** You must have LOS. Walls/dense forest block attacks.

### "Does rubble block LOS?"
**No.** Rubble provides +1 Defense (cover), but doesn't block LOS.

### "Do I need LOS to move?"
**Yes.** You can't move into hexes you can't see (no blind movement through walls).

### "Can I attack behind me without rotating?"
**No.** You can only attack targets in your front 180° arc. Rotate first (free action).

### "If I'm surrounded, can I be attacked from all sides?"
**Yes.** Enemies attack from whatever facing they're in (front/side/rear). Rear attackers get +2 damage.

### "Does cover stack?"
**No.** Maximum +1 Defense from cover, no matter how many cover sources.

### "Can I shoot over allies from higher ground?"
**Yes.** Higher ground ignores cover, including allied Caskets.

---

## Terrain Types Summary

| Terrain | LOS | Movement | Cover | Special |
|---------|-----|----------|-------|---------|
| **Clear** | Pass through | 1 SP/hex | No | Baseline |
| **Forest** | Pass through | 2 SP/hex (difficult) | +1 Def | None |
| **Rubble** | Pass through | 2 SP/hex (difficult) | +1 Def | None |
| **Wall** | BLOCKED | Impassable | N/A | Blocks LOS |
| **Water** | Pass through | 1 SP/hex | No | Remove 2 Heat/turn |
| **Elevated** | Pass through | 2 SP/hex (climb up) | No | +1 dmg if higher |

---

**END OF DOCUMENT**

---

*"Distance is measured in hexes. Death is measured in mistakes. Know your range. Know your angles. Miss once, and you're scrap."*
