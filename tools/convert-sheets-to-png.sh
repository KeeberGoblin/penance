#!/bin/bash
# Convert all TTS deck sheets from SVG to PNG
# Requires: Inkscape or ImageMagick

echo "============================================"
echo "TTS Deck Sheet Converter"
echo "Converting SVG → PNG for Tabletop Simulator"
echo "============================================"
echo ""

# Check for Inkscape (preferred)
if command -v inkscape &> /dev/null; then
    echo "✓ Found Inkscape (using for high-quality conversion)"
    CONVERTER="inkscape"
elif command -v convert &> /dev/null; then
    echo "✓ Found ImageMagick (using for conversion)"
    CONVERTER="imagemagick"
else
    echo "✗ Error: Neither Inkscape nor ImageMagick found"
    echo ""
    echo "Install one of these:"
    echo "  Inkscape: sudo apt-get install inkscape"
    echo "  ImageMagick: sudo apt-get install imagemagick"
    exit 1
fi

echo ""
echo "Converting files..."
echo ""

# Function to convert using Inkscape
convert_inkscape() {
    local input=$1
    local output=$2
    inkscape "$input" --export-type=png --export-filename="$output" --export-dpi=300 2>/dev/null
}

# Function to convert using ImageMagick
convert_imagemagick() {
    local input=$1
    local output=$2
    convert "$input" -resize 1500x5250 "$output" 2>/dev/null
}

# Universal Core
if [ -f "universal-core-sheet.svg" ]; then
    if [ "$CONVERTER" == "inkscape" ]; then
        convert_inkscape "universal-core-sheet.svg" "universal-core.png"
    else
        convert_imagemagick "universal-core-sheet.svg" "universal-core.png"
    fi
    echo "✓ universal-core.png"
fi

# Church sheets
for i in 1 2 3; do
    if [ -f "church-sample-sheet$i.svg" ]; then
        if [ "$CONVERTER" == "inkscape" ]; then
            convert_inkscape "church-sample-sheet$i.svg" "church-deck-$i.png"
        else
            convert_imagemagick "church-sample-sheet$i.svg" "church-deck-$i.png"
        fi
        echo "✓ church-deck-$i.png"
    fi
done

# Dwarven sheets
for i in 1 2 3; do
    if [ -f "dwarves-sample-sheet$i.svg" ]; then
        if [ "$CONVERTER" == "inkscape" ]; then
            convert_inkscape "dwarves-sample-sheet$i.svg" "dwarves-deck-$i.png"
        else
            convert_imagemagick "dwarves-sample-sheet$i.svg" "dwarves-deck-$i.png"
        fi
        echo "✓ dwarves-deck-$i.png"
    fi
done

echo ""
echo "============================================"
echo "Conversion Complete!"
echo "============================================"
echo ""
echo "Next steps:"
echo "1. Upload PNG files to Imgur: https://imgur.com/upload"
echo "2. Copy image URLs (right-click → copy image address)"
echo "3. Import to TTS using Custom Deck"
echo ""
echo "See TTS-PROVING-GROUNDS-SETUP.md for detailed instructions"
echo ""
