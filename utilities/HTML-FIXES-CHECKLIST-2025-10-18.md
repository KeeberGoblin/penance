# HTML Fixes Checklist - Quick Reference
**Date**: October 18, 2025
**Source**: HTML-ACCURACY-AUDIT-2025-10-18.md

This checklist provides exact file paths and line numbers for all fixes identified in the audit.

---

## CRITICAL PRIORITY - Fix Broken Links (5 minutes)

### ✅ Fix 1: Nomad Faction Deck Link
**File**: `/workspaces/penance/docs/codex/faction-nomads.html`
**Line**: 62
**Current**:
```html
<td><a href="https://github.com/KeeberGoblin/penance/blob/main/docs/factions/nomads/deck-complete-design.md" target="_blank">View Full Nomad Deck</a></td>
```
**Replace With**:
```html
<td><a href="https://github.com/KeeberGoblin/penance/blob/main/docs/factions/nomads/deck-equipment-system.md" target="_blank">View Full Nomad Deck (v2.0 Equipment System)</a></td>
```

---

### ✅ Fix 2: Emergent Faction Deck Link
**File**: `/workspaces/penance/docs/codex/faction-emergent.html`
**Line**: 58
**Current**:
```html
<td><a href="https://github.com/KeeberGoblin/penance/blob/main/docs/factions/emergent/deck-complete-design.md" target="_blank">View Full Emergent Deck (v2.0 Equipment System)</a></td>
```
**Replace With**:
```html
<td><a href="https://github.com/KeeberGoblin/penance/blob/main/docs/factions/emergent/deck-equipment-system.md" target="_blank">View Full Emergent Deck (v2.0 Equipment System)</a></td>
```

---

## HIGH PRIORITY - Update Outdated Content (1-2 hours)

### ✅ Fix 3: Combat System Page v2.0 Update
**File**: `/workspaces/penance/docs/codex/rules-combat.html`
**Lines**: 24-58 (entire "Deck Composition" section)

**Current Issue**: Describes v1.0 fixed 30-card deck system
**Required**: Update to v2.0 variable deck system (26-50 cards)

**Replacement Content**:
Replace lines 24-58 with:

```html
<h3>Deck Composition (v2.0 Modular Equipment System)</h3>

<p>Your deck represents your Casket's HP. Every card you discard = damage taken.</p>

<p><strong>v2.0 Variable Deck System</strong> (26-50 cards depending on equipment):</p>
<ul>
    <li><strong>10 Universal Cards</strong> (mandatory, everyone has these)</li>
    <li><strong>6 Faction Core Cards</strong> (faction-specific foundation)</li>
    <li><strong>Equipment Cards (variable 3-30 cards)</strong>: Weapon + Shield/Offhand + Accessories</li>
    <li><strong>2 Faction Tactic Cards</strong> (chosen from 5 available, pick 2 before battle)</li>
</ul>

<p><strong>Total: 26-50 cards</strong> (Light Caskets ~26-32, Heavy Caskets ~38-50)</p>

<div style="background: var(--aged-gold); border-left: 5px solid var(--dark-red); padding: 1rem; margin: 1.5rem 0;">
    <p style="margin: 0; font-style: italic;">
        <strong>NOTE:</strong> The examples below show simplified v1.0 fixed-deck structure for teaching purposes. In v2.0, players have full flexibility to customize equipment loadouts. See individual faction deck pages for complete v2.0 modular equipment options.
    </p>
</div>
```

**Also Update**: Line 19 description
**Current**: "tactical combat Hybrid • Version 2.0 • Dual-Layer Damage: Casket HP (30 cards) + Pilot Wounds (10 cards)"
**Replace With**: "tactical combat Hybrid • Version 2.0 • Dual-Layer Damage: Casket HP (26-50 cards, variable) + Pilot Wounds (10 cards)"

---

## MEDIUM PRIORITY - Add Disclaimers (30 minutes)

### ✅ Fix 4: Scenarios Page - Church Pre-Built Deck Disclaimer
**File**: `/workspaces/penance/docs/codex/scenarios.html`
**Line**: After line 140 (end of Church deck section)

**Add**:
```html
<p style="font-style: italic; opacity: 0.8; color: var(--aged-gold); margin-top: 1rem; padding: 0.75rem; background: rgba(139, 115, 85, 0.2); border-left: 3px solid var(--dark-red);">
    <strong>NOTE:</strong> This is a simplified starter deck (29 cards) for teaching scenario purposes. In v2.0 full rules, players can build decks ranging from 26-50 cards using the modular equipment system. See the <a href="faction-church.html">Church faction page</a> for complete equipment options.
</p>
```

---

### ✅ Fix 5: Scenarios Page - Dwarves Pre-Built Deck Disclaimer
**File**: `/workspaces/penance/docs/codex/scenarios.html`
**Line**: After line 155 (end of Dwarves deck section)

**Add**:
```html
<p style="font-style: italic; opacity: 0.8; color: var(--aged-gold); margin-top: 1rem; padding: 0.75rem; background: rgba(139, 115, 85, 0.2); border-left: 3px solid var(--dark-red);">
    <strong>NOTE:</strong> This is a simplified starter deck (33 cards) for teaching scenario purposes. In v2.0 full rules, players can build decks ranging from 26-50 cards using the modular equipment system. See the <a href="faction-dwarves.html">Dwarven faction page</a> for complete equipment options.
</p>
```

---

### ✅ Fix 6: Content Home - Add Version Guide
**File**: `/workspaces/penance/docs/codex/content-home.html`
**Line**: After line 46 (after "For the Uninitiated" section, before "The Manuscript's Contents")

**Add**:
```html
<h2>Version Guide: What Do I Need?</h2>

<table style="margin-bottom: 2rem;">
    <thead>
        <tr>
            <th>Version</th>
            <th>Description</th>
            <th>Status</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>v2.0 Base Rules</strong></td>
            <td>Complete playable game (turn structure, combat, equipment, 4 factions with decks + support units)</td>
            <td>✅ Required</td>
        </tr>
        <tr>
            <td><strong>v3.0 Optional Rules</strong></td>
            <td>Advanced mechanics: Dice Pool Advantage, Taint Exploitation, Pilot Grit - use if desired for additional tactical depth</td>
            <td>⭕ Optional</td>
        </tr>
        <tr>
            <td><strong>Campaign System</strong></td>
            <td>Long-term persistent play with pilot progression, settlement management, 15-enemy bestiary, event tables, loot economy (works with v2.0 or v3.0)</td>
            <td>⭕ Optional</td>
        </tr>
    </tbody>
</table>

<p style="font-style: italic; opacity: 0.8;">
    <strong>TL;DR:</strong> v2.0 is the complete game. v3.0 adds optional complexity. Campaign extends gameplay. Pick what fits your table.
</p>
```

---

## LOW PRIORITY - Add Status Banners (15 minutes total)

**Template** (use for all 6 design-only faction pages):
```html
<!-- Insert AFTER the faction header/torn paper effect, BEFORE the <div class="content"> tag -->
<div style="background: linear-gradient(135deg, #d4af37 0%, #b8956a 100%); border: 3px solid var(--dark-red); padding: 1.5rem; margin: 0;">
    <p style="color: var(--ink-brown); font-weight: 700; text-align: center; margin: 0; font-size: 1.1rem;">
        ⚠️ PLAYTEST-READY FACTION ⚠️
    </p>
    <p style="color: var(--ink-brown); text-align: center; margin: 0.5rem 0 0 0;">
        Complete deck system (21 cards), support units (6), and faction mechanics. Ready for alpha playtesting. Not included in official v2.0 playtest package.
    </p>
</div>
```

### ✅ Fix 7: Nomad Collective Status Banner
**File**: `/workspaces/penance/docs/codex/faction-nomads.html`
**Line**: After line 22 (after torn paper SVG), before line 24 (`<div class="content">`)

---

### ✅ Fix 8: The Exchange Status Banner
**File**: `/workspaces/penance/docs/codex/faction-exchange.html`
**Line**: After torn paper SVG, before `<div class="content">`

---

### ✅ Fix 9: Vestige Bloodlines Status Banner
**File**: `/workspaces/penance/docs/codex/faction-bloodlines.html`
**Line**: After line 22 (after torn paper SVG), before line 24 (`<div class="content">`)

---

### ✅ Fix 10: Emergent Syndicate Status Banner
**File**: `/workspaces/penance/docs/codex/faction-emergent.html`
**Line**: After line 22 (after torn paper SVG), before line 24 (`<div class="content">`)

---

### ✅ Fix 11: Crucible Packs Status Banner
**File**: `/workspaces/penance/docs/codex/faction-crucible.html`
**Line**: After torn paper SVG, before `<div class="content">`

---

### ✅ Fix 12: The Wyrd Conclave Status Banner
**File**: `/workspaces/penance/docs/codex/faction-fae.html`
**Line**: After torn paper SVG, before `<div class="content">`

---

## LOW PRIORITY - Standardize Labels (10 minutes)

### ✅ Fix 13-18: Add "(v2.0 Equipment System)" to Faction Links

**Files to update**: All 6 design-only faction pages
**Line**: The `<td>` with deck link in the "Complete Deck" row

**Pages**:
1. `faction-nomads.html` line 62 (already updating for broken link)
2. `faction-exchange.html` - deck link row
3. `faction-bloodlines.html` line 58 - already has label ✅
4. `faction-emergent.html` line 58 (already updating for broken link)
5. `faction-crucible.html` - deck link row
6. `faction-fae.html` - deck link row

**Template**:
```html
<td><a href="https://github.com/KeeberGoblin/penance/blob/main/docs/factions/[faction-folder]/deck-equipment-system.md" target="_blank">View Full [Faction Name] Deck (v2.0 Equipment System)</a></td>
```

---

## OPTIONAL - External Link Verification (30 minutes)

### ✅ Fix 19: Run Link Checker

**Command**:
```bash
cd /workspaces/penance
grep -rh "github.com/KeeberGoblin/penance/blob/main" docs/codex/*.html | grep -o "blob/main/[^\"]*" | sort -u > /tmp/github-links.txt
```

**Then manually verify each path exists**:
```bash
while read path; do
    file_path="${path#blob/main/}"
    if [ ! -f "$file_path" ]; then
        echo "BROKEN: $path"
    fi
done < /tmp/github-links.txt
```

---

## Summary

| Priority | Fixes | Time Estimate |
|----------|-------|---------------|
| CRITICAL | 2 broken links | 5 minutes |
| HIGH | 1 combat page update | 1-2 hours |
| MEDIUM | 3 disclaimers/guides | 30 minutes |
| LOW | 6 status banners + 6 label updates | 25 minutes |
| OPTIONAL | Link verification | 30 minutes |
| **TOTAL** | **18 fixes** | **~3 hours** |

---

## Testing After Fixes

1. ✅ Click both Nomad and Emergent deck links - should load markdown files
2. ✅ Check combat system page displays v2.0 variable deck info
3. ✅ Verify scenarios page has deck disclaimers
4. ✅ Confirm content-home has version guide
5. ✅ Check all 6 design-only faction pages have status banners
6. ✅ Verify all faction deck links have "(v2.0 Equipment System)" label

---

**Checklist Complete** - All fixes documented with exact paths and line numbers.
