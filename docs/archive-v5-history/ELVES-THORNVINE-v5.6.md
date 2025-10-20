# Elves Redesign: Thornvine System (v5.6)

**Date**: 2025-10-20
**Change Type**: Mechanical Redesign
**Goal**: Replace bleed mechanic with thematic plant summoning system

---

## Summary

**What Changed**: Elves faction completely redesigned from bleed-stacking damage-over-time to Thornvine plant summoning system.

**Why**: Plant summoning is:
- More thematic (forest elves summon nature)
- More interactive (enemies can destroy plants)
- More strategic (seed placement and timing matter)
- More fun (creatures on battlefield > invisible counters)

**Balance Impact**: None expected. Elves remain at ~52% WR (balanced).

---

## Changes Applied

### Faction Cards Updated (5 cards)

**1. Thorn Strike**
- OLD: "Deal 3 damage. Apply Bleed 2"
- NEW: "Deal 3 damage. Plant 2 Thornvine seeds in target's hex"

**2. Root Bind**
- OLD: "Immobilize. If move, take 3 damage + Bleed 1"
- NEW: "Immobilize. Plant 2 Thornvine seeds. If move, take 3 damage"

**3. Nature's Wrath**
- OLD: "Deal 6 damage to target. 2 damage to adjacent enemies"
- NEW: "Detonate all Thornvine seeds. Deal 2 damage per seed (max 8/hex). Clear all seeds"

**4. Wild Growth**
- OLD: "Create difficult terrain in 3 hexes. 1 damage/hex"
- NEW: "Add 1 Thornvine seed to all hexes within 2 of you. Passive: +1 seed in your hex/round"

**5. Overgrowth** (NEW)
- "Target hex with 3+ seeds sprouts into Thornvine Snare immediately. Lasts 3 turns"

---

### Equipment Cards Updated (2 cards)

**1. Thorn Blade Slash**
- OLD: "Deal 3 damage. Apply Bleed 2"
- NEW: "Deal 3 damage. Plant 2 Thornvine seeds"

**2. Vine Whip Lash**
- OLD: "Deal 2 damage. Apply Bleed 1"
- NEW: "Deal 2 damage. Plant 1 Thornvine seed"

---

### Plant Creatures Added (3 support units)

**1. Thornvine Snare**
- **HP**: 4
- **Defense**: 2
- **Movement**: 0 (stationary)
- **Duration**: 3 turns
- **Effect**: Enemy in hex has -2 Movement, takes 2 damage/turn
- **Spawns**: Automatically when hex has 3 seeds at end of Elves turn

**2. Bramble Sentinel**
- **HP**: 6
- **Defense**: 3
- **Movement**: 0 (stationary)
- **Duration**: 2 turns
- **Effect**: Allies within 2 hexes gain +1 Defense, provides hard cover
- **Spawns**: Automatically when hex has 4 seeds, OR manually with Overgrowth card

**3. Spore Bloom**
- **HP**: 3
- **Defense**: 1
- **Movement**: 0 (stationary)
- **Duration**: 1 turn (then explodes)
- **Effect**: Explodes for 3 damage to all adjacent hexes (friendly fire possible)
- **Spawns**: When Elves kill enemy with 3+ seeds in hex

---

## How Thornvine Works

### Step 1: Plant Seeds
- Elves attacks plant 1-2 seeds in target hex
- Max 4 seeds per hex
- Seeds persist between turns

### Step 2: Seeds Sprout
- At end of Elves turn, hexes with 3+ seeds auto-sprout
- 3 seeds = Thornvine Snare
- 4 seeds = Bramble Sentinel
- Kill enemy with seeds = Spore Bloom

### Step 3: Plants Act
- Plants are stationary support units
- Thornvine Snare: Immobilizes + damages enemy
- Bramble Sentinel: Buffs allies' Defense
- Spore Bloom: Explodes after 1 turn

### Step 4: Plants Wither
- Plants self-destruct after duration
- OR enemies can attack/destroy them
- Sprouting consumes all seeds in hex

---

## Strategic Gameplay

### Seed Stacking Combos

**Fast Stack (1 turn → plant)**:
- Root Bind (2 seeds) + Thorn Strike (2 seeds) = 4 seeds
- Auto-sprouts Bramble Sentinel at end of turn

**Area Denial**:
- Wild Growth (1 seed to all hexes in 2-hex radius)
- Creates "minefields" that sprout if enemies linger

**Detonation**:
- Stack 4 seeds in multiple hexes
- Nature's Wrath detonates all (8 damage per hex!)
- Board-wide nuke

### Plant Tactics

**Thornvine Snare** (3 seeds):
- Use on melee enemies (locks them down)
- Use on objectives (forces enemies to destroy plant first)
- Use in choke points (blocks movement)

**Bramble Sentinel** (4 seeds):
- Use near wounded allies (+1 Defense save)
- Use as cover (hard cover blocks LOS)
- Use defensively (2-turn buffer)

**Spore Bloom** (kill trigger):
- Combo with Root Bind (trap enemy near bloom)
- Bait enemies (they must destroy or take 3 damage)
- Sacrifice play (detonate among grouped enemies)

---

## Balance Comparison

### Old Bleed Mechanic

**Power**:
- Stack 1-4 Bleed counters on enemy
- Deal 1-4 damage/turn automatically
- Max 4 damage/turn passive

**Gameplay**:
- Simple (just stack counters)
- Passive (no decisions after stacking)
- No counterplay (enemy can't remove bleed)

**Thematic**: ❌ Generic DOT, not forest-themed

---

### New Thornvine Mechanic

**Power**:
- Plant 1-4 seeds per hex
- Seeds sprout into plants
- Plants deal 2-3 damage/turn OR buff allies

**Gameplay**:
- Complex (seed placement, timing, plant type)
- Interactive (enemies destroy plants, Elves detonate seeds)
- Counterplay (attack plants, avoid seeded hexes)

**Thematic**: ✅ Forest elves summon nature, battlefield becomes ecosystem

---

### Power Level Analysis

**Damage Output** (similar):
- Bleed: 2-4 damage/turn guaranteed
- Thornvine Snare: 2 damage/turn (but enemy must stay in hex)
- Nature's Wrath: 2-8 damage/hex burst (but consumes seeds)

**Utility Gain** (Thornvine wins):
- Bleed: None (just damage)
- Thornvine: Immobilize (-2 Movement), Defense buff (+1), hard cover, area denial

**Counterplay** (Thornvine has more):
- Bleed: No counterplay
- Thornvine: Destroy plants (3-6 HP), avoid seeded hexes, pressure Elves before setup

**Verdict**: Thornvine is **similar power**, **higher skill ceiling**, **more fun**.

---

## Expected Impact

### Win Rate Projection
- **Current**: Elves at ~52% WR (post-v5.5 nerf)
- **Expected**: Elves at ~52% WR (unchanged)
- **Reasoning**: Damage output similar, utility trades guaranteed damage for flexibility

### Playstyle Changes
- **Before**: Stack bleed, attack repeatedly, passive damage
- **After**: Plan seed placement, time sprouting/detonation, manage plants
- **Skill Floor**: Slightly higher (more mechanics to learn)
- **Skill Ceiling**: Much higher (optimal seed placement, combo timing)

### Player Experience
- **Before**: "I bleed you, then wait"
- **After**: "I'm growing a forest to trap you"
- **Fantasy**: Forest elves > bleeding attackers
- **Visual**: Plants on board > invisible counters

---

## Files Modified/Created

### Database Changes
1. [complete-card-data.json](cards/complete-card-data.json) - v5.5 → v5.6
   - 5 faction cards updated (Thornvine effects)
   - 2 equipment cards updated (Thornvine effects)
   - 1 faction card added (Overgrowth)
   - 3 plant support units added (159 behavior cards total)

### Documentation Created
2. [thornvine-mechanic.md](rules/thornvine-mechanic.md) - Complete Thornvine rules
3. [ELVES-THORNVINE-v5.6.md](ELVES-THORNVINE-v5.6.md) - This document

---

## Playtesting Recommendations

### Critical Tests
1. **Seed Stacking Speed** - Can Elves get 3+ seeds in 1-2 turns?
2. **Plant Durability** - Are 3-6 HP plants too fragile?
3. **Counterplay Balance** - Can enemies react to seeds before sprout?

### Balance Monitoring
4. **Win Rate** - Does Elves WR stay at ~52%?
5. **Damage Output** - Is plant damage comparable to old bleed?
6. **Player Feedback** - Is Thornvine fun to play/play against?

### Edge Cases
7. **Spore Bloom Friendly Fire** - Does 3 damage to allies feel fair?
8. **Nature's Wrath Scaling** - Is 8 damage/hex too strong with 4 seeds?
9. **Wild Growth Spam** - Can Elves blanket battlefield with seeds?

---

## Design Notes

### Why This Change?

**Problem with Bleed**:
- Generic mechanic (every game has bleed)
- Not thematic (elves = forest, not bleeding)
- Low interactivity (just stack counters)
- Low skill expression (no decisions after stacking)

**Solution with Thornvine**:
- Unique mechanic (plant summoning rare in mech games)
- Highly thematic (forest grows on battlefield)
- High interactivity (plants, seeds, sprouting, detonation)
- High skill expression (placement, timing, combo optimization)

**Player Fantasy**:
- Elves = forest warriors
- Forest = grows, spreads, entangles
- Thornvine = brings forest to battlefield
- "I'm not just attacking you, I'm terraforming the battlefield"

---

## Future Expansion Ideas

**Additional Plant Types** (not implemented):
- **Healing Bloom**: Restores 1 card/turn to nearby allies
- **Poison Ivy**: Spreads seeds to adjacent hexes automatically
- **Treant Guardian**: Mobile plant (2 Movement, 8 HP, 4 Defense)

**Advanced Mechanics** (not implemented):
- **Seed Nutrients**: Killing enemies plants seeds in their hex
- **Photosynthesis Buff**: Plants heal 1 HP/turn in sunlight terrain
- **Forest Fire**: Fire damage destroys seeds + plants instantly

---

## References

- [Thornvine Mechanic Rules](rules/thornvine-mechanic.md) - Complete gameplay rules
- [Support Units](rules/support-units.md) - Plant creatures as support units
- [Elves Faction Cards](cards/complete-card-data.json) - All Elves cards (line 1191+)

---

## Conclusion

**Status**: ✅ Complete

**Changes**:
- 7 Elves cards updated (bleed → Thornvine)
- 3 plant creatures added
- 1 new faction card (Overgrowth)
- Complete rules documentation

**Balance**: No change expected (~52% WR maintained)

**Thematic Impact**: ⭐⭐⭐⭐⭐ Major improvement (forest elves now summon nature!)

**Gameplay Impact**: ⭐⭐⭐⭐ More strategic, more interactive, higher skill ceiling

**Ready for playtesting**: Yes

---

*"The forest remembers. The forest hungers."* - Elves motto
