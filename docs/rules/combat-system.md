# Combat & Damage System (GKR + KDM Hybrid)
## Penance: Absolution Through Steel

**Version**: 2.0 (GKR-Style Redesign)
**Last Updated**: October 10, 2025

---

## Core Concept: Dual-Layer Damage

Inspired by **GKR: Heavy Hitters** (deck-as-HP) + **Kingdom Death: Monster** (brutal consequences)

**Two Separate Systems**:
1. **Casket HP Deck** (30 cards) - Your mech's structural integrity
2. **Pilot Wound Deck** (10 cards) - Your pilot's physical/mental state

When **Casket HP Deck runs out** → Casket is destroyed (pilot may survive)
When **Pilot Wound Deck runs out** → Pilot dies (Casket becomes inert)

---

## 1. Casket HP Deck (30 Cards)

### Deck Composition (GKR-Style)

Your 30-card deck represents your Casket's HP. Every card you discard = damage taken.

**Breakdown**:
- **10 Universal Cards** (mandatory, everyone has these)
- **12 Primary Weapon Cards** (faction-specific, your main identity)
- **6 Secondary Weapon/Equipment Cards** (customizable gear)
- **2 Faction Tactic Cards** (chosen from 5 available, pick 2 before battle)

**Total: 30 cards**

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

## 2. Damage Resolution (GKR-Style)

### When You Take Damage

**Step 1: Calculate Final Damage**
- Base damage from attack card
- Apply modifiers (facing, buffs, debuffs)
- Subtract Defense (if any)
- Minimum 1 damage

**Step 2: Discard Cards from HP Deck**
- Discard X cards from **top of your deck** (not from hand)
- X = final damage amount
- Example: Take 5 damage → discard top 5 cards of deck

**Step 3: Check for Critical Damage**
- If you discarded any **Primary Weapon cards**, you suffer **Component Damage**
- If you discarded **Universal Core cards**, no extra effect
- If you discarded **Secondary Equipment cards**, that equipment may malfunction

---

### Component Damage (KDM-Style Brutality)

When you discard **Primary Weapon cards** due to damage:

**Track Component Damage per Location**:
- Right Arm (Primary Weapon)
- Left Arm (Secondary Equipment)
- Legs (Movement)
- Head (Sensors)
- Chassis (Core)

**How it works**:
1. Attacker declares which component they're targeting (or random if not specified)
2. If damage causes you to discard cards from that component's type, mark Component Damage
3. **3 Component Damage to same location = Component Destroyed**

**Example**:
- Enemy attacks your Right Arm for 6 damage
- You discard top 6 cards from deck
- 2 of those cards are Primary Weapon cards (your arm weapons)
- Mark 2 Component Damage on Right Arm
- Next hit that discards 1+ Primary Weapon card → Right Arm destroyed

**Component Destroyed Effects**:
- **Right Arm**: Discard all Primary Weapon cards from hand, cannot use them
- **Left Arm**: Discard all Secondary Equipment cards from hand, cannot use them
- **Legs**: Movement costs +1 SP per hex
- **Head**: Cannot use Sensor Sweep, -1 to ranged attacks
- **Chassis**: Permanent -1 SP maximum

---

### Deck Depletion (Running Out of HP)

**When your deck runs out mid-turn**:
- Continue taking damage by discarding from **discard pile**
- If discard pile is empty, you're **Defeated**

**When you would draw a card but deck is empty**:
- **Reshuffle Trigger** (like GKR, but with KDM twist)
- Shuffle discard pile into new deck
- **Add 1 "Damage" card** to the deck (permanent degradation)
- Draw normally

**Damage Cards** (KDM-Style):
- Dead draws (do nothing when played)
- Dilute your deck over time
- Make it harder to draw useful cards
- After 3-4 reshuffles, deck is 30% Damage cards → death spiral

---

## 3. Pilot Wound Deck (10 Cards)

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

**Pilots take damage separately from Casket in these situations**:

1. **Capsule Breach** (enemy specifically targets capsule, rare)
2. **Neural Feedback** (when 5+ Component Damage accumulated)
3. **Thread Snap** (when Hand Threads break from damage)
4. **Taint Overload** (when Taint reaches 10)
5. **Casket Destruction** (when Casket HP deck runs out, pilot must save)

**When Pilot takes damage**:
- Flip 1 Wound Card face-up per damage
- Read effect immediately
- Card remains face-up (permanent)

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

## 4. SP Economy (Energy System)

### SP by Frame Type

Following GKR's energy economy, but adapted to Penance's weight classes:

| Casket Type | SP Maximum | Deck Size | Philosophy |
|-------------|------------|-----------|------------|
| **Light** | 6 SP | 30 cards | Speed & efficiency |
| **Medium** | 5 SP | 30 cards | Balanced |
| **Heavy** | 4 SP | 30 cards | Endurance |
| **Assault** | 3 SP | 30 cards | Power over finesse |

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

## 5. Card Draw & Hand Management

### Starting Hand: 6 Cards

**At start of battle**:
- Shuffle 30-card deck
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

## 6. Victory Conditions

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

## 7. Deck Construction Summary

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

## 8. Differences from Standard Deck-Builders

### Like GKR:
- ✅ Deck = HP (discard cards when damaged)
- ✅ Energy/SP refresh each turn
- ✅ Primary vs Secondary weapon split
- ✅ Deck is fixed 30 cards (no mid-game deck-building)
- ✅ Hand size fixed at 6

### Like KDM:
- ✅ Component damage tracking (arms, legs, head destroyed)
- ✅ Permanent injuries (Pilot Wound deck)
- ✅ Death spiral (Damage cards added to deck on reshuffle)
- ✅ Brutal consequences (losing Primary Weapon cards = component damage)

### Unique to Penance:
- 🔥 Heat system (risk/reward pushing into Danger Zone)
- 🧠 Pilot Wound deck (separate from Casket HP)
- 🩸 Neural Thread damage (pilot takes damage when components destroyed)
- ⚙️ Asymmetric factions (Primary Weapon cards completely different per faction)

---

## Example Combat Sequence

### Setup:
- **Player A**: Church Confessor (30 HP, 6 SP, 6 cards in hand)
- **Player B**: Dwarven Ironclad (30 HP, 4 SP, 6 cards in hand)

---

### Round 1

**Player A Turn** (Confessor):
1. Refresh to 6 SP
2. Play **Desperate Lunge** (1 SP) → Move 2 hexes toward enemy
3. Play **Faithful Thrust** (2 SP) → Attack for 4 damage, Range: Melee
   - Player B is in front arc → No facing bonus
4. Player B takes 4 damage → Discards top 4 cards from deck
   - Cards discarded: 2× Universal, 1× Primary, 1× Secondary
   - 1 Primary card discarded → Mark 1 Component Damage on targeted component (Right Arm)
5. Player A has 3 SP remaining → Passes
6. Draw Phase: Draw 2 cards (hand back to 6)

**Player B Turn** (Ironclad):
1. Refresh to 4 SP
2. Play **Advance** (2 SP) → Move 2 hexes, gain +1 Defense this turn
3. Play **Hammer Strike** (3 SP) → Attack for 6 damage, ignore 1 Armor
   - Player A has no armor, takes full 6 damage
4. Player A discards top 6 cards
   - Cards: 3× Primary (Penitent Blades), 2× Universal, 1× Tactic
   - 3 Primary cards discarded → 3 Component Damage on Right Arm
   - **Right Arm Destroyed!** (3 Component Damage threshold)
   - Player A discards all Penitent Blade cards from hand (cannot use Primary Weapon)
5. Player B has 0 SP → Turn ends
6. Draw Phase: Draw 3 cards

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
