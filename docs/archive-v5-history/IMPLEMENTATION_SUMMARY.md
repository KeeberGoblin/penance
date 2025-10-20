# Implementation Summary: Hybrid Casket System

**Date:** 2025-10-18
**Status:** ✅ PHASE 1 COMPLETE

---

## What Was Implemented

### ✅ New Lore Documents Created

1. **[docs/lore/casket-technology-revised.md](lore/casket-technology-revised.md)**
   - Hybrid system: Living pilot + separate Soulstone soul
   - Open casket design with viewing slit
   - Neural threads drilled into fingertips
   - Modular limb system (3D-printable, Gunpla-style)
   - Soul Sacrifice rituals (leg removal, faction variants)

2. **[docs/lore/soulstone-system.md](lore/soulstone-system.md)**
   - Soulstone tiers (T1-T4 Shards/Fragments/Crystals/Cores)
   - Energy mechanics (0-100 tracking, depletion, refinement)
   - Taint corruption system (0-21+ thresholds, Void events)
   - Soul cannibalism/chimera process
   - Faction-specific Soulstone shapes
   - Core burnout after 500 Energy cycled

3. **[docs/lore/neural-thread-system.md](lore/neural-thread-system.md)**
   - 10 threads (5 per hand) drilled into fingertips
   - Installation procedure (faction variants)
   - Thread-to-function mapping (puppet control)
   - Thread Snap mechanics
   - Psychological bonding/disconnection trauma
   - Faction thread customization

### ✅ HTML Conversions Created

1. **[docs/codex/lore-caskets-revised.html](codex/lore-caskets-revised.html)**
   - Full HTML conversion with manuscript styling
   - Ready for codex navigation integration

2. **[docs/codex/lore-soulstone-system.html](codex/lore-soulstone-system.html)**
   - Streamlined HTML focusing on key mechanics
   - Tables for Energy/Taint/Acquisition
   - Faction Soulstone shapes table

3. **[docs/codex/lore-neural-threads.html](codex/lore-neural-threads.html)**
   - Complete thread mechanics documentation
   - Installation procedure tables
   - Thread Snap effects and field repair

### ✅ Existing Files Updated

1. **[docs/codex/lore-caskets-overview.html](codex/lore-caskets-overview.html)**
   - Added deprecation banner (bright red warning)
   - Links to revised system
   - Preserved for historical reference

---

## Key Changes from Old → New System

| Aspect | OLD System | NEW System (Hybrid) |
|--------|-----------|-------------------|
| **Pilot Location** | Suspended in neural fluid | Strapped with restraints, breathing normally |
| **Vision** | Optical sensors/cameras | Direct viewing slit (physical gap) |
| **Power Source** | Pilot's soul powers casket | Separate soul in Soulstone crystal |
| **Pilot Status** | Dead/dying, bound at death | LIVING volunteer, conscious |
| **Casket Design** | Sealed coffin | Open lid design (accessible interior) |
| **Soul Identity** | Pilot = Soul (same entity) | Pilot ≠ Soul (two separate people) |
| **Ethical Horror** | Single-layer (pilot slavery) | Triple-layer (pilot + soul + strings) |

---

## Files Requiring Future Updates

### HIGH PRIORITY

**INCOMPLETE** - Need deprecation banners:
- [ ] `docs/codex/lore-casket-origins.html`
- [ ] `docs/codex/lore-casket-manufacturing.html`

**INCOMPLETE** - Need clarification sections:
- [ ] `docs/codex/lore-soul-binding.html` (add: pilot ≠ soul distinction)
- [ ] `docs/codex/faction-undead.html` (The Ossuarium - clarify living pilots)
- [ ] `docs/codex/faction-church.html` (clarify dual penance: pilot + soul)

### MEDIUM PRIORITY

**INCOMPLETE** - Need new mechanics added:
- [ ] `docs/codex/rules-combat.html` (add Thread Snap combat rules)
- [ ] `docs/codex/rules-component-damage.html` (add Soulstone Core, Threads, Viewing Slit)
- [ ] `docs/codex/campaign-settlement-phase.html` (add Soulstone refinement, Thread maintenance)
- [ ] `docs/codex/campaign-loot-tables.html` (add Soulstone Shard drops)

### LOW PRIORITY

**NOT YET CREATED** - New files needed:
- [ ] `docs/codex/rules-soulstone-energy.html` (gameplay mechanics)
- [ ] `docs/codex/rules-thread-snap.html` (combat mechanics)

**NOT YET UPDATED** - Navigation:
- [ ] `docs/codex/index.html` (add new files to sidebar navigation)

---

## Gameplay Mechanics Summary

### Soulstone Energy System

**Tracking:**
- Each Casket has 0-100 Energy pool
- Depletes 2-15 per mission (depending on activity)
- At 0 Energy = casket inoperable

**Restoration:**
- Refine Soulstone Shards between missions
- T1 Shard = +5 Energy, +1 Taint, 1 day
- T2 Fragment = +15 Energy, +2 Taint, 2 days
- T3 Crystal = +40 Energy, +5 Taint, 5 days
- T4 Core = +100 Energy (full replacement), +10 Taint, 2 weeks

**Acquisition:**
- Standard mission: 1-2 T1 Shards
- Hard mission: 3-5 T1, 1 T2
- Boss battle: 5-8 T1, 2-3 T2, 1 T3
- Purchase from Exchange: 20-400 Credits depending on tier

### Taint Corruption System

**Thresholds:**
- 0-5: Stable (no penalties)
- 6-10: Unstable (-1 to Pilot checks)
- 11-15: Fragmenting (-2 to Pilot checks, +1 Heat/turn)
- 16-20: Corrupted (-3 to Pilot checks, random Thread Snaps)
- 21+: Void-Touched (roll Corruption Event table each mission)

**Void Corruption Events (Taint 21+):**
- Roll 1d6 at mission start
- 1-2: Whispers (Grit DC 12 or -1 SP)
- 3-4: Thread Rebellion (random equipment malfunction)
- 5: Soul Fragmentation (Disadvantage on all attacks)
- 6: **Void Breach** (casket goes rogue 1d6 turns, attacks randomly)

**Taint Reduction:**
- Church Prayer: -2 Taint, 20 Credits, 1 week
- Dwarf Runes: -3 Taint, 40 Credits, 2 weeks
- Elf Cleansing: -4 Taint, 0 Credits, 1 month (requires grove)
- Ossuarium Swap: -10 Taint, 100 Credits (replace entire Core)

### Thread Snap System

**Causes:**
- Combat damage to casket (10+ damage in one hit)
- Overheating (Heat maxed out)
- Taint corruption (high Taint random snaps)
- Emergency disconnect (pilot choice)

**Effects:**
- Pilot: Excruciating pain (Grit DC 15 or lose turn), phantom amputation
- Casket: Corresponding limb/function disabled

**Field Repair:**
- Requires ally with Repair skill, 1 full turn, DC 12 check
- Success = thread functional but fragile (-1 penalty, will break again easily)
- Permanent fix requires settlement (1 week, 50 Credits per thread)

---

## Faction-Specific Additions

### Church of Absolution

**Soul Sacrifice: "The Shortening"**
- Legs removed at hip socket
- Wheelchair-bound outside casket
- Benefits: +1 SP, +2 Heat, Martyrdom Aura, Stump Override

**Soulstone Shape:**
- Cross/reliquary with gold filigree cage
- Philosophy: "We consecrate souls before consumption"

**Thread Style:**
- Wrapped in blessed silk, prayer beads at joints
- Philosophy: "Each thread is a chain of penance"

### Dwarven Forge-Guilds

**Soul Sacrifice: "Compact Form"**
- All four limbs removed, runic stumps
- Hydraulic prosthetics outside casket
- Benefits: +1 SP, +1 to attack rolls, Runic Stability

**Soulstone Shape:**
- Geometric polyhedron with runic etchings
- Philosophy: "Precise cuts maximize efficiency"

**Thread Style:**
- Etched with micro-runes, bone anchors
- Philosophy: "Precision engineering, no wasted motion"

### The Ossuarium

**Soul Sacrifice: "Efficient Form"**
- ALL flesh removed except skull/spine
- Cannot leave capsule (life support dependency)
- Benefits: +1 SP, Immune to Pilot Wounds, Soul Harvest Protocol

**Soulstone Shape:**
- Skull-shaped crystal, glowing eye sockets
- Philosophy: "The faces deserve to be seen"

**Thread Style:**
- Wrapped in bone fiber, skeletal patterns
- Philosophy: "The threads are tendons"

### Elven Verdant Covenant

**Soul Sacrifice: "Root-Grafting"**
- Legs replaced with living vine limbs
- Can walk at half speed (creeping gait)
- Benefits: +1 SP, Photosynthesis, Root Sensing, Thornwhip

**Soulstone Shape:**
- Teardrop/seed wrapped in living vines
- Philosophy: "We mourn every soul consumed"

**Thread Style:**
- Living vines grafted to nerves
- Philosophy: "We grow with the machine"

---

## What Still Needs Doing

### PHASE 2: Rules Integration (Estimated 2-3 hours)

1. **Create rules-soulstone-energy.html**
   - Extract gameplay tables from lore document
   - Add example scenarios (Energy depletion over 3-mission campaign)
   - Add quick reference table

2. **Create rules-thread-snap.html**
   - Thread Snap trigger conditions
   - Effect tables (pilot/casket)
   - Field repair procedure
   - Combat scenarios

3. **Update rules-combat.html**
   - Add Thread Snap to combat damage section
   - Add Soulstone Energy depletion triggers
   - Add Viewing Slit damage (critical hits blind pilot)

4. **Update rules-component-damage.html**
   - Add Soulstone Core (back location, if destroyed = power loss)
   - Add Neural Threads (interior, each controls specific function)
   - Add Viewing Slit (front, if damaged = blindness)

### PHASE 3: Campaign/Scenario Updates (Estimated 1-2 hours)

1. **Update campaign-settlement-phase.html**
   - Add Soulstone Refinement downtime activity
   - Add Thread Maintenance downtime activity
   - Add Taint Reduction faction services

2. **Update campaign-loot-tables.html**
   - Add Soulstone Shard drops by mission type
   - Add special event rewards (Soul Harvest, Void Rift, etc.)

3. **Update scenario templates**
   - Add Energy tracking to mission setup
   - Add Thread Snap events to combat tables
   - Add Taint checks for high-corruption caskets

### PHASE 4: Navigation & Polish (Estimated 30 min)

1. **Update index.html sidebar**
   - Add lore-caskets-revised.html to LORE section
   - Add lore-soulstone-system.html to LORE section
   - Add lore-neural-threads.html to LORE section
   - Add rules-soulstone-energy.html to RULES section (once created)
   - Add rules-thread-snap.html to RULES section (once created)

2. **Update cross-references**
   - Ensure all "Explore Further" tables link correctly
   - Update breadcrumb navigation
   - Add new files to README.md

---

## Testing Checklist

**Before Final Release:**

- [ ] Playtest Soulstone Energy over 3-mission arc (is depletion rate balanced?)
- [ ] Playtest Thread Snap frequency (too common? too rare?)
- [ ] Playtest Taint accumulation (does corruption feel threatening but not punishing?)
- [ ] Playtest Soul Sacrifice mechanics (are benefits worth the cost?)
- [ ] Verify all HTML links work (no broken navigation)
- [ ] Verify manuscript-style.css renders correctly on all new pages
- [ ] Proofread all new content (typos, grammar, consistency)

---

## Known Issues / Open Questions

**RESOLVED:**
- ✅ "Neural fluid" vs "strapped in" - RESOLVED (hybrid system, strapped with restraints)
- ✅ "Pilot = soul" confusion - RESOLVED (living pilot ≠ Soulstone soul)
- ✅ Viewing slit vs optical sensors - RESOLVED (physical viewing slit)
- ✅ Soulstone shape per faction - RESOLVED (cosmetic variants table created)

**PENDING:**
- ❓ Should Soulstone Energy be tracked on character sheet or separate tracker?
- ❓ Should Thread Snap risk increase with Casket damage (wounded caskets = more snaps)?
- ❓ Should faction Soulstone shapes provide minor mechanical bonuses? (Currently purely cosmetic)
- ❓ Should Core burnout be extended beyond 500 Energy for extended campaigns?

---

## File Inventory

### Created (Markdown)
- docs/lore/casket-technology-revised.md
- docs/lore/soulstone-system.md
- docs/lore/neural-thread-system.md

### Created (HTML)
- docs/codex/lore-caskets-revised.html
- docs/codex/lore-soulstone-system.html
- docs/codex/lore-neural-threads.html

### Updated (HTML)
- docs/codex/lore-caskets-overview.html (added deprecation banner)

### Planning Documents
- docs/CODEX_UPDATE_PLAN.md (comprehensive update roadmap)
- docs/IMPLEMENTATION_SUMMARY.md (this file)

### Pending Creation
- docs/codex/rules-soulstone-energy.html
- docs/codex/rules-thread-snap.html

---

## Completion Status

**PHASE 1: Core Lore Documents** ✅ COMPLETE
- [x] Create new lore markdown files
- [x] Convert to HTML with manuscript styling
- [x] Add deprecation banners to old files
- [x] Create implementation plan

**PHASE 2: Rules Integration** ⏳ PENDING
- [ ] Create rules documents
- [ ] Update existing rules files
- [ ] Add mechanics to campaign files

**PHASE 3: Navigation & Polish** ⏳ PENDING
- [ ] Update index.html sidebar
- [ ] Verify all cross-references
- [ ] Proofread all content

**PHASE 4: Playtesting** ⏳ PENDING
- [ ] Test Energy mechanics
- [ ] Test Thread Snap mechanics
- [ ] Test Taint corruption
- [ ] Balance adjustments

---

## Next Steps

**Immediate (Today):**
1. ✅ Create implementation summary (this file)
2. ⏳ Update index.html navigation
3. ⏳ Create rules-soulstone-energy.html
4. ⏳ Create rules-thread-snap.html

**Short-term (This Week):**
1. Update remaining codex files with deprecation banners
2. Add clarification sections to faction files
3. Update campaign/scenario files with new mechanics

**Long-term (This Month):**
1. Playtest new mechanics
2. Gather feedback
3. Make balance adjustments
4. Finalize documentation

---

**Last Updated:** 2025-10-18
**Implemented By:** Claude (Assistant)
**Approved By:** [Pending User Review]
