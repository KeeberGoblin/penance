# Critical Simulation Fixes Needed

## Summary of Issues

The combat simulator has **completely wrong mechanics** for Church, Dwarves, and Ossuarium. This explains the catastrophic balance issues:
- **Church: 17.8% WR** (should be ~50%)
- **Dwarves: 93.1% WR** (should be ~50%)
- **Ossuarium: 81.1% WR** (should be ~50%)

---

## CHURCH OF ABSOLUTION - Critical Fixes

### Current (WRONG) Implementation:
```python
# Blood Offering: Self-harm HP for damage boost
if len(attacker.hand) >= 3:
    attacker.take_damage(1)        # WRONG: Loses HP
    blood_offering_bonus = 3
base_damage = 4 + blood_offering_bonus  # 7 damage
```

### Actual Card Data (complete-card-data.json line 181):
```json
{
  "name": "Blood Offering",
  "type": "gambit",
  "cost": 0,
  "effect": "Discard 1 card from top of your deck (self-harm). Your next attack this turn: +3 damage, ignores 1 Defense, and -1 to target number (easier to hit). LIMIT: 1 per turn."
}
```

### Correct Implementation:
```python
# Blood Offering: Discard cards for damage boost (NOT HP loss!)
if len(attacker.hand) >= 3 and len(attacker.deck) >= 1:
    # Discard 1 card from top of deck
    if attacker.deck:
        discarded = attacker.deck.popleft()
        attacker.discard.append(discarded)
        attacker._invalidate_hp_cache()

    blood_offering_bonus = 3
    # In simulation: -1 to hit = auto-hit (skip accuracy check)

base_damage = 4 + blood_offering_bonus  # 7 damage
```

**Why this fixes Church:**
- Old: Church loses HP faster than enemy (suicide mechanic)
- New: Church discards cards (like drawing extra for burst), still costs resources but doesn't kill itself
- Net trade: Lose 1 card now, deal +3 damage = positive trade if it kills enemy faster

---

## DWARVEN FORGE-GUILDS - Critical Fixes

### Current (WRONG) Implementation:
```python
# Rune Stacking: FREE offensive damage boost
attacker.rune_counters += 2        # WRONG: Free runes
attacker.heat += 1
base_damage = 3 + min(attacker.rune_counters // 2, 5)  # WRONG: Offensive damage
```

**Turn 5: 10 runes = 3 + 5 = 8 damage per turn = BROKEN**

### Actual Card Data (complete-card-data.json line 542):
```json
{
  "name": "Rune of Protection",
  "type": "buff",
  "cost": 2,
  "effect": "Gain 1 Rune Counter. While you have Rune Counters, reduce all damage by 1 per counter (max 3 counters). Duration: Until end of mission or destroyed."
}
```

### Correct Implementation:
```python
# Dwarves should use DEFENSIVE runes (damage reduction), not offensive
# Runes are gained by PLAYING CARDS (costs 2 SP), not automatic!

# In simulate_attack_phase for Dwarves:
def simulate_attack_phase(self, attacker, defender, ...):
    if attacker.faction == "dwarves":
        # Option 1: Play Rune of Protection (costs 2 SP, once per several turns)
        # Since this is simplified simulation, apply 1 rune every 3 turns
        if attacker.turn_count % 3 == 0 and attacker.rune_counters < 3:
            attacker.rune_counters += 1
            attacker.sp -= 2  # Cost to play

        # Attack: Crushing Blow (4 damage, armor-piercing)
        base_damage = 4
        defender.take_damage(base_damage)

        # Runes provide DEFENSE, not offense!
        # (Applied in take_damage function)

# In take_damage function:
def take_damage(self, amount: int):
    # Apply Dwarven rune reduction
    if self.faction == "dwarves" and self.rune_counters > 0:
        reduction = min(self.rune_counters, 3)  # Max 3 reduction
        amount = max(1, amount - reduction)  # Minimum 1 damage

    # ... rest of damage logic
```

**Alternative Simplified Implementation (Balanced):**
```python
# Simplified Dwarven mechanics for simulation
if attacker.faction == "dwarves":
    # Crushing Blow: 4 damage, armor-piercing
    base_damage = 4
    defender.take_damage(base_damage)

    # Gain 1 rune every 2 turns (slow defensive stacking)
    if self.turn % 2 == 0 and attacker.rune_counters < 3:
        attacker.rune_counters += 1

# Defensive rune application (in take_damage):
if self.faction == "dwarves":
    damage_reduction = min(self.rune_counters, 3)
    amount = max(1, amount - damage_reduction)
```

**Why this fixes Dwarves:**
- Old: Free +5 damage by turn 5 = exponential scaling = 100% WR
- New: Defensive runes reduce incoming damage, not boost outgoing
- Balanced: Dwarves become tanky attrition fighters (as designed), not glass cannons

---

## THE OSSUARIUM - Critical Fixes

### Current (WRONG) Implementation:
```python
# Lifesteal: FREE (no SP cost), recycle 2 cards
base_damage = 4
for _ in range(2):
    if attacker.discard:
        recycled = attacker.discard.pop()
        attacker.hand.append(recycled)
```

**Problem: FREE sustain every attack = infinite grind**

### Actual Card Data (complete-card-data.json line 844):
```json
{
  "name": "Soul Harvest",
  "type": "attack",
  "cost": 3,
  "effect": "Deal 4 damage. Recover cards equal to damage dealt from your discard pile (max 4 cards)."
}
```

### Correct Implementation:
```python
# Soul Harvest: Costs 3 SP (not free!)
if attacker.faction == "ossuarium":
    # Check if enough SP to use Soul Harvest
    if attacker.sp >= 3:
        # Use Soul Harvest (costs 3 SP)
        attacker.sp -= 3
        base_damage = 4
        defender.take_damage(base_damage)

        # Recover cards equal to damage dealt (max 4)
        cards_recovered = min(base_damage, 4)
        for _ in range(cards_recovered):
            if attacker.discard:
                recycled = attacker.discard.pop()
                attacker.hand.append(recycled)

        attacker._invalidate_hp_cache()
        self.log_event(f"{attacker.name} uses Soul Harvest for {base_damage} damage, recovers {cards_recovered} cards")
    else:
        # Not enough SP: use basic attack instead
        base_damage = 3
        defender.take_damage(base_damage)
        self.log_event(f"{attacker.name} attacks for {base_damage} damage (insufficient SP for Soul Harvest)")
```

**Why this fixes Ossuarium:**
- Old: Free lifesteal every attack = 70-110 turn grinds = 100% WR vs most factions
- New: Soul Harvest costs 3 SP (Warden has 5 SP = can only use once per turn max)
- Opportunity cost: Use Soul Harvest (sustain) OR save SP for movement/defense
- Still strong in long fights, but not oppressive

---

## Additional Faction Mechanics to Check

### Elves (55% WR - Actually Balanced!)
**Current implementation appears correct:**
```python
# Elves: Bleed stacking
base_damage = 3
defender.take_damage(base_damage)
defender.bleed_counters = min(defender.bleed_counters + 2, 10)
```

**Card data verification needed:** Check if bleed application is correct.

### Other Factions (40-44% WR)
All other factions are clustering around 40-44% WR, suggesting they might all be slightly underpowered OR the simulation is missing key mechanics for them as well.

**Recommended:** Review ALL faction mechanics against complete-card-data.json to ensure accuracy.

---

## Implementation Priority

### Priority 1 (Critical - Breaks Game Balance):
1. **Fix Dwarves offensive → defensive runes** (93.1% WR → ~50% WR expected)
2. **Fix Church HP loss → card discard** (17.8% WR → ~50% WR expected)
3. **Fix Ossuarium free lifesteal → 3 SP cost** (81.1% WR → ~50-55% WR expected)

### Priority 2 (Important - Verify Mechanics):
4. Verify Elves bleed mechanics (currently 55% WR - looks balanced)
5. Review Crucible, Exchange, Nomads, Bloodlines, Emergent, Wyrd (all 40-44% WR)

### Priority 3 (Quality of Life):
6. Add faction-specific passives (Phylactery, Righteous Fury, etc.)
7. Add SP costs to all abilities (currently many are free)
8. Add card-based decision making (when to use which card)

---

## Expected Results After Fixes

**Current Broken State:**
- Dwarves: 93.1% WR (8/9 matchups perfect 100%)
- Ossuarium: 81.1% WR (6/9 matchups perfect 100%)
- Church: 17.8% WR (loses to everyone)

**Expected After Fixes:**
- Dwarves: ~50-55% WR (defensive tank, wins long fights)
- Ossuarium: ~50-55% WR (sustain specialist, wins attrition)
- Church: ~45-50% WR (burst damage, wins fast fights)
- Elves: ~50-55% WR (DoT specialist, counters sustain)

**Rock-Paper-Scissors (Intended):**
- Elves (Bleed) > Ossuarium (Lifesteal) ✓ (Already working: 75% WR)
- Church (Burst) > Fast fights
- Dwarves (Tank) > Church (Survive burst)
- Ossuarium (Sustain) > Dwarves (Grind down)

---

## Testing After Fixes

Run the same faction matchup test (20 runs × 90 matchups) and verify:
1. **No faction above 60% overall WR**
2. **No faction below 40% overall WR**
3. **No 100% or 0% matchups** (every matchup should be 30-70% WR range)
4. **Average match length: 15-30 turns** (not 9 turns for Dwarves, not 100+ for Ossuarium)
