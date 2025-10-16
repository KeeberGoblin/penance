# Mercenary Hiring - Summon Mechanics

**Core Mechanic**: Hire Mercenary (3 Credits, summon temporary allied unit)  
**Maximum Active**: 2 Mercenaries simultaneously  
**Duration**: Until destroyed or mission ends

---

## Mercenary Unit Stats

### Base Mercenary

**HP**: 8 (deck of 8 cards)  
**Damage**: 3 per attack  
**Movement**: 5 hexes per turn  
**SP**: 3 per turn (basic actions only)  
**Range**: Melee (1 hex) or Ranged (4 hexes)

**Special Rules**:
- Acts on your turn (immediately after you finish)
- Uses simplified AI (if player doesn't control, follows basic attack pattern)
- Can't use faction cards (only basic attacks and movement)
- Doesn't generate Credits (only you do via War Profiteer when Mercenary kills)

---

## Hiring Mechanics

### Hire Mercenary (Faction Card)

**Cost**: 3 Credit tokens  
**Range**: 3 hexes  
**Effect**: Summon 1 Mercenary unit (8 HP, 3 damage). Mercenary appears in target hex (must be unoccupied). Can have up to 2 Mercenaries active simultaneously.

**Summon Location Rules**:
- Must target empty hex within 3 hexes of you
- Can't summon on enemy-occupied hex
- Can't summon on impassable terrain (walls, pits, lava)
- Can summon on difficult terrain (but Mercenary pays movement cost)

**Timing**:
- Can summon during your turn (costs SP to play card, but Mercenary acts immediately after)
- Can't summon during enemy turn (not a reactive card)

---

## Mercenary Control

### Player Control (Default)

**If you want direct control**:
- On your turn, after your actions, you can command each Mercenary
- Mercenaries act in order summoned (first summoned acts first)
- Each Mercenary has 3 SP to spend:
  - Move (1 SP per hex)
  - Attack (2 SP, melee or ranged)
  - Hold position (0 SP, do nothing)

**Example Turn**:
1. Your turn: Play cards, attack, move (5 SP spent)
2. Mercenary 1: Move 2 hexes, attack enemy (3 SP spent)
3. Mercenary 2: Move 1 hex, attack different enemy (3 SP spent)
4. End turn

---

### AI Control (Optional/Lazy Mode)

**If you don't want to micromanage**:
- Mercenaries follow simple AI:
  1. Move toward nearest enemy
  2. Attack if in range
  3. If can't reach enemy, hold position

**Pros**: Saves time, simple decisions  
**Cons**: Not optimal, AI can't coordinate complex plays

---

## Mercenary Actions

### Attack (Melee)

**Cost**: 2 SP  
**Range**: 1 hex  
**Damage**: 3  
**Effect**: Deal 3 damage to adjacent enemy. Roll 2d6, hit on 5+.

**When to Use**: Mercenary is adjacent to enemy

---

### Attack (Ranged)

**Cost**: 2 SP  
**Range**: 4 hexes  
**Damage**: 2  
**Effect**: Deal 2 damage to enemy within 4 hexes. Roll 2d6, hit on 6+ (ranged penalty).

**When to Use**: Mercenary can't reach melee range, shoot from distance

---

### Move

**Cost**: 1 SP per hex  
**Range**: Self  
**Effect**: Move up to 3 hexes (Mercenary has 3 SP total, can spend all on movement)

**When to Use**: Need to reposition, close distance, retreat

---

### Hold Position

**Cost**: 0 SP  
**Range**: Self  
**Effect**: Do nothing. Bank SP for... wait, SP doesn't carry over. This is just "pass turn."

**When to Use**: Mercenary has no valid actions (all enemies out of range, no movement needed)

---

## Mercenary Buffs

### Contract Enforcement (Faction Card)

**Cost**: 2 SP  
**Range**: 4 hexes  
**Effect**: All friendly Mercenary units within range gain +2 damage and +2 Defense until end of round. Spend 1 Credit token to extend duration to 2 rounds.

**Why This Is Critical**:
- **+2 damage**: 3 damage → 5 damage (almost doubles Mercenary damage)
- **+2 Defense**: Mercenaries survive longer (enemies need more hits to kill)
- **Area buff**: Affects both Mercenaries if grouped

**Optimal Play**:
- Use before Mercenaries attack (maximize damage)
- Keep Mercenaries within 4 hexes of each other (both get buff)
- Spend 1 Credit to extend if Mercenaries will survive to next round

---

### Mercenary Contract (Secondary Equipment)

**Cost**: 2 SP  
**Range**: 4 hexes  
**Effect**: Target friendly Mercenary immediately moves up to 3 hexes and makes a 3-damage attack.

**Why This Is Valuable**:
- **Extra action**: Mercenary acts twice in one turn (your SP, then Mercenary's SP)
- **Forced positioning**: Move Mercenary into optimal attack position, then attack
- **Coordination**: Combine with Contract Enforcement (move + buffed attack = 5 damage)

**Optimal Play**:
- Use on Mercenary that already acted (effectively gives them 2 turns)
- Move Mercenary to flank enemy (then attack for Pack Tactics bonus from other Mercenary)
- Emergency escape (move Mercenary away from danger, attack different target)

---

## Mercenary Lifespan

### How Long Do Mercenaries Survive?

**Average Lifespan**: 2-3 turns

**Factors**:
- **Enemy focus**: If enemies target Mercenaries, they die fast (8 HP = 2-3 hits)
- **Positioning**: Mercenaries in front line die faster (tank damage for you)
- **Buffs**: Contract Enforcement (+2 Defense) extends lifespan significantly

**Example**:
- Turn 1: Summon Mercenary (8 HP)
- Turn 2: Enemy attacks Mercenary (takes 4 damage, 4 HP remaining)
- Turn 3: Enemy attacks again (takes 4 damage, 0 HP remaining, destroyed)

**Result**: 2 turns of value for 3 Credits

---

### Mercenary Death

**When Mercenary reaches 0 HP**:
- Mercenary is destroyed (removed from battlefield)
- You can summon new Mercenary (costs 3 Credits again)
- War Profiteer triggers if enemy killed Mercenary (gain 2 Credits)

**Net Cost**:
- Mercenary cost: 3 Credits
- Mercenary death refund (War Profiteer): 2 Credits
- **Net cost**: 1 Credit per Mercenary (effectively)

---

## Mercenary Sacrifice

### Liquidate Assets (Faction Card)

**Cost**: 0 SP (Gambit)  
**Range**: Self  
**Effect**: Destroy all your active Mercenaries. Gain 2 Credit tokens per Mercenary destroyed.

**When to Use**:
- Mercenaries are damaged and about to die (convert dying assets into Credits)
- Need Credits immediately (emergency Credit generation)
- Mercenaries out of position (better to re-summon in better location)

**Example**:
- You have 2 Mercenaries (both at 2 HP, about to die)
- Use Liquidate Assets (destroy both, gain 4 Credits)
- Re-summon 1 Mercenary in better position (spend 3 Credits)
- **Result**: Net +1 Credit, fresh 8 HP Mercenary in optimal location

---

## Advanced Mercenary Tactics

### Tactic 1: Mercenary Wall

**Setup**: 2 Mercenaries + you

**Execution**:
1. Summon 2 Mercenaries in front line (block enemy approach)
2. You stay behind Mercenaries (safe from melee attacks)
3. Mercenaries tank damage, you attack from range
4. **Result**: Mercenaries absorb 16 HP total damage (saves your HP)

**Value**: 3 Credits = 16 HP meat shield

---

### Tactic 2: Flanking Formation

**Setup**: 2 Mercenaries + Pack Tactics enemies

**Execution**:
1. Mercenary 1 attacks enemy from front
2. Mercenary 2 flanks enemy from behind (adjacent to Mercenary 1)
3. Both Mercenaries get flanking bonus (+1-2 damage if enemy has Pack Tactics weakness)
4. **Result**: 6-8 damage coordinated strike

**Value**: Positioning multiplies damage

---

### Tactic 3: Hit-and-Run Mercenaries

**Setup**: Mercenary Contract + ranged attacks

**Execution**:
1. Mercenary moves into range (2 hexes toward enemy)
2. Mercenary shoots (2 damage ranged, 2 SP)
3. Mercenary moves away (1 hex back, 1 SP)
4. Next turn, use Mercenary Contract (move Mercenary 3 hexes away, attack from range)
5. **Result**: Mercenary never gets hit (kiting strategy)

**Value**: Mercenary survives longer (4-5 turns instead of 2-3)

---

### Tactic 4: Sacrifice Chain

**Setup**: Liquidate Assets + Buyout Strike

**Execution**:
1. Mercenaries kill 1-2 enemies (generate 2-4 Credits via War Profiteer)
2. Mercenaries damaged (3-4 HP remaining)
3. Use Liquidate Assets (destroy both, gain 4 Credits)
4. Use Buyout Strike (kill enemy, summon free Mercenary)
5. Re-summon 2nd Mercenary (spend 3 Credits)
6. **Result**: 2 fresh Mercenaries, net +1-3 Credits, enemies dead

**Value**: Convert damaged Mercenaries into Credits, then refresh board state

---

## Mercenary Loadout Synergies

### Best Faction Cards for Mercenary Builds

**Must-Have**:
1. **Hire Mercenary** (obviously, can't run Mercenary build without it)
2. **War Profiteer** (Mercenary kills generate Credits, sustains economy)
3. **Contract Enforcement** (buffs Mercenaries, doubles their effectiveness)

**Strong Synergy**:
4. **Buyout Strike** (free Mercenary on kill, saves 3 Credits)
5. **Liquidate Assets** (convert dying Mercenaries into Credits)
6. **Mercenary Contract** (extra Mercenary action, force positioning)

**Avoid**:
- Insurance Policy (Mercenaries are expendable, don't waste Credits defending them)
- Golden Parachute (you don't die if Mercenaries tank for you)

---

## Mercenary Checklist

**Before Summoning**:
- [ ] Do I have 3 Credits? (Check Credit bank)
- [ ] Is summon location valid? (Empty hex within 3 hexes)
- [ ] Do I have War Profiteer? (If no, Mercenaries don't generate value)
- [ ] Can I afford to lose this Mercenary? (Don't summon if you need Credits for defense)

**During Mercenary Turn**:
- [ ] Optimal target? (Focus fire or spread damage?)
- [ ] Positioning safe? (Will Mercenary die next turn?)
- [ ] Buff available? (Contract Enforcement ready?)
- [ ] Coordinate with other Mercenary? (Flanking bonus?)

**After Mercenary Dies**:
- [ ] Did War Profiteer trigger? (Should gain 2 Credits)
- [ ] Re-summon now or later? (Do I need board presence immediately?)
- [ ] Should I have used Liquidate Assets? (Wasted Credit opportunity?)

---

## Mercenary Mistakes to Avoid

### X Don't Summon Without War Profiteer

**Problem**: Mercenaries cost 3 Credits but don't generate Credits back if you don't have War Profiteer
**Solution**: Always run War Profiteer in Mercenary builds

### X Don't Over-Invest in Dying Mercenaries

**Problem**: Spending Credits to heal/buff Mercenary that will die anyway
**Solution**: Liquidate Assets early, re-summon fresh Mercenary

### X Don't Summon Both Mercenaries Turn 1

**Problem**: 6 Credits spent immediately, no Credits for defense
**Solution**: Summon 1 Mercenary Turn 2-3, 2nd Mercenary Turn 4-5 (stagger spending)

### X Don't Forget Maximum Active = 2

**Problem**: Can't summon 3rd Mercenary (game won't allow)
**Solution**: Kill or Liquidate 1 Mercenary before summoning new one

### X Don't Ignore Mercenary Positioning

**Problem**: Mercenaries summoned in bad location, die immediately
**Solution**: Summon behind cover, behind allies, or out of enemy range

---

## Mercenary FAQ

**Q: Can Mercenaries use my faction cards?**  
A: No. Mercenaries only have basic attacks and movement.

**Q: Do Mercenaries generate Credits when they kill?**  
A: No. Only you generate Credits via War Profiteer (but Mercenary kills trigger it).

**Q: Can enemies target my Mercenaries?**  
A: Yes. Mercenaries are valid targets (often targeted first, which is good—they tank for you).

**Q: Can I heal Mercenaries?**  
A: No direct healing cards for Mercenaries. If damaged, better to Liquidate and re-summon.

**Q: What happens to Mercenaries at end of mission?**  
A: Mercenaries disappear (don't carry over between missions).

**Q: Can Mercenaries capture objectives?**  
A: Yes (if scenario allows, Mercenaries count as allied units for objective control).

**Q: Can I summon Mercenaries during Setup Phase?**  
A: No. Hire Mercenary is played during your turn (not Setup).

**Q: Do Mercenaries benefit from my passive abilities?**  
A: Depends. Contract Enforcement buffs them. Other abilities (like Monopoly Control) only affect you, not Mercenaries.

---

**[← Previous: Credit Economy](credit-economy.md)** | **[Next: Ledger Orthodox vs Rational →](ledger-orthodox-vs-rational.md)**
