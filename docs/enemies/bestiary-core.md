# Bestiary: Core Enemies
## Penance: Campaign System

**Version**: 3.0
**Last Updated**: October 14, 2025

---

## Overview

This bestiary contains **15 core enemies** for campaign missions, settlement defense events, and random encounters. Enemies use **player-like mechanics** (HP deck, SP economy) but with **simplified AI behavior cards** (draw a card, execute its instructions).

**Enemy Categories**:
- **Swarm (3-5 HP)**: Many weak enemies. Simple AI.
- **Elite (15-25 HP)**: 1-2 per mission. Medium complexity AI.
- **Boss (30-60 HP)**: Mission capstone. Complex AI with phases.

**AI System**: Enemies draw from **behavior decks** each turn. Cards have "If-Then" logic (e.g., "If enemy within 2 hexes, attack. Else, move closer").

---

## Enemy Stat Block Format

```
NAME
Type: Swarm | Elite | Boss
HP Deck: X cards
Movement: X hexes
Armor: X
SP: X

Behavior Deck (Y cards):
- Card Name (× copies): If-Then logic

Special Abilities: Passive effects

Loot (on death): Credits, Scrap, Equipment rolls
```

---

## SWARM ENEMIES (3-5 HP)

### 1. TAINTED RAT SWARM

**Type**: Swarm
**HP Deck**: 3 cards (Universal Core only)
**Movement**: 4 hexes
**Armor**: 0
**SP**: 2

**Behavior Deck (3 cards)**:
- **"Swarm Tactics" (×2)**:
  - If 2+ allies within 2 hexes, move toward nearest enemy and attack for 1d6 damage.
  - Else, move toward nearest ally.
- **"Panic Scatter" (×1)**:
  - If below 2 HP, move away from all enemies (flee).

**Special Abilities**:
- **Diseased Bite**: When attack hits, target rolls Willpower Save (1d6+Grit, need 4+) or gain 1 Taint.

**Tactics**: Deploy 5-10 rats. Swarm from multiple directions. Die easily but overwhelm with numbers.

**Loot**: 5 Credits per rat. 1/10 chance of 1 Scrap.

---

### 2. CORRUPTED VILLAGER

**Type**: Swarm
**HP Deck**: 5 cards (Universal Core only)
**Movement**: 3 hexes
**Armor**: 0
**SP**: 3

**Behavior Deck (5 cards)**:
- **"Shambling Advance" (×3)**:
  - Move toward nearest enemy.
  - If adjacent, attack for 2d6 damage.
- **"Desperate Lunge" (×1)**:
  - Move 4 hexes toward nearest enemy (sprint).
  - Attack for 3d6 damage, then take 1 damage (self-harm).
- **"Tainted Scream" (×1)**:
  - All enemies within 3 hexes make Willpower Save (4+) or lose 1 SP next turn (fear effect).

**Special Abilities**:
- **Engine-Touched**: When killed, explodes for 1d6 damage to all adjacent units (Taint burst).

**Tactics**: Deploy 3-5 villagers. Mix with rats for chaotic combat. Scream disrupts player SP economy.

**Loot**: 10 Credits per villager. 1/5 chance of torn clothing scrap (flavor item).

---

### 3. SCRAP DRONE

**Type**: Swarm
**HP Deck**: 4 cards (Universal Core only)
**Movement**: 5 hexes (flying)
**Armor**: 1
**SP**: 4

**Behavior Deck (4 cards)**:
- **"Patrol" (×2)**:
  - If no enemies within 6 hexes, move in random direction.
  - If enemy within 6 hexes, move toward and attack for 1d6 damage.
- **"Self-Destruct" (×1)**:
  - If below 2 HP, move adjacent to nearest enemy and explode for 3d6 damage to all adjacent (Drone destroyed).
- **"Repair Protocol" (×1)**:
  - If allied Scrap Drone within 2 hexes, both recover 1 card from discard.

**Special Abilities**:
- **Flying**: Ignores terrain. Can move over obstacles.
- **Construct**: Immune to Taint and Morale effects.

**Tactics**: Deploy 4-6 drones. They patrol, harass with ranged attacks, then kamikaze when low HP. Repair each other if grouped.

**Loot**: 15 Credits, 1 Scrap per drone (guaranteed - they're made of scrap).

---

## ELITE ENEMIES (15-25 HP)

### 4. BANDIT RAIDER

**Type**: Elite
**HP Deck**: 15 cards (10 Universal + 5 Equipment)
**Movement**: 4 hexes
**Armor**: 1
**SP**: 4

**Behavior Deck (15 cards)**:
- **"Aggressive Strike" (×5)**:
  - If within melee range, attack for 3d6 damage.
  - Else, move toward nearest enemy.
- **"Flank" (×3)**:
  - Move to target's rear arc if possible.
  - If in rear arc, attack for 4d6 damage (+1d6 bonus).
- **"Defend" (×2)**:
  - If below 8 HP, gain +2 Defense this turn. Do not move.
- **"Grenade Throw" (×2)**:
  - If 3-6 hexes from enemy, throw grenade for 4d6 damage, ignoring cover.
  - Cannot use if adjacent to enemy.
- **"Retreat" (×2)**:
  - If below 5 HP and no allies within 4 hexes, move away from enemies (flee).
- **"Rally Cry" (×1)**:
  - All allied bandits within 4 hexes gain +1 damage this turn.

**Special Abilities**:
- **Scavenger Armor**: When hit, roll 1d6. On 6, reduce damage by 2 (lucky deflection off scrap armor).

**Tactics**: Bandits use hit-and-run tactics. Flank when possible, throw grenades at range, retreat when wounded. Deploy 1-2 per mission.

**Loot**: 50 Credits, 1d3 Scrap, roll on Equipment Table (1d20, 15+ = loot 1 weapon).

---

### 5. BANDIT CAPTAIN

**Type**: Elite (Leader)
**HP Deck**: 20 cards (10 Universal + 6 Faction Core + 4 Equipment)
**Movement**: 4 hexes
**Armor**: 2
**SP**: 5

**Behavior Deck (20 cards)**:
- **"Commanding Strike" (×6)**:
  - Attack for 4d6 damage.
  - If hit, one allied bandit within 4 hexes gains +2 damage on their next attack.
- **"Tactical Repositioning" (×4)**:
  - Move to position with most allies within 2 hexes.
  - If 2+ allies adjacent, gain +1 Defense until next turn (shield wall).
- **"Inspire Troops" (×3)**:
  - All allied bandits within 4 hexes gain +1 SP next turn.
  - Captain does not attack this turn (leadership action).
- **"Execute the Weak" (×2)**:
  - Attack nearest enemy with lowest HP for 6d6 damage (execute).
  - If kill is successful, all allies gain +1 Morale (simulated boost).
- **"Desperate Gambit" (×2)**:
  - If below 10 HP, attack for 5d6 damage and take 2 damage (reckless aggression).
- **"Tactical Retreat" (×2)**:
  - If below 5 HP, move away from enemies. All allies also retreat 2 hexes (coordinated withdrawal).
- **"Smoke Grenade" (×1)**:
  - Create 3-hex smoke cloud. All attacks through smoke have -2 to hit. Lasts 2 turns.

**Special Abilities**:
- **Leader Aura**: All bandits within 4 hexes gain +1 to Attack rolls.
- **Combat Veteran**: Immune to forced movement (cannot be pushed/pulled).

**Tactics**: Captain buffs allies, coordinates attacks, and fights strategically. Always deploy with 3-5 Bandit Raiders. Kill Captain first to demoralize bandits.

**Loot**: 100 Credits, 2d3 Scrap, roll twice on Equipment Table, 1/5 chance of "Captain's Insignia" (Relic: +1 to Leadership rolls).

---

### 6. TAINTED OGRE

**Type**: Elite (Brute)
**HP Deck**: 25 cards (12 Universal + 8 Equipment + 5 Taint-specific)
**Movement**: 3 hexes
**Armor**: 3 (thick hide)
**SP**: 4

**Behavior Deck (25 cards)**:
- **"Brutal Smash" (×8)**:
  - Attack for 5d6 damage.
  - If damage exceeds 6, push target 2 hexes backward (knockback).
- **"Enraged Charge" (×5)**:
  - Move 4 hexes toward nearest enemy (sprint).
  - If reach target, attack for 6d6 damage and gain 2 Heat (overexertion).
- **"Regenerate" (×3)**:
  - If below 15 HP, recover 2 cards from discard.
  - Gain 1 Taint (corruption accelerates healing).
- **"Ground Slam" (×3)**:
  - AOE attack: All enemies within 2 hexes take 4d6 damage.
  - Ogre takes 1 Heat (exertion).
- **"Intimidating Roar" (×2)**:
  - All enemies within 4 hexes make Willpower Save (5+) or lose 2 SP next turn (fear).
- **"Berserk Rage" (×2)**:
  - If below 10 HP, gain +3 damage and +1 Movement for rest of combat.
  - Ogre cannot use defensive actions (blind fury).
- **"Cannibalize" (×1)**:
  - If allied corpse within 2 hexes, consume it. Recover 5 cards from discard.
  - Gain 2 Taint. All enemies make Morale check (lose 1 Morale on fail).
- **"Throw Boulder" (×1)**:
  - Ranged attack (4-8 hexes): Deal 4d6 damage, ignore cover.
  - Can only use once per combat (no more boulders).

**Special Abilities**:
- **Thick Hide**: Reduce all damage by 3 (before Defense rolls).
- **Taint Regeneration**: At end of turn, if Ogre has 5+ Taint, recover 1 card from discard.
- **Massive**: Occupies 2 hexes (large creature). Cannot be forced to move by units smaller than Caskets.

**Tactics**: Ogre is slow but devastating. Charges into melee, smashes everything, regenerates damage. Focus fire to kill before it reaches you. Deploy 1 per mission (always boss of area).

**Loot**: 150 Credits, 3d3 Scrap, roll on Equipment Table, 1/3 chance of "Tainted Ogre Hide" (crafting material: +2 Armor plating).

---

### 7. SCRAP GOLEM

**Type**: Elite (Construct)
**HP Deck**: 20 cards (15 Universal + 5 Equipment)
**Movement**: 3 hexes
**Armor**: 4 (metal plating)
**SP**: 3

**Behavior Deck (20 cards)**:
- **"Hydraulic Punch" (×6)**:
  - Attack for 4d6 damage.
  - If damage exceeds 5, target Component Damage +1 (armor-piercing).
- **"Defensive Stance" (×4)**:
  - Do not move. Gain +3 Defense this turn.
  - If attacked in melee while in stance, deal 2d6 damage to attacker (counter).
- **"Repair Subroutine" (×3)**:
  - If below 10 HP, recover 3 cards from discard.
  - Requires 1 Scrap from battlefield (consumes terrain scrap or ally corpse).
- **"Ram" (×2)**:
  - Move 4 hexes in straight line.
  - All enemies in path take 3d6 damage and are pushed aside (trampled).
- **"Overload" (×2)**:
  - If below 5 HP, next attack deals 7d6 damage.
  - Golem takes 3 damage after attack (overheating).
- **"Summon Drones" (×2)**:
  - Spawn 2 Scrap Drones adjacent to Golem.
  - Can only use once per combat.
- **"Shutdown" (×1)**:
  - If no enemies within 6 hexes, enter hibernation mode.
  - Recover 5 cards from discard. Golem does not activate next turn (recharging).

**Special Abilities**:
- **Construct**: Immune to Taint, Morale, Willpower effects. Cannot be Corrupted.
- **Heavy Armor**: Reduce all damage by 4 (before Defense rolls).
- **Repair Protocol**: If Scrap Drones are within 2 hexes at end of turn, recover 1 card from discard.

**Tactics**: Golem is defensive tank. Stands ground, counters melee attacks, repairs itself. Summons drones for support. Hard to kill but slow. Deploy 1 per mission (guardian of ruins).

**Loot**: 200 Credits, 5 Scrap (guaranteed - made of metal), roll on Equipment Table, 1/4 chance of "Golem Core" (Relic: Casket gains +1 Armor permanently).

---

### 8. ENGINE WRAITH

**Type**: Elite (Supernatural)
**HP Deck**: 12 cards (8 Universal + 4 Taint-specific)
**Movement**: 6 hexes (teleport)
**Armor**: 0
**SP**: 5

**Behavior Deck (12 cards)**:
- **"Phase Strike" (×4)**:
  - Teleport up to 6 hexes (ignores terrain/obstacles).
  - If teleport adjacent to enemy, attack for 3d6 damage + 1 Taint to target.
- **"Taint Drain" (×3)**:
  - Attack for 2d6 damage.
  - If target has 3+ Taint, recover 2 cards from discard (feeding on corruption).
  - Target gains 1 Taint.
- **"Void Shift" (×2)**:
  - Move 8 hexes (teleport).
  - Leave behind "Void Echo" (3 HP minion) at departure location. Echo attacks once for 2d6 then disappears.
- **"Taint Pulse" (×2)**:
  - AOE: All enemies within 4 hexes gain 2 Taint.
  - Wraith recovers 1 card per enemy affected.
- **"Reality Anchor" (×1)**:
  - Target enemy cannot teleport, be forced to move, or use movement abilities for 2 turns.
  - Target gains 1 Taint per turn while anchored.

**Special Abilities**:
- **Ethereal**: Cannot be targeted by melee attacks unless Wraith attacked that target this turn (becomes solid momentarily).
- **Taint Incarnate**: Immune to Taint and Corruption. Gains +1 damage for each point of Taint on target (max +5).
- **Death Explosion**: When killed, all enemies within 3 hexes gain 3 Taint.

**Tactics**: Wraith teleports constantly, never staying in one place. Drains life, spreads Taint, leaves echoes behind. Difficult to pin down. Kill fast before Taint accumulates. Deploy 1 per mission (haunts Engine ruins).

**Loot**: 100 Credits, 0 Scrap (ethereal, no physical form), roll on Loot Table, guaranteed 1 Soulstone Fragment (wraith was trapped soul).

---

## BOSS ENEMIES (30-60 HP)

### 9. TAINTED LEVIATHAN

**Type**: Boss (Monster)
**HP Deck**: 40 cards (20 Universal + 15 Equipment + 5 Taint-specific)
**Movement**: 4 hexes (massive stride)
**Armor**: 5 (armored hide)
**SP**: 5

**Phases**:
- **Phase 1 (40-25 HP)**: Basic attacks
- **Phase 2 (24-10 HP)**: Enraged (+2 damage all attacks, +1 Movement)
- **Phase 3 (9-0 HP)**: Berserk (AOE attacks, regeneration)

**Behavior Deck (40 cards - Phase 1)**:
- **"Crushing Bite" (×10)**:
  - Attack for 6d6 damage.
  - If damage exceeds 8, target gains "Bleeding" (lose 1 card per turn for 3 turns).
- **"Tail Sweep" (×6)**:
  - AOE: All enemies in rear 3 hexes take 4d6 damage and are pushed 2 hexes backward (knockback).
- **"Charge" (×5)**:
  - Move 6 hexes in straight line.
  - All enemies in path take 5d6 damage and are trampled (knocked prone).
- **"Regenerate" (×4)**:
  - Recover 3 cards from discard.
  - Gain 1 Taint.
- **"Roar" (×3)**:
  - All enemies make Willpower Save (6+) or lose 3 SP next turn (terror).
- **"Focus Fire" (×2)**:
  - Attack enemy with highest damage dealt to Leviathan for 8d6 damage (revenge).

**Phase 2 Additions (24-10 HP)** - Add these 5 cards to deck when reshuffling:
- **"Enraged Frenzy" (×2)**:
  - Attack twice in one turn (2 × 6d6 damage). Gain 2 Heat.
- **"Taint Burst" (×2)**:
  - AOE: All enemies within 4 hexes gain 2 Taint and take 3d6 damage.
- **"Desperate Lunge" (×1)**:
  - Move 8 hexes toward nearest enemy. Attack for 10d6 damage. Leviathan takes 3 damage (overexertion).

**Phase 3 Additions (9-0 HP)** - Add these 5 cards:
- **"Death Throes" (×2)**:
  - AOE: All enemies within 6 hexes take 5d6 damage.
  - Leviathan recovers 5 cards from discard (desperation healing).
- **"Final Stand" (×2)**:
  - Attack nearest enemy for 12d6 damage.
  - If kill is successful, Leviathan gains +3 damage permanently (stacks).
- **"Apocalyptic Roar" (×1)**:
  - All enemies make Willpower Save (7+) or immediately reshuffle deck with +2 Damage cards (mental attack).

**Special Abilities**:
- **Massive**: Occupies 4 hexes (huge creature). Cannot be moved by Caskets.
- **Armored Hide**: Reduce all damage by 5 (before Defense rolls).
- **Taint Regeneration**: At end of turn, recover 1 card per 3 Taint on battlefield (absorbs corruption).
- **Death Explosion**: When killed, all enemies within 6 hexes gain 5 Taint and take 8d6 damage (final Taint burst).

**Tactics**: Leviathan is slow but devastating. Charges, bites, regenerates constantly. Gets more dangerous as wounded. Focus fire, manage Taint, use terrain for cover. Deploy as mission climax boss.

**Loot**: 500 Credits, 8d6 Scrap, roll 3 times on Equipment Table, guaranteed Legendary item: "Leviathan Fang" (Weapon: 6 cards, 8 damage melee attacks, gain 1 Taint per hit).

---

### 10. ROGUE CASKET (Enemy Pilot)

**Type**: Boss (Rival Pilot)
**HP Deck**: 30 cards (10 Universal + 12 Primary + 6 Secondary + 2 Tactics)
**Movement**: 5 hexes (Medium Casket)
**Armor**: 2
**SP**: 5

**Behavior Deck (30 cards)** - Uses player mechanics:
- **10× Universal Core cards** (MOVE, SPRINT, BRACE, etc.)
- **12× Primary Weapon cards** (faction-specific, randomize)
- **6× Secondary Equipment cards** (Shield, Repair Kit, etc.)
- **2× Tactics** (chosen from enemy faction)

**AI Logic** (Draw 6 cards per turn, play best 3):
1. **If below 10 HP**: Prioritize defensive cards (BRACE, Repair Kit, Shield).
2. **If enemy within melee range**: Play Primary Weapon attacks.
3. **If enemy 3-6 hexes away**: Move closer OR use ranged equipment.
4. **If enemy 7+ hexes away**: SPRINT toward enemy.
5. **If Heat 5+**: Play low-Heat cards or cooling abilities.

**Special Abilities**:
- **Player Mechanics**: Uses full Casket rules (Component Damage, Heat, SP economy, deck reshuffle).
- **Faction Traits**: Roll randomly for faction (Church/Dwarves/Ossuarium/Elves) and apply faction bonuses.
- **Veteran Pilot**: Starts with Grit 2 (+2 to Willpower Saves).

**Tactics**: Rogue Casket fights like a player. Manages SP, uses cover, flanks, retreats when low HP. Most challenging non-boss enemy. Deploy 1 as mission boss or rival encounter.

**Loot**: 300 Credits, 4d6 Scrap, loot entire enemy deck (30 cards - players can salvage enemy equipment), roll on Legendary Table.

---

### 11. BONELORD THRESH (Faction Boss)

**Type**: Boss (Ossuarium Champion)
**HP Deck**: 50 cards (15 Universal + 20 Faction Core + 10 Equipment + 5 Tactics)
**Movement**: 4 hexes
**Armor**: 3
**SP**: 5

**Phases**:
- **Phase 1 (50-35 HP)**: Summons undead minions
- **Phase 2 (34-15 HP)**: Taint corruption attacks
- **Phase 3 (14-0 HP)**: Resurrection + AOE corruption

**Behavior Deck (50 cards - Phase 1)**:
- **"Corruption Strike" (×12)**:
  - Attack for 5d6 damage + 2 Taint.
  - If kill is successful, recover 3 cards from discard (feeding on death).
  - Add 1 "Decay" card to Thresh's deck (Ossuarium mechanic).
- **"Raise Dead" (×8)**:
  - Summon 3 Bone Thralls (5 HP each) adjacent to Thresh.
  - Can only summon if corpses on battlefield (consume 1 corpse per 3 Thralls).
- **"Bone Armor" (×6)**:
  - Gain +3 Armor this turn. Do not move.
  - If attacked while armored, attacker gains 1 Taint (necrotic backlash).
- **"Necrotic Bolt" (×5)**:
  - Ranged attack (4-8 hexes): Deal 4d6 damage + 2 Taint.
  - Target makes Willpower Save (5+) or gain "Curse" (all attacks against cursed target deal +1 damage for 3 turns).
- **"Move" (×5)**: Standard movement.
- **"Defend" (×4)**: Gain +2 Defense this turn.

**Phase 2 Additions (34-15 HP)** - Add these 8 cards:
- **"Necrotic Surge" (×4)**:
  - Attack for 6d6 damage + 3 Taint.
  - If target has 5+ Taint, recover 3 cards from discard (feeding on corruption).
  - Target gains "Bleeding" (lose 1 card per turn for 3 turns).
- **"Mass Raise Dead" (×2)**:
  - Summon 6 Bone Thralls adjacent to Thresh.
  - All Thralls gain +1 damage for rest of combat (empowered undead).
- **"Corruption Pulse" (×2)**:
  - Ranged AOE (4-hex radius): All enemies take 3d6 damage + 2 Taint.
  - Thresh recovers 1 card per enemy with 5+ Taint affected.

**Phase 3 Additions (14-0 HP)** - Add these 7 cards:
- **"Resurrection" (×1)**:
  - When Thresh would be defeated (0 HP), reshuffle all cards from discard back into deck.
  - Thresh returns with 15 HP.
  - Can only trigger once per battle.
- **"Apocalyptic Harvest" (×3)**:
  - AOE: All enemies within 8 hexes take 5d6 damage and gain 3 Taint.
  - Thresh recovers 2 cards per enemy hit.
- **"The Ledger's Command" (×3)**:
  - All Bone Thralls on battlefield explode for 4d6 damage (sacrifice).
  - For each Thrall sacrificed, Thresh recovers 3 cards from discard.

**Special Abilities**:
- **Ossuarium Faction**: Uses Decay cards (negative effects when drawn) instead of Damage cards.
- **Necromantic Aura**: At end of turn, if 3+ corpses on battlefield, summon 1 Bone Thrall automatically (no action required).
- **The Ledger**: When Thresh kills an enemy, write their name in The Ledger. Gain +1 damage permanently per name (stacks infinitely).
- **Undying**: When killed, has 50% chance to resurrect at 10 HP (roll 1d6, 4+ = resurrect). Can only trigger once.

**Tactics**: Thresh summons waves of undead, spreads Taint corruption, feeds on highly corrupted enemies (5+ Taint), gets stronger with every kill. Focus fire to burn through HP fast. Kill Bone Thralls to deny corpses. Deploy as Ossuarium faction boss.

**Loot**: 600 Credits, 10d6 Scrap, roll 4 times on Equipment Table, guaranteed Legendary: "The Ledger (Relic)" - Write enemy name after kill, gain +1 damage permanently. Max 10 names. Cursed item (gain 1 Taint per name).

---

## SUPPORT ENEMIES (Special)

### 12. TAINTED WOLF PACK

**Type**: Swarm (Pack Tactics)
**HP Deck**: 5 cards each
**Movement**: 5 hexes
**Armor**: 0
**SP**: 4

**Behavior Deck (5 cards per wolf)**:
- **"Pack Attack" (×3)**:
  - If 2+ wolves adjacent to same enemy, all attack together for combined 4d6 damage (pack tactics).
  - If solo, move toward nearest ally wolf.
- **"Lunge" (×1)**:
  - Move 6 hexes toward nearest enemy (sprint).
  - Attack for 3d6 damage, gain 1 Heat.
- **"Howl" (×1)**:
  - All allied wolves gain +1 Movement and +1 damage next turn (coordination).

**Special Abilities**:
- **Pack Tactics**: If 2+ wolves attack same target, combine damage dice (3 wolves = 6d6 total).
- **Fast**: Movement 5 (faster than Caskets).

**Tactics**: Wolves coordinate attacks, flank, surround prey. Deploy 4-6 as pack. Kill one at a time to reduce pack bonus.

**Loot**: 20 Credits per wolf, 1/5 chance of wolf pelt (flavor item).

---

### 13. CHURCH ZEALOT

**Type**: Elite (Fanatic)
**HP Deck**: 18 cards (10 Universal + 6 Church Core + 2 Equipment)
**Movement**: 4 hexes
**Armor**: 1
**SP**: 5

**Behavior Deck (18 cards)**:
- **"Blood Offering" (×4)**:
  - Discard 2 cards (self-harm).
  - Next attack deals +3 damage, ignores 1 Defense.
- **"Martyrdom Protocol" (×3)**:
  - If ally within 2 hexes would take damage, intercept damage (redirect to self).
- **"Righteous Fury" (×3)**:
  - Attack for 5d6 damage.
  - Gain +1 damage permanently per enemy killed (stacks).
- **"Divine Judgment" (×2)**:
  - Attack for 8d6 damage, ignore Defense.
  - Can only use if below 10 HP (execute).
- **"Consecrated Ground" (×2)**:
  - Create 3-hex zone. Allied units in zone recover 1 card per turn for 3 turns.
- **"Last Rites" (×2)**:
  - If Zealot would be defeated, deal 10 damage to nearest enemy (death explosion).
- **"Move" (×2)**: Standard movement.

**Special Abilities**:
- **Martyrdom Training**: Gains +1 damage for each point of self-harm damage taken (max +5).
- **Zealot's Rage**: At 5 or fewer HP, gain +2 damage and +1 Movement (near-death power spike).

**Tactics**: Zealot self-harms for burst damage, protects allies, executes low-HP enemies. Gets stronger as wounded. Kill fast or kite. Deploy 1-2 as Church faction enemies.

**Loot**: 80 Credits, 2d3 Scrap, roll on Equipment Table, 1/5 chance of "Martyr's Brand Sigil" (Equipment: Self-harm cards deal +1 damage).

---

### 14. DWARVEN IRONCLAD

**Type**: Elite (Tank)
**HP Deck**: 22 cards (12 Universal + 6 Dwarven Core + 4 Equipment)
**Movement**: 3 hexes
**Armor**: 4 (heavy plating)
**SP**: 4

**Behavior Deck (22 cards)**:
- **"Forge-Hammer Strike" (×6)**:
  - Attack for 4d6 damage, armor-piercing (ignore 2 armor).
  - Generate 1 Rune Counter (Dwarven mechanic).
- **"Runic Shield" (×4)**:
  - Gain +3 Defense this turn.
  - For each Rune Counter, gain additional +1 Defense (stacks).
- **"Stone Endurance" (×3)**:
  - Recover 2 cards from discard.
  - Generate 1 Rune Counter.
- **"Earthquake Stomp" (×3)**:
  - AOE: All enemies within 2 hexes take 3d6 damage.
  - Consume 3 Rune Counters (requires setup).
- **"Defensive Stance" (×3)**:
  - Do not move. Gain +4 Defense this turn.
  - If attacked, counter for 3d6 damage.
- **"Move" (×3)**: Standard movement.

**Special Abilities**:
- **Rune Counter System**: Ironclad generates Rune Counters through attacks/abilities. Spend them for powerful effects.
- **Stone Endurance**: +2 Universal Core cards (32 HP total instead of 30).
- **Heavy Armor**: Reduce all damage by 4 (before Defense rolls).

**Tactics**: Ironclad stacks Rune Counters, builds massive Defense, then unleashes AOE attacks. Slow but unkillable. Deploy 1 as Dwarven faction elite.

**Loot**: 120 Credits, 4d3 Scrap, roll on Equipment Table, 1/4 chance of "Runic Plating" (Equipment: Gain +1 Armor, generate 1 Rune Counter per turn).

---

### 15. ELVEN VERDANT STALKER

**Type**: Elite (Assassin)
**HP Deck**: 16 cards (10 Universal + 4 Elven Core + 2 Equipment)
**Movement**: 6 hexes
**Armor**: 0 (evasion-based)
**SP**: 6

**Behavior Deck (16 cards)**:
- **"Bleed Strike" (×5)**:
  - Attack for 3d6 damage.
  - Target gains "Bleed 1" (lose 1 card per turn, stacks infinitely).
- **"Shadow Step" (×3)**:
  - Move 8 hexes (teleport through shadows).
  - If move adjacent to enemy, attack for 4d6 damage (ambush).
- **"Verdant Regeneration" (×2)**:
  - Recover 3 cards from discard.
  - If standing in forest/vegetation terrain, recover 5 cards instead.
- **"Thorn Volley" (×2)**:
  - Ranged attack (4-8 hexes): Deal 2d6 damage + Bleed 2.
- **"Nature's Wrath" (×2)**:
  - If target has Bleed 3+, deal 6d6 damage (execute bleeding enemies).
- **"Camouflage" (×2)**:
  - If standing in forest/vegetation, gain +4 Defense this turn (hard to see).

**Special Abilities**:
- **Bleed Stacking**: Bleed effects stack infinitely. High-Bleed enemies lose cards rapidly.
- **Forest Affinity**: Gains +1 Movement and +2 Defense when in forest terrain.
- **Evasion**: When attacked, roll 1d6. On 5-6, take half damage (agility).

**Tactics**: Stalker applies Bleed, kites, executes bleeding enemies. Stays in forest terrain for bonuses. Hard to pin down. Deploy 1 as Elven faction elite.

**Loot**: 100 Credits, 1d3 Scrap, roll on Equipment Table, 1/3 chance of "Thorn Bow" (Weapon: Ranged attacks apply Bleed 1).

---

## Using Enemies in Missions

### Swarm Missions (10-15 enemies)
- 8× Tainted Rats
- 4× Corrupted Villagers
- 2× Scrap Drones

**Goal**: Overwhelm players with numbers. Teach target prioritization.

### Elite Missions (3-5 enemies)
- 2× Bandit Raiders
- 1× Bandit Captain (leader)
- 1× Scrap Golem (guardian)

**Goal**: Tactical combat. Players must coordinate to kill leader/tank.

### Boss Missions (1 boss + minions)
- 1× Tainted Leviathan
- 4× Tainted Rats (adds)
- Spawns 2× Corrupted Villagers each Phase

**Goal**: Epic encounter. Players manage boss + adds simultaneously.

### Settlement Defense (varies)
- Roll 2d6 on Settlement Defense Table:
  - 2-4: 10× Tainted Rats + 3× Corrupted Villagers
  - 5-7: 4× Bandit Raiders + 1× Bandit Captain
  - 8-10: 1× Tainted Ogre + 6× Tainted Wolves
  - 11-12: 1× Rogue Casket (rival faction)

---

## Enemy Loot Tables

**Minor Loot (Swarm enemies)**:
- Roll 1d20:
  - 1-10: 5-20 Credits
  - 11-15: 1 Scrap
  - 16-19: Roll on Equipment Table
  - 20: 1 Soulstone Fragment

**Major Loot (Elite enemies)**:
- Roll 1d20:
  - 1-5: 50-100 Credits + 1d3 Scrap
  - 6-10: Roll on Equipment Table
  - 11-14: Roll twice on Equipment Table
  - 15-17: 1 Soulstone Fragment + roll Equipment
  - 18-19: Roll on Rare Loot Table
  - 20: Roll on Legendary Loot Table

**Boss Loot (Boss enemies)**:
- Guaranteed: 300-600 Credits + 5-10 Scrap
- Roll 3 times on Equipment Table
- Roll 1 time on Legendary Loot Table
- 50% chance of Unique Relic (GM creates)

---

## Enemy Design Philosophy

**Why Player-Like Decks?**
- Consistent mechanics (players learn once, apply everywhere)
- Emergent behavior (enemies can get unlucky draws, just like players)
- Component Damage applies (players can cripple enemy weapons)
- Death spiral works (enemies weaken as damaged)

**Why If-Then AI?**
- Predictable but dynamic (players can anticipate but not control)
- Scales with complexity (simple enemies = simple logic, bosses = complex)
- Behavior decks create narrative moments (lucky/unlucky draws affect outcomes)
- GM-friendly (no complex flowcharts, just read card and execute)

**Balance Notes**:
- Swarm: 3-5 HP (die in 1-2 hits)
- Elite: 15-25 HP (mini-boss, requires focus fire)
- Boss: 30-60 HP (campaign capstone, party effort)
- Players have 30 HP average, so 3× Elites ≈ 1.5× player HP total (balanced encounter)

---

**END OF DOCUMENT**

*"Know your enemy. Study their patterns. Exploit their weaknesses. Or die trying."*
