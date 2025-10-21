# Settlement Phase Procedure
## Penance: Campaign System

**Version**: 3.0
**Last Updated**: October 14, 2025

---

## Overview

The **Settlement Phase** occurs **between missions** in campaign play. This is where you spend resources, heal injuries, build structures, and prepare for the next mission. It's the strategic layer of Penance, inspired by Kingdom Death: Monster's settlement phase.

**Duration**: ~15-30 minutes of real-time play

**Frequency**: After every mission (successful or failed)

---

## Settlement Phase Structure

The Settlement Phase has **6 steps**, performed in order:

```
1. RETURN → 2. INCOME → 3. EVENT → 4. SETTLEMENT ACTIONS → 5. PILOT CARE → 6. MISSION SELECT
```

---

## STEP 1: RETURN

**Narrative**: Your Caskets limp back to the settlement. The gates open. Survivors are extracted from capsules.

### 1.1 Casualty Assessment
- **Pilots who survived**: Remain in your roster
- **Pilots who died** (Casket HP reached 0 and failed all save mechanics):
  - Remove from roster permanently
  - Survivors may mourn (see Morale effects)
  - Settlement may hold funeral (optional narrative)

### 1.2 Salvage Collection
- Collect **Scrap** from mission:
  - Base mission reward: Varies by scenario (0-5 Scrap)
  - Enemy Caskets destroyed: +1 Scrap each
  - Equipment destroyed: Can be scrapped (see settlement actions)
- Collect **Credits** from mission reward (varies by scenario: 50-300 Credits)

### 1.3 Loot Roll
- If mission had loot tables, roll now (see [loot-tables.md](loot-tables.md))
- Assign loot to pilots or settlement storage

---

## STEP 2: INCOME

**Passive income from settlement buildings.**

### 2.1 Building Income
Calculate passive income from structures:

| Building | Income per Phase |
|----------|-----------------|
| **The Market** | +25 Credits |
| **Soulstone Refinery** | +1 Soulstone Fragment (= 75 Credits or special crafting) |
| **The Scrapyard** (Scrap-Clans faction) | +2 Scrap |
| **Living Grove** (Elves faction, if planted) | Roll on Nature's Bounty table |

**Example**:
```
You have: Market + Refinery
Income this phase: +25 Credits + 1 Soulstone Fragment
```

### 2.2 Upkeep Costs
Deduct maintenance costs (if any):
- **Pilot Salaries**: 10 Credits per pilot per phase (optional rule)
- **Attendants**: 40 Credits per Efficient Form pilot (Ossuarium life support)
- **Building Repairs**: If settlement was damaged by events, pay repair costs

---

## STEP 3: EVENT ROLL

**Random events occur. Roll 1d100 on the Settlement Event Table.**

### Event Table (Simplified)

| d100 | Event | Effect |
|------|-------|--------|
| 01-10 | **Refugee Arrival** | +2 pilots join settlement (random class). Roll for quirks. |
| 11-20 | **Bandit Raid** | Pay 50 Credits or lose 2 Scrap. If you refuse, fight a Bandit Defense mission next. |
| 21-30 | **Bountiful Hunt** | Gain +50 Credits (hunters brought back game). |
| 31-40 | **Illness Outbreak** | All pilots with Minor Injuries become Severe unless you have Apothecary. |
| 41-50 | **Void Leak** (if Refinery exists) | Refinery damaged. Lose 1 Soulstone Fragment. Repair costs 100 Credits. |
| 51-60 | **Market Boom** | All equipment costs -25% this phase only. |
| 61-70 | **Rival Faction Visit** | Roll 1d6: 1-2 Church, 3-4 Dwarves, 5 Ossuarium, 6 Elves. They offer a mission. |
| 71-80 | **Discovery** | Scouts found Old World ruins. Gain 1d3 Scrap OR roll on Loot Table. |
| 81-90 | **Peaceful Phase** | No event. Morale +1. |
| 91-95 | **Pilgrimage** (Church territory) | Pilgrims visit. Gain +2 Morale if you have Shrine/Sanctuary. |
| 96-100 | **Anomalous Event** | Roll on [Anomalous Event Table](../campaigns/anomalous-events.md) (100 weird events). |

**Note**: Full Settlement Event Table is in development. Use this simplified version for playtesting.

---

## STEP 4: SETTLEMENT ACTIONS

**Players may perform actions using settlement buildings.**

### 4.1 Available Actions

Each player may perform **2 settlement actions** per phase (unless buildings grant more).

**Universal Actions** (always available):
- **Rest**: Do nothing. Recover 1 Morale.
- **Train**: Spend 50 Credits. Gain +1 to one skill (Initiative, Grit, etc.). Max +2 per stat.
- **Scavenge**: Roll 1d6. On 4+, find 1 Scrap.

**Building-Dependent Actions** (require specific structures):

#### The Forge (Universal)
- **Craft Equipment**: Spend Credits + Scrap to build equipment (see equipment costs)
- **Repair Equipment**: Restore destroyed equipment for 50% of crafting cost
- **Scrap Salvage**: Convert 1 destroyed equipment into 1 Scrap (once per phase)

#### The Apothecary (Universal)
- **Heal Minor Injury**: Spend 25 Credits, remove 1 Minor Injury from pilot
- **Heal Severe Injury**: Spend 100 Credits, downgrade 1 Severe Injury to Minor
- **Surgery**: Spend 200 Credits, attempt to remove 1 Trauma card (roll 1d6, 4+ success)

#### The Barracks (Universal)
- **Drill Training**: Spend 50 Credits, grant 1 pilot +1 Initiative permanently (max +2, once per pilot)

#### The Market (Universal)
- **Trade**: Roll on Trade Table (buy/sell equipment)
- **Black Market Contact**: Purchase 1 random equipment at 50% discount (once per phase)

#### The Shrine (Universal)
- **Ritual of Cleansing**: Spend 100 Credits, remove 2 Taint from 1 pilot

#### The Archive (Special)
- **Research**: Roll on Research Table (unlock lore, ancient schematics)
- **Ask Lore Question**: Ask GM 1 lore question, receive truthful answer (once per phase)

#### The Arsenal (Military)
- **Unlock Tier 2 Equipment**: Craft Relic-grade weapons (high-cost, high-power)

#### The Workshop (Infrastructure)
- **Modify Casket**: Change weight class, swap components (50-200 Credits depending on scope)

#### The Soulstone Refinery (Economic)
- **Convert Fragments**: Spend Soulstone Fragments as 75 Credits each
- **Special Crafting**: Craft Soulstone-powered equipment (requires fragments, not Credits)

#### Faction-Specific Buildings
- **Runeworks** (Dwarves): Inscribe runes on equipment (+1 to attack/defense, costs 100 Credits)
- **Living Grove** (Elves): Plant Casket for organic upgrades (roll on Nature's Bounty table)
- **The Ossuary** (Ossuarium): Raise dead pilots as lesser undead attendants (costs 150 Credits)

### 4.2 Building Construction

**If you have resources, you may build new structures.**

**Process**:
1. Choose building from [settlements.md](settlements.md)
2. Pay Scrap + Credit cost
3. If "Build Time: 1 phase" → Building completes next settlement phase
4. If "Build Time: Immediate" → Use building this phase

**Example**:
```
You want to build The Market.
Cost: 1 Scrap + 50 Credits
Build Time: Immediate
You pay the cost. Market is built. You can now use Trade actions this phase.
```

---

## STEP 5: PILOT CARE

**Manage pilot health, progression, and Flesh Bargain choices.**

### 5.1 Injury Recovery
- **Automatic Healing**: All pilots recover 1 Minor Injury at end of phase (free)
- **Barracks Bonus**: If you have Barracks, pilots recover 1 additional injury (2 total)
- **Severe Injuries**: Do NOT automatically heal (require Apothecary actions)

### 5.2 Grit Progression (v3.0)
- Check pilot missions survived
- Update Grit stat if thresholds met:
  - 5 missions → Grit 1
  - 10 missions → Grit 2
  - 20 missions → Grit 3
- Update for Severe Injuries survived:
  - 1 Severe Injury → Grit 1 (fast-track)
  - 3 Severe Injuries → Grit 2
  - 5 Severe Injuries → Grit 3

### 5.3 Flesh Bargain Offers
**After mission 5, 10, or 15**, faction specialists offer Flesh Bargain procedures:

**Offer Triggers**:
- **Mission 5**: First offer (Church = Shortening, Dwarves = Compact Form, etc.)
- **Mission 10**: Second offer (if declined first time)
- **Mission 15**: Third offer (last chance for standard sacrifice)
- **Mission 20+**: Extreme variants unlock (Living Martyr, Skull Pilot, etc.)

**Procedure** (see [flesh-bargain-variants.md](flesh-bargain-variants.md)):
1. Pilot chooses to undergo sacrifice (or declines)
2. Pay surgery cost (80-200 Credits, 2-5 Medical Supplies)
3. Pilot enters recovery (4-12 weeks downtime, cannot deploy)
4. After recovery, pilot gains benefits (+1 SP max, +2 Heat capacity, +1 Grit, etc.)

### 5.4 Pilot Relationships (Optional)
- Pilots may form bonds, rivalries, romances (narrative tracking)
- Affects Morale when paired or separated in missions

---

## STEP 6: MISSION SELECT

**Choose your next mission and embark.**

### 6.1 Available Missions
**GM presents 2-3 mission options** from:
- **Story Missions**: Advance campaign narrative
- **Side Missions**: Optional, resource-focused
- **Faction Missions**: Offered by rival factions (affects reputation)
- **Engine Expeditions**: High-risk Sibarian Wastes missions (rare, high reward)

**If you have The Watchtower**:
- May **scout 1 mission** before choosing
- Reveals: Mission objectives, 1 enemy type, map hazard

### 6.2 Mission Briefing
GM describes:
- **Objective**: What you need to accomplish
- **Reward**: Credits, Scrap, Loot, Reputation
- **Known Threats**: Enemy types, hazards (partial info unless scouted)
- **Special Conditions**: Time limits, ally NPCs, environmental effects

### 6.3 Pilot Assignment
- Choose which pilots deploy (max depends on scenario, usually 1-4 pilots)
- Assign equipment from settlement storage
- Final deck construction (26-50 cards: 10 Universal + 6 Faction Core + Equipment cards + 2 Tactics)

### 6.4 Embark
- Narrative transition: "You board your Caskets. The capsules seal. Fluid floods your lungs. The Thread pierces your fingers. You are one with the machine."
- **BEGIN MISSION** → Tactical combat phase begins

---

## Settlement Phase Flowchart

```
┌─────────────────────────────────────────────────────────┐
│  MISSION COMPLETE                                       │
│  (Survive or Die Trying)                                │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 1: RETURN                                          │
│  • Count casualties                                     │
│  • Collect Scrap from mission (0-5 base + kills)        │
│  • Collect Credits from mission reward                  │
│  • Roll loot tables (if applicable)                     │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 2: INCOME                                          │
│  • Market: +25 Credits                                  │
│  • Refinery: +1 Soulstone Fragment                      │
│  • Other buildings: +resources                          │
│  • Deduct upkeep costs (pilots, attendants, repairs)    │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 3: EVENT ROLL                                      │
│  • Roll 1d100 on Settlement Event Table                 │
│  • Apply effects immediately                            │
│  • (Refugee Arrival, Bandit Raid, Void Leak, etc.)      │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 4: SETTLEMENT ACTIONS                              │
│  • Each player performs 2 actions                       │
│  • (Craft, Heal, Train, Research, Build, etc.)          │
│  • Construct new buildings (if resources available)     │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 5: PILOT CARE                                      │
│  • Auto-heal 1 Minor Injury per pilot                   │
│  • Check Grit progression thresholds                    │
│  • Flesh Bargain offers (if mission 5/10/15/20+)       │
│  • Update relationships (optional)                      │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 6: MISSION SELECT                                  │
│  • GM presents 2-3 mission options                      │
│  • Scout with Watchtower (if built)                     │
│  • Assign pilots to mission                             │
│  • Finalize equipment/decks                             │
│  • EMBARK → Begin tactical combat                       │
└─────────────────────────────────────────────────────────┘
```

---

## Example Settlement Phase

**Context**: You just completed "Arena Gauntlet" mission (success). You have 2 pilots: Gareth (Church) and Thrain (Dwarf). Your settlement has: The Forge, The Apothecary, The Market.

### Step 1: Return
- **Casualties**: None (both survived)
- **Scrap Collected**: 2 (base reward) + 1 (destroyed enemy Casket) = 3 Scrap total
- **Credits Collected**: 100 (mission reward)
- **Loot**: Roll 1d6 on Loot Table → Result: 5 = Kite Shield (equipment)

**Your Resources**: 3 Scrap, 100 Credits, 1 Kite Shield

---

### Step 2: Income
- **Market Income**: +25 Credits
- **No Upkeep Costs** (you don't use pilot salaries)

**New Total**: 3 Scrap, 125 Credits, 1 Kite Shield

---

### Step 3: Event Roll
- **Roll 1d100**: Result = 42
- **Event**: Illness Outbreak
- **Effect**: "All pilots with Minor Injuries become Severe unless you have Apothecary."
- **Your Apothecary**: Protects pilots. No effect.

---

### Step 4: Settlement Actions

**Gareth's Actions** (2 actions):
1. **Heal Minor Injury** (Apothecary): Pay 25 Credits, remove Broken Finger injury
2. **Rest**: Recover 1 Morale (Gareth now at Morale 3)

**Thrain's Actions** (2 actions):
1. **Craft Equipment** (Forge): Craft Warhammer (costs 5 Scrap + 80 Credits... you don't have enough)
   - **FAILED**: Not enough resources
2. **Scrap Salvage** (Forge): Convert destroyed Longsword into 1 Scrap
   - **SUCCESS**: Gain 1 Scrap (now have 4 Scrap total)

**Settlement Building**:
- You want to build **The Barracks** (costs 2 Scrap + 100 Credits, Immediate)
- **You pay**: 2 Scrap, 100 Credits
- **Barracks Built**: Can now use Drill Training actions

**New Total**: 2 Scrap, 0 Credits, 1 Kite Shield

---

### Step 5: Pilot Care
- **Auto-Healing**: Both pilots recover 1 Minor Injury (Gareth already healed his, Thrain recovers Bruised Ribs)
- **Grit Progression**: Gareth has 6 missions survived → Gains Grit 1 (Seasoned)
- **Flesh Bargain**: Gareth qualifies (6 missions), but you decline the offer

---

### Step 6: Mission Select
- **GM offers 3 missions**:
  1. "Caravan Escort" (50 Credits, 1 Scarp, Low Danger)
  2. "Bandit Camp Raid" (150 Credits, 3 Scrap, Medium Danger)
  3. "Church Crusade: Purge the Blighted" (200 Credits, 5 Scrap, High Danger, +Church Reputation)

- **You choose**: "Bandit Camp Raid" (medium risk, good reward)
- **Assign Pilots**: Both Gareth and Thrain deploy
- **Equip**: Assign Kite Shield to Thrain

**EMBARK** → Next mission begins!

---

## Tracking Sheets

### Settlement Resources Sheet
```
┌─────────────────────────────────────┐
│ SETTLEMENT: Ironhold                │
├─────────────────────────────────────┤
│ RESOURCES:                          │
│  Credits: ___________               │
│  Scrap: ___________                 │
│  Soulstone Fragments: ___________   │
│                                     │
│ BUILDINGS (check when built):       │
│  ☐ The Forge                        │
│  ☐ The Barracks                     │
│  ☐ The Apothecary                   │
│  ☐ The Market                       │
│  ☐ The Shrine                       │
│  ☐ The Arsenal                      │
│  ☐ The Workshop                     │
│  ☐ The Soulstone Refinery           │
│  ☐ The Archive                      │
│  ☐ The Watchtower                   │
│  ☐ Other: _________________         │
│                                     │
│ MORALE: _____ / 10                  │
│                                     │
│ INSTABILITY (Engine): _____ / 20    │
└─────────────────────────────────────┘
```

### Pilot Roster Sheet
```
┌─────────────────────────────────────┐
│ PILOT: _________________________    │
├─────────────────────────────────────┤
│ Faction: ____________               │
│ Casket Type: ____________           │
│ Missions Survived: _____            │
│                                     │
│ GRIT: ____ (0-3)                    │
│ MORALE: ____ (0-10)                 │
│ TAINT: ____ (0-10)                  │
│                                     │
│ INJURIES:                           │
│  Minor: _______________________     │
│  Severe: ______________________     │
│  Trauma: ______________________     │
│                                     │
│ SOUL SACRIFICE:                     │
│  ☐ Not Taken                        │
│  ☐ Shortening (Church)              │
│  ☐ Compact Form (Dwarves)           │
│  ☐ Efficient Form (Ossuarium)       │
│  ☐ Root-Grafting (Elves)            │
│  ☐ Other: _________________         │
└─────────────────────────────────────┘
```

---

## Campaign Milestones

Track these across multiple settlement phases:

| Milestone | Trigger | Reward |
|-----------|---------|--------|
| **First Victory** | Win first mission | +50 Credits, Morale +2 |
| **Five Survivors** | 5 pilots survive to mission 5 | Unlock Elite Training (Barracks upgrade) |
| **Industrialized** | Build 5+ settlement structures | +1 Settlement Action per pilot (3 total) |
| **Engine Contact** | Complete first Engine Expedition | Unlock Soulstone Refinery blueprint |
| **Factional Alliance** | Complete 3 missions for one faction | Unlock faction-specific building |
| **Hardened Veterans** | 2 pilots reach Grit 3 | Unlock "Veteran's Gambit" special mission |
| **The Long Campaign** | Survive 20 missions | Unlock endgame mission options (Church/Dwarves/Elves/etc.) |

---

## Designer's Notes

### Why Settlement Phase Matters
1. **Strategic Depth**: Not just "fight missions" - resource management, long-term planning
2. **Narrative Beats**: Downtime creates character moments (injuries, relationships, Flesh Bargain choices)
3. **Campaign Tension**: Instability Clock ticks, events force reactions, missions have consequences
4. **Kingdom Death Inspiration**: Scarcity, tough choices, meaningful upgrades

### Pacing Tips for GMs
- **Fast Phase** (15 min): Skip Step 3 Event, limit actions to 1 per pilot, pre-select missions
- **Standard Phase** (30 min): Use all steps, 2 actions per pilot
- **Epic Phase** (60 min): Add roleplaying, detailed NPC interactions, settlement political intrigue

---

**END OF DOCUMENT**

---

*"Between battles, we build. Between deaths, we remember. This is how we survive."*
