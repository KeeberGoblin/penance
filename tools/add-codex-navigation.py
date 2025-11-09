#!/usr/bin/env python3
"""
Add standalone navigation bar to codex content pages.
Only shows when pages are accessed directly (not in iframe).
"""

import os
import re
from pathlib import Path

CODEX_DIR = Path('docs/codex')

# Navigation HTML to insert
NAV_HTML = '''    <!-- Navigation bar (only shows when page opened directly, not in iframe) -->
    <nav class="codex-nav" id="codexNav">
        <div class="codex-nav-content">
            <a href="index.html" class="nav-home">← Return to Codex</a>
            <span class="nav-separator">|</span>
            <a href="content-home.html">Home</a>
        </div>
    </nav>
    <script>
        // Show navigation only if page is NOT in an iframe
        if (window.self === window.top) {
            document.getElementById('codexNav').style.display = 'block';
        }
    </script>'''

# CSS styles to add to <style> block
NAV_CSS = '''        /* Navigation bar for direct page access (not in iframe) */
        .codex-nav {
            display: none;
            background: linear-gradient(135deg, #2b1f17 0%, #1a1410 100%);
            border-bottom: 2px solid var(--aged-gold);
            padding: 0.75rem 1.5rem;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 8px rgba(0,0,0,0.5);
        }
        .codex-nav-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            gap: 1.5rem;
            flex-wrap: wrap;
        }
        .codex-nav a {
            color: var(--aged-gold);
            text-decoration: none;
            font-family: 'Cinzel', serif;
            font-size: 0.9rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            transition: color 0.3s;
            white-space: nowrap;
        }
        .codex-nav a:hover {
            color: var(--parchment);
        }
        .codex-nav .nav-home {
            color: var(--dark-red);
            font-weight: 700;
        }
        .codex-nav .nav-separator {
            color: var(--medium-brown);
            margin: 0 0.25rem;
        }

'''

def has_codex_nav(content):
    """Check if file already has codex navigation."""
    return 'class="codex-nav"' in content or 'id="codexNav"' in content

def add_navigation_to_file(filepath):
    """Add navigation to a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has navigation
    if has_codex_nav(content):
        return False

    # Add CSS to style block
    # Find the </style> tag and insert before it
    style_pattern = r'(</style>)'
    if re.search(style_pattern, content):
        content = re.sub(style_pattern, NAV_CSS + r'\1', content, count=1)
    else:
        # If no style tag, add one in <head>
        head_pattern = r'(</head>)'
        if re.search(head_pattern, content):
            css_block = f'    <style>\n{NAV_CSS}    </style>\n'
            content = re.sub(head_pattern, css_block + r'\1', content, count=1)

    # Add navigation HTML after <body>
    body_pattern = r'(<body[^>]*>)'
    if re.search(body_pattern, content):
        content = re.sub(body_pattern, r'\1\n' + NAV_HTML, content, count=1)

    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    """Process all codex HTML files."""
    # Files to skip
    skip_files = {'index.html', 'content-home.html'}

    # Find all HTML files
    html_files = list(CODEX_DIR.glob('*.html'))

    updated_count = 0
    skipped_count = 0

    for filepath in sorted(html_files):
        if filepath.name in skip_files:
            continue

        try:
            if add_navigation_to_file(filepath):
                print(f"✅ Updated: {filepath.name}")
                updated_count += 1
            else:
                print(f"⏭️  Skipped: {filepath.name} (already has navigation)")
                skipped_count += 1
        except Exception as e:
            print(f"❌ Error processing {filepath.name}: {e}")

    print(f"\n📊 Summary:")
    print(f"   Updated: {updated_count} files")
    print(f"   Skipped: {skipped_count} files")
    print(f"   Total: {updated_count + skipped_count} files processed")

if __name__ == '__main__':
    main()
