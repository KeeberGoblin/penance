# Honor Duel System - 1v1 Combat Challenges

**Core Mechanic**: Honor Duel (2 SP, Gambit)  
**Duration**: 1 round (you and target only attack each other)  
**Reward**: 3 Forge tokens + 3 cards on kill  
**Punishment**: Coward's Mark (+2 damage permanently) if enemy refuses

---

## Honor Duel Rules

### How to Challenge

**Honor Duel Card** (2 SP, Gambit):
- **Cost**: 2 SP
- **Range**: 6 hexes
- **Effect**: Challenge 1 visible enemy to Honor Duel. For 1 round, only you and target enemy can attack each other (all other units are ignored). If you kill target, gain 3 Forge tokens and recover 3 cards. If target refuses duel, they gain "Coward's Mark" (all Crucible attacks against them deal +2 damage permanently this mission).

---

### Duel Mechanics

**When Duel is Accepted**:
1. **Isolation**: Only you and target can attack each other
2. **Allies ignored**: Your allies can't help you, enemy allies can't help target
3. **Other enemies ignored**: You can't attack other enemies, they can't attack you
4. **Duration**: 1 round (your turn + enemy turn)
5. **Ends when**: Round ends OR target dies OR you die

**Example Turn Sequence**:
- **Your turn**: You attack dueled enemy (5 damage), enemy takes it
- **Enemy turn**: Enemy attacks you (4 damage), you take it
- **Other players' turns**: Can't attack you or dueled enemy (duel is sacred)
- **Next round**: Duel ends, normal combat resumes

---

### Duel Acceptance

**Enemy AI Decision** (How enemy decides to accept/refuse):

**Factors**:
1. **Strength comparison**: Is enemy stronger than you? (more HP, higher damage)
2. **Allies present**: Does enemy have allies nearby? (wants help)
3. **Honor culture**: Is enemy Crucible or honor-bound faction? (more likely to accept)
4. **Coward's Mark fear**: Does enemy fear +2 damage penalty? (forces acceptance)

**Acceptance Rate**:
- **Crucible enemies**: 90% accept (honor culture)
- **Church/Dwarves**: 70% accept (respect duels)
- **Nomads**: 60% accept (pragmatic warriors)
- **Elves/Exchange**: 40% accept (prefer tactics over honor)
- **Ossuarium/Syndicate**: 20% accept (no honor code)
- **Abominations**: 0% accept (mindless, can't understand honor)

---

### Coward's Mark

**If Enemy Refuses Duel**:
- Enemy gains "Coward's Mark" debuff
- **Effect**: All Crucible attacks against marked enemy deal +2 damage permanently this mission
- **Visible**: Mark appears above enemy (glowing brand, everyone sees it)
- **Stacks**: No (mark is binary, either marked or not)
- **Removal**: Permanent for mission (can't be removed)

**Why This Is Powerful**:
- **Team benefit**: ALL Crucible players deal +2 damage to marked enemy
- **Psychological**: Enemies fear being marked (forces duel acceptance)
- **Punishment**: Refusing duel doesn't save enemy (takes more damage anyway)

---

## Duel Tactics

### When to Challenge

**Ideal Duel Targets**:
1. **Strong but beatable**: Enemy has 10-15 HP (you can kill in 2-3 hits)
2. **Enemy carry**: Priority target (support, healer, ranged damage dealer)
3. **Isolated enemy**: Enemy separated from allies (duel prevents their help)
4. **Wounded enemy**: Enemy at 50% HP (easy kill, gain 3 tokens + 3 cards)

**Avoid Dueling**:
1. **Tanks**: Enemies with 20+ HP (duel lasts too long, wastes time)
2. **Enemies with allies adjacent**: If enemy has support, they're harder to kill
3. **Enemies in lava**: If enemy is already taking environmental damage, let them burn
4. **When you're low HP**: Duel locks you into combat, can't retreat

---

### Duel Builds

**Aggressive Duelist** (Maximize Duel Damage):

**Deck**:
- Honor Duel (challenge)
- Emberforged Strike (5 damage + 2 tokens for 7 damage + burn)
- Duelist's Stance (+2 damage buff)
- Pack Fury (+3 damage if outnumbered)
- Ashen King's Wrath (6 damage, 8 if outnumbered)

**Strategy**: Challenge strongest enemy, use Duelist's Stance (+2 damage), then Ashen King's Wrath (8 damage with outnumbered bonus), then Emberforged Strike (7 damage). Total: 15 damage in one round (kills most targets).

---

**Defensive Duelist** (Survive Long Duels):

**Deck**:
- Honor Duel (challenge)
- Forge Blessing (reduce damage by 3-5)
- Ember Shield (reduce damage by 2-4)
- Last Stand (+3 damage, +2 Defense at low HP)
- Trial by Fire (immune to fire, +3 damage, regenerate)

**Strategy**: Challenge tanky enemy, tank their attacks with Forge Blessing + Ember Shield, use Last Stand at low HP for power spike, wear them down over 2-3 rounds.

---

### Coward's Mark Exploitation

**Setup**: Honor Duel + Coward's Brand

**Execution**:
1. Challenge enemy with Honor Duel (2 SP)
2. Enemy refuses (gains Coward's Mark)
3. Use Coward's Brand (2 SP, ranged): Deal 3 damage, if target has mark → 6 damage + target can't use defense cards
4. **Result**: Enemy takes 6 damage and can't defend (punished for cowardice)

**Value**: Forcing duel refusal is sometimes better than winning duel (mark applies to entire team)

---

## Honor Duel Synergies

### Card Synergies

**Honor Duel + Pack Fury**:
- Challenge enemy, trigger Pack Fury (outnumbered bonus)
- Gain +3 damage against dueled enemy
- **Combo**: 1v1 technically counts as "outnumbered" (you're alone vs enemy + their team in reserve)

**Honor Duel + Trial by Fire**:
- Use Trial by Fire (3 tokens, +3 damage, immune to fire, regenerate)
- Challenge enemy to duel
- **Combo**: +3 damage to all attacks, regenerate 1 card/turn during duel = sustain + power

**Honor Duel + Duelist's Stance**:
- Use Duelist's Stance (+2 damage, +1 damage taken)
- Challenge enemy
- **Combo**: High-risk/high-reward (kill enemy fast, accept taking more damage)

---

### Ancestral Iron Synergies

**+1 Damage Ancestral Weapon**:
- Every attack in duel deals +1 damage (permanent)
- **Value**: +1 damage per attack × 3 attacks/duel = +3 damage total

**+1 Defense Ancestral Weapon**:
- Reduces all damage taken in duel by 1
- **Value**: Survive longer duels (tankier)

**+1 Movement Ancestral Weapon**:
- No direct duel synergy (movement locked during duel)
- **Value**: Better positioning before challenging (get into duel range faster)

---

## NPC Duel Challenges

### Ashen-King Torrak Challenges Players

**Scenario**: Torrak challenges player to Honor Duel

**Torrak's Stats**:
- **HP**: 30 (deck of 30 cards)
- **Damage**: 5 per attack
- **Special**: Undefeated passive (+2 damage during duels)
- **Strategy**: Aggressive, uses Duelist's Stance (+2 damage)

**Player Options**:
1. **Accept duel**: Fight Torrak 1v1 (win = gain Torrak as ally, lose = owe him debt)
2. **Refuse duel**: Gain Coward's Mark (all Crucible deal +2 damage to player permanently)
3. **Negotiate**: Convince Torrak to delay duel (Persuasion check, hard)

**If Player Wins**:
- Torrak respects player (pledges Ironpeak Pack as allies)
- Torrak gives player Ancestral Weapon (+1 damage, his personal sword)
- **Quote**: "You have earned my steel. Fight well."

**If Player Loses**:
- Torrak spares player (doesn't kill, honorable)
- Player owes Torrak "blood debt" (must complete quest for him)
- **Quote**: "You fought with honor. Your debt is one task. Choose wisely."

**If Player Refuses**:
- Torrak brands player coward (Coward's Mark permanently)
- All Crucible NPCs deal +2 damage to player (entire campaign)
- Torrak becomes enemy (hunts player for dishonoring challenge)
- **Quote**: "Craven. You do not deserve the flame."

---

## Honor Duel Campaign Integration

### Early Campaign: Duel Introduction

**Quest**: "Trial of Steel"
- Forge-Matron Kerra offers trial: "Duel my champion to prove your worth."
- Player must duel Crucible warrior (10 HP, 3 damage)
- **Reward**: If player wins → Kerra grants Crucible blessing (start with 3 Forge tokens next mission)
- **Failure**: If player loses → Kerra respects courage, offers second chance (retry duel later)

---

### Mid Campaign: Honor Crisis

**Quest**: "The Coward's Shame"
- Allied NPC refuses Honor Duel from Crucible warrior
- NPC gains Coward's Mark (all Crucible enemies target NPC)
- **Choice**: Defend NPC (fight off Crucible) OR abandon NPC (let them die to restore honor)
- **Outcome**: Defend = Crucible become enemies, Abandon = Crucible respect player's honor

---

### Late Campaign: Torrak's Final Challenge

**Quest**: "The Undefeated"
- Ashen-King Torrak challenges player to final duel (ultimate test)
- **Stakes**: Win = Torrak pledges entire Ironpeak Pack to player's cause (2,000 warriors)
- **Failure**: Lose = Player owes blood debt (must complete suicide mission for Torrak)
- **Refusal**: Refuse = Torrak declares player enemy, hunts them forever

---

## Honor Duel Lore

### The Sacred Duel (Crucible Tradition)

**Origin**: Pre-Sundering Forge-Clans
- Disputes settled via duels (instead of clan wars)
- Loser's family honored winner (bloodless resolution)
- Cowards exiled (refusing duel = unforgivable)

**Post-Sundering Evolution**:
- Duels became religious (blessed by First Forge deity)
- Coward's Mark introduced (permanent brand, visible to all)
- **Result**: Duels rarely refused (mark worse than death)

---

### Famous Duels

**The Founding Duel** (Year 50):
- First Forge-Matron challenged rival clan leader
- Fought for 3 hours (both exhausted)
- Matron won, united two clans into single Pack
- **Legacy**: Established Forge-Matron authority (strongest duelist leads)

**Torrak's 47th Victory** (Year 437, recent):
- Torrak challenged Church Inquisitor (strongest Church warrior)
- Inquisitor refused (viewed duels as pagan ritual)
- Torrak branded Inquisitor coward (entire Church offended)
- **Result**: Church-Crucible relations soured (current tension)

---

## Duel Etiquette

### Pre-Duel Rituals

**Challenger's Rites**:
1. Announce challenge publicly (witnesses required)
2. State reason for challenge (insult, dispute, test of strength)
3. Offer opponent choice of weapons (honor tradition)
4. Pray to First Forge (bless duel outcome)

**Acceptor's Rites**:
1. Accept challenge publicly (witnesses required)
2. Choose weapon (or accept challenger's choice)
3. Pray to ancestors (honor lineage)
4. Burn offering (ash, ember, or Forge token)

**If Refused**:
1. Challenger brands opponent coward (Coward's Mark applied)
2. Opponent shunned by Crucible (social exile)
3. Opponent's family dishonored (lineage stained)

---

### Post-Duel Rituals

**If Challenger Wins**:
1. Winner honors fallen (if opponent died)
2. Winner claims trophy (weapon, token, or honor)
3. Winner's lineage glorified (recorded in Pack history)

**If Acceptor Wins**:
1. Challenger admits defeat (public acknowledgment)
2. Challenger pays debt (material or service)
3. Challenger's honor intact (losing honorably ≠ shame)

**If Draw** (rare):
1. Both warriors honored (mutual respect)
2. Duel postponed (rematch later)
3. Dispute unresolved (elders mediate)

---

## Duel Mistakes to Avoid

### X Don't Challenge When Low HP

**Problem**: Duel locks you into combat, can't retreat or get healing
**Solution**: Only challenge when healthy (15+ HP recommended)

### X Don't Challenge Tanks

**Problem**: Enemies with 20+ HP take too long to kill, duel wastes turns
**Solution**: Challenge squishy targets (10-15 HP, easy kills)

### X Don't Refuse Duels Lightly

**Problem**: Coward's Mark applies permanently (+2 damage from ALL Crucible)
**Solution**: Accept duels unless guaranteed death (better to lose honorably than be marked)

### X Don't Forget Duel Rewards

**Problem**: Winning duel gives 3 Forge tokens + 3 cards (huge value), but players forget to track
**Solution**: After duel victory, immediately mark +3 tokens and draw 3 cards

### X Don't Duel Without Buffs

**Problem**: Challenging enemy without buffs active = harder fight
**Solution**: Use Duelist's Stance, Pack Fury, or Trial by Fire BEFORE challenging

---

## Honor Duel FAQ

**Q: Can I retreat from Honor Duel?**  
A: No. Duel lasts 1 round (no early exit). Retreating = automatic Coward's Mark.

**Q: Can allies heal me during duel?**  
A: No. Duel is 1v1 (allies can't interfere, even with buffs/heals).

**Q: Can I challenge multiple enemies?**  
A: No. Honor Duel targets 1 enemy (can't multi-challenge).

**Q: What happens if I die in duel?**  
A: You die (normal death rules). No penalty beyond normal death.

**Q: What happens if enemy dies in duel?**  
A: You win. Gain 3 Forge tokens + 3 cards. Duel ends immediately.

**Q: Can non-Crucible use Honor Duel?**  
A: No. Honor Duel is Crucible-exclusive card.

**Q: Can I refuse NPC duel challenges?**  
A: Yes, but gain Coward's Mark (all Crucible NPCs deal +2 damage permanently).

**Q: Does Coward's Mark stack?**  
A: No. Mark is binary (either marked or not).

**Q: Can Coward's Mark be removed?**  
A: No. Permanent for mission duration (no removal).

**Q: Does winning duel restore honor if I'm marked?**  
A: No. Coward's Mark persists even if you win later duels (stain is permanent).

---

**[← Previous: Forge Token Mechanics](forge-token-mechanics.md)** | **[Next: Ancestral Iron →](ancestral-iron.md)**
