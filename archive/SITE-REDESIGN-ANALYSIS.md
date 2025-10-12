# Penance Website - Critical Analysis & Redesign Proposal

## Current State Analysis

### What You Have Now:
1. **Hero Section** - Tagline and description
2. **Chronicle** - 437-year timeline (horizontal scroll)
3. **Pilots (NPCs)** - 5 iconic characters
4. **Factions** - 9 factions with relationship matrix
5. **Playtest** - Download CTA

---

## Issues with Current Layout

### ❌ Information Overload
- **Too much detail too soon** - Timeline has 14 events with full paragraphs
- **Relationship matrix is complex** - 9×9 grid overwhelms first-time visitors
- **NPC bios are lengthy** - Full backstories before understanding the game

### ❌ Poor Information Hierarchy
- **No clear "What is this game?"** section
- **Mechanics buried** - Core gameplay not explained until playtest section
- **No visual hooks** - Text-heavy, no imagery or icons
- **Random order** - Timeline → NPCs → Factions → Playtest (disjointed flow)

### ❌ Weak Call-to-Action
- **Playtest CTA is last** - Users must scroll through everything
- **No sticky download button** - Easy to miss primary action
- **No "Quick Start" option** - High friction to try the game

### ❌ Missing Elements
- **No footer** - No GitHub, Discord, social links
- **No "Why play this?" section** - Missing value proposition
- **No visual identity** - All text, no iconography or thematic elements
- **No quick facts** - Playtime, player count, difficulty not stated

---

## Modern Game Site Best Practices

### ✅ Hero Section (Zenless Zone Zero, Elden Ring, Helldivers 2)
**What they do:**
- Large hero image/video background
- Concise tagline (5-10 words max)
- Single primary CTA button ("Play Now", "Download", "Wishlist")
- Optional secondary CTA ("Watch Trailer", "Learn More")

**Penance should have:**
```
[BACKGROUND: Year 0 art or mech silhouette]

PENANCE
Absolution Through Steel

"Four centuries after the end, the dead still walk.
Bound to iron shells. Seeking redemption through violence."

[DOWNLOAD PLAYTEST PACKAGE]  [EXPLORE LORE]
```

---

### ✅ Core Experience Section
**What they do:**
- 3-4 key selling points with icons
- Visual > Text (images, GIFs, diagrams)
- "At a glance" information

**Penance should have:**
```
WHY PLAY PENANCE?

[Icon: Skull+Mech]
BRUTAL TACTICAL COMBAT
Deck-as-HP. Component destruction.
Death spirals. Kingdom Death-style brutality.

[Icon: 9 Symbols]
ASYMMETRIC FACTIONS
Church martyrs. Dwarven engineers.
Fae tricksters. 9 unique playstyles.

[Icon: Casket]
BODY HORROR MECHS
Pilot your own corpse. Sacrifice
limbs for power. Permanent consequences.

[Icon: Book]
437 YEARS OF LORE
Post-apocalyptic world. 14 major
events. Deep narrative campaign.
```

---

### ✅ "Show, Don't Tell" Content
**What they do:**
- Large images/screenshots
- Short captions
- Interactive elements

**Penance should have:**
```
FACTIONS AT WAR

[Grid of 9 faction cards with art/icons]
Hover to see faction description (2-3 sentences)
Click to expand full lore

Instead of: Full relationship matrix upfront
```

---

### ✅ Social Proof & Momentum
**What they do:**
- "Join 10,000 players"
- Community quotes/testimonials
- Development updates/roadmap

**Penance should have:**
```
CURRENTLY IN ALPHA PLAYTEST

2 Complete Factions | 2 Scenarios | 64-Page Rulebook
More factions coming Q2 2025

[GitHub Stars] [Discord Members] [Playtest Downloads]
```

---

### ✅ Footer (Every Modern Site)
**What they need:**
- GitHub repo
- Discord/community
- Creator contact
- License info
- Related projects

**Penance footer:**
```
PENANCE: Absolution Through Steel
A tactical card-driven mech combat game

[GitHub] [Rules PDF] [Tabletop Simulator]
Created by [Your Name] | MIT License
```

---

## Proposed New Layout (Top to Bottom)

### 1. **HERO** (Full screen, immediate impact)
- Background: Year 0 art or mech silhouette
- Tagline: "Absolution Through Steel"
- Subtitle: One sentence hook
- Primary CTA: "Download Playtest"
- Secondary CTA: "Explore Chronicle"

### 2. **CORE EXPERIENCE** (4 boxes, visual icons)
- Brutal Combat
- Asymmetric Factions
- Body Horror Mechs
- Deep Lore
- Each: Icon + Title + 2 sentences

### 3. **FACTIONS SHOWCASE** (Visual grid)
- 9 cards with faction icons/symbols
- Hover: Faction name + tagline
- Click: Expand to full description
- Remove relationship matrix (move to dedicated page)

### 4. **KEY MECHANICS** (Diagram-based)
- Deck-as-HP visual
- Component damage illustration
- SP economy chart
- Less text, more diagrams

### 5. **CHRONICLE** (Condensed, optional)
- Keep horizontal scroll timeline
- BUT: Collapse to "Major Events" by default
- Show only year numbers, expand on click
- OR: Move to dedicated /chronicle page

### 6. **ICONIC PILOTS** (Keep but simplify)
- 5 cards with character art
- Name + Faction + One-liner
- Click to expand full bio
- Remove upfront detail

### 7. **PLAYTEST CTA** (Prominent, repeated)
- Same as hero section
- "Ready to play? Download the alpha."
- Links to rules, TTS mod, Discord

### 8. **FOOTER** (Essential links)
- GitHub, Discord, itch.io, Reddit
- Rules PDF, Playtest package, TTS Workshop
- Creator info, License

---

## Recommended Cuts

### Move to Dedicated Pages:
- **Full Chronicle** → `/chronicle.html` (keep simple version on home)
- **Relationship Matrix** → `/factions.html` (keep grid on home)
- **Full NPC Bios** → `/pilots.html` (keep cards on home)
- **Detailed Mechanics** → `/rules.html` (keep overview on home)

### Remove Entirely:
- Inline rulebook sections (link to PDF instead)
- Excessive timeline detail (14 events is too many for homepage)

---

## Visual Identity Improvements

### Add Iconography:
- Faction symbols (9 unique icons)
- Mechanic icons (SP, Heat, Component Damage)
- Resource icons (Soulstones, Taint, etc.)

### Add Color Coding:
- Factions: Each has a signature color
- Card types: Universal, Primary, Secondary, Tactics
- Threat levels: Safe Zone, Danger Zone

### Add Diagrams:
- Casket anatomy (component locations)
- Deck composition pie chart
- Example combat flow

---

## Implementation Priority

### Phase 1: Immediate (Homepage Redesign)
1. Simplify Hero section
2. Add Core Experience section (4 boxes)
3. Condense Factions to grid
4. Move Chronicle to condensed version
5. Add Footer

### Phase 2: Polish
6. Add faction icons/symbols
7. Create mechanic diagrams
8. Add hover interactions
9. Optimize mobile layout

### Phase 3: Expansion
10. Create dedicated `/chronicle.html`
11. Create dedicated `/factions.html`
12. Create dedicated `/pilots.html`
13. Add media gallery (card art, Casket designs)

---

## Example Flow (New Homepage)

```
[SCROLL]

HERO (Full screen)
"PENANCE: Absolution Through Steel"
[Download] [Explore]
   ↓
CORE EXPERIENCE (4 boxes)
Why play this game?
   ↓
FACTIONS (9-card grid)
Choose your path
   ↓
MECHANICS (Visual diagrams)
How it works
   ↓
CHRONICLE (Collapsed timeline)
437 years of history
   ↓
PILOTS (5 character cards)
Iconic heroes
   ↓
PLAYTEST CTA (Repeated)
Ready to play?
   ↓
FOOTER (Links)
GitHub | Discord | Rules
```

---

## Brutalist Style Preserved

### Keep:
- Black/white/blood-red color scheme
- Sharp borders, no rounded corners
- System fonts
- High contrast
- Minimal animations
- Direct, unflinching language

### Add:
- Strong grid layouts
- Bold typography hierarchy
- Generous white space
- Iconography (brutal, simple symbols)
- Clear visual sections

---

## Bottom Line

**Current site:** Encyclopedia of information, hard to parse, weak CTA
**Goal:** Product showcase, clear value prop, easy to start playing

**Key Changes:**
1. Hero-first design
2. Visual hierarchy (icons, diagrams, cards)
3. Condensed content (details in sub-pages)
4. Strong, repeated CTAs
5. Footer with community links

**Inspiration:** Zenless Zone Zero, Elden Ring, Helldivers 2, Slay the Spire
**Style:** Brutalist product page, not a wiki
