# Tactical Map Generator

Generate beautiful SVG hex maps for Penance scenarios using simple text abbreviations.

## Quick Start

```bash
python3 generate-tactical-map.py example-map-config.txt output-map.svg
```

## Terrain Abbreviations

| Code | Terrain Type | Game Effect |
|------|-------------|-------------|
| `OG` | Open Ground | No modifiers |
| `FR` | Forest | +1 Defense when targeted |
| `RU` | Rubble | +1 Defense, costs 2 SP to enter |
| `WA` | Water/Mud | -1 Heat generation |
| `E1` | Elevation +1 | +1 damage to lower targets |
| `E2` | Elevation +2 | +2 damage, +1 Range to lower targets |
| `PC` | Church Deploy | Player starting zone (auto-highlighted) |
| `PD` | Dwarf Deploy | Enemy starting zone (auto-highlighted) |

## Config File Format

```
TITLE: Your Map Title
SUBTITLE: Optional subtitle text

ROW1:  PC PC FR FR OG OG OG OG FR FR OG OG
ROW2:  PC WA WA WA RU RU RU RU WA WA WA OG
ROW3:  PC WA OG OG OG OG OG OG OG OG WA OG
...
```

### Rules:
- Lines starting with `#` are comments
- `TITLE:` sets the map title (appears at top)
- `SUBTITLE:` sets optional subtitle text
- `ROW1:`, `ROW2:`, etc. define terrain row-by-row
- Each row contains space-separated terrain codes
- All rows should have the same number of columns (typically 12)

## Example

See [example-map-config.txt](example-map-config.txt) for a complete 12×12 map configuration.

Generate it with:
```bash
python3 generate-tactical-map.py example-map-config.txt my-map.svg
```

## Features

- **Automatic hex offset**: Even rows are automatically offset for proper hex grid alignment
- **Deployment zones**: `PC` and `PD` codes auto-highlight with colored borders
- **Elevation labels**: E1 and E2 hexes display text labels
- **Full legend**: Generated maps include complete terrain legend and compass rose
- **Gothic theme**: Dark parchment background with golden accents matching Penance aesthetic

## Tips

1. **Grid size**: Standard maps are 12×12 (144 hexes), but any size works
2. **Deployment zones**: Place 6-9 hexes in opposite corners for balanced deployment
3. **Terrain variety**: Mix 30-40% special terrain (water, rubble, forest, elevation)
4. **Chokepoints**: Use water/rubble to create tactical bottlenecks
5. **High ground**: Place E2 hexes centrally as contested objectives

## Workflow

1. Sketch your map on paper or in a spreadsheet
2. Convert to terrain codes in a text file
3. Run the generator
4. Open SVG in browser or image viewer
5. Tweak config and regenerate as needed
6. Copy final SVG to `docs/codex/images/`

## Output

Generated SVG files are:
- 1200×1100 viewBox (scalable vector graphics)
- Self-contained (no external dependencies)
- Ready for web use or print
- ~15-20KB file size

## Advanced Usage

### Custom Titles
```
TITLE: The Scorched Wastes
SUBTITLE: 10×10 Hex Tactical Map - Scenario #5
```

### Asymmetric Maps
```
ROW1: OG OG FR FR OG OG
ROW2: WA WA WA OG OG FR
ROW3: WA E1 WA OG RU RU
```
*Each row can have different column counts (generator will handle it)*

### Comments
```
# Northern deployment zone
ROW1: PC PC FR OG OG OG
ROW2: PC PC OG OG OG OG

# Central contested area
ROW3: OG E2 E2 OG OG OG
ROW4: OG E2 E2 OG OG OG

# Southern deployment zone
ROW5: OG OG OG OG PD PD
ROW6: OG OG OG FR PD PD
```
