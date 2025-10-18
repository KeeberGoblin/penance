# Combat & Damage System (GKR + KDM Hybrid)
## Penance: Absolution Through Steel

**Version**: 2.0 Base Rules (October 10, 2025)
**v3.0 Enhancements**: Optional [Dice Pool Advantage](dice-pool-advantage.md) and [Taint Exploitation](taint-exploitation.md) available

---

## Core Concept: Dual-Layer Damage

Inspired by **GKR: Heavy Hitters** (deck-as-HP) + **Kingdom Death: Monster** (brutal consequences)

**Two Separate Systems**:
1. **Casket HP Deck** (26-50 cards, varies by [Casket Class](casket-classes.md) and equipment loadout) - Your mech's structural integrity
2. **Pilot Wound Deck** (10 cards) - Your pilot's physical/mental state

When **Casket HP Deck runs out** → Casket is destroyed (pilot may survive)
When **Pilot Wound Deck runs out** → Pilot dies (Casket becomes inert)

---

## 1. Casket HP Deck (Variable Size)

### The 3-Pile System (CRITICAL CONCEPT)

**Your Casket uses THREE separate card piles during battle:**

1. **HP Draw Deck** (26-50 cards) - Your active deck, represents structural integrity
2. **Discard Pile** - Cards you've **played/used** during your turn (attacks, movement, abilities)
3. **Damage Graveyard** - Cards **destroyed by taking damage** (permanent loss, gone forever)

**Key Distinction:**
- **Play a card** (attack, defend, move) → Goes to **Discard Pile** → Will reshuffle when draw deck empty
- **Take damage** (enemy hits you) → Cards go to **Damage Graveyard** → **NEVER comes back** (death spiral)
- Some factions can interact with Damage Graveyard (Ossuarium resurrect, Nomads scavenge, etc.)

**Example:**
- You play "Faithful Thrust" (2 SP attack) → Card goes to **Discard Pile**
- Enemy hits you for 5 damage → You discard 5 cards from deck/hand to **Damage Graveyard** (gone forever)
- Later, your HP Draw Deck is empty → Reshuffle **Discard Pile** into new deck (Damage Graveyard stays separate)

---

### Major Wounds & DAMAGED Cards

**When you take major damage in a single attack:**
- This is a **Major Wound** (threshold varies by [Casket Class](casket-classes.md): Scout 3+, Warden 5+, Vanguard 7+, Colossus 9+)
- Add 1 **DAMAGED card** to your **Discard Pile** immediately
- That DAMAGED card will enter your HP Draw Deck on your next reshuffle
- DAMAGED cards represent lingering injuries

**DAMAGED Card Text:**
> **"DAMAGED"**
>
> *This card persists in your hand (not discarded at end of round). Takes up 1 card slot.*
>
> **0 SP Action - Remove this card (choose one):**
> - **Sacrifice** (to Discard Pile): Roll Damage Die → Card will reshuffle back into deck later
> - **Purge** (to Damage Graveyard): Roll Damage Die → Card removed permanently
>
> *When discarded by damage: Roll 1 Damage Die (cascading failure).*

**Damage Die (1d6) Results:**

| Roll | Result | Effect |
|------|--------|--------|
| **1** | **Minor Strain** | Gain 1 Heat |
| **2** | **System Glitch** | -1 SP at start of next turn |
| **3** | **Internal Bleeding** | Discard 1 card at start of next turn |
| **4** | **Structural Weakness** | Next attack against you: +1 Component Damage |
| **5** | **Critical Malfunction** | +1 Pilot Wound |
| **6** | **Adrenaline Surge** | Gain 1 SP immediately (rare good outcome!) |

**Strategic Impact:**
- **DAMAGED cards persist in hand** like a curse, taking up valuable card slots
- **Tactical choice**: Keep it (clogs hand), Sacrifice it (comes back later), or Purge it (roll die but gone forever)
- Drawing DAMAGED early = more control over when to deal with it
- Getting hit while DAMAGED cards are in deck = cascading failures
- After 3-4 Major Wounds in your hand simultaneously = crippling hand pressure

**Example Flow:**
1. **Round 1, Turn 3**: Church takes 7 damage from Dwarf (Major Wound!)
   - Discard 7 cards to **Damage Graveyard** (gone forever)
   - Add 1 **DAMAGED card** to **Discard Pile**
   - **End of Round 1**: Discard hand to Discard Pile (no DAMAGED in hand yet)

2. **Round 2, Turn 1**: Church's HP Draw Deck runs out during draw phase
   - Reshuffle **Discard Pile** into new HP Draw Deck
   - Draws 6 cards, one is the **DAMAGED card**
   - Hand: [Faithful Thrust] [Blood Offering] [DAMAGED] [Brace] [Feint] [Rally]

3. **Round 2, Turn 3**: Church plays 3 cards, DAMAGED card stays in hand
   - **End of Round 2**: Discard 2 useful cards to Discard Pile
   - **DAMAGED card persists in hand** (curse!)

4. **Round 3, Turn 1**: Church draws 4 cards (already has 1 DAMAGED in hand)
   - Hand: [DAMAGED] + 4 new cards = 5 cards total
   - **Decision time**: "I'll Purge this wound now"
   - Church uses 0 SP action: **Purge DAMAGED** → Roll Damage Die
   - Roll: **2 (System Glitch)** → -1 SP next turn
   - DAMAGED card goes to **Damage Graveyard** (gone forever!)
   - Hand now freed up, Church draws 1 more card to reach 6

---

### Deck Composition (GKR-Style + v2.0 Modular Equipment)

Your HP Draw Deck represents your Casket's structural integrity.

**v2.0 Variable Deck System** (26-50 cards depending on equipment):
- **10 Universal Cards** (mandatory, everyone has these)
- **6 Faction Core Cards** (faction-specific foundation)
- **Equipment Cards** (variable 3-30 cards: Weapon + Shield/Offhand + Accessories)
- **2 Faction Tactic Cards** (chosen from 5 available, pick 2 before battle)

**Total: 26-50 cards** (Light Caskets ~26-32, Heavy Caskets ~38-50)

> **NOTE**: This section shows **simplified v1.0 example** for teaching. See [deck-equipment-system.md](../factions/church/deck-equipment-system.md) for full v2.0 modular equipment.

---

### Universal Core (10 Cards)

Everyone has these 10 cards (basic movement, defense, utility):

| Card Name | Type | SP Cost | Effect |
|-----------|------|---------|--------|
| **Desperate Lunge** | Movement | 1 | Move up to 2 hexes |
| **Brace for Impact** | Defense (Reactive) | 0 | Reduce next damage by 2 |
| **Emergency Vent** | Heat Management | 2 | Remove 3 Heat |
| **Sensor Sweep** | Utility | 1 | Reveal 1 enemy card in hand |
| **Overextend** | Movement | 1 | Move 3 hexes, gain 1 Heat |
| **Rally Cry** | Support | 2 | Ally within 3 hexes draws 1 card |
| **Survey the Field** | Utility | 1 | Draw 1 card |
| **Feint** | Combat | 1 | Next attack this turn: +1 damage |
| **Retreat** | Movement | 2 | Move 4 hexes, cannot attack this turn |
| **Breathe the Core** | Heat Management | 1 | Remove 1 Heat, draw 1 card |

---

### Primary Weapon Cards (12 Cards)

**Faction-specific, defines your playstyle.**

This is your **main weapon system** built into the Casket. Cannot be changed mid-campaign (it's part of the Casket chassis).

**Example: Church Confessor - "Penitent Blades"** (12 cards)

| Card Name | SP Cost | Effect |
|-----------|---------|--------|
| **Blood Offering** × 2 | 0 | Discard 2 cards (self-harm). Next attack: +3 damage, ignore 1 Armor |
| **Faithful Thrust** × 3 | 2 | Deal 4 damage. Rear attack: +2 damage |
| **Righteous Cleave** × 2 | 3 | Deal 5 damage to primary target, 2 damage to adjacent enemy |
| **Martyrdom Protocol** × 2 | 1 | Redirect 1 attack targeting ally to yourself this round |
| **Divine Judgment** × 2 | 4 | If target has 10 or fewer cards in deck, deal 8 damage |
| **Consecrated Ground** × 1 | 3 | Create healing zone (3-hex radius). Allies recover 2 cards/turn |

**Design Notes**:
- Some cards have **multiple copies** (Faithful Thrust × 3 = you can draw it more often)
- Mix of offense, utility, and self-sacrifice
- Total: 12 cards

---

### Secondary Weapon/Equipment Cards (6 Cards)

**Customizable loadout** chosen during deck construction.

Choose ONE of the following equipment sets (each adds 6 cards):

**Option A: Buckler Shield**
- Deflect × 2 (Reactive, 0 SP: Reduce damage by 1)
- Bash × 2 (1 SP: Deal 2 damage, push 1 hex)
- Hunker Down × 2 (2 SP: +2 Defense this round)

**Option B: Tower Shield**
- Wall of Iron × 2 (Reactive, 0 SP: Reduce damage by 3, gain 1 Heat)
- Shield Wall × 2 (3 SP: Allies behind you get +2 Defense)
- Advance × 2 (2 SP: Move 2 hexes, Defense +1 this turn)

**Option C: Repair Kit (Relic)**
- Emergency Repair × 2 (2 SP: Recover 3 cards from discard)
- Scrap Armor × 2 (1 SP: Gain 1 Armor until damaged)
- Jury-Rig × 2 (3 SP: Shuffle discard into deck, do not add Damage card)

**Option D: Secondary Weapon (Pistol)**
- Quick Shot × 3 (1 SP: Deal 2 damage, Range 3)
- Dual Wield × 2 (2 SP: Deal 3 damage, then discard 1 card)
- Suppressing Fire × 1 (3 SP: Deal 2 damage to up to 3 targets)

---

### Faction Tactic Cards (2 Cards)

**Choose 2 from 5 available before each battle** (GKR-style deck customization).

**Example: Church of Absolution Tactics**

Available pool (choose 2):
1. **Blood Offering** (already in Primary, don't duplicate)
2. **Righteous Fury** (Passive: Each enemy killed this mission: +1 permanent damage)
3. **Martyrdom Protocol** (already in Primary, don't duplicate)
4. **Divine Judgment** (already in Primary, don't duplicate)
5. **Flagellant's Zeal** (Once per mission: Discard 5 cards, gain 5 SP immediately)

Wait, this creates duplication issues. Let me revise:

**Faction Tactics are UNIQUE cards not in Primary weapon.**

**Church Tactics** (choose 2 from 5):
1. **Righteous Fury** (Passive: Each kill: +1 damage to all attacks permanently this mission)
2. **Flagellant's Zeal** (4 SP: Discard 5 cards, gain 5 SP immediately)
3. **Last Rites** (0 SP, Reactive: When ally is defeated, recover 5 cards)
4. **Absolution** (5 SP: Remove all Heat, recover 3 cards, gain 1 Taint)
5. **Crusader's Vow** (Passive: While above 20 cards in deck, -1 SP to all attacks)

---

## 2. Attack Resolution (To-Hit System)

### Step 1: Declare Attack

**Attacker declares**:
1. Target enemy
2. Which attack card to play (sets base damage)
3. **Which component to target:**

**Targeting Methods (choose one):**

**A. Attacker Chooses (Tactical) - RECOMMENDED**
- Attacker selects component: Head, Right Arm, Left Arm, Chassis, or Legs
- Gives tactical control (target exposed components, focus fire, etc.)

**B. Random Hit Location (Chaotic)**
- Roll **1d6** for hit location:
  - **1:** Head
  - **2:** Left Arm
  - **3:** Right Arm
  - **4-5:** Chassis (most likely, center mass)
  - **6:** Legs
- Use for "wild" attacks or when card doesn't specify
- Creates unpredictability (might hit fresh or damaged components)

**C. Card Specifies**
- Some cards have built-in targeting (e.g., "Leg Sweep" always targets Legs)
- Card text overrides player choice

4. Range and facing

---

### Step 2: Calculate To-Hit Number

**Base To-Hit**: **5+** (roll 2d6 Attack Dice, need 5+ total)

> **v3.0 OPTIONAL**: Instead of static modifiers (+1/+2), use [Dice Pool Advantage](dice-pool-advantage.md) system. Roll 3d6 take 2 highest (Advantage) or 3d6 take 2 lowest (Disadvantage). See quick-reference.md for conversion table.

**Apply ALL applicable modifiers**:

#### Range Modifiers
- **Short Range (0-3 hexes)**: +0
- **Medium Range (4-6 hexes)**: +1 to target number (need 6+)
- **Long Range (7-10 hexes)**: +2 to target number (need 7+)
- **Extreme Range (11+ hexes)**: +3 to target number (need 8+)

#### Attacker Movement (This Turn)
- **Stationary (0 hexes moved)**: +0
- **Moved 1-3 hexes**: +1
- **Moved 4-6 hexes**: +2
- **Sprinted (7+ hexes)**: +3

#### Defender Movement (Last Turn)
- **Stationary**: +0
- **Moved 1-3 hexes**: +1
- **Moved 4-6 hexes**: +2
- **Sprinted (7+ hexes)**: +3

#### Hex-Side Facing
- **Front Arc (Hex 1)**: +0
- **Weapon-Side (Hex 2)**: +0 (but +1 damage if hit)
- **Flanks (Hex 3, 5)**: -1 (easier, need 4+)
- **Rear (Hex 4)**: -2 (easier, need 3+)
- **Shield-Side (Hex 6)**: +1 (harder, need 6+)

#### Terrain Modifiers
- **Light Cover** (rubble, low walls): +1
- **Heavy Cover** (fortress walls, forest): +2
- **Obscured** (smoke, darkness): +2
- **Elevated** (attacker on high ground): -1 (easier)

**Example**:
- Base: 5+
- Medium range: +1 (need 6+)
- Attacker moved 4 hexes: +1 (need 7+)
- Defender moved 2 hexes: +1 (need 8+)
- Shield-side facing: +1 (need **9+**)

---

### Step 3: Roll Attack Dice

**Roll 2d6 Attack Dice** (custom dice with symbols):

#### Attack Die Faces
| Symbol | Value | Name |
|--------|-------|------|
| | 3 | STRIKE |
| | 4 | DOUBLE STRIKE |
| | 5 | DEATH BLOW |
| | 1 | GLANCE |
| | 0 | JAM |
| | 2 | BLOOD |

**Add both dice results, compare to target number**:

#### Hit Results
- **5-6 total** = **Hit** (standard damage)
- **7-8 total** = **Strong Hit** (standard damage +1)
- **9-10 total** = **Critical Hit** (standard damage +2, bypass 1 Defense)
- **10 (double )** = **EXECUTION** (auto-destroy 1 Component, bypass ALL Defense)

#### Miss Results
- **Below target number** = **MISS** (no damage, attack wasted)
- **2 (double )** = **CATASTROPHIC FAILURE**:
 - Weapon jams (discard all Primary Weapon cards from hand)
 - +2 Heat (weapon overload)
 - Next attack -2 damage (weapon damaged)

---

### Step 4: Roll Defense Dice (If Hit)

**If attack hits, Defender rolls Defense Dice**:

**Roll 1d6 Defense Die per damage point**

#### Defense Die Faces
| Symbol | Effect |
|--------|--------|
| **SHIELD** | Block 1 damage |
| **ABSORB** | Block 1 damage |
| **FLESH WOUND** | Take damage (discard 1 card) |
| **CRITICAL** | Take damage + 1 Component Damage |
| **PIERCE** | Take damage, cannot use reactive cards |
| **HEAT** | Take damage + 1 Heat |

**Count results**:
1. Count **SHIELD** () and **ABSORB** () symbols → Reduce damage by this amount
2. Apply special effects from **CRITICAL** (), **PIERCE** (), **HEAT** ()
3. Final damage = Original damage - Blocks

**Example**: Take 6 damage → Roll 6 Defense Dice
- Result: 
- **2 blocks** = Reduce to 4 damage
- **1 Critical** () = +1 Component Damage
- **1 Heat** () = +1 Heat
- **1 Pierce** () = Cannot use reactive defense cards
- **Final**: Discard 4 cards + 1 Component Damage + 1 Heat

---

### Step 5: Apply Damage (Damage Graveyard)

**Defender chooses how to discard cards to Damage Graveyard**:

- **From Hand**: Lose tactical options but control what's lost
- **From Deck**: Keep hand intact but risk losing key cards randomly
- **Mixed**: Discard some from hand, some from deck

**Example**: Take 5 damage → Discard 3 from hand + 2 from deck top to **Damage Graveyard**

**Strategic Depth**: Do you burn your hand to avoid Component Damage? Or keep cards and risk it?

**Major Wound Check:**
- If damage taken ≥ 5 in this single attack → Add 1 **DAMAGED card** to your **Discard Pile** immediately
- If you discarded any DAMAGED cards from your hand/deck during this damage → Roll Damage Die for each

---

### Step 6: Check for Component Damage

**If you discarded any Primary Weapon equipment cards**:
- Mark 1 Component Damage per Primary Weapon card to targeted component
- Track separately: Right Arm, Left Arm, Legs, Head, Chassis
- **Component destruction threshold varies by limb** (Head 3, Arms 4, Chassis 5, Legs 6)

**If Defense Dice showed CRITICAL symbols ()**:
- Add +1 Component Damage per symbol to targeted component

> **v2.0 NOTE**: "Primary Weapon cards" refers to your equipped weapon cards (e.g., Longsword, Greatsword, Pistol). These are the cards you discarded from your Primary Weapon slot equipment.

## 3. Component Damage (AP/Structure/Pilot Exposure System)

> **COMPREHENSIVE RULES**: See [component-damage-system.md](component-damage-system.md) for full AP/Structure/Pilot Exposure mechanics, SCRAP card rules, and complete examples.

### Quick Reference: Component HP Zones

**Each component has three defensive zones:**

> **NOTE:** These values are for the **Warden** (standard) Casket class. Component HP varies by class - see [Casket Classes](casket-classes.md) for Scout/Vanguard/Colossus variants.

| Component | Total HP | AP Zone | Structure Zone | Pilot Exposure Zone |
|-----------|----------|---------|----------------|---------------------|
| **Head** | 8 HP | 0-3 dmg | 4-5 dmg | 6-8 dmg |
| **Right Arm** | 8 HP | 0-3 dmg | 4-5 dmg | 6-8 dmg |
| **Left Arm** | 8 HP | 0-3 dmg | 4-5 dmg | 6-8 dmg |
| **Chassis** | 10 HP | 0-4 dmg | 5-6 dmg | 7-10 dmg |
| **Legs** | 10 HP | 0-4 dmg | 5-10 dmg | NEVER |

**Zone Effects:**
- **AP Zone**: Armor absorbs damage, no penalties
- **Structure Zone**: Functional penalties begin (-1 to -2 damage, +1 SP costs, etc.)
- **Pilot Exposure Zone**: **Every Component Damage = +1 Pilot Wound** (CRITICAL)

### Tracking Component Damage

**How it accumulates**:
1. Attacker declares target component (choose method):
   - **Tactical (recommended):** Attacker chooses component
   - **Random:** Roll 1d6 (1=Head, 2=L.Arm, 3=R.Arm, 4-5=Chassis, 6=Legs)
   - **Card-specified:** Some cards auto-target (e.g., "Headshot" → Head)

2. When **Primary Weapon or Shield/Offhand cards** are discarded from damage → 1 Component Damage per card

3. When Defense Dice show **CRITICAL ()** → +1 Component Damage (bypasses AP layer!)

4. Component Damage accumulates, moving through zones (AP → Structure → Pilot Exposure → Destroyed)

**Example Progression:**
- Right Arm at 3/8 HP (AP zone, no penalties)
- Takes 4 Component Damage → Now at 7/8 HP
- Progression: 3 (AP) → 4 (enter structure, -1 dmg) → 5 (structure, -1 dmg) → 6 (enter pilot exposure, **+1 Wound**) → 7 (pilot exposed, **+1 Wound**)
- **Total: +2 Pilot Wounds from this attack, arm near destruction**

---

### Component Effects by Zone

**AP Zone (Armor Plating):**
- No functional penalties
- Armor cracking, sparks flying, but fully operational
- This is the "safe zone" - pilot protected

**Structure Zone (Frame Damage):**
- Functional penalties begin:
  - Arms: -1 to -2 damage from attacks
  - Chassis: -1 to -2 SP maximum, movement penalties
  - Head: -1 ranged attacks, +1 Heat/turn
  - Legs: +1 to +2 SP per hex movement
- Component degrading but still usable
- Pilot still protected (no wounds yet)

**Pilot Exposure Zone (CRITICAL):**
- **Every Component Damage taken = +1 Pilot Wound**
- Capsule breached, pilot directly vulnerable
- Component near total failure
- Desperate situation - one more hit could destroy component

**Component Destroyed:**
- All associated equipment cards → **SCRAP** (see component-damage-system.md)
- SCRAP cards can be cannibalized (0 SP): Discard → Draw 1 card
- Component unusable for rest of battle
- **Final destruction wound:** +1 Pilot Wound (except Legs)
- **Chassis destruction special:** +3 Pilot Wounds immediately, ejection save required

## 4. Deck Depletion (Running Out of HP)

**When your HP Draw Deck runs out mid-turn while taking damage**:
- Continue taking damage by discarding from **Discard Pile** to **Damage Graveyard**
- If Discard Pile is also empty, you're **Defeated** (structural collapse)

**When you would draw a card but HP Draw Deck is empty**:
- **Reshuffle Trigger**
- Shuffle your **Discard Pile** into a new HP Draw Deck
- **Damage Graveyard stays separate** (those cards are gone forever)
- Draw normally
- **NOTE**: You do NOT add DAMAGED cards on reshuffle - only when taking Major Wounds (5+ damage)

**Death Spiral Mechanics**:
- Every card in **Damage Graveyard** = permanent HP loss
- DAMAGED cards in your deck = dead draws + cascading penalties
- Factions can interact with Damage Graveyard (resurrect, scavenge, etc.)
- After 20 damage taken + 3 Major Wounds, you might have:
  - 20 cards in Damage Graveyard (gone forever)
  - 3 DAMAGED cards in your remaining deck
  - Death spiral is inevitable but manageable

---

## 5. Pilot Wound Deck (10 Cards)

### Separate from Casket HP

**The Pilot has their own 10-card Wound Deck.**

This represents pilot physical/mental state inside the capsule.

**Starting Wound Deck** (10 cards, all face-down):

| Card | Quantity | Type |
|------|----------|------|
| **Minor Injury** | 5 | Recoverable |
| **Severe Injury** | 3 | Permanent effect |
| **Trauma** | 2 | Mental breakdown |

---

### When Pilot Takes Damage

**Pilots take damage (flip Wound cards) in these situations**:

1. **Component Pilot Exposure** (NEW PRIMARY SOURCE)
   - Any Component Damage while component is in Pilot Exposure Zone → +1 Wound per damage
   - Can take 2-3 Wounds in single attack if component destroyed from exposure zone
   - See [component-damage-system.md](component-damage-system.md) for full mechanics

2. **Chassis Destruction** (CRITICAL - INSTANT DEATH RISK)
   - Chassis destroyed → +3 Wounds immediately
   - Then roll ejection save: 1-2 = +2 more Wounds (likely death), 3-6 = survive

3. **Head Destruction**
   - Head destroyed → +1 Wound (neural feedback from sensor destruction)

4. **Neural Feedback** (Cumulative Strain)
   - When total Component Damage across ALL components ≥ 15 → +1 Wound
   - Check at end of each attack that adds Component Damage

5. **Casket HP Deck Empty**
   - Deck + Discard both empty → Roll save (1d6): 1-3 = +2 Wounds, 4-6 = survive extraction

> **v3.0 OPTIONAL**: Use [Taint Exploitation](taint-exploitation.md) to spend Taint tactically (offensive debuffs, defensive power-ups). Taint becomes a resource, not just a threshold.

**When Pilot takes damage**:
- Flip 1 Wound Card face-up per damage
- Read effect immediately
- Card remains face-up (permanent)

> **v3.0 OPTIONAL**: Roll 1d6 + [Pilot Grit](../campaigns/pilot-grit-system.md) to resist Wound. On 5+, ignore 1 Wound. Veterans (Grit 2-3) are mechanically tougher.

---

### Wound Card Effects

**Minor Injury** (5 cards):
1. **Concussion**: -1 to all SP until end of mission
2. **Broken Finger**: Cannot use 1 specific card type (roll d10 for which finger/thread)
3. **Internal Bleeding**: At start of each round, discard 1 card from Casket deck
4. **Dislocated Shoulder**: -2 damage to all attacks until end of mission
5. **Cracked Rib**: Each time you gain Heat, gain +1 additional Heat

**Severe Injury** (3 cards):
1. **Shattered Hand**: Permanently lose 2 Neural Threads. -2 SP maximum (PERMANENT, even after mission)
2. **Spinal Trauma**: Movement costs +1 SP per hex (PERMANENT)
3. **Ruptured Organ**: Start each mission at -5 Casket HP (discard 5 cards at deployment)

**Trauma** (2 cards):
1. **PTSD**: Cannot attack enemies from behind (triggers panic)
2. **Dissociation**: At start of each turn, roll 1d6. On 1-2, lose 1 SP this turn (pilot zones out)

---

### Pilot Death

**If all 10 Wound Cards are face-up → Pilot Dies**

- Casket becomes inert (stops moving)
- Pilot must be extracted (if allies present)
- Campaign: Pilot is dead, roll new character
- Arena: Match loss

---

## 6. Suffering Dice (Church & Event System)

**For Church of Absolution and brutal campaign events**, use **Suffering Dice (d6)** for self-harm mechanics:

### Suffering Die Faces

| Symbol | Effect |
|--------|--------|
| **BLOOD PRICE** | Discard 2 cards (self-harm) |
| **MARTYRDOM** | Discard 3 cards, +3 damage to next attack |
| **ZEALOT'S FURY** | Discard 1 card, +1 damage to all attacks this turn |
| **DIVINE MERCY** | No self-harm |
| **PENANCE** | Discard 1 card, +1 Heat, +2 damage next attack |
| **ABSOLUTION** | Discard 1 card, recover 1 card from discard |

### When to Roll Suffering Dice

**Church Faction Abilities**:
- **BLOOD OFFERING** card: Instead of auto-discarding 2 cards, roll 1 Suffering Die
- **Flagellant's Zeal** Tactic: Roll 2 Suffering Dice, apply both effects
- **Martyrdom Protocol**: When redirecting damage, roll 1 Suffering Die per 3 damage redirected

**Campaign Events**:
- **Penance Rituals** (settlement events)
- **Taint Purging** (when Taint reaches 8+)
- **Soul Bargains** (desperate deals with Bonelord Thresh)

---

## 7. SP Economy (Energy System)

### SP by Frame Type

Following GKR's energy economy, but adapted to Penance's weight classes:

| Casket Type | SP Maximum | Deck Size Range | Philosophy |
|-------------|------------|-----------------|------------|
| **Scout (Light)** | 6 SP | 26-32 cards | Speed & efficiency (minimal equipment) |
| **Assault (Medium)** | 5 SP | 30-38 cards | Balanced (moderate equipment) |
| **Heavy** | 4 SP | 35-45 cards | Endurance (heavy equipment) |
| **Fortress** | 3 SP | 38-50 cards | Power over finesse (maximum equipment) |

**Why decreasing SP for heavier frames?**
- Heavy Caskets are slower, less energy-efficient
- Forces different playstyles (Light = many small actions, Assault = few powerful actions)
- Balances high armor/HP with lower action economy

---

### SP Refresh

**At start of your turn**:
- Restore SP to maximum
- Exception: If in **Danger Zone** (5+ Heat), roll Strain first

**SP costs examples**:
- Movement: 1 SP per hex
- Attacks: 1-5 SP (varies by card)
- Reactive defense: 0 SP (interrupt opponent's turn)
- Utility: 1-3 SP

---

### Heat System (Limits SP)

**Heat replaces GKR's "Energy drain" mechanic.**

**Heat Zones**:
- **Safe Zone** (0-4 Heat): No penalties
- **Danger Zone** (5+ Heat): Roll Strain at start of turn
- **Critical** (10+ Heat): Automatic system failures

**Strain Roll** (1d6 + Heat):
- 1-5: Gain 1 Heat
- 6-8: Lose 1 SP this turn
- 9-11: Take 2 damage (discard 2 cards)
- 12+: Component malfunction (lose 1 random Component)

**Heat Management**:
- Vent actively (Emergency Vent card, Breathe the Core)
- Stand in water hexes (remove 2 Heat/turn)
- Pass your turn (remove 1 Heat)

---

## 8. Card Draw & Hand Management

### Starting Hand: 6 Cards

**At start of battle**:
- Shuffle your Casket HP deck (26-50 cards depending on equipment loadout)
- Draw 6 cards
- Mulligan: May shuffle hand back and draw 6 new cards (once)

### Drawing Cards

**Draw Phase** (end of your turn):
- Draw until hand = 6 cards
- If deck empty, trigger Reshuffle (add 1 Damage card)

**Mid-Turn Draw**:
- Some cards have "Draw 1 card" effect
- Draw immediately from deck

---

## 9. Victory Conditions

### Arena/Skirmish

**Win by**:
- Reducing enemy Casket to 0 HP (deck empty + discard empty)
- Killing enemy pilot (10 Wounds)
- Enemy surrenders

**Defeat**:
- Your Casket destroyed
- Your pilot dies
- You surrender

### Campaign

**Mission Success**:
- Achieve primary objective
- At least 1 pilot survives

**Partial Success**:
- Primary objective failed
- But pilots survived (can retreat)

**Mission Failure**:
- All pilots dead or captured

---

## 10. Deck Construction Summary

### Template: Church Confessor (Light Casket)

**Total Deck: 30 cards**

1. **Universal Core** (10 cards) - MANDATORY
 - Desperate Lunge, Brace for Impact, Emergency Vent, Sensor Sweep, Overextend, Rally Cry, Survey the Field, Feint, Retreat, Breathe the Core

2. **Primary Weapon: Penitent Blades** (12 cards) - FACTION-SPECIFIC
 - Blood Offering × 2
 - Faithful Thrust × 3
 - Righteous Cleave × 2
 - Martyrdom Protocol × 2
 - Divine Judgment × 2
 - Consecrated Ground × 1

3. **Secondary Equipment: Buckler Shield** (6 cards) - PLAYER CHOICE
 - Deflect × 2
 - Bash × 2
 - Hunker Down × 2

4. **Faction Tactics** (2 cards) - CHOOSE 2 FROM 5
 - Righteous Fury
 - Flagellant's Zeal

**SP Maximum**: 6 (Light Casket)
**Pilot Wound Deck**: 10 cards (separate)

---

## 11. Differences from Standard Deck-Builders

### Like GKR:
- ✅ Deck = HP (discard cards when damaged)
- ✅ Energy/SP refresh each turn
- ✅ Primary vs Secondary weapon split
- ✅ Pre-built decks (no mid-game deck-building)
- ✅ Hand size fixed at 6

### Like KDM:
- ✅ Component damage tracking (arms, legs, head destroyed)
- ✅ Permanent injuries (Pilot Wound deck)
- ✅ Death spiral (Damage cards added to deck on reshuffle)
- ✅ Brutal consequences (losing Primary Weapon cards = component damage)

### Unique to Penance:
- Heat system (risk/reward pushing into Danger Zone)
- Pilot Wound deck (separate from Casket HP)
- Neural Thread damage (pilot takes damage when components destroyed)
- Asymmetric factions (Primary Weapon cards completely different per faction)

---

## 12. Example Combat Sequence (With Dice)

### Setup:
- **Player A**: Church Confessor (28-card deck, 6 SP, 6 cards in hand)
- **Player B**: Dwarven Ironclad (36-card deck, 4 SP, 6 cards in hand)

---

### Round 1

**Player A Turn** (Confessor):
1. Refresh to 6 SP
2. Play **Desperate Lunge** (1 SP) → Move 2 hexes toward enemy (total moved: 2 hexes)
3. Play **Faithful Thrust** (2 SP) → Declare attack for 4 damage, Range: Melee
 - **To-Hit Calculation**: Base 5+ | Moved 2 hexes +1 | Front arc +0 = **Need 6+**
 - **Attack Roll**: (3) + (4) = **7 total** → **STRONG HIT** (+1 damage)
 - Final damage: 4 base + 1 (Strong Hit) = **5 damage**
4. Player B rolls **5 Defense Dice**: 
 - **1 Shield block** → Reduce to 4 damage
 - **1 Critical ()** → +1 Component Damage to Right Arm
 - **1 Heat ()** → +1 Heat
5. Player B discards 4 cards (chooses: 2 from hand, 2 from deck)
 - Discarded from hand: 1× Primary Weapon card → +1 Component Damage
 - **Total Component Damage to Right Arm: 2** (1 from , 1 from Primary card)
6. Player A has 3 SP remaining → Passes
7. Draw Phase: Draw 2 cards (hand back to 6)

**Player B Turn** (Ironclad):
1. Refresh to 4 SP, currently at 1 Heat (safe)
2. Play **Advance** (2 SP) → Move 2 hexes toward enemy
3. Play **Hammer Strike** (3 SP) → Declare attack for 6 damage, ignore 1 Armor
 - **To-Hit Calculation**: Base 5+ | Moved 2 hexes +1 | Attacking front +0 = **Need 6+**
 - **Attack Roll**: (5) + (3) = **8 total** → **STRONG HIT** (+1 damage)
 - Final damage: 6 base + 1 (Strong Hit) = **7 damage**
4. Player A rolls **7 Defense Dice**: 
 - **1 Shield block** → Reduce to 6 damage
 - **2 Critical ()** → +2 Component Damage to Right Arm
 - **1 Heat ()** → +1 Heat
 - **1 Pierce ()** → Cannot use reactive defense cards
5. Player A discards 6 cards (chooses: 3 from hand, 3 from deck)
 - Discarded from hand: 2× Primary Weapon (Penitent Blades) → +2 Component Damage
 - **Total Component Damage to Right Arm**: 2 (from ) + 2 (from Primary cards) = **4 Component Damage**
 - Right Arm has **REACHED 4 HP THRESHOLD** → **RIGHT ARM DESTROYED!**
 - Player A discards all remaining Penitent Blade cards from hand (cannot use Primary Weapon)
6. Player B has 0 SP → Turn ends
7. Draw Phase: Draw 3 cards

---

### Round 2

**Player A Turn**:
- Now has NO Primary Weapon cards in hand (all discarded)
- Must rely on Universal cards + Secondary Equipment (Buckler)
- Desperate situation → Might use **Blood Offering** (discard 2 cards for +3 damage boost)

---

This creates **brutal, desperate combat** where Component Damage matters and losing your Primary Weapon mid-fight is catastrophic.

---

**END OF DOCUMENT**

---

*"Your deck is your life. Every card you lose brings you closer to death. When your Primary Weapon cards are gone, you're just a broken puppet swinging fists in the dark."*
