# Soul Shard System - Simulation Implementation Guide

## Overview

This document describes how to implement the Soul Shard system in the combat simulator.

## Changes Required

### 1. Add Soul Shard Tracking to Casket Class

```python
@dataclass
class Casket:
    # ... existing fields ...
    soul_shards: int = 0        # Soul Shards accumulated (Ossuarium only)
    taint_tokens: int = 0       # Taint from salvaging (already exists)
```

### 2. Soul Shard Generation (On Kill)

When an enemy is destroyed, award Soul Shards to Ossuarium:

```python
def handle_enemy_destroyed(attacker: Casket, defender: Casket):
    """Called when defender is reduced to 0 HP"""
    if attacker.faction.lower() == 'ossuarium':
        # Base reward
        shards_gained = 3  # Standard for Casket kills

        # Check for Death Mark bonus (if implemented)
        if defender.has_death_mark:
            shards_gained += 2  # Bonus from Death Mark

        # Check for Corpse Fuel passive (if within 3 hexes - always true in 1v1)
        if attacker.has_corpse_fuel_passive:
            shards_gained += 2

        attacker.soul_shards += shards_gained
        log(f"{attacker.name} gained {shards_gained} Soul Shards from kill ({attacker.soul_shards} total)")
```

### 3. Salvage Protocol Implementation

When "Salvage Protocol" card is played:

```python
def play_salvage_protocol(casket: Casket):
    """Spend 3 Soul Shards to recover 3 cards, gain 2 Taint"""
    shard_cost = 3
    cards_to_recover = 3
    taint_cost = 2

    if casket.soul_shards < shard_cost:
        log(f"Cannot salvage - need {shard_cost} Shards, have {casket.soul_shards}")
        return False

    # Spend Soul Shards
    casket.soul_shards -= shard_cost

    # Recover cards from discard
    cards_recovered = casket.recover_cards(cards_to_recover, source="salvage")

    # Gain Taint
    old_taint = casket.taint_tokens
    casket.taint_tokens = min(casket.taint_tokens + taint_cost, 10)
    taint_gained = casket.taint_tokens - old_taint

    log(f"{casket.name} salvaged: -{shard_cost} Shards, +{cards_recovered} cards, +{taint_gained} Taint")
    log(f"  Resources: {casket.soul_shards} Shards, {casket.taint_tokens}/10 Taint")

    return True
```

### 4. Update Taint Penalties (Harsher)

```python
def apply_taint_penalties(casket: Casket):
    """Apply taint penalties at turn start"""
    if casket.taint_tokens == 0:
        return

    heat_penalty = 0
    damage_penalty = 0
    sp_penalty = 0

    if casket.taint_tokens >= 9:
        heat_penalty = 2
        damage_penalty = 4
        sp_penalty = 1
    elif casket.taint_tokens >= 7:
        heat_penalty = 2
        damage_penalty = 3
        sp_penalty = 0
    elif casket.taint_tokens >= 5:
        heat_penalty = 2
        damage_penalty = 2
        sp_penalty = 0
    elif casket.taint_tokens >= 3:
        heat_penalty = 1
        damage_penalty = 1
        sp_penalty = 0
    else:  # 1-2 Taint
        heat_penalty = 1
        damage_penalty = 1
        sp_penalty = 0

    casket.heat += heat_penalty
    casket.taint_damage_penalty = damage_penalty
    casket.taint_sp_penalty = sp_penalty

    log(f"{casket.name} Taint corruption: -{damage_penalty} damage, +{heat_penalty} Heat")
```

### 5. Remove Lifesteal Logic

**REMOVE** all existing Ossuarium lifesteal code:

```python
# V5.23: REMOVED LIFESTEAL - DELETE THIS SECTION
# if attacker.faction.lower() == 'ossuarium' and actual_damage > 0:
#     cards_to_recover = min(actual_damage, 3)
#     attacker.recover_cards(cards_to_recover)
```

Replace with Soul Shard on-kill check.

### 6. Update Card Damage Values

Update attack card damage in simulation data:

```python
# Old values (too high)
"Soul Harvest": 4 damage
"Death Grasp": 3 damage
"Soul Rend": 5 damage
"Drain Life": 6 damage

# New values (balanced)
"Soul Harvest": 3 damage
"Death Grasp": 2 damage
"Soul Rend": 4 damage
"Drain Life": 5 damage
```

### 7. Phylactery Auto-Revival

```python
def check_phylactery(casket: Casket):
    """Check if Phylactery can activate"""
    if casket.hp <= 0 and not casket.phylactery_used:
        if casket.soul_shards >= 5:
            # Spend 5 Shards
            casket.soul_shards -= 5

            # Recover to 3 HP
            casket.recover_cards(3, source="phylactery")

            # Gain massive Taint
            casket.taint_tokens = min(casket.taint_tokens + 5, 10)

            casket.phylactery_used = True
            log(f"⚠️ {casket.name} PHYLACTERY ACTIVATED! -5 Shards, +5 Taint")
            return True
    return False
```

## Implementation Priority

### Phase 1 (Core System):
1. ✅ Add `soul_shards` field to Casket
2. ✅ Implement Soul Shard generation on kill
3. ✅ Implement Salvage Protocol card effect
4. ✅ Remove old lifesteal logic
5. ✅ Update Taint penalties (harsher)

### Phase 2 (Card Effects):
6. Update attack card damage values
7. Implement execution bonus Shards
8. Implement Corpse Fuel passive
9. Implement Death Mark bonus

### Phase 3 (Testing):
10. Run faction_balance_MULTIUNIT.py
11. Target: Ossuarium 48-52% WR
12. Adjust Shard costs/Taint penalties if needed

## Expected Simulation Changes

### Before (v5.23):
```
Ossuarium: 68.9% WR
- No lifesteal (removed)
- Weak Taint penalties (max -2 damage)
- Still overpowered from base stats
```

### After (v6.0 Soul Shard System):
```
Ossuarium: ~50% WR (predicted)
- Must kill to get Shards (0 Shards = no sustain)
- Must spend Shards + Taint to heal (trade-off)
- Harsh Taint penalties (up to -4 damage)
- Reduced base damage (3 instead of 4-5)
```

## Simulation Test Cases

### Test 1: No Kills = No Sustain
```python
# Ossuarium that doesn't get kills should accumulate no Shards
# Should have 0 Shards throughout fight
# Should take damage with no way to recover
assert ossuarium.soul_shards == 0
```

### Test 2: Killing Grants Shards
```python
# Ossuarium kills enemy
enemy.hp = 0
handle_enemy_destroyed(ossuarium, enemy)
assert ossuarium.soul_shards == 3  # Base reward
```

### Test 3: Salvage Costs Shards + Taint
```python
ossuarium.soul_shards = 5
ossuarium.taint_tokens = 2
play_salvage_protocol(ossuarium)
assert ossuarium.soul_shards == 2  # 5 - 3
assert ossuarium.taint_tokens == 4  # 2 + 2
```

### Test 4: High Taint Cripples Damage
```python
ossuarium.taint_tokens = 9
apply_taint_penalties(ossuarium)
assert ossuarium.taint_damage_penalty == 4  # -4 damage at 9 Taint
```

### Test 5: Phylactery Requires Shards
```python
ossuarium.hp = 0
ossuarium.soul_shards = 3  # Not enough
assert check_phylactery(ossuarium) == False  # Doesn't activate

ossuarium.soul_shards = 5  # Enough
assert check_phylactery(ossuarium) == True  # Activates
assert ossuarium.taint_tokens >= 5  # Gained Taint
```

## Balance Knobs (If WR Still Wrong)

If Ossuarium is **still too strong** (>55% WR):
- Increase Taint costs (3 Shards → +3 Taint instead of +2)
- Reduce Shard generation (3 → 2 per kill)
- Increase Taint penalties (9 Taint → -5 damage instead of -4)

If Ossuarium is **too weak** (<45% WR):
- Reduce Taint costs (3 Shards → +1 Taint instead of +2)
- Increase Shard generation (3 → 4 per kill)
- Slightly increase attack damage (3 → 3.5 average)

---

**Target:** 48-52% win rate in multi-unit combat simulation
**Philosophy:** Kill to survive, but corruption will consume you
