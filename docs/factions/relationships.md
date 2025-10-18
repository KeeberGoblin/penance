# Faction Relationship Tracker
## Political Web & Grudge System

**Version**: 0.1
**Last Updated**: October 10, 2025

---

## Design Philosophy

Inspired by Kingdom Death's **intimacy and rivalry** mechanics, this system tracks:
- **Complex relationships** - factions don't simply "hate" or "ally" with each other
- **Historical grudges** - past events create ongoing friction
- **Player influence** - your actions shift the political landscape
- **Asymmetric dynamics** - Faction A's view of Faction B may differ from B's view of A

---

## Relationship Scale

Faction relationships are rated on a **7-tier scale**:

| Tier | Relationship | Mechanical Effect |
|------|-------------|-------------------|
| **+3** | **Allied** | Provide military aid, share resources freely, offer safe harbor |
| **+2** | **Friendly** | Trade at discounted prices (-20%), provide intel, minor assistance |
| **+1** | **Cordial** | Neutral trade, won't attack unprovoked, tolerate presence |
| **0** | **Neutral** | Default state. Cold but professional. No bonuses or penalties. |
| **-1** | **Suspicious** | Trade at inflated prices (+20%), spread rumors, passive obstruction |
| **-2** | **Hostile** | Refuse trade, sabotage missions, send bounty hunters |
| **-3** | **War** | Active military conflict, kill-on-sight, total embargo |

---

## Faction Relationship Matrix (Starting State - Year 100)

|  | Church | Covenant | Forge | Scrap | Bone | Fae | Draconid |
|---|--------|----------|-------|-------|------|-----|----------|
| **Church of Absolution** | — | -1 | 0 | -2 | -3 | -2 | +1 |
| **Verdant Covenant** | -1 | — | -1 | 0 | -2 | +1 | +2 |
| **Forge-Guilds** | 0 | -1 | — | +1 | 0 | -1 | +1 |
| **Scrap-Clans** | -2 | 0 | +1 | — | 0 | 0 | -1 |
| **The Ossuarium** | -3 | -2 | 0 | 0 | — | +1 | 0 |
| **The Wyrd Conclave** | -2 | +1 | -1 | 0 | +1 | — | +2 |
| **Draconid Remembrance** | +1 | +2 | +1 | -1 | 0 | +2 | — |

---

## Detailed Faction Dynamics

### Church of Absolution (Humans)

**Philosophy**: "Taint is sin. Soulstones are cursed. Redemption through suffering."

#### Relationships:

**vs. Verdant Covenant (-2 Hostile, formerly -3 War)**
- **Why**: Elves worship the "Worldheart" instead of the Creator. Heresy.
- **Friction Points**: Competing for same territories, ideological incompatibility
- **Historical Grudge**: The Forest Wars (Year 223-227). Church views Elves as heretics who chose nature-worship over salvation.
- **Church Perspective on War**:
  - **Roothold Purge (Year 223)**: High Confessor Aldric declared Elven groves "Tainted sanctuaries" and ordered purification by fire. Church claims 3,000 Elves died "resisting redemption."
  - **Supply Convoy Attacks (Year 224)**: Church calls Elven ambush tactics "cowardly" and "dishonorable warfare."
  - **Cathedral Siege (Year 226)**: Church martyrs celebrated the 15,000 civilians who starved rather than surrender. The siege is taught as example of "faithful endurance."
  - **Treaty of Ash and Root (Year 227)**: Church begrudgingly accepted Forest Sanctuaries, viewing it as "tactical retreat" not true peace.
- **Current Status**: Ceasefire holds, but Church still sends missionaries to "save" Elves. Elves view this as cultural warfare.

**vs. Forge-Guilds (0 Neutral)**
- **Why**: Dwarves sell weapons to the Church but mock their religion
- **Friction Points**: Church wants free aid (charity), Dwarves demand payment (business)
- **Trade**: Church buys Dwarven equipment at standard prices
- **Tension**: Dwarves refuse to build "holy relics" (won't participate in superstition)

**vs. Scrap-Clans (-2 Hostile)**
- **Why**: Orcs raid Church settlements, don't respect "sacred law"
- **Friction Points**: Orcs view Church as weak, Church views Orcs as barbaric
- **Historical Grudge**: Orcish warlord "Graul the Unrepentant" burned the Cathedral of Chains (Year 93)
- **Ongoing Conflict**: Border skirmishes, bounty hunters, retaliatory raids

**vs. The Ossuarium (-3 War)**
- **Why**: Undead are abominations in Church doctrine. Necromancy is ultimate sin.
- **Friction Points**: EVERYTHING. Theological incompatibility.
- **Historical Grudge**: The Undead view the Church as "wasteful" (all those corpses, unused!)
- **Active Conflict**: Church sends Crusades into Bone-Marches regularly. Undead retaliate with plague-corpse catapults.

**vs. The Wyrd Conclave (-2 Hostile)**
- **Why**: Fae make deals that corrupt souls. Church sees them as devils.
- **Friction Points**: Fae trick desperate believers into bargains, undermining Church authority
- **Historical Grudge**: Fae replaced an entire town's population with doppelgangers (Year 78). Church noticed too late.
- **Tension**: Church Inquisition hunts Fae-touched individuals

**vs. Draconid Remembrance (+1 Cordial)**
- **Why**: Draconids are neutral, scholarly, not actively blasphemous
- **Friction Points**: Draconids know the Church's origin story is wrong (they were there). They politely don't mention it.
- **Trade**: Church buys historical texts from Draconids
- **Respect**: Draconids are old enough to be dangerous - Church doesn't provoke them

---

### Verdant Covenant (Elves)

**Philosophy**: "The world is alive. Harmonize with it, or be pruned."

#### Relationships:

**vs. Church of Absolution (-2 Hostile, formerly -3 War)**
- **Why**: Church clear-cuts forests for lumber, poisons rivers with runoff
- **Friction Points**: Environmental destruction vs. civilization's needs
- **Historical Grudge**: The Forest Wars (Year 223-227) ended in ceasefire but deep scars remain
- **Major Battles**:
  - **Betrayal at Roothold (Year 223)**: Church Crusaders burned sacred groves using alchemical fire, killing 3,000 Elves and destroying centuries-old Worldtrees. Sparked 4-year war.
  - **The Verdant Retaliation (Year 224)**: Elven rangers ambushed Church supply convoys, using guerrilla tactics. 12 Penitent Caskets destroyed in forest ambushes over 6 months.
  - **Siege of the Iron Cathedral (Year 226)**: Elven forces besieged Church capital for 8 months. Cathedral walls held, but famine killed 15,000 civilians. Both sides exhausted.
  - **Treaty of Ash and Root (Year 227)**: Ceasefire brokered by The Exchange. Church agreed to "Forest Sanctuaries" (no-logging zones). Elves agreed to stop attacks on Church settlements. Uneasy peace holds, but neither side trusts the other.

**vs. Forge-Guilds (-1 Suspicious)**
- **Why**: Dwarven mining scars the earth, disrupts ley lines
- **Friction Points**: Industry vs. nature
- **Trade**: Minimal. Elves trade rare herbs, Dwarves trade tools. Both grudgingly.
- **Tension**: One Dwarven mine collapsed a ley line nexus (Year 82). Elves haven't forgotten.

**vs. Scrap-Clans (0 Neutral)**
- **Why**: Orcs live in wastelands Elves don't want anyway
- **Friction Points**: Occasional border disputes, but no sustained conflict
- **Odd Respect**: Orcs don't pretend to be civilized. Elves appreciate the honesty.

**vs. The Ossuarium (-2 Hostile)**
- **Why**: Undead twist the natural cycle of life and death
- **Friction Points**: Necromancy is ecological violation (corpses should decompose and feed the soil)
- **Historical Grudge**: Undead raised an entire Elven burial grove as skeletons (Year 89). Unforgivable.

**vs. The Wyrd Conclave (+1 Cordial)**
- **Why**: Fae respect nature (in their own twisted way). Shared interest in dimensional ecology.
- **Friction Points**: Fae are unpredictable, dangerous
- **Alliance**: Elves and Fae occasionally cooperate against industrial factions
- **Tension**: Elves know better than to trust Fae, but they're useful allies

**vs. Draconid Remembrance (+2 Friendly)**
- **Why**: Draconids also remember the Old World's mistakes. Shared long-term perspective.
- **Friction Points**: None, really. Both are isolationist and patient.
- **Trade**: Knowledge exchange, historical records
- **Mutual Respect**: Both factions are ancient and wise

---

### Forge-Guilds (Dwarves)

**Philosophy**: "The Cataclysm was an engineering failure. Fix it with better engineering."

#### Relationships:

**vs. Church of Absolution (0 Neutral)**
- **Why**: Church buys weapons, Dwarves sell them. Business is business.
- **Friction Points**: Church wants charity, Dwarves want profit
- **Trade**: Robust. Church is a major customer.

**vs. Verdant Covenant (-1 Suspicious)**
- **Why**: Elves oppose mining, industry, progress
- **Friction Points**: Resource extraction vs. environmental protection
- **Historical Grudge**: Elves sabotaged a Dwarven mining operation (Year 84), claiming it "poisoned the Worldheart"
- **Tension**: Cold war. No open conflict, but lots of passive sabotage.

**vs. Scrap-Clans (+1 Cordial)**
- **Why**: Orcs buy Dwarven weapons (or steal them and reverse-engineer them). Dwarves respect Orcish ingenuity.
- **Friction Points**: Orcs don't *pay* for goods, they "acquire" them
- **Trade**: One-sided. Orcs raid, Dwarves pursue, eventually Orcs pay compensation (in salvage)
- **Odd Respect**: Dwarves admire Orcish scrap-tech. "Crude, but functional."

**vs. The Ossuarium (0 Neutral)**
- **Why**: Undead buy equipment, don't haggle, pay on time. Model customers.
- **Friction Points**: Dwarves find Undead creepy but profitable
- **Trade**: Steady. Undead pay premium prices for weapons (they have patience, don't need discounts)

**vs. The Wyrd Conclave (-1 Suspicious)**
- **Why**: Fae bargains are bad business (hidden clauses, reality-altering prices)
- **Friction Points**: Dwarves value contracts. Fae value *loopholes*.
- **Tension**: Dwarves refuse Fae deals (learned the hard way)

**vs. Draconid Remembrance (+1 Cordial)**
- **Why**: Draconids have Old World technical schematics. Dwarves want them.
- **Friction Points**: Draconids won't share certain knowledge (claiming it's "too dangerous")
- **Trade**: Technology for historical records

---

### Scrap-Clans (Orcs)

**Philosophy**: "Survive. Get stronger. Die gloriously."

#### Relationships:

**vs. Church of Absolution (-2 Hostile)**
- **Why**: Church settlements are soft targets for raids
- **Friction Points**: Orcs need resources, Church has them
- **Historical Grudge**: Church executed captured Orcish raiders instead of ransoming them (Year 90). Orcs took it personally.
- **Ongoing Conflict**: Regular raids vs. Crusader reprisals

**vs. Verdant Covenant (0 Neutral)**
- **Why**: Orcs and Elves rarely interact (different territories)
- **Friction Points**: Occasional skirmishes when Orcs cross Elven borders
- **Respect**: Elves are deadly in their forests. Orcs know better than to invade.

**vs. Forge-Guilds (+1 Cordial)**
- **Why**: Orcs admire Dwarven craftsmanship (and steal it)
- **Friction Points**: Theft. Constant theft.
- **Trade**: Barter system - Orcs trade salvage for weapons
- **Respect**: Dwarves are tough. Orcs like tough.

**vs. The Ossuarium (0 Neutral)**
- **Why**: Undead don't raid Orcish territories (nothing worth taking)
- **Friction Points**: None. Mutual indifference.
- **Odd Dynamic**: Orcs find Undead boring (they don't bleed, don't fear, no glory in fighting them)

**vs. The Wyrd Conclave (0 Neutral)**
- **Why**: Orcs avoid Fae territories (too weird, not enough loot)
- **Friction Points**: Fae occasionally trick Orcs into bargains for amusement
- **Tension**: Orcs who've been tricked want revenge, but can't find Fae afterward

**vs. Draconid Remembrance (-1 Suspicious)**
- **Why**: Draconids hoard knowledge and treasure. Orcs want to raid them.
- **Friction Points**: Draconids are too powerful to raid safely
- **Respect**: Grudging. Orcs know Draconids would wipe them out if provoked.

---

### The Ossuarium (Undead)

**Philosophy**: "Death is no longer the end. We are proof. We are patient."

#### Relationships:

**vs. Church of Absolution (-3 War)**
- **Why**: Theological hatred. Church wants all Undead destroyed.
- **Friction Points**: EXISTENCE ITSELF.
- **Historical Grudge**: The entire Sundering. Church blames necromancy. Undead blame Church ignorance.
- **Active Conflict**: Crusades into Bone-Marches, Undead plague-attacks on Church cities

**vs. Verdant Covenant (-2 Hostile)**
- **Why**: Undead violate the natural cycle
- **Friction Points**: Elves want corpses to return to the earth, Undead want to *use* them
- **Historical Grudge**: Undead raid Elven burial groves for fresh corpses
- **Tension**: Elves send rangers to burn Undead territories

**vs. Forge-Guilds (0 Neutral)**
- **Why**: Business is business. Undead pay well.
- **Friction Points**: Dwarves find Undead unsettling but profitable
- **Trade**: Steady. Undead buy equipment, don't complain about prices.

**vs. Scrap-Clans (0 Neutral)**
- **Why**: Mutual indifference
- **Friction Points**: None
- **Dynamic**: Orcs find Undead boring. Undead find Orcs... ephemeral.

**vs. The Wyrd Conclave (+1 Cordial)**
- **Why**: Both factions exist "between" states (Undead between life/death, Fae between worlds)
- **Friction Points**: Fae are chaotic, Undead are orderly
- **Alliance**: Occasional cooperation against "living" factions
- **Respect**: Shared immortality

**vs. Draconid Remembrance (0 Neutral)**
- **Why**: Draconids are too old to fear Undead
- **Friction Points**: Draconids view Undead as "a temporary phenomenon"
- **Tension**: Undead are offended by Draconid dismissiveness

---

### The Wyrd Conclave (Fae)

**Philosophy**: "Reality is negotiable. Everything has a price."

#### Relationships:

**vs. Church of Absolution (-2 Hostile)**
- **Why**: Church hunts Fae-touched individuals
- **Friction Points**: Ideological incompatibility (faith vs. bargains)
- **Historical Grudge**: Fae find Church hilarious (they're so serious!). Church finds Fae terrifying.

**vs. Verdant Covenant (+1 Cordial)**
- **Why**: Shared interest in preserving dimensional overlap
- **Friction Points**: Fae are unpredictable
- **Alliance**: Occasional cooperation, but Elves never fully trust Fae

**vs. Forge-Guilds (-1 Suspicious)**
- **Why**: Dwarves refuse Fae bargains
- **Friction Points**: Dwarves value ironclad contracts. Fae value exploitable loopholes.
- **Tension**: Fae are offended Dwarves won't play their games

**vs. Scrap-Clans (0 Neutral)**
- **Why**: Orcs are boring (too straightforward for good bargains)
- **Friction Points**: Fae trick Orcs occasionally, just for fun

**vs. The Ossuarium (+1 Cordial)**
- **Why**: Shared "outsider" status
- **Friction Points**: Philosophical differences (Fae are chaotic, Undead are methodical)
- **Alliance**: Mutual benefit against living factions

**vs. Draconid Remembrance (+2 Friendly)**
- **Why**: Draconids are old enough to bargain intelligently with Fae
- **Friction Points**: None. Mutual respect for ancient power.
- **Trade**: Knowledge for favors (both are patient enough to wait out long-term bargains)

---

### Draconid Remembrance

**Philosophy**: "We've seen this before. History repeats. We endure."

#### Relationships:

**vs. Church of Absolution (+1 Cordial)**
- **Why**: Church respects ancient power
- **Friction Points**: Draconids know Church doctrine is wrong (but don't correct them)

**vs. Verdant Covenant (+2 Friendly)**
- **Why**: Shared long-term perspective
- **Friction Points**: None
- **Alliance**: Intellectual exchange

**vs. Forge-Guilds (+1 Cordial)**
- **Why**: Shared interest in technology
- **Friction Points**: Draconids withhold "dangerous" knowledge

**vs. Scrap-Clans (-1 Suspicious)**
- **Why**: Orcs want to raid Draconid hoards
- **Friction Points**: Orcs are too short-sighted for Draconid patience

**vs. The Ossuarium (0 Neutral)**
- **Why**: Draconids view Undead as "a phase"
- **Friction Points**: Undead are offended by dismissiveness

**vs. The Wyrd Conclave (+2 Friendly)**
- **Why**: Mutual respect for ancient power
- **Friction Points**: None. Both are immortal and patient.

---

## Changing Relationships (Player Actions)

### How Players Influence Factions

Players start at **0 (Neutral)** with all factions. Actions shift relationships:

**Positive Actions** (+1 per action):
- Complete a faction's mission successfully
- Donate resources (100 Credits or 5 Scrap)
- Defend faction territory from attack
- Return stolen artifact/relic
- Share valuable intelligence

**Negative Actions** (-1 per action):
- Fail a faction's mission
- Kill faction members
- Raid faction territory
- Steal resources
- Break a treaty/bargain

**Major Actions** (±2 relationship):
- Destroy a faction's major settlement
- Assassinate a faction leader (see Iconic NPCs)
- Broker peace between warring factions
- Sabotage faction's strategic objective

---

## Faction Missions (By Relationship Tier)

### At +1 (Cordial)
Factions offer **basic missions**:
- Scout territory (50 Credits)
- Escort caravan (75 Credits)
- Clear Abomination nest (100 Credits)

### At +2 (Friendly)
Factions offer **strategic missions**:
- Sabotage rival faction (150 Credits + rare equipment)
- Retrieve lost relic (200 Credits)
- Assassinate enemy leader (300 Credits + faction support)

### At +3 (Allied)
Factions offer **endgame support**:
- Military reinforcements (NPC allies in missions)
- Safe harbor (free repairs and healing)
- Faction-specific endings (unique campaign conclusions)

---

## Faction War Events

If 2 factions reach **-3 (War)** with each other, the campaign enters a **Faction War Arc**:

**Effects**:
- All missions occur on battlefields (terrain littered with corpses, burning buildings)
- Players must choose a side (neutrality becomes impossible)
- Winning side grants massive rewards
- Losing side is destroyed (removed from campaign)

**Example: Church vs. The Ossuarium War**
- Mission: Defend the Iron Cathedral from Undead siege
- Stakes: If Church loses, Undead raise the entire population as skeletons
- Reward: If Church wins, players gain +3 relationship and Penitent Knight reinforcements

---

## Faction Victory Conditions

If a faction reaches **total dominance** (Allied with players, destroyed all rivals), the campaign ends:

**Church Victory**: "The Age of Absolution"
- Taint is purged, but magic dies. Technological dark age.

**Covenant Victory**: "The Green Harmony"
- World becomes feral paradise. Civilization collapses into druidic communes.

**Forge Victory**: "The Industrial Epoch"
- Dwarves stabilize the Engine. Magic is industrialized. Dystopian technocracy.

**Scrap Victory**: "The Eternal Krush"
- Warlords rule. Might makes right. Brutal but free.

**Bone Victory**: "The Deathless Empire"
- Undead achieve true immortality. Living become irrelevant.

**Fae Victory**: "The Endless Bargain"
- Reality becomes negotiable. Fae rules apply everywhere. Nothing is certain.

**Draconid Victory**: "The Fourth Cycle"
- Draconids trigger controlled Cataclysm. World resets. History repeats.

---

*"Every handshake hides a dagger. Every alliance is temporary. Trust no one."*
