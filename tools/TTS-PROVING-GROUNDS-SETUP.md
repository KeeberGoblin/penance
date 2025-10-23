# Tabletop Simulator Setup Guide
## Scenario #1: The Proving Grounds

**Quick Start**: Get the Proving Grounds scenario running in TTS in 30-60 minutes

---

## What You're Creating

A 1v1 arena match between:
- **Church of Absolution** (Aggressive Martyr build)
- **Dwarven Clans** (Defensive Fortress build)

On a 12×12 hex battlefield with elevation, water, forest, and rubble terrain.

---

## Files Generated

Your `/tools/` folder now contains:

### Deck Sheets (SVG format)
```
✅ universal-core-sheet.svg     (10 cards - both players use this)
✅ church-sample-sheet1.svg     (10 Church faction cards)
✅ church-sample-sheet2.svg     (10 Church faction cards)
✅ church-sample-sheet3.svg     (1 Church faction card)
✅ dwarves-sample-sheet1.svg    (10 Dwarven faction cards)
✅ dwarves-sample-sheet2.svg    (10 Dwarven faction cards)
✅ dwarves-sample-sheet3.svg    (1 Dwarven faction card)
```

**Total: 7 card sheets**

---

## Step 1: Convert SVG to PNG

TTS requires PNG images. You have 3 options:

### Option A: Inkscape (Best Quality)

```bash
# Install Inkscape (if not already installed)
# Ubuntu/Debian:
sudo apt-get install inkscape

# Convert all sheets
cd /workspaces/penance/tools
inkscape universal-core-sheet.svg --export-type=png --export-filename=universal-core.png
inkscape church-sample-sheet1.svg --export-type=png --export-filename=church-deck-1.png
inkscape church-sample-sheet2.svg --export-type=png --export-filename=church-deck-2.png
inkscape church-sample-sheet3.svg --export-type=png --export-filename=church-deck-3.png
inkscape dwarves-sample-sheet1.svg --export-type=png --export-filename=dwarves-deck-1.png
inkscape dwarves-sample-sheet2.svg --export-type=png --export-filename=dwarves-deck-2.png
inkscape dwarves-sample-sheet3.svg --export-type=png --export-filename=dwarves-deck-3.png
```

### Option B: ImageMagick (Command Line)

```bash
# Install ImageMagick
sudo apt-get install imagemagick

# Convert all sheets
cd /workspaces/penance/tools
convert universal-core-sheet.svg -resize 1500x5250 universal-core.png
convert church-sample-sheet1.svg -resize 1500x5250 church-deck-1.png
convert church-sample-sheet2.svg -resize 1500x5250 church-deck-2.png
convert church-sample-sheet3.svg -resize 1500x5250 church-deck-3.png
convert dwarves-sample-sheet1.svg -resize 1500x5250 dwarves-deck-1.png
convert dwarves-sample-sheet2.svg -resize 1500x5250 dwarves-deck-2.png
convert dwarves-sample-sheet3.svg -resize 1500x5250 dwarves-deck-3.png
```

### Option C: Browser Export

1. Open each SVG file in Chrome/Firefox
2. Right-click → "Save Image As..." → PNG
3. Repeat for all 7 files

---

## Step 2: Upload PNG Files

Upload your PNG files to get direct image URLs. Choose one:

### Imgur (Easiest)

1. Go to https://imgur.com/upload
2. Upload all 7 PNG files
3. For each image:
   - Right-click → "Copy image address"
   - Save the URL (should end in `.png`)

### Google Drive

1. Upload PNGs to Google Drive
2. For each file:
   - Right-click → "Get link" → "Anyone with link can view"
   - Open in browser, right-click image → "Open image in new tab"
   - Copy URL

### GitHub (For Version Control)

1. Commit PNGs to your repo
2. Navigate to each file on GitHub
3. Click "Raw" → Copy URL
   - Format: `https://raw.githubusercontent.com/user/repo/main/file.png`

---

## Step 3: Import Decks to TTS

### A. Universal Core Deck (Both Players Need)

1. **Launch Tabletop Simulator**
2. **Objects → Components → Custom → Custom Deck**
3. **Settings**:
   - Face URL: `[your universal-core.png URL]`
   - Back URL: `[your card back URL]` *(see Card Back section below)*
   - Width: `2`
   - Height: `5`
   - Number: `10`
   - Sideways: `No`
   - Back is Hidden: `Yes`
4. **Click Import**
5. **Right-click deck → "Copy" → paste to create 2nd copy**

You now have 2 Universal Core decks (one for each player).

### B. Church Deck (3 sheets = 21 cards)

**Sheet 1 (10 cards)**:
1. Objects → Custom → Custom Deck
2. Face URL: `[church-deck-1.png URL]`
3. Back URL: `[card back URL]`
4. Width: `2`, Height: `5`, Number: `10`
5. Import

**Sheet 2 (10 cards)**:
1. Repeat with `church-deck-2.png`

**Sheet 3 (1 card)**:
1. Face URL: `[church-deck-3.png URL]`
2. Width: `2`, Height: `5`, Number: `1` ← **Important: Set to 1**

**Combine All Church Cards**:
1. Stack all 3 Church decks on top of each other
2. Right-click → "Group"
3. You now have 21 Church faction cards

### C. Dwarven Deck (3 sheets = 21 cards)

Repeat the same process for Dwarves:
- dwarves-deck-1.png (10 cards)
- dwarves-deck-2.png (10 cards)
- dwarves-deck-3.png (1 card)

### D. Build Complete Decks

**Church "Martyr's Fury" (29 cards)**:
1. Take 1 Universal Core deck (10 cards)
2. Add Church faction cards (21 cards)
   - *Note: Scenario calls for 6 Church Core + 11 Equipment + 2 Tactics*
   - *Database has 21 cards total, use all*
3. Stack together → Right-click → "Group"
4. Right-click → "Shuffle"
5. Label as "Church Deck"

**Dwarven "Immovable Wall" (33 cards)**:
1. Take 1 Universal Core deck (10 cards)
2. Add Dwarven faction cards (21 cards)
3. Stack together → Group → Shuffle
4. Label as "Dwarven Deck"

---

## Step 4: Create Card Back (Optional)

If you don't have a card back yet:

### Quick Option: Solid Color
1. Objects → Components → Cards → Playing Cards
2. Take 1 card, flip it face-down
3. Use as template, or upload solid color image

### Custom Card Back:
Use the included `tts-card-back.svg`:
1. Convert to PNG (750×1050 pixels)
2. Upload to Imgur
3. Use this URL for all "Back URL" fields above

---

## Step 5: Create Hex Board

### Option A: Use TTS Built-In Hexes (Quick)

1. **Objects → Components → Layout Tools → Hex Grid**
2. **Settings**:
   - Grid Size: 12×12
   - Hex Size: Medium
   - Snap to Grid: Yes
3. **Place on table**

### Option B: Custom Hex Board (Better)

1. Create 12×12 hex grid image (use tool like Inkscape or GIMP)
2. Mark terrain types:
   - Forest (green) - 8 hexes
   - Rubble (brown) - 8 hexes
   - Water/Mud (blue) - 20 hexes
   - Elevation 1 (light gray) - 4 hexes
   - Elevation 2 (dark gray) - 4 hexes
3. Export as PNG (2048×2048 recommended)
4. Upload to Imgur
5. **Objects → Components → Custom → Custom Board**
6. Paste image URL

**Terrain Layout** (from scenario):
```
Row 1:  [F][F][ ][ ][ ][ ][ ][ ][ ][ ][F][F]
Row 2:  [F][F][R][ ][ ][ ][ ][ ][ ][R][F][F]
Row 3:  [ ][R][R][ ][ ][W][W][ ][ ][R][R][ ]
Row 4:  [ ][ ][ ][ ][W][W][W][W][ ][ ][ ][ ]
Row 5:  [ ][ ][ ][W][W][E1][E1][W][W][ ][ ][ ]
Row 6:  [ ][ ][W][W][E1][ ][ ][E1][W][W][ ][ ]
Row 7:  [ ][ ][W][W][E2][ ][ ][E2][W][W][ ][ ]
Row 8:  [ ][ ][ ][W][W][E2][E2][W][W][ ][ ][ ]
Row 9:  [ ][ ][ ][ ][W][W][W][W][ ][ ][ ][ ]
Row 10: [ ][R][R][ ][ ][W][W][ ][ ][R][R][ ]
Row 11: [F][F][R][ ][ ][ ][ ][ ][ ][R][F][F]
Row 12: [F][F][ ][ ][ ][ ][ ][ ][ ][ ][F][F]
```

**Legend**:
- F = Forest (+1 Defense)
- R = Rubble (+1 Defense, difficult terrain)
- W = Water (difficult terrain, -1 Heat when ending turn)
- E1 = Elevation 1 (+1 damage, ignore cover)
- E2 = Elevation 2 (+2 damage, +1 range, ignore cover)

---

## Step 6: Create Player Mats & Tokens

### Tokens Needed:

**Heat Tracker**:
- Use TTS built-in counters
- Objects → Components → Counters
- Label "Heat" (range 0-10)

**SP Tracker**:
- Counter labeled "SP" (range 0-5)

**Component Damage Markers**:
- Use colored cubes
- Objects → Components → Chips & Dice → Cubes
- Red for damaged components

**Casket Miniatures**:
- Use chess pieces or custom models
- Objects → Components → Chess → Knight (or use Figurines)
- Color Church piece white, Dwarven piece gray

**Facing Indicator**:
- Use small arrow or d4 die pointing direction
- Important for tracking hex-side facing

---

## Step 7: Setup Checklist

Before starting the game:

### Table Setup
- [ ] 12×12 hex board placed
- [ ] Church deployment zone marked (top-left, rows 1-3, cols 1-3)
- [ ] Dwarven deployment zone marked (bottom-right, rows 10-12, cols 10-12)

### Church Player
- [ ] Church deck (29 cards, shuffled)
- [ ] Universal Core cards mixed in
- [ ] Casket miniature (white/silver)
- [ ] Heat counter (starts at 0)
- [ ] SP counter (starts at 5)
- [ ] Component damage tracker
- [ ] Facing indicator

### Dwarven Player
- [ ] Dwarven deck (33 cards, shuffled)
- [ ] Universal Core cards mixed in
- [ ] Casket miniature (gray/brown)
- [ ] Heat counter (starts at 0)
- [ ] SP counter (starts at 4-5, check scenario)
- [ ] Rune counter (for Rune of Protection stacks)
- [ ] Component damage tracker
- [ ] Facing indicator

### Shared
- [ ] Attack dice (2d6 or custom)
- [ ] Defense dice (10+ d6 or custom)
- [ ] Initiative dice (2d6)
- [ ] Quick reference card
- [ ] Damage card deck (or proxies)

---

## Step 8: Starting the Game

### Deployment Phase

1. **Roll Initiative**: Each player rolls 2d6
   - Higher roll chooses who deploys first

2. **Deploy Caskets**:
   - First player: Place casket in deployment zone, choose facing
   - Second player: Place casket in deployment zone, choose facing

3. **Draw Opening Hands**:
   - Each player shuffles deck
   - Draw 6 cards

4. **Begin Turn 1**: First player goes first

---

## Quick Reference: TTS Controls

### Camera
- `WASD`: Pan camera
- `Right-click + drag`: Rotate view
- `Scroll wheel`: Zoom in/out
- `Q/E`: Rotate objects

### Card Manipulation
- `Left-click + drag`: Move card
- `Right-click`: Context menu (shuffle, search, etc.)
- `F`: Flip card
- `R`: Rotate card
- `Alt + Shift + Right-click`: Measure distance

### Dice
- `Left-click`: Pick up die
- `Shake mouse`: Roll die
- `Right-click`: Lock die result
- `Number keys 1-6`: Set die to specific value

---

## Troubleshooting

### Cards appear blurry
- **Fix**: Re-export PNG at higher resolution (2048×5250 instead of 1500×5250)
- Or export SVG with `--export-dpi=300` in Inkscape

### Sheet 3 shows 10 cards but only 1 exists
- **Fix**: In TTS import dialog, set "Number" to `1` instead of `10`

### Decks won't combine
- **Fix**: Make sure all decks are same card size
- Stack them directly on top of each other, then right-click → "Group"

### Card backs don't show
- **Fix**: Check "Back is Hidden" is enabled in Custom Deck settings
- Verify back URL ends in `.png` and is accessible

### Hex grid doesn't align
- **Fix**: Use TTS snap points
- Or manually place hex grid using Zone Tools mod

---

## Advanced: Lua Scripting (Optional)

### Auto-Shuffle When Deck Runs Out

```lua
function onObjectLeaveContainer(container, object)
    if container.tag == "Deck" and container.getQuantity() == 0 then
        -- Shuffle discard into new deck
        local discardPile = getObjectFromGUID("YOUR_DISCARD_GUID")
        if discardPile ~= nil then
            discardPile.shuffle()
            printToAll("Deck reshuffled! +1 Damage card added.", {1,0,0})
        end
    end
end
```

### Heat Tracker Button

Add buttons to increment/decrement heat:

```lua
function createHeatButtons()
    self.createButton({
        click_function = "addHeat",
        label = "+1 Heat",
        position = {0, 0.2, -1},
        width = 800,
        height = 400,
        font_size = 200
    })
end

function addHeat()
    local counter = getObjectFromGUID("HEAT_COUNTER_GUID")
    counter.Counter.increment()
end
```

---

## Next Steps

1. **Convert SVG to PNG** (Step 1)
2. **Upload to Imgur** (Step 2)
3. **Import to TTS** (Step 3)
4. **Create hex board** (Step 5)
5. **Invite friend** → Host multiplayer game
6. **Play Proving Grounds!**

---

## Expected Playtime

- **First game** (learning rules): 60-90 minutes
- **Experienced** (know rules): 30-45 minutes

---

## Resources

- **Main TTS Guide**: `/docs/reference/tabletop-simulator-guide.md`
- **Scenario Rules**: `/docs/scenarios/01-proving-grounds.md`
- **Card Database**: `/docs/cards/complete-card-data.json`
- **TTS Workshop**: https://steamcommunity.com/app/286160/workshop/

---

## Feedback

After playing, consider:
- Did the deck sheets display correctly?
- Were any cards confusing?
- Did the hex board work well?
- How long did setup take?

Report issues: https://github.com/KeeberGoblin/penance/issues

---

**"In iron we seek forgiveness. Through TTS, we bring it to the table."**
