# CRITICAL INSIGHT: Ossuarium Balance Paradox

## The Paradox

**Ossuarium has 68.9% WR even though lifesteal is DISABLED in the simulation!**

### v5.23 Changes (Current)
```python
# V5.23: REMOVED LIFESTEAL - Ossuarium now only gains Taint from dealing damage
# Taint accumulates and causes penalties, but NO card recovery
if attacker.faction.lower() == 'ossuarium' and actual_damage > 0:
    taint_gain = (actual_damage + 2) // 3  # 1 Taint per 3 damage
```

**Lifesteal does NOT work in simulation** - no cards are recovered!

## Current Taint System

### Taint Gain Rate:
- 1 Taint per 3 damage dealt
- Caps at 10 Taint
- Decays by -1 per turn

### Taint Penalties (v5.25 - REVERTED to lighter v5.23 levels):

| Taint Level | Heat Penalty | Damage Penalty |
|-------------|--------------|----------------|
| 1-2 Taint | +1 Heat/turn | -0 damage |
| 3-4 Taint | +1 Heat/turn | -1 damage |
| 5-7 Taint | +2 Heat/turn | -1 damage |
| 8-10 Taint | +2 Heat/turn | -2 damage |

**Note:** v5.24 tried harsher penalties but made balance WORSE, so they reverted.

## Why Ossuarium Is Still Overpowered

### Theory 1: Taint Penalties Too Weak
- Dealing 9 damage = gain 3 Taint = only -1 damage penalty
- Taint decays by 1/turn, so penalties never accumulate
- At 10 Taint (max): only -2 damage and +2 Heat
- **This is NOT enough downside for zero lifesteal cost**

### Theory 2: Base Card Efficiency
Without lifesteal, Ossuarium cards are still efficient:

| Card | Cost | Damage | Efficiency |
|------|------|--------|------------|
| Siphon Essence | 2 | 2 | 1.0 dmg/SP |
| Death Grasp | 2 | 3 | 1.5 dmg/SP |
| Necrotic Touch | 2 | 2 | 1.0 dmg/SP |
| Bone Scythe Swing | 3 | 4 | 1.33 dmg/SP |
| Soul Harvest | 3 | 4 | 1.33 dmg/SP |
| Soul Rend | 4 | 5 | 1.25 dmg/SP |
| Drain Life | 5 | 6 | 1.2 dmg/SP |

Average: **1.22 dmg/SP** (above average)

Compare to Dwarves (22.2% WR):
- Average: **1.01 dmg/SP** (below average)

### Theory 3: Passive Cards Still Work
Even without lifesteal, Ossuarium has strong passives:
- **Phylactery:** Auto-revive to 3 HP (NO TAINT PENALTY)
- **Soul Well:** Draw cards when hand ≤5 (NO TAINT PENALTY)
- **Deathless Advance:** Damage cap at 5 (NO TAINT PENALTY)
- **Corpse Shield:** +3 Defense when enemy dies nearby

## The Real Problem

**The card text PROMISES lifesteal that doesn't work, but Ossuarium is still OP because:**

1. **Base damage efficiency is too high** (1.22 dmg/SP)
2. **Taint penalties are too weak** (max -2 damage at 10 Taint)
3. **Passives have no downsides** (Phylactery, Soul Well, Deathless Advance)
4. **Taint decays too fast** (-1 per turn means penalties never stick)

## Revised Balance Recommendations

### Option A: Increase Taint Penalties (Simulation Fix)
```python
# Harsher Taint penalties
if attacker.taint_tokens >= 8:
    damage_penalty = 4  # Was 2
elif attacker.taint_tokens >= 5:
    damage_penalty = 3  # Was 1
elif attacker.taint_tokens >= 3:
    damage_penalty = 2  # Was 1
```

### Option B: Reduce Base Damage (Card Fix)
- Soul Harvest: 4 damage → 3 damage
- Soul Rend: 5 damage → 4 damage
- Drain Life: 6 damage → 5 damage
- Death Grasp: 3 damage → 2 damage

### Option C: Nerf Passives (Card Fix)
- Phylactery: Add "Gain 5 Taint when triggered"
- Soul Well: Add "Gain 1 Taint when triggered"
- Deathless Advance: Increase cost from 2 SP → 3 SP

### Option D: Prevent Taint Decay
```python
# Taint no longer decays naturally
# Can only be removed by resting or purge abilities
```

## What Actually Needs To Happen

**The card text needs to match the simulation:**

1. **Remove lifesteal text from cards** → Replace with "Gain X Taint"
2. **OR implement lifesteal in simulation** → But add Taint as a cost
3. **Increase Taint penalties** → Make them actually matter
4. **OR reduce base damage** → Make cards less efficient without lifesteal

## Conclusion

Ossuarium is overpowered because:
- **Cards promise lifesteal (doesn't work)**
- **Base damage is efficient anyway**
- **Taint penalties are too weak**
- **Passives have no costs**

The 68.9% WR proves that **the faction is broken even without their signature mechanic working**.

This is a fundamental design problem that needs both:
1. **Simulation fix** (implement lifesteal + proper Taint costs)
2. **Card rebalance** (reduce efficiency or increase costs)

---

**Recommendation:** Either fully implement the Taint-as-cost system with harsher penalties, OR restore lifesteal but with proper costs. The current middle-ground doesn't work.
