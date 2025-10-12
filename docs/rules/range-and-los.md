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

## Range Bands (For To-Hit Modifiers)

**Cards specify maximum range, but to-hit modifiers apply based on distance:**

| Range Band | Distance | To-Hit Modifier | Weapon Examples |
|------------|----------|-----------------|-----------------|
| **Short** | 0-3 hexes | +0 (no penalty) | Melee, pistols, shotguns |
| **Medium** | 4-6 hexes | +1 to target number | Rifles, bows, crossbows |
| **Long** | 7-10 hexes | +2 to target number | Sniper rifles, long bows |
| **Extreme** | 11+ hexes | +3 to target number | Artillery, siege weapons |

**How It Works**:
- **Base To-Hit**: 5+ (roll 2d6 Attack Dice)
- **Apply range modifier** to target number
- Example: Medium range (5 hexes) = need **6+** instead of 5+

**Card Range Examples**:
- **Faithful Thrust**: "Range: Melee" (1 hex only, Short range modifier +0)
- **Quick Shot** (Pistol): "Range 3" (up to 3 hexes, Short range modifier +0)
- **Rifle Shot**: "Range 8" (up to 8 hexes, Long range modifier +2 if shooting 7-8 hexes)
- **Sniper Shot**: "Range 12" (up to 12 hexes, Extreme range modifier +3 if shooting 11-12 hexes)

**Special Range Types**:
- **Self**: Range 0 (affects only you)
- **Aura X**: X hexes radius (affects all units within X hexes, ignores LOS)

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

## Cover System (For To-Hit Modifiers)

**Cover provides defensive bonuses without blocking LOS.**

### Cover Rules

**If target is:**
- In or adjacent to cover terrain (forests, rubble)
- AND attacker's LOS passes through/near that terrain
- **Attacker gets +1 to target number** (harder to hit)

**Cover Terrain Types**:
- **Light Cover** (forest, rubble): +1 to target number
- **Heavy Cover** (fortress walls, dense forest): +2 to target number
- **Other Caskets**: +1 to target number if enemy Casket is between you and attacker

**Cover does NOT stack**:
- Use highest cover modifier only (even if multiple cover sources)
- Example: Target in forest (+1) AND behind fortress wall (+2) = **+2 total** (highest)

**To-Hit Example**:
- Base 5+, target in light cover (rubble) = need **6+** to hit
- Base 5+, target in heavy cover (fortress wall) = need **7+** to hit

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

## Facing & Firing Arcs (6-Hex-Side System)

**Caskets have a facing (which direction they're pointed) AND a shield-side/weapon-side.**

### Hex Facing (6 Directional Sides)

**Each Casket occupies 1 hex and faces ONE of the 6 hex sides.**

```
Hex Sides (6 possible directions):
         1
      6     2
      5     3
         4

1 = Front (primary facing)
2 = Front-Right
3 = Rear-Right
4 = Rear (directly behind)
5 = Rear-Left
6 = Front-Left
```

---

### 6-Hex-Side Arc System

**Attacks from each hex side have different modifiers based on shield/weapon positioning:**

```
         [1]          1 = FRONT (0° - 60°)
      [6] [X] [2]     2 = FRONT-RIGHT (60° - 120°)
      [5]   [3]       3 = REAR-RIGHT (120° - 180°)
         [4]          4 = REAR (180° - 240°)
                      5 = REAR-LEFT (240° - 300°)
X = Your Casket       6 = FRONT-LEFT (300° - 360°)
```

**Rotation**:
- **Free action** (once per turn)
- Rotate 1 hex-side clockwise or counter-clockwise
- Can rotate multiple times by spending 1 SP per additional rotation
- Example: Rotate 3 hex-sides = 1 free + 2 SP

---

### Shield Side & Weapon Side (BattleTech-Inspired)

**When building your Casket, declare which side has your shield:**

**Shield-Side Options**:
- **Left-Shield (default)**: Shield on hex-sides 5, 6, 1 (left + front)
- **Right-Shield**: Shield on hex-sides 1, 2, 3 (right + front)
- **No Shield**: No shield bonuses (if using 2-handed weapon or dual weapons)

**Example - Left-Shield Casket**:
```
    [6-Shield][X][2-Weapon]     Shield protects Left + Front
    [5-Shield]   [3-Weapon]     Weapons on Right side
       [4-Rear]
```

---

### Facing Modifiers (Detailed 6-Hex System + To-Hit)

**Attacking from different hex-sides has specific effects:**

| Hex Side | Arc Name | To-Hit Modifier | Damage Bonus | Defender Defense | Shield Blocks? |
|----------|----------|-----------------|--------------|------------------|----------------|
| **1** (Front) | Front | +0 | +0 | Full Defense | Yes (if shield) |
| **2** (Front-Right) | Weapon Side | +0 | +1 | -1 Defense | No (weapon side exposed) |
| **3** (Rear-Right) | Flank (Weapon) | -1 (easier) | +2 | -2 Defense | No |
| **4** (Rear) | Rear | -2 (easier) | +3 | -3 Defense | No (blind spot) |
| **5** (Rear-Left) | Flank (Shield) | -1 (easier) | +2 | -2 Defense | No |
| **6** (Front-Left) | Shield Side | +1 (harder) | +0 | Full Defense +1 | Yes (shield covered) |

**To-Hit Modifier Explanation**:
- **Easier to hit** (flanks, rear): -1 or -2 to target number (need lower roll)
  - Example: Base 5+, attacking rear (hex 4) = need **3+** instead
- **Harder to hit** (shield-side): +1 to target number (need higher roll)
  - Example: Base 5+, attacking shield-side (hex 6) = need **6+** instead
- **Front/weapon-side**: +0 to target number (standard difficulty)

**Shield Side Advantage**:
- Attacks from **shield-side hexes (6, 1)** can be blocked with shield
- **Hex-side 6 (Front-Left with left-shield)** grants +1 Defense bonus
- Shield-side reactive cards (Deflect, Shield Wall) work on these hexes

**Weapon Side Vulnerability**:
- Attacks from **weapon-side hexes (2, 3)** cannot be blocked by shields
- **Hex-side 2 (Front-Right with left-shield)** gives attacker +1 damage
- You cannot use shield reactive cards against these attacks

**Rear Arc (Hex-sides 3, 4, 5)**:
- All rear attacks gain +2 or +3 damage
- Cannot use reactive defense cards from rear attacks
- Must rotate to defend properly

---

### Tactical Shield Positioning

**"Shield-Wall" Tactic** (BattleTech-inspired):
- Present your shield-side to the most dangerous enemy
- Rotate to keep weapon-side away from threats
- Force enemies to either:
  - Attack your defended side (lower damage)
  - Move to flank (costs them movement SP)

**Example**:
```
Enemy A is dangerous, Enemy B is weak

    [A]                Keep shield facing Enemy A
    [6][X][2]          Enemy A attacks hex-side 6 (shield protected)
        [B]            Enemy B on weapon-side (hex-side 2)
                       But Enemy B is weak, acceptable risk
```

**"Damage Soaking" Tactic**:
- If one side is already damaged (Right Arm destroyed)
- Present that side to enemies (absorb damage on already-broken side)
- Protect your functional side

**Example**:
```
Right Arm destroyed, Left Arm has weapon

    [E]                Present damaged right side
    [2-DMG][X][6-OK]   Enemy attacks hex-side 2 (already broken)
                       Hex-side 6 still functional, protected
```

---

## Facing Diagrams (6-Hex System)

```
DIRECT REAR ATTACK (Hex-side 4 - Most Vulnerable):
       [ ]
    [ ][T][  ]   T = Target (facing DOWN ↓)
    [A][ ][  ]   A = Attacker (hex-side 4)
       ↓

    Attacker at hex-side 4 (rear)
    +3 damage, target's Defense -3
    Target CANNOT use reactive defense cards
```

```
FLANK ATTACK - WEAPON SIDE (Hex-side 2 or 3):
       [ ]
    [ ][T←][A]   T = Target (left-shield, facing LEFT ←)
       [ ]       A = Attacker (hex-side 2, weapon side)

    Attacker at hex-side 2 (front-right, weapon side)
    +1 damage, target's Defense -1
    Target CANNOT block with shield
```

```
SHIELD SIDE ATTACK (Hex-side 6 - Best Defense):
       [ ]
    [A][T→][ ]   T = Target (left-shield, facing RIGHT →)
       [ ]       A = Attacker (hex-side 6, shield side)

    Attacker at hex-side 6 (front-left, shield side)
    +0 damage, target's Defense FULL +1
    Target CAN use shield reactive cards
```

```
FRONT ATTACK (Hex-side 1 - Expected):
       [A]
    [ ][T][ ]   T = Target (facing UP ↑)
       [ ]      A = Attacker (hex-side 1)
       ↑

    Attacker at hex-side 1 (front)
    +0 damage, target's Defense FULL
    Target can defend normally
```

---

## Elevation & Height

**Some hexes are elevated (hills, platforms, buildings).**

### Elevation Rules (For To-Hit & Damage)

**Higher Ground Advantage**:
- If you are **1+ levels higher** than target:
  - **-1 to target number** (easier to hit)
  - **+1 damage** to attacks (if hit)
  - Ignore cover (shoot over it)

**Shooting Uphill Penalty**:
- If you are **1+ levels lower** than target:
  - **+1 to target number** (harder to hit)
  - **-1 damage** to attacks (if hit)

**Levels**:
- Level 0: Ground level (most of map)
- Level 1: Hills, platforms (+1 elevation)
- Level 2: Towers, rooftops (+2 elevation)

**Climbing**:
- Moving UP 1 level: Costs +1 SP (2 SP total)
- Moving DOWN 1 level: Normal cost (1 SP)

**To-Hit Example**:
- Attacker on Level 2, target on Level 0 (2 levels higher)
- Base 5+ → -1 modifier (higher ground) = need **4+** to hit
- If hit, +1 damage bonus

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

## Quick Reference: Range/LOS/Facing Checklist (With To-Hit)

**Before attacking, check:**

1. ✅ **In range?** (Count hexes from you to target)
2. ✅ **In firing arc?** (Target in front 180° of your facing?)
3. ✅ **Have LOS?** (No walls blocking straight line?)
4. ✅ **Calculate To-Hit Number:**
   - Base: 5+
   - Range modifier: Short +0, Medium +1, Long +2, Extreme +3
   - Attacker movement: 0 hexes +0, 1-3 +1, 4-6 +2, 7+ +3
   - Defender movement: 0 hexes +0, 1-3 +1, 4-6 +2, 7+ +3
   - Hex-side facing: Front +0, Weapon +0, Flank -1, Rear -2, Shield +1
   - Cover: Light +1, Heavy +2
   - Elevation: Higher -1, Lower +1
5. ✅ **Roll 2 Attack Dice** (add values, compare to target number)
6. ✅ **If hit, apply damage modifiers:**
   - Strong Hit (7-8): +1 damage
   - Critical Hit (9): +2 damage, bypass 1 Defense
   - EXECUTION (10): Auto-destroy component, bypass all Defense
   - Hex-side bonus: Weapon +1, Flank +2, Rear +3
   - Elevation: Higher +1, Lower -1

### Hex-Side Quick Reference Table (With To-Hit)

| Hex-Side | Name | To-Hit Mod | Damage Bonus | Defense Penalty | Shield Blocks? | Reactive Cards? |
|----------|------|------------|--------------|-----------------|----------------|-----------------|
| 1 | Front | +0 | +0 | 0 | Yes | Yes |
| 2 | Front-Right (Weapon) | +0 | +1 | -1 | No | Yes |
| 3 | Rear-Right (Flank) | -1 | +2 | -2 | No | No |
| 4 | Rear (Blind) | -2 | +3 | -3 | No | No |
| 5 | Rear-Left (Flank) | -1 | +2 | -2 | No | No |
| 6 | Front-Left (Shield) | +1 | +0 | 0 (+1 if shield) | Yes | Yes |

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

### "I have a shield on my left arm. Which hex-sides does it protect?"
**Left-Shield protects hex-sides 5, 6, and 1** (rear-left, front-left, and front).
Hex-sides 2, 3, 4 are vulnerable (weapon side + rear).

### "My opponent has a right-shield. Which side should I attack?"
**Attack their LEFT side (your right when facing them)** - hex-sides 5, 6.
Their shield is on hex-sides 1, 2, 3 (their right), so attacking from their left bypasses the shield.

### "Can I block an attack from my weapon-side with my shield?"
**No.** Shield reactive cards (Deflect, Shield Wall, etc.) only work if the attack comes from your shield-side hexes.

### "I'm being attacked from hex-side 4 (direct rear). Can I use Brace for Impact?"
**No.** Rear attacks (hex-sides 3, 4, 5) cannot be defended with reactive cards. You must rotate to defend.

### "How do I know which hex-side an attack is coming from?"
**Determine which of the 6 hexes adjacent to the defender contains the attacker.**
```
         [1]
      [6] [D] [2]    D = Defender
      [5]   [3]
         [4]
```
If attacker is in hex 2, it's a Front-Right (weapon-side) attack.

### "Can I rotate to change my facing mid-combat?"
**Yes.** Rotate once per turn for free, or spend 1 SP per additional rotation.
**Example**: Rotate 180° (3 hex-sides) = 1 free + 2 SP = costs 2 SP total.

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
