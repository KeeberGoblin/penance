# Tabletop Simulator Playtest Guide
## Penance: Absolution Through Steel

**Version**: 0.1
**Last Updated**: October 9, 2025

---

## Yes! You Can Absolutely Playtest in Tabletop Simulator

Tabletop Simulator (TTS) is perfect for online playtesting with friends. Here's how to create Penance resources for TTS.

---

## Quick Start: What You Need

### 1. **Card Sheets** (Most Important)
TTS imports cards from image sheets (10 cards per sheet recommended).

**Standard TTS Card Sheet Format**:
- Resolution: **4096x4096 pixels** (or 2048x2048 for smaller files)
- Format: **PNG or JPG**
- Layout: **10 cards in 2 rows of 5** (most common)
  - Each card: **819x1024 pixels** (poker-sized)
- Alternative: **69 cards in 7x10 grid** (for full decks)

### 2. **Card Backs**
- Single image for all card backs
- Resolution: **819x1024 pixels**
- Can be same image repeated, or unique artwork

### 3. **Player Mats / Boards**
- Hex board image
- Player reference mat
- Format: **PNG**, any reasonable size (2048x2048 works well)

### 4. **Tokens**
- Heat tokens, Taint tokens, Ammo tokens
- Can use TTS built-in tokens or custom images

---

## Step-by-Step: Creating TTS Card Sheets

### Method 1: Nanideck (Recommended for Prototyping)

**Nanideck** is a free tool specifically for creating card sheets for TTS.

1. Download Nanideck: https://www.nandeck.com/
2. Write card data in simple script format
3. Export directly to TTS-compatible sheets

**Example Nanideck Script** (for Universal Cards):
```
CARDSIZE=6.3,8.8
DPI=300
LINK=data.csv

[Card]
RECTANGLE=0,0,6.3,8.8,#FFFFFF,SOLID
FONT=Arial,24,B
TEXT="[name]",0.5,0.5,5.8,1,CENTER,#000000
FONT=Arial,18
TEXT="[type]",0.5,1.5,5.8,0.5,LEFT,#666666
TEXT="SP: [sp_cost]",0.5,2,2.5,0.5,LEFT,#333333
TEXT="Range: [range]",3.5,2,2.5,0.5,LEFT,#333333
FONT=Arial,16
TEXTBOX="[effect]",0.5,3,5.8,3,LEFT,#000000,#F5F5F5
```

### Method 2: Photoshop / GIMP Template

1. Create 4096x4096 canvas
2. Place 10 card images (2 rows x 5 columns)
3. Each card: 819x1024 pixels
4. Export as PNG

**Template Layout**:
```
┌─────────────────────────────────────────────────────┐
│  [Card1] [Card2] [Card3] [Card4] [Card5]            │
│  [Card6] [Card7] [Card8] [Card9] [Card10]           │
└─────────────────────────────────────────────────────┘
```

### Method 3: Google Sheets → Image Export

1. Design cards in Google Sheets (each cell = 1 card)
2. Use "Download as PDF"
3. Convert PDF to PNG (online tools or Photoshop)
4. Crop and arrange into 10-card grid

---

## Uploading to Tabletop Simulator

### Option A: Direct Image URL (Fastest)

1. Upload card sheets to **Imgur** or **Google Drive** (public link)
2. In TTS: `Objects → Components → Custom → Custom Deck`
3. Paste image URLs:
   - **Face URL**: Your card sheet image
   - **Back URL**: Your card back image
4. Set deck dimensions: **Width 5, Height 2** (for 10 cards)
5. Click "Import"

### Option B: Steam Workshop (Best for Sharing)

1. Create mod in TTS
2. Add all cards, boards, tokens
3. Save & Upload to Steam Workshop
4. Friends subscribe to your workshop mod
5. Load mod in-game

**Pros**: Permanent, easy to share, version control
**Cons**: Requires Steam account, upload time

---

## Penance-Specific TTS Setup

### What You'll Need to Create

#### 1. **Universal Card Deck** (10 cards)
- 1 sheet with all 10 Universal cards
- Card back: "Penance Universal" design

#### 2. **Equipment Cards** (Start with 5 weapons)
- Longsword (4 cards)
- Greatsword (5 cards)
- Bow (4 cards)
- Shield (3 cards)
- Hammer (4 cards)
- Total: 20 cards = 2 sheets

#### 3. **Damage Cards** (10 types)
- Cracked Soulveins
- Shattered Plating
- Creaking Joints
- Mangled Actuators
- etc.
- 1 sheet with 10 different Damage cards

#### 4. **Hex Board**
- 7x7 hex grid for Arena mode
- Can use TTS built-in hexes OR custom image
- Recommend: Use **TTS Zone Tools** to create hex snap points

#### 5. **Player Mats**
- Casket status tracker (component damage)
- Heat tracker (0-9)
- Taint tracker (0-10)
- SP dial
- Deck/Discard/Hand zones

#### 6. **Tokens**
- Heat: Red cubes/chips
- Taint: Purple cubes/chips
- Ammo: Yellow cubes/chips
- Damage markers: Use TTS built-in damage counters

---

## Sample Card Sheet Creation Workflow

### For Your First Playtest (Minimal Viable):

**Week 1: Create Assets**
1. Design 10 Universal cards in PowerPoint/Google Slides (simple text boxes)
2. Export each card as PNG (819x1024)
3. Arrange 10 PNGs into grid using free tool: **PhotoCollage** or **Canva**
4. Upload to Imgur
5. Import to TTS

**Week 2: Playtest**
6. Host TTS game, invite 1 friend
7. Play 1v1 Arena match (Scout vs Heavy)
8. Take notes on:
   - Confusing rules
   - Balance issues
   - Fun factor
   - Card text clarity

**Week 3: Iterate**
9. Revise card text based on feedback
10. Re-export card sheet
11. Update TTS deck (replace old image URL with new one)
12. Playtest again

---

## TTS Scripting (Optional, Advanced)

Tabletop Simulator supports Lua scripting for automation.

### Useful Scripts for Penance:

**Auto-Shuffle on Deck Empty**:
```lua
function onObjectDeck(deck)
    if deck.tag == "Deck" and deck.getQuantity() == 0 then
        -- Shuffle discard pile into new deck
        local discard = getObjectFromGUID("discard_pile_guid")
        discard.shuffle()
    end
end
```

**Heat Tracker Button**:
```lua
function addHeat()
    local counter = getObjectFromGUID("heat_counter_guid")
    counter.Counter.increment()
end
```

**Taint Tracker with Warning at 10**:
```lua
function checkTaint()
    local taint = getObjectFromGUID("taint_counter_guid")
    if taint.Counter.getValue() >= 10 then
        printToAll("ABOMINATION TRANSFORMATION!", {1,0,0})
    end
end
```

**You don't NEED scripting for first playtest**, but it can automate tedious bookkeeping.

---

## Free Tools for Card Creation

### Graphic Design (No Photoshop Required):
1. **Canva** (browser-based, free tier): https://www.canva.com
   - Templates for cards
   - Drag-and-drop interface
   - Export as PNG

2. **GIMP** (free Photoshop alternative): https://www.gimp.org
   - Full image editing
   - Layer support
   - Batch processing

3. **Inkscape** (vector graphics, free): https://inkscape.org
   - Scalable card designs
   - PDF export

### Card Sheet Generators:
1. **Nanideck** (recommended): https://www.nandeck.com
   - Script-based card generation
   - CSV data import
   - Direct TTS export

2. **Squib** (Ruby-based): https://squib.rocks
   - Code-driven card creation
   - Version control friendly
   - Programmers will love this

3. **Card Maker** (online): https://mtg.design (Magic card style, but adaptable)
   - Browser-based
   - Quick prototypes
   - Export PNG

### Image Hosting:
1. **Imgur** (easiest): https://imgur.com
   - Free, no account needed
   - Direct image links work in TTS

2. **Google Drive** (if you have storage):
   - Upload image
   - Share → "Anyone with link can view"
   - Right-click image → "Open in new tab" → Copy URL

3. **GitHub** (if you're a developer):
   - Upload to repo
   - Use raw.githubusercontent.com URLs
   - Free, version controlled

---

## Example: Creating Your First TTS Deck (30 Minutes)

### Step 1: Design Cards (15 min)
1. Open Google Slides
2. Set slide size: Custom → 2.5" x 3.5" (poker card size)
3. Create 10 slides (1 per Universal card)
4. Format:
   - Title: Card name (e.g., "Desperate Lunge")
   - Subtitle: Type (e.g., "UNIVERSAL - Action")
   - Body: SP cost, Range, Effect
   - Footer: Heat, Keywords

### Step 2: Export & Arrange (10 min)
5. File → Download → PNG (all slides)
6. Use free tool "PhotoCollage" or open PowerPoint
7. Create 4096x4096 canvas
8. Place 10 card images in 2x5 grid
9. Export as PNG

### Step 3: Upload to TTS (5 min)
10. Upload PNG to Imgur
11. Open TTS → Objects → Custom → Custom Deck
12. Paste image URL
13. Set Width: 5, Height: 2
14. Click Import
15. **Done!** You now have a playable deck.

---

## Hex Board for TTS

### Option 1: Use TTS Built-In Hexes
1. `Objects → Components → Layout Tools → Hex Grid`
2. Set to 7x7
3. Enable "Snap to grid"
4. Good for quick prototypes

### Option 2: Custom Hex Image
1. Create hex board in Inkscape/Illustrator
2. Export as PNG (2048x2048)
3. Upload to Imgur
4. TTS: `Objects → Components → Custom → Custom Board`
5. Paste image URL
6. Set snap points manually (or use TTS Zone Tool mod)

**Recommended Size**: 7x7 hexes for Arena, 12x12 for Raid mode

---

## Player Mat Template

Create a simple reference mat:

```
┌─────────────────────────────────────────┐
│  CASKET STATUS                          │
│  ┌────────┬────────┬────────┬────────┐  │
│  │ R.Arm  │ L.Arm  │Chassis │ Legs   │  │
│  │ [    ] │ [    ] │ [    ] │ [    ] │  │
│  │ 0-9    │ 0-9    │ 0-9    │ 0-9    │  │
│  └────────┴────────┴────────┴────────┘  │
│                                         │
│  HEAT: [ 0 1 2 3 4 5 6 7 8 9 ]          │
│  TAINT: [ 0 1 2 3 4 5 6 7 8 9 10 ]      │
│  SP SAFE ZONE: [ Scout: 5 | Heavy: 3 ] │
│                                         │
│  ┌──────┐  ┌──────┐  ┌──────┐          │
│  │ Deck │  │ Hand │  │Discard│          │
│  │      │  │      │  │       │          │
│  └──────┘  └──────┘  └──────┘          │
└─────────────────────────────────────────┘
```

Export this as PNG, upload, use as custom table in TTS.

---

## Recommended First Playtest Setup

### Minimal TTS Mod Contents:
1. **2 Decks**: Universal cards (10 each player)
2. **2 Equipment sets**: Longsword + Shield (Scout), Greatsword (Heavy)
3. **1 Hex board**: 7x7 grid
4. **2 Player mats**: Status trackers
5. **Tokens**: Heat (red cubes), Taint (purple cubes)
6. **1 Rule card**: Quick reference (SP costs, combat resolution)

**Total Assets Needed**:
- 3-4 card sheets (40 cards total)
- 1 hex board image
- 2 player mat images
- Built-in TTS tokens (no custom needed)

**Time to Create**: 2-3 hours if you've never used TTS before, 30-60 min once you know the workflow.

---

## Steam Workshop Publishing (Once You're Happy)

1. In TTS: `Games → Create → Single Player`
2. Build your mod (place all cards, boards, tokens)
3. `Menu → Save & Play → Create`
4. Name it: "Penance: Absolution Through Steel - Playtest v0.1"
5. Add description with rules summary
6. `Upload` → Steam Workshop
7. Share Workshop link with friends
8. They subscribe, load mod, play!

---

## Tips for Online Playtesting

### Communication:
- Use **Discord** voice chat while playing TTS
- Screen share rules doc on second monitor
- One person narrates combat resolution

### House Rules for First Test:
- Use simplified combat (auto-hit, no dice)
- Ignore Heat/Taint for first game (focus on core loop)
- Play to 5 VP instead of 10 (faster games)
- Allow "take-backs" for rule misunderstandings

### Note-Taking During Play:
- One player keeps Google Doc open
- Write down:
  - "This card text is confusing"
  - "SP costs feel wrong for X"
  - "We had fun when Y happened"
  - "Turn took too long because Z"

---

## Alternative: Roll20 (If You Don't Have TTS)

Roll20 is free and browser-based (no Steam required).

**Pros**:
- Free, no purchase needed
- Browser-based (works on any OS)
- Built-in dice roller

**Cons**:
- More tedious setup than TTS
- Less 3D immersion
- Harder to manipulate cards

**If using Roll20**:
1. Upload card images individually
2. Create deck using "Card Deck" tool
3. Use hex grid overlay
4. Manually track Heat/Taint in text boxes

---

## Next Steps

1. **This Week**: Create 10 Universal cards in Google Slides
2. **Next Week**: Export, upload to Imgur, import to TTS
3. **Week After**: Host first playtest game with 1 friend
4. **Month 1**: Iterate based on feedback, expand to 30 cards

---

## Resources

### Software:
- **Nanideck**: https://www.nandeck.com
- **Canva**: https://www.canva.com
- **GIMP**: https://www.gimp.org
- **Inkscape**: https://inkscape.org

### TTS Guides:
- Official TTS Wiki: https://kb.tabletopsimulator.com/custom-content/custom-deck/
- TTS Subreddit: r/tabletopsimulator
- Boardgame Design Lab (TTS tutorials): https://www.youtube.com/@BoardGameDesignLab

### Image Hosting:
- **Imgur**: https://imgur.com
- **Google Drive**: https://drive.google.com

---

**You absolutely can playtest Penance online with friends!** Start simple (10 Universal cards + 2 weapons), get it into TTS, play a game, iterate. The first version will be rough, but that's the point—playtesting reveals what works and what doesn't.

Good luck, and happy playtesting! 🎲⚔️
