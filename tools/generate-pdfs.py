#!/usr/bin/env python3
"""
PDF Generator for Penance: Absolution Through Steel
Converts markdown documentation to professionally styled PDFs
"""

import os
import sys
import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import re

# PDF Styling Template
PDF_STYLE = """
@page {
    size: Letter;
    margin: 1in 0.75in 1in 0.75in;

    @top-left {
        content: "PENANCE: Absolution Through Steel";
        font-family: "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
        font-size: 9pt;
        color: #666;
        border-bottom: 1px solid #d4af37;
        padding-bottom: 3pt;
    }

    @top-right {
        content: counter(page);
        font-family: "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
        font-size: 9pt;
        color: #666;
    }

    @bottom-center {
        content: "© 2025 Penance Project • CC BY-NC-SA 4.0";
        font-family: "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
        font-size: 8pt;
        color: #999;
        padding-top: 5pt;
        border-top: 1px solid #d4af37;
    }
}

body {
    font-family: "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #2c1810;
    background: #f4e8d0;
    max-width: 7.5in;
    margin: 0 auto;
}

/* Cover Page Styling */
.cover-page {
    page-break-after: always;
    text-align: center;
    padding-top: 3in;
}

.cover-title {
    font-size: 48pt;
    font-weight: 700;
    letter-spacing: 0.1em;
    color: #2c1810;
    margin-bottom: 0.5in;
    text-transform: uppercase;
}

.cover-subtitle {
    font-size: 24pt;
    font-weight: 400;
    letter-spacing: 0.05em;
    color: #8b0000;
    margin-bottom: 1.5in;
}

.cover-tagline {
    font-size: 14pt;
    font-style: italic;
    color: #666;
    margin-bottom: 0.25in;
}

.cover-version {
    font-size: 10pt;
    color: #999;
}

/* Typography */
h1 {
    font-size: 28pt;
    font-weight: 700;
    color: #2c1810;
    letter-spacing: 0.05em;
    margin-top: 24pt;
    margin-bottom: 12pt;
    padding-bottom: 6pt;
    border-bottom: 3px solid #d4af37;
    page-break-after: avoid;
}

h2 {
    font-size: 20pt;
    font-weight: 700;
    color: #4a3425;
    margin-top: 18pt;
    margin-bottom: 10pt;
    page-break-after: avoid;
}

h3 {
    font-size: 16pt;
    font-weight: 700;
    color: #5c3d2e;
    margin-top: 14pt;
    margin-bottom: 8pt;
    page-break-after: avoid;
}

h4 {
    font-size: 13pt;
    font-weight: 700;
    color: #8b7355;
    margin-top: 12pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
}

p {
    margin-bottom: 10pt;
    text-align: justify;
    orphans: 3;
    widows: 3;
}

/* Lists */
ul, ol {
    margin-bottom: 12pt;
    padding-left: 30pt;
}

li {
    margin-bottom: 4pt;
}

/* Code Blocks */
pre {
    background: #f9f6f0;
    border: 1px solid #d4af37;
    border-left: 4px solid #8b0000;
    padding: 12pt;
    margin: 12pt 0;
    font-family: "Courier New", monospace;
    font-size: 9pt;
    line-height: 1.4;
    overflow-x: auto;
    page-break-inside: avoid;
}

code {
    font-family: "Courier New", monospace;
    font-size: 10pt;
    background: #f9f6f0;
    padding: 2pt 4pt;
    border-radius: 2pt;
    color: #8b0000;
}

pre code {
    background: transparent;
    padding: 0;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 12pt 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

th {
    background: #2c1810;
    color: #f4e8d0;
    font-weight: 700;
    padding: 8pt;
    text-align: left;
    border: 1px solid #5c3d2e;
}

td {
    padding: 6pt 8pt;
    border: 1px solid #d4af37;
    background: #f9f6f0;
}

tr:nth-child(even) td {
    background: #f4e8d0;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #8b0000;
    padding-left: 16pt;
    margin: 12pt 0 12pt 20pt;
    font-style: italic;
    color: #5c3d2e;
    background: #f9f6f0;
    padding: 10pt 10pt 10pt 16pt;
}

/* Horizontal Rules */
hr {
    border: none;
    border-top: 2px solid #d4af37;
    margin: 20pt 0;
}

/* Links */
a {
    color: #8b0000;
    text-decoration: none;
    border-bottom: 1px dotted #8b0000;
}

a:hover {
    border-bottom-style: solid;
}

/* Strong/Bold */
strong, b {
    color: #2c1810;
    font-weight: 700;
}

/* Emphasis/Italic */
em, i {
    color: #4a3425;
    font-style: italic;
}

/* Page Breaks */
.page-break {
    page-break-after: always;
}

/* Special Boxes */
.warning-box, .note-box, .tip-box {
    padding: 12pt;
    margin: 12pt 0;
    border-left: 4px solid;
    page-break-inside: avoid;
}

.warning-box {
    background: #fff5f5;
    border-color: #8b0000;
}

.note-box {
    background: #f9f6f0;
    border-color: #d4af37;
}

.tip-box {
    background: #f5f9f5;
    border-color: #4a3425;
}
"""


def extract_title_from_markdown(md_content):
    """Extract the first H1 title from markdown content"""
    lines = md_content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line.replace('# ', '').strip()
    return "Penance Documentation"


def create_cover_page(title, subtitle="", tagline="", version=""):
    """Generate HTML for cover page"""
    return f"""
    <div class="cover-page">
        <div class="cover-title">PENANCE</div>
        <div class="cover-subtitle">{title}</div>
        {f'<div class="cover-tagline">{tagline}</div>' if tagline else ''}
        {f'<div class="cover-version">{version}</div>' if version else ''}
    </div>
    """


def markdown_to_pdf(md_file_path, output_pdf_path, add_cover=True, subtitle="", tagline="Absolution Through Steel"):
    """
    Convert a markdown file to a professionally styled PDF

    Args:
        md_file_path: Path to input markdown file
        output_pdf_path: Path to output PDF file
        add_cover: Whether to add a cover page
        subtitle: Subtitle for cover page
        tagline: Tagline for cover page
    """
    try:
        # Read markdown file
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()

        # Extract title
        title = extract_title_from_markdown(md_content)

        # Convert markdown to HTML
        md_processor = markdown.Markdown(extensions=[
            'extra',
            'codehilite',
            'tables',
            'toc',
            'sane_lists',
            'smarty'
        ])
        html_content = md_processor.convert(md_content)

        # Create full HTML document
        cover_html = create_cover_page(
            title=subtitle or title,
            tagline=tagline,
            version=f"Generated {Path(md_file_path).stem}"
        ) if add_cover else ""

        full_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>{title}</title>
        </head>
        <body>
            {cover_html}
            {html_content}
        </body>
        </html>
        """

        # Convert HTML to PDF
        HTML(string=full_html).write_pdf(
            output_pdf_path,
            stylesheets=[CSS(string=PDF_STYLE)]
        )

        print(f"✓ Generated: {output_pdf_path}")
        return True

    except Exception as e:
        print(f"✗ Error generating {output_pdf_path}: {str(e)}")
        return False


def batch_generate_pdfs(docs_dir, output_dir, file_list=None):
    """
    Generate PDFs for multiple markdown files

    Args:
        docs_dir: Root documentation directory
        output_dir: Output directory for PDFs
        file_list: List of relative paths to convert (None = all .md files)
    """
    docs_path = Path(docs_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Get list of markdown files
    if file_list:
        md_files = [docs_path / f for f in file_list]
    else:
        md_files = list(docs_path.rglob('*.md'))

    success_count = 0
    fail_count = 0

    for md_file in md_files:
        # Skip CLAUDE.md and README.md in root
        if md_file.name in ['CLAUDE.md', 'README.md'] and md_file.parent == docs_path.parent:
            continue

        # Generate output filename
        relative_path = md_file.relative_to(docs_path)
        pdf_name = str(relative_path).replace('/', '-').replace('.md', '.pdf')
        output_file = output_path / pdf_name

        # Convert to PDF
        if markdown_to_pdf(str(md_file), str(output_file)):
            success_count += 1
        else:
            fail_count += 1

    print(f"\n{'='*60}")
    print(f"PDF Generation Complete")
    print(f"Success: {success_count} | Failed: {fail_count}")
    print(f"Output directory: {output_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    # Priority documents for PDF generation
    PRIORITY_DOCS = [
        "reference/PLAYTEST-READY.md",
        "rules/quick-reference.md",
        "rules/turn-structure.md",
        "rules/combat-system.md",
        "rules/deck-construction.md",
        "rules/range-and-los.md",
        "rules/dice-reference.md",
        "rules/support-units.md",
        "reference/equipment-pool-complete.md",
        "campaigns/event-tables-kdm-style.md",
        "campaigns/anomalous-events-scp-style.md",
        "lore/world-overview.md",
        "lore/chronicle.md",
        "scenarios/01-proving-grounds.md",
        "scenarios/02-reliquary-ruins.md",
        "scenarios/03-escort-duty.md",
        "scenarios/04-king-of-the-hill.md",
        "scenarios/05-sabotage-mission.md",
        "scenarios/example-of-play.md",
        "factions/church/deck-equipment-system.md",
        "factions/dwarves/deck-equipment-system.md",
        "factions/ossuarium/deck-equipment-system.md",
        "factions/elves/deck-equipment-system.md",
        "factions/crucible/deck-equipment-system.md",
        "factions/nomads/deck-equipment-system.md",
        "factions/exchange/deck-equipment-system.md",
        "factions/emergent/deck-equipment-system.md",
        "factions/wyrd-conclave/deck-equipment-system.md",
        "factions/vestige-bloodlines/deck-equipment-system.md",
    ]

    # Get script directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    docs_dir = project_root / "docs"
    output_dir = project_root / "docs" / "pdfs"

    print("PENANCE PDF Generator")
    print("=" * 60)
    print(f"Docs directory: {docs_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Generating {len(PRIORITY_DOCS)} priority PDFs...\n")

    # Generate PDFs for priority documents
    batch_generate_pdfs(docs_dir, output_dir, PRIORITY_DOCS)
