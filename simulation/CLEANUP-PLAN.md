# Simulation Folder Cleanup Plan

## Current State
- **18 Markdown reports** (140+ KB total)
- **16 Python scripts** (150+ KB total)
- **5 Text reports** (22+ KB total)
- Total: 39 files

---

## Files to KEEP (Essential)

### Active Scripts (Keep)
1. **equipment_simulator.py** (25K) - Current combat simulator
2. **faction_balance_with_combos.py** (6K) - Balance testing script
3. **test_sp_banking.py** (4.1K) - SP mechanics test

### Current Reports (Keep)
1. **NEW-EQUIPMENT-BALANCE-REPORT.md** (9.1K) - Latest results (Oct 20, 2025)
2. **GODOT-FEASIBILITY-ASSESSMENT.md** (16K) - Implementation roadmap
3. **SIMULATION-FIXES-NEEDED.md** (8.5K) - Critical fixes doc

### Final Documentation (Keep)
1. **FINAL-BALANCE-FIXES.md** (11K) - Consolidated balance data
2. **ROUND-17-POST-MORTEM.md** (5.1K) - Lessons learned

---

## Files to ARCHIVE (Historical)

### Old Round Reports (Archive)
- ROUND-1-V2-POST-MORTEM.md (9.2K)
- ROUND-2-V2-POST-MORTEM.md (11K)
- ROUND-6-FINAL-BALANCE.md (7.0K)
- ROUND-7-EMERGENCY-FIX.md (4.2K)
- ROUND-15-CONVERGENCE-PUSH.md (5.6K)
- ROUND-16-EMERGENCY-CORRECTIONS.md (5.4K)
- ROUND-17-FINE-TUNING.md (6.2K)

### Superseded Reports (Archive)
- 6-POINT-BATTLE-REPORT.md (6.4K) - Superseded by equipment system
- BALANCE-ANALYSIS.md (9.6K) - Old analysis
- COLOSSUS-BUFF-RESULTS.md (7.5K) - Specific test, no longer relevant
- COMBO-SYSTEM-REPORT.md (8.2K) - Integrated into current system
- S-TIER-BALANCE-FIXES.md (8.4K) - Old fixes
- V2-REALISTIC-SIMULATOR-SUMMARY.md (5.9K) - Old version

---

## Files to DELETE (Redundant/Obsolete)

### Old Simulators (Delete)
- combat_simulator.py (34K) - Replaced by equipment_simulator.py
- combat_simulator_v2.py (18K) - Old version

### Obsolete Scripts (Delete)
- add-missing-equipment.py (5.3K) - One-time use, already done
- comprehensive_balance_test.py (9.8K) - Superseded by faction_balance_with_combos.py
- faction_matchup_test.py (11K) - Old version
- faction_matchup_test_v2.py (7.3K) - Old version
- fix-weak-factions.py (7.5K) - One-time use
- run_multiple_simulations.py (12K) - Redundant
- team_combat_test.py (14K) - Not used
- test_combo_system.py (3.3K) - Integrated into main simulator

### Old Text Reports (Delete)
- balance_report.txt (9.3K) - Old format
- comprehensive_balance_report.txt (2.0K) - Superseded
- faction_matchup_report.txt (8.6K) - Old data
- faction_matchup_report_v2.txt (1.5K) - Old data
- summary_report.txt (1.3K) - Superseded
- team_combat_report.txt (829B) - Not relevant

---

## Action Plan

### Step 1: Create Archive
```bash
mkdir -p archived-rounds
mkdir -p archived-scripts
```

### Step 2: Move Historical Reports
```bash
mv ROUND-*.md archived-rounds/
mv 6-POINT-BATTLE-REPORT.md archived-rounds/
mv BALANCE-ANALYSIS.md archived-rounds/
mv COLOSSUS-BUFF-RESULTS.md archived-rounds/
mv COMBO-SYSTEM-REPORT.md archived-rounds/
mv S-TIER-BALANCE-FIXES.md archived-rounds/
mv V2-REALISTIC-SIMULATOR-SUMMARY.md archived-rounds/
```

### Step 3: Move Obsolete Scripts
```bash
mv combat_simulator*.py archived-scripts/
mv comprehensive_balance_test.py archived-scripts/
mv faction_matchup_test*.py archived-scripts/
mv add-missing-equipment.py archived-scripts/
mv fix-weak-factions.py archived-scripts/
mv run_multiple_simulations.py archived-scripts/
mv team_combat_test.py archived-scripts/
mv test_combo_system.py archived-scripts/
```

### Step 4: Delete Old Reports
```bash
rm *.txt
```

---

## Final Structure (After Cleanup)

### simulation/
- equipment_simulator.py (active simulator)
- faction_balance_with_combos.py (balance testing)
- test_sp_banking.py (mechanics testing)
- NEW-EQUIPMENT-BALANCE-REPORT.md (latest results)
- GODOT-FEASIBILITY-ASSESSMENT.md (implementation guide)
- SIMULATION-FIXES-NEEDED.md (critical fixes)
- FINAL-BALANCE-FIXES.md (consolidated data)
- ROUND-17-POST-MORTEM.md (lessons learned)
- archived-rounds/ (historical reports)
- archived-scripts/ (old code)
- __pycache__/ (Python cache)

**Before:** 39 files (300+ KB)
**After:** 8 active files + 2 archive folders (organized)

---

## Benefits

1. **Easier Navigation** - Only current files visible
2. **Preserved History** - Old files archived, not deleted
3. **Clear Structure** - Active vs archived separation
4. **Reduced Clutter** - 80% reduction in root folder files

