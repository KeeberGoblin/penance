# Card Template Specification
## Penance: Absolution Through Steel - Visual Design Document

**Version**: 1.0
**Date**: October 12, 2025
**Purpose**: Technical specification for card template creation

---

## Template Overview

**Design Philosophy**: 70% Artwork, 30% Information (Hybrid Minimal Frame)

**Inspiration**: Pokémon TCG Full Art + MTG Borderless + Custom Penance Identity

---

## Physical Card Specifications

### Dimensions
- **Standard Size**: 2.5" × 3.5" (63mm × 88mm) - Poker card standard
- **Print Resolution**: 300 DPI
- **Digital Dimensions**: 750px × 1050px @ 300 DPI
- **Bleed Area**: +0.125" (3mm) all sides → 2.75" × 3.75" total print area
- **Safe Zone**: -0.25" (6mm) from edge (critical text only)

### Print Specifications
- **Color Mode**: CMYK (printing), RGB (digital/TTS)
- **Card Stock**: 300gsm linen finish
- **Coating**: Matte finish (anti-glare)
- **Corner Radius**: 3mm rounded corners

---

## Card Anatomy - Detailed Breakdown

### Vertical Layout Distribution

```
┌─────────────────────────────────────┐ 0px
│ HEADER BAR (15% height = 158px) │
│ - Card Name (left) │
│ - SP Cost Badge (top right) │
│ - Faction Icon (top left) │
├─────────────────────────────────────┤ 158px
│ │
│ │
│ ARTWORK AREA (60% height = 630px) │
│ │
│ - Full bleed to edges │
│ - Extends behind text box │
│ │
│ │
├─────────────────────────────────────┤ 788px
│ TEXT BOX (25% height = 262px) │
│ - Semi-transparent background │
│ - Effect text │
│ - Keywords │
│ - Flavor quote │
│ - Corner badges (DMG, RNG, INIT) │
└─────────────────────────────────────┘ 1050px
```

---

## Element Specifications

### 1. Header Bar (0-158px)

**Position**: Top 15% of card (0-158px vertical)
**Background**: Faction-specific gradient (left-to-right)

#### Header Background Colors (CMYK)

**Church of Absolution**:
- Gradient: `#2A0000 → #8B0000` (dark crimson → blood red)
- CMYK: C:0 M:100 Y:100 K:83 → C:0 M:100 Y:100 K:45

**Dwarven Forge-Guilds**:
- Gradient: `#3D2800 → #DAA520` (dark bronze → molten gold)
- CMYK: C:0 M:35 Y:100 K:76 → C:0 M:26 Y:85 K:14

**The Ossuarium**:
- Gradient: `#1A1A1A → #4B8B3B` (shadow black → necrotic green)
- CMYK: C:0 M:0 Y:0 K:90 → C:70 M:0 Y:80 K:45

**Elven Verdant Covenant**:
- Gradient: `#0D3D0D → #228B22` (deep forest → emerald)
- CMYK: C:90 M:0 Y:90 K:76 → C:90 M:0 Y:90 K:45

---

#### Card Name
- **Position**: 30px from left, 60px from top (centered vertically in header)
- **Font**: "Cinzel" or "Trajan Pro" (serif, all caps)
- **Size**: 32px (14pt @ 300 DPI)
- **Weight**: Bold (700)
- **Color**: White (#FFFFFF)
- **Stroke**: 3px black outline (for contrast)
- **Max Width**: 450px (truncate if needed)

#### SP Cost Badge
- **Position**: 680px from left, 30px from top (top right corner)
- **Shape**: Circle (80px diameter)
- **Background**: Gold (#DAA520) with inner glow
- **Border**: 4px white outline
- **Number Font**: "Anton" or "Impact" (bold sans-serif)
- **Number Size**: 48px (21pt @ 300 DPI)
- **Number Color**: Black (#000000)

#### Faction Icon
- **Position**: 30px from left, 30px from top (top left corner)
- **Size**: 60×60px
- **Style**: White silhouette icon on transparent background
- **Icons**:
 - Church: Gothic cross with crown of thorns
 - Dwarves: Anvil with hammer
 - Ossuarium: Skull with vertebrae
 - Elves: Thornbush leaf with roots

---

### 2. Artwork Area (158-788px)

**Position**: 15% to 75% vertical (158-788px)
**Dimensions**: 750px wide × 630px tall
**Treatment**: Full bleed, extends to left/right edges

#### Artwork Guidelines
- **Bleed**: Artwork extends 3mm beyond card edges (left/right)
- **Composition**: Keep critical detail in center 600×500px area
- **Bottom 30%**: Avoid busy detail (text box overlay area)
- **Top 20%**: Avoid busy detail (header bar area)
- **Safe Composition Area**: 600px × 350px (center of artwork)

#### Artwork Masking
- **No Mask Top/Left/Right**: Artwork extends to card edges
- **Bottom Mask**: Soft gradient fade (788-830px) where text box begins
- **Opacity**: Artwork 100% at 788px → 80% at 830px (fade into text box)

---

### 3. Text Box Area (788-1050px)

**Position**: Bottom 25% of card (788-1050px vertical)
**Dimensions**: 750px wide × 262px tall

#### Background
- **Color**: Black (#000000)
- **Opacity**: 40% (artwork visible behind)
- **Top Border**: 2px solid faction color (full width)
- **Gradient Overlay**: Subtle vignette (darker at edges)

#### Effect Text
- **Position**: 40px from left, 820px from top
- **Font**: "Roboto" or "Open Sans" (sans-serif)
- **Size**: 26px (11pt @ 300 DPI)
- **Weight**: Regular (400)
- **Color**: White (#FFFFFF)
- **Stroke**: 1px black outline (readability)
- **Line Height**: 32px (1.23 ratio)
- **Max Width**: 670px
- **Max Lines**: 4 lines (truncate if exceeds)

#### Keywords
- **Position**: 40px from left, 960px from top
- **Font**: "Roboto Condensed" (sans-serif, uppercase)
- **Size**: 20px (9pt @ 300 DPI)
- **Weight**: Bold (700)
- **Color**: Faction-specific color (lighter shade)
 - Church: #FF4444 (light crimson)
 - Dwarves: #FFD700 (bright gold)
 - Ossuarium: #66CC66 (bright green)
 - Elves: #44FF44 (bright emerald)
- **Separator**: " • " (bullet point between keywords)
- **Max Length**: 60 characters (truncate after)

#### Flavor Quote
- **Position**: 40px from left, 995px from top
- **Font**: "Crimson Text" or "Lora" (serif, italic)
- **Size**: 22px (9pt @ 300 DPI)
- **Weight**: Italic (400)
- **Color**: Light gray (#CCCCCC)
- **Max Width**: 550px
- **Max Lines**: 2 lines
- **Format**: Quotation marks "" included

---

### 4. Corner Badges

#### Damage Badge (Bottom Left)
- **Position**: 40px from left, 1000px from top
- **Shape**: Hexagon (60px width, 70px height)
- **Background**: Blood red (#8B0000)
- **Border**: 3px white outline
- **Icon**: Crossed swords (white, 30×30px)
- **Number Font**: "Anton" (bold sans-serif)
- **Number Size**: 36px (16pt @ 300 DPI)
- **Number Color**: White (#FFFFFF)
- **Format**: Damage value only (e.g., "4", "3-6", "X")

#### Range Badge (Bottom Right - Primary)
- **Position**: 600px from left, 1000px from top
- **Shape**: Hexagon (80px width, 70px height)
- **Background**: Steel blue (#4682B4)
- **Border**: 3px white outline
- **Text Font**: "Roboto Condensed" (sans-serif)
- **Text Size**: 18px (8pt @ 300 DPI)
- **Text Color**: White (#FFFFFF)
- **Format**: "Melee", "Range 3", "Arc", etc.

#### Initiative Badge (Bottom Right - Secondary)
- **Position**: 690px from left, 1000px from top
- **Shape**: Rectangular bracket "[3]"
- **Background**: Transparent (no fill)
- **Border**: 2px gold (#DAA520)
- **Number Font**: "Anton" (bold sans-serif)
- **Number Size**: 28px (12pt @ 300 DPI)
- **Number Color**: Gold (#DAA520)
- **Format**: Bracketed number (e.g., "[2]", "[—]")

---

## Faction-Specific Frame Variations

### Church of Absolution - "Martyrdom Frame"

**Frame Texture**: Gothic filigree
- **Top Corners**: Ornate cross patterns (60×60px, white, 20% opacity)
- **Bottom Corners**: Thorn vine patterns (80×40px, white, 20% opacity)
- **Border Accent**: 1px inner glow (blood red, 30% opacity)

**Header Gradient**: Dark crimson → Blood red (left to right)
**Text Box Border**: 2px blood red (#8B0000)
**Keyword Color**: Light crimson (#FF4444)

---

### Dwarven Forge-Guilds - "Forge Frame"

**Frame Texture**: Hammered metal
- **Top Corners**: Rivet patterns (5×5px dots, bronze, 40% opacity)
- **Bottom Corners**: Rune etchings (runic symbols, gold, 30% opacity)
- **Border Accent**: 2px embossed effect (darker top, lighter bottom)

**Header Gradient**: Dark bronze → Molten gold (left to right)
**Text Box Border**: 2px molten gold (#DAA520)
**Keyword Color**: Bright gold (#FFD700)

---

### The Ossuarium - "Necromantic Frame"

**Frame Texture**: Skeletal motifs
- **Top Corners**: Skull silhouettes (50×50px, white, 15% opacity)
- **Side Borders**: Vertebrae spine pattern (repeating, 10px width, 20% opacity)
- **Bottom Corners**: Bone pile patterns (scattered bones, white, 15% opacity)
- **Border Accent**: Ethereal glow (necrotic green, 10% outer glow)

**Header Gradient**: Shadow black → Necrotic green (left to right)
**Text Box Border**: 2px necrotic green (#4B8B3B)
**Keyword Color**: Bright green (#66CC66)

---

### Elven Verdant Covenant - "Living Frame"

**Frame Texture**: Organic growth
- **Top Corners**: Leaf clusters (40×60px, forest green, 30% opacity)
- **Side Borders**: Vine tendrils (flowing curves, 8px width, 25% opacity)
- **Bottom Corners**: Root patterns (branching roots, emerald, 20% opacity)
- **Border Accent**: Bioluminescent glow (soft green, 15% outer glow)

**Header Gradient**: Deep forest → Emerald (left to right)
**Text Box Border**: 2px emerald (#228B22)
**Keyword Color**: Bright emerald (#44FF44)

---

## Typography Hierarchy

### Font Families (Priority Order)

1. **Card Name**: "Cinzel" (primary) / "Trajan Pro" (fallback) / "Georgia" (web safe)
2. **Effect Text**: "Roboto" (primary) / "Open Sans" (fallback) / "Arial" (web safe)
3. **Keywords**: "Roboto Condensed" (primary) / "Arial Narrow" (fallback)
4. **Flavor Quote**: "Crimson Text" (primary) / "Lora" (fallback) / "Georgia Italic" (web safe)
5. **Numbers**: "Anton" (primary) / "Impact" (fallback) / "Arial Black" (web safe)

### Font Weights
- **Card Name**: 700 (Bold)
- **Effect Text**: 400 (Regular)
- **Keywords**: 700 (Bold)
- **Flavor Quote**: 400 (Italic)
- **Numbers**: 700 (Bold)

### Font Sizes @ 300 DPI
- **Card Name**: 32px (14pt)
- **SP Cost**: 48px (21pt)
- **Effect Text**: 26px (11pt)
- **Keywords**: 20px (9pt)
- **Flavor Quote**: 22px (9pt)
- **Damage Number**: 36px (16pt)
- **Range Text**: 18px (8pt)
- **Initiative Number**: 28px (12pt)

---

## Color Palette - Master Reference

### Universal Colors (All Cards)
- **White**: #FFFFFF (text, borders)
- **Black**: #000000 (text stroke, backgrounds)
- **Light Gray**: #CCCCCC (flavor text)
- **Gold**: #DAA520 (SP badge, initiative)

### Church of Absolution
- **Primary**: #8B0000 (blood red)
- **Dark**: #2A0000 (dark crimson)
- **Light**: #FF4444 (light crimson)
- **Accent**: #D4AF37 (gold leaf)

### Dwarven Forge-Guilds
- **Primary**: #DAA520 (molten gold)
- **Dark**: #3D2800 (dark bronze)
- **Light**: #FFD700 (bright gold)
- **Accent**: #A9A9A9 (iron gray)

### The Ossuarium
- **Primary**: #4B8B3B (necrotic green)
- **Dark**: #1A1A1A (shadow black)
- **Light**: #66CC66 (bright green)
- **Accent**: #F5F5DC (bone white)

### Elven Verdant Covenant
- **Primary**: #228B22 (emerald)
- **Dark**: #0D3D0D (deep forest)
- **Light**: #44FF44 (bright emerald)
- **Accent**: #DAA520 (amber gold)

---

## Layering Order (Bottom to Top)

1. **Base Card Background** (white, for bleed safety)
2. **Faction Frame Texture** (corner decorations, border accents)
3. **Header Bar** (gradient, solid)
4. **Artwork** (full bleed, extends to edges)
5. **Text Box Background** (40% opacity black)
6. **Text Box Top Border** (2px faction color)
7. **Effect Text** (white with stroke)
8. **Keywords** (faction color)
9. **Flavor Quote** (light gray)
10. **Corner Badges** (hexagons/brackets)
11. **Card Name** (white with stroke, on header)
12. **SP Cost Badge** (gold circle, top layer)
13. **Faction Icon** (white silhouette, top layer)

---

## Production File Structure

### Photoshop/GIMP Layer Organization

```
Card_Template_FACTION.psd
├── [LAYER GROUP] Header
│ ├── SP_Cost_Badge (smart object)
│ ├── Card_Name_Text (editable text)
│ ├── Faction_Icon (smart object)
│ └── Header_Gradient (faction-specific)
│
├── [LAYER GROUP] Artwork
│ ├── Artwork_Main (smart object, linked)
│ ├── Artwork_Fade_Mask (gradient mask)
│ └── Artwork_Safe_Guide (non-printing guide)
│
├── [LAYER GROUP] Text_Box
│ ├── Effect_Text (editable text, linked style)
│ ├── Keywords (editable text, linked style)
│ ├── Flavor_Quote (editable text, linked style)
│ ├── Text_Box_Background (40% black)
│ └── Top_Border (2px faction color)
│
├── [LAYER GROUP] Corner_Badges
│ ├── Damage_Badge (smart object)
│ ├── Range_Badge (smart object)
│ └── Initiative_Badge (smart object)
│
├── [LAYER GROUP] Frame_Decoration
│ ├── Top_Left_Corner (faction-specific)
│ ├── Top_Right_Corner (faction-specific)
│ ├── Bottom_Left_Corner (faction-specific)
│ ├── Bottom_Right_Corner (faction-specific)
│ └── Border_Accent (faction glow/texture)
│
└── [LAYER GROUP] Guides_and_Bleed
 ├── Safe_Zone_Guide (non-printing, 0.25" margin)
 ├── Bleed_Guide (non-printing, +0.125" extend)
 └── Base_Card (white background, safety layer)
```

---

## Export Settings

### For Print Production
- **Format**: PDF (Press Quality)
- **Color Mode**: CMYK
- **Resolution**: 300 DPI
- **Bleed**: 0.125" (3mm) all sides
- **Crop Marks**: Yes (outside bleed area)
- **Embed Fonts**: Yes
- **Compression**: Maximum quality (lossless)

### For Digital/Tabletop Simulator
- **Format**: PNG
- **Color Mode**: RGB
- **Resolution**: 1024×1024px (power of 2, TTS standard)
- **Transparency**: Yes (for overlay effects)
- **Compression**: PNG-24 with alpha channel

### For Web Preview
- **Format**: JPG
- **Color Mode**: RGB (sRGB color space)
- **Resolution**: 750×1050px @ 72 DPI
- **Quality**: 85% (balance size/quality)
- **Progressive**: Yes (faster web loading)

---

## Accessibility Compliance

### WCAG 2.1 AAA Standards

**Text Contrast Ratios**:
- **Card Name** (white on dark): 12:1 ratio ✓ (exceeds 7:1 requirement)
- **Effect Text** (white on 40% black over artwork): Minimum 7:1 ✓
- **Keywords** (bright color on dark): Minimum 4.5:1 ✓
- **Flavor Quote** (light gray on dark): Minimum 4.5:1 ✓

**Font Size Minimums**:
- **Primary Text** (Effect): 11pt ✓ (above 10pt minimum)
- **Secondary Text** (Keywords): 9pt ✓ (acceptable for labels)
- **Tertiary Text** (Flavor): 9pt ✓ (acceptable for decorative)

**Color Independence**:
- Damage indicated by: Red color + sword icon + "DMG" label ✓
- Faction indicated by: Color + unique icon + border texture ✓
- Card type indicated by: Text label + visual hierarchy ✓

---

## Mockup Examples

### Example 1: Church Faction Core Card

**Card**: "Blood Offering"
**Type**: Utility (Gambit)

```
┌─────────────────────────────────────┐
│ BLOOD OFFERING [0 SP] │ ← Crimson gradient header
│ ✟ (icon) │
├─────────────────────────────────────┤
│ ╔═══════════════════════════════╗ │
│ ║ [BAROQUE ARTWORK] ║ │
│ ║ Priest in Puppeteer ║ │
│ ║ Capsule, blood dripping ║ │
│ ║ from stigmata wounds, ║ │
│ ║ stained glass background ║ │
│ ╚═══════════════════════════════╝ │
├─────────────────────────────────────┤
│ Discard 2 cards from deck. Your │ ← 40% black box
│ next attack this turn: +3 damage, │ (artwork behind)
│ ignore 1 Defense. │
│ │
│ GAMBIT • SELF-HARM • BUFF │ ← Light crimson
│ "Pain purifies. Blood absolves." │ ← Gray italic
│ │
│ [Self] [1] │ ← Range, Initiative
└─────────────────────────────────────┘
```

---

### Example 2: Dwarven Faction Core Card

**Card**: "Crushing Blow"
**Type**: Attack

```
┌─────────────────────────────────────┐
│ CRUSHING BLOW [2 SP] │ ← Bronze→Gold gradient
│ ⚒ (icon) [+1 Heat] │
├─────────────────────────────────────┤
│ ╔═══════════════════════════════╗ │
│ ║ [BAROQUE ARTWORK] ║ │
│ ║ Dwarven Casket mid-swing, ║ │
│ ║ runic warhammer glowing ║ │
│ ║ blue-white, sparks flying, ║ │
│ ║ forge fires background ║ │
│ ╚═══════════════════════════════╝ │
├─────────────────────────────────────┤
│ Deal 4 damage. ARMOR PIERCING │
│ (ignore all armor/defense buffs). │
│ │
│ │
│ ATTACK • MELEE • ARMOR-PIERCING │ ← Bright gold
│ "Runes flare as hammer strikes." │ ← Gray italic
│ │
│ [4 DMG] [Melee] [2] │ ← Badges
└─────────────────────────────────────┘
```

---

### Example 3: Ossuarium Faction Core Card

**Card**: "Soul Harvest"
**Type**: Attack

```
┌─────────────────────────────────────┐
│ SOUL HARVEST [3 SP] │ ← Black→Green gradient
│ (icon) │
├─────────────────────────────────────┤
│ ╔═══════════════════════════════╗ │
│ ║ [BAROQUE ARTWORK] ║ │
│ ║ Bone Scythe mid-reap, ║ │
│ ║ green ethereal souls ║ │
│ ║ flowing from enemy into ║ │
│ ║ skeletal pilot, necrotic ║ │
│ ║ glow illuminating darkness ║ │
│ ╚═══════════════════════════════╝ │
├─────────────────────────────────────┤
│ Deal 4 damage. Recover cards equal │
│ to damage dealt from discard pile │
│ (max 4 cards). │
│ │
│ ATTACK • LIFESTEAL • VAMPIRIC │ ← Bright green
│ "Their life becomes yours." │ ← Gray italic
│ │
│ [4 DMG] [Melee] [3] │
└─────────────────────────────────────┘
```

---

### Example 4: Elven Faction Core Card

**Card**: "Leaf Dance"
**Type**: Movement + Attack

```
┌─────────────────────────────────────┐
│ LEAF DANCE [3 SP] │ ← Forest→Emerald gradient
│ (icon) │
├─────────────────────────────────────┤
│ ╔═══════════════════════════════╗ │
│ ║ [BAROQUE ARTWORK] ║ │
│ ║ Elven Casket mid-leap, ║ │
│ ║ amber-preserved pilot ║ │
│ ║ visible, thorn blades ║ │
│ ║ trailing green energy, ║ │
│ ║ leaves swirling around ║ │
│ ╚═══════════════════════════════╝ │
├─────────────────────────────────────┤
│ Move up to 3 hexes. You may make │
│ 1 attack during movement. After │
│ attacking, continue moving. │
│ │
│ MOVEMENT • ATTACK • HIT-AND-RUN │ ← Bright emerald
│ "Strike where weak. Vanish fast." │ ← Gray italic
│ │
│ [Self] [3] │
└─────────────────────────────────────┘
```

---

## Quality Control Checklist

### Before Finalizing Template:

- [ ] All fonts embedded (no missing fonts)
- [ ] Color mode correct (CMYK for print, RGB for digital)
- [ ] Resolution at 300 DPI (print) or 1024px (TTS)
- [ ] Bleed area extends 0.125" beyond trim
- [ ] Safe zone clear of critical text (0.25" margin)
- [ ] Text contrast meets WCAG AAA (7:1 ratio)
- [ ] All layers properly named and organized
- [ ] Smart objects linked (for batch editing)
- [ ] Faction-specific elements on separate layers
- [ ] Corner radius 3mm (rounded corners)

### Before Print Production:

- [ ] Artwork composition leaves space for text
- [ ] Text readable at arm's length (24-30 inches)
- [ ] Faction colors distinct from each other
- [ ] Keywords visible over artwork (contrast test)
- [ ] Damage/Range badges clear and legible
- [ ] Card name truncated properly (max 50 characters)
- [ ] Flavor quote fits in 2 lines (no overflow)
- [ ] Print test on 300gsm linen card stock
- [ ] Matte coating applied (anti-glare)
- [ ] Colors accurate (match Pantone reference)

---

**END OF SPECIFICATION**

*Template ready for implementation in Photoshop, GIMP, or Figma.*
