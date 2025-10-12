# INDEX.HTML DICE SYSTEM OVERHAUL

**Date**: October 12, 2025
**Status**: COMPLETE
**File Updated**: `docs/index.html`

---

## Summary

Complete overhaul of the main documentation landing page ([docs/index.html](docs/index.html)) to showcase the new custom dice system. Added dedicated dice system section, updated hero statistics, revised playtest information, and integrated dice reference links throughout.

---

## Changes Made

### 1. Navigation Menu
**Added**: "DICE SYSTEM" link to top navigation bar (highlighted in accent color)

```html
<a href="#dice-system" class="nav-link" style="color: var(--accent);">DICE SYSTEM</a>
```

**Location**: Line 278
**Purpose**: Prominent navigation to new dice system section

---

### 2. Hero Section Statistics
**Updated**: Added "3 Custom Dice Types" statistic between Complete Factions and Equipment Items

**Before**:
- 4 Complete Factions
- 60+ Equipment Items
- 437 Years of Lore

**After**:
- 4 Complete Factions
- **3 Custom Dice Types** (NEW)
- 60+ Equipment Items
- 437 Years of Lore

**Location**: Lines 598-618
**Purpose**: Highlight dice system as a major feature immediately on landing

---

### 3. "Why Play" Section
**Updated**: Replaced "MODULAR EQUIPMENT SYSTEM" card with "CUSTOM DICE SYSTEM" as the 2nd feature

**New Card**:
```
CUSTOM DICE SYSTEM
3 custom d6 dice with symbols. GKR-style to-hit rolls with BattleTech modifiers.
Defense Dice create brutal variance. Every attack is a risk for attacker and defender.
```

**Location**: Lines 628-631
**Purpose**: Position dice system as a core selling point alongside deck-as-HP combat

---

### 4. NEW SECTION: Dice System (MAJOR ADDITION)

**Location**: Lines 651-864 (213 lines)
**Section ID**: `#dice-system`
**Placement**: Between "Why Play" and "Chronicle" sections

#### Subsections Included:

##### A. Announcement Banner
- Gradient background (blood-red to black)
- Highlights: "3 custom dice types, 39 cards, 7+ modifiers"
- Tagline: "Every attack is a gamble"

##### B. Dice Type Grid (3 Cards)

**Attack Dice (2d6)**:
- Symbol breakdown (⚔️ STRIKE, 💀 DEATH BLOW, ⚙️ JAM, etc.)
- Hit results table (5-6 = Hit, 9 = Crit, 10 = Component destroyed)
- Border: Blood-red

**Defense Dice (1d6 per damage)**:
- Symbol breakdown (🛡️ SHIELD, 💀 CRITICAL, 🔥 HEAT, etc.)
- Statistics: 33% block rate, 17% critical escalation
- Border: Accent (gold)

**Suffering Dice (1d6)**:
- Church-specific mechanics
- Symbols (🛡️ DIVINE MERCY, 💀 MARTYRDOM, ⚙️ ABSOLUTION)
- Border: White

##### C. To-Hit Modifiers Table
4-column grid showing:
- **Range**: Short (+0) to Extreme (+3)
- **Movement**: Attacker/defender movement penalties
- **Facing**: Front/Flank/Rear/Shield modifiers
- **Environment**: Cover, elevation

**Example**: "Long-range (+2) + moving fast (+2) + target in cover (+1) = need 10+ to hit"

##### D. Expected Hit Rates
5 probability examples:
- **97%** - Need 2+ (Rear + higher ground)
- **72%** - Need 4+ (Close range, stationary)
- **42%** - Need 7+ (Medium range + movement)
- **28%** - Need 8+ (Long range + cover)
- **8%** - Need 10+ (Extreme range + modifiers)

##### E. Dice-Optimized Cards (4 Types)
- **Accuracy Buffs**: Precision Strike, Hunter's Patience, Forge-Tempered Precision
- **Reroll Mechanics**: Second Chance, Stone Certainty
- **Auto-Hits**: Martyrdom's Certainty, Soul Harvest
- **Miss Compensation**: Divine Judgment, Runic Wrath

##### F. Design Philosophy
4 key principles:
1. **Brutal for Everyone** - Randomness affects both sides
2. **Tactical Depth** - BattleTech modifier stacking
3. **Player Agency** - 39 cards to manipulate dice
4. **Faction Identity Preserved** - Each faction has unique dice interactions

##### G. Call-to-Action
- Link to [docs/rules/dice-reference.md](docs/rules/dice-reference.md)
- Highlights: "17,000+ word specification, probability tables, card integration guide"

---

### 5. Playtest Section Updates

#### "What's Included" Statistics
**Added**: "3 Custom Dice Types" to grid

**Before**:
- 4 Complete Factions
- 60+ Equipment Items
- 132 Event Tables
- 100 Anomalous Artifacts

**After**:
- 4 Complete Factions
- **3 Custom Dice Types** (NEW)
- 60+ Equipment Items
- 132 Event Tables
- 100 Anomalous Artifacts

**Location**: Lines 1013-1015

#### Feature Cards Grid
**Added**: "Custom Dice System" card as first item

**New Card**:
```
Custom Dice System - Brutal Randomness
3 custom d6 dice (Attack, Defense, Suffering). GKR-style to-hit (base 5+)
with BattleTech modifiers. Defense Dice create unpredictable outcomes.
39 cards optimized for dice manipulation (rerolls, accuracy buffs, auto-hits,
miss compensation).
```

**Location**: Lines 1033-1039
**Purpose**: Ensure playtest section prominently features dice system

#### Download Package Summary
**Updated**: Added "3 dice types" to feature list

**Before**: "4 factions • 60+ equipment • 132 events • Campaign-ready"
**After**: "4 factions • **3 dice types** • 60+ equipment • 132 events • Campaign-ready"

**Location**: Line 1063

---

### 6. Footer Resources
**Added**: "Dice System Reference" link (2nd position after Playtest Package)

**New Link**:
```html
<li><a href="rules/dice-reference.md" class="footer-link" download>Dice System Reference</a></li>
```

**Location**: Line 1082
**Purpose**: Quick access to complete dice documentation from footer

---

## Visual Design Choices

### Color Coding by Dice Type
- **Attack Dice**: Blood-red borders (`var(--blood-red)`)
- **Defense Dice**: Accent/gold borders (`var(--accent)`)
- **Suffering Dice**: White borders (`var(--white)`)

### Section Hierarchy
1. **Announcement Banner**: Gradient background, attention-grabbing
2. **Dice Type Grid**: 3-column equal emphasis
3. **To-Hit Modifiers**: Dark background, 4-column functional layout
4. **Expected Hit Rates**: Black background with red border (emphasizes risk)
5. **Card Optimization**: Standard feature grid (familiar layout)
6. **Design Philosophy**: Left-accent border (editorial/explanatory tone)
7. **CTA**: Centered, accent-bordered, download link

### Typography Hierarchy
- **Section Header**: 1.75-2rem, accent color for dice system
- **Subsection Headers**: 1.5rem, white/accent
- **Card Titles**: 1rem, uppercase, color-coded
- **Body Text**: 0.85-1rem, light-gray, monospace for tables

---

## User Experience Improvements

### 1. Progressive Disclosure
- **Hero Stats**: Quick "3 dice types" metric
- **Why Play**: One-sentence dice system pitch
- **Dice System Section**: Full 200+ line deep dive
- **Footer**: Quick link to complete reference

### 2. Scannable Content
- Dice symbol tables use visual grid layouts
- Probability percentages use large font (2.5rem)
- Modifier categories clearly separated

### 3. Multiple Entry Points
- Top navigation menu
- "Why Play" feature card
- Dice System dedicated section
- Playtest feature card
- Footer resources link

### 4. Educational Flow
1. Show the dice (symbols, results)
2. Explain modifiers (how to-hit works)
3. Show probabilities (expected outcomes)
4. Reveal player tools (cards that manipulate dice)
5. Explain design philosophy (why this exists)
6. Link to complete reference (for deep dive)

---

## Statistics

### New Content Added
- **Lines Added**: 213 lines (Dice System section)
- **Word Count**: ~1,200 words of new content
- **Sections Modified**: 6 (Hero, Why Play, Dice System, Playtest, Footer, Navigation)
- **New Links**: 3 (Navigation, Footer Resources, CTA download)

### File Size Impact
- **Before**: ~925 lines
- **After**: ~1,138 lines
- **Increase**: +23% file size

---

## Cross-References

### Internal Links Created
1. Navigation → `#dice-system` (smooth scroll)
2. Dice System CTA → `rules/dice-reference.md` (download)
3. Footer Resources → `rules/dice-reference.md` (download)

### Related Files Referenced
- [docs/rules/dice-reference.md](docs/rules/dice-reference.md) - Complete dice system spec (17,000+ words)
- [docs/cards/new-cards-dice-system.md](docs/cards/new-cards-dice-system.md) - 39 dice-optimized cards
- [docs/reference/card-optimization-dice-system.md](docs/reference/card-optimization-dice-system.md) - Design analysis
- [DICE-SYSTEM-IMPLEMENTATION-COMPLETE.md](DICE-SYSTEM-IMPLEMENTATION-COMPLETE.md) - Master summary

---

## Testing Recommendations

### Visual Regression Testing
1. **Desktop (1920x1080)**: Verify 4-column modifier grid displays correctly
2. **Tablet (768px)**: Check dice type grid collapses to 2 columns
3. **Mobile (375px)**: Verify single-column layout, readable font sizes
4. **Smooth Scrolling**: Test `#dice-system` anchor from navigation

### Content Validation
1. **Symbol Rendering**: Verify emojis (⚔️🛡️💀🩸🔥⚙️) display correctly across browsers
2. **Link Functionality**: Test all 3 new links (nav, footer, CTA)
3. **Download Attribute**: Verify `dice-reference.md` download behavior

### Accessibility
1. **Color Contrast**: Verify light-gray text on dark backgrounds meets WCAG AA
2. **Keyboard Navigation**: Tab through navigation links, CTA buttons
3. **Screen Reader**: Test semantic HTML (h2, h3, section, nav)

---

## Next Steps (Optional Future Enhancements)

### 1. Interactive Dice Roller
- JavaScript-based dice roller widget
- Visual dice rolling animation
- Show probability distribution dynamically

### 2. Printable Dice Faces
- Downloadable PDF templates for custom d6 dice
- Cut-and-fold instructions
- Symbol stickers for standard d6

### 3. Video/GIF Examples
- Embed attack resolution walkthrough
- Show Defense Dice variance in action
- Animated to-hit modifier stacking

### 4. Comparison Table
- Side-by-side: GKR vs BattleTech vs Penance
- Highlight unique innovations

---

## Conclusion

The [docs/index.html](docs/index.html) overhaul successfully integrates the custom dice system as a core feature throughout the landing page. Users encounter the dice system at multiple touchpoints (hero stats, features, dedicated section, playtest, footer) with progressive depth of information.

The dice system section provides comprehensive visual reference (symbol tables, modifier grids, probability charts) while maintaining scannable, brutalist aesthetic consistent with Penance's design language.

**Status**: Ready for production deployment.

---

**Files Modified**:
- [docs/index.html](docs/index.html) (213 lines added, 6 sections updated)

**Files Created**:
- [INDEX-HTML-DICE-SYSTEM-UPDATE.md](INDEX-HTML-DICE-SYSTEM-UPDATE.md) (this summary)

**Related Documentation**:
- [DICE-SYSTEM-IMPLEMENTATION-COMPLETE.md](DICE-SYSTEM-IMPLEMENTATION-COMPLETE.md) - Master implementation summary
- [docs/rules/dice-reference.md](docs/rules/dice-reference.md) - Complete dice system specification
