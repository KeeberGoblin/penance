#!/usr/bin/env python3
"""
Tactical Map Generator for Penance
Generates SVG hex maps from simple text abbreviations.

Usage:
    python3 generate-tactical-map.py map-config.txt output.svg

Map Config Format:
    TITLE: The Proving Grounds
    SUBTITLE: Scenario #1
    CHURCH_DEPLOY: 1,1 1,2 2,1 2,2 3,1 3,2
    DWARF_DEPLOY: 10,10 10,11 10,12 11,10 11,11 11,12 12,10 12,11 12,12

    ROW1: PC PC FR FR OG OG OG OG FR FR OG OG
    ROW2: PC WA WA WA RU RU RU RU WA WA WA OG
    ROW3: PC WA OG OG OG OG OG OG OG OG WA OG
    ...

Terrain Abbreviations:
    OG = Open Ground
    FR = Forest
    RU = Rubble
    WA = Water/Mud
    E1 = Elevation +1
    E2 = Elevation +2
    PC = Player Church Deploy (will auto-mark)
    PD = Player Dwarf Deploy (will auto-mark)
"""

import sys
import re

# Terrain type definitions
TERRAIN_TYPES = {
    'OG': {'name': 'Open Ground', 'fill': '#3d3428', 'pattern': None, 'label': None},
    'FR': {'name': 'Forest', 'fill': 'url(#forest)', 'pattern': 'forest', 'label': None},
    'RU': {'name': 'Rubble', 'fill': 'url(#rubble)', 'pattern': 'rubble', 'label': None},
    'WA': {'name': 'Water', 'fill': 'url(#water)', 'pattern': 'water', 'label': None},
    'E1': {'name': 'Elevation +1', 'fill': 'url(#elevation1)', 'pattern': 'elevation1', 'label': 'E1'},
    'E2': {'name': 'Elevation +2', 'fill': 'url(#elevation2)', 'pattern': 'elevation2', 'label': 'E2'},
    'PC': {'name': 'Church Deploy', 'fill': 'url(#church-deploy)', 'pattern': 'church-deploy', 'label': None},
    'PD': {'name': 'Dwarf Deploy', 'fill': 'url(#dwarf-deploy)', 'pattern': 'dwarf-deploy', 'label': None},
}

# SVG pattern definitions
SVG_PATTERNS = """
    <!-- Hex pattern definition -->
    <polygon id="hex" points="30,0 60,17.32 60,51.96 30,69.28 0,51.96 0,17.32" />

    <!-- Terrain patterns -->
    <pattern id="forest" patternUnits="userSpaceOnUse" width="60" height="69.28">
      <rect width="60" height="69.28" fill="#1a3d1a"/>
      <circle cx="15" cy="17" r="3" fill="#2d5a2d" opacity="0.7"/>
      <circle cx="35" cy="25" r="4" fill="#2d5a2d" opacity="0.7"/>
      <circle cx="45" cy="45" r="3" fill="#2d5a2d" opacity="0.7"/>
      <circle cx="20" cy="50" r="4" fill="#2d5a2d" opacity="0.7"/>
    </pattern>

    <pattern id="rubble" patternUnits="userSpaceOnUse" width="60" height="69.28">
      <rect width="60" height="69.28" fill="#3d3428"/>
      <rect x="10" y="10" width="8" height="6" fill="#5a4d3a" opacity="0.8"/>
      <rect x="35" y="15" width="6" height="8" fill="#5a4d3a" opacity="0.8"/>
      <rect x="15" y="40" width="10" height="7" fill="#5a4d3a" opacity="0.8"/>
      <rect x="40" y="45" width="7" height="5" fill="#5a4d3a" opacity="0.8"/>
    </pattern>

    <pattern id="water" patternUnits="userSpaceOnUse" width="60" height="69.28">
      <rect width="60" height="69.28" fill="#1a3d5a"/>
      <path d="M0,30 Q15,25 30,30 T60,30" stroke="#2a5a7a" stroke-width="1.5" fill="none" opacity="0.6"/>
      <path d="M0,45 Q15,40 30,45 T60,45" stroke="#2a5a7a" stroke-width="1.5" fill="none" opacity="0.6"/>
    </pattern>

    <pattern id="elevation1" patternUnits="userSpaceOnUse" width="60" height="69.28">
      <rect width="60" height="69.28" fill="#4a3d2a"/>
      <line x1="0" y1="20" x2="60" y2="20" stroke="#3d3020" stroke-width="1" opacity="0.5"/>
      <line x1="0" y1="40" x2="60" y2="40" stroke="#3d3020" stroke-width="1" opacity="0.5"/>
      <line x1="0" y1="60" x2="60" y2="60" stroke="#3d3020" stroke-width="1" opacity="0.5"/>
    </pattern>

    <pattern id="elevation2" patternUnits="userSpaceOnUse" width="60" height="69.28">
      <rect width="60" height="69.28" fill="#5a4d3a"/>
      <line x1="0" y1="15" x2="60" y2="15" stroke="#4a3d2a" stroke-width="1.5" opacity="0.6"/>
      <line x1="0" y1="30" x2="60" y2="30" stroke="#4a3d2a" stroke-width="1.5" opacity="0.6"/>
      <line x1="0" y1="45" x2="60" y2="45" stroke="#4a3d2a" stroke-width="1.5" opacity="0.6"/>
      <line x1="0" y1="60" x2="60" y2="60" stroke="#4a3d2a" stroke-width="1.5" opacity="0.6"/>
    </pattern>

    <!-- Deployment zone highlights -->
    <pattern id="church-deploy" patternUnits="userSpaceOnUse" width="60" height="69.28">
      <rect width="60" height="69.28" fill="#3d2a1a" opacity="0.7"/>
      <path d="M30,10 L35,25 L50,25 L38,35 L42,50 L30,40 L18,50 L22,35 L10,25 L25,25 Z"
            fill="#8B4513" opacity="0.3"/>
    </pattern>

    <pattern id="dwarf-deploy" patternUnits="userSpaceOnUse" width="60" height="69.28">
      <rect width="60" height="69.28" fill="#2a2a3d" opacity="0.7"/>
      <rect x="20" y="20" width="20" height="30" fill="#4a5a7a" opacity="0.3"/>
      <rect x="15" y="15" width="30" height="5" fill="#4a5a7a" opacity="0.3"/>
    </pattern>
"""

SVG_LEGEND = """
  <!-- Legend -->
  <g id="legend" transform="translate(100, 750)">
    <rect x="0" y="0" width="1000" height="280" fill="#1a1410" stroke="#d4af37" stroke-width="2" rx="8"/>
    <text x="500" y="30" font-family="serif" font-size="18" font-weight="bold" fill="#d4af37" text-anchor="middle">TERRAIN LEGEND</text>

    <!-- Row 1 -->
    <use href="#hex" x="20" y="50" fill="#3d3428" stroke="#555" stroke-width="1" transform="scale(0.7)"/>
    <text x="80" y="85" font-family="serif" font-size="14" fill="#d0d0d0">Open Ground</text>
    <text x="80" y="102" font-family="serif" font-size="11" fill="#888">No modifiers</text>

    <use href="#hex" x="220" y="50" fill="url(#forest)" stroke="#555" stroke-width="1" transform="scale(0.7)"/>
    <text x="280" y="85" font-family="serif" font-size="14" fill="#d0d0d0">Forest</text>
    <text x="280" y="102" font-family="serif" font-size="11" fill="#888">+1 Defense when targeted</text>

    <use href="#hex" x="420" y="50" fill="url(#rubble)" stroke="#555" stroke-width="1" transform="scale(0.7)"/>
    <text x="480" y="85" font-family="serif" font-size="14" fill="#d0d0d0">Rubble</text>
    <text x="480" y="102" font-family="serif" font-size="11" fill="#888">+1 Defense, costs 2 SP to enter</text>

    <use href="#hex" x="720" y="50" fill="url(#water)" stroke="#555" stroke-width="1" transform="scale(0.7)"/>
    <text x="780" y="85" font-family="serif" font-size="14" fill="#d0d0d0">Water/Mud</text>
    <text x="780" y="102" font-family="serif" font-size="11" fill="#888">-1 Heat generation</text>

    <!-- Row 2 -->
    <use href="#hex" x="20" y="140" fill="url(#elevation1)" stroke="#555" stroke-width="1" transform="scale(0.7)"/>
    <text x="80" y="175" font-family="serif" font-size="14" fill="#d0d0d0">Elevation +1</text>
    <text x="80" y="192" font-family="serif" font-size="11" fill="#888">+1 damage to lower targets</text>

    <use href="#hex" x="220" y="140" fill="url(#elevation2)" stroke="#555" stroke-width="1" transform="scale(0.7)"/>
    <text x="280" y="175" font-family="serif" font-size="14" fill="#d0d0d0">Elevation +2</text>
    <text x="280" y="192" font-family="serif" font-size="11" fill="#888">+2 damage, +1 Range to lower</text>

    <use href="#hex" x="520" y="140" fill="url(#church-deploy)" stroke="#8B4513" stroke-width="2" transform="scale(0.7)"/>
    <text x="580" y="175" font-family="serif" font-size="14" fill="#d0d0d0">Church Deploy</text>
    <text x="580" y="192" font-family="serif" font-size="11" fill="#888">Player starting zone (NW)</text>

    <use href="#hex" x="720" y="140" fill="url(#dwarf-deploy)" stroke="#4a5a7a" stroke-width="2" transform="scale(0.7)"/>
    <text x="780" y="175" font-family="serif" font-size="14" fill="#d0d0d0">Dwarf Deploy</text>
    <text x="780" y="192" font-family="serif" font-size="11" fill="#888">Enemy starting zone (SE)</text>

    <!-- Strategic notes -->
    <text x="20" y="235" font-family="serif" font-size="12" font-weight="bold" fill="#d4af37">TACTICAL NOTES:</text>
    <text x="20" y="255" font-family="serif" font-size="11" fill="#a0a0a0">• Use elevation for tactical advantage</text>
    <text x="20" y="272" font-family="serif" font-size="11" fill="#a0a0a0">• Water and rubble create natural chokepoints</text>
  </g>

  <!-- Compass rose -->
  <g id="compass" transform="translate(1100, 150)">
    <circle cx="0" cy="0" r="35" fill="#1a1410" stroke="#d4af37" stroke-width="2"/>
    <polygon points="0,-25 5,-5 0,-10 -5,-5" fill="#d4af37"/>
    <text x="0" y="-40" font-family="serif" font-size="14" font-weight="bold" fill="#d4af37" text-anchor="middle">N</text>
  </g>
"""


def parse_config(config_file):
    """Parse the map configuration file."""
    with open(config_file, 'r') as f:
        lines = f.readlines()

    config = {
        'title': 'Tactical Map',
        'subtitle': '',
        'rows': []
    }

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        if line.startswith('TITLE:'):
            config['title'] = line.split(':', 1)[1].strip()
        elif line.startswith('SUBTITLE:'):
            config['subtitle'] = line.split(':', 1)[1].strip()
        elif line.startswith('ROW'):
            # Extract row data: ROW1: PC PC FR FR ...
            row_match = re.match(r'ROW\d+:\s*(.+)', line)
            if row_match:
                terrain_codes = row_match.group(1).split()
                config['rows'].append(terrain_codes)

    return config


def calculate_hex_position(row, col):
    """Calculate SVG x,y position for a hex at given row/col."""
    x_offset = 45 if row % 2 == 0 else 0  # Offset every other row
    x = col * 90 + x_offset
    y = row * 52
    return x, y


def generate_hex_grid(rows):
    """Generate SVG hex grid elements from row data."""
    grid_elements = []
    labels = []

    for row_idx, row_terrains in enumerate(rows):
        grid_elements.append(f"    <!-- Row {row_idx + 1} -->")

        for col_idx, terrain_code in enumerate(row_terrains):
            if terrain_code not in TERRAIN_TYPES:
                print(f"Warning: Unknown terrain code '{terrain_code}' at Row {row_idx + 1}, Col {col_idx + 1}. Using OG.")
                terrain_code = 'OG'

            terrain = TERRAIN_TYPES[terrain_code]
            x, y = calculate_hex_position(row_idx, col_idx)

            # Determine stroke style based on deployment zones
            if terrain_code == 'PC':
                stroke = 'stroke="#8B4513" stroke-width="2"'
            elif terrain_code == 'PD':
                stroke = 'stroke="#4a5a7a" stroke-width="2"'
            else:
                stroke = 'stroke="#555" stroke-width="1"'

            grid_elements.append(
                f'    <use href="#hex" x="{x}" y="{y}" fill="{terrain["fill"]}" {stroke}/>'
            )

            # Add label if needed (E1, E2)
            if terrain['label']:
                label_x = x + 30
                label_y = y + 36
                labels.append(
                    f'    <text x="{label_x}" y="{label_y}" font-family="monospace" font-size="10" fill="#fff" text-anchor="middle">{terrain["label"]}</text>'
                )

    return '\n'.join(grid_elements), '\n'.join(labels)


def generate_svg_map(config):
    """Generate complete SVG map from config."""
    hex_grid, hex_labels = generate_hex_grid(config['rows'])

    # Determine grid dimensions
    num_rows = len(config['rows'])
    num_cols = max(len(row) for row in config['rows'])

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1100" style="background: #2a2520;">
  <defs>
{SVG_PATTERNS}
  </defs>

  <!-- Title -->
  <text x="600" y="35" font-family="serif" font-size="28" font-weight="bold"
        fill="#d4af37" text-anchor="middle">{config['title'].upper()}</text>
  <text x="600" y="60" font-family="serif" font-size="14" fill="#a0a0a0" text-anchor="middle">
    {config['subtitle']}
  </text>

  <!-- Hex grid ({num_rows} rows × {num_cols} columns) -->
  <g id="hexGrid" transform="translate(100, 100)">
{hex_grid}
  </g>

  <!-- Hex labels -->
  <g id="hexLabels" transform="translate(100, 100)">
{hex_labels}
  </g>

{SVG_LEGEND}
</svg>
"""

    return svg


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 generate-tactical-map.py <config-file> <output-svg>")
        print("\nExample:")
        print("  python3 generate-tactical-map.py proving-grounds.txt map-proving-grounds.svg")
        sys.exit(1)

    config_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        config = parse_config(config_file)
        svg = generate_svg_map(config)

        with open(output_file, 'w') as f:
            f.write(svg)

        print(f"✓ Generated tactical map: {output_file}")
        print(f"  Title: {config['title']}")
        print(f"  Grid: {len(config['rows'])} rows × {max(len(r) for r in config['rows'])} columns")

    except FileNotFoundError:
        print(f"Error: Config file '{config_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
