# COMBAT RESOLUTION FLOWCHART
**Visual Guide to Attack → Damage Flow**

---

## FULL COMBAT SEQUENCE (Step-by-Step)

```
┌─────────────────────────────────────────────────────┐
│ STEP 1: ATTACKER DECLARES ATTACK                   │
├─────────────────────────────────────────────────────┤
│ • Play attack card from hand (costs SP)            │
│ • Declare target enemy                             │
│ • Declare which component to target:               │
│   - Right Arm (Primary Weapon)                     │
│   - Left Arm (Secondary Equipment)                 │
│   - Legs (Movement)                                │
│   - Head (Sensors)                                 │
│   - Chassis (Core)                                 │
│   - OR Random (roll 1d6)                           │
└─────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────┐
│ STEP 2: CALCULATE TO-HIT NUMBER                    │
├─────────────────────────────────────────────────────┤
│ BASE: 5+ (need to roll 5 or higher on 2d6)        │
│                                                     │
│ ADD PENALTIES (+makes it harder):                  │
│   +1 if attacker moved this turn                   │
│   +1 if defender moved last turn                   │
│   +1 if attacking shield-side or front             │
│   +1 per range band (Medium/Long/Extreme)          │
│   +1 if in light cover                             │
│   +2 if in heavy cover/smoke                       │
│                                                     │
│ SUBTRACT BONUSES (-makes it easier):               │
│   -1 if attacking flank                            │
│   -2 if attacking rear                             │
│   -1 if on high ground                             │
│                                                     │
│ EXAMPLE: 5 (base) +1 (moved) +1 (target moved)    │
│          +1 (medium range) = NEED 8+               │
└─────────────────────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────────┐
│ STEP 3: ROLL 2d6 ATTACK DICE                       │
├─────────────────────────────────────────────────────┤
│ Roll 2 Attack Dice, add results:                   │
│                                                     │
│ ATTACK DIE FACES:                                  │
│   [STRIKE] = 3                                     │
│   [DOUBLE STRIKE] = 4                              │
│   [DEATH BLOW] = 5                                 │
│   [GLANCE] = 1                                     │
│   [JAM] = 0                                        │
│   [BLOOD] = 2                                      │
│                                                     │
│ COMPARE TO TARGET NUMBER:                          │
│   • Below target = MISS (no damage)                │
│   • 5-6 total = HIT (standard damage)              │
│   • 7-8 total = STRONG HIT (+1 damage)             │
│   • 9-10 total = CRITICAL HIT (+2 damage,          │
│                  bypass 1 Defense)                 │
│   • 10 (double DEATH BLOW) = EXECUTION             │
│     (auto-destroy component, bypass ALL Defense)   │
│   • 0 (double JAM) = CATASTROPHIC FAILURE          │
│     (discard Primary Weapon cards, +2 Heat)        │
└─────────────────────────────────────────────────────┘
            ↓
        ┌───┴───┐
        │       │
       MISS    HIT
        │       │
        ↓       ↓
┌───────────┐ ┌─────────────────────────────────────┐
│  ATTACK   │ │ STEP 4: ROLL DEFENSE DICE           │
│   ENDS    │ ├─────────────────────────────────────┤
└───────────┘ │ Roll 1d6 Defense Die PER DAMAGE pt  │
              │                                     │
              │ If attack deals 6 damage:           │
              │   Roll 6 Defense Dice               │
              │                                     │
              │ DEFENSE DIE FACES:                  │
              │   [SHIELD] = Block 1 damage         │
              │   [ABSORB] = Block 1 damage         │
              │   [BLOOD] = Take damage (no effect) │
              │   [CRITICAL] = Take damage +1 CD    │
              │   [HEAT] = Take damage +1 Heat      │
              │   [PIERCE] = Take damage, no React  │
              │                                     │
              │ Count [SHIELD] + [ABSORB]:          │
              │   = Damage reduction                │
              │                                     │
              │ EXAMPLE: 6 damage, roll 6 dice:     │
              │   [SHIELD][SHIELD][BLOOD][CRITICAL] │
              │   [HEAT][PIERCE]                    │
              │   = 2 blocks → 4 final damage       │
              │   + 1 Component Damage              │
              │   + 1 Heat                          │
              │   + Can't use reactive cards        │
              └─────────────────────────────────────┘
                            ↓
              ┌─────────────────────────────────────┐
              │ STEP 5: APPLY FINAL DAMAGE          │
              ├─────────────────────────────────────┤
              │ Defender DISCARDS cards =  damage:  │
              │                                     │
              │ DEFENDER CHOOSES:                   │
              │   • From Hand (lose options)        │
              │   • From Deck Top (risk key cards)  │
              │   • Mixed (some hand, some deck)    │
              │                                     │
              │ EXAMPLE: 4 damage →                 │
              │   Discard 2 from hand + 2 from deck │
              │                                     │
              │ IF DISCARDED PRIMARY WEAPON CARDS:  │
              │   +1 Component Damage per card      │
              └─────────────────────────────────────┘
                            ↓
              ┌─────────────────────────────────────┐
              │ STEP 6: CHECK COMPONENT DAMAGE      │
              ├─────────────────────────────────────┤
              │ Track Component Damage:             │
              │                                     │
              │ SOURCES:                            │
              │   • 1 per Primary Weapon discarded  │
              │   • 1 per [CRITICAL] defense die    │
              │                                     │
              │ 3 COMPONENT DAMAGE = DESTROYED:     │
              │   • Right Arm → Can't use Primary   │
              │   • Left Arm → Can't use Secondary  │
              │   • Legs → Movement +1 SP per hex   │
              │   • Head → -1 to ranged attacks     │
              │   • Chassis → -1 SP maximum         │
              │                                     │
              │ THIS IS THE DEATH SPIRAL            │
              └─────────────────────────────────────┘
                            ↓
              ┌─────────────────────────────────────┐
              │ COMBAT RESOLVED                     │
              └─────────────────────────────────────┘
```

---

## QUICK REFERENCE TABLE

| Roll | Result | Effect |
|------|--------|--------|
| **0** (double JAM) | Catastrophic Failure | Discard Primary cards, +2 Heat, -2 damage next |
| **Below target** | Miss | No damage |
| **5-6** | Hit | Standard damage |
| **7-8** | Strong Hit | +1 damage |
| **9-10** | Critical Hit | +2 damage, bypass 1 Defense |
| **10** (double DEATH BLOW) | Execution | Auto-destroy component, bypass ALL Defense |

---

## COMMON MISTAKES

❌ **Forgetting to calculate ALL modifiers** → Roll wrong target number
❌ **Not tracking Component Damage** → Miss destroyed components
❌ **Discarding Primary Weapon cards carelessly** → Accelerate destruction
❌ **Not using Defense Dice** → Take full damage when you could block

✅ **Remember:**
- Every modifier matters (+1 can mean miss vs hit)
- Component Damage is tracked PER LOCATION
- You CHOOSE how to discard (hand vs deck)
- Defense Dice can save you (or doom you with [CRITICAL])

---

*"Your deck is your life. Every card matters."*
