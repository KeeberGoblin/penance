# Tabletop Simulator Import Guide
## Penance: Absolution Through Steel

This guide shows you how to import Penance cards into Tabletop Simulator for online playtesting.

---

## Quick Start (5 Minutes)

### Step 1: Generate Card Sheets

**Option A: Use Pre-Generated Sheets (Recommended)**
1. Navigate to `/tools/` folder
2. Find `church-sample-sheet.svg` (5 Church cards)
3. Open in browser or image editor
4. Export as PNG at **1500×5250 pixels**
5. Save as `church-deck-1.png`

**Option B: Generate Custom Sheets**
```bash
cd tools/
python3 generate-tts-deck.py
```

This creates SVG files you can customize and export as PNG.

---

### Step 2: Prepare Card Back

1. Open `tts-card-back.svg` in browser/editor
2. Export as PNG at **750×1050 pixels**
3. Save as `penance-card-back.png`

---

### Step 3: Upload to TTS

#### Method 1: Using Imgur (Easiest)

1. Go to https://imgur.com/upload
2. Upload your PNG files:
   - `church-deck-1.png` (deck sheet)
   - `penance-card-back.png` (card back)
3. **Right-click each image** → "Copy image address"
4. Save both URLs

#### Method 2: Using Cloud Storage

Upload to:
- Google Drive (get shareable link)
- Dropbox (get direct link)
- GitHub raw file URL

**IMPORTANT**: URL must be a direct image link ending in `.png`

---

### Step 4: Create Custom Deck in TTS

1. **Launch Tabletop Simulator**
2. **Click Objects → Components → Custom → Custom Deck**
3. **Fill in the fields:**

   **Face:**
   - Paste your deck sheet URL (`church-deck-1.png`)

   **Back:**
   - Paste your card back URL (`penance-card-back.png`)

   **Deck Configuration:**
   - Width: `2` (cards per row)
   - Height: `5` (cards per column)
   - Number: `5` (if you only made 5 cards)
   - Sideways: `No`
   - Back is Hidden: `Yes`

4. **Click Import**
5. **Your deck spawns on the table!**

---

## Technical Specifications

### Card Dimensions
- **Individual Card**: 750×1050 pixels (poker size, 5:7 aspect ratio)
- **Card Back**: 750×1050 pixels
- **Deck Sheet**: 1500×5250 pixels (2×5 grid = 10 cards max)

### File Format
- **Format**: PNG (TTS doesn't support SVG directly)
- **Compression**: Standard PNG (no need for high compression)
- **Max File Size**: ~10MB per image (Imgur limit)

### Grid Layout
Cards are arranged **left-to-right, top-to-bottom**:

```
┌─────────┬─────────┐
│ Card 1  │ Card 2  │
├─────────┼─────────┤
│ Card 3  │ Card 4  │
├─────────┼─────────┤
│ Card 5  │ Card 6  │
├─────────┼─────────┤
│ Card 7  │ Card 8  │
├─────────┼─────────┤
│ Card 9  │ Card 10 │
└─────────┴─────────┘
```

TTS automatically cuts the sheet into individual cards.

---

## Creating Complete Faction Decks

### Church of Absolution (30 Cards)

You'll need **3 deck sheets** (10 cards each):

**Sheet 1 (10 cards):**
- 10× Universal Core cards

**Sheet 2 (10 cards):**
- 10× Primary Weapon: Penitent Blades cards

**Sheet 3 (10 cards):**
- 6× Secondary Equipment cards
- 2× Faction Tactics cards
- 2× Filler/extras

**How to import multiple sheets:**
1. Create Sheet 1 as described above
2. Repeat for Sheet 2 and Sheet 3 (different URLs)
3. In TTS, combine all decks:
   - Stack them on top of each other
   - Right-click → "Group"
4. Shuffle the combined deck

---

## Customizing Card Templates

### Edit SVG Templates

All templates are in `/tools/`:

**tts-card-template.svg** - Individual card template
- Edit text fields: `[CARD NAME]`, `[TYPE]`, etc.
- Modify colors in `<style>` section
- Adjust layout with `<rect>`, `<text>` positions

**tts-card-back.svg** - Card back design
- Change faction branding
- Modify quote text
- Adjust geometric patterns

### Using Python Script

Edit `generate-tts-deck.py`:

```python
# Add your card data to CHURCH_CARDS list:
CHURCH_CARDS = [
    {
        'name': 'Your Card Name',
        'type': 'Attack',  # Attack, Defense, Movement, Utility, etc.
        'cost': 2,         # SP cost
        'initiative': '[2]',
        'range': 'Melee (Range 1)',
        'effect': 'Your card effect text here.',
        'damage': '5',     # Optional
        'heat': '+2',      # Optional
        'keywords': ['attack', 'melee'],
        'quote': 'Your flavor quote here.'
    },
    # Add more cards...
]
```

Run script:
```bash
python3 generate-tts-deck.py
```

Output: `church-sample-sheet.svg` (1500×5250px)

---

## Converting SVG to PNG

### Method 1: Browser Export

1. Open SVG in Chrome/Firefox
2. Right-click → "Inspect Element"
3. Console: `document.querySelector('svg').setAttribute('width', '1500')`
4. Console: `document.querySelector('svg').setAttribute('height', '5250')`
5. Right-click SVG → "Save Image As..." → PNG

### Method 2: Inkscape (Best Quality)

1. Download Inkscape (free): https://inkscape.org/
2. Open SVG file
3. **File → Export PNG Image**
4. Set dimensions: **1500×5250** (for deck sheet) or **750×1050** (for card back)
5. Export

### Method 3: Command Line (ImageMagick)

```bash
# Install ImageMagick
sudo apt-get install imagemagick

# Convert deck sheet
convert church-sample-sheet.svg -resize 1500x5250 church-deck-1.png

# Convert card back
convert tts-card-back.svg -resize 750x1050 penance-card-back.png
```

---

## Testing Your Deck

### In TTS

1. **Spawn your deck** on the table
2. **Right-click deck** → "Search"
3. **Verify all cards** display correctly
4. **Check card backs** when face-down
5. **Test shuffling** and drawing

### Common Issues

**❌ Cards appear stretched/distorted**
- Fix: Export PNG at exact dimensions (1500×5250 or 750×1050)
- Don't let image editor auto-resize

**❌ Cards are blurry**
- Fix: Export at higher DPI (300 DPI recommended)
- Ensure SVG font sizes are readable

**❌ Card back doesn't show**
- Fix: Check "Back is Hidden" is enabled
- Verify card back URL is correct

**❌ Deck imports as 10 cards but you only made 5**
- Fix: Change "Number" field to `5` in TTS import dialog
- Or fill remaining slots with blank/duplicate cards

---

## Advanced: Full Church Deck (30 Cards)

### Step-by-Step

1. **Read faction deck list**: [faction-deck-church-complete.md](../docs/faction-deck-church-complete.md)

2. **Edit Python script** with all 30 card entries:
   - 10× Universal Core
   - 12× Penitent Blades (Primary)
   - 6× Secondary Equipment (your choice)
   - 2× Faction Tactics (your choice)

3. **Generate 3 sheets**:
   ```python
   # Sheet 1: Cards 1-10
   sheet1 = create_deck_sheet(CHURCH_CARDS[0:10], sheet_number=1)

   # Sheet 2: Cards 11-20
   sheet2 = create_deck_sheet(CHURCH_CARDS[10:20], sheet_number=2)

   # Sheet 3: Cards 21-30
   sheet3 = create_deck_sheet(CHURCH_CARDS[20:30], sheet_number=3)
   ```

4. **Export all 3 sheets** as PNG
5. **Upload all 3** to Imgur
6. **Import each sheet** separately in TTS
7. **Stack and group** into one deck

---

## Dwarven Clans Deck (32 Cards)

Same process, but you'll need **4 sheets** (3 full + 1 with 2 cards):

- Sheet 1: 10 cards (Universal Core)
- Sheet 2: 10 cards (Runic Warhammer Primary)
- Sheet 3: 10 cards (Secondary + Tactics)
- Sheet 4: 2 cards (Stone Endurance bonus cards)

**Tip**: On Sheet 4, duplicate the card back SVG 8 times to fill the grid (TTS will ignore extras if you set "Number" to 2).

---

## Troubleshooting

### Font Rendering Issues

If TTS doesn't show fonts correctly:

**Option 1: Convert text to paths (Inkscape)**
1. Open SVG in Inkscape
2. Select all text: `Ctrl+A`
3. **Path → Object to Path**
4. Export PNG (fonts now baked in)

**Option 2: Use web-safe fonts**
- Change `font-family: 'Courier New'` to `font-family: monospace`

### Image Hosting Issues

**Imgur best practices:**
- Upload during off-peak hours (faster)
- Use direct image link (ends in `.png`)
- Don't use album links (use individual image URLs)

**GitHub hosting:**
1. Push PNG files to GitHub repo
2. Navigate to file on GitHub
3. Click "Raw" button
4. Copy URL (e.g., `https://raw.githubusercontent.com/user/repo/main/card.png`)

---

## Community Templates

Share your TTS deck sheets:
- Upload to GitHub: `/workspaces/penance/community/tts-decks/`
- Include faction name and version
- Follow naming: `church-v1-sheet1.png`

---

## Next Steps

1. **Generate your first deck sheet** (use `church-sample-sheet.svg`)
2. **Export as PNG** (1500×5250)
3. **Upload to Imgur**
4. **Import to TTS**
5. **Playtest online!**

For questions or help:
- Open GitHub issue: https://github.com/KeeberGoblin/penance/issues
- Tag with `[TTS]` in title

---

*"In iron we seek forgiveness. Through code, we bring it to the table."*
