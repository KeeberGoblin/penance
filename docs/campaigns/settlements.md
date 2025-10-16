# Settlement Mechanics
## Campaign Base-Building System

**Version**: 0.1
**Last Updated**: October 10, 2025

---

## Design Philosophy

Drawing from Kingdom Death's settlement phase, this system focuses on:
- **Meaningful scarcity** - resources are always limited, forcing hard choices
- **Interconnected upgrades** - buildings unlock other buildings, creating strategic paths
- **Narrative consequences** - settlements tell stories through their architecture
- **Asymmetric disasters** - settlements can be destroyed, and recovery is brutal
- **No pure optimization** - every choice has a cost

---

## Core Mechanics

### Settlement Phases

**Campaign Structure**: Missions → Settlement Phase → Missions → Settlement Phase

After every **2-3 missions**, players return to their settlement for:
1. **Triage** - Repair damaged Caskets, treat wounded pilots
2. **Workshop** - Spend Credits on upgrades and equipment
3. **Construction** - Build or upgrade settlement buildings
4. **Events** - Roll on the Settlement Event table (both good and bad)
5. **Preparation** - Choose next mission, assign pilots

---

## The Settlement Sheet

### Core Resources

**Credits** (Primary Currency)
- Earned from missions (100 for primary objective, 50 for secondary)
- Spent on repairs, equipment, and construction
- **Scarcity Rule**: Credits don't accumulate infinitely - max bank is 500 (represents logistical limits)

**Scrap** (Salvage Material)
- Gained from destroyed enemy Caskets (1d3 Scrap per kill)
- Used for building construction and emergency repairs
- Can be traded to Forge-Guilds at 2 Scrap = 50 Credits (poor exchange rate)

**Population** (Settlement Size)
- Starts at 10 (small outpost)
- Increases by +1 per successful mission (survivors flock to safety)
- Decreases when settlement is attacked or suffers catastrophic events
- **Maximum Population**: 50 (depends on housing capacity)
- **Population Benefits**: Higher population = more building slots unlocked

**Morale** (Settlement Spirit)
- Starts at 5 (Neutral)
- Scale: 0 (Despair) → 10 (Hope)
- Affects event table results (low morale = worse events)
- **Morale Modifiers**:
 - Mission success: +1 Morale
 - Mission failure: -2 Morale
 - Pilot death: -1 Morale
 - Abomination raid survived: +2 Morale
 - Certain buildings provide passive +1 Morale

---

## Settlement Buildings

### Building Slots
- **Tier 1**: Start with 3 building slots
- **Tier 2**: Unlocked at Population 20 (adds 2 slots)
- **Tier 3**: Unlocked at Population 35 (adds 2 slots)
- **Maximum**: 7 building slots total

### Building Categories

Buildings are categorized by function:
- **Infrastructure** (essential services)
- **Military** (combat support)
- **Economic** (resource generation)
- **Special** (unique, faction-specific)

---

## Tier 1 Buildings (Starting Options)

### 1. **The Forge** (Infrastructure) 🔨
**Cost**: 3 Scrap, 100 Credits
**Build Time**: Immediate
**Effect**:
- Unlocks equipment crafting
- Repair costs reduced by 25%
- **Special Action**: Scrap Salvage - Convert 1 destroyed equipment card into 1 Scrap (once per settlement phase)

**Narrative**: A crude workshop with a bellows-forge and anvil. Sparks fly as blacksmiths hammer out repairs.

---

### 2. **The Barracks** (Military) 
**Cost**: 2 Scrap, 50 Credits
**Build Time**: Immediate
**Effect**:
- Increases pilot roster capacity from 4 to 6
- Pilots heal 1 additional injury per settlement phase
- **Special Action**: Drill Training - Spend 50 Credits to grant 1 pilot +1 Initiative permanently (max +2, once per pilot)

**Narrative**: Rows of cots and training dummies. The smell of sweat and oil.

---

### 3. **The Apothecary** (Infrastructure) 🏥
**Cost**: 2 Scrap, 75 Credits
**Build Time**: Immediate
**Effect**:
- Reduces injury recovery time by 1 phase
- Unlocks advanced medical treatments (see Treatment Table)
- **Special Action**: Emergency Stabilization - Prevent 1 pilot death per mission (must be declared immediately when pilot would die)

**Narrative**: Shelves lined with bloodied bandages and herbal tinctures. The screams of the wounded echo.

---

### 4. **The Market** (Economic) 
**Cost**: 1 Scrap, 50 Credits
**Build Time**: Immediate
**Effect**:
- Generates +25 Credits per settlement phase (passive income)
- Unlocks **Trade Actions** (see Trade Table)
- **Special Action**: Black Market Contact - Once per settlement phase, purchase 1 piece of equipment at 50% discount (random selection, roll on loot table)

**Narrative**: A bustling bazaar where refugees trade scavenged goods. Prices are brutal.

---

### 5. **The Shrine** (Infrastructure) 
**Cost**: 2 Scrap, 50 Credits
**Build Time**: Immediate
**Effect**:
- +1 Morale (passive)
- Reduces Taint accumulation by 1 point per settlement phase (for all pilots)
- **Special Action**: Ritual of Cleansing - Spend 100 Credits to remove 2 Taint from 1 pilot (once per phase)

**Narrative**: Incense burns before an altar draped in prayer chains. Penitents kneel in silent devotion.

---

## Tier 2 Buildings (Unlocked at Population 20)

### 6. **The Arsenal** (Military) 
**Cost**: 5 Scrap, 200 Credits
**Build Time**: 1 settlement phase
**Requires**: The Forge
**Effect**:
- Unlocks Tier 2 equipment crafting (Relic-grade weapons)
- +1 Relic slot for all Caskets
- **Special Action**: Weapon Enchantment - Spend 150 Credits to upgrade 1 weapon with a permanent bonus (roll on Enchantment Table)

**Narrative**: A vault filled with Soulstone-powered weaponry. The air hums with latent energy.

---

### 7. **The Workshop** (Infrastructure) 
**Cost**: 4 Scrap, 150 Credits
**Build Time**: 1 settlement phase
**Requires**: The Forge
**Effect**:
- Unlocks Casket modifications (weight class changes, component swaps)
- Allows combining 2 broken equipment pieces into 1 functional item
- **Special Action**: Emergency Retrofit - Completely rebuild 1 destroyed Casket (costs 200 Credits + 3 Scrap)

**Narrative**: A cavernous hangar where Caskets hang on chains like carcasses in a butcher's shop.

---

### 8. **The Soulstone Refinery** (Economic) 
**Cost**: 6 Scrap, 250 Credits
**Build Time**: 2 settlement phases
**Requires**: The Forge
**Effect**:
- Generates 1 Soulstone Fragment per settlement phase (can be spent as 75 Credits OR used for special crafting)
- Unlocks Soulstone-powered equipment
- **Danger**: Every settlement phase, roll 1d6. On a 1, the refinery suffers a **Void Leak** (see Disasters)

**Narrative**: A pulsing crystal chamber surrounded by arcane wards. Workers wear lead-lined suits.

---

### 9. **The Archive** (Special) 📚
**Cost**: 3 Scrap, 100 Credits
**Build Time**: 1 settlement phase
**Effect**:
- Unlocks **Research Actions** (see Research Table)
- Once per settlement phase, players may ask the GM 1 lore question and receive a truthful answer
- **Special Action**: Ancient Schematic - Roll on the Lost Technology table to discover forgotten equipment designs

**Narrative**: A dusty library filled with water-damaged pre-Cataclysm tomes. Knowledge is hoarded here.

---

### 10. **The Watchtower** (Military) 
**Cost**: 4 Scrap, 100 Credits
**Build Time**: 1 settlement phase
**Effect**:
- Reduces chance of surprise attacks on settlement by 50%
- Players may scout the next mission before committing (reveal mission objectives and 1 enemy type)
- **Special Action**: Early Warning System - Once per campaign, avoid 1 settlement disaster entirely

**Narrative**: A crude tower built from scrap metal and salvaged wood. Sentries scan the horizon, watching for rifts.

---

## Tier 3 Buildings (Unlocked at Population 35)

### 11. **The Reliquary** (Special) 
**Cost**: 10 Scrap, 400 Credits
**Build Time**: 3 settlement phases
**Requires**: The Shrine + The Archive
**Effect**:
- Unlocks **Forbidden Technologies** (Aberrant-class Caskets, Tainted weapons)
- Pilots may permanently gain +1 Taint to unlock a unique Relic ability
- **Danger**: Attracts Void attention - settlement attack chance increases by +1 per phase

**Narrative**: A sealed vault where heretical artifacts glow with unnatural light. Only the desperate enter.

---

### 12. **The Foundry** (Military) 🏭
**Cost**: 8 Scrap, 500 Credits
**Build Time**: 3 settlement phases
**Requires**: The Workshop + The Arsenal
**Effect**:
- Allows construction of **1 custom Casket** per campaign (players design from scratch within balance limits)
- Reduces all equipment costs by 30%
- **Special Action**: Mass Production - Spend 300 Credits to equip all pilots with standardized Tier 1 weapons

**Narrative**: Smokestacks belch ash. The clangor of hammers on steel never ceases.

---

### 13. **The Sanctuary** (Infrastructure) 
**Cost**: 7 Scrap, 300 Credits
**Build Time**: 2 settlement phases
**Requires**: The Apothecary + The Shrine
**Effect**:
- +2 Morale (passive, replaces Shrine's +1)
- All pilots automatically remove 1 Permanent Injury at the start of each campaign arc (every 5 missions)
- **Special Action**: Miracle Cure - Once per campaign, fully heal 1 pilot of all injuries and Taint (but they gain a **Debt** to the Sanctuary - must complete a side quest)

**Narrative**: A tranquil garden inside the settlement. Patients rest under makeshift pavilions, tended by healers.

---

### 14. **The War Council Hall** (Military) 
**Cost**: 5 Scrap, 200 Credits
**Build Time**: 2 settlement phases
**Effect**:
- Unlocks **Strategic Missions** (high-risk, high-reward)
- Players may choose to repeat previously failed missions (re-attempt)
- **Special Action**: Faction Embassy - Negotiate with 1 faction to improve relationship by 1 tier (see Faction Relationship Tracker)

**Narrative**: A round table surrounded by maps and battle plans. Leaders argue late into the night.

---

## Special: Faction-Specific Buildings

If players align strongly with a faction, they may unlock unique buildings:

### **Church of Absolution: The Martyrium**
**Cost**: 6 Scrap, 300 Credits
**Effect**: All pilots may take the **Penitent's Vow** - gain +1 SP but take 1 damage at the start of each mission (representing self-flagellation rituals)

### **Verdant Covenant: The Living Grove**
**Cost**: 5 Scrap, 250 Credits
**Effect**: Caskets may be "planted" for 1 settlement phase, growing organic upgrades (random, roll on Nature's Bounty table)

### **Forge-Guilds: The Runeworks**
**Cost**: 8 Scrap, 400 Credits
**Effect**: All equipment gains +1 durability (harder to destroy). Unlocks Runic Inscriptions (minor stat bonuses)

### **Scrap-Clans: The Scrapyard**
**Cost**: 3 Scrap, 100 Credits
**Effect**: Generates 2 Scrap per settlement phase. Allows building makeshift Caskets from pure salvage (unreliable but free)

### **The Ossuarium: The Ossuarium**
**Cost**: 7 Scrap, 350 Credits
**Effect**: Dead pilots may be raised as Undead (lose all personality, but can still fight - stats reduced by 50%)

### **The Wyrd Conclave: The Feywild Gate**
**Cost**: 10 Scrap, 500 Credits
**Effect**: Once per settlement phase, make a **Bargain with the Fae** - gain a massive boon, but suffer a hidden curse (GM's choice)

---

## Settlement Events Table

Roll 1d20 at the end of each Settlement Phase:

**Morale Modifiers**: +1 to roll per 2 Morale above 5, -1 per 2 Morale below 5

| Roll | Event |
|------|-------|
| 1-2 | **Void Rift Opens** - Settlement is attacked by 1d3 Abominations. Defend or lose 1d6 Population and 1 random building. |
| 3-4 | **Plague Outbreak** - Lose 1d3 Population. If you have The Apothecary, reduce loss by half. |
| 5-6 | **Raider Attack** - Bandits demand 100 Credits. Pay or fight (roll opposed d6 vs raiders, lose if you roll lower). |
| 7-8 | **Supply Shortage** - All repairs cost +50% this phase. |
| 9-10 | **Refugee Caravan** - Gain 1d3 Population. They bring rumors of distant Soulstone deposits. |
| 11-12 | **Uneventful** - Nothing happens. A rare moment of peace. |
| 13-14 | **Salvage Discovery** - Gain 1d3 Scrap for free. |
| 15-16 | **Talented Recruit** - Gain 1 new pilot with a random positive trait (roll on Pilot Trait table). |
| 17-18 | **Trade Windfall** - Visiting merchants offer rare goods. Gain access to 1 random Tier 2 equipment (discounted by 100 Credits). |
| 19-20 | **Morale Surge** - +2 Morale. The people believe in you. Gain 50 Credits from donations. |

---

## Settlement Disasters

Some events or building failures trigger **Disasters** - catastrophic events that can cripple your settlement.

### **Void Leak** (Soulstone Refinery failure)
- 1d3 Population dies from Taint exposure
- All pilots gain +1 Taint
- Refinery is disabled until repaired (costs 100 Credits + 2 Scrap)

### **Fire** (Random chance, increases with wooden buildings)
- Roll 1d6: Lose that number of Scrap
- 1 random building takes 1 damage (3 damage = destroyed)

### **Betrayal** (Low Morale event, Morale <3)
- 1 pilot deserts, taking 1 piece of equipment with them
- Lose 1d6 Population
- -2 Morale

### **Inquisition Raid** (High Taint event, any pilot has Taint 8+)
- Church sends Penitent Knights to "cleanse" your settlement
- Fight them off or surrender the corrupted pilot
- If you fight and lose: Lose 2d6 Population and 1 building

---

## Settlement Growth Path (Example Campaign)

**Phase 1 (Missions 1-5): Survival**
- Build: Forge, Barracks, Shrine
- Focus: Repair infrastructure, stockpile Credits
- Population: 10 → 18

**Phase 2 (Missions 6-10): Expansion**
- Build: Workshop, Market, Apothecary
- Focus: Unlock better equipment, stabilize Morale
- Population: 18 → 27

**Phase 3 (Missions 11-15): Specialization**
- Build: Arsenal OR Soulstone Refinery (choose your path)
- Focus: Push toward Tier 3 buildings or faction alignment
- Population: 27 → 40

**Phase 4 (Endgame): Powerhouse or Ruin**
- Build: Reliquary, Foundry, or faction-specific building
- Outcome: Either dominate the campaign or suffer spectacular collapse

---

## Design Notes

### Why This System Works
1. **Scarcity Creates Tension** - You can't build everything, forcing priorities
2. **Buildings Tell Stories** - A settlement with a Reliquary and Ossuarium feels different from one with a Sanctuary and Archive
3. **Disasters Hurt** - Kingdom Death's lesson: loss must be meaningful
4. **Asymmetric Paths** - Church settlements play differently from Scrap-Clan ones

### Balancing Act
- **Income Rate**: ~150-200 Credits per 2 missions (after repairs)
- **Building Costs**: Tier 1 (~100), Tier 2 (~200), Tier 3 (~400)
- **Timeline**: ~15 missions to build a fully upgraded settlement (if you're efficient and lucky)

---

*"Your settlement is a promise. Will you keep it, or watch it burn?"*
