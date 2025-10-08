# Damage & Injury System
## Penance: Absolution Through Steel

**Version**: 0.1
**Last Updated**: October 8, 2025

---

## Core Principle: Deck-as-Health

Your deck represents your Casket's operational capacity. When you take damage, your deck shrinks. When your deck (and hand) are empty, your Casket is disabled.

---

## Taking Damage

### Damage Resolution Choices

When you take damage, you must discard cards equal to damage taken. You choose HOW to discard:

**Option A: Discard from Hand**
- Lose tactical options immediately
- Preserve deck size (cards will cycle back when you reshuffle)
- Good when: You have duplicate cards or weak options in hand

**Option B: Mill from Deck**
- Remove cards from top of deck without looking
- Preserve your current hand (keep your combo/good cards)
- Risk: You might mill important cards
- Good when: You're holding critical cards you need this turn

**Option C: Mixed**
- Discard 2 from hand, mill 1 from deck (for 3 damage, etc.)
- Balanced approach

### Example:

**Scenario**: You take 4 damage. You have 6 cards in hand, 18 cards in deck.

**Choice**:
- Discard all 4 from hand → Left with 2 cards in hand, 18 in deck
- Mill all 4 from deck → Keep 6 card hand, 14 cards left in deck
- Discard 2 from hand, mill 2 from deck → 4 cards in hand, 16 in deck

---

## Component Damage & Hit Location

### Targeting Specific Components

Some attacks specify hit location:
- **Rear attacks**: Target Chassis or Back-mounted equipment
- **Flank attacks**: Target arm on that side (Left or Right)
- **Called shots**: Attacker declares target (may require penalty or higher SP cost)

### When a Component is Hit

**If specific component is targeted** (e.g., "Right Arm takes 3 damage"):

1. You still choose hand vs deck for discarding
2. **BUT**: After you reshuffle, add component-specific Damage cards
3. Track damage by component on player mat

**Example**:
- Right Arm takes 3 damage (you equipped "Faithkeeper Longsword")
- You discard 3 cards (your choice from hand/deck)
- Mark "Right Arm: 3 damage" on player mat
- When you reshuffle: Add 1 Right Arm Damage card to deck per 2 damage taken (round down)
- So 3 damage = 1 Damage card ("Damaged Sword Arm")

### Component Damage Thresholds

| Component Damage | Effect |
|------------------|--------|
| 0-2 damage | Minor - No immediate effect, 1 Damage card when reshuffle |
| 3-5 damage | Moderate - 2 Damage cards when reshuffle |
| 6-8 damage | Major - 3 Damage cards, component degraded (penalties apply) |
| 9+ damage | Critical - Component disabled, all cards from that equipment unusable |

### Component Degradation

**Degraded Components** (6+ damage):
- **Right Arm degraded**: All Right Arm weapon attacks -1 damage
- **Left Arm degraded**: Shield defense reduced by 1
- **Chassis degraded**: Safe Zone SP -1
- **Legs degraded**: Movement costs +1 SP

**Disabled Components** (9+ damage):
- **Right Arm disabled**: Cannot play any Right Arm equipment cards
- **Left Arm disabled**: Cannot play any Left Arm equipment cards
- **Chassis disabled**: Casket is destroyed (mission loss)
- **Legs disabled**: Cannot move (can still rotate and attack)

---

## Damage Card Types

When you reshuffle your deck, add Damage cards based on injuries sustained.

### Minor Damage Cards (0-2 damage to component)

**"Creaking Joints"** (Legs)
```
╔═══════════════════════════════════════╗
║  💔 CREAKING JOINTS             [—]   ║
╠═══════════════════════════════════════╣
║  Type: DAMAGE (Legs)                  ║
║  Cannot be played                     ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  This card clogs your deck.           ║
║                                       ║
║  Movement costs +1 SP.                ║
╠═══════════════════════════════════════╣
║  Keywords: Injury, Minor              ║
╠═══════════════════════════════════════╣
║  "Every step protests."               ║
╚═══════════════════════════════════════╝
```

**Other Minor Damage Cards**:
- **"Dented Plating"** (Chassis) - All damage +1
- **"Strained Servos"** (Arm) - Attacks with this arm cost +1 SP
- **"Flickering Core"** (Chassis) - Generate +1 Heat per turn

### Major Damage Cards (3-5 damage to component)

**"Shattered Plating"** (Chassis)
```
╔═══════════════════════════════════════╗
║  💔 SHATTERED PLATING           [—]   ║
╠═══════════════════════════════════════╣
║  Type: DAMAGE (Chassis)               ║
║  Cannot be played                     ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  This card clogs your deck.           ║
║                                       ║
║  Defense reduced by 2.                ║
╠═══════════════════════════════════════╣
║  Keywords: Injury, Major              ║
╠═══════════════════════════════════════╣
║  "Exposed mechanisms weep oil."       ║
╚═══════════════════════════════════════╝
```

**Other Major Damage Cards**:
- **"Cracked Soulveins"** (Chassis) - All SP costs +1
- **"Mangled Actuators"** (Arm) - This arm's attacks -2 damage
- **"Locked Joints"** (Legs) - Movement -1 hex range

### Critical Damage Cards (6-8 damage to component)

**"Sundered Servos"** (Right Arm)
```
╔═══════════════════════════════════════╗
║  💔 SUNDERED SERVOS             [—]   ║
╠═══════════════════════════════════════╣
║  Type: DAMAGE (Right Arm)             ║
║  Cannot be played                     ║
╠═══════════════════════════════════════╣
║  EFFECT:                              ║
║  This card clogs your deck.           ║
║                                       ║
║  Right Arm attacks deal half damage.  ║
║  All Right Arm cards cost +1 SP.      ║
╠═══════════════════════════════════════╣
║  Keywords: Injury, Critical           ║
╠═══════════════════════════════════════╣
║  "Hanging by cables and hope."        ║
╚═══════════════════════════════════════╝
```

**Other Critical Damage Cards**:
- **"Hemorrhaging Core"** (Chassis) - Gain 2 Heat per turn, leak Soulstone energy
- **"Compound Fracture"** (Legs) - Cannot move more than 1 hex per turn
- **"Blind Sensors"** (Chassis) - All attacks against you gain +1 to hit

---

## Reshuffling & Damage Accumulation

### Reshuffle Trigger

When your deck runs out of cards (during Draw Phase):
1. Shuffle your discard pile
2. **Add Damage cards** based on component injuries
3. Form new deck
4. Continue drawing

### How Many Damage Cards?

**Formula**: 1 Damage card per 2 damage taken to each component (round down)

**Example**:
- Right Arm: 5 damage → Add 2 Right Arm Damage cards
- Left Arm: 2 damage → Add 1 Left Arm Damage card
- Chassis: 0 damage → Add 0 Chassis Damage cards
- Total: 3 Damage cards added to reshuffled deck

### Permanent Damage Tracking

Use player mat to track cumulative damage per component:

```
CASKET STATUS:
├─ Right Arm:  ████░░░░░ (5/9 damage)
├─ Left Arm:   ██░░░░░░░ (2/9 damage)
├─ Chassis:    ░░░░░░░░░ (0/9 damage)
└─ Legs:       ███░░░░░░ (3/9 damage)
```

**Important**: Damage doesn't heal automatically. It persists through reshuffles.

---

## Healing & Repair

### Field Repairs (During Mission)

**Support Class Ability**:
- **Field Suture** (Universal card for Support): Remove 1 Damage card from target's discard pile from game
- Can target self or adjacent ally
- 2 SP cost, Initiative 4
- Only works on cards in discard pile (not in deck/hand)

**Repair Kits** (Relic slot):
- Once per mission: Remove 1 Damage card from your deck (search and remove)
- Costly but effective

### Workshop Repairs (Between Missions)

**Campaign Mode Only**:

**Minor Repair** (50 Credits):
- Reduce component damage by 3
- Remove associated Damage cards from deck

**Major Repair** (150 Credits):
- Fully repair one component
- Remove all Damage cards from that component

**Full Overhaul** (500 Credits):
- Repair all components
- Remove all Damage cards
- Restore Casket to pristine condition

**Permanent Injury**:
- Some critical damage cannot be fully repaired (story/campaign consequences)
- "Scarred Components" - permanently degraded but functional

---

## Component Destruction vs Temporary Damage

### Temporary Damage (Repairable)
- Dents, cracks, hydraulic leaks
- Can be fixed at Workshop
- Represented by Damage cards that can be removed

### Permanent Destruction (Campaign)
- Component is shattered beyond repair
- Must replace entire component (expensive)
- Lose access to that equipment piece permanently
- Example: "Right Arm destroyed" → Must buy new Right Arm equipment

---

## Death Spiral Mitigation

### The Problem:
As you take damage, Damage cards clog your deck → harder to fight effectively → take more damage → more Damage cards → death spiral

### Mitigation Strategies:

1. **Support Class**: Allies can remove your Damage cards
2. **Repair Kits**: Relic slots dedicated to self-repair
3. **Deck Size**: Larger decks (Heavy/Assault) dilute Damage card density
4. **Strategic Reshuffling**: Manage when you reshuffle (don't spam low-cost cards early)
5. **Component Protection**: Use shields, defensive positioning to avoid specific component hits

---

## Defeat Conditions

### Mission Loss (Casket Disabled)

**You are disabled when**:
- Deck is empty AND hand is empty (cannot draw/play cards)
- Chassis component takes 9+ damage (core destroyed)
- Scenario-specific loss condition (mission timer, objective failure)

### Campaign Consequences

**PvP/Arena**:
- Match loss
- No permanent consequences (reset for next match)

**Campaign/Co-op**:
- Pilot may die (permadeath setting dependent)
- Casket heavily damaged (expensive repairs needed)
- Permanent injuries possible (scars, trauma)
- Mission failure may lock campaign paths

---

## Damage Examples

### Example 1: Scout Takes Rear Attack

**Situation**: Scout (24 card deck, 6 in hand) takes 4 damage from rear attack to Chassis.

**Resolution**:
1. Player discards 2 from hand, mills 2 from deck (now 4 cards in hand, 16 in deck)
2. Marks "Chassis: 4 damage" on player mat
3. Continues fighting
4. Later, deck runs out → Reshuffles discard pile
5. Adds 2 Chassis Damage cards (4 damage ÷ 2 = 2 cards)
6. New deck: 22 cards total (20 original + 2 Damage cards)

### Example 2: Heavy Takes Called Shot to Shield Arm

**Situation**: Heavy (34 card deck) takes 6 damage targeted to Left Arm (equipped with Great Shield).

**Resolution**:
1. Player mills 6 from deck (keeps hand intact)
2. Marks "Left Arm: 6 damage" → **Component degraded**
3. Shield defense reduced by 1 (degradation penalty)
4. Continues fighting until reshuffle
5. At reshuffle: Adds 3 Left Arm Damage cards (6 damage ÷ 2 = 3)
6. New deck has 3 "Mangled Shield Arm" cards that reduce defense and clog hand

### Example 3: Support Heals Ally

**Situation**: Support uses "Field Suture" on damaged Scout ally.

**Resolution**:
1. Support spends 2 SP, plays "Field Suture" card
2. Scout has 2 Damage cards in discard pile
3. Scout's player chooses 1 Damage card to remove from game permanently
4. That card won't be added when Scout reshuffles next time

---

## Advanced: Overflow Damage

### When Damage Exceeds Deck + Hand

**Situation**: You have 8 cards total (4 in hand, 4 in deck) but take 10 damage.

**Resolution**:
1. Discard entire hand (4 cards)
2. Mill entire deck (4 cards)
3. Remaining 2 damage "overflows" → Automatically triggers reshuffle
4. Draw 2 cards from newly reshuffled deck, then immediately discard them
5. Add Damage cards for accumulated component damage
6. Continue (if deck/hand not empty)

---

## Quick Reference: Damage Card Ratios

| Total Component Damage | Damage Cards Added at Reshuffle |
|------------------------|----------------------------------|
| 0-1 damage | 0 cards |
| 2-3 damage | 1 card (Minor) |
| 4-5 damage | 2 cards (Major) |
| 6-7 damage | 3 cards (Critical) + Component Degraded |
| 8 damage | 4 cards (Critical) + Component Degraded |
| 9+ damage | Component Disabled (cards unusable) |

---

## Next Steps

- [ ] Design full set of Damage cards (10 unique types)
- [ ] Create player mat tracking zones for component damage
- [ ] Playtest death spiral pacing
- [ ] Balance Support class healing vs damage accumulation
- [ ] Determine campaign permanent injury rules

---

*Damage is inevitable. How you manage it determines survival.*
