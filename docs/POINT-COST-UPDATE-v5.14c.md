# Point Cost Update v5.14c

**Date:** October 20, 2025
**Change Type:** Balance Adjustment
**Reason:** Prevent Colossus from appearing at Easy difficulty

---

## Changes Made

### Point Costs Updated

**Before (v5.14b):**
| Unit | Old Cost |
|------|----------|
| Scout | 1 |
| Warden | 2 |
| Vanguard | 3 |
| Colossus | 4 |
| Support | 0.5 |

**After (v5.14c):**
| Unit | New Cost |
|------|----------|
| Scout | 2 (+1) |
| Warden | 3 (+1) |
| Vanguard | 4 (+1) |
| Colossus | 5 (+1) |
| Support | 1 (+0.5, doubled) |

---

## Impact on Difficulty Levels

### Easy Difficulty (4 Points)

**Before:** Could afford 1 Colossus (4 pts)
**After:** Cannot afford Colossus (needs 5 pts)

**New compositions:**
- 2 Scouts (2+2 = 4 pts)
- 1 Vanguard (4 pts)
- 1 Warden + 1 Support (3+1 = 4 pts)
- 4 Supports (1+1+1+1 = 4 pts)

**Result:** Easier enemies, Colossus only appears at Medium+ difficulty

---

### Medium Difficulty (6 Points)

**Before:** 1 Colossus + Warden (4+2 = 6 pts)
**After:** 1 Colossus + 1 Support (5+1 = 6 pts)

**New compositions:**
- 2 Wardens (3+3 = 6 pts)
- 3 Scouts (2+2+2 = 6 pts)
- 1 Vanguard + 1 Scout (4+2 = 6 pts)
- 1 Colossus + 1 Support (5+1 = 6 pts)

**Result:** Colossus now appears, but with less backup

---

### Hard Difficulty (8 Points)

**Before:** 2 Colossi (4+4 = 8 pts)
**After:** 1 Colossus + 1 Warden (5+3 = 8 pts)

**New compositions:**
- 2 Vanguards (4+4 = 8 pts)
- 4 Scouts (2+2+2+2 = 8 pts)
- 1 Colossus + 1 Warden (5+3 = 8 pts)
- 2 Wardens + 1 Scout (3+3+2 = 8 pts)

**Result:** Can still get Colossus, but only 1 (not 2)

---

### Boss Difficulty (12 Points)

**Before:** 3 Colossi (4+4+4 = 12 pts)
**After:** 2 Colossi + 1 Warden (5+5+3 = 13 pts - need adjustment)

**New compositions:**
- 2 Colossi + 1 Scout (5+5+2 = 12 pts)
- 4 Wardens (3+3+3+3 = 12 pts)
- 6 Scouts (2×6 = 12 pts)
- 1 Colossus + 1 Vanguard + 1 Warden (5+4+3 = 12 pts)

**Result:** More variety, still challenging

---

## Verification Test

Ran 10 random Easy difficulty armies:

```
Army 1: 3.0 pts - WARDEN
Army 2: 4.0 pts - SCOUT, SCOUT
Army 3: 3.0 pts - WARDEN
Army 4: 4.0 pts - VANGUARD
Army 5: 4.0 pts - SCOUT, SCOUT
Army 6: 3.0 pts - WARDEN
Army 7: 3.0 pts - WARDEN
Army 8: 3.0 pts - SCOUT + 1 Support
Army 9: 3.0 pts - WARDEN
Army 10: 4.0 pts - WARDEN + 1 Support
```

✅ **No Colossus appeared** (requires 5 pts, Easy only has 4)

---

## Files Modified

1. **equipment_simulator_dice.py**
   - Line 149-152: Updated CasketClass point costs
   - Line 275: Updated SupportUnit cost (0.5 → 1.0)
   - Line 372: Updated support calculation (/ 0.5 → / 1.0)
   - Line 380: Updated remaining points (-0.5 → -1.0)
   - Line 384-387: Updated comment point costs
   - Line 390: Updated while loop (>= 1 → >= 2)
   - Line 324-328: Updated Difficulty preset comments

2. **ARMY-BUILDER-SYSTEM.md**
   - Updated all point cost tables
   - Updated difficulty preset examples
   - Added note: Colossus not available at Easy

---

## Reasoning

User requested: "So even the lowest difficulty Colossi isn't involved"

**Goal:** Easy difficulty (4 points) should NOT have Colossus

**Solution:** Increase all costs by +1:
- Colossus: 4 → 5 (now unaffordable at Easy)
- All other units scaled proportionally
- Support: 0.5 → 1.0 (simpler math, whole numbers only)

**Result:** Progression curve is smoother:
- Easy: Scouts, Wardens, Vanguards only
- Medium: First Colossus appearance (with minimal backup)
- Hard: Colossus + stronger units
- Boss: Multiple Colossi or large armies

---

## Impact on Balance Testing

Point-based armies now have:
- ✅ Clear difficulty curve (no Colossus at Easy)
- ✅ Whole number point costs (easier to calculate)
- ✅ More varied compositions at each difficulty
- ✅ Colossus feels like a boss unit (appears at Medium+)

Future testing should use:
- Easy (4 pts) for basic faction balance
- Medium (6 pts) for standard balance
- Hard (8 pts) for advanced compositions
- Boss (12 pts) for stress testing

---

## Next Steps

1. Update test scripts to verify new compositions
2. Document difficulty recommendations for players
3. Consider adding:
   - Very Easy (3 pts) - 1 Warden or 1 Scout + 1 Support
   - Nightmare (15 pts) - 3 Colossi or 7-8 units

---

**Document Version:** 1.0
**Author:** Claude (AI Assistant)
**Status:** Point cost rebalance complete
**Version:** v5.14c
