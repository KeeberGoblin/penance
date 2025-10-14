# Turn Structure (Final)
## Penance: Absolution Through Steel

**Version**: 2.0 Base Rules (October 10, 2025)
**v3.0 Enhancements**: Optional [Taint Exploitation](taint-exploitation.md) available

---

## Game Structure

### Setup
1. Both players shuffle their 30-card Casket HP decks
2. Draw starting hand (6 cards)
3. **Mulligan** (optional): Shuffle hand back into deck, draw 6 new cards (once only)
4. Place Pilot Wound deck (10 cards, face-down) next to Casket deck
5. Set SP tracker to maximum (varies by Casket type)
6. Set Heat tracker to 0
7. Deploy Caskets on map (see scenario rules)

---

## Game Round

**A round consists of all players taking one turn each.**

### Initiative Phase
- All players roll 1d6
- Highest roll acts first
- Ties: Re-roll
- Turn order proceeds clockwise from first player

### Player Turns
- Each player takes one complete turn
- Once all players have acted, the round ends
- Start new round (roll initiative again)

---

## Player Turn Structure

**Each turn has 4 phases: Refresh → Action → Draw → End**

---

### PHASE 1: REFRESH

**Restore your resources and check status.**

**1.1 Restore SP**
- Set SP to your maximum (based on Casket type)
  - Scout Caskets: 6 SP
  - Assault Caskets: 5 SP
  - Heavy Caskets: 4 SP
  - Fortress Caskets: 3 SP
- Modified by:
  - Chassis destroyed: -1 SP max
  - Leg-Skimmed pilots: +1 SP max
  - Certain Scars/Wounds

**1.1b Overspending SP (GKR-Style Push System)**
- You can spend UP TO DOUBLE your SP maximum per turn
- **Every SP beyond your maximum costs 1 card** (discard from hand or deck)
- **Example**: Scout (6 SP) can spend up to 12 SP total
  - First 6 SP: Free
  - 7th-12th SP: Discard 1 card each
- This is **voluntary self-harm** for tactical advantage
- Discarded cards go to discard pile (can be recovered)
- "Burn HP for power. Risk everything for the kill."

**1.2 Heat Check**
- If you have **5+ Heat** (Danger Zone):
  - Roll **Strain** (1d6 + current Heat)
  - Apply result from Strain Table (see Quick Reference)
- If you have **0-4 Heat** (Safe Zone):
  - No penalties, skip this step

**1.3 Start-of-Turn Effects**
- Resolve any "at start of your turn" card effects
- Example: Internal Bleeding Wound = discard 1 card

---

### PHASE 2: ACTION PHASE

**Spend SP to play cards and perform actions.**

**You may:**
- Play cards from your hand (costs SP)
- Move your Casket (costs 1 SP per hex)
- Use free actions (0 SP cards)
- Mix actions in any order

**Continue until:**
- You run out of SP, OR
- You choose to pass (saving SP for reactive cards), OR
- Your hand is empty

**Card Types**:
- **Standard Cards**: Cost SP (listed on card)
- **Free Actions**: 0 SP cost (can play multiple)
- **Reactive Cards**: 0 SP, can only be played during opponent's turn

**Movement Rules**:
- Costs **1 SP per hex** moved
- Can move through allies (don't stop)
- Cannot move through enemies
- Cannot move through walls/obstacles
- Difficult terrain: +1 SP per hex (2 SP total)
- Must have line of sight to destination hex (can't move blindly through walls)

**Rotation**:
- Rotating to face different direction: **Free** (can do once per turn)
- Facing matters for attacks (front/side/rear modifiers)

**Common Actions**:
| Action | SP Cost | Notes |
|--------|---------|-------|
| Move 1 hex | 1 SP | +1 SP if difficult terrain |
| Play attack card | Varies | 1-5 SP depending on card |
| Play defense card | 0 SP | Reactive, during enemy turn |
| Play utility card | Varies | 1-3 SP typically |
| Vent Heat | 2 SP | Remove 3 Heat (Emergency Vent card) |
| Rotate facing | Free | Once per turn |

---

### PHASE 3: DRAW PHASE

**Refill your hand to 6 cards.**

**3.1 Draw Cards**
- Draw cards from your Casket HP deck until hand size = 6
- If hand already has 6+ cards, don't draw
- Draw one at a time (order matters for deck-out situations)

**3.2 Reshuffle Trigger**
- If deck runs out while drawing:
  1. Shuffle your discard pile into a new deck
  2. **Add 1 "Damage" card** to the deck (permanent)
  3. Continue drawing normally
- **Damage cards**: Blank cards that do nothing when played (death spiral mechanic)

**3.3 Deck Empty = Defeated**
- If you need to draw but deck AND discard are both empty:
  - Your Casket is **defeated** (structural failure)
  - Pilot must roll on Survival table (see Campaign rules)
  - In Arena: You lose the match

---

### PHASE 4: END TURN

**Wrap up your turn.**

**4.1 End-of-Turn Effects**
- Resolve any "at end of your turn" effects
- Example: "Gain 1 Heat at end of turn"

**4.2 Discard Down**
- If hand size exceeds 6: Discard down to 6 cards
- Choose which cards to discard
- (Rare, usually only happens if cards say "Draw 2 cards")

**4.3 Announce Done**
- Say "Turn complete" or "I pass"
- Next player begins their turn

---

## Special Timing: Reactive Cards

**Reactive cards can be played during OPPONENT'S turn.**

**How Reactives Work**:

**Trigger**: Opponent declares an action (usually an attack)

**Response Window**: Before damage is resolved, you may play 1 reactive card
- Must have **Initiative [—]** keyword
- Costs **0 SP** (doesn't use your SP pool)
- Played from hand

**Examples**:
- **Brace for Impact**: "Reduce next damage by 2"
- **Deflect** (Shield): "Reduce damage by 1"
- **Unyielding Bulwark**: "Reduce damage by 3, gain 1 Heat"

**Limits**:
- Can only play **1 reactive card per attack**
- Must be played BEFORE damage is calculated
- If you have no reactive cards in hand, you cannot respond

**Resolution** (With Dice System):
1. Attacker plays attack card, declares target component
2. **Calculate To-Hit Number** (see Dice Reference)
   - Base 5+, apply modifiers (range, movement, facing, cover, elevation)
3. **Attacker rolls 2 Attack Dice**, adds values
   - Hit (5-6), Strong Hit (7-8), Critical (9), EXECUTION (10), or Miss (<target)
4. **If hit**, Defender plays reactive card (if they have one)
5. **Defender rolls Defense Dice** (1 per damage point)
   - Count blocks (🛡️ ⚙️), apply special effects (💀 ⚔️ 🔥)
6. Defender discards final damage (original - blocks) from hand/deck

---

## Round End

**When all players have completed their turns:**

**Check Victory Conditions**:
- Any player defeated? (deck empty)
- Scenario objective completed?
- If yes: Game ends

**Start New Round**:
- Roll initiative again
- First player takes their turn
- Continue until game ends

---

## Special Rules

### Heat Management

**Heat Zones**:
- **Safe Zone** (0-4 Heat): No penalties
- **Danger Zone** (5-9 Heat): Roll Strain at start of turn
- **Critical** (10+ Heat): Auto-fail Strain roll (automatic malfunction)

**Gaining Heat**:
- Certain cards say "Gain X Heat"
- Pushing into Danger Zone (high-risk, high-reward)

**Removing Heat**:
- Play cards that say "Remove X Heat"
- Stand in water hexes (remove 2 Heat per turn)
- Pass entire turn without acting (remove 1 Heat)

**Strain Table** (Roll 1d6 + current Heat):
| Result | Effect |
|--------|--------|
| 1-5 | **Minor Overload**: Gain 1 Heat |
| 6-8 | **SP Drain**: Lose 1 SP this turn (max reduced temporarily) |
| 9-11 | **System Damage**: Take 2 damage (discard 2 cards) |
| 12+ | **Critical Failure**: Random component malfunctions (roll 1d6: 1-2=Arm, 3-4=Leg, 5=Head, 6=Chassis) |

---

### Component Damage Tracking

**When you discard Primary Weapon cards due to damage:**

**Mark Component Damage** on your pilot sheet:
- Attacker chooses which component to target (or roll randomly)
- Each Primary Weapon card discarded = 1 Component Damage
- Track separately: Right Arm, Left Arm, Legs, Head, Chassis

**Component Destroyed** (at 3 damage):
| Component | Effect When Destroyed |
|-----------|----------------------|
| **Right Arm** | Discard all Primary Weapon cards from hand. Cannot play Primary Weapon cards. |
| **Left Arm** | Discard all Secondary Equipment cards from hand. Cannot play Secondary Equipment cards. |
| **Legs** | Movement costs +1 SP per hex (2 SP per hex total). |
| **Head** | Cannot use Sensor Sweep. -1 to all ranged attacks. |
| **Chassis** | Permanent -1 SP maximum (even after Refresh). |

**Destroyed components remain destroyed** for rest of battle (cannot be repaired mid-combat).

---

### Pilot Wound System

**When Pilot Takes Damage:**

Pilots take damage in these situations:
1. **Capsule Breach** (enemy targets capsule specifically, rare)
2. **Neural Feedback** (when you accumulate 5+ total Component Damage)
3. **Thread Snap** (when Hand Thread cards are damaged)
4. **Taint Overload** (when Taint reaches 10)
5. **Casket Destruction** (when Casket HP reaches 0, pilot rolls save)

**When pilot takes 1 damage:**
- Flip top card of Pilot Wound deck face-up
- Read effect immediately
- Effect is permanent for rest of battle (some are permanent for campaign)

**Wound Types**:
- **Minor Injury** (5 cards): Temporary debuffs until end of mission
- **Severe Injury** (3 cards): PERMANENT effects even in future missions
- **Trauma** (2 cards): Mental breakdowns affecting behavior

**All 10 Wounds flipped = Pilot Death**
- Casket becomes inert
- In Arena: You lose
- In Campaign: Pilot is dead, create new character

---

## Example Turn Sequence

**Player: Church Confessor (Light, 6 SP)**

**Starting state:**
- 24 cards in deck
- 6 cards in hand
- 2 Heat
- Facing north

---

**PHASE 1: REFRESH**
- Restore to 6 SP
- Heat check: 2 Heat (Safe Zone) → No roll needed
- No start-of-turn effects

**PHASE 2: ACTION**
1. **Rotate** (free action) → Now facing enemy
2. **Move 3 hexes** (3 SP) → Advance toward enemy
3. **Play Blood Offering** (0 SP) → Discard 2 cards from deck (self-harm), gain "+3 damage, ignore 1 Armor" buff
4. **Play Faithful Thrust** (2 SP) → Declare attack for 4 damage + buffs
   - **To-Hit**: Base 5+ | Moved 3 hexes +1 | Medium range (5 hexes) +1 = **Need 7+**
   - **Roll Attack Dice**: ⚔️ (3) + 💀 (5) = **8 total** → **Strong Hit** (+1 damage)
   - Final damage: 4 base + 3 (Blood Offering) + 1 (Strong Hit) = **8 damage**
   - **Enemy rolls 8 Defense Dice**: 🛡️ 🛡️ 🩸 🩸 🩸 💀 🔥 ⚔️
   - **2 blocks** → Reduce to 6 damage
   - **1 Critical** (💀) → +1 Component Damage
   - **1 Heat** (🔥) → Enemy gains 1 Heat
   - Enemy chooses to discard 6 cards (4 from hand, 2 from deck)
5. **OVERSPEND**: Move 2 more hexes (2 SP) → Costs 7th and 8th SP
   - 7th SP = Discard 1 card (overspending cost)
   - 8th SP = Discard 1 card (overspending cost)
   - Result: Moved total 5 hexes + attacked, but discarded 2 extra cards
6. **Total spent: 8 SP (6 free + 2 paid with cards)**

**PHASE 3: DRAW**
- Hand has 4 cards (played Blood Offering, Faithful Thrust)
- Draw 2 cards → Hand back to 6

**PHASE 4: END TURN**
- No end-of-turn effects
- Announce "Done"
- Next player's turn

---

**Current state:**
- 22 cards in deck (started 24, discarded 2 from Blood Offering)
- 6 cards in hand
- 2 Heat (unchanged)
- 2 SP unused (could use for reactive defense if attacked)

---

## FAQ

**Q: Can I play multiple 0 SP cards in one turn?**
A: Yes! Free actions can be played as many times as you have them.

**Q: What happens if I'm attacked and have no reactive cards?**
A: You take full damage. Reactive cards are optional defenses, not mandatory.

**Q: Can I move after attacking?**
A: Yes! Actions can be done in any order during Action Phase.

**Q: Do I have to spend all my SP?**
A: No. You can pass early to save SP for reactive cards.

**Q: What if my hand is empty mid-turn?**
A: You can't play cards, but you can still move (costs SP directly).

**Q: Can I play a card during someone else's turn (not reactive)?**
A: No. Only [—] Initiative reactive cards can be played on opponent's turn.

**Q: What happens if both my deck and discard are empty?**
A: Your Casket is defeated. Game over (or mission failure in campaign).

**Q: Do Damage cards count as cards in my deck?**
A: Yes, they're physical cards. They just do nothing when played (dead draws).

**Q: Can I choose NOT to draw cards?**
A: No. Draw Phase is mandatory (draw to hand size 6).

**Q: If I take damage during my turn, do I draw back to 6?**
A: Damage discards from DECK, not hand. Hand only changes when you play cards or draw.

---

**END OF DOCUMENT**

---

*"Refresh. Fight. Draw. Endure. This is the rhythm of war. This is how Caskets die."*
