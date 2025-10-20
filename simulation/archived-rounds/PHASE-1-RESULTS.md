# Phase 1 Balance Fixes - Results

**Date**: 2025-10-20
**Target**: Achieve 7-10 factions in 45-55% WR range

---

## Changes Applied

### 1. Deck Size Reduction (-20%)
- Scout: 28 → 22 HP
- Warden: 34 → 28 HP
- Vanguard: 40 → 34 HP
- Colossus: 50 → 44 HP

**Result**: Combat length reduced ~20% (faster, less grindy)

### 2. Hit Target Reduction (5+ → 4+)
- Base hit target: 5+ → 4+
- Expected hit rate: 72% → 83%

**Result**: Hit rate improved from 57% to 59% (still not at target due to range modifiers)

### 3. Church "Cannot Miss" Removed
- Removed auto-hit bypass for Church equipment
- Church now rolls dice like everyone else

**Result**: Church dropped from 100% → 97.8% WR (minimal impact!)

### 4. Elves Bleed - Apply on ATTACK (not on HIT)
```python
# OLD: Bleed only applied if attack hits
if attack_hits:
    apply_bleed()

# NEW: Bleed applied on attack declaration
apply_bleed()  # Guaranteed
if attack_hits:
    deal_damage()
```

**Result**: Elves surged from 0.0% → **75.6%** WR! (MASSIVE change)

### 5. Crucible Forge - Generate on ATTACK (not on HIT)
```python
# OLD: Forge only generated if attack hits
if attack_hits:
    gain_forge()

# NEW: Forge generated on attack declaration
gain_forge()  # Guaranteed
if attack_hits:
    deal_damage()
```

**Result**: Crucible dropped from 24% → **11.1%** WR (WORSE!)

---

## Results Comparison

| Faction | Pre-Phase 1 | Post-Phase 1 | Change | Status |
|---------|-------------|--------------|--------|--------|
| Church | 100.0% | **97.8%** | -2.2% | Still broken |
| Ossuarium | 75.6% | **86.7%** | +11.1% | Worse! |
| Elves | **0.0%** | **75.6%** | **+75.6%** 🔥 | Fixed but OP |
| Dwarves | 84.4% | 73.3% | -11.1% | Improved |
| Wyrd | 66.7% | **55.6%** | -11.1% | Almost balanced! |
| Bloodlines | 55.6% | **44.4%** | -11.1% | Almost balanced! |
| Exchange | 44.4% | 33.3% | -11.1% | Worse |
| Emergent | 35.6% | 22.2% | -13.4% | Worse |
| Crucible | 24.4% | **11.1%** | -13.3% | Much worse! |
| Nomads | 13.3% | **0.0%** | -13.3% ☠️ | Collapsed! |

**Balance Score**: 0/10 (target: 7-10 in 45-55% range)

---

## Key Findings

### 1. "On Attack" Mechanics Are EXTREMELY Powerful

**Elves Bleed** (on attack):
- 0% WR → 75.6% WR (+75.6%!)
- Guaranteed bleed stacking (even on miss)
- Over 20 turns × 60% hit rate × bleed stacks = 30-40 bleed damage
- **WAY too strong**

**Crucible Forge** (on attack):
- Expected to improve (24% → ~45%)
- Actually got WORSE (24% → 11%)
- **Why?** Forge tokens generated, but Crucible equipment still too weak

### 2. Church "Cannot Miss" Was NOT the Problem

- Removed auto-hit → Only dropped 2.2% (100% → 97.8%)
- Church still dominates with **regular dice rolls**
- **Real issue**: Church equipment damage is too high (even after nerfs)
- Divine Judgment 6 damage (faction card, not equipment) is still broken

### 3. Ossuarium Got Stronger (Unintended)

- 75.6% → 86.7% (+11.1%)
- **Why?** Shorter combats favor burst lifesteal
- Lifesteal more valuable when games end in 20-25 turns

### 4. Nomads Collapsed (0% WR)

- 13.3% → 0.0% (lost all 45 games!)
- **Why?** Movement costs SP, shorter combats = less time to position
- Nomads rely on mobility, but reduced deck sizes favor static attackers

---

## Problems with Current Balance

### Overpowered Tier (>60% WR)
1. **Church (97.8%)**: Equipment damage still too high
2. **Ossuarium (86.7%)**: Lifesteal too strong in short games
3. **Elves (75.6%)**: Bleed on-attack too guaranteed
4. **Dwarves (73.3%)**: High damage + tanky

### Almost Balanced (45-60% WR)
5. **Wyrd (55.6%)**: Close! Reality Fracture viable
6. **Bloodlines (44.4%)**: Close! Just needs +1-2 damage

### Catastrophically Weak (<20% WR)
7. Exchange (33.3%)
8. Emergent (22.2%)
9. **Crucible (11.1%)**: Forge mechanic still broken
10. **Nomads (0.0%)**: Movement penalty too harsh

---

## Why Crucible Got WORSE Despite Fix

**Expected**: Forge generation on-attack → Token economy viable → 45-50% WR

**Reality**: Crucible 24% → 11% WR (even worse!)

**Investigation**:
1. Forge tokens ARE generating on attack now ✓
2. But Crucible **equipment damage is too low** after nerf (Round 7 balance pass)
3. Crucible equipment was nerfed from ~5 avg damage → ~3 avg damage
4. Even with Forge tokens, 3 base damage + 2 bonus (Forge) = 5 total
5. **5 damage is not enough** when Church deals 6-8 damage baseline

**Fix Needed**: Restore Crucible equipment damage (undo Round 7 nerfs)

---

## Why Nomads Collapsed

**Expected**: Faster combats benefit all factions equally

**Reality**: Nomads 13% → 0% WR (catastrophic)

**Root Cause**:
- Nomads rely on **mobility** (hit-and-run, flanking)
- Movement costs **1 SP/hex**
- With Warden (5 SP max), moving 2 hexes = 2 SP
- **Only 3 SP left for attacks** (can't afford high-cost cards)
- In short combats (20-25 turns), Nomads **never get value from positioning**

**Fix Needed**:
1. Reduce movement cost to **1 SP/2 hexes** (round down)
2. OR increase Nomads equipment damage significantly

---

## Recommendations for Phase 2

### NERF (Top 4):
1. **Church**: Reduce equipment damage by -2 across the board (AGAIN)
2. **Ossuarium**: Reduce lifesteal recovery (2 cards → 1 card)
3. **Elves**: Reduce bleed application to "50% chance on attack" (not guaranteed)
4. **Dwarves**: Reduce base damage by -1

### BUFF (Bottom 4):
1. **Nomads**: Reduce movement cost to 1 SP/2 hexes OR +3 damage to all equipment
2. **Crucible**: Restore equipment damage (+2 to all attacks)
3. **Emergent**: +2 damage to all equipment
4. **Exchange**: +1 damage to all equipment

### KEEP (Near-Balanced):
5. **Wyrd**: No changes (55.6% WR is close!)
6. **Bloodlines**: +1 damage to most equipment (44.4% → ~50%)

---

## Expected Phase 2 Results

**After Nerfs/Buffs**:
- Church: 97.8% → ~60% WR
- Ossuarium: 86.7% → ~55% WR
- Elves: 75.6% → ~50% WR (if bleed made probabilistic)
- Dwarves: 73.3% → ~55% WR
- Wyrd: 55.6% → 55% WR (no change)
- Bloodlines: 44.4% → ~50% WR
- Exchange: 33.3% → ~45% WR
- Emergent: 22.2% → ~42% WR
- Crucible: 11.1% → ~48% WR (if damage restored)
- Nomads: 0.0% → ~40% WR (if movement cost reduced)

**Predicted Balance Score**: **8/10 factions** in 45-55% range

---

## Alternative: Simpler Approach

**Instead of complex nerfs/buffs**, try:

### Global Damage Scaling
```python
# Apply faction multipliers to all equipment damage
FACTION_DAMAGE_MULTIPLIER = {
    'church': 0.7,       # -30% damage (97.8% → ~60%)
    'ossuarium': 0.8,    # -20% damage (86.7% → ~65%)
    'elves': 0.85,       # -15% damage (75.6% → ~60%)
    'dwarves': 0.9,      # -10% damage (73.3% → ~60%)
    'wyrd-conclave': 1.0,  # No change (55.6% = good)
    'vestige-bloodlines': 1.1,  # +10% damage (44.4% → ~52%)
    'exchange': 1.2,     # +20% damage (33.3% → ~48%)
    'emergent': 1.3,     # +30% damage (22.2% → ~45%)
    'crucible': 1.4,     # +40% damage (11.1% → ~45%)
    'nomads': 1.6,       # +60% damage (0% → ~40%)
}
```

**Pros**: Simple, reversible, easy to test
**Cons**: Doesn't address root causes (movement cost, bleed mechanics)

---

## Next Steps

1. **Decide**: Card-by-card balance OR global multipliers?
2. **Implement Phase 2 fixes**
3. **Rerun simulation** (target: 8/10 factions in 45-55%)
4. **If successful**: Document final balance, move to complete damage system
5. **If unsuccessful**: Iterate with smaller adjustments

---

**Status**: Phase 1 showed Elves fix works (0% → 75.6%), but created new imbalances. Need Phase 2 aggressive nerfs/buffs.
