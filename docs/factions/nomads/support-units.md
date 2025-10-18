# Nomad Collective - Support Units
## Penance: Salvagers, Scouts, and Survivors

**Version**: 3.0 Equipment System (Asymmetric)
**Date**: October 16, 2025

The Nomad Collective fields scrappy survivors, fast scouts, and salvage specialists. Each unit embodies nomadic philosophy: mobility, improvisation, and resourcefulness.

---

## NOMAD SUPPORT UNITS OVERVIEW

**Faction-Specific Units** (Choose 1):
1. Salvage Crew (2 Equipment Slots)
2. Outrider Squadron (2 Equipment Slots)
3. Caravan Walker (3 Equipment Slots)

**Note**: Nomads have only 3 support options, reflecting their lean, mobile doctrine. For additional options, hire Neutral Mercenaries (see: Neutral Support Units).

---

## 1. SALVAGE CREW
**Category**: Infantry (Scavenger/Support)
**HP**: 7 | **Movement**: 4 | **Defense**: 1
**Equipment Slots**: 2
**Theme**: Opportunistic scavengers who loot battlefield wreckage and repair allies

### Visual Description
Five nomads wearing mismatched armor scavenged from a dozen factions. Tool belts heavy with wrenches, plasma cutters, and magnetic grapples. They carry collapsible carts loaded with spare parts. Their leader wears goggles made from broken Casket optics. They never stop moving - always looting, always fixing.

### Behavior Deck (4 Cards)

---

#### BATTLEFIELD SALVAGE
**Type**: Utility / Resource Generation
**Priority**: High

**Effect**:
- Salvage Crew moves toward nearest destroyed unit or debris
- If adjacent to wreckage, gain 1 Scrap Token
- Scrap Tokens can be spent for:
  - 2 Scrap = Heal ally 3 HP
  - 3 Scrap = Draw 2 cards
  - 4 Scrap = Summon temporary defensive barricade
- Max 6 Scrap Tokens stored

**Flavor**: "One faction's trash is our treasure."

---

#### FIELD REPAIRS
**Type**: Support / Healing
**Priority**: Critical (when ally within 3 hexes has <15 HP)

**Effect**:
- Crew moves toward wounded ally
- If adjacent, spend 2 Scrap Tokens (or take 2 damage if no Scrap)
- Target ally recovers 5 HP and draws 1 card
- Remove 1 Component Damage from target (if any)

**Flavor**: "Hold still! This'll hurt, but you'll thank me later."

---

#### IMPROVISED WEAPON
**Type**: Attack / Utility
**Priority**: Medium (when Crew has 3+ Scrap Tokens)

**Effect**:
- Crew assembles weapon from salvaged parts
- Spend 3 Scrap Tokens
- Attack nearest enemy for 6 damage
- Weapon breaks after use (one-time attack)

**Flavor**: "It's ugly, but it'll kill you just fine."

---

#### SCRAP ARMOR
**Type**: Defense / Utility
**Priority**: Medium (when Crew has 2+ Scrap Tokens)

**Effect**:
- Crew welds scrap metal to themselves or adjacent ally
- Spend 2 Scrap Tokens
- Target gains +3 Defense until end of round
- Armor is permanent until damage removes it

**Flavor**: "Not pretty, but neither are corpses."

---

#### DESPERATE SALVAGE
**Type**: Survival / Resource
**Priority**: Critical (when Crew has 0 Scrap Tokens AND ally needs healing)

**Effect**:
- Crew scavenges their own equipment for parts
- Crew takes 3 damage (self-harm for resources)
- Gain 2 Scrap Tokens immediately
- Can immediately use Field Repairs if ally within range

**Flavor**: "We'll rip the parts from our own backs if we have to."

---

#### SCRAP HOARD (Default)
**Type**: Passive / Movement
**Priority**: Low (when no urgent needs)

**Effect**:
- Crew moves 4 hexes toward nearest unclaimed wreckage or debris
- If no wreckage exists, move toward nearest ally (stay in support range)
- Automatically collect 1 Scrap Token if ending turn adjacent to wreckage
- Maintain readiness for Field Repairs or Salvage

**Flavor**: "Always collecting. Always prepared."

---

### Command Response
- **RALLY**: Move up to 4 hexes toward nearest wreckage. Gain 1 Scrap Token if wreckage within 2 hexes.
- **ATTACK**: Cannot attack without Scrap. If 3+ Scrap, spend 3 to attack target for 6 damage.
- **DEFEND**: Weld defensive position. +3 Defense, gain 1 Scrap Token from surrounding debris.
- **HOLD**: Frantically loot everything. Gain 2 Scrap Tokens.

### Special Ability: SCAVENGER ECONOMY
**Passive**: At end of each round, if any unit (friend or foe) was destroyed this round, Salvage Crew automatically gains 1 Scrap Token.

**Synergy**: Works with Nomad "Improvisation" mechanic - Scrap Tokens count as improvisation resources.

### Tactical Use
- Resource generation engine
- Mobile healing support
- Benefits from prolonged battles (more wreckage = more Scrap)
- Weak in combat but incredible utility

---

## 2. OUTRIDER SQUADRON
**Category**: Fast Attack (Cavalry)
**HP**: 6 | **Movement**: 7 | **Defense**: 0
**Equipment Slots**: 2
**Theme**: Lightning-fast scouts on salvaged motorcycles/hoverbikes

### Visual Description
Three nomads on jerry-rigged motorcycles - engines cobbled from Casket reactors, frames welded from scrap metal, tires mismatched. They wear leather jackets painted with tribal symbols. Goggles, scarves, and bandanas hide their faces. Weapons strapped everywhere. They never stop moving - circling, flanking, harassing. Engines roar constantly.

### Behavior Deck (4 Cards)

---

#### HIT AND RUN
**Type**: Attack / Mobile
**Priority**: High

**Effect**:
- Outriders move full speed (7 hexes) toward enemy
- If within 3 hexes of enemy, attack for 4 damage
- Immediately move 3 hexes in any direction (disengage)
- Cannot be counterattacked (too fast)

**Flavor**: "Blink and you'll miss us. Blink twice and you're dead."

---

#### FLANK MANEUVER
**Type**: Attack / Tactical
**Priority**: High (when enemy has rear arc exposed)

**Effect**:
- Outriders move at high speed to enemy's rear arc
- Attack from behind for 6 damage
- If this kills target, Outriders gain +1 movement permanently this battle (adrenaline)
- Enemy cannot react to rear attack (surprised)

**Flavor**: "Never saw us coming. Never will."

---

#### SMOKE SCREEN
**Type**: Utility / Escape
**Priority**: Critical (when Outriders HP ≤ 3)

**Effect**:
- Outriders deploy smoke grenades
- Create 3-hex smoke cloud (blocks LOS)
- Immediately move 5 hexes through smoke
- All allies in smoke gain +2 Defense until smoke clears (2 turns)

**Flavor**: "Can't hit what you can't see!"

---

#### SCOUTING RUN
**Type**: Utility / Reconnaissance
**Priority**: Medium (when no enemies within 5 hexes)

**Effect**:
- Outriders circle battlefield at high speed
- Reveal all hidden enemies within 8 hexes
- Reveal 1 random card from each enemy hand within 6 hexes
- Draw 1 card (intelligence gathered)

**Flavor**: "Eyes everywhere. Know everything."

---

#### MOMENTUM STRIKE
**Type**: Attack / Burst Damage
**Priority**: High (when Outriders have moved 10+ hexes this turn)

**Effect**:
- Trigger Maximum Mobility bonus (moved 10+ hexes)
- Attack nearest enemy for 7 damage (4 base + 3 momentum bonus)
- After attack, move 3 additional hexes (disengage)
- Gain +1 permanent movement for rest of battle if this kills target

**Flavor**: "Pure kinetic fury. Can't stop, won't stop!"

---

#### DEFENSIVE CIRCLE (Default)
**Type**: Movement / Patrol
**Priority**: Low (when no high-priority actions available)

**Effect**:
- Outriders circle friendly Casket or objective at 5-hex radius
- Movement: 7 hexes in circular pattern
- Ready to intercept any approaching enemies
- Attack any enemy entering 3-hex radius for 4 damage (reaction)

**Flavor**: "Always moving. Always watching. Always ready."

---

### Command Response
- **RALLY**: Move up to 7 hexes at breakneck speed. Engines screaming.
- **ATTACK**: Attack target for 5 damage, then move 3 hexes away (can't catch us).
- **DEFEND**: Outriders refuse (their doctrine is "never stop moving"). Execute Hit and Run instead.
- **HOLD**: Circle position defensively. Gain +2 Defense, attack any enemy entering 3-hex radius.

### Special Ability: MAXIMUM MOBILITY
**Passive**: Outriders ignore difficult terrain. They can move through enemy hexes without stopping (weave through legs). They cannot be slowed or immobilized by any effect.

**Triggered**: If Outriders move 10+ hexes in single turn, next attack deals +3 damage (momentum strike).

### Tactical Use
- Hit-and-run harassment
- Fastest unit in game (7 movement!)
- Fragile (0 Defense, 6 HP)
- Excellent objective grabbers
- Synergizes with Nomad mobility focus

---

## 3. CARAVAN WALKER
**Category**: Heavy Support (Mobile Base)
**HP**: 18 | **Movement**: 2 | **Defense**: 3
**Equipment Slots**: 3
**Theme**: Massive six-legged transport carrying supplies, refugees, and weapons

### Visual Description
A towering mechanical walker - twenty feet tall, six hydraulic legs, cobbled together from salvaged cargo haulers and mining equipment. The hull is painted with Nomad tribal symbols and covered in prayer flags. Refugees ride on external platforms. Supply crates lashed to every surface. A massive cannon (clearly scavenged from destroyed Casket) mounted on top. It moves slow but unstoppable.

### Behavior Deck (4 Cards)

---

#### SUPPLY DROP
**Type**: Support / Buff
**Priority**: High

**Effect**:
- Walker deploys supply cache in current hex
- All allies within 3 hexes immediately:
  - Draw 2 cards
  - Recover 3 HP
  - Gain +1 SP regeneration for 2 turns
- Cache remains for 3 turns (allies can return for supplies)

**Flavor**: "Fresh ammo, medical kits, rations. Take what you need."

---

#### COVERING FIRE
**Type**: Attack / Support
**Priority**: Medium

**Effect**:
- Walker fires scavenged cannon at enemy position
- Attack 1 target within 6 hexes for 5 damage
- All allies within 3 hexes of Walker gain +1 damage to next attack (emboldened by fire support)
- Walker takes 1 damage (recoil strain on old joints)

**Flavor**: "BOOM. Problem solved."

---

#### MOBILE FORTRESS
**Type**: Defense / Zone Control
**Priority**: High (when 2+ allies within 3 hexes)

**Effect**:
- Walker stops moving, deploys stabilizers
- Walker and all allies within 3 hexes gain +2 Defense
- Create 3-hex aura: enemies entering aura take 2 damage (defensive turrets)
- Walker cannot move while in fortress mode

**Flavor**: "Hunker down. Let them come to us."

---

#### EMERGENCY EVACUATION
**Type**: Utility / Rescue
**Priority**: Critical (when ally within 2 hexes has <5 HP)

**Effect**:
- Walker extends mechanical arm to grab ally
- Pull ally adjacent to Walker (teleport effect)
- Heal ally for 4 HP (emergency medical treatment)
- Ally gains +2 Defense while adjacent to Walker (protected by hull)

**Flavor**: "Get in! We're leaving!"

---

#### DEPLOY CARGO
**Type**: Utility / Summoning
**Priority**: High (when Walker has 2+ Cargo Tokens AND needs reinforcements)

**Effect**:
- Walker spends 2 Cargo Tokens
- Summon 3 Nomad Infantry at adjacent hexes
- Nomad Infantry: 5 HP, 3 movement, 1 Defense, 3 damage attack
- Infantry last for 3 turns, then return to Walker (cargo reclaimed)

**Flavor**: "Everyone fights! No passengers!"

---

#### STEADY ADVANCE (Default)
**Type**: Movement / Support
**Priority**: Low (when no urgent actions needed)

**Effect**:
- Walker moves 2 hexes toward nearest ally or objective
- Maintain Mobile Supply Base aura (allies within adjacent hexes gain bonuses)
- Automatically heal 2 HP to self (self-repair systems activate during movement)
- Ready to deploy supplies or provide covering fire next turn

**Flavor**: "Slow and steady. We'll get there."

---

### Command Response
- **RALLY**: Move up to 2 hexes (slow but steady). Deploy supplies in vacated hex.
- **ATTACK**: Fire cannon at target (5 damage). All allies within 3 hexes draw 1 card.
- **DEFEND**: Deploy Mobile Fortress. +4 Defense, cannot move, aura range +1 hex.
- **HOLD**: Fully stop. Recover 5 HP (self-repair systems). Deploy supply cache.

### Special Ability: MOBILE SUPPLY BASE
**Passive**: Any ally adjacent to Caravan Walker gains:
- +1 Defense (protected by hull)
- +1 SP regeneration (access to supplies)
- Can spend 1 SP to draw 1 card (rummage through supplies)

**Caravan Cargo**: Walker carries 3 "Cargo Tokens". Can spend tokens for:
- 1 Token = Heal ally 5 HP
- 2 Tokens = Summon 3 Nomad Infantry (5 HP, 3 movement, 1 Defense, last 3 turns)
- 3 Tokens = Deploy heavy weapon emplacement (stationary turret, 8 HP, 5 damage attack)

Cargo replenishes at start of each mission.

### Tactical Use
- Mobile supply depot
- Zone control through buffs
- Slow but tanky
- Synergizes with Nomad "community survival" theme
- Turns allies into army

---

## ASYMMETRIC DESIGN NOTES

### Why Only 3 Units?
Nomads are lean, mobile faction. They don't have standing armies. They improvise, scavenge, and adapt. Three units reflects this:
- **Salvage Crew**: Resourcefulness
- **Outriders**: Mobility
- **Caravan Walker**: Community

### Neutral Mercenaries
Nomads are encouraged to hire **Neutral Mercenary Units** (see: Neutral Support Units file) to supplement their forces. This reflects their philosophy:
- "Anyone can join the Collective"
- "Credits buy loyalty"
- "Adapt or die"

---

## DECK BUILDING EXAMPLES

### Example: Nomad Scout Casket with Outrider Squadron

**Total Deck Construction**:
- 10 Universal Core (mandatory)
- 6 Nomad Faction Core (mandatory)
- 6 Twin Pistols (weapon, 1 slot)
- **Outrider Squadron** (2 slots)
- 2 Nomad Tactics (choose 2)

**Total**: 24 cards, 1 Outrider Squadron

**Playstyle**: Maximum speed. Casket moves 5, Outriders move 7. Hit-and-run everywhere.

### Example: Nomad Heavy Casket with Caravan Walker

**Total Deck Construction**:
- 10 Universal Core
- 6 Nomad Faction Core
- 6 Assault Rifle (weapon, 1 slot)
- **Caravan Walker** (3 slots)
- 2 Nomad Tactics

**Total**: 24 cards, 1 Caravan Walker

**Playstyle**: Mobile fortress duo. Walker supplies, Casket attacks. Slow but unstoppable.

---

## FACTION SYNERGIES

### Improvisation + Salvage Crew
- Nomad core mechanic generates improv tokens
- Salvage Crew generates Scrap tokens
- Both create resource economy

### Movement Mastery + Outriders
- Nomad Caskets have +1 movement
- Outriders have 7 movement
- Both units dance around enemies

### Supply Cache + Caravan Walker
- Nomad Caskets can "Emergency Supply" (draw cards)
- Walker deploys physical supply caches
- Entire army runs on logistics

---

**END OF DOCUMENT**

*"We survive because we move. We thrive because we share. Join the Collective."* — Nomad Proverb
