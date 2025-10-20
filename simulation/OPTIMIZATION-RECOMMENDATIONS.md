# Simulation & Game Balance Optimization Recommendations

**Date**: 2025-10-20
**Context**: After implementing dice mechanics and discovering catastrophic balance issues

---

## 1. CRITICAL BALANCE FIXES (Highest Priority)

### Church - Remove "Cannot Miss" Advantage

**Problem**: Church has 100% WR (perfect record) in dice simulator
**Root Cause**: "Cannot miss" cards bypass 42% natural miss rate

**Fix Options**:

**A. Remove "Cannot Miss" Entirely** (Recommended)
```
OLD: "This attack cannot miss. Deal 5 damage."
NEW: "Deal 5 damage."
```
- **Impact**: Church drops from 100% → ~85% WR (estimated)
- **Implementation**: Text change only
- **Risk**: Low (Church still has Blood Offering +3 damage buff)

**B. Replace with Advantage** (Better long-term)
```
OLD: "This attack cannot miss."
NEW: "Roll with Advantage (3d6, take 2 highest)."
```
- **Impact**: Church ~90% WR (still strong but not perfect)
- **Implementation**: Requires Advantage dice pool system (+100 lines code)
- **Benefit**: Adds tactical depth (positioning for Advantage)

**Recommendation**: **Option A** (remove "cannot miss") immediately, then implement Option B in v3.0 update.

---

### Elves - Bleed Application Timing

**Problem**: Elves have 0.0% WR (lost all 45 games)
**Root Cause**: Bleed only applies on HIT. With 60% hit rate, can't stack bleed before dying

**Fix**:

**Change Bleed to Apply on ATTACK** (not on HIT)
```
OLD: "Deal 4 damage. Apply 1 Bleed."
     (Bleed only applied if attack hits)

NEW: "Apply 1 Bleed to target. If this attack hits, deal 4 damage."
     (Bleed applies even on miss, damage on hit)
```

**Implementation**:
```python
# In execute_turn(), BEFORE roll_attack()
if 'bleed' in attack_card.effect.lower():
    # Apply bleed immediately (on attack declaration)
    defender.bleed_stacks = min(defender.bleed_stacks + 1, 4)  # Cap at 4
    self.log(f"  Applied 1 Bleed ({defender.bleed_stacks}/4 stacks)")

# Then roll attack normally (damage only if hit)
attack_result, bonus_damage = self.roll_attack(attacker, attack_card, target_number)
```

**Impact**: Elves ~40-50% WR (viable faction)
**Trade-off**: Reduce bleed cap from 6 → 4 to compensate

---

### Crucible - Forge Token Generation Timing

**Problem**: Crucible 62.2% → 24.4% WR (collapsed with dice)
**Root Cause**: Forge tokens only generate on HIT. Miss 4 attacks → 0 Forge → dead economy

**Fix**:

**Change Forge to Generate on ATTACK** (not on HIT)
```
OLD: "Deal 4 damage. Gain 1 Forge token."
     (Forge only gained if attack hits)

NEW: "Gain 1 Forge token. Deal 4 damage."
     (Forge gained on attack declaration, damage if hit)
```

**Implementation**:
```python
# In execute_turn(), BEFORE roll_attack()
if 'forge' in attack_card.effect.lower() and 'gain' in attack_card.effect.lower():
    # Grant Forge token immediately
    attacker.forge_tokens = min(attacker.forge_tokens + 1, 5)  # Cap at 5
    self.log(f"  Gained 1 Forge ({attacker.forge_tokens}/5 tokens)")

# Then roll attack normally
attack_result, bonus_damage = self.roll_attack(attacker, attack_card, target_number)
```

**Impact**: Crucible ~45-55% WR (balanced)

---

## 2. SIMULATOR CODE OPTIMIZATIONS

### A. Parallel Battle Execution

**Current**: Battles run sequentially (225 battles = ~45 seconds)
**Optimization**: Run battles in parallel using multiprocessing

**Implementation**:
```python
from multiprocessing import Pool

def run_battle_batch(args):
    """Run a single battle (for parallel execution)"""
    faction1, faction2, builder, run_id = args
    casket1 = builder.build_random_deck(faction1, CasketClass.WARDEN)
    casket2 = builder.build_random_deck(faction2, CasketClass.WARDEN)
    simulator = DiceCombatSimulator(casket1, casket2, verbose=False)
    return simulator.run_combat()

# In faction_balance_DICE.py
def run_faction_matchup_parallel(faction1, faction2, builder, runs=5):
    """Run battles in parallel"""
    with Pool(processes=4) as pool:
        args = [(faction1, faction2, builder, i) for i in range(runs)]
        results = pool.map(run_battle_batch, args)

    # Aggregate results
    wins_f1 = sum(1 for r in results if faction1 in r['winner'])
    wins_f2 = len(results) - wins_f1
    return {'wins_f1': wins_f1, 'wins_f2': wins_f2, ...}
```

**Impact**: 225 battles in ~12 seconds (4× speedup with 4 cores)
**Trade-off**: Higher memory usage, harder to debug

---

### B. Optimize Card Drawing (Deque Performance)

**Current**: Using `deque` for deck/hand/discard
**Issue**: Frequent `append`/`popleft` operations

**Optimization**: Pre-allocate deck size, use index pointers

**Before**:
```python
def draw_cards(self, count):
    for _ in range(count):
        if self.deck:
            self.hand.append(self.deck.popleft())
```

**After**:
```python
def draw_cards(self, count):
    # Batch draw (fewer operations)
    draw_count = min(count, len(self.deck))
    new_cards = [self.deck.popleft() for _ in range(draw_count)]
    self.hand.extend(new_cards)
```

**Impact**: ~10% faster combat resolution
**Risk**: None (logic identical, just batched)

---

### C. Cache Attack/Defense Die Probabilities

**Current**: Dice rolls use `random.choice()` every time
**Optimization**: Pre-generate dice roll table for faster lookups

**Implementation**:
```python
# Pre-generate 10,000 attack dice rolls at startup
ATTACK_ROLL_CACHE = [(AttackDie.roll(), AttackDie.roll()) for _ in range(10000)]
DEFENSE_ROLL_CACHE = [DefenseDie.roll() for _ in range(50000)]

# In combat
_attack_roll_index = 0
def roll_2d6_cached():
    global _attack_roll_index
    die1, die2 = ATTACK_ROLL_CACHE[_attack_roll_index % 10000]
    _attack_roll_index += 1
    return (die1, die2, die1 + die2)
```

**Impact**: ~15% faster dice rolling (high-frequency operation)
**Risk**: Less random (repeats after 10K rolls), harder to debug

**Verdict**: **Not worth it** (premature optimization, loses true randomness)

---

### D. Reduce Logging Overhead

**Current**: Verbose logging even when `verbose=False`
**Issue**: String formatting happens before log check

**Before**:
```python
self.log(f"{attacker.name} attacks with {attack_card.name} for {damage} damage")
```

**After**:
```python
if self.verbose:
    self.log(f"{attacker.name} attacks with {attack_card.name} for {damage} damage")
```

**Impact**: ~5% faster when verbose=False
**Implementation**: Wrap all log calls in `if self.verbose:`

---

## 3. GAME DESIGN OPTIMIZATIONS

### A. Reduce Combat Length (Too Grindy)

**Current**: Average 37.6 turns per battle (too long)
**Issue**: Combats feel grindy, death spiral is slow

**Option 1: Global Damage Buff** (+1 damage to all attacks)
```python
# In equipment_simulator_dice.py
base_damage = attack_card.damage + 1  # Global +1 damage buff
```
**Impact**: Combats end in ~25 turns (33% faster)
**Risk**: May break balance (test carefully)

**Option 2: Increase Starting Range** (currently 2 hexes, change to 0)
```python
# In Casket class
range: int = 0  # Start at melee range (was 2)
```
**Impact**: Less movement, more fighting, ~30% faster combats
**Trade-off**: Movement becomes less important

**Option 3: Reduce Deck Sizes** (fewer HP)
```python
# In CasketClass enum
SCOUT = ("Scout", 6, 22, 1)      # Was 28, now 22 (-6 HP)
WARDEN = ("Warden", 5, 28, 2)    # Was 34, now 28 (-6 HP)
VANGUARD = ("Vanguard", 4, 34, 3)  # Was 40, now 34 (-6 HP)
COLOSSUS = ("Colossus", 4, 44, 4)  # Was 50, now 44 (-6 HP)
```
**Impact**: -20% HP = -20% combat length = ~30 turns
**Risk**: Low (scales all factions equally)

**Recommendation**: **Option 3** (reduce deck sizes by ~20%) - cleanest solution

---

### B. Fix Hit Rate (Too Low)

**Current**: 57.8% actual hit rate (expected 72% for target 5+)
**Issue**: Attacks miss too often, feels frustrating

**Root Cause Analysis**:
```python
# Expected for target 5+ (no modifiers)
# Dice faces: [1, 2, 3, 4, 5, 0] × 2
# Rolls ≥5: {5,6,7,8,9,10} = 72.2% probability

# Observed: 57.8% hit rate
# Why? Range modifiers pushing target to 6+ (58% hit rate)
```

**Fix**: Reduce base target number from 5+ to 4+
```python
def calculate_to_hit_target(self, attacker, defender):
    base_target = 4  # Was 5, now 4 (+17% hit rate)
    # ... apply modifiers
```

**Impact**: 57.8% → 72% hit rate (matches expected value)
**Trade-off**: Combats end faster, "cannot miss" becomes less valuable

**Recommendation**: **Implement** - fixes core UX issue (attacks should land more often)

---

### C. Catastrophic Failure Rate (Too High)

**Current**: 7.9% observed (expected 2.78%)
**Issue**: Nearly 3× higher than expected - weapons jam too often

**Investigation Needed**:
```python
# Check if JAM face is weighted incorrectly
print(f"Attack die faces: {AttackDie.FACES}")
# Should print: [1, 2, 3, 4, 5, 0]
# If prints [0, 0, 1, 2, 3, 4, 5, 0] → BUG (double JAM)
```

**If Bug**: Fix FACES array
**If Correct**: Working as intended (simulator limitation - no movement modifiers tracked accurately)

---

## 4. DATA STRUCTURE OPTIMIZATIONS

### A. Use Dataclass Slots for Memory Efficiency

**Current**: Dataclasses use `__dict__` (slow attribute access)
**Optimization**: Enable `__slots__` for faster access

**Before**:
```python
@dataclass
class Casket:
    name: str
    faction: str
    # ... 15 more fields
```

**After**:
```python
@dataclass(slots=True)
class Casket:
    name: str
    faction: str
    # ... 15 more fields
```

**Impact**: ~20% faster attribute access, 15% less memory
**Risk**: None (Python 3.10+ required)

---

### B. Lazy Load Card Database

**Current**: Load entire 605-card JSON at startup (~200KB)
**Optimization**: Load only needed factions

**Implementation**:
```python
def load_faction_cards(faction: str):
    """Load only one faction's cards"""
    with open('complete-card-data.json', 'r') as f:
        db = json.load(f)

    # Filter to faction only
    faction_equipment = [c for c in db['equipment']
                        if faction in c.get('keywords', [])]
    return {'equipment': faction_equipment}
```

**Impact**: 50% faster startup (load 2 factions vs all 10)
**Trade-off**: More complex code

**Verdict**: **Not worth it** (JSON load is <10ms, negligible)

---

## 5. TESTING & VALIDATION OPTIMIZATIONS

### A. Statistical Significance Testing

**Current**: Run 5 battles per matchup (small sample)
**Issue**: High variance (luck can swing results)

**Fix**: Increase to 10-20 battles per matchup
```python
# In faction_balance_DICE.py
result = run_faction_matchup(faction1, faction2, builder, runs=20)  # Was 5
```

**Impact**: More reliable balance data, less variance
**Trade-off**: 4× longer simulation time (offset by parallel execution)

---

### B. Confidence Intervals for Win Rates

**Current**: Report raw win rate (e.g., "60.0% WR")
**Improvement**: Report 95% confidence interval

**Implementation**:
```python
import scipy.stats as stats

def calculate_confidence_interval(wins, total, confidence=0.95):
    """Calculate Wilson score confidence interval"""
    if total == 0:
        return (0, 0)

    p = wins / total
    z = stats.norm.ppf((1 + confidence) / 2)
    denominator = 1 + z**2 / total
    center = (p + z**2 / (2 * total)) / denominator
    margin = z * (p * (1 - p) / total + z**2 / (4 * total**2))**0.5 / denominator

    return (center - margin, center + margin)

# Report: "Church: 60.0% WR (95% CI: 52-68%)"
```

**Impact**: Better understanding of balance uncertainty
**Example**: "Elves 0% (95% CI: 0-8%)" vs "Church 100% (95% CI: 92-100%)"

---

## 6. PRIORITY IMPLEMENTATION ORDER

### Phase 1: Critical Fixes (1-2 hours)
1. ✅ **Fix Church "cannot miss"** (remove text, test impact)
2. ✅ **Fix Elves bleed timing** (apply on attack, reduce cap to 4)
3. ✅ **Fix Crucible Forge timing** (generate on attack)
4. ✅ **Reduce base hit target** (5+ → 4+ for better UX)
5. ✅ **Reduce deck sizes 20%** (faster combats, less grindy)

**Expected Impact**:
- Church: 100% → ~70% WR
- Elves: 0% → ~45% WR
- Crucible: 24% → ~50% WR
- Combat length: 37 turns → ~28 turns

### Phase 2: Code Optimizations (2-3 hours)
1. ✅ **Enable dataclass slots** (20% faster)
2. ✅ **Optimize card drawing** (batch operations)
3. ✅ **Reduce logging overhead** (conditional formatting)
4. ✅ **Parallel battle execution** (4× speedup)

**Expected Impact**: Simulation runs in 10-15 seconds (was 45s)

### Phase 3: Statistical Improvements (1 hour)
1. ✅ **Increase battle count** (5 → 20 runs per matchup)
2. ✅ **Add confidence intervals** (uncertainty quantification)
3. ✅ **Track damage distribution** (not just average)

**Expected Impact**: Higher confidence in balance conclusions

### Phase 4: Complete Damage System (8-12 hours)
1. ❌ **DAMAGED cards + Damage Die** (Major Wounds)
2. ❌ **Component zones** (AP/Structure/Exposure)
3. ❌ **Pilot Wound deck** (separate 10-card deck)
4. ❌ **Strain system** (Heat 5+ danger zone)
5. ❌ **3-pile system** (Graveyard permanence)

**Expected Impact**: More realistic balance, slower simulation

---

## 7. IMMEDIATE ACTION ITEMS

**Run This Next**:
1. Apply Church/Elves/Crucible fixes (30 min)
2. Reduce deck sizes by 20% (5 min)
3. Change base hit target 5+ → 4+ (2 min)
4. Rerun 225-battle simulation (1 min)
5. Analyze results - target 7-10 factions in 45-55% WR

**If Balance Improves**:
- Implement Phase 2 optimizations (speed)
- Implement Phase 3 statistics (confidence)
- **THEN** consider complete damage system

**If Balance Still Broken**:
- Debug which factions still outliers
- Apply targeted nerfs/buffs
- Iterate until 7+ factions balanced

---

## 8. METRICS TO TRACK

**After Each Simulation**:
```
✓ Balance Score (factions in 45-55% WR range)
✓ Average combat length (turns)
✓ Average hit rate (should be ~72%)
✓ Catastrophic failure rate (should be ~2.78%)
✓ Execution rate (should be ~2.78%)
✓ Critical hit rate (should be ~11%)
✓ Faction diversity (how many viable factions?)
```

**Target Metrics**:
- Balance: **7-10/10 factions** in 45-55% WR
- Combat length: **20-30 turns** (not grindy)
- Hit rate: **70-75%** (feels responsive)
- Catastrophic failures: **2-3%** (rare but memorable)
- Diversity: **8+/10 factions** viable in competitive play

---

## Conclusion

**Highest ROI Optimizations**:
1. **Church/Elves/Crucible fixes** → Fix catastrophic imbalance (100%/0%/24% WR)
2. **Reduce deck sizes 20%** → Fix grindy combats (37 → 28 turns)
3. **Base hit target 4+** → Fix low hit rate (57% → 72%)
4. **Parallel execution** → 4× faster testing (45s → 12s)

**Implement these 4 optimizations** → **90% of balance/speed gains** for **10% of effort**.

**Defer complete damage system** until basic balance achieved (7+ factions in 45-55% range).

---

**[Next: Implement Phase 1 Fixes →](PHASE-1-BALANCE-FIXES.md)**
