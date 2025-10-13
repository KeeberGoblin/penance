# Expanded Terrain Types
## SCP/Post-Apocalyptic Inspired Terrain for Penance

**Version**: 1.0
**Last Updated**: October 13, 2025

---

## Standard Terrain (Existing)

### Forest [F]
- **Effect**: +1 Defense when standing in this hex
- **Movement**: Normal (1 SP per hex)
- **LOS**: Blocks LOS through multiple forest hexes

### Rubble [R]
- **Effect**: +1 Defense when standing in this hex
- **Movement**: Difficult Terrain (2 SP per hex)
- **LOS**: Does not block LOS

### Water/Mud [W]
- **Effect**: -1 Movement (max movement reduced by 1 hex)
- **Movement**: Difficult Terrain (2 SP per hex)
- **LOS**: Does not block LOS

### Elevation 1 [E1]
- **Effect**: +1 damage to attacks FROM this hex
- **Movement**: Costs 2 SP to enter from lower elevation
- **LOS**: Can see over non-elevated terrain

### Elevation 2 [E2]
- **Effect**: +2 damage to attacks FROM this hex
- **Movement**: Costs 3 SP to enter from E1, 5 SP from ground
- **LOS**: Can see over all terrain except E2
- **Special**: Attacks FROM E2 gain +1 Range

---

## Anomalous Terrain (SCP-Inspired)

### Void Rift [VR]
**Visual**: Crackling purple-black tears in reality, unstable edges
**Classification**: Keter

- **Effect**: Roll 1d6 when entering. 1-2: Take 3 damage. 3-4: Teleport to random [VR] hex. 5-6: Gain +2 SP this turn
- **Movement**: Costs 3 SP to enter (players avoid if possible)
- **LOS**: Does not block LOS, but distorts vision (-1 to ranged attacks through)
- **Danger**: At start of each round, all [VR] hexes expand by 1 hex (mark with [VR*]). If 50%+ board is [VR], mission fails
- **Narrative**: "The Engine's scars weep into reality. The Veil is thin here."

### Taint Pools [TP]
**Visual**: Viscous black-green liquid, faintly glowing, bubbling
**Classification**: Euclid

- **Effect**: Standing in this hex: +1 Taint per turn. At 5 Taint: Gain +1 damage, but -1 Defense. At 10 Taint: Roll Strain every turn
- **Movement**: Normal (1 SP), but sticky—leaving costs +1 SP
- **LOS**: Does not block LOS
- **Cleanup**: Can be "cleansed" with fire (deal 5+ fire damage to hex)
- **Narrative**: "Soulstone runoff. The dead dissolved here. Their hunger remains."

### Reality Anchor [RA]
**Visual**: Ancient obelisk, runic inscriptions, stable aura
**Classification**: Thaumiel

- **Effect**: Standing in this hex: Immune to Taint. Void Rifts cannot expand into adjacent hexes. Recover 1 card at end of turn
- **Movement**: Normal (1 SP)
- **LOS**: Blocks LOS (tall structure)
- **Strategic**: Only 1-2 per map. Control = survival in anomalous zones
- **Narrative**: "Pre-Sundering wards. The old world's desperate anchors."

### Bone Fields [BF]
**Visual**: Skeletal remains half-buried, ribcages and skulls, churned earth
**Classification**: Safe

- **Effect**: The Ossuarium units gain +2 Defense here. All other factions: Movement costs +1 SP (uneven terrain)
- **Movement**: Difficult Terrain (2 SP for non-Ossuarium)
- **LOS**: Does not block LOS
- **Special**: Ossuarium can spend 2 SP to raise 1 Bone Thrall from this hex (once per hex per game)
- **Narrative**: "The Ledger remembers. Bones answer the call."

### Living Thicket [LT]
**Visual**: Writhing thorn vines, bioluminescent blooms, shifting vegetation
**Classification**: Euclid

- **Effect**: Elven units gain +1 Movement when entering. Non-Elves: Take 1 damage when entering (thorns)
- **Movement**: Costs 2 SP for non-Elves, 1 SP for Elves
- **LOS**: Blocks LOS (dense vegetation)
- **Special**: Elves can spend 1 SP to "command" vines—push 1 adjacent enemy 1 hex (Strength check)
- **Narrative**: "The forests did not die. They evolved. They remember their children."

---

## Post-Apocalyptic Terrain

### Radiation Zone [RZ]
**Visual**: Glowing green pools, mutated flora, warped metal
**Classification**: Keter

- **Effect**: Standing here: Take 2 damage at start of turn. Casket takes 1 Component Damage (random location) per 3 turns spent here
- **Movement**: Normal (1 SP), but no sane pilot enters willingly
- **LOS**: Does not block LOS
- **Mitigation**: Lead-Lined Plating (equipment) grants immunity
- **Narrative**: "Pre-Sundering reactors still weep. The half-life measures in millennia."

### Scrap Heap [SH]
**Visual**: Rusted metal piles, twisted girders, pre-Sundering wreckage
**Classification**: Safe

- **Effect**: Nomads/Dwarves gain +1 Scrap when standing here (once per hex per game). All other factions: +1 Defense (cover)
- **Movement**: Difficult Terrain (2 SP per hex)
- **LOS**: Blocks LOS (tall piles)
- **Special**: Can spend 3 SP to "scavenge"—draw 1 random equipment card from discard pile (once per hex)
- **Narrative**: "The old world's bones. Salvage is survival."

### Soulstone Deposit [SD]
**Visual**: Crystalline formations, pulsing with inner light, geometric patterns
**Classification**: Euclid

- **Effect**: Standing here: Recover 2 cards at end of turn, but gain +1 Heat per turn
- **Movement**: Normal (1 SP)
- **LOS**: Does not block LOS
- **Strategic**: High-risk, high-reward. Prolonged exposure = Heat overload
- **Narrative**: "Raw power. Unrefined. Untamed. The Engine's blood crystallized."

### Fungal Overgrowth [FO]
**Visual**: Massive mushroom caps, spore clouds, bioluminescent mycelium
**Classification**: Euclid

- **Effect**: Standing here: Roll 1d6 at end of turn. 1-2: Take 2 damage (spore inhalation). 3-4: No effect. 5-6: Recover 1 card (medicinal spores)
- **Movement**: Normal (1 SP)
- **LOS**: Blocks LOS (tall mushrooms)
- **Special**: If destroyed (5+ damage to hex), releases spore cloud—all adjacent hexes become [FO] next round
- **Narrative**: "Post-Sundering ecology. The fungi inherited the earth."

### Engine Scar [ES]
**Visual**: Geometric void patterns, impossible angles, anti-light
**Classification**: Apollyon

- **Effect**: Cannot be entered. Blocks all movement and LOS. Deals 5 damage to any unit ending turn adjacent
- **Movement**: Impassable
- **LOS**: Blocks LOS completely
- **Danger**: Permanent map feature. Represents where The Engine touched reality
- **Narrative**: "Where the Engine sang, nothing remains. Not even void. Absence itself."

---

## Weather-Affected Terrain Modifiers

### Tainted Rain
- **Effect**: All [W] Water hexes become [TP] Taint Pools for this mission
- **Duration**: Entire scenario
- **Visual**: Black rain, oily puddles

### Void Storm
- **Effect**: 1d3 random hexes become [VR] Void Rifts at start of each round
- **Duration**: 5 rounds, then clears
- **Visual**: Purple lightning, reality tears

### Fungal Bloom
- **Effect**: All [F] Forest hexes become [FO] Fungal Overgrowth
- **Duration**: Entire scenario
- **Visual**: Bioluminescent mushrooms overtake trees

### Soulstone Eclipse
- **Effect**: All [SD] Soulstone Deposits glow brighter—recover 3 cards instead of 2, but +2 Heat instead of +1
- **Duration**: 3 rounds
- **Visual**: Crystalline formations pulse with blinding light

---

## Faction-Specific Terrain Interactions

### Church of Absolution
- **Consecrated Ground**: Can spend 3 SP to "cleanse" 1 hex within 2 hexes—remove [TP], [VR*], or [RZ] effects for 3 rounds
- **Holy Fire**: Fire damage from Church units permanently removes [TP] Taint Pools

### Dwarven Forge-Guilds
- **Stone Endurance**: Ignores movement penalties from [R] Rubble and [SH] Scrap Heaps
- **Rune Anchors**: Can spend 2 SP to convert 1 hex within 1 hex to [RA] Reality Anchor (once per game)

### The Ossuarium
- **Bone Harvest**: Gains +1 Scrap when standing on [BF] Bone Fields
- **Corpse Fuel**: Can spend 3 SP on [BF] to raise 1 Bone Thrall (support unit)

### Elven Verdant Covenant
- **Photosynthesis**: Standing on [LT] Living Thicket recovers +1 additional card per turn
- **Leaf Dance**: Can move through [LT] without penalty, ignoring thorns

### Nomadic Scrap-Takers (Future Faction)
- **Salvage Expertise**: Gains +2 Scrap from [SH] Scrap Heaps instead of +1
- **Jury-Rig**: Can spend 3 SP to convert [SH] to makeshift [RA] Reality Anchor (weaker, lasts 5 rounds)

---

## Scenario-Specific Terrain Combinations

### "The Tainted Wastes" (Radiation + Taint)
- 30% [RZ] Radiation Zones
- 20% [TP] Taint Pools
- 10% [RA] Reality Anchors (critical control points)
- Weather: Tainted Rain (all water becomes taint)

### "The Living Forest" (Elven Territory)
- 40% [LT] Living Thicket
- 20% [F] Normal Forest
- 10% [VR] Void Rifts (Engine scars)
- Weather: None (natural)

### "The Bone Wastes" (Ossuarium Domain)
- 50% [BF] Bone Fields
- 20% [SD] Soulstone Deposits
- 10% [ES] Engine Scars
- Weather: Void Storm (reality unstable)

### "The Scrap Barrens" (Nomad Territory)
- 40% [SH] Scrap Heaps
- 30% [R] Rubble
- 10% [RZ] Radiation Zones (old reactors)
- Weather: None

### "The Anomalous Zone" (High-Risk)
- 20% [VR] Void Rifts (expanding)
- 20% [TP] Taint Pools
- 20% [FO] Fungal Overgrowth
- 5% [ES] Engine Scars
- 5% [RA] Reality Anchors (desperate survival)
- Weather: Void Storm + Fungal Bloom

---

## Design Notes

### Balance Considerations
- **Anomalous terrain** should be rare (10-20% of map) but impactful
- **Faction-specific terrain** creates asymmetric map control
- **Weather effects** add scenario variety without new terrain types
- **Reality Anchors** are critical control points in anomalous scenarios

### Narrative Integration
- Terrain tells the story of The Engine's impact
- Post-apocalyptic ecology (fungal overgrowth, mutation)
- SCP-style containment failures (Void Rifts, Taint Pools)
- Faction identity reinforced through terrain interactions

### Playtesting Priorities
1. Test [VR] Void Rift expansion rate (too fast = unwinnable)
2. Balance [TP] Taint accumulation vs. benefits
3. Ensure [RA] Reality Anchors are worth fighting for
4. Verify faction-specific interactions don't break scenarios

---

*"The land remembers The Engine's song. Tread carefully, Pilot."*
