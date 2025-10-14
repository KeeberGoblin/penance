# Pilot Grit System
## Penance: Absolution Through Steel

**Version**: 3.0 (Trench Crusade Resilience-Inspired)
**Last Updated**: October 14, 2025

---

## Overview

Inspired by Trench Crusade's resilience mechanics, the **Pilot Grit** system represents a pilot's mental toughness, pain tolerance, and ability to shrug off injuries through sheer willpower. Veterans develop an iron resolve that lets them "tough it out" when lesser pilots would break.

**Core Concept**:
- Pilots have a **Grit stat** (0-3, increases with experience)
- When taking Pilot Damage, roll **1d6 + Grit** to resist Wound cards
- Higher Grit = better chance to shrug off injuries
- Creates campaign progression (veterans ARE mechanically tougher)

---

## Grit Stat

### Starting Grit: 0

**New pilots start with Grit 0** (untested, fragile).

---

### Maximum Grit: 3

**Veteran pilots cap at Grit 3** (battle-hardened, nearly unbreakable).

---

### Grit Progression Table

| Grit | Description | Requirements |
|------|-------------|--------------|
| **0** | Untested | Starting pilot, 0-4 missions survived |
| **1** | Seasoned | 5 missions survived |
| **2** | Hardened | 10 missions survived OR 1 Severe Injury survived |
| **3** | Iron Will | 20 missions survived OR 3 Severe Injuries survived |

---

## Grit Checks

### When Do You Roll Grit?

**WHEN PILOT TAKES DAMAGE** (before flipping Wound card):
- Capsule Breach (enemy targets capsule)
- Neural Feedback (5+ Component Damage accumulated)
- Thread Snap (Hand Thread cards damaged)
- Taint Overload (10+ Taint Corruption)
- Casket Destruction (Casket HP reaches 0, pilot must save)

**PROCEDURE**:
1. Trigger occurs (e.g., Neural Feedback from 5 Component Damage)
2. **Roll 1d6 + Pilot's Grit stat**
3. Compare to Grit Check Table (see below)
4. Apply result (flip Wound card, reduce severity, or shrug it off)

---

### Grit Check Results Table

**Roll 1d6 + Grit, compare to this table**:

| Result | Effect | Description |
|--------|--------|-------------|
| **1-3** | **Full Wound** | Flip Wound card normally (no reduction) |
| **4-5** | **Tough It Out** | Flip Wound card, but treat Severe as Minor this mission |
| **6-7** | **Shrug It Off** | Don't flip Wound card, gain 1 Heat instead (adrenaline surge) |
| **8+** | **Iron Will** | Don't flip Wound card, no penalty (pure willpower) |

---

### Example Grit Checks

**EXAMPLE 1: Rookie Pilot (Grit 0)**
```
SITUATION: Neural Feedback triggered (5 Component Damage)
ROLL: 1d6 + 0 Grit = 3
RESULT: Full Wound (flip Wound card normally)
WOUND FLIPPED: Severe Injury - Shattered Hand (-2 SP permanent)
OUTCOME: Rookie suffers full permanent injury
```

**EXAMPLE 2: Seasoned Pilot (Grit 1)**
```
SITUATION: Capsule Breach (enemy targeted capsule directly)
ROLL: 1d6 + 1 Grit = 5
RESULT: Tough It Out (flip Wound, but Severe → Minor)
WOUND FLIPPED: Severe Injury - Spinal Trauma (would be permanent -1 SP movement)
DOWNGRADE: Treated as Minor Injury - Dislocated Shoulder (-2 damage until end of mission)
OUTCOME: Seasoned pilot avoids permanent injury, temporary debuff only
```

**EXAMPLE 3: Hardened Pilot (Grit 2)**
```
SITUATION: Taint Overload (reached 10 Taint, failed Corruption Save)
ROLL: 1d6 + 2 Grit = 6
RESULT: Shrug It Off (don't flip Wound, gain 1 Heat instead)
OUTCOME: Hardened pilot grits teeth, ignores corruption damage, Casket overheats slightly
```

**EXAMPLE 4: Iron Will Pilot (Grit 3)**
```
SITUATION: Casket Destruction (HP deck reached 0, pilot must save)
ROLL: 1d6 + 3 Grit = 9 (rolled a 6!)
RESULT: Iron Will (no penalty, pure willpower)
OUTCOME: Veteran pilot REFUSES to die. Casket is wrecked but pilot unblemished. Extracted safely.
```

---

## Gaining Grit

### Mission Survival (Passive Progression)

**After each mission, check Grit progression**:

| Missions Survived | Grit Level |
|-------------------|------------|
| 0-4 missions | Grit 0 (Untested) |
| 5-9 missions | Grit 1 (Seasoned) |
| 10-19 missions | Grit 2 (Hardened) |
| 20+ missions | Grit 3 (Iron Will) |

**"Mission Survived" = Pilot extracted alive (even if Casket destroyed).**

---

### Injury-Based Progression (Fast-Track)

**Surviving trauma accelerates Grit growth**:

**Gain +1 Grit immediately when**:
- Survive 1st Severe Injury → Gain Grit 1 (even if under 5 missions)
- Survive 3rd Severe Injury → Gain Grit 2 (even if under 10 missions)
- Survive 5th Severe Injury → Gain Grit 3 (veteran of pain)

**Why This Exists**: Pilots who survive horrific injuries become tougher faster. A pilot with 2 missions but 1 Severe Injury is Grit 1 (trauma-hardened).

---

### Leg-Skimming Grit Bonus

**If pilot has Leg-Skimmed** (permanent soul sacrifice):
- **+1 Grit permanently** (traded soul for willpower)
- Stacks with mission/injury progression
- Max Grit still 3 (but easier to reach)

**Example**: Pilot with 3 missions Leg-Skims (+1 Grit). Now at Grit 1 without needing 5 missions.

---

### Trauma Grit Penalty

**If pilot has Trauma Wound card flipped** (PTSD, Dissociation):
- **-1 Grit on all Grit Checks** (mental instability)
- Does NOT reduce Grit stat (still shows as Grit 2 on sheet)
- Only applies to Grit Check rolls

**Example**: Grit 2 pilot with PTSD rolls 1d6 + 2 - 1 = 1d6 + 1 effective Grit.

---

## Faction Grit Modifiers

### Church of Absolution
**Martyrdom Training**: Church pilots start with **+1 Grit at character creation** (zealot conditioning)
- Starting Grit: 1 (instead of 0)
- Max Grit: Still 3 (but reach it faster)
- Flavor: "Pain is prayer. We are chosen to suffer."

---

### Dwarven Forge-Guilds
**Stoic Endurance**: Dwarven pilots gain **+1 to Grit Checks vs Severe Injuries** (not Minor or Trauma)
- Still roll normal Grit, but +1 when resisting Severe only
- Flavor: "Stone does not break. Neither do we."

---

### The Ossuarium
**Already Dead**: Ossuarium pilots are IMMUNE to Grit Checks (they don't flip Wound cards)
- Instead, they use "Decay Card" system (see Ossuarium faction rules)
- Flavor: "We died once. What's one more wound?"

---

### Elven Verdant Covenant
**Fragile Immortals**: Elven pilots have **-1 Grit at all times** (emotionally brittle)
- Can still gain Grit through missions, but always -1 penalty
- Max effective Grit: 2 (3 Grit - 1 penalty)
- Flavor: "We are ageless, not invincible. Pain is... unfamiliar."

---

## Grit in Play Examples

### Scenario 1: Rookie vs Veteran

**ROOKIE PILOT (Grit 0)**:
- Takes Neural Feedback damage
- Rolls 1d6 + 0 = 3 → Full Wound
- Flips Severe Injury: Ruptured Organ (permanent -5 HP per mission)
- **Outcome**: Crippled permanently, may retire

**VETERAN PILOT (Grit 3)**:
- Takes same Neural Feedback damage
- Rolls 1d6 + 3 = 8 → Iron Will
- No Wound flipped, no penalty
- **Outcome**: Shakes it off, keeps fighting

**This creates mechanical power creep for veterans (intentional KDM-style progression).**

---

### Scenario 2: Church Zealot Embracing Pain

**CHURCH PILOT (Starting Grit 1, Martyrdom Training)**:
- Mission 1: Takes Capsule Breach
- Rolls 1d6 + 1 = 4 → Tough It Out (Severe → Minor)
- Flips Minor Injury: Broken Finger (temporary debuff)
- **Outcome**: Zealot endures pain, praises suffering, continues mission

---

### Scenario 3: Elven Pilot Shattering

**ELVEN PILOT (Grit 2, -1 penalty = effective Grit 1)**:
- Takes Thread Snap damage
- Rolls 1d6 + 1 = 2 → Full Wound
- Flips Trauma: PTSD (cannot attack from behind)
- Now has -2 total Grit penalty (Elven -1, PTSD -1)
- **Outcome**: Elven fragility leads to mental breakdown

---

## Campaign Grit Tracking

### Pilot Sheet Example

```
PILOT: Gareth "Ironside" Kade
FACTION: Dwarven Forge-Guilds
MISSIONS SURVIVED: 12
SEVERE INJURIES SURVIVED: 2
LEG-SKIMMED: No
TRAUMA WOUNDS: 0

GRIT CALCULATION:
Base Grit (12 missions): 2
Severe Injuries (2): +0 (doesn't boost Grit)
Leg-Skimmed: +0 (not skimmed)
Trauma Penalty: +0 (no trauma)
Faction Bonus: +1 to Grit Checks vs Severe Injuries only

FINAL GRIT: 2
EFFECTIVE GRIT VS SEVERE: 3 (2 + 1 Dwarven bonus)
```

---

## Strategic Implications

### High-Grit Pilots Are More Valuable

**In campaign, protect your veterans**:
- Grit 3 pilots are MUCH harder to permanently injure
- 50% chance to ignore Pilot Damage (rolls 6+ on 1d6+3)
- Worth investing in extraction/rescue if they go down

---

### Rookies Are Expendable

**Low-Grit pilots are glass cannons**:
- 83% chance to take Full Wound (need 4+ on 1d6+0)
- High risk of permanent injury early
- Some factions "churn through" rookies intentionally (Church martyrs)

---

### Leg-Skimming for Grit

**Trade soul for survivability**:
- Leg-Skim early (gain +1 Grit immediately)
- Combine with mission progression for Grit 2 by mission 8 (instead of mission 10)
- Risk: Permanent soul damage, reduced max HP

---

## Advanced Rules: Grit Synergies

### Grit + Taint Exploitation

**High Grit helps resist Taint Overload**:
- When you reach 10 Taint, roll Corruption Save (1d6, need 4+)
- **VARIANT RULE**: Add Grit to Corruption Save roll
  - Grit 0: Roll 1d6, need 4+ (50% chance)
  - Grit 3: Roll 1d6+3, need 4+ (83% chance to resist)

**Why**: Veteran pilots have stronger willpower to resist Engine corruption.

---

### Grit + Pilot Progression

**Scars grant Grit**:
- Some Pilot Scars (see pilot-progression.md) grant +1 Grit
- Example: "Battle-Scarred" scar (survived 3 near-deaths) → +1 Grit
- Stacks with mission/injury progression

---

### Grit + Support Units

**High-Grit pilots command better**:
- Support Units (see support-units.md) gain +1 Morale if commanded by Grit 2+ pilot
- Represents veteran's leadership inspiring troops
- Mechanical benefit: Support Units less likely to flee

---

## Playtesting Notes

### If Grit Makes Pilots Too Tough:
- Increase thresholds (Shrug It Off at 7-8 instead of 6-7)
- Remove faction bonuses (Church doesn't start with +1 Grit)
- Cap Grit at 2 (no Grit 3)

### If Pilots Die Too Easily:
- Lower thresholds (Tough It Out at 3-4 instead of 4-5)
- Grant +1 Grit at 3 missions (instead of 5)
- Add more Grit sources (equipment grants +1 Grit)

### If Grit Feels Irrelevant:
- Increase Pilot Damage frequency (more chances to roll Grit)
- Add more triggers (Grit Check when taking 10+ Casket damage)
- Make Wound cards harsher (so avoiding them matters more)

### If Faction Modifiers Are Unbalanced:
- Remove Ossuarium immunity (they still use Grit, just harder Checks)
- Reduce Church bonus to +0 starting Grit (instead of +1)
- Change Elven penalty to -1 vs Trauma only (not all Checks)

---

## Designer's Notes

### Why Grit Works

1. **Campaign Progression**: Veterans feel mechanically superior (not just narrative)
2. **Risk/Reward**: Rookies are fragile but cheap, veterans are tough but irreplaceable
3. **Faction Flavor**: Church embraces pain, Dwarves endure, Elves shatter, Ossuarium transcend
4. **Trench Crusade Inspiration**: Blood Marker shaking creates similar "tough it out" moments

### Differences from Trench Crusade

**Trench Crusade**:
- Models can spend actions to shake off Blood Markers (active choice)
- Binary: Either marked or not

**Penance Grit**:
- Passive stat that grows with experience (not active choice)
- Rolled reactively when damage occurs
- Threshold-based: Different results at 4, 6, 8 (gradations of success)

---

## FAQ

**Q: Can I boost Grit mid-mission?**
A: No. Grit is a campaign stat, only changes between missions. (Unless card/equipment says otherwise.)

**Q: If I roll an 8 with Grit 3, is that Iron Will or just Shrug It Off?**
A: Iron Will (8+ = no penalty). Shrug It Off is 6-7 (gain 1 Heat).

**Q: Do I roll Grit for each point of Pilot Damage?**
A: Yes. If you take 3 Pilot Damage (e.g., Capsule Breach + Neural Feedback + Thread Snap), roll 3 separate Grit Checks (could flip 0-3 Wound cards depending on rolls).

**Q: Can Grit reduce Minor Injuries to nothing?**
A: No. Shrug It Off (6-7) and Iron Will (8+) prevent Wound flip entirely. Tough It Out (4-5) only reduces Severe → Minor. Minors stay Minor.

**Q: What if I have Grit 3 + Leg-Skimmed +1 Grit bonus?**
A: Max Grit is still 3. Bonuses help you REACH 3 faster, but don't exceed cap. (Unless GM houserules "Legendary Grit 4.")

**Q: Do Trauma penalties stack?**
A: Yes. If you flip 2 Trauma cards (PTSD + Dissociation), you have -2 Grit on all Checks.

**Q: Can I train Grit at settlements?**
A: Not in base rules. Grit is earned through survival, not training. (GMs may houserule "Meditation Training" for +1 Grit, costs 500 Credits.)

**Q: Does Grit help with Casket HP damage?**
A: No. Grit only applies to PILOT damage (Wound cards). Casket damage (discarding cards from HP deck) is separate.

---

## Quick Reference: Grit Check Procedure

**WHEN PILOT TAKES DAMAGE:**

1. **Identify Trigger**: Capsule Breach, Neural Feedback, Thread Snap, Taint Overload, or Casket Destruction
2. **Roll 1d6 + Pilot's Grit stat**
3. **Compare to Table**:
   - 1-3: Full Wound (flip normally)
   - 4-5: Tough It Out (Severe → Minor)
   - 6-7: Shrug It Off (no flip, +1 Heat)
   - 8+: Iron Will (no flip, no penalty)
4. **Apply Result**: Flip Wound card (or don't), apply penalties, continue

---

**GRIT PROGRESSION:**

- **0 Missions**: Grit 0
- **5 Missions**: Grit 1
- **10 Missions**: Grit 2
- **20 Missions**: Grit 3

**FAST-TRACK:**
- 1 Severe Injury survived: Grit 1
- 3 Severe Injuries survived: Grit 2
- 5 Severe Injuries survived: Grit 3

**BONUSES:**
- Leg-Skimmed: +1 Grit (permanent)
- Church Faction: +1 Starting Grit

**PENALTIES:**
- Trauma Wound: -1 Grit per Trauma
- Elven Faction: -1 Grit (always)

---

**END OF DOCUMENT**

---

*"Grit is not given. It is earned. In blood. In pain. In refusing to break when the universe demands it."*
