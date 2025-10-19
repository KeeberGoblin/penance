# Faction Balance Analysis: Church, Dwarves, Ossuarium

## Current Implementation Analysis

### CHURCH OF ABSOLUTION (17.8% WR - BROKEN WEAK)

**Current Mechanic:**
```python
# Blood Offering: Self-harm for damage boost
if len(hand) >= 3:
    attacker.take_damage(1)        # Pay 1 HP
    blood_offering_bonus = 3       # Gain +3 damage
base_damage = 4 + blood_offering_bonus  # Total: 7 damage
```

**Net Trade:**
- Church deals: **7 damage** (4 base + 3 bonus)
- Church pays: **1 HP** (self-harm)
- **Net: 7 damage for 1 HP**

**Why This Fails:**

1. **Death Spiral Acceleration**
   - Taking 1 damage = 1 card lost from hand/deck
   - Fewer cards = faster reshuffle
   - Faster reshuffle = more DAMAGED cards added
   - More DAMAGED cards = death spiral accelerates

2. **Math Doesn't Add Up**
   - Church attacks for 7 damage (costs 1 HP to self)
   - Enemy attacks back for ~4 damage
   - **Net result: Church loses MORE HP than enemy!**
   - Church: -1 (self-harm) -4 (enemy) = **-5 HP**
   - Enemy: -7 HP
   - Trade ratio: Church loses 5 to deal 7 = **71% efficiency**

3. **No Sustain Mechanic**
   - Every other faction either:
     - Deals more damage (Dwarves)
     - Has sustain (Ossuarium lifesteal)
     - Has DoT (Elves bleed)
   - Church has NEGATIVE sustain (self-harm)

4. **Hand Requirement is a Trap**
   - Requires 3+ cards in hand to activate
   - Late game: hand is full of DAMAGED cards
   - Can't use Blood Offering when desperate (when you need it most!)

**Why Church Loses to Everyone:**
- vs Dwarves: Dwarves ramp to 8+ damage by turn 5, Church kills itself before dealing enough damage
- vs Ossuarium: Church self-harms while Ossuarium recycles cards, outlasting forever
- vs Elves: Bleed stacks faster than Church can kill, self-harm accelerates death
- vs Everyone else: Church trades HP for damage at a net loss

---

### DWARVEN FORGE-GUILDS (93.1% WR - CATASTROPHICALLY OP)

**Current Mechanic:**
```python
# Rune Stacking: Exponential scaling
attacker.rune_counters += 2        # Gain 2 runes per turn
attacker.heat += 1                 # Gain 1 heat per turn
base_damage = 3 + min(rune_counters // 2, 5)  # Damage scales, capped at +5
```

**Turn-by-Turn Breakdown:**

| Turn | Runes | Damage | Cumulative Damage |
|------|-------|--------|-------------------|
| 1    | 2     | 4      | 4                 |
| 2    | 4     | 5      | 9                 |
| 3    | 6     | 6      | 15                |
| 4    | 8     | 7      | 22                |
| 5    | 10+   | 8      | 30                |

**Why This is Broken:**

1. **Exponential Scaling with No Counterplay**
   - By turn 5: dealing 8 damage per turn (capped at +5 bonus)
   - Warden has 44 HP = dead in ~6 attacks
   - **Average Dwarves victory: 9.5 turns** (matches the math!)

2. **No Cost for Rune Stacking**
   - Gaining runes costs NOTHING except 1 heat
   - Heat only matters at 5+ (50% chance to lose 1 SP on Strain roll)
   - Even then: Warden has 5 SP, losing 1 SP still leaves 4 SP (enough to attack + move)

3. **Ramp is Too Fast**
   - +2 runes per turn
   - Reaches cap (+5 damage) by turn 5
   - Most factions can't kill Dwarves before they reach critical mass

4. **Cap is Too High**
   - 3 base + 5 bonus = **8 damage per turn**
   - Warden takes 5-6 hits to die
   - Dwarves kill in 5-6 turns, opponents need 8-10 turns
   - Dwarves ALWAYS win the race

**Why Dwarves Beat Everyone:**
- vs Church: Church kills itself faster than it kills Dwarves
- vs Ossuarium: Dwarves ramp faster than Ossuarium can recycle cards
- vs Elves: Dwarves kill Elves before bleed stacks high enough (9 turns vs 15+ turns for bleed kill)
- vs Everyone else: Exponential scaling beats everything

**Only Counter:**
- Ossuarium (65% WR): Lifesteal recycling + longer HP pool outlasts the ramp *sometimes*

---

### THE OSSUARIUM (81.1% WR - MASSIVELY OP)

**Current Mechanic:**
```python
# Lifesteal (Fixed version - recycles from discard)
base_damage = 4
for _ in range(2):
    if attacker.discard:
        recycled = attacker.discard.pop()
        attacker.hand.append(recycled)
        cards_recycled += 1
```

**Net Trade:**
- Ossuarium deals: **4 damage**
- Ossuarium recycles: **2 cards from discard to hand**

**Why This is Still OP:**

1. **Card Advantage = HP Advantage**
   - HP = cards in deck + hand
   - Recycling from discard doesn't ADD HP
   - BUT: Delays deck reshuffles, which delays DAMAGED card additions
   - Fewer DAMAGED cards = slower death spiral

2. **Attrition Warfare Master**
   - Average battle length vs weak factions: **70-110 turns**
   - Ossuarium never runs out of cards (recycling keeps hand full)
   - Opponents eventually reshuffle, get DAMAGED cards, death spiral

3. **No Opportunity Cost**
   - Attacking for 4 damage AND recycling 2 cards
   - Other factions: attack OR special ability
   - Ossuarium: attack AND special ability

4. **Infinite Scaling**
   - Discard pile grows every turn (from attacks, card plays)
   - More cards in discard = more recyclable fuel
   - Late game: Ossuarium has 20+ cards in discard to recycle from

**Why Ossuarium Beats Most Factions:**
- vs Church: Church kills itself, Ossuarium recycles forever
- vs Crucible/Exchange/Nomads/Bloodlines/Emergent/Wyrd: Ossuarium grinds them down in 70-100 turn wars
- vs Elves: **LOSES 75%!** Bleed damage bypasses recycling (DoT ticks regardless of hand size)
- vs Dwarves: **LOSES 65%!** Dwarves ramp faster than Ossuarium can grind

---

## Balance Recommendations

### CHURCH: Needs Major Buffs

**Option 1: Remove Self-Harm Entirely**
```python
# Blood Offering v2: Sacrifice cards instead of HP
if len(hand) >= 3:
    # Discard 1 card for +4 damage (instead of 1 HP for +3 damage)
    attacker.discard.append(attacker.hand.popleft())
    blood_offering_bonus = 4
base_damage = 4 + blood_offering_bonus  # Total: 8 damage
```
- **Effect:** Trade hand size for damage (still risky but doesn't kill yourself)
- **Target WR:** 45-50%

**Option 2: Add Sustain to Offset Self-Harm**
```python
# Blood Offering v3: Self-harm with sustain
if len(hand) >= 3:
    attacker.take_damage(1)
    blood_offering_bonus = 5  # Increase bonus to +5
    # Recycle 1 card from discard (mini-lifesteal)
    if attacker.discard:
        attacker.hand.append(attacker.discard.pop())
base_damage = 4 + blood_offering_bonus  # Total: 9 damage
```
- **Effect:** High risk, high reward, with some sustain
- **Target WR:** 50-55%

**Option 3: Conditional Bonus Without Cost**
```python
# Blood Offering v4: Bonus damage at low HP (no cost)
if attacker.hp <= 22:  # Half HP or less
    blood_offering_bonus = 4
else:
    blood_offering_bonus = 0
base_damage = 4 + blood_offering_bonus
```
- **Effect:** Becomes dangerous when desperate (clutch potential)
- **Target WR:** 45-50%

---

### DWARVES: Needs Major Nerfs

**Option 1: Slower Ramp**
```python
# Rune Stacking v2: +1 rune per turn instead of +2
attacker.rune_counters += 1  # Changed from 2
attacker.heat += 1
base_damage = 3 + min(attacker.rune_counters // 2, 4)  # Cap at +4 instead of +5
```
- **Effect:** Half speed ramp, lower cap
- **Turn 5 damage:** 5 instead of 8
- **Target WR:** 60-65%

**Option 2: Rune Decay**
```python
# Rune Stacking v3: Runes decay over time
attacker.rune_counters += 2
attacker.heat += 1

# At end of turn: lose 1 rune
attacker.rune_counters = max(0, attacker.rune_counters - 1)

base_damage = 3 + min(attacker.rune_counters // 2, 5)
```
- **Effect:** Net gain of +1 rune per turn, requires stacking
- **Equilibrium:** ~10 runes max (+5 damage)
- **Target WR:** 55-60%

**Option 3: Heat Penalty**
```python
# Rune Stacking v4: Heat actually matters
attacker.rune_counters += 2
attacker.heat += 2  # Gain 2 heat instead of 1

# Damage reduced by heat
heat_penalty = max(0, (attacker.heat - 3))  # Every heat above 3 reduces damage by 1
base_damage = 3 + min(attacker.rune_counters // 2, 5) - heat_penalty
```
- **Effect:** High runes = high heat = damage penalty
- **Balance:** Must manage heat or lose damage output
- **Target WR:** 50-55%

---

### OSSUARIUM: Needs Moderate Nerfs

**Option 1: Recycle Less**
```python
# Lifesteal v2: Recycle 1 card instead of 2
base_damage = 4
if attacker.discard:
    recycled = attacker.discard.pop()
    attacker.hand.append(recycled)
    cards_recycled = 1  # Changed from 2
```
- **Effect:** Still sustains, but slower
- **Target WR:** 60-65%

**Option 2: Lifesteal Diminishing Returns**
```python
# Lifesteal v3: Diminishing returns after 10 recycled
base_damage = 4
max_recycle = 2 if attacker.lifesteal_healed < 10 else 1
for _ in range(max_recycle):
    if attacker.discard:
        recycled = attacker.discard.pop()
        attacker.hand.append(recycled)
        attacker.lifesteal_healed += 1
```
- **Effect:** Strong early, weakens late game
- **Target WR:** 55-60%

**Option 3: Conditional Lifesteal**
```python
# Lifesteal v4: Only recycle if hand is small
base_damage = 4
if len(attacker.hand) < 5:  # Only recycle if hand is small
    for _ in range(2):
        if attacker.discard:
            attacker.hand.append(attacker.discard.pop())
```
- **Effect:** Prevents infinite hand size, still provides sustain
- **Target WR:** 60-65%

---

## Summary

**Church Problems:**
1. Self-harm with no sustain = suicide
2. Math doesn't favor trades
3. Hand requirement limits flexibility

**Dwarves Problems:**
1. Exponential scaling too fast (+2 runes/turn)
2. Cap too high (+5 damage)
3. No meaningful cost (heat doesn't matter)

**Ossuarium Problems:**
1. Recycles too many cards (2 per attack)
2. No diminishing returns
3. Wins through attrition (70-110 turn grinds)

**Recommended Changes Priority:**
1. **Church:** Buff immediately (17.8% WR is unplayable)
2. **Dwarves:** Nerf immediately (93.1% WR breaks the game)
3. **Ossuarium:** Nerf soon (81.1% WR warps meta)
