# Component Damage System: AP/Structure/Pilot Exposure
## Penance: Absolution Through Steel

**Version**: 3.0 Comprehensive Rules (October 17, 2025)

---

## Overview: Three-Layer Defense

**Lore Context:** Caskets are mechanical armored frames powered by Soulstone energy. Pilots are living humans (usually desperate, dying, or half-dead volunteers) who have undergone soul-binding. The pilot is suspended in neural fluid inside a containment chamber (the capsule) within the Casket's chassis, arms crossed like a mummy. Ten neural threads pierce through their fingertips, connecting to the Casket's control nodes. The pilot manipulates the Casket like a puppeteer controlling a marionette—from inside. They are NOT autonomous machines - living pilots control every movement through the neural thread interface.

Caskets have **dual-layer HP tracking**:

1. **Casket HP Deck** (26-50 cards) - Overall structural integrity of the mechanical frame
2. **Component HP** (per limb) - Localized damage with **pilot chamber exposure risk**

**When you take damage:**
- **Discard cards** from deck/hand (Casket HP loss)
- **Equipment cards discarded** add Component Damage to targeted limb
- **Defense Dice CRITICAL symbols** add Component Damage (bypass AP)

**Each component has three defensive zones:**
- **AP Layer** (Armor Plating) - Absorbs early damage, no penalties
- **Structure Layer** - Functional penalties, component degrading
- **Pilot Exposure Zone** - **Every Component Damage = +1 Pilot Wound**

---

## Component HP Table (Master Reference)

| Component | Total HP | AP Zone | Structure Zone | Pilot Exposure Zone | Destroyed |
|-----------|----------|---------|----------------|---------------------|-----------|
| **Head** | 6 HP | 0-2 dmg | 3-4 dmg | 5-6 dmg | 6+ dmg |
| **Right Arm** | 8 HP | 0-3 dmg | 4-5 dmg | 6-8 dmg | 8+ dmg |
| **Left Arm** | 8 HP | 0-3 dmg | 4-5 dmg | 6-8 dmg | 8+ dmg |
| **Chassis** | 10 HP | 0-4 dmg | 5-6 dmg | 7-10 dmg | 10+ dmg |
| **Legs** | 8 HP | 0-3 dmg | 4-8 dmg | NEVER | 8+ dmg |

**Key Insight:** Legs have no pilot exposure (capsule is in chassis, above legs)

---

## How Component Damage Accumulates

### Sources of Component Damage

**1. Equipment Cards Discarded When Taking Damage**
- When you discard cards to absorb damage:
  - **Primary Weapon cards** → +1 Component Damage to targeted component
  - **Shield/Offhand cards** → +1 Component Damage if targeting Left Arm
  - **Accessory cards** → No Component Damage (utility equipment)

**2. Defense Dice CRITICAL Symbols (⚔️)**
- When rolling Defense Dice, each CRITICAL symbol:
  - **Bypasses AP layer entirely**
  - Adds +1 Component Damage directly to structure
  - Cannot be prevented (armor-piercing effect)

**3. Special Attack Effects**
- Some cards have "Armor-Piercing" or "Ignore AP" keywords
- These add Component Damage directly to structure layer

---

## Damage Flow Sequence (Step-by-Step)

### STEP 1: Attack Declared
- Attacker plays attack card
- **Declares target component** (choose one method):

**Method A: Attacker Chooses** (Tactical)
- Attacker selects which component to target
- **Recommended default** (gives attacker tactical control)
- Example: "I'm targeting your exposed Right Arm"

**Method B: Random Hit Location** (Chaotic)
- Roll **1d6** to determine hit location:
  - **1:** Head
  - **2:** Left Arm
  - **3:** Right Arm
  - **4-5:** Chassis (2 faces, most likely target)
  - **6:** Legs
- Use when attack card doesn't specify, or for "wild" attacks
- Creates unpredictability (might hit fresh armor or exposed component)

**Method C: Card Specifies** (Some cards have built-in targeting)
- Example: "Leg Sweep" (automatic Legs target)
- Example: "Headshot" (automatic Head target)
- Card text overrides player choice

- Rolls Attack Dice to hit

### STEP 2: Defender Response (If Hit)
**A. Play Reactive Card (Optional)**
- Defender may play [—] Initiative reactive card (0 SP)
- Shields reduce **total damage** (affects both Casket HP and Component Damage)
- Example: "Deflect" reduces 2 damage → 6 damage becomes 4 damage

**B. Roll Defense Dice**
- Roll **1d6 Defense Die per damage point** (after shields)
- Count symbols:
  - 🛡️ **SHIELD** / **ABSORB** → Block 1 damage each
  - ⚔️ **CRITICAL** → +1 Component Damage (bypasses AP)
  - 🔥 **HEAT** → +1 Heat to defender
  - 🗡️ **PIERCE** → Defender cannot use reactive cards (too late if already rolled)
  - 💔 **FLESH WOUND** → Take damage normally

### STEP 3: Apply Damage to Casket HP
- Final damage = Original damage - Shield blocks - Defense blocks
- Defender **discards cards** (from hand, deck, or mix)
- **Choice matters:**
  - Discard from **hand** → Control what's lost, but lose tactical options
  - Discard from **deck** → Random, might hit key cards, but preserve hand

### STEP 4: Calculate Component Damage
**Count all sources:**
1. **Equipment cards discarded** (Primary Weapon, Shield/Offhand)
2. **CRITICAL symbols** from Defense Dice

**Example:**
- Took 5 damage, discarded:
  - 2× Primary Weapon cards from hand
  - 1× Universal card from hand
  - 2× cards from deck (random)
- Defense Dice showed 1× CRITICAL
- **Component Damage = 2 (Primary Weapon cards) + 1 (CRITICAL) = 3 total**

### STEP 5: Apply Component Damage to Target
- Add Component Damage to targeted component's HP track
- Check which zone component is now in (AP / Structure / Pilot Exposure)
- Apply effects immediately

### STEP 6: Check for Pilot Wounds
**If component is in Pilot Exposure Zone:**
- **For each Component Damage that occurred in Pilot Exposure Zone:**
  - Pilot flips 1 Wound card

**Example:**
- Right Arm was at 5/8 HP (structure zone)
- Took 3 Component Damage → Now at 8/8 HP (destroyed)
- Damage progression: 5 → 6 (enters exposure) → 7 (still exposed) → 8 (destroyed)
- **Pilot Wounds:**
  - 5→6: +1 Wound (entered exposure)
  - 6→7: +1 Wound (still exposed)
  - 7→8: +1 Wound (destruction)
  - **Total: 3 Pilot Wounds from this attack**

---

## Component Zones and Effects

### HEAD (6 HP Total)

**Zone 1: AP Layer (0-2 damage)**
- Armor absorbing hits
- Sensors rattling but operational
- **No penalties**

**Zone 2: Structure (3-4 damage)**
- Sensor array damaged
- Targeting systems glitching
- **Effects:**
  - **-1 to all ranged attacks**
  - Cannot use "Sensor Sweep" cards
  - **+1 Heat per turn** (cooling system damaged)

**Zone 3: PILOT EXPOSURE (5-6 damage)**
- Head armor shattered
- Containment chamber breached near pilot's bound position
- **Effects:**
  - All Zone 2 penalties continue
  - **+1 Pilot Wound per Component Damage taken**
  - Soul-bound pilot's essence vulnerable to physical trauma

**Destroyed (6+ damage):**
- Head severed or crushed
- **Final effect:** +1 Pilot Wound (destruction wound)
- **-2 to all ranged attacks** (blind firing)
- Cannot use any targeting or sensor cards
- **+2 Heat per turn** (no cooling)

---

### RIGHT ARM (8 HP Total)

**Zone 1: AP Layer (0-3 damage)**
- Armor plating cracked
- Weapon mount stable
- **No penalties**

**Zone 2: Structure (4-5 damage)**
- Hydraulics leaking
- Weapon mount destabilized
- **Effects:**
  - **-1 damage** to all attacks using Primary Weapon
  - **+1 Heat** when playing Primary Weapon cards (strain)

**Zone 3: PILOT EXPOSURE (6-8 damage)**
- Arm frame shattered
- Shrapnel penetrating capsule wall
- **Effects:**
  - **-2 damage** to all Primary Weapon attacks
  - **+1 Pilot Wound per Component Damage taken**
  - **+1 Heat** per Primary Weapon card played

**Destroyed (8+ damage):**
- Arm severed at shoulder joint
- **Final effect:** +1 Pilot Wound (destruction wound)
- **All Primary Weapon cards → SCRAP**
- Cannot play Primary Weapon cards (original effects)
- Can only use Secondary Equipment + Universal cards

---

### LEFT ARM (8 HP Total)

**Zone 1: AP Layer (0-3 damage)**
- Shield/Offhand mount intact
- **No penalties**

**Zone 2: Structure (4-5 damage)**
- Mounting bracket bent
- Secondary systems failing
- **Effects:**
  - **Shield reactive cards block -1 less damage** (Deflect blocks 1 instead of 2)
  - Offhand weapons: **-1 damage**

**Zone 3: PILOT EXPOSURE (6-8 damage)**
- Arm collapsed
- Neural feedback from destroyed mount
- **Effects:**
  - **Shield reactive cards block -2 less damage** (many become useless)
  - **+1 Pilot Wound per Component Damage taken**
  - Offhand weapons: **-2 damage**

**Destroyed (8+ damage):**
- Arm destroyed
- **Final effect:** +1 Pilot Wound (destruction wound)
- **All Shield/Offhand cards → SCRAP**
- Cannot use shields or offhand equipment
- Must rely on Primary Weapon only

---

### CHASSIS (10 HP Total) - MOST CRITICAL

**Zone 1: AP Layer (0-4 damage)**
- External armor absorbing
- Core structure intact
- **No penalties**

**Zone 2: Structure (5-6 damage)**
- Frame buckling
- Core systems stressed
- **Effects:**
  - **-1 SP maximum** (5 SP → 4 SP)
  - Movement costs **+1 SP per 3 hexes** (heavy frame)

**Zone 3: PILOT EXPOSURE (7-10 damage) - CRITICAL**
- **CONTAINMENT CHAMBER BREACHED**
- Soul-bound pilot's capsule directly exposed to combat
- **Effects:**
  - **-2 SP maximum** (5 SP → 3 SP) - neural thread damage
  - Movement costs **+1 SP per 2 hexes** - frame integrity failing
  - **+1 Pilot Wound per Component Damage taken**
  - **+1 Heat per turn** (Soulstone containment breach)

**Destroyed (10+ damage):**
- Catastrophic structural failure
- Casket collapsing around pilot
- **Final effect: +3 Pilot Wounds immediately** (life-threatening)
  - Pilot rolls save (1d6):
    - 1-2: **Ejection failure** (pilot trapped, +2 additional Wounds = likely death)
    - 3-4: **Emergency ejection** (pilot survives but severely wounded)
    - 5-6: **Clean ejection** (pilot survives, no additional Wounds)
- **Casket is INERT** (cannot move or act)
- In campaign: Casket is salvage wreck
- In arena: **Match loss**

---

### LEGS (8 HP Total) - NO PILOT EXPOSURE

**Zone 1: AP Layer (0-3 damage)**
- Leg armor holding
- Hydraulics operational
- **No penalties**

**Zone 2: Structure (4-8 damage)**
- Locomotion systems damaged
- Redundant actuators failing
- **Effects by damage level:**
  - **4-5 damage:** Movement costs **+1 SP per hex** (limping)
  - **6-7 damage:** Movement costs **+2 SP per hex** (dragging leg)
  - **8 damage (destroyed):** Movement costs **+3 SP per hex**, max 2 hexes per turn (crawling)

**Zone 3: PILOT EXPOSURE**
- **LEGS HAVE NO PILOT EXPOSURE ZONE**
- Containment chamber is located in chassis, above leg systems
- Legs can be completely destroyed without breaching the pilot's chamber

**Destroyed (8+ damage):**
- Legs severed or immobilized
- **No pilot wound from destruction** (pilot not adjacent)
- Movement **+3 SP per hex**, maximum 2 hexes per turn
- Cannot sprint or use movement-enhancing cards
- Effectively immobile in combat

---

## Pilot Wound System Integration

### When Pilot Takes Wounds

**Pilot has separate 10-card Wound Deck:**
- 5× Minor Injury (temporary debuffs)
- 3× Severe Injury (PERMANENT effects)
- 2× Trauma (mental breakdown)

**Sources of Pilot Wounds:**

1. **Component Pilot Exposure** (NEW PRIMARY SOURCE)
   - Any Component Damage while in Pilot Exposure Zone → +1 Wound
   - Can take 2-3 Wounds in single attack if component destroyed from exposure zone

2. **Chassis Destruction** (CRITICAL)
   - Chassis destroyed → +3 Wounds immediately
   - Then roll ejection save (may add +2 more Wounds)

3. **Head Destruction**
   - Head destroyed → +1 Wound (neural feedback)

4. **Neural Feedback** (Cumulative Strain)
   - When **total Component Damage across ALL components reaches 5+** → +1 Wound (triggers once per threshold)
   - Check at end of each attack that adds Component Damage
   - **Clarification**: This triggers once when you first reach 5 total Component Damage, then again at 10, 15, etc.

5. **Casket HP Deck Empty**
   - Deck + Discard both empty → Pilot rolls save (1d6)
   - 1-3: +2 Wounds (structural collapse)
   - 4-6: Survives extraction (0 Wounds)

**10 Wounds Flipped = PILOT DEATH**

---

## SCRAP Card System (Destroyed Component Cards)

### When Component is Destroyed

**All equipment cards associated with that component become "SCRAP":**
- Primary Weapon cards (if Right Arm destroyed)
- Shield/Offhand cards (if Left Arm destroyed)
- Cards **remain in deck** but lose original function

### SCRAP Card Universal Rules

**SCRAP cards have new universal effect (ignore printed text):**

```
┌──────────────────────────────┐
│   [DAMAGED EQUIPMENT]        │
│                              │
│  This component is destroyed.│
│  You cannot use its printed  │
│  effect.                     │
│                              │
│  SCRAP VALUE:                │
│                              │
│  • Still counts as card for  │
│    Casket HP (can be         │
│    discarded to absorb dmg)  │
│                              │
│  • Can discard to pay for    │
│    overspending SP           │
│                              │
│  • Play this card (0 SP):    │
│    CANNIBALIZE               │
│    Discard this card,        │
│    draw 1 card.              │
│                              │
│  "Scrap is still useful in   │
│   desperate times."          │
└──────────────────────────────┘
```

### Cannibalize Action (0 SP)

**Play SCRAP card as action during your turn:**
- **Cost:** 0 SP (free action)
- **Effect:** Discard this SCRAP card → Draw 1 card immediately
- **Limit:** Can play as many SCRAP cards per turn as you have
- **Timing:** During Action Phase (not reactive)

**Strategic Uses:**
- **Cycle dead draws:** Convert 3 SCRAP cards → Draw 3 fresh cards (0 SP total)
- **Dig for key cards:** Cycle SCRAP until you find the card you need
- **Avoid hand clog:** Don't waste turns with 4 SCRAP + 2 useful cards

**Example Turn with SCRAP:**
```
Church Confessor, Right Arm destroyed (12 Primary Weapon cards = SCRAP)

Hand: [SCRAP] [SCRAP] [SCRAP] [Desperate Lunge] [Brace for Impact] [Emergency Vent]

Action Phase:
1. Play SCRAP card (0 SP) → Cannibalize → Draw 1 (get "Rally Cry")
2. Play SCRAP card (0 SP) → Cannibalize → Draw 1 (get "Feint")
3. Play SCRAP card (0 SP) → Cannibalize → Draw 1 (get another SCRAP, discard it)
4. Play "Feint" (1 SP) → +1 damage next attack
5. Move 2 hexes (2 SP)
6. Play "Bash" with Left Arm (1 SP) → Attack for 2 damage + 1 (Feint) = 3 damage

Total: Cycled 3 SCRAP cards for free, used 4 SP for actions
```

---

## Damage Mitigation Layers (In Order)

### Layer 1: Reactive Cards (Shields)
- Played **before** Defense Dice roll
- Reduces **total damage**
- Example: "Deflect" (-2 damage) → 7 damage becomes 5 damage

**Strategic Choice:**
- Use shield early (protect AP layer)?
- Save shield for pilot exposure zone?
- No shields in hand = Take full damage

### Layer 2: Defense Dice
- Roll **1d6 per damage point** (after reactive cards)
- SHIELD/ABSORB symbols → Block damage
- CRITICAL symbols → **Add Component Damage** (bypasses AP)

**Randomness Factor:**
- 8 damage attack → Defender rolls 8 dice
- Lucky roll: 4× SHIELD = Block 4 damage (only take 4)
- Unlucky roll: 3× CRITICAL = +3 Component Damage (bypasses AP, could enter exposure zone)

### Layer 3: Discard Choice (Casket HP)
- Defender chooses which cards to discard
- **From hand:** Control what's lost, but lose tactical options
- **From deck:** Random, but preserve hand

**Component Damage Impact:**
- Discarding **Primary Weapon cards** → +1 Component Damage each
- Discarding **Universal cards** → No Component Damage
- Strategic: "Do I sacrifice weapon cards to take Component Damage, or discard from deck randomly?"

### Layer 4: Component AP Layer
- First X damage to component absorbed by armor
- **No functional penalties** while in AP zone
- Once AP depleted → Structure damage begins

### Layer 5: Component Structure
- Functional penalties accumulate
- Component still operational but degraded
- **No pilot wounds yet** (pilot still protected by inner structure)

### Layer 6: Pilot Exposure Zone
- **Every Component Damage = +1 Pilot Wound**
- Pilot directly at risk
- Component near destruction

---

## Tactical Decision Points

### For Attacker: Target Selection

**Q: Which component to target?**

**Option A: Focus Fire (Destroy One Component)**
- Pros: Guaranteed to cripple one system, force SCRAP cards
- Cons: Other components still at full HP, pilot protected longer
- Example: Destroy Right Arm (8 hits) → Enemy loses all weapon attacks

**Option B: Spread Damage (Multiple Pilot Exposures)**
- Pros: Multiple components in exposure zones → Every future hit causes Pilot Wounds
- Cons: No components fully destroyed, enemy still has all tools
- Example: Get Head to 5/6, Right Arm to 6/8, Chassis to 7/10 → All exposed, every hit hurts pilot

**Option C: Snipe Weak Components**
- Pros: Head only 6 HP (easy to destroy), immediate impact
- Cons: Less pilot wound potential than Chassis, enemy can still fight
- Example: Destroy Head (6 hits) → Enemy blind, -2 ranged, +2 Heat/turn

**Option D: Chassis Rush (High Risk/Reward)**
- Pros: Chassis destruction = +3 Wounds immediately, possible instant death
- Cons: Chassis has 10 HP (highest), 4 AP (most armor), takes many turns
- Example: Pummel Chassis relentlessly → If destroyed, likely victory

### For Defender: Survival Choices

**Q: Discard from hand or deck?**

**Discard from Hand:**
- Pros: Control Component Damage (avoid discarding Primary Weapon cards)
- Cons: Lose tactical options, smaller hand = fewer plays next turn

**Discard from Deck:**
- Pros: Preserve hand (keep reactive shields, attack cards)
- Cons: Random, might discard Primary Weapon cards anyway → Component Damage

**Mixed Strategy:**
- Discard non-critical cards from hand first (Universal cards)
- Then discard from deck
- Save key cards (shields, finisher attacks)

**Q: Use shield now or save?**

**Use Shield Early (AP Zone):**
- Pros: Preserve armor, delay pilot exposure
- Cons: Waste shield when pilot not at risk

**Save Shield for Exposure Zone:**
- Pros: Protect pilot life when critical
- Cons: Might not survive to exposure zone without shields

### For Both: SP Economy Under Pressure

**Wounded pilots have reduced SP maximum:**
- 6 SP → 3 SP (after -3 from wounds)
- Can only afford small actions
- Must cannibalize SCRAP cards for cycling
- Cannot afford big attacks (5 SP) anymore

**Strategic Shift:**
- Early game: Big attacks (5 SP), mobility (3 hexes)
- Late game (wounded): Small attacks (2 SP), minimal movement (1 hex)
- Desperation: Overspend SP (pay with cards) for final push

---

## Example Combat: Full Match

### Setup
- **Church Confessor** (28-card deck, 6 SP, Light Casket)
- **Dwarven Ironclad** (36-card deck, 4 SP, Heavy Casket)
- Both pilots: 0/10 Wounds

---

### Turn 1: Opening Engagement

**Confessor Turn:**
- Moves 3 hexes forward (3 SP)
- Plays "Blood Offering" (0 SP, self-harm): Discard 2 cards → Gain "+3 damage next attack"
- Plays "Faithful Thrust" (2 SP): Attack Right Arm for 4 damage + 3 (buff) = 7 damage
- To-Hit: 5+ (base) +1 (moved 3 hexes) = Need 6+
- Rolls: (3)+(5) = 8 → **Strong Hit** (+1 damage) = 8 damage total
- Passes (1 SP remaining)

**Ironclad Response:**
- Plays reactive "Deflect" (-2 damage) → 8 damage becomes 6 damage
- Rolls 6 Defense Dice: 🛡️🛡️💔💔⚔️🔥
  - 2× SHIELD → Block 2 damage
  - 1× CRITICAL → +1 Component Damage
  - 1× HEAT → +1 Heat
- Final: 6 - 2 blocks = **4 damage to Casket HP**
- Discards: 2 from hand (both Universal) + 2 from deck (random: 1× Primary Weapon, 1× Universal)
- Component Damage: 1 (discarded Primary Weapon) + 1 (CRITICAL) = **2 Component Damage to Right Arm**

**Ironclad Status:**
- Casket HP: 36 → 32 cards
- Right Arm: **2/8 HP** (AP zone, no penalties)
- Heat: 1

---

**Ironclad Turn:**
- Moves 2 hexes (2 SP)
- Plays "Hammer Strike" (3 SP, Armor-Piercing): Attack Confessor's Chassis for 6 damage
- Rolls hit for 6 damage
- Passes (0 SP remaining, turn ends)

**Confessor Response:**
- No reactive cards in hand
- Rolls 6 Defense Dice: 💔💔💔🛡️⚔️⚔️
  - 1× SHIELD → Block 1 damage
  - 2× CRITICAL → +2 Component Damage (bypass AP!)
- Final: 6 - 1 = **5 damage to Casket HP**
- Discards: 3 from hand (2× Primary Weapon, 1× Universal) + 2 from deck
- Component Damage: 2 (Primary Weapon cards) + 2 (CRITICALS) = **4 Component Damage to Chassis**

**Confessor Status:**
- Casket HP: 28 → 23 cards
- Chassis: **4/10 HP** (AP zone edge, no penalties yet)

---

### Turn 3: Armor Depleted

**Confessor Status:**
- Chassis: 4/10 HP
- Right Arm: 0/8 HP (pristine)

**Confessor Turn:**
- Moves 2 hexes (2 SP)
- Plays "Righteous Cleave" (3 SP): Attack Ironclad's Right Arm for 5 damage
- Rolls hit
- Passes (1 SP)

**Ironclad Response:**
- Right Arm was at 2/8 HP
- No reactive shield
- Rolls 5 Defense Dice: 💔💔💔⚔️🔥
  - 1× CRITICAL → +1 Component Damage
  - 1× HEAT → +1 Heat
- Final: 5 damage (no blocks)
- Discards: 2 from hand (1× Primary Weapon) + 3 from deck (random: 1× Primary Weapon)
- Component Damage: 2 (Primary Weapon cards) + 1 (CRITICAL) = **+3 Component Damage**

**Ironclad Status:**
- Right Arm: 2 → **5/8 HP** (STRUCTURE ZONE)
- **Effect:** -1 damage to all Primary Weapon attacks, +1 Heat when using weapons
- Heat: 3 total
- Arm damaged but still functional

---

**Ironclad Turn:**
- Plays "Rune Strike" (4 SP): Attack Confessor's Chassis for 5 damage
- Hits for 5 damage
- Passes

**Confessor Response:**
- Chassis at 4/10 HP (AP zone)
- Plays reactive "Brace for Impact" (-2 damage) → 5 becomes 3 damage
- Rolls 3 Defense Dice: 💔⚔️🔥
  - 1× CRITICAL → +1 Component Damage
  - 1× HEAT → +1 Heat
- Final: 3 damage (no blocks)
- Discards: 1 from hand (Universal) + 2 from deck (random: 1× Primary Weapon)
- Component Damage: 1 (Primary Weapon) + 1 (CRITICAL) = **+2 Component Damage**

**Confessor Status:**
- Chassis: 4 → **6/10 HP** (STRUCTURE ZONE)
- **Effect:** -1 SP maximum (6 → 5 SP), movement +1 SP per 3 hexes
- SP now limited, mobility hindered

---

### Turn 5: First Pilot Exposure

**Ironclad Status:**
- Right Arm: 5/8 HP (structure damaged)
- Casket HP: 27/36 cards

**Confessor Status:**
- Chassis: 6/10 HP (structure damaged)
- SP: 5 (reduced from 6)
- Casket HP: 18/28 cards

**Confessor Turn:**
- Moves 2 hexes (2 SP)
- Plays "Divine Judgment" (4 SP): Attack Ironclad's Right Arm for 8 damage (target has low HP)
- Rolls hit
- Passes (0 SP, turn ends, discarded to 0)

**Ironclad Response:**
- Right Arm at 5/8 HP
- Plays reactive "Wall of Iron" (Tower Shield, -3 damage, +1 Heat) → 8 becomes 5 damage
- Rolls 5 Defense Dice: 🛡️💔⚔️⚔️💔
  - 1× SHIELD → Block 1 damage
  - 2× CRITICAL → +2 Component Damage
- Final: 5 - 1 = **4 damage to Casket HP**
- Discards: 3 from hand (2× Primary Weapon) + 1 from deck (Universal)
- Component Damage: 2 (Primary Weapon) + 2 (CRITICALS) = **+4 Component Damage**

**Right Arm progression:**
- 5 → 6 (enter exposure) → 7 → 8 → **9/8 HP (DESTROYED + overage)**

**Damage breakdown:**
- 5 → 6: Enters Pilot Exposure Zone → **+1 Pilot Wound**
- 6 → 7: Still in exposure → **+1 Pilot Wound**
- 7 → 8: Component destroyed → **+1 Pilot Wound**
- 8 → 9: Overage (component already destroyed, no additional wound)

**Ironclad Status:**
- Right Arm: **DESTROYED**
- All Primary Weapon cards (Warhammer, Hammer Strike, Rune Strike) → **SCRAP**
- **Pilot: 3/10 Wounds**
- Wounds flipped:
  1. **Minor Injury - Concussion:** -1 SP max (4 → 3 SP)
  2. **Minor Injury - Broken Finger:** -1 to attacks this mission
  3. **Severe Injury - Shattered Hand:** -2 SP max PERMANENT (3 → 1 SP total!)

**Ironclad crippled:** Only 1 SP per turn now!

---

**Ironclad Turn:**
- **SP: 1 (was 4, now 1 after wounds)**
- Hand: [SCRAP] [SCRAP] [SCRAP] [Advance] [Emergency Vent] [Survey Field]
- Plays SCRAP card (0 SP) → Cannibalize → Draw (gets "Bash")
- Plays SCRAP card (0 SP) → Cannibalize → Draw (gets another SCRAP)
- Plays "Bash" with Left Arm (1 SP): Attack for 2 damage, push 1 hex
- Rolls hit for 2 damage
- Passes (0 SP)

**Confessor Response:**
- Rolls 2 Defense Dice: 💔🛡️
  - 1× SHIELD → Block 1 damage
- Final: 1 damage
- Discards 1 from deck (Universal)
- No Component Damage (no equipment cards discarded)

---

### Turn 7: Death Spiral

**Ironclad Status:**
- Right Arm: DESTROYED (SCRAP cards)
- Pilot: 3/10 Wounds, 1 SP per turn
- Casket HP: 20/36 cards
- Cannot mount effective offense

**Confessor Status:**
- Chassis: 6/10 HP (structure damaged)
- Pilot: 0/10 Wounds (unharmed)
- Casket HP: 15/28 cards
- Full offensive capability

**Confessor Turn:**
- Targets Ironclad's exposed Chassis (4/10 HP)
- Plays "Righteous Cleave" (3 SP): 5 damage to Chassis
- Hits

**Ironclad Response:**
- Chassis at 4/10 HP (AP zone)
- No reactive shields in hand (all SCRAP)
- Rolls 5 Defense Dice: 💔💔💔⚔️⚔️
  - 2× CRITICAL → +2 Component Damage (bypass AP!)
- Final: 5 damage (no blocks)
- Discards: 2 from hand (Universal) + 3 from deck (random: 1× Shield card)
- Component Damage: 1 (Shield card) + 2 (CRITICALS) = **+3 Component Damage**

**Chassis: 4 → 7/10 HP (PILOT EXPOSURE!)**

**Effects:**
- Entered Pilot Exposure Zone → **+1 Pilot Wound**
- Chassis exposure: -2 SP max (1 → -1 SP, minimum 1 SP)
- +1 Heat per turn

**Ironclad Pilot: 4/10 Wounds**

---

**Ironclad Turn:**
- SP: 1
- Cannot attack effectively
- Plays "Emergency Vent" (2 SP) → **Overspends by 1 SP** (discard 1 card to pay)
- Removes 3 Heat
- Turn ends

**Ironclad is effectively defeated:**
- Cannot attack (no weapons, 1 SP)
- Chassis exposed (every hit = Pilot Wound)
- 6 Wounds away from death
- Confessor can kill in 2-3 more turns

---

### Turn 9: Finishing Blow

**Confessor targets exposed Chassis again:**
- "Divine Judgment" (4 SP): 8 damage to Chassis (target low HP)
- Hits for 8 damage

**Ironclad Response:**
- Chassis at 7/10 HP (pilot exposed)
- Rolls 8 Defense Dice: 🛡️💔💔💔⚔️⚔️💔🔥
  - 1× SHIELD → Block 1 damage
  - 2× CRITICAL → +2 Component Damage
  - 1× HEAT → +1 Heat
- Final: 8 - 1 = **7 damage to Casket HP**
- Discards: 4 from hand + 3 from deck (random: 2× Shield cards)
- Component Damage: 2 (Shield cards) + 2 (CRITICALS) = **+4 Component Damage**

**Chassis progression:**
- 7 → 8 → 9 → 10 → **11/10 (DESTROYED + overage)**

**Pilot Wounds:**
- 7 → 8: **+1 Wound** (5 total)
- 8 → 9: **+1 Wound** (6 total)
- 9 → 10: **+1 Wound** (7 total)
- Chassis destroyed: **+3 Wounds immediately** (10 total)

**IRONCLAD PILOT: 10/10 WOUNDS = DEATH**

**Ejection Save:** Roll 1d6 = **2 (FAILURE)**
- Pilot trapped in collapsing Casket
- +2 additional Wounds (would be 12, but capped at 10)
- **Pilot dies instantly**

**Match Over: Confessor Victory**

---

## Component Destruction Summary Table

| Component | HP | AP | Exposure | Destroyed Effect | Pilot Wound |
|-----------|----|----|----------|------------------|-------------|
| Head | 6 | 0-2 | 5-6 | -2 ranged, blind, +2 Heat/turn | +1 |
| Right Arm | 8 | 0-3 | 6-8 | All Primary Weapon → SCRAP, -3 damage | +1 |
| Left Arm | 8 | 0-3 | 6-8 | All Shield/Offhand → SCRAP | +1 |
| Chassis | 10 | 0-4 | 7-10 | **+3 Wounds**, ejection save, likely death | +3 |
| Legs | 8 | 0-3 | Never | Immobile (+3 SP/hex, max 2 hexes) | 0 |

---

## Quick Reference: Damage Math

**Taking 6 damage to Right Arm (currently at 4/8 HP):**

1. **Reactive card?** → Play "Deflect" (-2 damage) = 4 damage final
2. **Roll 4 Defense Dice:** 🛡️💔⚔️💔
   - 1× SHIELD = -1 damage = **3 damage to Casket HP**
   - 1× CRITICAL = +1 Component Damage
3. **Discard 3 cards:** 1× Primary Weapon from hand, 2× from deck (1× Primary Weapon)
   - Component Damage = 2 (cards) + 1 (CRITICAL) = **+3 total**
4. **Right Arm: 4 → 7/8 HP**
   - 4 (AP zone) → 5 (structure, -1 dmg) → 6 (exposure, +1 Wound) → 7 (exposure, +1 Wound)
   - **Total: +2 Pilot Wounds this attack**

**Final state:**
- Casket HP: -3 cards
- Right Arm: 7/8 HP (pilot exposed, -2 damage)
- Pilot: +2 Wounds
- 1 hit away from Right Arm destruction

---

## Edge Cases and Clarifications

### Q: What if I take 10 Component Damage to a 6 HP component?
**A:** Component destroyed at 6 HP. Excess damage is wasted (doesn't transfer to other components).

**Example:**
- Head at 3/6 HP, takes 8 Component Damage
- 3 → 4 → 5 (enter exposure, +1 Wound) → 6 (destroyed, +1 Wound) → 7-10 (excess, no effect)
- Total: +2 Pilot Wounds, Head destroyed

---

### Q: Can I target a destroyed component?
**A:** Yes, but pointless.
- Component already destroyed, no equipment cards left to discard
- Defense Dice CRITICALS would add Component Damage, but component already destroyed
- No additional Pilot Wounds (component already destroyed means past exposure zone)

---

### Q: If my Right Arm is destroyed, do I still take Component Damage when discarding SCRAP Primary Weapon cards?
**A:** No.
- SCRAP cards are generic (not equipment type anymore)
- Discarding SCRAP does not add Component Damage
- SCRAP cards only count as Casket HP (body mass)

---

### Q: Can I voluntarily discard Primary Weapon cards to avoid Component Damage?
**A:** No.
- You must discard from hand or deck (your choice of source)
- If you discard from deck, it's random (can't cherry-pick)
- If you discard Primary Weapon cards from hand, you take Component Damage (no choice)

**Strategic workaround:** Discard all non-Primary cards from hand first, then discard from deck

---

### Q: What if I have no cards in hand and deck is empty?
**A:** Casket defeated.
- Cannot absorb damage
- Casket structural failure
- Pilot rolls ejection save (see Chassis destruction rules)

---

### Q: Can shields block Component Damage?
**A:** Indirectly, yes.
- Shields reduce **total damage** (before Defense Dice)
- Less damage = fewer cards discarded = less Component Damage
- But Defense Dice CRITICALS still bypass shields and add Component Damage

---

### Q: If I'm in Pilot Exposure Zone, do I take Wounds for damage that doesn't add Component Damage?
**A:** No.
- Pilot Wounds only occur when **Component Damage is added while in Exposure Zone**
- If you discard 5 Universal cards (no Component Damage), no Pilot Wounds
- Only equipment cards discarded (Primary Weapon, Shield) add Component Damage

---

### Q: Can I target multiple components with one attack?
**A:** No (normally).
- Attacker declares 1 target component per attack
- Some special cards have "Cleave" (deal damage to multiple targets)
- For Cleave attacks, defender distributes damage and rolls Defense Dice per target separately

---

### Q: Does Neural Feedback (15+ total Component Damage) stack with Pilot Exposure Wounds?
**A:** Yes.
- If attack pushes total Component Damage from 14 to 17 (across all components):
  - Pilot Exposure Wounds apply per attack
  - Neural Feedback triggers once at 15+ threshold (+1 Wound)
  - Both sources apply

---

## Campaign Implications

### Destroyed Components Persist Between Missions

**In campaign mode:**
- Destroyed components require **repairs** at settlement
- Repairs cost **Scrap** (salvaged materials) and **time** (mission turns)
- SCRAP cards remain in deck until repaired

**Repair Costs:**
| Component | Scrap Cost | Time (Missions) |
|-----------|------------|-----------------|
| Head | 3 Scrap | 1 mission |
| Arm | 5 Scrap | 2 missions |
| Chassis | 10 Scrap | 3 missions |
| Legs | 6 Scrap | 2 missions |

**If not repaired:**
- Must deploy with SCRAP cards in deck
- Component still destroyed (functional penalties persist)
- Can cannibalize SCRAP for cycling, but deck bloated

---

### Pilot Wounds Persist Between Missions

**Minor Injuries (5 cards):**
- Last **1 mission** after flipped
- Removed during Settlement Phase recovery

**Severe Injuries (3 cards):**
- **PERMANENT** (campaign-long)
- Can only be healed with "Reconstructive Surgery" (rare, expensive)
- Pilot carries debuff for entire campaign

**Trauma (2 cards):**
- **PERMANENT** until psychological treatment
- Requires "Soul Cleansing" event or 5 missions rest

---

## Playtester Notes

**Tuning knobs for balance:**

1. **Component HP totals:** Increase if combats too fast, decrease if too slow
2. **AP layer thickness:** Increase AP = longer safe phase, decrease = faster exposure
3. **Pilot Exposure threshold:** Move earlier (lower HP) = more brutal, later = safer
4. **SCRAP Cannibalize cost:** Currently 0 SP (free), could charge 1 SP if too strong
5. **Pilot Wound deck size:** Currently 10 cards, increase to 12-15 if pilots die too fast

**Known power interactions:**
- Church "Blood Offering" self-harm → Risks Component Damage → Can self-expose pilot
- Dwarven "Rune Strike" Armor-Piercing → Bypasses AP, hits structure directly → Very strong against fresh components
- Ossuarium "Soul Harvest" → Recovers cards from discard → Can recover SCRAP cards and re-cannibalize

---

**END OF DOCUMENT**

*"Three layers: Armor, Structure, Flesh. When the third breaks, you pray the pilot survives."*

*"SCRAP is still useful. Even broken weapons have weight. Use them."*
