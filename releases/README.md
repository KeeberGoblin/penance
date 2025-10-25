# PENANCE: Release Structure

## Overview

The Penance game is organized into **4 release tiers** designed for progressive complexity and strategic depth. This structure allows players to:

1. **Learn the core mechanics** with balanced, accessible factions
2. **Expand tactical options** with advanced factions
3. **Master complexity** with expert-level systems

---

## Release Tiers

### 🎯 Core Box (Required - Start Here)

**4 Factions:** Church, Dwarves, Ossuarium, Elves

**Coverage:**
- ✅ All playstyles (Aggressive / Defensive / Attrition / Mobility)
- ✅ Complete core rules (turn structure, combat, dice)
- ✅ Equipment system (60+ items)
- ✅ Support units (24 AI companions)
- ✅ Campaign system (pilot generation, settlement phase, bestiary)
- ✅ 5 scenarios (tutorial + 2 battles + walkthrough + overview)

**Complexity:** Low to Medium
**Playtime:** 45-60 minutes per battle
**Recommended:** Start here. Master these 4 factions before expansions.

📁 **Folder:** [`core-box/`](core-box/)

---

### 🎭 Expansion 1: Tricksters & Merchants

**2 Factions:** Wyrd Conclave (Fae), The Exchange

**New Mechanics:**
- Reality manipulation (illusions, stolen faces)
- Economic warfare (Credits, bribery, mercenaries)

**Complexity:** High
**Prerequisites:** 5+ games with Core Box
**Players:** Experienced players who want mind games and economy

📁 **Folder:** [`expansion-1-tricksters-merchants/`](expansion-1-tricksters-merchants/)

---

### 🔥 Expansion 2: Forged in Fire

**2 Factions:** Crucible Packs, Nomad Collective

**New Mechanics:**
- Honor duel system (1v1 combat buffs, Pack Tactics)
- Salvage economy (loot equipment from kills)
- New terrain (volcanic, desert)

**Complexity:** Medium
**Prerequisites:** 3+ games with Core Box
**Players:** Melee enthusiasts and scavenger tacticians

📁 **Folder:** [`expansion-2-forged-fire/`](expansion-2-forged-fire/)

---

### 🧬 Expansion 3: Evolution (Advanced)

**2 Factions:** Vestige Bloodlines, Emergent Syndicate

**New Mechanics:**
- Biomass mutation (5 bloodline variants)
- Hive mind coordination (swarm tactics)
- Extinction Clock (permanent death in campaign)
- Metamorph evolution paths

**Complexity:** Very High
**Prerequisites:** 10+ games with Core Box, mastery of all core mechanics
**Players:** Veterans seeking ultimate complexity and campaign stakes

📁 **Folder:** [`expansion-3-evolution/`](expansion-3-evolution/)

---

## Recommended Play Order

### Phase 1: Learn Core Mechanics (Week 1-2)
1. Read Core Box rules
2. Play Tutorial scenario (30 min)
3. Play 2-3 Arena battles with pre-built decks
4. Learn all 4 Core factions

### Phase 2: Master Core Factions (Week 3-4)
1. Build custom decks with equipment system
2. Try all faction matchups (4 × 3 = 12 combinations)
3. Add Support Units to battles
4. Start first campaign (settlement phase + missions)

### Phase 3: Expand Tactical Options (Month 2)
1. Add Expansion 1 (Wyrd + Exchange)
2. Learn economic/deception mechanics
3. Try mixed matchups (6 factions × 5 = 30 combinations)

### Phase 4: Add Melee & Salvage (Month 3)
1. Add Expansion 2 (Crucible + Nomads)
2. Learn honor duels and salvage
3. Try all 8 faction combinations (8 × 7 = 56 combinations)

### Phase 5: Ultimate Complexity (Month 4+)
1. Add Expansion 3 (Bloodlines + Emergent)
2. Learn 5 Bloodline variants
3. Master hive mind coordination
4. All 10 factions unlocked (10 × 9 = 90 combinations)

---

## Faction Complexity Rating

| Faction | Complexity | Learning Time | Skill Ceiling |
|---------|------------|---------------|---------------|
| **Core Box** | | | |
| Dwarven Forge-Guilds | ⭐ Low | 1 game | Medium |
| Church of Absolution | ⭐⭐ Medium | 2-3 games | High |
| The Ossuarium | ⭐⭐ Medium | 2-3 games | High |
| Elven Verdant Covenant | ⭐⭐⭐ Medium-High | 3-5 games | High |
| **Expansion 1** | | | |
| The Exchange | ⭐⭐⭐ High | 5+ games | High |
| Wyrd Conclave | ⭐⭐⭐⭐ Very High | 5+ games | Highest |
| **Expansion 2** | | | |
| Crucible Packs | ⭐⭐ Medium | 3-4 games | Medium |
| Nomad Collective | ⭐⭐⭐ Medium-High | 3-4 games | High |
| **Expansion 3** | | | |
| Vestige Bloodlines | ⭐⭐⭐⭐⭐ Very High | 10+ games | Highest |
| Emergent Syndicate | ⭐⭐⭐⭐ High | 8+ games | Very High |

---

## Balance Status (v5.29-FINAL)

### Core Box
- **Church:** 44-58% win rate (B tier) ✅ Balanced
- **Dwarves:** 50-55% win rate (B+ tier) ✅ Balanced
- **Ossuarium:** 48-52% win rate (B tier) ✅ Balanced
- **Elves:** 45-50% win rate (B tier) ✅ Balanced

### Expansions
- **Wyrd Conclave:** 45-55% (skill-dependent) ✅ Balanced
- **The Exchange:** 48-52% ✅ Balanced
- **Crucible Packs:** 50-55% (melee range), 35-40% (vs kiting) ⚠️ Matchup-dependent
- **Nomads:** 45-50% ✅ Balanced
- **Bloodlines:** 40-45% (beginner), 55-60% (expert) ⚠️ Skill-dependent
- **Emergent:** 45-50% ✅ Balanced

**Result:** 7/10 factions competitive (44-58% win rate range)

---

## File Organization

```
releases/
├── README.md                               (This file)
│
├── core-box/                               (Start here)
│   ├── rules/                              13 core rule files
│   ├── factions/                           4 faction files (Church, Dwarves, Ossuarium, Elves)
│   ├── scenarios/                          5 scenario files
│   ├── lore/                               5 lore files
│   ├── campaign/                           3 campaign files
│   └── README.md
│
├── expansion-1-tricksters-merchants/       (Requires Core Box)
│   ├── factions/                           2 faction files (Wyrd, Exchange)
│   └── README.md
│
├── expansion-2-forged-fire/                (Requires Core Box)
│   ├── factions/                           2 faction files (Crucible, Nomads)
│   └── README.md
│
└── expansion-3-evolution/                  (Requires Core Box, Recommend Exp 1+2)
    ├── factions/                           2 faction files (Bloodlines, Emergent)
    └── README.md
```

---

## What You Need to Play

### Core Box (Minimum)
- HTML files from `core-box/` folder
- 3 custom d6 dice per player (Attack, Defense, Suffering)
- 30-card starter deck per faction
- Hex map (6-10 hexes across)
- Component damage trackers
- SP/Heat/Energy tokens

### Expansions (Optional)
- Faction files from expansion folders
- Core Box rules (shared)
- Same dice and components

---

## Recommended Purchases (Physical Production)

### Starter Set (Core Box Only)
- **Contents:** 4 factions, core rules, 2 scenarios
- **Price Point:** $50-60 USD
- **Target Audience:** New players

### Deluxe Set (Core + Expansion 1)
- **Contents:** 6 factions, advanced mechanics
- **Price Point:** $80-90 USD
- **Target Audience:** Experienced tabletop gamers

### Ultimate Set (All 4 Releases)
- **Contents:** 10 factions, all mechanics
- **Price Point:** $120-140 USD
- **Target Audience:** Collectors, campaign players

### Expansion Packs (Sold Separately)
- **Expansion 1:** $20-25 USD (2 factions)
- **Expansion 2:** $20-25 USD (2 factions)
- **Expansion 3:** $25-30 USD (2 complex factions + campaign rules)

---

## Digital vs Physical

### Digital Release (Current)
- ✅ Free HTML files (open in browser)
- ✅ Printable PDFs
- ✅ Interactive deck builder
- ✅ Pilot generator tool
- ❌ Requires printing cards
- ❌ Requires custom dice (can use standard d6 with lookup table)

### Physical Release (Future)
- ✅ Pre-printed cards
- ✅ Custom dice included
- ✅ Rulebooks (professionally formatted)
- ✅ Tokens/trackers included
- ❌ Costs money
- ❌ Requires manufacturing

---

## FAQ

### Q: Do I need all expansions?
**A:** No. Core Box is a complete game. Expansions add variety and complexity.

### Q: Can I skip Expansion 1 and go straight to Expansion 2?
**A:** Yes, but Expansion 3 requires deep understanding of core mechanics (recommend playing Core + Exp 1 + Exp 2 first).

### Q: Which expansion should I buy first?
**A:**
- **Expansion 1** if you want mind games and economy (high complexity)
- **Expansion 2** if you want melee duels and salvage (medium complexity)
- **Expansion 3** only if you've mastered Core Box (very high complexity)

### Q: Are expansions balanced against Core Box factions?
**A:** Yes. All 10 factions are balanced through v5.29-FINAL (7/10 competitive, 3/10 matchup-dependent).

### Q: Can I play Bloodlines without the Extinction Clock?
**A:** Yes. Extinction Clock is optional (campaign-only). You can play Bloodlines in Arena mode without permanent death.

---

## Support

- **GitHub:** https://github.com/KeeberGoblin/penance
- **Issues:** Report bugs, balance feedback
- **Discussions:** Community strategy, house rules
- **Wiki:** Comprehensive tactics guides (coming soon)

---

## License

PENANCE is released under MIT License.
- ✅ Free to print, modify, share
- ✅ Commercial use allowed
- ❌ No warranty (play at your own risk)

---

**"Choose your steel. Choose your sins. Choose your penance."**

— Welcome to the Bound
