# Quick Reference Sheet
## Penance: Absolution Through Steel

**Print this page for table reference** (8.5" × 11", 1 page front/back)

---

## TURN STRUCTURE

### 1. START OF TURN
- ☑ Draw 6 cards (or hand size limit)
- ☑ Refresh SP (5 SP for Warden, 6/4/3 for other classes)
- ☑ Trigger passive effects (Living Forge, etc.)
- ☑ Take environmental damage (lava, poison, etc.)
- ☑ Roll Strain if Heat ≥ 5

### 2. ACTION PHASE
- Play cards (cost SP)
- Move, attack, defend, use abilities
- Activate support units (independent)
- Spend until SP = 0 or choose to end turn

### 3. END OF TURN
- ☑ Discard entire hand (all cards → discard pile)
- ☑ Unspent SP lost (cannot bank)
- ☑ Remove expired buffs/debuffs
- ☑ Check for Heat reduction (safe zone 0-4)

---

## DAMAGE & HP

### The 3-Pile System
1. **HP Draw Deck** (26-50 cards) - Active deck
2. **Discard Pile** - Played cards → Reshuffles
3. **Damage Graveyard** - Damaged cards → Gone forever

### Taking Damage
- **Play a card** → Goes to **Discard Pile**
- **Take damage** → Cards go to **Damage Graveyard** (never returns)
- **Major Wound (5+ damage)** → Add 1 DAMAGED card to Discard Pile

### DAMAGED Cards (Persistent Curse)
- **Persist in hand** (not discarded at end of round)
- Take up 1 card slot (count toward 6-card hand limit)
- **0 SP Action to Remove (choose one):**
  - **Sacrifice** (to Discard Pile): Roll Damage Die, cycles back later
  - **Purge** (to Damage Graveyard): Roll Damage Die, gone forever
- **When discarded by damage:** Roll Damage Die (cascading failure)

**Damage Die (1d6):**
- 1: Gain 1 Heat | 2: -1 SP next turn | 3: Discard 1 card next turn
- 4: +1 Component Damage next hit | 5: +1 Pilot Wound | 6: Gain 1 SP!

### Reshuffling
- When HP Draw Deck empty: Reshuffle **Discard Pile** into new deck
- **Damage Graveyard stays separate** (permanent loss)
- DAMAGED cards from Discard Pile enter your deck

---

## SP ECONOMY

| Casket Class | SP per Turn | Weight | Speed |
|--------------|-------------|---------|-------|
| Scout (Light) | 6 | 700-900 lbs | Fast |
| **Warden (Medium)** | **5** | 1,100-1,300 lbs | **Balanced** |
| Vanguard (Heavy) | 4 | 1,600-1,800 lbs | Slow |
| Colossus (Assault) | 3 | 2,200-2,500 lbs | Immobile |

**Common SP Costs**:
- Move: 1 SP (4 hexes)
- Basic Attack: 2 SP (3-4 damage)
- Powerful Attack: 3-4 SP (5-7 damage)
- Ultimate Ability: 5 SP (game-changing)

---

## HEAT & STRAIN

### Heat Zones
- **Safe Zone (0-4 Heat)**: No penalties
- **Danger Zone (5+ Heat)**: Roll Strain at start of turn

### Strain Roll (1d6)
| Roll | Effect |
|------|--------|
| 1-2 | **Critical Failure**: Lose 2 SP + take 2 damage |
| 3-4 | **Failure**: Lose 1 SP or take 1 damage |
| 5-6 | **Success**: No penalty |

### Gaining Heat
- Powerful abilities (+1-2 Heat)
- Standing in lava (+1 Heat per turn)
- Overcharging weapons (+1 Heat)

### Removing Heat
- Vent abilities (-2-3 Heat)
- End turn in safe zone (0 Heat)
- Heat Sink equipment (passive -1)

---

## FACTION MECHANICS (Quick)

| Faction | Resource | How to Generate | How to Spend |
|---------|----------|-----------------|--------------|
| **Church** | Blood Offering stacks | Self-harm, discard cards | +1 damage per stack |
| **Dwarves** | Rune Counters | Standing still, defensive | Damage reduction, armor-piercing |
| **Elves** | Bleed stacks | Attacks hit, no removal | Infinite scaling damage |
| **Ossuarium** | Soul Harvest | Kill enemies | Heal, resurrect, thralls |
| **Crucible** | Forge Tokens | Stand in lava | Buffs, terrain, weapons |
| **Exchange** | Credits | Debt Collector, contracts | Hire mercenaries mid-battle |
| **Nomads** | Scrap Tokens | Salvage destroyed units | Craft equipment mid-battle |
| **Vestige** | Bloodline Forms | Metamorph, pack tactics | Transform, pack bonuses |
| **Emergent** | Metamorph Tokens | Molting, evolution | Transform forms (Assault/Tank/Scout/Support) |

---

## COMBAT RESOLUTION

### Attack Sequence
1. Declare attack (target + card)
2. Check range (melee = 1 hex, ranged = varies)
3. Calculate damage (base + buffs)
4. Target applies Defense (reduce damage)
5. Deal damage (discard cards from deck)
6. Check for Component Damage (3+ same type)

### Defense Formula
**Damage Dealt = Total Damage - Defense**
- Minimum damage: 1 (cannot reduce below 1)
- Defense buffs stack (Shield Wall +2, Guard Stance +1 = +3 total)

### Range
| Type | Range | Line of Sight |
|------|-------|---------------|
| Melee | 1 hex | Not required |
| Ranged (Short) | 1-4 hexes | Required |
| Ranged (Long) | 1-6 hexes | Required |
| Artillery | 4-8 hexes | Not required (indirect fire) |

---

## TERRAIN EFFECTS

| Terrain | Movement | Combat Effect | Special |
|---------|----------|---------------|---------|
| **Lava** | Normal | 2 dmg/turn standing | Crucible: +2 Forge tokens |
| **Ruins** | +1 SP | +1 DEF vs ranged | Cover |
| **Forest** | +1 SP | Elves: +1 DEF | Dense vegetation |
| **Water** | +1 SP | -1 to ranged attacks | Difficult footing |
| **Elevated** | Normal | +1 dmg ranged attacks | High ground |
| **Difficult** | +1 SP per hex | None | Rubble, mud |

---

## SUPPORT UNITS (Quick Reference)

### Activation
- Support units act independently (behavior deck AI)
- Do not cost your SP
- Draw 1 behavior card per turn, resolve effect

### Common Unit Stats
| Unit Type | HP | Movement | Defense | Role |
|-----------|-----|----------|---------|------|
| Scout | 6-10 | 6-8 | 0-1 | Recon, marking |
| Tank | 15-20 | 3-4 | 3-4 | Protection, taunt |
| Support | 8-12 | 4-5 | 1-2 | Buffs, healing |
| Assault | 10-15 | 5-6 | 1-2 | Damage, pressure |

### Support Unit Actions
- Move toward/away from threats
- Attack marked targets
- Buff allies within range
- Generate faction resources (Forge tokens, Blood stacks, etc.)

---

## HONOR DUELS (Crucible Only)

### Challenge
- Cost: 2 SP, range 6 hexes
- Target must accept or refuse

### If Accepted
- Only you and target attack each other (1 round)
- Allies/enemies ignored
- Kill target → gain 3 Forge tokens + recover 3 cards

### If Refused
- Target gains **Coward's Mark**
- All Crucible deal +2 damage to marked target (permanent)

---

## COMMON KEYWORDS

| Keyword | Meaning |
|---------|---------|
| **Armor-Piercing** | Ignore Defense buffs |
| **Bleed** | Damage over time (stacks infinitely) |
| **Reactive** | Play on opponent's turn (response) |
| **Passive** | Always active, no SP cost |
| **AoE** | Area of Effect (hits multiple targets) |
| **Taunt** | Forces enemies to attack this unit |
| **Flying** | Ignore terrain, move over enemies |
| **Mark** | Target takes +1 damage from faction |
| **Grappled** | Cannot move next turn |
| **Stunned** | Lose 2 SP next turn |

---

## UNIVERSAL CORE CARDS (All Decks)

| Card Name | Cost | Effect |
|-----------|------|--------|
| **Move** | 1 SP | Move up to 4 hexes |
| **Attack** | 2 SP | Deal 3 damage (melee) |
| **Defend** | 0 SP (Reactive) | Reduce damage by 2 |
| **Sprint** | 2 SP | Move up to 6 hexes, gain 1 Heat |
| **Overwatch** | 1 SP | Next attack +1 damage |
| **Brace** | 1 SP | +1 Defense until next turn |
| **Vent Heat** | 1 SP | Remove 2 Heat |
| **Draw Card** | 2 SP | Draw 1 additional card |
| **Recover** | 3 SP | Recover 3 cards from discard |
| **Desperate Strike** | 0 SP | Deal 2 damage, take 1 damage |

---

## DECK CONSTRUCTION

### Standard Deck (30 cards)
- **10 Universal Core** (always included)
- **6 Faction Cards** (choose 6 from 10 available)
- **12 Primary Weapon** (fixed, comes with Casket)
- **2 Tactics** (choose 2 from 5 available)

**Total**: 30 cards = 30 HP

### Equipment Expansion
- Add **Secondary Equipment** (6 cards): Shields, accessories, plating
- Add **Faction Tactics** (2 cards): Special abilities
- Add **Support Units** (behavior decks, independent)

**Max Deck Size**: ~40 cards (with full equipment)

**Total deck size varies**: Light ~26-32 cards, Medium ~30-38, Heavy ~35-45, Fortress ~38-50

---

## WINNING CONDITIONS

### Victory
- Reduce enemy Casket to **0 HP** (deck empty after reshuffles)
- Complete scenario objective (capture, survive, escort, etc.)
- Enemy surrenders (optional rule)

### Defeat
- Your deck reaches 0 cards (death)
- Fail scenario objective (time limit, VIP death, etc.)
- Surrender (optional)

---

## ADVANCED RULES (Quick Notes)

### Pilot Wound Deck (10 cards)
- Flip 1 when pilot takes damage (capsule breach, Thread snap, etc.)
- 5 Minor Injuries (temporary debuffs)
- 3 Severe Injuries (PERMANENT effects)
- 2 Trauma (mental breakdowns)
- All 10 Wounds = Pilot Death

### Ancestral Iron (Crucible)
- Spend 5 Forge tokens at end of mission
- Forge 1 Ancestral Weapon (+1 dmg OR +1 DEF OR +1 move)
- Permanent upgrade (persists across missions)
- Max 3 Ancestral Weapons total

### Leg-Skimming (Campaign)
- Sacrifice pilot legs permanently
- Gain permanent SP boost (+1 SP per turn)
- Cannot undo (irreversible)

---

## PLAYTEST CHECKLIST

Before first game:
- ☑ Print 2 decks (30 cards each)
- ☑ Print hex map (12×10 grid)
- ☑ Tokens: SP, Heat, Forge/Blood stacks
- ☑ D6 dice (for Strain rolls)
- ☑ Support unit cards + behavior decks
- ☑ Quick reference sheet (this page)

During game:
- ☑ Track SP each turn (refresh start of turn)
- ☑ Discard hand at end of turn (important!)
- ☑ Check Component Damage (3+ same type)
- ☑ Roll Strain at 5+ Heat
- ☑ Mark terrain effects (lava, ruins, etc.)

---

## COMMON MISTAKES

### ❌ Don't Forget:
1. Discard entire hand at end of turn (even unplayed cards)
2. Lava damage happens at START of turn (not end)
3. Unspent SP is lost (cannot bank)
4. Component Damage requires 3+ of SAME TYPE (not just 3+ total)
5. Defense reduces damage but minimum 1 damage always dealt
6. Support units act independently (don't cost your SP)

### ✅ Remember:
1. Draw 6 cards EVERY turn (unless modified)
2. Passive abilities trigger automatically (Living Forge, etc.)
3. Reactive cards play on opponent's turn (Defend, Parry, etc.)
4. Buffs expire at end of round (unless specified)
5. Heat Strain roll ONLY at 5+ Heat (not below)

---

**"Know these rules. Master the flow. Dominate the battlefield."**

*Quick Reference Sheet v1.0 - Penance*

---

[← Back to Rules](../index.html) | [Example of Play](example-of-play.md) | [Full Combat Rules](combat-resolution-detailed.md)
