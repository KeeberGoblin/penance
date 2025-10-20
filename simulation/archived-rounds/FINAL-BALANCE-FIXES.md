# Final Balance Fixes - Round 3

## Current State After S-Tier Nerfs

| Faction | WR% | Status | Key Issue |
|---------|-----|--------|-----------|
| **Elves** | 78.9% | BROKEN | 6/9 matchups at 100%, killing in 9 turns |
| **Dwarves** | 69.4% | TOO STRONG | Still 100% vs 6 factions, stalemate vs Ossuarium |
| **Ossuarium** | 68.6% | TOO STRONG | Still 100% vs 6 factions, stalemate vs Dwarves |
| **Church** | 55.6% | BALANCED ✓ | Working perfectly! |
| **Crucible** | 34.2% | WEAK | 0% vs top 3, needs faction mechanics |
| **Bloodlines** | 33.9% | WEAK | 0% vs top 3, needs faction mechanics |
| **Nomads** | 33.3% | WEAK | 0% vs top 3, needs faction mechanics |
| **Emergent** | 33.3% | WEAK | 0% vs top 3, needs faction mechanics |
| **Wyrd** | 30.3% | WEAK | 0% vs top 3, needs faction mechanics |
| **Exchange** | 25.0% | WEAKEST | 0% vs top 3, needs faction mechanics |

---

## PRIORITY 1: FIX ELVES (78.9% → 50-55%)

### Problem Analysis:
```python
# Current implementation:
base_damage = 2  # Reduced from 3
defender.bleed_counters = min(defender.bleed_counters + 2, 10)  # +2 bleed per attack

# Turn progression:
# Turn 1: 2 dmg + 2 bleed applied = 2 total
# Turn 2: 2 dmg + 4 bleed damage = 6 total (bleed reduced to 3)
# Turn 3: 2 dmg + 5 bleed damage = 7 total (bleed reduced to 4)
# Turn 4: 2 dmg + 6 bleed damage = 8 total (bleed reduced to 5)
# Turn 5: 2 dmg + 10 bleed cap = 12 damage per turn!
# Turn 6-9: 2 dmg + 10 bleed = 12 damage/turn = kills in 9 turns
```

**Why 100% WR vs Bottom-6:**
- Bottom-6 have no sustain mechanics (no lifesteal, no damage reduction)
- Bleed bypasses defenses completely
- 12 damage per turn from turn 5 onwards is unstoppable
- Warden has 44 HP → dead by turn 9

### Recommended Fix: SLOWER BLEED STACKING + FASTER DECAY

```python
# Elves v5: Slower stacking, faster decay
base_damage = 2
defender.bleed_counters = min(defender.bleed_counters + 1, 8)  # CHANGED: +1 per attack, cap 8

# End of turn bleed damage (in simulate_turn):
if defender.bleed_counters > 0:
    bleed_dmg = defender.bleed_counters
    defender.take_damage(bleed_dmg)
    defender.bleed_counters = max(0, defender.bleed_counters - 2)  # CHANGED: -2 decay
```

**Expected Result:**
- Turn 1: 2 dmg + 1 bleed applied
- Turn 2: 2 dmg + 1 bleed damage, reduced to 0, apply 1 more = 1 bleed
- Turn 3-8: Bleed oscillates between 0-2 (never stacks high)
- Turn 8: Eventually reaches cap of 8 bleed
- Max damage: 2 direct + 8 bleed = 10 damage/turn (vs 12 before)
- **Effect:** Much weaker early game, needs to maintain aggression
- **Target WR:** 50-55%

---

## PRIORITY 2: FIX DWARVES/OSSUARIUM STALEMATE

### Current Problem:
```python
# Ossuarium: 4 damage, recover 3 cards, costs 3 SP (Warden has 5 SP)
# Dwarves: -2 damage reduction (rune cap 2)
# Net: 4 - 2 = 2 damage dealt, 3 cards recovered = +1 HP advantage for Ossuarium
# But takes 150+ turns = automatic draw limit
```

**20/20 matches end in draw at 150-turn limit!**

### Recommended Fix: INCREASE SOUL HARVEST SP COST

```python
# Ossuarium v3: Increase SP cost from 3 → 4
if attacker.sp >= 4:  # CHANGED: 4 instead of 3
    attacker.sp -= 4
    base_damage = 4
    cards_recovered = 3  # 75% lifesteal
    # ... rest of Soul Harvest
else:
    # Not enough SP: use basic attack
    base_damage = 3
    defender.take_damage(base_damage)
```

**Why This Works:**
- Warden has 5 SP total
- Soul Harvest costs 4 SP → only 1 SP left for movement/defense
- Forces choice: Soul Harvest OR positioning
- Can't use Soul Harvest every single turn
- **Effect:** Ossuarium must alternate between Soul Harvest and basic attacks
- **vs Dwarves:** Basic attack (3 dmg - 2 runes = 1 dmg), no lifesteal
- **Result:** Dwarves can outlast Ossuarium in grind wars

**Expected Result:**
- Ossuarium: 68.6% → 55-58% WR
- Dwarves: 69.4% → 55-58% WR
- Dwarves vs Ossuarium: No longer stalemate, Dwarves slight advantage

---

## PRIORITY 3: IMPLEMENT BOTTOM-6 FACTION MECHANICS

Currently all bottom-6 factions use **generic 4-damage attacks** with no faction abilities!

### CRUCIBLE PACT (34.2% WR → 45-50%)

**Card Data (complete-card-data.json line 1102):**
```json
{
  "name": "Honor Duel",
  "type": "gambit",
  "cost": 1,
  "effect": "Challenge target enemy. Both pilots gain +2 to hit. Damage dealt this turn ignores Armor. If you win (deal more damage), gain +2 damage next turn."
}
```

**Implementation:**
```python
# Crucible: Honor Duel (high-risk, high-reward burst)
if attacker.sp >= 1:
    attacker.sp -= 1
    base_damage = 5  # +1 bonus damage from Honor Duel
    defender.take_damage(base_damage)
    # Next turn bonus (simplified)
    attacker.honor_duel_bonus = 2
    self.log_event(f"{attacker.name} uses Honor Duel for {base_damage} damage")
else:
    base_damage = 4  # Basic attack
    defender.take_damage(base_damage)
```

---

### EXCHANGE (25.0% WR → 45-50%)

**Card Data (complete-card-data.json line 1391):**
```json
{
  "name": "Mercenary Contract",
  "type": "gambit",
  "cost": 2,
  "effect": "Gain +2 damage this turn. If you destroy enemy components, gain 1 Credit Counter. Spend 3 Credits: Draw 3 cards."
}
```

**Implementation:**
```python
# Exchange: Credit economy (resource generation)
if attacker.sp >= 2 and attacker.credit_counters < 3:
    attacker.sp -= 2
    base_damage = 4 + 2  # +2 from Mercenary Contract
    defender.take_damage(base_damage)
    attacker.credit_counters += 1  # Gain credit
    self.log_event(f"{attacker.name} uses Mercenary Contract for {base_damage} damage, gains 1 credit")
elif attacker.credit_counters >= 3:
    # Spend 3 credits: draw 3 cards (sustain)
    attacker.credit_counters -= 3
    for _ in range(3):
        if attacker.discard:
            recycled = attacker.discard.pop()
            attacker.hand.append(recycled)
    attacker._invalidate_hp_cache()
    base_damage = 4
    defender.take_damage(base_damage)
    self.log_event(f"{attacker.name} spends 3 credits, recovers 3 cards")
else:
    base_damage = 4
    defender.take_damage(base_damage)
```

---

### NOMADS (33.3% WR → 45-50%)

**Card Data (complete-card-data.json line 1654):**
```json
{
  "name": "Improvised Weapon",
  "type": "attack",
  "cost": 1,
  "effect": "Deal 3-5 damage (random). Discard this card after use (one-time weapon)."
}
```

**Implementation:**
```python
# Nomads: Random burst damage (high variance)
import random
if attacker.sp >= 1:
    attacker.sp -= 1
    base_damage = random.randint(3, 6)  # 3-6 random damage
    defender.take_damage(base_damage)
    self.log_event(f"{attacker.name} uses Improvised Weapon for {base_damage} damage")
else:
    base_damage = 4
    defender.take_damage(base_damage)
```

---

### BLOODLINES (33.9% WR → 45-50%)

**Card Data (complete-card-data.json line 1923):**
```json
{
  "name": "Biomass Absorption",
  "type": "gambit",
  "cost": 2,
  "effect": "Absorb 2 cards from your discard pile. Your next attack: +2 damage and gains lifesteal (recover 1 card per 2 damage dealt)."
}
```

**Implementation:**
```python
# Bloodlines: Biomass absorption (burst + lifesteal)
if attacker.sp >= 2 and len(attacker.discard) >= 2:
    attacker.sp -= 2
    # Absorb 2 cards (add to hand)
    for _ in range(2):
        if attacker.discard:
            absorbed = attacker.discard.pop()
            attacker.hand.append(absorbed)
    attacker._invalidate_hp_cache()

    base_damage = 4 + 2  # +2 damage
    defender.take_damage(base_damage)

    # Lifesteal: recover 1 card per 2 damage (6 damage = 3 cards)
    cards_recovered = base_damage // 2
    for _ in range(cards_recovered):
        if attacker.discard:
            recycled = attacker.discard.pop()
            attacker.hand.append(recycled)
    attacker._invalidate_hp_cache()

    self.log_event(f"{attacker.name} uses Biomass Absorption for {base_damage} damage, recovers {cards_recovered} cards")
else:
    base_damage = 4
    defender.take_damage(base_damage)
```

---

### EMERGENT (33.3% WR → 45-50%)

**Card Data (complete-card-data.json line 2178):**
```json
{
  "name": "Metamorph",
  "type": "buff",
  "cost": 3,
  "effect": "Transform your casket. Gain +1 to all stats (HP, SP, damage) for 3 turns. After 3 turns, take 2 strain damage."
}
```

**Implementation:**
```python
# Emergent: Metamorph (temporary power spike)
if attacker.sp >= 3 and not hasattr(attacker, 'metamorph_turns'):
    attacker.sp -= 3
    attacker.metamorph_turns = 3
    base_damage = 4 + 1  # +1 from metamorph
    defender.take_damage(base_damage)
    self.log_event(f"{attacker.name} uses Metamorph, +1 damage for 3 turns")
elif hasattr(attacker, 'metamorph_turns') and attacker.metamorph_turns > 0:
    base_damage = 4 + 1
    defender.take_damage(base_damage)
    attacker.metamorph_turns -= 1
    if attacker.metamorph_turns == 0:
        attacker.take_damage(2)  # Strain damage
        self.log_event(f"{attacker.name} Metamorph ends, takes 2 strain damage")
        del attacker.metamorph_turns
else:
    base_damage = 4
    defender.take_damage(base_damage)
```

---

### WYRD CONCLAVE (30.3% WR → 45-50%)

**Card Data (complete-card-data.json line 2443):**
```json
{
  "name": "Reality Distortion",
  "type": "gambit",
  "cost": 2,
  "effect": "Force enemy to reroll 1 die (choose lowest). Your next attack: +2 damage and ignores Defense."
}
```

**Implementation:**
```python
# Wyrd: Reality Distortion (defense bypass)
if attacker.sp >= 2:
    attacker.sp -= 2
    base_damage = 4 + 2  # +2 damage, ignores defense
    # In simulation: bypasses Dwarven runes
    original_runes = defender.rune_counters if hasattr(defender, 'rune_counters') else 0
    if defender.faction == "dwarves":
        defender.rune_counters = 0  # Bypass rune defense

    defender.take_damage(base_damage)

    if defender.faction == "dwarves":
        defender.rune_counters = original_runes  # Restore runes

    self.log_event(f"{attacker.name} uses Reality Distortion for {base_damage} damage (ignores defense)")
else:
    base_damage = 4
    defender.take_damage(base_damage)
```

---

## EXPECTED RESULTS AFTER ALL FIXES

### Top-Tier (Should be 50-55% WR):
- **Church:** 55.6% → 52-55% (already balanced)
- **Ossuarium:** 68.6% → 55-58%
- **Dwarves:** 69.4% → 55-58%
- **Elves:** 78.9% → 50-55%

### Mid-Tier (Should be 45-52% WR):
- **Crucible:** 34.2% → 48-52% (with Honor Duel)
- **Bloodlines:** 33.9% → 48-52% (with Biomass)
- **Nomads:** 33.3% → 45-50% (with Improvised Weapon)
- **Emergent:** 33.3% → 48-52% (with Metamorph)
- **Wyrd:** 30.3% → 45-50% (with Reality Distortion)
- **Exchange:** 25.0% → 45-50% (with Credit economy)

### No More 100% or 0% Matchups:
- Target: All matchups between 30-70% WR
- No more 9-turn stomps
- No more 150-turn stalemates

---

## IMPLEMENTATION ORDER

1. **Fix Elves bleed** (most urgent - 78.9% WR with 100% matchups)
2. **Fix Ossuarium SP cost** (fixes Dwarves stalemate)
3. **Implement bottom-6 mechanics** (bring them up to competitive level)
4. **Run comprehensive test** (20 runs × 90 matchups = 1,800 battles)
5. **Final balance pass** if needed
