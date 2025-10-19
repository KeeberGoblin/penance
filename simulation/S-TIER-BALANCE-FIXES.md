# S-Tier Faction Balance Analysis & Fixes

## Current S-Tier Problems

After fixing Church, Dwarves, and Ossuarium core mechanics, we still have 3 factions dominating:

| Faction | WR% | Key Issues |
|---------|-----|------------|
| **Ossuarium** | 66.9% | Still has 6/9 matchups at 75%+ WR |
| **Elves** | 65.6% | Bleed stacking too strong |
| **Dwarves** | 61.9% | Defensive runes too strong late game |

---

## OSSUARIUM (66.9% WR - Still OP)

### Current Implementation:
```python
if attacker.sp >= 3:
    attacker.sp -= 3
    base_damage = 4
    cards_recovered = min(base_damage, 4)  # Recover 4 cards
    # Recycle 4 cards from discard
```

### Why Still OP:

1. **4 Cards Recovered = Full Lifesteal**
   - Deals 4 damage, recovers 4 cards
   - 100% lifesteal ratio
   - Can sustain forever in long fights

2. **SP Cost Not Limiting Enough**
   - Warden has 5 SP, costs 3 SP
   - Still has 2 SP left for movement/defense
   - Can use Soul Harvest every turn without real cost

3. **No Diminishing Returns**
   - Works at full power from turn 1 to turn 150
   - Never weakens, never exhausts
   - Late game = guaranteed win

### Match Results Showing OP:
- vs Crucible: 95% WR (19-0-1)
- vs Exchange: 95% WR (19-0-1)
- vs Nomads: 90% WR (18-0-2)
- vs Emergent: 85% WR (17-0-3)
- vs Wyrd: 85% WR (17-0-3)
- vs Bloodlines: 75% WR (15-0-5)

**Only counters:** Dwarves (stalemate), Church (50%), Elves (50%)

### Proposed Fixes:

**Option 1: Reduce Lifesteal Ratio**
```python
# Soul Harvest v2: 75% lifesteal instead of 100%
if attacker.sp >= 3:
    attacker.sp -= 3
    base_damage = 4
    cards_recovered = 3  # CHANGED: 3 instead of 4 (75% lifesteal)
```
- **Effect:** Still strong sustain, but can be out-damaged
- **Target WR:** 55-60%

**Option 2: Increase SP Cost**
```python
# Soul Harvest v3: Costs 4 SP instead of 3
if attacker.sp >= 4:  # CHANGED: 4 instead of 3
    attacker.sp -= 4
    base_damage = 4
    cards_recovered = 4
```
- **Effect:** Forces choice between Soul Harvest OR movement
- **Target WR:** 55-60%

**Option 3: Diminishing Returns (Recommended)**
```python
# Soul Harvest v4: Weakens after repeated use
if attacker.sp >= 3:
    attacker.sp -= 3
    base_damage = 4

    # Diminishing returns: reduce recovery if used too much
    if attacker.lifesteal_healed < 12:
        cards_recovered = 4
    elif attacker.lifesteal_healed < 24:
        cards_recovered = 3
    else:
        cards_recovered = 2  # Late game: only 50% lifesteal
```
- **Effect:** Strong early, weakens late game
- **Prevents:** Infinite grind wars
- **Target WR:** 50-55%

---

## ELVES (65.6% WR - Strong DoT)

### Current Implementation:
```python
base_damage = 3
defender.bleed_counters = min(defender.bleed_counters + 2, 10)
# End of turn: deal bleed_counters damage, reduce by 1
```

### Why Strong:

1. **Bleed Stacks Fast**
   - +2 bleed per attack
   - Reaches 10 bleed cap by turn 5
   - Turn 6+: dealing 3 (attack) + 10 (bleed) = 13 damage per turn cycle!

2. **Bypasses All Defenses**
   - Bleed damage happens at end of turn
   - Dwarven runes don't reduce it
   - Lifesteal doesn't counter it
   - No way to remove bleed in simulation

3. **Exponential Scaling**
   - Early game: 3 damage (weak)
   - Mid game: 3 + 6 bleed = 9 damage (strong)
   - Late game: 3 + 10 bleed = 13 damage (OP)

### Match Results Showing Strength:
- vs Exchange: 80% WR
- vs Dwarves: 75% WR (counters the tank!)
- vs Crucible: 70% WR
- vs Bloodlines: 70% WR
- vs Wyrd: 70% WR
- vs Nomads: 65% WR
- vs Church: 65% WR

**Only balanced matchups:** Ossuarium (50%), Emergent (55%)

### Proposed Fixes:

**Option 1: Slower Bleed Stacking**
```python
# Bleed v2: +1 per attack instead of +2
base_damage = 3
defender.bleed_counters = min(defender.bleed_counters + 1, 8)  # Also lower cap
```
- **Effect:** Takes 8 turns to cap instead of 5
- **Target WR:** 55-60%

**Option 2: Bleed Decay**
```python
# Bleed v3: Decays by 2 instead of 1
base_damage = 3
defender.bleed_counters = min(defender.bleed_counters + 2, 10)

# End of turn damage (in simulate_turn):
if defender.bleed_counters > 0:
    bleed_dmg = defender.bleed_counters
    defender.take_damage(bleed_dmg)
    defender.bleed_counters = max(0, defender.bleed_counters - 2)  # CHANGED: -2
```
- **Effect:** Must continuously apply bleed to maintain
- **Rewards aggression, punishes passive play
- **Target WR:** 55-60%

**Option 3: Lower Damage (Recommended)**
```python
# Bleed v4: Base attack reduced to 2
base_damage = 2  # CHANGED: 2 instead of 3
defender.bleed_counters = min(defender.bleed_counters + 2, 10)
```
- **Effect:** Early game weaker (2 dmg), late game same (2 + 10 bleed = 12)
- **Total damage reduced but DoT fantasy maintained**
- **Target WR:** 55-60%

---

## DWARVES (61.9% WR - Tank Too Strong)

### Current Implementation:
```python
# Gain 1 rune every 2 turns (max 3)
if self.turn % 2 == 0 and attacker.rune_counters < 3:
    attacker.rune_counters += 1

# In take_damage:
if self.faction == "dwarves":
    reduction = min(self.rune_counters, 3)
    amount = max(1, amount - reduction)  # -3 damage at max runes
```

### Why Strong:

1. **Becomes Unkillable Late Game**
   - By turn 6: Has 3 runes = -3 damage reduction
   - Takes 4 damage → reduced to 1 damage
   - Takes 3 damage → reduced to 1 damage
   - Minimum 1 damage means can survive 44 attacks!

2. **Free Rune Stacking**
   - Gains runes automatically (no cost)
   - Never loses runes
   - Reaches max defense quickly

3. **Vs Ossuarium Stalemate**
   - Ossuarium deals 4 damage → reduced to 1
   - Dwarves gain 1 rune every 2 turns
   - Ossuarium recovers 4 cards per attack
   - **Result:** All 20 matches hit 150-turn limit, 18 draws!

### Match Results Showing Issues:
- vs Ossuarium: 0% WR but 18/20 draws (stalemate!)
- vs Emergent: 95% WR (19-0-1)
- vs Nomads: 85% WR (17-1-2)
- vs Wyrd: 85% WR (17-0-3)
- vs Exchange: 80% WR (16-0-4)
- vs Crucible: 80% WR (16-0-4)
- vs Bloodlines: 75% WR (15-0-5)

**Counters:** Elves (15% WR - bleed bypasses defense), Church (35% WR - burst damage)

### Proposed Fixes:

**Option 1: Slower Rune Gain**
```python
# Rune v2: Gain 1 rune every 3 turns instead of every 2
if self.turn % 3 == 0 and attacker.rune_counters < 3:
    attacker.rune_counters += 1
```
- **Effect:** Reaches max defense by turn 9 instead of turn 6
- **Target WR:** 55-58%

**Option 2: Rune Decay**
```python
# Rune v3: Lose 1 rune every 4 turns
if self.turn % 2 == 0 and attacker.rune_counters < 3:
    attacker.rune_counters += 1

# End of turn decay:
if self.turn % 4 == 0 and attacker.rune_counters > 0:
    attacker.rune_counters -= 1
```
- **Effect:** Fluctuates between 2-3 runes, never permanent max
- **Target WR:** 55-60%

**Option 3: Lower Cap (Recommended)**
```python
# Rune v4: Max 2 runes instead of 3
if self.turn % 2 == 0 and attacker.rune_counters < 2:  # CHANGED: max 2
    attacker.rune_counters += 1

# In take_damage:
reduction = min(self.rune_counters, 2)  # CHANGED: max 2 reduction
amount = max(1, amount - reduction)
```
- **Effect:** 4 dmg → 2 dmg instead of 1 dmg
- **Still tanky but not unkillable**
- **Target WR:** 52-57%

---

## Recommended Implementation Priority

### Phase 1 (Critical - Prevents Stalemates):
1. **Dwarves: Lower rune cap to 2** (prevents Ossuarium stalemate)
2. **Ossuarium: Reduce lifesteal to 3 cards** (75% lifesteal instead of 100%)

### Phase 2 (Important - General Balance):
3. **Elves: Reduce base damage to 2** (keeps DoT fantasy, lowers early burst)

### Expected Results After Phase 1+2:
- Ossuarium: 66.9% → 55-58% WR
- Elves: 65.6% → 55-58% WR
- Dwarves: 61.9% → 52-55% WR
- Church: 50.0% → 50-52% WR (unchanged, already balanced!)
- Bottom 6: Should naturally rise to 40-45% WR as S-tier comes down

---

## Additional Considerations

### Why Bottom 6 Factions Are Weak (34-37% WR):

The simulation might be missing key mechanics for:
- **Nomads** (40% WR with generics - needs improvisation mechanic?)
- **Bloodlines** (36% WR - needs Biomass absorption mechanic?)
- **Crucible** (35% WR - needs honor duel/forge mechanic?)
- **Exchange** (35% WR - needs credit economy mechanic?)
- **Wyrd** (34% WR - needs reality distortion mechanic?)
- **Emergent** (34% WR - needs Metamorph mechanics?)

These factions are using generic 4-damage attacks with no faction mechanics in the simulation!

### Next Steps:
1. **Nerf S-tier first** (bring down to 50-55% WR)
2. **Then implement bottom-tier mechanics** (bring up from 34-37% to 45-50%)
3. **Final balance pass** once all factions have proper mechanics
