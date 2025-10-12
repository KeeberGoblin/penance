# GitHub Pages Setup Guide
## Hosting Your Interactive HTML as a Live Website

---

## ✅ SETUP COMPLETE!

Your interactive HTML compendium has been set up for GitHub Pages!

**What was done:**
- ✅ Created `/docs` folder
- ✅ Copied your fancy interactive HTML as `docs/index.html`
- ✅ Committed to git

---

## Final Step: Enable GitHub Pages (2 minutes)

**Go to GitHub and enable Pages:**

1. Visit: `https://github.com/KeeberGoblin/penance`
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar, under "Code and automation")
4. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select `main` and `/docs` folder ⚠️ **(Important: choose /docs, not root!)**
   - Click **Save**

5. Wait 1-2 minutes for GitHub to build your site

**Your site will be live at:**
```
https://keebrgoblin.github.io/penance/
```

That's it! Your interactive compendium with timeline animations, card tiles, and faction visualizations will be live.

---

## Option 2: Create a Simpler URL Structure

If you want a cleaner URL like `https://keebrgoblin.github.io/penance/`, you can:

### Method A: Move HTML to Root

1. Copy the HTML file to the root of your repo:
   ```bash
   cp tools/card-generator/index-v2.html index.html
   ```

2. Commit and push:
   ```bash
   git add index.html
   git commit -m "Add interactive compendium to root for GitHub Pages"
   git push origin main
   ```

3. Your site will now be at: `https://keebrgoblin.github.io/penance/`

### Method B: Use a `docs/` Folder

1. Create a docs folder with your HTML:
   ```bash
   mkdir -p docs
   cp tools/card-generator/index-v2.html docs/index.html
   ```

2. In GitHub Settings > Pages, change **Branch** folder to `/docs`

3. Commit and push:
   ```bash
   git add docs/
   git commit -m "Add interactive compendium to docs folder"
   git push origin main
   ```

4. Site will be at: `https://keebrgoblin.github.io/penance/`

---

## Option 3: Use Both Versions

Create an index page that lets users choose:

**Create `index.html` in root:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Penance: Absolution Through Steel</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0a0a0a;
            color: #e0e0e0;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            padding: 2rem;
        }
        .container {
            text-align: center;
            max-width: 800px;
        }
        h1 {
            font-size: 3rem;
            color: #d4af37;
            margin-bottom: 1rem;
        }
        .tagline {
            font-style: italic;
            margin-bottom: 3rem;
            color: #999;
        }
        .button-group {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }
        a {
            display: block;
            background: linear-gradient(135deg, #8b0000, #1a1a1a);
            color: #d4af37;
            padding: 2rem;
            text-decoration: none;
            border: 2px solid #444;
            border-radius: 12px;
            transition: all 0.3s;
        }
        a:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(212, 175, 55, 0.3);
            border-color: #d4af37;
        }
        a h2 {
            margin: 0 0 0.5rem 0;
            font-size: 1.5rem;
        }
        a p {
            margin: 0;
            color: #999;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚔ PENANCE ⚔</h1>
        <p class="tagline">"In iron we seek forgiveness. Through blood, absolution."</p>

        <div class="button-group">
            <a href="tools/card-generator/index-v2.html">
                <h2>✨ Interactive Compendium (NEW)</h2>
                <p>Fancy timeline, card tiles, faction web, animations</p>
            </a>

            <a href="tools/card-generator/index.html">
                <h2>📖 Classic Reference</h2>
                <p>Original tabbed interface, printable cards</p>
            </a>

            <a href="https://github.com/KeeberGoblin/penance">
                <h2>🔧 View on GitHub</h2>
                <p>Source code, design docs, development</p>
            </a>
        </div>
    </div>
</body>
</html>
```

Then commit and push:
```bash
git add index.html
git commit -m "Add landing page for GitHub Pages"
git push origin main
```

---

## Troubleshooting

### "404 - Page Not Found"
- Wait 2-3 minutes after enabling GitHub Pages
- Check that your branch is `main` (not `master`)
- Verify the file path is correct

### "Site isn't updating"
- GitHub Pages can take 1-5 minutes to rebuild
- Try clearing your browser cache (Ctrl+F5)
- Check the Actions tab on GitHub to see build status

### "Styles/animations not working"
- Make sure all CSS is inline or in the same HTML file
- GitHub Pages serves static files - JavaScript should work fine
- Check browser console for errors (F12)

---

## Current Repository Structure

```
penance/
├── index.html                          # (NEW) Landing page or main site
├── tools/
│   └── card-generator/
│       ├── index.html                  # Original interactive reference
│       └── index-v2.html               # New fancy compendium
├── docs/                               # All your markdown documentation
│   ├── world-lore.md
│   ├── iconic-npcs.md
│   ├── settlement-mechanics.md
│   ├── resonance-engine-mechanics.md
│   ├── faction-relationships.md
│   ├── chronicle-entries.md
│   ├── pilot-scars-traits.md
│   ├── loot-tables.md
│   └── (20+ other docs)
└── README.md
```

---

## Recommended Approach

**For best results, I recommend:**

1. **Use Method B (docs folder)** - This keeps your repo organized
2. **Copy the new fancy version** (`index-v2.html`) as your main site
3. **Keep the old version** as a backup/alternative

**Commands:**
```bash
# Create docs folder
mkdir -p docs

# Copy new fancy version to docs
cp tools/card-generator/index-v2.html docs/index.html

# Commit
git add docs/
git commit -m "🎨 Add interactive compendium to GitHub Pages

- Fancy timeline with scroll animations
- Tile-based card gallery with modals
- Faction relationship network visualization
- Iconic NPCs showcase
- Settlement building guide
- Modern UI with smooth animations"

# Push
git push origin main
```

Then go to GitHub Settings > Pages > Branch > Select `/docs` folder.

---

## Alternative: Use GitHub Pages with Custom Domain

If you have a custom domain (e.g., `penance-game.com`):

1. Add a `CNAME` file to your root/docs folder:
   ```
   penance-game.com
   ```

2. Configure your domain DNS:
   - Add an `A` record pointing to GitHub's IPs
   - Or add a `CNAME` record pointing to `keebrgoblin.github.io`

3. Enable "Enforce HTTPS" in GitHub Pages settings

---

## Next Steps

Once your site is live, you can:
- Share the URL on social media
- Add it to your README.md
- Submit to board game directories
- Get playtest feedback via the live site

**Your live site will be:**
```
https://keebrgoblin.github.io/penance/
```

---

*Need help? Check GitHub Pages documentation: https://docs.github.com/en/pages*
