# Soul Shard System - Ossuarium Faction Mechanic

## Core Concept

**Ossuarium mechs are necro-mechanical war machines that salvage enemy wrecks for parts.**

Instead of magical "lifesteal," they:
- Gain **Soul Shards** from destroyed enemies
- Spend **Soul Shards** to perform emergency repairs
- Accumulate **Taint** from using corrupted necro-tech
- Suffer penalties when Taint gets too high

## Soul Shard Economy

### Gaining Soul Shards

| Event | Soul Shards Gained |
|-------|-------------------|
| Enemy Casket destroyed | **3 Shards** |
| Enemy Support Unit destroyed | **1 Shard** |
| Marked enemy destroyed | **+1 Shard** (bonus) |

**Storage:** Soul Shards persist throughout the battle (no cap)

### Spending Soul Shards

Soul Shards can be spent on **Salvage Actions** to recover cards:

| Salvage Action | Cost | Effect | Taint |
|----------------|------|--------|-------|
| **Emergency Patch** | 2 Shards | Recover 2 cards | +1 Taint |
| **Field Salvage** | 3 Shards | Recover 3 cards | +2 Taint |
| **Desperate Rebuild** | 5 Shards | Recover 5 cards | +3 Taint |

**Important:** Salvage actions cost SP (typically 1-2 SP) AND Soul Shards.

### Universal Salvage Card (All Ossuarium Decks)

Every Ossuarium deck includes:

```
SALVAGE PROTOCOL
Cost: 1 SP, Utility
Effect: Spend 3 Soul Shards to recover 3 cards. Gain 2 Taint.
Flavor: "Strip the wreckage for usable components."
```

## Taint System (Brutal Penalties)

### Taint Accumulation
- Taint is gained when spending Soul Shards on repairs
- Taint NEVER decays naturally (persists entire battle)
- Taint resets to 0 between missions

### Taint Penalties

| Taint Level | Penalty | Description |
|-------------|---------|-------------|
| **0-2** | None | "Systems stable" |
| **3-4** | -1 damage | "Minor corruption detected" |
| **5-6** | -2 damage, +1 Heat/turn | "Necro-tech destabilizing" |
| **7-8** | -3 damage, +2 Heat/turn | "Critical system corruption" |
| **9-10** | -4 damage, +2 Heat/turn, SP costs +1 | "Catastrophic failure imminent" |

### Taint Management

**Ways to avoid high Taint:**
- Don't spend Soul Shards (tough it out)
- Use small repairs (2 Shards = only +1 Taint)
- End fights quickly before corruption accumulates

**No way to remove Taint mid-battle** (brutal design)

## Card Design Philosophy

### Attack Cards (Damage-Focused)
- Deal good damage
- Optional: Gain bonus Shards on kill
- NO automatic healing

**Example:**
```
SOUL HARVEST
3 SP, 4 damage
"Deal 4 damage. If this kills the target, gain +2 Soul Shards."
```

### Utility Cards (Shard Generation)
- Generate Shards from kills
- Mark enemies for bonus Shards
- Convert resources into Shards

**Example:**
```
CORPSE FUEL
2 SP, Passive
"Whenever an enemy is destroyed within 3 hexes, gain 2 Soul Shards."
```

### Salvage Cards (Spending Shards)
- Spend Shards to recover cards
- Always generate Taint
- Must make trade-off decisions

**Example:**
```
DESPERATE REBUILD
2 SP, Utility
"Spend 5 Soul Shards to recover 5 cards. Gain 3 Taint."
```

### Passive Cards (Conditional Benefits)
- No automatic effects
- Require kills or specific conditions
- May have Taint costs

## Strategic Gameplay

### Early Battle (0-2 Taint)
- Focus on killing enemies
- Bank Soul Shards
- Use small repairs if needed (2 Shards, +1 Taint)

### Mid Battle (3-5 Taint)
- -2 damage penalty starting to hurt
- Be selective with repairs
- Prioritize finishing wounded enemies

### Late Battle (6+ Taint)
- -3 to -4 damage penalty (crippling)
- Avoid further repairs if possible
- Try to end fight quickly

### Death Spiral (9-10 Taint)
- You're severely crippled
- Almost useless offensively
- Hope you can survive to end of battle

## Balance Considerations

### Why This Fixes 68.9% WR

**Old System (Broken):**
- Automatic lifesteal on every attack
- No meaningful resource management
- Weak Taint penalties

**New System (Balanced):**
- Must kill to get resources ✅
- Must spend resources wisely (Taint) ✅
- Can't sustain forever (harsh penalties) ✅
- Rewards aggressive play (more kills = more Shards) ✅
- Punishes greed (high Taint cripples you) ✅

### Expected Win Rate: 48-52%

**Strong points:**
- Excellent sustain IF you get kills
- Can recover from low HP
- Aggressive playstyle works

**Weak points:**
- Useless if you can't get kills
- Taint accumulates fast
- Late-game severely weakened
- No sustain against evasive enemies

## Thematic Wins

✅ **Mech-appropriate** - Salvaging parts, not magic
✅ **Resource management** - Must manage Shards and Taint
✅ **Aggressive playstyle** - Rewarded for kills
✅ **Brutal choices** - Every repair costs corruption
✅ **Counterplay** - Enemies can deny kills
✅ **Skill expression** - Good players manage resources better

---

**Design Pillars:**
1. **Kill to survive** - No kills = no sustain
2. **Power at a price** - Repairs generate Taint
3. **Death spiral possible** - High Taint cripples you
4. **No safety nets** - Taint never leaves
5. **Aggressive gameplay** - Must be proactive

**Player Fantasy:**
> "I am a relentless war machine fueled by death itself. Every fallen enemy makes me stronger, but the corrupted necro-tech slowly tears me apart. I must kill fast and end fights before the corruption consumes me."
