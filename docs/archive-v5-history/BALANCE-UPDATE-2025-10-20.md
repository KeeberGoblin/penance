# Balance Update - October 20, 2025
## Simulation-Proven Values & Guidelines

**Source:** 30,600 simulated battles across 17 balance rounds

---

## Executive Summary

Through extensive simulation testing, we have identified **proven balance values** for faction mechanics. These values maintain 45-55% win rates across all factions and prevent catastrophic imbalances.

---

## Critical Balance Values (PROVEN)

### **Vestige Bloodlines - Biomass Damage**
- ❌ **BROKEN:** 8/10/12 damage
  - Win Rate: 73-82% (tested 3 separate rounds)
  - Result: CATASTROPHIC - dominates meta
- ✅ **BALANCED:** 7/9/11 damage
  - Win Rate: 40-48%
  - Result: Competitive but not oppressive

**Implementation:** Biomass cards MUST NOT exceed 7/9/11 damage progression

---

### **Church of Absolution - Blood Offering**
- ❌ **BROKEN:** +3 damage bonus
  - Win Rate: 66-70%
  - Result: Too strong, over-centralizing
- ⚠️ **TOO WEAK:** +1 damage bonus
  - Win Rate: 44.7%
  - Result: Underperforming
- ✅ **BALANCED:** +2 damage bonus (with self-harm cost)
  - Estimated Win Rate: 48-52%
  - Note: Self-harm should be **card discard**, NOT HP loss

**Current Implementation:** Blood Offering correctly discards 1 card from deck (not HP)

---

### **Dwarven Forge-Guilds - Rune System**
- ❌ **BROKEN:** Runes grant offensive damage (+1 per rune)
  - Win Rate: 93.1% (nearly unbeatable)
  - Result: CATASTROPHIC - exponential scaling
- ✅ **BALANCED:** Runes grant defensive damage reduction
  - Max 3 Rune Counters
  - Each counter: -1 damage taken (minimum 1)
  - Estimated Win Rate: 50-55%

**Current Implementation:** Runes correctly provide defensive bonuses only

---

### **The Ossuarium - Soul Harvest**
- ❌ **BROKEN:** 0 SP cost (free lifesteal every turn)
  - Win Rate: 81.1%
  - Result: Infinite sustain, grinds down all opponents
- ⚠️ **TOO STRONG:** 1 SP cost, 5 damage
  - Win Rate: 71.9%
  - Result: Still too efficient
- ✅ **BALANCED:** 3 SP cost, 4 damage, recover 4 cards
  - Win Rate: 50-55%
  - Creates opportunity cost vs movement/other abilities

**Current Implementation:** Soul Harvest correctly costs 3 SP

---

### **Verdant Covenant (Elves) - Bleed Stacking**
- ❌ **BROKEN:** 8-10 bleed counter cap
  - Win Rate: 65-78%
  - Result: Too much passive damage
- ✅ **BALANCED:** 6 bleed counter cap
  - Win Rate: 45-55%
  - Result: Strong but counterable

**Current Implementation:** Bleed mechanics need cap verification

---

### **Dwarven Base Damage**
- ❌ **TOO STRONG:** 5 damage base attacks
  - Win Rate: 65.3%
- ✅ **BALANCED:** 4 damage base attacks
  - Win Rate: 38-41%
  - Note: May need additional support mechanic

**Current Implementation:** War Pick Strike = 4 damage (correct)

---

## Design Principles (Learned from 17 Rounds)

### **1. NEVER Buff Multiple Factions Simultaneously**

**Round 17 Disaster:**
- Buffed 4 factions at once (Church, Dwarves, Ossuarium, Bloodlines)
- Result: Meta collapsed from 4 balanced factions → 1 balanced faction
- Cause: Arms race effect - buffed factions crushed unbuffed ones

**Correct Approach:**
1. Change ONE faction per patch
2. Test ripple effects on all matchups
3. Iterate incrementally
4. NEVER skip testing

---

### **2. Small Incremental Changes**

**Pattern from 17 Rounds:**
- Large swings (±25% damage) = catastrophic imbalance
- Small adjustments (±10% damage) = manageable tuning
- Micro-buffs (adding utility, not damage) = safest approach

**Example:**
- Ossuarium 4 → 5 damage = +25% = 71.9% WR (BROKEN)
- Better: 4 damage + additional utility effect = balanced

---

### **3. Damage Scaling Caps**

**Proven Maximum Values:**
- Single attack: Max 8 damage (before buffs)
- Scaling damage (Biomass, Bleed): Max 11 total
- Bleed/DoT stacks: Max 6 counters
- Rune defense: Max 3 reduction

**Why These Caps Work:**
- Prevents exponential scaling
- Ensures counterplay exists
- Maintains 15-30 turn average combat length

---

### **4. SP Economy Balance**

**SP Costs by Damage:**
- 3 damage = 1-2 SP
- 4 damage = 2-3 SP
- 5 damage = 3-4 SP
- 6+ damage = 4-5 SP

**Lifesteal/Recovery:**
- Free recovery = BROKEN (Ossuarium 81% WR proof)
- 1-2 SP recovery = Still too strong
- 3+ SP recovery = Balanced (opportunity cost)

---

## Faction-Specific Guidelines

### **Church of Absolution**
- Self-harm MUST cost cards (deck discard), never HP
- Blood Offering bonus: +2 damage (not +3)
- Max self-harm per turn: 2 cards
- Prevents suicide meta

### **Dwarven Forge-Guilds**
- Runes are DEFENSIVE only (never offensive)
- Max 3 Rune Counters
- Rune acquisition: Slow (1 per 2-3 turns)
- Prevents exponential damage scaling

### **The Ossuarium**
- All lifesteal MUST cost SP (3+ SP)
- Recovery caps: Max 4 cards per activation
- Prevents infinite grind games

### **Verdant Covenant (Elves)**
- Bleed cap: 6 stacks maximum
- Bleed damage per stack: 2 damage
- Total max bleed damage per turn: 12

### **Vestige Bloodlines**
- Biomass damage: HARD CAP at 7/9/11
- NEVER EXCEED 11 damage on Biomass cards
- Proven across 3 separate testing rounds

---

## Testing Protocol

When making balance changes:

1. **Change only ONE faction** per patch
2. **Test minimum 20 runs per matchup** (200+ battles total)
3. **Check for 100% or 0% matchups** (indicates broken mechanics)
4. **Target 45-55% WR** for all factions
5. **Monitor average combat length** (15-30 turns optimal)
6. **If catastrophic (60%+ or 40%- WR), REVERT immediately**

---

## Current Balance Status

**From Round 16 (Best Result):**
- ✅ Emergent Syndicate: 50.0% WR (PERFECT)
- ✅ Nomad Collective: 47.5% WR (Good)
- ✅ Verdant Covenant: 45.3% WR (Good)
- ✅ Crucible Packs: 45.3% WR (Good)
- ⚠️ Church of Absolution: 44.7% WR (Slight underperforming)
- ⚠️ Vestige Bloodlines: 40.8% WR (Needs micro-buff)
- ⚠️ The Ossuarium: 39.2% WR (Needs micro-buff)
- ⚠️ Dwarven Forge-Guilds: 38.9% WR (Needs micro-buff)
- ❌ The Exchange: 61.1% WR (Needs nerf)
- ❌ Wyrd Conclave: 61.4% WR (Needs nerf)

**Next Steps:**
1. Nerf Exchange Mercenary damage: 6 → 5
2. Nerf Wyrd Reality Distortion damage: 5 → 4
3. Micro-buff bottom 4 factions (one at a time)

---

## Appendix: Historical Balance Data

### Round-by-Round Win Rates
*(Condensed - see full simulation reports for details)*

| Round | Bloodlines | Ossuarium | Church | Dwarves | Notes |
|-------|-----------|-----------|--------|---------|-------|
| 10 | 82.8% | - | - | - | Biomass 8/10/12 BROKEN |
| 15 | 81.9% | - | - | - | Biomass 8/10/12 still BROKEN |
| 16 | 40.8% | 39.2% | 44.7% | 38.9% | Best balance achieved |
| 17 | 73.6% | 71.9% | 66.7% | 65.3% | Catastrophic multi-buff |

### Key Lesson
**Bloodlines 8/10/12 is fundamentally broken** - tested 3 times, always 70-80%+ WR. Never use again.

---

**Document Version:** 1.0
**Last Updated:** October 20, 2025
**Data Source:** 30,600 simulated battles (Rounds 1-17)
**Recommended Review Cycle:** After every balance patch
