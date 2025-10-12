# Card Layout Design Research
## Penance: Absolution Through Steel

**Research Date**: October 12, 2025
**Purpose**: Explore artwork-prominent card layouts with minimal text for Penance TCG

---

## Research Summary

Based on analysis of modern TCG design trends (Pokémon TCG, Magic: The Gathering, and industry best practices), this document outlines design principles for creating cards that showcase artwork while maintaining functional gameplay information.

---

## Key Design Principles

### 1. Visual Hierarchy Fundamentals

**Primary Rule**: "There's a pecking order to the data elements on a card"

**Hierarchy Tools**:
- **Size**: Larger elements = more importance
- **Color**: High contrast = attention grabbing
- **Location**: Top/center = primary focus
- **Shape**: Unique shapes = distinct information types
- **Texture**: Visual interest guides the eye

**Application for Penance**:
- Artwork should be largest element (60-70% of card)
- Card name should be second most prominent
- SP cost/damage values need high contrast (gold/blood-red)
- Faction identity through color coding (borders/frames)

---

### 2. Artwork-to-Text Ratio

**Industry Standard**:
- **Full Art Cards**: 70-85% artwork, 15-30% text/data
- **Standard Cards**: 50-60% artwork, 40-50% text/data
- **Text-Heavy Cards**: 30-40% artwork, 60-70% text/data

**Best Practice**: "Art usually serves no gameplay purpose other than eye candy, but benefits most from being front and center and as large as possible."

**Recommendation for Penance**:
- Use **Full Art** approach for faction core cards (showcase identity)
- Use **Hybrid** approach for equipment/tactics (balance function/beauty)
- Artwork positioned center/top-center with minimal text overlay

---

### 3. Text Legibility Standards

**Minimum Font Size**: 10pt (accessibility requirement)
- Below 10pt = accessibility issues for visually impaired
- 12-14pt recommended for primary gameplay text
- 8-9pt acceptable ONLY for flavor quotes

**Contrast Requirements**:
- White text on dark backgrounds (85%+ contrast)
- Drop shadows or stroke outlines for text over artwork
- Avoid placing critical text over busy artwork sections

**Text Priority**:
1. Card name (largest)
2. SP cost/damage (high contrast, corner placement)
3. Effect text (readable size, clear background)
4. Flavor text (smallest, lowest priority)

---

### 4. Modern TCG Layout Trends (2024-2025)

### Pokémon TCG Full Art Cards

**Introduced**: Black & White expansion (2011)
**Design Philosophy**: "Full art cards are a type of card where the artwork takes up the whole card, allowing illustrators to make the most of their creative abilities"

**Key Features**:
- Artwork extends to all edges (bleed to border)
- Text boxes are transparent overlays or minimal frames
- Card name integrated into artwork (top center)
- Stats/costs in small corner badges

**2024 Evolution** (Pokémon TCG Pocket):
- "Artwork new to the game, following the expanding line of alternate art cards"
- Depicts creatures "in their natural habitat or expressing their personality outside of battle"
- Minimal UI elements, maximum immersion

---

### Magic: The Gathering Borderless Cards

**Total MTG Borderless Cards**: 2,804+ designs (as of 2024)

**Borderless Definition**: "Artwork illustrated with artistic aesthetics that extend beyond traditional card frames"

**Notable Implementations**:
- **Wilds of Eldraine**: Anime borderless cards (Japanese art style)
- **FINAL FANTASY crossover**: Woodblock borderless (50 cards)
- **Unstable**: Borderless basic lands (landscape focus)

**Design Approach**:
- No visible border/frame (or extremely minimal)
- Text placed in semi-transparent boxes overlaid on art
- Card information concentrated in top/bottom strips
- Artwork "bleeds" to edges for immersive effect

---

## Card Layout Archetypes

### Archetype 1: Full Art Overlay (80% Artwork)

**Structure**:
```
┌─────────────────────┐
│  [NAME]      [COST] │  ← Transparent overlay, top 10%
│                     │
│                     │
│    FULL ARTWORK     │  ← 80% of card space
│                     │
│                     │
│ [TEXT BOX - SEMI]   │  ← Transparent overlay, bottom 10%
│  TRANSPARENT        │
└─────────────────────┘
```

**Pros**:
- Maximum artwork showcase
- Stunning visual impact
- Great for faction identity cards

**Cons**:
- Limited text space (not suitable for complex effects)
- Text readability depends on artwork contrast
- May need multiple font sizes

**Best For**:
- Faction core cards (6 per faction)
- Iconic legendary pilots
- Promotional/showcase cards

---

### Archetype 2: Center Art with Framed Text (60% Artwork)

**Structure**:
```
┌─────────────────────┐
│ [NAME]       [COST] │  ← Solid header bar
├─────────────────────┤
│                     │
│   CENTER ARTWORK    │  ← 60% of card space
│                     │
├─────────────────────┤
│  SOLID TEXT BOX     │  ← 30% bottom area
│  - Effect text      │
│  - Keywords         │
│  "Flavor quote"     │
└─────────────────────┘
```

**Pros**:
- Clear separation of art and text
- Excellent readability
- Space for complex mechanics

**Cons**:
- More traditional layout
- Less immersive than full art
- Artwork feels "boxed in"

**Best For**:
- Equipment cards (varied text complexity)
- Universal core cards (standardization)
- Tactical cards (detailed effects)

---

### Archetype 3: Hybrid Minimal Frame (70% Artwork)

**Structure** (RECOMMENDED FOR PENANCE):
```
┌─────────────────────┐
│[NAME]         [SP]  │  ← Minimal top bar (10%)
│ ┌─────────────────┐ │
│ │                 │ │
│ │   FULL BLEED    │ │  ← 70% artwork
│ │    ARTWORK      │ │     (extends behind)
│ │                 │ │
│ └─────────────────┘ │
│ [DMG] Effect text   │  ← Bottom strip (20%)
│ "Flavor"      [RNG] │     Semi-transparent
└─────────────────────┘
```

**Pros**:
- Best of both worlds (art + readability)
- Artwork extends behind text (depth effect)
- Clean, modern aesthetic
- Faction colors visible in frame

**Cons**:
- Requires careful artwork composition
- Text placement must avoid busy art areas
- More complex to template

**Best For**:
- PRIMARY RECOMMENDATION for Penance
- Works for all card types
- Scalable complexity (adjust text area as needed)

---

## Specific Recommendations for Penance

### Layout Choice: Hybrid Minimal Frame (70% Artwork)

**Rationale**:
1. Showcases baroque-romanticist-brutalist art (primary visual identity)
2. Maintains clear gameplay information (critical for complex mechanics)
3. Faction colors visible in frame borders (Church red, Dwarves gold, etc.)
4. Text boxes semi-transparent (artwork visible behind, adds depth)

---

### Card Anatomy - Penance Template

```
DIMENSIONS: 2.5" × 3.5" (standard poker size, 63mm × 88mm)

┌─────────────────────────────────┐
│ CARD NAME            [SP COST]  │  ← 15% height
│ Faction Icon         [HEAT]     │     Solid colored bar
├─────────────────────────────────┤     (faction-specific gradient)
│ ╔═══════════════════════════╗   │
│ ║                           ║   │
│ ║                           ║   │
│ ║    BAROQUE ARTWORK        ║   │  ← 60% height
│ ║    (Full Bleed)           ║   │     Artwork extends to edges
│ ║                           ║   │
│ ║                           ║   │
│ ╚═══════════════════════════╝   │
├─────────────────────────────────┤
│ [DAMAGE] Effect text here       │  ← 25% height
│ Keywords: attack, melee         │     Semi-transparent (40%)
│ "Flavor quote in italics"       │     Artwork visible behind
│ [RANGE]           [INITIATIVE]  │
└─────────────────────────────────┘
```

---

### Element Specifications

#### 1. Header Bar (Top 15%)
- **Background**: Faction-specific gradient
  - Church: Dark crimson → blood red
  - Dwarves: Dark bronze → molten gold
  - Ossuarium: Shadow black → necrotic green
  - Elves: Deep forest → vibrant emerald
- **Card Name**: 14pt bold, white with black stroke
- **SP Cost**: 16pt bold, gold circle badge (top right)
- **Faction Icon**: 20×20px symbol (top left)

#### 2. Artwork Area (60%)
- **Full Bleed**: Artwork extends to card edges
- **No Internal Border**: Artwork flows seamlessly
- **Composition Guide**: Leave bottom 30% less busy (text overlay area)

#### 3. Text Box (Bottom 25%)
- **Background**: 40% opacity black (artwork visible behind)
- **Border**: 2px faction-colored line (top edge only)
- **Effect Text**: 11pt sans-serif, white, 1px black stroke
- **Flavor Text**: 9pt serif italic, light gray
- **Keywords**: 9pt uppercase, faction color highlights

#### 4. Corner Badges
- **Damage (Bottom Left)**: Red hexagon, white number, 12pt
- **Range (Bottom Right)**: Blue hexagon, white icon/text, 10pt
- **Initiative (Bottom Right)**: Gold bracket [3], 10pt

---

## Visual Hierarchy Execution

### Primary (Seen First):
1. **Artwork** (largest element, central focus)
2. **Card Name** (top, high contrast)
3. **SP Cost** (gold badge, recognizable shape)

### Secondary (Seen Second):
4. **Effect Text** (clear, readable, high contrast)
5. **Damage/Range** (corner badges, color-coded)

### Tertiary (Seen Last):
6. **Keywords** (small, supplementary)
7. **Flavor Text** (decorative, lowest priority)
8. **Initiative** (reference info, corner)

---

## Faction Frame Variations

### Church of Absolution
- **Frame Color**: Blood red (#8B0000)
- **Accent**: Gold leaf details
- **Texture**: Gothic filigree (subtle, corners only)
- **Artwork Style**: Martyrdom scenes, stained glass, dramatic lighting

### Dwarven Forge-Guilds
- **Frame Color**: Molten gold (#DAA520)
- **Accent**: Iron gray rivets
- **Texture**: Hammered metal, rune etchings
- **Artwork Style**: Fortress-tanks, forge fires, stone architecture

### The Ossuarium
- **Frame Color**: Necrotic green (#4B8B3B) over shadow black
- **Accent**: Bone white
- **Texture**: Skeletal motifs (vertebrae spine border)
- **Artwork Style**: Necromantic rituals, bone architecture, ethereal glow

### Elven Verdant Covenant
- **Frame Color**: Forest green (#228B22)
- **Accent**: Amber gold
- **Texture**: Organic vines, leaf patterns
- **Artwork Style**: Living wood, thorns, bioluminescent flora

---

## Technical Implementation Notes

### For Print Production:
- **Bleed Area**: 0.125" (3mm) on all sides
- **Safe Zone**: Keep critical text 0.25" (6mm) from edges
- **Resolution**: 300 DPI minimum for artwork
- **Color Mode**: CMYK for printing (not RGB)

### For Digital (Tabletop Simulator):
- **Resolution**: 1024×1024px recommended
- **Format**: PNG with transparency (for overlay effects)
- **Color Mode**: RGB for digital display
- **File Size**: Under 2MB per card (performance)

### For Prototyping:
- **Print Size**: Standard poker cards (2.5" × 3.5")
- **Card Stock**: 300gsm linen finish
- **Coating**: Matte finish (reduces glare, tactile feel)
- **Corners**: Rounded 3mm radius

---

## Accessibility Considerations

### Text Contrast:
- **WCAG AAA Standard**: 7:1 contrast ratio (large text)
- **Implementation**: White text on dark backgrounds
- **Stroke/Shadow**: 1-2px black outline for text over artwork

### Font Size Accessibility:
- **Primary Text**: 11-12pt minimum (gameplay effects)
- **Secondary Text**: 10pt minimum (keywords)
- **Tertiary Text**: 9pt minimum (flavor quotes)
- **Never Below**: 8pt (unreadable for many players)

### Color Blindness:
- **Don't Rely on Color Alone**: Use icons + text
- **Damage Badge**: Red hex + sword icon
- **Defense Badge**: Blue hex + shield icon
- **Faction Identity**: Color + unique border texture

---

## Comparison to Existing TCG Layouts

### Pokémon TCG Full Art Style
- **Similarity**: Artwork bleeds to edges
- **Difference**: Penance uses semi-transparent text box (not floating badges)
- **Why Different**: Complex effects need more text space

### MTG Borderless Style
- **Similarity**: No visible frame/border
- **Difference**: Penance retains minimal top bar (faction identity)
- **Why Different**: Players need instant faction recognition

### Flesh and Blood TCG
- **Similarity**: Bottom text box with artwork above
- **Difference**: Penance artwork extends behind text (depth effect)
- **Why Different**: Maximize artwork visibility while keeping text readable

---

## Next Steps

### Phase 1: Template Creation
1. Create Photoshop/GIMP template (layered PSD)
2. Define exact pixel measurements (300 DPI print)
3. Create faction-specific frame variations (4 templates)

### Phase 2: Prototype Testing
1. Print 10 sample cards (2-3 per faction + universal)
2. Test readability at arm's length (gameplay distance)
3. Gather feedback on artwork visibility vs. text clarity

### Phase 3: Iteration
1. Adjust text box opacity (30-50% range testing)
2. Refine corner badge sizes/placement
3. Finalize font choices (readability + theme)

### Phase 4: Full Production
1. Commission artwork (baroque-romanticist-brutalist style)
2. Apply template to all 60+ cards
3. Create print-ready files (CMYK, 300 DPI, bleed)

---

## Reference Images Analysis

Based on user-provided Pinterest examples, common design patterns:

### Pattern 1: Overlay Text on Full Art
- Text boxes are semi-transparent (20-50% opacity)
- Critical info (name, cost) in solid color bars
- Artwork composition leaves space for text (top/bottom)

### Pattern 2: Minimal Geometric Frames
- Thin border lines (1-3px) define card edges
- Corner accents (faction symbols, decorative elements)
- Artwork extends to frame (not boxed in)

### Pattern 3: Layered Depth Effect
- Artwork appears behind text box (layering)
- Drop shadows create depth perception
- Text "floats" above artwork (visual separation)

**Recommended Approach for Penance**: Combine all three patterns
- Semi-transparent text box (40% opacity)
- Thin faction-colored border (2px)
- Layered artwork extending behind text

---

## Inspirational Quote

*"Art usually serves no gameplay purpose other than eye candy, but benefits most from being front and center and as large as possible."*
— Dylan Mangini, Card Game Designer

*"There's a pecking order to the data elements on a card. Hierarchical design uses characteristics like size, color, and location to guide players through information in a specific and intentional manner."*
— Matt Paquette, Tabletop Graphic Designer

---

**END OF RESEARCH DOCUMENT**

*"In iron we seek forgiveness. Through blood, absolution."*
