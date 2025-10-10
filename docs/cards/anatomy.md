# Card Anatomy Reference
## Penance: Absolution Through Steel

**Version**: 0.1
**Last Updated**: October 8, 2025

---

## Card Template Structure

Every card in Penance follows this standard layout:

```
╔═══════════════════════════════════════╗
║  [Icon] CARD TITLE            [Init] ║  <- Title + Initiative Number
╠═══════════════════════════════════════╣
║  Type: CARD TYPE (Slot)               ║  <- Card Type + Equipment Slot
║  SP Cost: X  |  Range: RANGE          ║  <- Soul-Point Cost + Range
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  Mechanical description of what       ║  <- Rules Text
║  this card does when played.          ║
║                                       ║
║  Additional effects or conditions.    ║
╠═══════════════════════════════════════╣
║  Heat: +X  |  Keywords: Tag, Tag      ║  <- Heat Generation + Keywords
╠═══════════════════════════════════════╣
║  "Flavor text goes here."             ║  <- Atmospheric Quote
╚═══════════════════════════════════════╝
```

---

## Card Information Fields

### 1. Title & Icon
- **Icon**: Visual symbol (⚔ weapon, 🛡 defense, ⚡ movement, 🔥 spell, 💔 damage)
- **Title**: Evocative fantasy name (e.g., "Faithful Thrust", "Soulfire Lance", "Desperate Lunge")

### 2. Initiative Number [X]
- **Range**: 0-10 (lower = faster)
- **0-2**: Lightning fast (scout abilities, quick strikes)
- **3-5**: Standard speed (most actions)
- **6-8**: Slow/deliberate (heavy weapons, defensive actions)
- **9-10**: Very slow (siege weapons, massive attacks)
- **[—]**: No initiative (reactive/passive cards)

### 3. Card Type
**Primary Types**:
- **WEAPON** - Attack cards from equipped weapons
- **SPELL** - Magic from Source Conduit arms
- **UNIVERSAL** - Base cards every deck has
- **DAMAGE** - Injury cards added when taking damage
- **RELIC** - Special equipment effects

**Slot Designation**:
- (Right Arm), (Left Arm), (Relic Slot), (Action), (Chassis), etc.

### 4. SP Cost
- Soul-Points required to play this card
- Range: 0-4 SP typically
- Pushes you into Danger Zone if over Safe Zone limit

### 5. Range
**Range Categories**:
- **Self**: Only affects your Casket
- **Melee**: Adjacent hex only
- **Close**: 2-3 hexes
- **Medium**: 4-6 hexes
- **Long**: 7+ hexes
- **AOE**: Area of effect (multiple hexes)

### 6. Effect Text
- Clear mechanical description
- Damage values, movement, conditions
- "If/Then" statements for conditional effects
- Keywords referenced here

### 7. Heat Generation
- **Heat: 0** - No heat
- **Heat: +1/+2/+3** - Generates heat when played
- **Heat: -X** - Removes heat (cooling effects)

### 8. Keywords
**Common Keywords**:
- **Universal** - Base card, always in deck
- **Tainted** - Requires 3+ Taint to use
- **Forbidden** - Requires 7+ Taint to use
- **Corruption** - Causes Taint gain
- **Relic** - Ancient technology
- **Tech** - Requires ammunition/charges
- **Fire/Ice/Void** - Spell school tags
- **Blade/Hammer/Bow** - Weapon type tags
- **Injury** - Damage card
- **Reactive** - Play in response to enemy action

### 9. Flavor Text
- Italicized quote
- Atmospheric lore
- Character voice or world-building
- 1-2 short sentences

---

## Card Types in Detail

### WEAPON Cards

Equipment weapons add 3-5 cards to your deck. Each weapon has a unique set.

**Example: Longsword "Faithkeeper"**
```
╔═══════════════════════════════════════╗
║  ⚔ FAITHFUL THRUST              [3]   ║
╠═══════════════════════════════════════╣
║  Type: WEAPON (Right Arm)             ║
║  SP Cost: 2  |  Range: Melee          ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  Deal 4 damage to adjacent enemy.     ║
║                                       ║
║  If attacking from rear: +2 damage.   ║
╠═══════════════════════════════════════╣
║  Heat: 0  |  Keywords: Blade, Holy    ║
╠═══════════════════════════════════════╣
║  "Steel guided by conviction."        ║
╚═══════════════════════════════════════╝
```

### UNIVERSAL Cards

Every deck contains 10 universal cards regardless of equipment.

**Example: Movement**
```
╔═══════════════════════════════════════╗
║  ⚡ DESPERATE LUNGE              [1]   ║
╠═══════════════════════════════════════╣
║  Type: UNIVERSAL (Action)             ║
║  SP Cost: 1  |  Range: Self           ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  Move up to 2 hexes in any direction. ║
║  You may rotate once during movement. ║
║                                       ║
║  Generate 1 Heat.                     ║
╠═══════════════════════════════════════╣
║  Heat: +1  |  Keywords: Universal     ║
╠═══════════════════════════════════════╣
║  "Desperation grants wings."          ║
╚═══════════════════════════════════════╝
```

### SPELL Cards

Source Conduit arms grant 5 spell cards from a chosen school.

**Example: Fire School**
```
╔═══════════════════════════════════════╗
║  🔥 SOULFIRE LANCE              [4]   ║
╠═══════════════════════════════════════╣
║  Type: SPELL (Source Conduit)         ║
║  SP Cost: 2  |  Range: Medium         ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  Deal 3 damage to target.             ║
║                                       ║
║  Ignite: Target gains 1 Heat token.   ║
╠═══════════════════════════════════════╣
║  Heat: 0  |  Keywords: Fire, Tainted  ║
╠═══════════════════════════════════════╣
║  "The stone remembers burning."       ║
╚═══════════════════════════════════════╝
```

### DAMAGE Cards

Added to deck when injured. Cannot be played, clog your hand/deck.

**Example: Injury**
```
╔═══════════════════════════════════════╗
║  💔 CRACKED SOULVEINS           [—]   ║
╠═══════════════════════════════════════╣
║  Type: DAMAGE (Chassis)               ║
║  Cannot be played                     ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  This card clogs your deck.           ║
║                                       ║
║  All SP costs increased by 1.         ║
╠═══════════════════════════════════════╣
║  Keywords: Injury, Critical           ║
╠═══════════════════════════════════════╣
║  "The stone bleeds its light."        ║
╚═══════════════════════════════════════╝
```

### RELIC Cards

Rare technology with limited uses (ammo/charge tokens).

**Example: Ancient Tech**
```
╔═══════════════════════════════════════╗
║  🔫 THUNDERSPEAKER'S ROAR       [4]   ║
╠═══════════════════════════════════════╣
║  Type: RELIC WEAPON (Right Arm)       ║
║  SP Cost: 2  |  Range: Long           ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  Spend 1 Ammo token: Deal 5 damage.   ║
║                                       ║
║  If no Ammo: This card cannot be      ║
║  played.                              ║
╠═══════════════════════════════════════╣
║  Heat: 0  |  Keywords: Relic, Tech    ║
╠═══════════════════════════════════════╣
║  "Thunder from the old world."        ║
╚═══════════════════════════════════════╝
```

---

## Deck-as-Health System

Your deck represents your Casket's operational capacity.

### Taking Damage
When you take damage, you must discard cards equal to damage taken:
- **Option A**: Discard from hand (lose tactical options)
- **Option B**: Mill from top of deck (preserve hand, but closer to reshuffle)
- **Option C**: Mix of both

### Reshuffling
When your deck runs out:
1. Shuffle discard pile to form new deck
2. Add Damage cards based on injuries sustained
3. Deck becomes clogged with unplayable injury cards
4. Continue fighting

### Defeat Condition
When both deck AND hand are empty, your Casket is disabled.

---

## Player Mat Zones

**Essential Zones** (GKR-style layout):
- **Casket Profile** - Weight class, Safe Zone SP tracking
- **Heat Tracker** - Heat token storage
- **Taint Tracker** - Corruption level (0-10)
- **Draw Deck** - Face-down cards
- **Discard Pile** - Used/damaged cards
- **Hand** - Active cards (6 card default hand size)
- **Equipped Loadout** - Visual reference of current equipment
- **Ammo/Charge Tokens** - For relic tech weapons
- **Strain Dial** - Track current SP spent this turn

---

## Turn Structure

### 1. Planning Phase
All players secretly choose 1 card from hand and place face-down.

### 2. Reveal Phase
Flip cards simultaneously. Resolve in initiative order (lowest to highest).
- Ties = simultaneous resolution (both effects happen)

### 3. Resolution Phase
Execute card effects in initiative order:
- Movement
- Attacks
- Defensive actions
- Support abilities

### 4. Damage Resolution
When damaged, choose to discard from hand or mill from deck.

### 5. Draw Phase
Draw back up to hand size (6 cards default).
- If deck empty: Shuffle discard pile (add Damage cards)
- If deck AND hand empty: Casket disabled

### 6. End Phase
Remove temporary effects, reduce Heat (if applicable), check win conditions.

---

## Equipment Slot System

### Primary Slots (Everyone)
- **Right Arm** - Weapon, shield, or tool
- **Left Arm** - Weapon, shield, or tool

### Relic/Modification Slots (Class-dependent)
- **Scout**: 1 slot (focused, specialized builds)
- **Support**: 2 slots (balanced utility)
- **Heavy**: 3 slots (modular fortress)
- **Assault**: 3 slots (maximum firepower)
- **Aberrant**: 2 slots (unstable compatibility)

### Permanent Modifications
Some equipment replaces arm slots entirely and cannot be swapped:
- **Blade Arm** - Integrated melee weapon
- **Siege Cannon Arm** - Built-in heavy weapon
- **Source Conduit Arm** - Magic casting limb (+1 hand size)
- **Grappler Claw** - Grappling/throw specialist

---

## Hand Size Modifications

**Base Hand Size**: 6 cards

**Increases**:
- **Source Conduit Arm**: +1 (total 7)
- **Tome of Echoes** (Relic): +1 (total 7)
- **Twin Minds** (Aberrant Relic): +2, gain 1 Taint/turn (total 8)

**Decreases** (trade power for tactical options):
- **Berserker Implant** (Relic): -1 hand size, +1 damage on all attacks
- **Focused Targeting** (Relic): -1 hand size, ignore partial cover

---

## Naming Conventions

### Fantasy Naming Guidelines
Use evocative, atmospheric names that players want to say aloud.

**Patterns**:
- [Evocative Word] + [Action/Noun]
- "Faithful Thrust", "Earthshaker Smash", "Soulfire Lance"

**Avoid**:
- Generic terms: "Attack 1", "Move Card", "Damage Type B"
- Modern military jargon: "Tactical Strike", "Suppressive Fire" (unless relic tech)

**Embrace**:
- Medieval fantasy: "Godstrike", "Rending Arc", "Bulwark of Faith"
- Corrupted/dark themes: "Hungering Dark", "Voidtear", "Abyssal Touch"
- Natural imagery: "Swiftwing Arrow", "Thorngrasp", "Winter's Kiss"

---

## Next Steps

- [ ] Finalize 10 universal cards list
- [ ] Design damage card types (minor/major/critical injuries)
- [ ] Create equipment catalog (base weapons for each type)
- [ ] Develop racial unique card mechanics
- [ ] Create card template generator tool

---

*This document will evolve as playtesting reveals what works best.*
