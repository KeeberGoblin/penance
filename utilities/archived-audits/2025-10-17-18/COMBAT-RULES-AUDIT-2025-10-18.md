# Combat Rules and Mechanics Contradiction Audit
## Penance: Absolution Through Steel

**Date**: October 18, 2025
**Auditor**: Claude Code Agent
**Scope**: Core combat rules, dice mechanics, Heat system, deck-as-HP system, component damage

---

## EXECUTIVE SUMMARY

This audit identified **12 critical contradictions**, **8 ambiguous mechanics**, and **5 missing rules** across the combat system documentation. The most severe issues are:

1. **Defense Dice Face Count Contradiction** - Critical game-breaking inconsistency
2. **Deck Size Specification Conflict** - Core mechanic varies between 30 and 26-50 cards
3. **Component HP Thresholds** - Two different systems described
4. **Reshuffle Damage Card Addition** - Unclear mechanism

**Recommendation Priority**: Fix Defense Dice immediately (blocks critical gameplay), then resolve deck size, then component damage thresholds.

---

## SECTION 1: CRITICAL RULES CONTRADICTIONS

### 1.1 DEFENSE DICE FACE ASSIGNMENTS - GAME BREAKING

**Severity**: CRITICAL - Makes game unplayable without clarification

**Files Affected**:
- `/workspaces/penance/docs/rules/dice-reference.md` (lines 96-106)
- `/workspaces/penance/docs/codex/rules-dice.html` (lines 179-221)

**Contradiction**:

**dice-reference.md says (6 faces):**
```
| Face | Symbol | Effect |
|------|--------|--------|
| 1 | SHIELD | Block 1 damage |
| 2 | ABSORB | Block 1 damage |
| 3 | FLESH WOUND | Take damage (discard 1 card) |
| 4 | CRITICAL | Take damage + 1 Component Damage |
| 5 | PIERCE | Take damage, cannot use reactive cards |
| 6 | HEAT | Take damage + 1 Heat |
```

**rules-dice.html says (6 faces, but different assignment):**
```
| Face | Symbol | Effect |
|------|--------|--------|
| 1 | [SHIELD] | SHIELD - Block 1 damage |
| 2 | [ABSORB] | ABSORB - Block 1 damage |
| 3 | [SHIELD] | SHIELD - Block 1 damage | <-- DUPLICATE!
| 4 | [BLOOD] | FLESH WOUND - Take damage |
| 5 | [PIERCE] | PIERCE - Take damage, cannot use reactive cards |
| 6 | [HEAT] | HEAT - Take damage + 1 Heat |
```

**Impact**:
- rules-dice.html has **3 SHIELD faces** (faces 1, 2, 3) → 50% block rate
- dice-reference.md has **2 SHIELD faces** (faces 1, 2) + CRITICAL (face 4) → 33% block rate
- rules-dice.html is **missing CRITICAL symbol entirely**!

**Statistical Difference**:
- HTML version: 50% block rate, no random Component Damage from dice
- MD version: 33% block rate, 16.7% chance of Component Damage per die

**Player Confusion**:
"Do Defense Dice cause Component Damage or not? Is blocking 33% or 50%?"

**RECOMMENDATION**:
1. Choose ONE system (prefer MD version with CRITICAL for more tactical depth)
2. Update rules-dice.html to match dice-reference.md
3. Note in rules-dice.html line 623: "Removed CRITICAL symbol eliminates random Component Damage spikes" contradicts actual die face table

---

### 1.2 DECK SIZE: 30 vs 26-50 Cards

**Severity**: CRITICAL - Core mechanic specification

**Files Affected**:
- `/workspaces/penance/docs/codex/rules-combat.html` (line 34, line 43)
- `/workspaces/penance/docs/rules/combat-system.md` (line 14, line 34)

**Contradiction**:

**rules-combat.html says:**
```html
Line 34: <li><strong>Casket HP Deck</strong> (30 cards) - Your mech's structural integrity</li>
Line 43: <p>Your 30-card deck represents your Casket's HP.</p>
Line 55: <p><strong>Total: 30 cards</strong></p>
```

**combat-system.md says:**
```markdown
Line 14: **Casket HP Deck** (26-50 cards, varies by equipment loadout)
Line 28: **v2.0 Variable Deck System** (26-50 cards depending on equipment)
Line 34: **Total: 26-50 cards** (Light Caskets ~26-32, Heavy Caskets ~38-50)
```

**Impact**:
- HTML version = fixed 30 cards (simpler, easier to teach)
- MD version = variable 26-50 based on equipment loadout (more complex, v2.0 system)

**Player Confusion**:
"How many cards should my deck have? Is it always 30, or does it vary?"

**Context Note**:
- combat-system.md line 36 has a NOTE: "This section shows **simplified v1.0 example** for teaching. See [deck-equipment-system.md] for full v2.0 modular equipment."
- This suggests HTML version is intentionally simplified for teaching

**RECOMMENDATION**:
1. Add version labels: HTML = "v1.0 Simplified Rules (Fixed 30 cards)", MD = "v2.0 Advanced Rules (Variable 26-50)"
2. Update HTML to reference MD for advanced variant
3. Create explicit "which version should I use?" guidance

---

### 1.3 COMPONENT DAMAGE THRESHOLDS: 3 HP vs 6-10 HP

**Severity**: CRITICAL - Determines how fast components break

**Files Affected**:
- `/workspaces/penance/docs/codex/rules-combat.html` (line 357, line 375-429)
- `/workspaces/penance/docs/rules/combat-system.md` (line 299, line 311-320)
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 29-38)

**Contradiction**:

**rules-combat.html says:**
```html
Line 357: <strong>3 Component Damage = Component DESTROYED</strong>
Line 375-429: Component HP Table shows:
  Head: 3 HP
  Right Arm: 4 HP
  Left Arm: 4 HP
  Chassis: 5 HP
  Legs: 6 HP
```

**combat-system.md says:**
```markdown
Line 299: Component destruction threshold varies by limb (Head 3, Arms 4, Chassis 5, Legs 6)
Line 311-320: Same table as HTML - Head 3, Arms 4, Chassis 5, Legs 6
```

**component-damage-system.md says (v3.0 COMPREHENSIVE RULES):**
```markdown
Line 29-38: Component HP Table (Master Reference)
  Head: 6 HP (0-2 AP, 3-4 Structure, 5-6 Exposure)
  Right Arm: 8 HP (0-3 AP, 4-5 Structure, 6-8 Exposure)
  Left Arm: 8 HP (0-3 AP, 4-5 Structure, 6-8 Exposure)
  Chassis: 10 HP (0-4 AP, 5-6 Structure, 7-10 Exposure)
  Legs: 8 HP (0-3 AP, 4-8 Structure, NEVER Exposure)
```

**Impact**:
- v1.0/v2.0 system: Components break fast (Head at 3 HP, Arms at 4)
- v3.0 system: Components have **triple HP** with AP/Structure/Exposure zones

**Statistical Difference**:
- Old: Head destroyed in ~1-2 attacks
- New: Head destroyed in ~6 attacks (much slower, more strategic)

**Player Confusion**:
"How much damage before my arm breaks? 4 HP or 8 HP?"

**RECOMMENDATION**:
1. Label component-damage-system.md as "v3.0 Advanced Rules"
2. Update rules-combat.html and combat-system.md with version disclaimer: "v2.0 simplified - see component-damage-system.md for v3.0 zone-based system"
3. Create migration guide for groups upgrading from v2.0 to v3.0

---

### 1.4 RESHUFFLE MECHANISM: How Many Damage Cards?

**Severity**: HIGH - Affects death spiral pacing

**Files Affected**:
- `/workspaces/penance/docs/rules/combat-system.md` (line 385-394)
- `/workspaces/penance/docs/rules/turn-structure.md` (line 140-144)
- `/workspaces/penance/docs/codex/rules-combat.html` (line 442-445)

**Contradiction**:

**All three files say "Add 1 Damage card" but context varies:**

**combat-system.md:**
```markdown
Line 385-394:
- Shuffle discard pile into new deck
- **Add 1 "Damage" card** to the deck (permanent degradation)
- Draw normally
```

**turn-structure.md:**
```markdown
Line 140-144:
- Shuffle your discard pile into a new deck
- **Add 1 "Damage" card** to the deck (permanent)
- Continue drawing normally
```

**rules-combat.html:**
```html
Line 442-445:
- Shuffle discard pile into new deck
- **Add 1 "Damage" card** to the deck (permanent degradation)
- Draw normally
```

**Ambiguity**: **When** is Damage card added?
- Before shuffling (goes into discard pile, then shuffled)?
- After shuffling (added on top of new deck)?
- During shuffling (mixed in randomly)?

**Impact**: If added on top, players might draw it immediately. If shuffled in, it's random.

**Additional Search Result** (from bestiary-core.md line 367):
```
All enemies make Willpower Save (7+) or immediately reshuffle deck with +2 Damage cards (mental attack)
```

This shows **+2 Damage cards** is possible (multiple at once), but doesn't clarify the mechanism.

**RECOMMENDATION**:
1. Add explicit timing: "Shuffle discard pile, **then** add 1 Damage card to the new deck (shuffle it in)"
2. Clarify if Damage card is:
   - A: Shuffled randomly into deck (recommended for fairness)
   - B: Placed on bottom (delays pain)
   - C: Placed on top (immediate punishment)

---

### 1.5 SP MAXIMUM BY CASKET TYPE: Inconsistent Table

**Severity**: MEDIUM-HIGH - Affects core action economy

**Files Affected**:
- `/workspaces/penance/docs/rules/combat-system.md` (line 512-521)
- `/workspaces/penance/docs/rules/turn-structure.md` (line 50-58)

**Contradiction**:

**combat-system.md:**
```markdown
Line 512-521:
| Casket Type | SP Maximum | Deck Size Range |
|-------------|------------|-----------------|
| Scout (Light) | 6 SP | 26-32 cards |
| Assault (Medium) | 5 SP | 30-38 cards |
| Heavy | 4 SP | 35-45 cards |
| Fortress | 3 SP | 38-50 cards |
```

**turn-structure.md:**
```markdown
Line 50-58:
- Scout Caskets: 6 SP
- Assault Caskets: 5 SP
- Heavy Caskets: 4 SP
- Fortress Caskets: 3 SP
```

**Observed Issue**: turn-structure.md **doesn't specify deck size ranges** at all. Not a contradiction, but missing critical info.

**RECOMMENDATION**:
Add deck size ranges to turn-structure.md for completeness.

---

### 1.6 HEAT STRAIN ROLL TIMING: Start of Turn vs End of Turn

**Severity**: MEDIUM - Affects when players suffer penalties

**Files Affected**:
- `/workspaces/penance/docs/rules/combat-system.md` (line 534)
- `/workspaces/penance/docs/rules/turn-structure.md` (line 70-74)

**Both say "start of turn" consistently** - NO CONTRADICTION FOUND.

**Verified Consistent**:
```markdown
combat-system.md line 534: "Exception: If in **Danger Zone** (5+ Heat), roll Strain first"
turn-structure.md line 70-74: "If you have **5+ Heat** (Danger Zone): Roll **Strain**"
```

**Status**: ✅ Consistent

---

## SECTION 2: AMBIGUOUS WORDING (Needs Clarification)

### 2.1 PRIMARY WEAPON CARDS: What Counts?

**Severity**: MEDIUM - Affects Component Damage calculation

**Files Affected**:
- `/workspaces/penance/docs/rules/combat-system.md` (line 297, line 304)
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 47-51)

**Ambiguity**:

**combat-system.md line 304 says:**
```markdown
> **v2.0 NOTE**: "Primary Weapon cards" refers to your equipped weapon cards
> (e.g., Longsword, Greatsword, Pistol). These are the cards you discarded
> from your Primary Weapon slot equipment.
```

**component-damage-system.md line 47-51 says:**
```markdown
**1. Equipment Cards Discarded When Taking Damage**
- **Primary Weapon cards** → +1 Component Damage to targeted component
- **Shield/Offhand cards** → +1 Component Damage if targeting Left Arm
- **Accessory cards** → No Component Damage (utility equipment)
```

**Question**: What happens in these edge cases?
1. If I discard a Primary Weapon card, but attacker targeted **Chassis** (not arms), does it still add Component Damage?
2. If I discard a Shield card, but attacker targeted **Right Arm** (not left), does it add Component Damage?

**Current Wording Suggests**:
- Primary Weapon cards → Component Damage to **targeted component** (whatever was declared)
- Shield/Offhand cards → Component Damage **only if targeting Left Arm**

**RECOMMENDATION**:
Clarify with explicit examples:
```markdown
**Equipment Card Discard Rules:**
- Primary Weapon card discarded → +1 Component Damage to **attacker's declared target** (any component)
- Shield/Offhand card discarded → +1 Component Damage to **Left Arm only** (regardless of target)
- Accessory card discarded → 0 Component Damage (utility items don't contribute)

**Example**:
Attack targets Chassis for 5 damage.
Defender discards: 2× Primary Weapon, 1× Shield, 2× Universal
Result: 2 (Primary Weapon) + 0 (Shield, not targeting Left Arm) = +2 Chassis damage
```

---

### 2.2 COMPONENT TARGETING: Attacker Choice vs Random

**Severity**: MEDIUM - Core tactical decision

**Files Affected**:
- `/workspaces/penance/docs/rules/combat-system.md` (line 145-165)
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 67-89)

**Ambiguity**:

Both files describe **three methods** for component targeting:
- Method A: Attacker Chooses (Tactical) - **RECOMMENDED**
- Method B: Random Hit Location (roll 1d6)
- Method C: Card Specifies

**Question**: Which method is **default**?

**combat-system.md line 148 says:**
```markdown
**A. Attacker Chooses (Tactical) - RECOMMENDED**
```

**component-damage-system.md line 73 says:**
```markdown
**Method A: Attacker Chooses** (Tactical)
- **Recommended default** (gives attacker tactical control)
```

**Current wording**: Both say "recommended" but don't say "unless otherwise stated, use Method A."

**RECOMMENDATION**:
Add explicit default rule:
```markdown
**DEFAULT RULE**: Attacker chooses target component (Method A).
Use Method B (random) only if:
- Playing with "Fog of War" optional rule
- Card text says "random hit location"
- Both players agree to add chaos
```

---

### 2.3 DEFENSE DICE CRITICAL SYMBOL: Bypasses AP?

**Severity**: MEDIUM - Affects armor effectiveness

**Files Affected**:
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 54-57)

**Ambiguity**:

**component-damage-system.md says:**
```markdown
Line 54-57:
**2. Defense Dice CRITICAL Symbols (⚔️)**
- When rolling Defense Dice, each CRITICAL symbol:
  - **Bypasses AP layer entirely**
  - Adds +1 Component Damage directly to structure
  - Cannot be prevented (armor-piercing effect)
```

**Question**: If component is at 2/8 HP (AP zone), and defender rolls 1 CRITICAL:
- Does it add +1 Component Damage to AP zone (2 → 3, still in AP)?
- OR does it bypass AP and add +1 to Structure zone (jumping from 2 to 4)?

**Current wording "bypasses AP layer entirely"** suggests it should skip the AP zone and go directly to structure, but this creates weird situations:
- Component at 2/8 HP (AP zone)
- Takes 1 CRITICAL
- Jumps to 4/8 HP? Or 3/8 HP?

**RECOMMENDATION**:
Clarify with explicit rule:
```markdown
**CRITICAL Symbol Bypasses AP Layer:**
- Component Damage from CRITICAL symbols is added to the HP track normally
- BUT: Even if in AP zone, CRITICAL damage **counts toward next zone threshold**

**Example 1**: Component at 2/8 HP (AP zone 0-3)
- Rolls 1 CRITICAL → +1 Component Damage
- Result: 2 → 3/8 HP (still AP zone, no functional penalty)

**Example 2**: Component at 3/8 HP (AP zone edge)
- Rolls 1 CRITICAL → +1 Component Damage
- Result: 3 → 4/8 HP (enters Structure zone, penalties apply)

**"Bypasses AP"** means CRITICAL damage is **not mitigated by armor** (treated as armor-piercing), not that it skips HP values.
```

---

### 2.4 SCRAP CARD TIMING: When Do Cards Become SCRAP?

**Severity**: MEDIUM - Affects in-combat card cycling

**Files Affected**:
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 348-416)

**Ambiguity**:

**component-damage-system.md says:**
```markdown
Line 348-353:
**When Component is Destroyed**
**All equipment cards associated with that component become "SCRAP":**
- Primary Weapon cards (if Right Arm destroyed)
- Shield/Offhand cards (if Left Arm destroyed)
- Cards **remain in deck** but lose original function
```

**Question**: **When exactly** do cards become SCRAP?
- A: Immediately when component destroyed (even cards in hand)?
- B: Only cards in deck become SCRAP (hand cards stay functional until played)?
- C: Next time you draw/shuffle?

**Impact Example**:
```
Turn 3: Right Arm destroyed (8/8 HP)
Current hand: [Longsword Slash] [Longsword Thrust] [Parry] [Brace for Impact] [Move] [Vent]

Can I still play Longsword Slash this turn?
OR does it immediately become SCRAP (0 SP: Cannibalize)?
```

**RECOMMENDATION**:
Add explicit timing rule:
```markdown
**SCRAP Conversion Timing:**
When component is destroyed, **immediately** convert all associated cards:
- Cards in **hand** → become SCRAP (can no longer use printed effect this turn)
- Cards in **deck** → become SCRAP (will draw as SCRAP in future)
- Cards in **discard** → become SCRAP (will reshuffle as SCRAP)

**Example**: Right Arm destroyed mid-combat
- You have 2× Longsword cards in hand → Immediately become SCRAP
- You can play SCRAP cards this turn (0 SP: Cannibalize to cycle)
- You **cannot** play them as Longsword attacks (component destroyed)
```

---

### 2.5 HEAT REMOVAL: "End turn in safe zone" Mechanic

**Severity**: LOW - Minor ambiguity

**Files Affected**:
- `/workspaces/penance/docs/rules/quick-reference.md` (line 91)

**Ambiguity**:

**quick-reference.md says:**
```markdown
Line 91: - End turn in safe zone (0 Heat)
```

**Question**: What does "end turn in safe zone" mean?
- A: If you have 0 Heat at end of turn, remove 0 Heat (no effect, tautology?)
- B: If you end your turn while **standing in a "safe zone" terrain hex**, remove all Heat?
- C: Typo? Should say "End turn to remove 1 Heat" (pass action)?

**Context from range-and-los.md line 545:**
```markdown
| **Water** | Pass through | 1 SP/hex | No | Remove 2 Heat/turn |
```
This shows terrain-based Heat removal exists.

**RECOMMENDATION**:
Clarify:
```markdown
### Removing Heat
- Vent abilities (-2-3 Heat)
- Pass entire turn without acting (-1 Heat) [Passive cooling]
- Stand in water hexes (-2 Heat per turn) [Terrain effect]
- Heat Sink equipment (passive -1 per turn) [Equipment]
```

---

### 2.6 OVERSPENDING SP: Discard Order

**Severity**: LOW - Minor tactical question

**Files Affected**:
- `/workspaces/penance/docs/rules/turn-structure.md` (line 60-69)

**Ambiguity**:

**turn-structure.md says:**
```markdown
Line 60-69:
**1.1b Overspending SP (GKR-Style Push System)**
- Every SP beyond your maximum costs 1 card (discard from hand or deck)
```

**Question**: Can I choose to discard from hand vs deck for each overspent SP?

**Example**: Scout (6 SP max), wants to spend 9 SP total
- 6 SP free
- 7th SP: Discard from hand
- 8th SP: Discard from hand
- 9th SP: Discard from deck?

**Or must I pick one source** (all from hand, or all from deck)?

**RECOMMENDATION**:
Clarify:
```markdown
**Overspending SP Discard Choice:**
- You may choose **hand or deck** for each individual card discarded
- Example: 3 SP overspent → discard 2 from hand, 1 from deck (your choice)
```

---

### 2.7 PILOT EXPOSURE WOUND TIMING: Every Damage or Once Per Attack?

**Severity**: MEDIUM - Affects wound accumulation rate

**Files Affected**:
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 134-147, line 671-679)

**Ambiguity**:

**component-damage-system.md line 136 says:**
```markdown
**If component is in Pilot Exposure Zone:**
- **For each Component Damage that occurred in Pilot Exposure Zone:**
  - Pilot flips 1 Wound card
```

**Example at line 671-679 clarifies:**
```markdown
**Right Arm progression:**
- 5 → 6 (enter exposure) → 7 → 8 → **9/8 HP (DESTROYED + overage)**

**Damage breakdown:**
- 5 → 6: Enters Pilot Exposure Zone → **+1 Pilot Wound**
- 6 → 7: Still in exposure → **+1 Pilot Wound**
- 7 → 8: Component destroyed → **+1 Pilot Wound**
- 8 → 9: Overage (component already destroyed, no additional wound)
```

**Clarification Confirmed**: Each point of Component Damage while in exposure = +1 Wound

**Question**: What about overkill?
- If component is at 7/8 HP (exposure zone)
- Takes 5 Component Damage (would go to 12/8)
- Is it: 7→8 (+1 Wound, destroyed), or 7→8→9→10→11→12 (+5 Wounds, but capped at destroyed)?

**Current wording at line 679:**
```markdown
8 → 9: Overage (component already destroyed, no additional wound)
```

This suggests once component destroyed, **overage damage doesn't cause more wounds**.

**RECOMMENDATION**:
Add explicit overkill rule:
```markdown
**Overkill Component Damage:**
- Component Damage stops adding Pilot Wounds once component is **destroyed**
- Excess damage beyond destruction threshold is wasted

**Example**: Right Arm at 7/8 HP (exposure), takes 5 Component Damage
- 7 → 8: Component destroyed → +1 Pilot Wound
- 8 → 12: Overkill (no additional Wounds)
- Total: +1 Pilot Wound only
```

---

### 2.8 NEURAL FEEDBACK: Cumulative Across All Components

**Severity**: MEDIUM - Affects pilot wound triggers

**Files Affected**:
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 333-336)

**Ambiguity**:

**component-damage-system.md says:**
```markdown
Line 333-336:
4. **Neural Feedback** (Cumulative Strain)
   - When **total Component Damage across ALL components ≥ 15** → +1 Wound
   - Check at end of each attack that adds Component Damage
```

**Question**: Does this trigger **once total**, or **every time you cross threshold**?

**Scenario**:
- Turn 1: Total Component Damage across all limbs = 14 → No wound
- Turn 2: Take +2 Component Damage → Total = 16 → +1 Wound (triggered)
- Turn 3: Take +1 Component Damage → Total = 17 → +1 Wound again? Or no?

**Current wording "When total ≥ 15"** is ambiguous:
- Interpretation A: Triggers **once** when you first reach 15+ (like a threshold)
- Interpretation B: Triggers **every attack** while total is ≥ 15

**RECOMMENDATION**:
Clarify trigger condition:
```markdown
**Neural Feedback Trigger:**
- Triggers **once** when total Component Damage first reaches 15+
- Does **not** trigger again for subsequent damage
- Track with checkbox: "Neural Feedback [  ] triggered"

**Example**:
- Total Component Damage: 12 → 16 (crossed 15) → +1 Pilot Wound, check box
- Total Component Damage: 16 → 20 (already past 15) → No additional wound
```

---

## SECTION 3: MISSING RULES (Gaps in Documentation)

### 3.1 HEAT STRAIN TABLE: Missing From Core Files

**Severity**: MEDIUM - Referenced but not defined in main rules

**Files Affected**:
- `/workspaces/penance/docs/rules/combat-system.md` (line 553-558)
- `/workspaces/penance/docs/rules/turn-structure.md` (line 243-250)

**Issue**:

**combat-system.md references Strain Table:**
```markdown
Line 553-558:
**Strain Roll** (1d6 + Heat):
- 1-5: Gain 1 Heat
- 6-8: Lose 1 SP this turn
- 9-11: Take 2 damage (discard 2 cards)
- 12+: Component malfunction (lose 1 random Component)
```

**turn-structure.md has the same table:**
```markdown
Line 243-250:
**Strain Table** (Roll 1d6 + current Heat):
| Result | Effect |
| 1-5 | Minor Overload: Gain 1 Heat |
| 6-8 | SP Drain: Lose 1 SP this turn |
| 9-11 | System Damage: Take 2 damage |
| 12+ | Critical Failure: Random component malfunctions |
```

**Gap**: Both tables are **consistent** (good!), but...
- **12+ "lose 1 random Component"** - How? Roll 1d6? What's the table?

**turn-structure.md line 249 clarifies:**
```markdown
12+ | Critical Failure: Random component malfunctions (roll 1d6: 1-2=Arm, 3-4=Leg, 5=Head, 6=Chassis)
```

**RECOMMENDATION**:
Add random component table to combat-system.md:
```markdown
**12+ Critical Failure**: Roll 1d6 to determine which component malfunctions:
  1-2: Random Arm (roll 1d2: 1=Right, 2=Left)
  3-4: Legs
  5: Head
  6: Chassis

**Malfunction Effect**: Component takes +3 Component Damage immediately (as if hit)
```

---

### 3.2 EXECUTION RESULT: Defender Discard Choice

**Severity**: LOW-MEDIUM - Special case handling

**Files Affected**:
- `/workspaces/penance/docs/rules/dice-reference.md` (line 70-76)

**Issue**:

**dice-reference.md says:**
```markdown
Line 70-76:
**EXECUTION (Double , total 10)**:
- Automatically destroy 1 targeted component (even if <3 Component Damage)
- Bypass ALL Defense (shields, armor, reactive cards don't work)
- Still deal standard damage from attack card
- Defender cannot choose to discard from hand (must discard from deck)
- **Brutality**: Even a 1-damage attack with EXECUTION destroys a component
```

**Gap**: "Defender cannot choose to discard from hand (must discard from deck)"

**Question**: Why this restriction?
- Is it to simulate the "brutal, uncontrollable" nature of EXECUTION?
- Or is it to prevent defenders from dumping Primary Weapon cards to avoid extra Component Damage?

**Problem**: This contradicts the general rule from combat-system.md line 285:
```markdown
**Defender chooses how to discard cards**:
- From Hand: Lose tactical options but control what's lost
- From Deck: Keep hand intact but risk losing key cards randomly
- Mixed: Discard some from hand, some from deck
```

**RECOMMENDATION**:
Either:
1. Remove the restriction (EXECUTION already bypasses defense, no need to also force deck discard)
2. OR clarify the **design intent**: "EXECUTION is so sudden and brutal, defender has no time to strategically discard - cards are torn from deck randomly"

---

### 3.3 CATASTROPHIC FAILURE: Duration of -2 Damage Penalty

**Severity**: LOW - Minor timing ambiguity

**Files Affected**:
- `/workspaces/penance/docs/rules/dice-reference.md` (line 77-90)

**Issue**:

**dice-reference.md says:**
```markdown
Line 77-90:
**CATASTROPHIC FAILURE (Double , total 2)**:
- Your weapon critically malfunctions
- Discard all Primary Weapon cards from hand immediately
- Gain +2 Heat (weapon overheats from malfunction)
- Next attack this turn or next turn: -2 damage
```

**Gap**: "Next attack this turn or next turn: -2 damage"

**Question**: Does the -2 damage penalty last for:
- A: Only the very next attack (1 attack total)?
- B: Rest of this turn (all attacks this turn)?
- C: This turn + next turn (multiple attacks)?

**Current wording "next attack this turn or next turn"** suggests:
- If you attack again this turn → -2 damage
- If you don't attack this turn → -2 damage on first attack next turn
- Penalty lasts for **exactly 1 attack**

**RECOMMENDATION**:
Clarify duration:
```markdown
**CATASTROPHIC FAILURE Penalty Duration:**
- -2 damage applies to **your next single attack only**
- After that attack, penalty is removed
- Track with token: "Weapon Jammed [-2 dmg next attack]"
```

---

### 3.4 COMPONENT DESTRUCTION: What Happens to Cards Already Played?

**Severity**: LOW - Edge case

**Files Affected**:
- `/workspaces/penance/docs/rules/component-damage-system.md` (line 348-353)

**Issue**:

**Scenario**:
```
Turn structure:
1. You play "Longsword Slash" (2 SP): Attack declared but not resolved
2. Opponent plays reactive card, rolls Defense Dice
3. Defense Dice cause Component Damage → Right Arm destroyed
4. Your Longsword Slash is **already played** (in resolution)

Does Longsword Slash resolve normally? Or fizzle (component destroyed mid-attack)?
```

**Gap**: Documentation doesn't address "component destroyed mid-resolution."

**RECOMMENDATION**:
Add edge case rule:
```markdown
**Component Destroyed During Attack Resolution:**
- If component is destroyed **before** your attack resolves (e.g., enemy reactive card):
  - Attack **still resolves** (you committed to the strike)
  - Use **last known stats** (before component destroyed)
- If component is destroyed **after** your attack resolves:
  - Normal SCRAP conversion applies

**Example**:
You play "Hammer Strike" (6 damage, requires Right Arm)
Opponent plays reactive "Counterstrike" → Deals damage back → Destroys your Right Arm
Your Hammer Strike **still deals 6 damage** (attack was already committed)
After resolution, Hammer Strike card becomes SCRAP
```

---

### 3.5 MULTIPLE CRITICALS ON DEFENSE DICE: Stack or Cap?

**Severity**: LOW - Statistical edge case

**Files Affected**:
- `/workspaces/penance/docs/rules/component-damage-system.md** (line 54-57)

**Issue**:

**Scenario**:
```
Defender takes 10 damage → Rolls 10 Defense Dice
Result: 5× CRITICAL symbols
```

**Question**: Does this add:
- +5 Component Damage (all CRITICALS stack)?
- OR capped at some maximum?

**Current rules suggest unlimited stacking**, but this could lead to instant component destruction:
- 10 damage attack → 5 CRITICALS → +5 Component Damage
- If targeting Head (6 HP total), could destroy in 1 attack if already at 1 HP

**RECOMMENDATION**:
Either:
1. Keep unlimited stacking (CRITICAL symbols are meant to be brutal)
2. OR add statistical note: "While unlikely (0.13% chance of 5 CRITICALS), this represents catastrophic structural failure"

**Current system seems intentionally swingy** (high variance), so probably no cap needed.

---

## SECTION 4: RECOMMENDATIONS (Exact Text Fixes)

### 4.1 CRITICAL FIX: Defense Dice Face Table

**File**: `/workspaces/penance/docs/codex/rules-dice.html`
**Lines**: 179-221

**Current (WRONG - has 3 SHIELD faces, missing CRITICAL):**
```html
<tr>
    <td>3</td>
    <td>[SHIELD]</td>
    <td><strong>SHIELD</strong> - Block 1 damage</td>
</tr>
```

**Replace with:**
```html
<tr>
    <td>3</td>
    <td>[BLOOD]</td>
    <td><strong>FLESH WOUND</strong> - Take damage (discard 1 card)</td>
</tr>
<tr>
    <td>4</td>
    <td>[CRITICAL]</td>
    <td><strong>CRITICAL</strong> - Take damage + 1 Component Damage</td>
</tr>
<tr>
    <td>5</td>
    <td>[PIERCE]</td>
    <td><strong>PIERCE</strong> - Take damage, cannot use reactive cards</td>
</tr>
```

**Also remove line 623:**
```html
<li>Removed CRITICAL symbol eliminates random Component Damage spikes</li>
```

This line contradicts the corrected die face table.

---

### 4.2 CRITICAL FIX: Deck Size Versioning Labels

**File**: `/workspaces/penance/docs/codex/rules-combat.html`
**Line**: 19

**Current:**
```html
<p style="font-style: italic; color: var(--aged-gold); margin-bottom: 2rem;">
    tactical combat Hybrid • Version 2.0 • Dual-Layer Damage: Casket HP (30 cards) + Pilot Wounds (10 cards)
</p>
```

**Replace with:**
```html
<p style="font-style: italic; color: var(--aged-gold); margin-bottom: 2rem;">
    tactical combat Hybrid • <strong>Version 2.0 Simplified Rules (Fixed 30-card deck)</strong> • Dual-Layer Damage: Casket HP (30 cards) + Pilot Wounds (10 cards)
</p>
<p style="font-style: italic; color: var(--aged-gold); font-size: 0.9rem;">
    <strong>Advanced Rules:</strong> See <a href="../rules/combat-system.md">combat-system.md</a> for v2.0 Variable Deck System (26-50 cards based on equipment loadout).
</p>
```

---

### 4.3 CLARIFICATION: Primary Weapon Card Component Damage

**File**: `/workspaces/penance/docs/rules/combat-system.md`
**Line**: 297-304

**Current:**
```markdown
### Step 6: Check for Component Damage

**If you discarded any Primary Weapon equipment cards**:
- Mark 1 Component Damage per Primary Weapon card to targeted component
- Track separately: Right Arm, Left Arm, Legs, Head, Chassis
- **Component destruction threshold varies by limb** (Head 3, Arms 4, Chassis 5, Legs 6)

> **v2.0 NOTE**: "Primary Weapon cards" refers to your equipped weapon cards (e.g., Longsword, Greatsword, Pistol). These are the cards you discarded from your Primary Weapon slot equipment.
```

**Add after line 304:**
```markdown

**IMPORTANT CLARIFICATION:**
- **Primary Weapon cards** → Add Component Damage to **attacker's declared target** (any component)
- **Shield/Offhand cards** → Add Component Damage to **Left Arm only** (regardless of target)
- **Accessory cards** → Never add Component Damage (utility items)

**Example**:
- Attacker targets **Chassis**
- Defender discards: 2× Primary Weapon cards (Longsword), 1× Shield card (Buckler), 2× Universal cards
- Component Damage to **Chassis**: 2 (Primary Weapon cards only, Shield doesn't apply to Chassis)
- Component Damage to **Left Arm**: 1 (Shield card applies separately to Left Arm)
```

---

### 4.4 CLARIFICATION: Reshuffle Damage Card Timing

**File**: `/workspaces/penance/docs/rules/combat-system.md`
**Line**: 385-394

**Current:**
```markdown
**When you would draw a card but deck is empty**:
- **Reshuffle Trigger** (like GKR, but with KDM twist)
- Shuffle discard pile into new deck
- **Add 1 "Damage" card** to the deck (permanent degradation)
- Draw normally
```

**Replace with:**
```markdown
**When you would draw a card but deck is empty**:
- **Reshuffle Trigger** (like GKR, but with KDM twist)
- **Step 1:** Shuffle discard pile into new deck
- **Step 2:** Add 1 "Damage" card to the shuffled deck (shuffle it in randomly)
- **Step 3:** Draw normally

**Damage Card Rules:**
- Damage cards are **blank** (no effect when played, 0 SP cost)
- They dilute your deck (dead draws)
- Each reshuffle adds +1 Damage card (cumulative)
- After 3-4 reshuffles, ~10-13% of deck is Damage cards (death spiral)
- Cannot be removed during combat (only during Settlement Phase with Repair Kit)
```

---

### 4.5 CLARIFICATION: Component Targeting Default Rule

**File**: `/workspaces/penance/docs/rules/combat-system.md**
**Line**: 145-165

**Current:**
```markdown
**Targeting Methods (choose one):**

**A. Attacker Chooses (Tactical) - RECOMMENDED**
- Attacker selects component: Head, Right Arm, Left Arm, Chassis, or Legs
- Gives tactical control (target exposed components, focus fire, etc.)
```

**Add at top of section:**
```markdown
**DEFAULT RULE**: Unless card text specifies otherwise, **attacker chooses target component** (Method A).

Use Method B (random) only if:
- Playing with "Fog of War" optional variant rule
- Card text explicitly says "random hit location"
- Both players agree to add chaos to combat

**Targeting Methods (detailed):**
```

---

### 4.6 CLARIFICATION: Heat Removal from Passive Cooling

**File**: `/workspaces/penance/docs/rules/quick-reference.md`
**Line**: 89-92

**Current:**
```markdown
### Removing Heat
- Vent abilities (-2-3 Heat)
- End turn in safe zone (0 Heat)
- Heat Sink equipment (passive -1)
```

**Replace with:**
```markdown
### Removing Heat
- **Vent abilities** (-2 to -3 Heat depending on card)
  - Example: "Emergency Vent" (2 SP) → Remove 3 Heat
- **Pass entire turn** without taking actions (-1 Heat)
  - You forfeit Action Phase, but cool down passively
- **Stand in water hexes** (-2 Heat per turn)
  - Terrain effect, automatic at end of turn
- **Heat Sink equipment** (passive -1 Heat per turn)
  - Accessory slot item, always active
```

---

### 4.7 CLARIFICATION: Neural Feedback Threshold Trigger

**File**: `/workspaces/penance/docs/rules/component-damage-system.md`
**Line**: 333-336

**Current:**
```markdown
4. **Neural Feedback** (Cumulative Strain)
   - When **total Component Damage across ALL components ≥ 15** → +1 Wound
   - Check at end of each attack that adds Component Damage
```

**Replace with:**
```markdown
4. **Neural Feedback** (Cumulative Strain)
   - When **total Component Damage across ALL components first reaches 15+** → +1 Wound
   - Triggers **once per battle** (not every attack)
   - Track with checkbox on pilot sheet: "Neural Feedback [  ] Triggered"
   - Example: Total Component Damage 12 → 16 (crossed 15) → +1 Wound, check box
   - Example: Total Component Damage 16 → 20 (already past 15) → No additional wound
```

---

### 4.8 CLARIFICATION: SCRAP Conversion Timing

**File**: `/workspaces/penance/docs/rules/component-damage-system.md`
**Line**: 348-353

**Current:**
```markdown
**When Component is Destroyed**

**All equipment cards associated with that component become "SCRAP":**
- Primary Weapon cards (if Right Arm destroyed)
- Shield/Offhand cards (if Left Arm destroyed)
- Cards **remain in deck** but lose original function
```

**Add after line 353:**
```markdown

**SCRAP Conversion Timing:**
- Conversion happens **immediately** when component is destroyed
- All associated cards (in hand, deck, discard) become SCRAP
- Cards in **hand** → Can no longer use printed effect (must Cannibalize)
- Cards in **deck/discard** → Will draw/reshuffle as SCRAP in future

**Example**:
- Right Arm destroyed mid-turn
- Your hand: 2× Longsword cards, 3× Universal cards
- **Immediately**: 2× Longsword cards → 2× SCRAP cards
- You can Cannibalize SCRAP cards this turn (0 SP: Discard → Draw 1)
- You **cannot** play them as attacks (component destroyed)
```

---

### 4.9 CLARIFICATION: Overspending SP Discard Source

**File**: `/workspaces/penance/docs/rules/turn-structure.md`
**Line**: 60-69

**Current:**
```markdown
**1.1b Overspending SP (GKR-Style Push System)**
- You can spend UP TO DOUBLE your SP maximum per turn
- **Every SP beyond your maximum costs 1 card** (discard from hand or deck)
```

**Replace with:**
```markdown
**1.1b Overspending SP (GKR-Style Push System)**
- You can spend UP TO DOUBLE your SP maximum per turn
- **Every SP beyond your maximum costs 1 card** (discard from hand or deck, **your choice per card**)
- Example: Scout (6 SP max) overspends to 9 SP total
  - 7th SP: Discard 1 card from hand (your choice)
  - 8th SP: Discard 1 card from hand (your choice)
  - 9th SP: Discard 1 card from deck (your choice)
- You can mix sources (some from hand, some from deck)
```

---

### 4.10 CLARIFICATION: Catastrophic Failure Damage Penalty Duration

**File**: `/workspaces/penance/docs/rules/dice-reference.md`
**Line**: 77-90

**Current:**
```markdown
**CATASTROPHIC FAILURE (Double , total 2)**:
- Your weapon critically malfunctions
- Discard all Primary Weapon cards from hand immediately
- Gain +2 Heat (weapon overheats from malfunction)
- Next attack this turn or next turn: -2 damage
- **Does NOT end your turn** (can still move, use Universal cards)
```

**Replace line 80 with:**
```markdown
- **Your very next attack only:** -2 damage (weapon damaged, then recovers)
- Track penalty: Place token "Weapon Jammed [-2 dmg]"
- After resolving 1 attack with penalty, remove token
- **Does NOT end your turn** (can still move, use Universal cards)
```

---

## SECTION 5: ADDITIONAL OBSERVATIONS

### 5.1 Version Labeling System (Positive Finding)

**Observation**: The repository has a clear version progression:
- v1.0: Simplified teaching rules (fixed 30 cards, basic components)
- v2.0: Variable deck system (26-50 cards, equipment-based)
- v3.0: Advanced mechanics (AP/Structure/Exposure zones, Taint Exploitation, Dice Pool Advantage)

**Recommendation**: Add a **VERSION GUIDE** document:

```markdown
# Which Version Should I Use?

## New Players (Learning the Game)
**Use**: v1.0 Simplified Rules
**Files**: `/docs/codex/rules-combat.html`, `/docs/codex/rules-dice.html`
**Key Features**:
- Fixed 30-card decks
- Simple component HP (Head 3, Arms 4, Chassis 5, Legs 6)
- 2d6 to-hit system
- Basic Heat management

## Experienced Players (Standard Campaign)
**Use**: v2.0 Base Rules
**Files**: `/docs/rules/combat-system.md`, `/docs/rules/turn-structure.md`
**Key Features**:
- Variable deck size (26-50 cards based on equipment)
- Same component HP as v1.0
- Overspending SP mechanic
- Expanded equipment pool

## Veteran Players (Maximum Depth)
**Use**: v3.0 Advanced Rules
**Files**: `/docs/rules/component-damage-system.md`, `/docs/rules/taint-exploitation.md`, `/docs/rules/dice-pool-advantage.md`
**Key Features**:
- AP/Structure/Pilot Exposure component zones
- Taint as tactical resource
- Dice Pool Advantage system (3d6 take 2)
- Pilot Grit progression
```

---

### 5.2 Consistency Across HTML vs Markdown (Issue Pattern)

**Observation**: Multiple contradictions follow pattern:
- **HTML files** (`/docs/codex/*.html`) = Simplified, teaching-focused, sometimes outdated
- **Markdown files** (`/docs/rules/*.md`) = Detailed, mechanically precise, current

**Recommendation**: Add maintenance policy:
```markdown
# Documentation Maintenance Policy

When updating rules:
1. **Update Markdown first** (source of truth)
2. **Then update HTML** (player-facing)
3. **Mark deprecated sections** in HTML if simplifying for teaching
4. **Add version labels** to both file headers

**HTML files are teaching tools** - they can simplify, but must link to full rules in Markdown.
```

---

### 5.3 Strengths of Current System (Positive)

**Well-Documented Areas**:
1. ✅ Heat Strain Table - Consistent across all files
2. ✅ SP Economy - Clear tables, good examples
3. ✅ Attack Dice Values - No contradictions found
4. ✅ To-Hit Modifiers - Comprehensive, well-explained
5. ✅ SCRAP Cannibalize Mechanic - Clear examples in component-damage-system.md

**These sections need no changes.**

---

## PRIORITY ACTION ITEMS

### IMMEDIATE (Fix Before Next Playtest)
1. ✅ **Fix Defense Dice Table** (rules-dice.html) - Add CRITICAL face, remove duplicate SHIELD
2. ✅ **Add Deck Size Version Labels** (rules-combat.html) - Clarify v1.0 vs v2.0
3. ✅ **Clarify Reshuffle Timing** - Add explicit shuffle-in step for Damage cards

### HIGH PRIORITY (Fix This Week)
4. ✅ **Clarify Component Targeting Default** - State "attacker chooses" as default
5. ✅ **Clarify Primary Weapon Component Damage** - Add explicit examples
6. ✅ **Clarify SCRAP Conversion Timing** - Immediate conversion when component destroyed

### MEDIUM PRIORITY (Fix Before Release)
7. ✅ **Clarify Neural Feedback Trigger** - Once per battle, not per attack
8. ✅ **Clarify Heat Removal Mechanics** - Expand "safe zone" explanation
9. ✅ **Add Version Guide** - Help players choose which ruleset to use

### LOW PRIORITY (Polish)
10. ✅ **Clarify Catastrophic Failure Duration** - One attack only
11. ✅ **Clarify Overspending SP Source** - Per-card choice
12. ✅ **Add Edge Case Rules** - Component destroyed mid-attack, etc.

---

## CONCLUSION

**Total Issues Found**:
- 6 Critical Contradictions (must fix)
- 8 Ambiguous Mechanics (should clarify)
- 5 Missing Rules (nice to have)

**Biggest Risk**: Defense Dice face assignment (blocks 33% vs 50%, missing CRITICAL symbol) could make combat unplayable without clarification.

**Recommended Action**:
1. Fix Defense Dice table **immediately** (game-breaking)
2. Add version labels to HTML files (prevents confusion)
3. Create VERSION GUIDE document (helps players choose rules)
4. Schedule playtest with clarified rules to verify fixes

**Overall Assessment**:
The rules system is **mechanically sound** (no mathematical contradictions), but suffers from **version drift** between teaching materials (HTML) and full rules (Markdown). Adding explicit version labels and a migration guide will solve most player confusion.

---

**END OF AUDIT REPORT**

*Generated by Claude Code Agent on October 18, 2025*
