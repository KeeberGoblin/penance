# Penance Simulation Folder

**Last Updated:** October 20, 2025  
**Database Version:** 5.1

---

## Active Files

### Simulators
- **equipment_simulator.py** - Current combat simulator with equipment randomization
- **faction_balance_with_combos.py** - Balance testing script (runs 225 battles)
- **test_sp_banking.py** - SP banking and positioning mechanics test

### Reports
- **NEW-EQUIPMENT-BALANCE-REPORT.md** - Latest balance results (Oct 20, 2025)
- **GODOT-FEASIBILITY-ASSESSMENT.md** - Godot 4.5 implementation feasibility analysis
- **SIMULATION-FIXES-NEEDED.md** - Critical simulator bugs and fixes needed
- **FINAL-BALANCE-FIXES.md** - Consolidated balance data from all rounds

---

## Archived Files

### archived-rounds/
Historical balance testing reports from Rounds 1-17 (Oct 15-19, 2025)
- 14 markdown reports documenting iterative balance testing

### archived-scripts/
Obsolete Python scripts superseded by current simulators
- 10 old simulator versions and one-time utility scripts

---

## Quick Start

### Run Balance Test
```bash
python3 faction_balance_with_combos.py
```

Runs 225 battles (10 factions × 9 matchups × 5 runs)  
Output: Win rates, damage stats, balance analysis

### Test SP Banking
```bash
python3 test_sp_banking.py
```

Tests SP accumulation, movement costs, and combo mechanics

---

## Latest Results (Oct 20, 2025)

**Balance Score:** 2/10 factions in 45-55% target range

| Tier | Factions | Win Rate |
|------|----------|----------|
| S (Broken) | Church | 95.6% |
| A (Too Strong) | Dwarves, Elves | 84.4%, 71.1% |
| **B (BALANCED)** | **Crucible, Exchange** | **53.3%, 48.9%** |
| C (Too Weak) | Nomads, Ossuarium, Wyrd | 37.8%, 35.6%, 28.9% |
| D (Broken) | Bloodlines, Emergent | 26.7%, 17.8% |

See [NEW-EQUIPMENT-BALANCE-REPORT.md](NEW-EQUIPMENT-BALANCE-REPORT.md) for full analysis.

---

## Key Lessons

1. **Equipment must synergize with faction mechanics**  
   Crucible/Exchange balanced because equipment matches their token economies

2. **High damage dominates**  
   Church (4.6 avg damage) = 95.6% WR

3. **Token economies need balance**  
   Slow generation (Bloodlines Biomass) = 26.7% WR

4. **Change one faction at a time**  
   Round 17 disaster: Changed 4 factions → meta collapsed

---

## Next Steps

1. Nerf Church equipment damage: 4.6 → 3.5 avg
2. Buff Bloodlines Biomass generation: 1 → 2 per kill
3. Buff Emergent base damage (remove Metamorph requirements)
4. Re-run simulation and iterate

---

For detailed balance guidelines, see:  
[/docs/BALANCE-UPDATE-2025-10-20.md](../docs/BALANCE-UPDATE-2025-10-20.md)
