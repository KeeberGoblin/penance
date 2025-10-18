# Codex Update Plan: Hybrid Casket System Integration

**Date:** 2025-10-18
**Purpose:** Document all contradictions between OLD lore (neural fluid, pilot=soul) and NEW lore (hybrid system: living pilot + separate Soulstone soul)

---

## Summary of Changes

### Old System (To Be Replaced)
- Pilot is **suspended in neural fluid** inside sealed capsule
- Pilot's **soul is bound to the Casket at their death**
- Pilot = Soul = Power Source (all one entity)
- Vision through **optical sensors/cameras**
- Casket is **fully sealed coffin**

### New System (Hybrid Horror)
- Pilot is **strapped with restraints**, breathing normally
- Pilot is **LIVING volunteer** (conscious human)
- Soulstone contains **DIFFERENT person's soul** (separate power source)
- Vision through **physical viewing slit** (direct line-of-sight)
- Casket has **open lid design** with accessible interior

---

## Files Requiring Updates

### HIGH PRIORITY (Major Contradictions)

#### 1. `docs/codex/lore-caskets-overview.html`
**Lines with Contradictions:**
- Line 20: "bound in neural fluid" → Should be "strapped with restraints"
- Line 25: "suspended in neural fluid" → Should be "strapped inside the pilot capsule"
- Line 56: "bound at pilot's death, powers the chassis" → Should be "separate soul in Soulstone crystal"
- Line 64: "bound at death to power core" → Should be "living volunteer, separate power source"
- Line 95: "suspended in neural fluid inside a containment chamber" → Should be "strapped inside with restraints, breathing normally"
- Line 115-119: Soulstone Core description → Needs clarification that soul inside ≠ pilot
- Line 149-162: "The Pilot Experience" → Add viewing slit, remove references to floating/fluid

**Recommended Action:** Replace entire file with `lore-caskets-revised.html`

---

#### 2. `docs/codex/lore-casket-origins.html`
**Lines with Contradictions:**
- Line 277-298: "Soul Core" and "Deck System" descriptions conflate pilot with bound soul
- Line 305-325: "The Soul Experience" section → Should differentiate between:
  - Pilot's experience (strapped in, viewing through slit, neural threads)
  - Soul's experience (trapped in crystal, screaming, fed fragments)

**Recommended Action:** Add section clarifying **two separate entities**:
```html
<h3>Critical Distinction: Pilot vs. Soul</h3>
<p>The <strong>Living Pilot</strong> (you) is strapped inside the casket core. You are conscious, awake, breathing.</p>
<p>The <strong>Bound Soul</strong> (someone else) is trapped in the Soulstone crystal on the casket's back. They are the battery.</p>
<p>You pilot. They power. Both suffer.</p>
```

---

#### 3. `docs/codex/lore-soul-binding.html`
**Current Focus:** Soul-binding process for Soulstones (correct)

**Missing Context:**
- Does NOT explain that bound souls are **separate from pilots**
- Does NOT explain Soulstone refinement (feeding fragments to Core)
- Does NOT cover Taint corruption from soul cannibalism

**Recommended Action:** Add sections:
- **"Who Gets Bound?"** (volunteers, executed criminals, battlefield recovery)
- **"The Soulstone Economy"** (Cores need feeding, refinement creates chimera souls)
- **"Pilot vs. Soul Distinction"** (clarify living human pilots machine powered by dead soul)

---

#### 4. `docs/codex/campaign-leg-skimming.html`
**Current Focus:** Soul Sacrifice for pilots (correct)

**Minor Contradiction:**
- Implies leg removal is ONLY for space optimization
- Should also mention: "Makes pilot more dependent on casket (cannot flee, cannot escape)"

**Recommended Action:** Add narrative weight:
```html
<p><strong>The Trap:</strong> Once your legs are gone, you NEED the casket. You cannot run. You cannot escape. You are committed.</p>
```

---

### MEDIUM PRIORITY (Implicit Contradictions)

#### 5. `docs/codex/faction-undead.html` (The Ossuarium)
**Likely Contradictions:**
- May reference "soul-powered" without distinguishing pilot vs. Soulstone
- May describe Ossuarium pilots as "undead" when they should be "living humans piloting caskets powered by dead souls"

**Recommended Action:** Review faction description, clarify:
- Ossuarium **binds souls to Soulstones** (creates batteries)
- Ossuarium **recruits living pilots** (desperate, dying, or debt-ridden volunteers)
- "Efficient Form" = living pilot has all flesh removed except skull/spine

---

#### 6. `docs/codex/faction-church.html` (Church of Absolution)
**Likely Contradictions:**
- May describe soul-binding as "pilot's penance" when it should be "dual penance: pilot's suffering + soul's imprisonment"

**Recommended Action:** Clarify doctrine:
- Pilot sacrifices body (legs removed, strapped in casket)
- Soul sacrifices afterlife (trapped in crystal, powers machine)
- BOTH are performing penance together (shared suffering)

---

#### 7. `docs/codex/rules-combat.html`
**Missing Mechanics:**
- No rules for **Thread Snap** (neural threads severed by damage)
- No rules for **Soulstone Energy** depletion mid-mission
- No rules for **Viewing Slit** damage (pilot blinded)

**Recommended Action:** Add combat rules sections:
- **Thread Snap:** When casket takes 10+ damage in one hit, roll 1d6. On 5-6, random neural thread severs.
- **Soulstone Depletion:** Track Energy, casket shuts down at 0.
- **Slit Damage:** Critical hit to casket head = viewing slit cracked (Disadvantage on all attacks)

---

#### 8. `docs/codex/rules-component-damage.html`
**Missing Components:**
- Soulstone Core (back-mounted, vulnerable if flanked)
- Neural Threads (can be severed individually)
- Viewing Slit (critical vulnerability)

**Recommended Action:** Add component damage table:
```
| Component         | Location | Damage Effect                          |
|-------------------|----------|----------------------------------------|
| Soulstone Core    | Back     | If destroyed, casket loses all power  |
| Neural Thread (1) | Interior | Lose control of 1 limb function       |
| Viewing Slit      | Front    | Pilot blinded (Disadvantage on attacks)|
```

---

### LOW PRIORITY (Clarifications Needed)

#### 9. `docs/codex/campaign-pilot-grit.html`
**Context:** Pilot willpower/trauma system

**Potential Addition:**
- Add Grit checks for **Thread Snap** (resist pain, maintain control)
- Add Grit checks for **Soulstone screaming** (resist psychological horror)
- Add Grit checks for **Viewing Slit claustrophobia** (resist panic in tight space)

---

#### 10. `docs/codex/rules-turn-structure.html`
**Context:** Turn sequence

**Potential Addition:**
- Add phase: **"Soulstone Check"** (high-Taint caskets roll for Void Corruption each turn)
- Add phase: **"Thread Maintenance"** (check if damaged threads are still functional)

---

## New Files to Add

### 1. `docs/codex/lore-soulstone-system.html`
**Content:** Energy mechanics, refinement, Taint corruption, Core burnout, faction Soulstone shapes

**Status:** Markdown source complete ([docs/lore/soulstone-system.md](../lore/soulstone-system.md))

**Action Needed:** Convert to HTML, add to index.html navigation

---

### 2. `docs/codex/lore-neural-threads.html`
**Content:** Thread installation, puppet control, Thread Snap mechanics, field repair, faction thread variants

**Status:** Markdown source complete ([docs/lore/neural-thread-system.md](../lore/neural-thread-system.md))

**Action Needed:** Convert to HTML, add to index.html navigation

---

### 3. `docs/codex/rules-soulstone-energy.html`
**Content:** Gameplay mechanics for Energy tracking, refinement costs, Taint thresholds, emergency recharge

**Status:** Not yet created

**Action Needed:** Extract gameplay tables from lore document, create rules-focused version

---

### 4. `docs/codex/rules-thread-snap.html`
**Content:** Combat mechanics for Thread Snap, field repair, limb control loss

**Status:** Not yet created

**Action Needed:** Extract gameplay tables from lore document, create rules-focused version

---

## Navigation Updates

### `docs/codex/index.html` Sidebar Additions

**Add to LORE section:**
```html
<li><a href="lore-caskets-revised.html" target="content">Casket Technology (Revised)</a></li>
<li><a href="lore-soulstone-system.html" target="content">Soulstone Power System</a></li>
<li><a href="lore-neural-threads.html" target="content">Neural Thread Interface</a></li>
```

**Add to RULES section:**
```html
<li><a href="rules-soulstone-energy.html" target="content">Soulstone Energy Tracking</a></li>
<li><a href="rules-thread-snap.html" target="content">Thread Snap & Limb Control</a></li>
```

---

## Deprecation Plan

### Files to Mark as "Legacy/Old System"

Option A: **Delete** old files entirely (clean slate)
Option B: **Rename** old files with `-legacy` suffix (preserve history)
Option C: **Add warning banner** to old files (gradual transition)

**Recommendation:** Option C (gradual transition)

Add banner to top of old files:
```html
<div style="background: #ff6b6b; color: white; padding: 1rem; margin-bottom: 2rem; border: 3px solid #c92a2a;">
    <strong>⚠️ OUTDATED CONTENT</strong><br>
    This page describes the OLD casket system (pilot suspended in neural fluid, soul = pilot).<br>
    For the REVISED hybrid system (living pilot + separate Soulstone soul), see:<br>
    <a href="lore-caskets-revised.html" style="color: white; text-decoration: underline;">Casket Technology (Revised)</a>
</div>
```

---

## Scenario & Campaign Integration

### Scenarios Requiring Mechanical Updates

#### 1. `docs/codex/scenario-*.html` (All Scenarios)
**Add mechanics for:**
- Soulstone Energy tracking (caskets start missions at 80-100 Energy)
- Thread Snap events (combat damage can sever threads)
- Viewing Slit vulnerabilities (critical hits to head blind pilot)

#### 2. `docs/codex/campaign-settlement-phase.html`
**Add downtime activities:**
- **Soulstone Refinement** (spend Shards to restore Energy, gain Taint)
- **Thread Maintenance** (replace degraded threads, 20-30 Credits per thread)
- **Taint Reduction** (faction-specific rituals, 20-100 Credits)

#### 3. `docs/codex/campaign-loot-tables.html`
**Add loot drops:**
- **Soulstone Shards** (T1: common, T2: uncommon, T3: rare)
- **Replacement Threads** (salvaged from destroyed caskets)
- **Soulstone Cores** (rare, from boss enemies or faction vendors)

---

## Faction-Specific Expansions

### Church of Absolution
**Add lore section: "The Dual Penance"**
- Pilot's penance = physical suffering (strapped in, legs removed, neural thread pain)
- Soul's penance = spiritual torment (trapped in crystal, feeding on fragments)
- Both must earn redemption through service

### Dwarven Forge-Guilds
**Add lore section: "Runic Thread Engineering"**
- Threads etched with micro-runes (enhance signal strength, reduce Thread Snap risk)
- Soulstone Cores shaped as geometric polyhedrons (maximize energy efficiency)
- "Compact Form" ritual = all four limbs removed, runic stumps replace flesh

### The Ossuarium
**Add lore section: "Efficient Form Philosophy"**
- Living pilots undergo flesh reduction (only skull + spine remain)
- Bound souls are fed constantly (high refinement rate, high Taint accumulation)
- "Souls are fuel. We've always been clear about this."

### Elven Verdant Covenant
**Add lore section: "The Mourned Necessity"**
- Elves view caskets as abomination (against natural cycle)
- But use them anyway to survive (pragmatic horror)
- Root-Grafting ritual = legs replaced with living vines (pilot becomes part-plant)

---

## Testing & Validation

### Playtesting Checklist

- [ ] Test Soulstone Energy depletion over 3-mission campaign
- [ ] Test Thread Snap mechanics in combat (frequency, impact on gameplay)
- [ ] Test Taint accumulation and Void Corruption events
- [ ] Test faction-specific Soul Sacrifice mechanics (Church Shortening, Dwarf Compact Form, etc.)
- [ ] Test Soulstone refinement economy (are Shards too common? too rare?)
- [ ] Test emergency field recharge (is risk/reward balanced?)

---

## Implementation Priority

### Phase 1: Core Lore Updates (Week 1)
1. Add `lore-caskets-revised.html`
2. Add `lore-soulstone-system.html`
3. Add `lore-neural-threads.html`
4. Add deprecation banners to old files

### Phase 2: Rules Integration (Week 2)
1. Create `rules-soulstone-energy.html`
2. Create `rules-thread-snap.html`
3. Update `rules-combat.html` with Thread Snap mechanics
4. Update `rules-component-damage.html` with new components

### Phase 3: Campaign/Scenario Updates (Week 3)
1. Update settlement phase (refinement, thread maintenance, Taint reduction)
2. Update loot tables (add Soulstone Shards)
3. Update scenario templates (add Energy/Thread mechanics)

### Phase 4: Faction Expansions (Week 4)
1. Expand Church lore (Dual Penance)
2. Expand Dwarf lore (Runic Threads)
3. Expand Ossuarium lore (Efficient Form)
4. Expand Elf lore (Mourned Necessity)

---

## Open Questions

1. **Should old files be deleted or preserved?**
   - Recommendation: Preserve with deprecation banners (historical reference)

2. **Should Soulstone Energy be tracked per-mission or per-campaign?**
   - Recommendation: Per-campaign (resource management tension)

3. **How frequently should Thread Snaps occur?**
   - Recommendation: ~10-15% chance per mission (impactful but not constant)

4. **Should Taint be reversible or permanent?**
   - Recommendation: Reversible but expensive (tension between power and corruption)

5. **Should faction Soulstone shapes be purely cosmetic or have mechanical effects?**
   - Recommendation: Purely cosmetic (maintains balance, supports player expression)

---

## Completion Criteria

**Definition of Done:**
- [ ] All contradictions resolved (no references to "neural fluid" or "pilot = soul")
- [ ] All new mechanics documented (Energy, Taint, Thread Snap)
- [ ] All faction lore expanded (Church, Dwarves, Ossuarium, Elves)
- [ ] All HTML files cross-referenced (proper navigation links)
- [ ] Playtest scenarios updated with new mechanics
- [ ] README.md updated with "Revised Casket System" notice

---

**Next Steps:**
1. Review this plan
2. Approve/modify proposed changes
3. Begin Phase 1 implementation (convert markdown to HTML, add deprecation banners)
4. Playtest new mechanics
5. Iterate based on feedback
