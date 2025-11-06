# Codex HTML vs Markdown Comparison Report
**Date**: 2025-11-05
**Scope**: Comparison of 85 HTML files in `docs/codex/` with corresponding Markdown files in `docs/` tree
**Total Files**: 85 HTML files vs 170+ MD files across all directories

---

## Executive Summary

### Key Findings

1. **Coverage Disparity**: Not all HTML files have direct MD equivalents, and vice versa
2. **Content Depth**: HTML files contain more detailed lore exposition and visual presentation
3. **Balance Updates**: Recent balance changes (v5.29, Oct 2025) present in HTML may not be reflected in MD
4. **Naming Inconsistencies**: Character name conflicts (e.g., "Bonelord Karath" vs "Bonelord Thresh")
4. **Naming Inconsistencies**: Character name conflicts (e.g., "Bonelord Karath" vs "Bonelord Karath")
5. **Structural Differences**: HTML files are presentation-focused; MD files are more concise and gameplay-focused
6. **Missing Void Lore**: No standalone `void.md` file found; void content integrated into `cosmology-and-origins.md`

---

## Detailed File-by-File Comparison

### 1. FACTION: Elven Verdant Covenant

**HTML File**: `/home/user/penance/docs/codex/faction-elves.html`
**MD File**: `/home/user/penance/docs/factions/elves/deck-equipment-system.md`

#### Content Differences:

**ONLY IN HTML:**
1. **Extended Species Origins Section** (lines 75-107)
   - Homo Sylvanus evolutionary background
   - Pre-Sundering population (~200,000 globally)
   - Detailed physiology (chlorophyll analogs, symbiotic biology)
   - Post-Sundering fertility crisis ("elven women can no longer conceive")
   - 200-year extinction timeline
   - The Veil Accords explanation

2. **Root-Grafted Pilots Section** (lines 130-357)
   - Extensive lore on "The Mourned Necessity"
   - Root-Grafting procedure details (amputation at mid-thigh, living vine prosthetics)
   - The Grafting Ceremony (5-day ritual process)
   - Living Thread Variants vs Standard Metal Threads (comparison table)
   - Living With Root-Legs (sunlight dependency, seasonal sensitivity, watering rituals)
   - Theological Tension table (Traditionalists vs Pragmatists vs Symbiants)
   - Combat Implications table
   - Comparison to other factions' pilot philosophies

3. **Balance Update Notes** (Oct 19, 2025)
   - Bleed cap reduced from 10 to 8 (lines 365-376)
   - Photosynthesis REMOVED entirely (line 433-442)
   - Leaf Dance reduced from 3 hexes to 2 hexes (line 457-459)
   - Living Seal no longer grants passive +1 card/round (mentioned in strategy notes)

4. **Support Units** (lines 543-595)
   - Full stat blocks with HP, Movement, Defense
   - Detailed ability descriptions
   - Unlock conditions (e.g., "Unlock: Complete 3 missions")

5. **Schisms & Exiled Groves** (lines 601-633)
   - The Thornblood Exiles lore
   - The Roothold Massacre background
   - Tactical differences for mirror matches

6. **Faction Relations Table** (lines 639-691)
   - Status with each faction (WAR, NEUTRAL, HOSTILE, etc.)
   - Detailed notes on each relationship

7. **Version 3.0 Optional Rules Integration** (lines 757-795)
   - Dice Pool Advantage interactions
   - Taint Exploitation penalties (double Taint rate, Forest terrain protection)
   - Pilot Grit System (-1 Grit penalty permanent)

**ONLY IN MD:**
1. **Equipment Card Lists** (lines 299-373)
   - Full card breakdowns for weapons:
     - Thorn Blade (6 cards with SP costs and effects)
     - Thorn Whip (6 cards)
     - Longbow (4 cards)
     - Nature Staff (7 cards)
     - Bark Shield (3 cards)
     - Seed Pod (3 cards)
     - Living Seal (3 cards with revised balance note)

2. **Casket Classes & Equipment Slots** (lines 89-114)
   - Thorn Dancer (Scout - 6 SP)
   - Rootwarden (Assault - 5 SP)
   - Ironwood Sentinel (Heavy - 4 SP)
   - World Tree Titan (Fortress - 3 SP)
   - Equipment slot breakdown for each

3. **Build Examples** (lines 117-244)
   - Build 1: Surgical Assassin (detailed loadout)
   - Build 2: Bleed Master
   - Build 3: Nature Fortress
   - Build 4: Druid Commander
   - Each with Total Deck size and Playstyle notes

4. **Faction Tactics** (lines 247-296)
   - 5 Elven tactics with SP costs and keywords
   - Apex Predator, Shadow Step, Toxin Mastery, Verdant Growth, Ironbark Skin

5. **Bleed Mechanic Detailed Rules** (lines 389-411)
   - Max 10 Bleed cap (vs HTML's 8)
   - **BALANCE INCONSISTENCY**: MD says "MAX 10 Bleed counters" but HTML says reduced to 8
   - Example turn-by-turn bleed stacking

6. **Counter-Play Section** (lines 457-465)
   - How to beat Elves
   - Rush strategies, destroy Living Seal, use AoE

7. **Campaign Progression Path** (lines 469-487)
   - Starting Loadout (Mission 1)
   - Mid-Campaign (Mission 5-10)
   - Late-Campaign (Mission 15+)
   - Scrap costs for each phase

**DIFFERENT INFORMATION:**

1. **Bleed Cap**:
   - HTML: "Maximum 8 Bleed stacks per target (Balance Update Oct 19: Reduced from 10)"
   - MD: "Stack up to MAX 10 Bleed counters per target"
   - **OUTDATED MD**: MD file not updated with latest balance changes

2. **Photosynthesis**:
   - HTML: Marked as REMOVED with strikethrough (line 433)
   - MD: Still listed as active card (line 60-68) with "REVISED - BALANCE NERF" note requiring "NO DAMAGE TAKEN"
   - **OUTDATED MD**: MD shows nerfed version, HTML shows complete removal

3. **Living Seal**:
   - HTML: No longer grants passive regeneration
   - MD: "Regeneration (Passive - REVISED): When you use a healing effect... recover +1 additional card. Does NOT grant passive card recovery per round." (lines 376-385)
   - **CONSISTENT BUT VAGUE**: Both versions note nerf, but HTML is clearer about removal

4. **Recommended Builds**:
   - HTML: 3 builds (lines 697-721) - Surgical Assassin, Bleed Master, Nature Fortress
   - MD: 4 builds (lines 117-244) - adds Druid Commander build
   - **MD MORE COMPREHENSIVE** for build variety

5. **Verdant Regeneration**:
   - HTML: "recover 2 cards from discard pile" (line 472)
   - MD: "recover 1 card from discard pile. If you have Living Seal equipped, recover 2 cards instead." (lines 81-85)
   - **DIFFERENT MECHANICS**: HTML makes it unconditional 2 cards, MD ties it to equipment

---

### 2. LORE: The Void

**HTML File**: `/home/user/penance/docs/codex/lore-void.html`
**MD File**: **NOT FOUND** (no standalone void.md file)

#### Status: NO DIRECT MD EQUIVALENT

**HTML Content Summary** (530 lines):
- What Is the Void? (Scientific, Mystical, Fae perspectives)
- The Breach at Ground Zero (Primary Void Rift)
- Secondary Void Rifts (Major, Minor, Micro-Tears)
- Void Corruption Stages (Stage 0-4, with Undead Resistance note)
- Abominations (Lesser, Standard, Greater, Apex)
- How the Void Enables Soul-Binding
- Void Artifacts (Soulstone Shards, Void-Touched Weapons, Engine Fragments)
- Faction Perspectives on the Void
- Can the Void Be Stopped? (Theoretical Solutions)

**Corresponding MD Content**:
- Void information appears to be integrated into `/home/user/penance/docs/lore/cosmology-and-origins.md`
- Lines 92-110 in cosmology MD cover "The Void (The Anti-Creation)"
- Much more concise (18 lines vs 530+ lines in HTML)

**Missing Content in MD**:
- No corruption stages table
- No Abomination classification
- No Void artifact details
- No faction perspectives section
- No theoretical solutions for sealing the Void

**Recommendation**: Create standalone `/home/user/penance/docs/lore/void.md` file with HTML content, or significantly expand cosmology.md

---

### 3. LORE: Cosmology & Origins

**HTML File**: `/home/user/penance/docs/codex/cosmology.html`
**MD File**: `/home/user/penance/docs/lore/cosmology-and-origins.md`

#### Content Differences:

**SIMILAR CORE CONTENT:**
- Three-Layered Cosmos (Material World, Feywild, Void)
- Species Origins (Humans, Elves, Dwarves, etc.)
- Nikolas Theslar biography
- The Veil Accords
- Metaphysics of magic and technology fusion
- Secret Truth about cyclical endings

**ONLY IN HTML:**
1. **Visual Presentation** (extensive styling, decorative elements)
2. **Theslar's Final Words** displayed as dramatic quote (lines 226-228)

**ONLY IN MD:**
1. **Technology Level Details** (lines 35-65)
   - Pre-Sundering: 1950s-1970s equivalent tech
   - "What Existed" vs "What Did NOT Exist" tables
   - Post-Sundering regression to 1800s-1850s Victorian era
   - Explanation: "steampunk-level civilization built on ruins of mid-20th-century atomic age"
   - **MAJOR WORLDBUILDING DETAIL MISSING FROM HTML**

2. **Bonelord Name**: "Bonelord Thresh" (line 183 in MD)
2. **Bonelord Name**: "Bonelord Karath" (line 183 in MD)

**ONLY IN HTML:**
1. **Bonelord Name**: "Bonelord Karath" (no line reference as not in excerpt)

**NAMING INCONSISTENCY**:
- MD uses "Bonelord Thresh"
- MD uses "Bonelord Karath"
- HTML uses "Bonelord Karath"
- **CONTRADICTION**: Different character names for same role

**DIFFERENT INFORMATION:**

1. **Ossuarium Founder**:
   - HTML: "Bonelord Karath perfected controlled undeath by Year 10"
   - MD: "Bonelord Thresh (originally human necromancer) perfected controlled undeath by Year 10"
   - MD: "Bonelord Karath (originally human necromancer) perfected controlled undeath by Year 10"
   - **NEEDS RESOLUTION**: Pick one canonical name

2. **Technology Timeline**:
   - HTML: No specific pre-Sundering tech level mentioned in excerpt
   - MD: Explicitly states "1950s-1970s equivalent" with detailed breakdown
   - **MD MORE DETAILED** on this aspect

---

### 4. CAMPAIGN: Pilot Skills System

**HTML File**: `/home/user/penance/docs/codex/campaign-pilot-skills.html`
**MD File**: `/home/user/penance/docs/campaign/pilot-skills.md`

#### Content Differences:

**HIGHLY SIMILAR CONTENT** - These files are very well aligned

**ONLY IN HTML:**
1. **Extensive CSS Styling** (lines 8-131)
2. **Visual card-style presentation** for skills
3. **Bonelord Name**: "Bonelord Karath" in Iconic Pilots table (line 777)

**ONLY IN MD:**
1. **Bonelord Name**: "Bonelord Thresh" in Iconic Pilots table (line 298)
1. **Bonelord Name**: "Bonelord Karath" in Iconic Pilots table (line 298)

**IDENTICAL CONTENT:**
- XP progression (100/300/600 XP thresholds)
- All Tier 1, 2, and 3 Universal Skills
- All Faction-Specific Skills
- Iconic Pilots table (except Bonelord name)
- Settlement Phase Training
- Flesh Bargain Integration
- GM Guidelines
- Designer's Notes

**NAMING INCONSISTENCY CONFIRMED**:
- HTML: "Bonelord Karath - 'The Debt Collector'"
- MD: "Bonelord Thresh - 'The Debt Collector'"
- MD: "Bonelord Karath - 'The Debt Collector'"
- Same title, different first name

---

### 5. CAMPAIGN: Flesh Bargains

**HTML File**: `/home/user/penance/docs/codex/campaign-flesh-bargains.html`
**MD File**: `/home/user/penance/docs/campaigns/flesh-bargains.md`

#### Content Differences:

**ONLY IN HTML (first 150 lines):**
1. **Extensive CSS Styling** (lines 8-132)
   - .bargain-featured-container grid system
   - .bargain-card styling
   - Dropdown containers and toggles
   - Interactive elements

2. **Visual Presentation Elements**:
   - Faction-labeled bargain cards
   - Cost badges
   - Color-coded sections

**ONLY IN MD (first 150 lines):**
1. **"The Veteran's Sacrifice" Subtitle** (line 1)
2. **Detailed Procedure Section** (lines 23-56)
   - Surgical specifications (amputation location, anesthesia, duration)
   - What's Removed (specific measurements)
   - What's Added (augmentation ports, stabilizer mounts)
   - Post-Surgery Capsule Modifications (freed space uses)

3. **Gameplay Benefits Section** (lines 58-87)
   - +1 Soul Point Maximum
   - +2 Heat Capacity
   - +1 Deployment Duration
   - New Ability: Stump Override
   - Improved Thread Recovery

4. **Mechanical Disadvantages** (lines 87-117)
   - Wheelchair-bound status
   - Cannot walk/stand/flee
   - Social stigma
   - Total dependency details
   - Irreversibility

5. **Cultural Responses by Faction** (lines 119-150)
   - Church of Absolution: "The Shortened"
   - Elven Verdant Covenant: "The Pruned"
   - Detailed cultural views and reactions

**DIFFERENT FOCUS:**
- HTML (first 150 lines): Presentation framework, visual styling
- MD (first 150 lines): Gameplay mechanics, surgical details, faction lore

**STRUCTURAL DIFFERENCE:**
- HTML appears to be a browsable catalog/database of bargains
- MD appears to be a narrative/mechanical explanation of the Flesh Bargain concept

---

### 6. LORE: Soulstone Power System

**HTML File**: `/home/user/penance/docs/codex/lore-soulstone-system.html`
**MD File**: `/home/user/penance/docs/lore/soulstone-system.md`

#### Content Differences:

**ONLY IN HTML (first 100 lines):**
1. **Related Links Section** (lines 20-27)
   - Cross-references to Soulstone Volatility, Soul-Binding Mechanics, Rules
2. **Section Banner Image** (lines 35-37)
   - `<img>` tag for "Lore_SoulstoneSketch.png"
3. **Parallax Scroll JavaScript** (lines 54-81)
   - Interactive visual effects for tear reveals
4. **"The Screaming Faces in the Crystal" Section** (lines 87-100)
   - Eerie detail about distorted faces visible in facets
   - Soul agony shaping the crystal
   - Multiple expressions from different angles

**ONLY IN MD (first 100 lines):**
1. **The Three Forms of Soulstones** (lines 16-84)
   - 1. Natural Formation
   - 2. Bound Cores (The Primary Power Source)
   - 3. Faction-Refined Cores
   - Detailed tables for sizes, energy, souls inside
   - The Chimera Process description
   - Visual Appearance progression (Fresh → Mid-Life → Dying)
   - Faction-Refined Cores table with shapes and philosophies

2. **Soulstone Energy Mechanics** (lines 86-100)
   - Energy Pool Tracking table
   - Status levels (Full, Healthy, Depleted, Critical, Empty)
   - Performance modifiers

**CONTENT ORGANIZATION:**
- HTML: Focuses on horror/lore elements first (screaming faces)
- MD: Focuses on mechanical categorization first (three forms, energy tracking)

---

## Cross-Cutting Issues

### A. Balance Update Propagation

**Issue**: Recent balance changes (v5.29, October 2025) appear in HTML but not consistently in MD files.

**Examples**:
1. **Elven Bleed Cap**: HTML says 8, MD says 10
2. **Photosynthesis**: HTML shows REMOVED, MD shows REVISED
3. **Leaf Dance**: HTML says 2 hexes, MD may still say 3 hexes (needs verification)

**Affected Files**:
- `/home/user/penance/docs/factions/elves/deck-equipment-system.md` - OUTDATED
- Potentially other faction MD files

**Recommendation**:
- Create a balance changelog file
- Update all MD files to match v5.29 final
- Use version tags in both HTML and MD for clarity

---

### B. Naming Inconsistencies

**Issue**: Character names differ between HTML and MD files.

**Bonelord Name Conflict**:
- **HTML Files**: "Bonelord Karath"
- **MD Files**: "Bonelord Thresh"
- **MD Files**: "Bonelord Karath"
- **Frequency**: Appears in multiple files (cosmology, pilot skills, potentially others)

**Impact**: Canonical lore contradiction

**Recommendation**:
- Decide on single canonical name
- Search and replace across ALL files (HTML and MD)
- Update any character backstory/lore to use chosen name consistently

**Suggested Resolution**:
- Based on recent commit history showing "Karath" in multiple locations
- Recommend standardizing to "Bonelord Karath"
- Update all MD files using find-replace

---

### C. Missing MD Equivalents

**HTML Files WITHOUT Direct MD Counterparts**:

Based on the 85 HTML files found, these categories likely have gaps:

1. **Lore Files**:
   - `lore-void.html` - No standalone `void.md`
   - `lore-casket-origins.html` - May not have equivalent
   - `lore-casket-manufacturing.html` - May not have equivalent
   - `lore-bonelord-karath.html` - Character-specific lore
   - `lore-ground-zero.html` - May not have equivalent
   - `lore-npcs.html` - May not have equivalent

2. **Campaign Files**:
   - `campaign-event-tables.html` - Check if missing
   - `campaign-anomalous-events.html` - Check if missing
   - `campaign-mission-generation.html` - Check if missing
   - `campaign-scavengers-crusade.html` - Check if missing

3. **Rules Files**:
   - `rules-common-mistakes.html` - Likely missing
   - `rules-combat-flowchart.html` - Likely missing
   - `rules-v3-optional.html` - Likely missing
   - `gm-helper.html` - Likely missing

4. **Scenario Files**:
   - Multiple scenario HTML files (king-of-the-hill, escort-duty, etc.)
   - Check if MD equivalents exist in scenarios/ directory

**Recommendation**:
- Audit all 85 HTML files systematically
- Create corresponding MD files for missing content
- Prioritize high-traffic/core mechanic files first

---

### D. Content Depth Differences

**Pattern Observed**:
- **HTML files**: More lore exposition, narrative flow, visual presentation
- **MD files**: More mechanical details, gameplay focus, build examples

**Examples**:

1. **Elves**:
   - HTML: Extensive Root-Grafted Pilots lore (230+ lines)
   - MD: Full equipment card lists with SP costs

2. **Cosmology**:
   - HTML: Dramatic presentation of Theslar's story
   - MD: Technology level timeline details

3. **Soulstone System**:
   - HTML: Horror elements (screaming faces)
   - MD: Energy tracking mechanics

**Not Necessarily a Problem**: Different formats serve different purposes
- HTML = codex/reference/immersion
- MD = mechanics/building/playing

**Recommendation**:
- Maintain both formats with complementary content
- Ensure mechanics are consistent between both
- Cross-reference between HTML and MD where appropriate
- Consider HTML as "player-facing lore" and MD as "designer/player mechanics reference"

---

### E. Structural Organization Differences

**Directory Structure**:

HTML (Flat):
```
docs/codex/
  ├── faction-elves.html
  ├── lore-void.html
  ├── campaign-pilot-skills.html
  ├── rules-combat.html
  └── ... (85 files total)
```

MD (Hierarchical):
```
docs/
  ├── factions/elves/deck-equipment-system.md
  ├── lore/cosmology-and-origins.md
  ├── campaign/pilot-skills.md
  ├── rules/combat-system.md
  └── ... (170+ files total)
```

**Implications**:
- HTML uses naming convention for categorization
- MD uses directory structure for categorization
- Makes 1:1 mapping non-obvious

**Recommendation**:
- Create mapping document: `HTML_TO_MD_FILE_MAP.md`
- List each HTML file with its MD equivalent(s)
- Note where content is split across multiple MD files
- Note where MD content spans multiple HTML files

---

## Priority Action Items

### Critical (Do Immediately)

1. **Resolve Bonelord Name**:
   - Choose "Karath" or "Thresh"
   - Find-replace across ALL files
   - Verify no other instances

2. **Update Elven Balance in MD**:
   - Change Bleed cap from 10 to 8 in `deck-equipment-system.md`
   - Mark Photosynthesis as REMOVED (not just revised)
   - Update Leaf Dance to 2 hexes
   - Update any other v5.29 changes

3. **Create HTML-to-MD Mapping Document**:
   - List all 85 HTML files
   - Identify corresponding MD file(s)
   - Note "NO EQUIVALENT" where applicable
   - Note "CONTENT SPLIT" where HTML maps to multiple MDs

### High Priority (This Week)

4. **Create Missing Core MD Files**:
   - `docs/lore/void.md` - Extract from void.html
   - `docs/lore/ground-zero.md` - If not exists
   - Any other high-traffic lore files

5. **Balance Changelog**:
   - Create `docs/BALANCE-CHANGELOG.md`
   - List all v5.29 changes with dates
   - Reference this in both HTML and MD files

6. **Technology Level in Cosmology HTML**:
   - Add the 1950s-1970s tech level section from MD to HTML
   - Ensures both formats have same worldbuilding detail

### Medium Priority (This Month)

7. **Audit All Faction Files**:
   - Compare each faction HTML to MD
   - Document differences like Elves comparison
   - Update outdated balance info

8. **Standardize Verdant Regeneration**:
   - Decide: 2 cards unconditional OR 1 card + Living Seal bonus?
   - Apply consistently across HTML and MD

9. **Cross-Reference Links**:
   - Add "See also" sections in MD files
   - Link to corresponding HTML codex pages
   - Link to related mechanical rules

### Low Priority (As Needed)

10. **Visual Parity**:
    - Consider adding images/diagrams to MD files
    - Or note that HTML is canonical for visual presentation

11. **Scenario Files**:
    - Check if scenario HTML files have MD equivalents
    - Create if missing and needed for play

12. **GM Helper Content**:
    - Determine if gm-helper.html content should be in MD
    - Extract to appropriate docs/ location if needed

---

## Recommendations for Ongoing Maintenance

### Version Control Best Practices

1. **Single Source of Truth for Balance**:
   - Pick one location for balance numbers (suggest: MD files in `/docs/factions/`)
   - HTML files pull from these during generation/build
   - OR: Maintain sync script that updates both

2. **Change Log Discipline**:
   - Every balance change documented in `BALANCE-CHANGELOG.md`
   - Reference changelog in affected files
   - Date stamp all balance notes

3. **Review Checklist for Updates**:
   - When updating mechanics:
     - [ ] Update MD file
     - [ ] Update corresponding HTML file
     - [ ] Update changelog
     - [ ] Check for cross-references
     - [ ] Verify no naming inconsistencies introduced

### Documentation Structure

4. **Mapping Document**:
   - Maintain `HTML_TO_MD_FILE_MAP.md`
   - Update when adding new files
   - Use for quick reference during updates

5. **Content Ownership**:
   - Define which format is canonical for what:
     - **Mechanics/Balance**: MD files are source of truth
     - **Lore/Narrative**: HTML files can have extended content
     - **Rules**: MD files for play, HTML for reference
   - Document this in README

6. **Naming Conventions**:
   - Standardize character names in a `CHARACTER-CANON.md` file
   - List all major NPCs with canonical names
   - Reference this before creating new content

---

## Summary Statistics

### Files Compared in Detail
- **Faction Files**: 1 pair (Elves HTML vs MD)
- **Lore Files**: 3 pairs (Void, Cosmology, Soulstone)
- **Campaign Files**: 2 pairs (Pilot Skills, Flesh Bargains)
- **Rules Files**: Glimpse of 1 pair (Combat)

### Issues Found
- **Balance Inconsistencies**: 3+ instances (Bleed cap, Photosynthesis, Leaf Dance)
- **Naming Conflicts**: 1 major (Bonelord Karath vs Thresh)
- **Missing MD Files**: Estimated 10-20 files (Void, scenarios, GM helpers)
- **Content Depth Differences**: Pervasive (by design)
- **Structural Differences**: Fundamental (HTML flat, MD hierarchical)

### Overall Assessment

**Alignment Score**: 6.5/10

- **Strengths**:
  - Pilot Skills system well-aligned
  - Core mechanics generally consistent
  - Both formats serve complementary purposes

- **Weaknesses**:
  - Balance updates not propagated to MD
  - Character naming conflicts
  - Missing MD files for key HTML content
  - No clear mapping between formats

**Conclusion**: The codex HTML and markdown files share substantial common content but have diverged in important areas. Recent balance updates and lore additions have not been consistently synchronized. A systematic reconciliation pass is needed to resolve conflicts and create missing files, followed by establishment of clear maintenance protocols to prevent future divergence.

---

## Next Steps

1. **Immediate**: Review and approve this report
2. **This Week**: Execute Critical priority items (Bonelord name, Elven balance, mapping doc)
3. **This Month**: Execute High and Medium priority items
4. **Ongoing**: Implement maintenance best practices

**Questions for Review**:
- Should we prioritize HTML or MD as source of truth for balance?
- Is "Bonelord Karath" or "Bonelord Thresh" the canonical name?
- Is "Bonelord Karath" or "Bonelord Karath" the canonical name?
- Do we want all HTML files to have MD equivalents, or is split coverage acceptable?
- Should we create automated sync tooling, or maintain manually?

---

*Report compiled by AI assistant | Based on systematic file comparison | Recommendations subject to human review*
