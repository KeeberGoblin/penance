# Godot 4.5 Implementation Feasibility Assessment
## Penance: Absolution Through Steel

**Date:** October 19, 2025

---

## Executive Summary

**Complexity Rating: MODERATE (6-8 weeks for solo dev, 3-4 weeks for team)**

**Good News:**
- Card game mechanics are PERFECT for Godot (2D UI-heavy)
- Turn-based combat = no real-time physics complexity
- Hex grid movement = well-documented in Godot
- Deck/hand management = standard card game logic

**Challenges:**
- Component damage system (AP/Structure/Exposure zones) needs custom UI
- Dice rolling with custom symbols (🛡️ ⚔️ 🔥 💔) requires sprite work
- 10 faction-specific mechanics need individual implementations
- AI opponent for single-player

---

## System Breakdown by Complexity

### EASY (Already solved problems in Godot)

**1. Card System (Godot's Control nodes)**
- **Deck/Hand/Discard:** Simple Array management
- **Card display:** TextureRect + Label nodes
- **Drag-and-drop:** Godot's built-in drag system
- **Card animations:** Tween for draw/discard
- **Estimated Time:** 2-3 days

**Implementation:**
```gdscript
extends Node2D
class_name CardGame

var deck: Array[Card] = []
var hand: Array[Card] = []
var discard: Array[Card] = []

func draw_card():
    if deck.size() > 0:
        var card = deck.pop_front()
        hand.append(card)
        emit_signal("card_drawn", card)
```

---

**2. Turn Structure**
- **Phase system:** Simple state machine
- **SP tracking:** Integer variable + UI label
- **Heat tracking:** Same as SP
- **Estimated Time:** 1 day

**Implementation:**
```gdscript
enum Phase { PLANNING, ACTION, END }
var current_phase: Phase = Phase.PLANNING
var sp: int = 6
var heat: int = 0

func next_phase():
    match current_phase:
        Phase.PLANNING:
            current_phase = Phase.ACTION
        Phase.ACTION:
            current_phase = Phase.END
        Phase.END:
            end_turn()
```

---

**3. Hex Grid Movement**
- **Godot has built-in hex grid support** (TileMap or custom hex class)
- **Pathfinding:** AStar2D works with hex grids
- **Line of sight:** Raycasting on hex grid
- **Estimated Time:** 3-4 days

**Implementation:**
```gdscript
class_name HexGrid

const HEX_SIZE = Vector2(64, 56) # Flat-top hexes

func axial_to_pixel(q: int, r: int) -> Vector2:
    var x = HEX_SIZE.x * (3.0/2.0 * q)
    var y = HEX_SIZE.y * (sqrt(3)/2 * q + sqrt(3) * r)
    return Vector2(x, y)

func get_neighbors(hex: Vector2i) -> Array[Vector2i]:
    return [
        Vector2i(hex.x + 1, hex.y),
        Vector2i(hex.x - 1, hex.y),
        Vector2i(hex.x, hex.y + 1),
        Vector2i(hex.x, hex.y - 1),
        Vector2i(hex.x + 1, hex.y - 1),
        Vector2i(hex.x - 1, hex.y + 1)
    ]
```

---

### MODERATE (Requires custom implementation)

**4. Component Damage UI**
- **Visual limb display:** Sprite + damage bars
- **Three-zone system (AP/Structure/Exposure):** Color-coded bars
- **Dynamic tooltips:** Show current zone + penalties
- **Estimated Time:** 4-5 days

**UI Mockup:**
```
┌─────────────────────────────┐
│   CASKET STATUS             │
├─────────────────────────────┤
│  HEAD [██████░░] 6/6 HP     │
│  R.ARM [████████] 8/8 HP    │
│  L.ARM [████████] 8/8 HP    │
│  CHASSIS [██████████] 10/10 │
│  LEGS [████████] 8/8 HP     │
└─────────────────────────────┘
```

**Implementation:**
```gdscript
class_name ComponentDamage extends Control

var component_hp = {
    "head": {"current": 6, "max": 6, "ap": 2, "structure": 4, "exposure": 5},
    "right_arm": {"current": 8, "max": 8, "ap": 3, "structure": 5, "exposure": 6},
    # etc...
}

func get_zone(component: String) -> String:
    var hp = component_hp[component]
    if hp.current <= hp.ap:
        return "AP"
    elif hp.current <= hp.structure:
        return "STRUCTURE"
    elif hp.current <= hp.exposure:
        return "EXPOSURE"
    else:
        return "DESTROYED"

func update_ui():
    for comp in component_hp:
        var bar = get_node("Bars/" + comp)
        bar.value = component_hp[comp].current
        bar.max_value = component_hp[comp].max

        # Color-code by zone
        match get_zone(comp):
            "AP": bar.modulate = Color.GREEN
            "STRUCTURE": bar.modulate = Color.YELLOW
            "EXPOSURE": bar.modulate = Color.RED
            "DESTROYED": bar.modulate = Color.DARK_GRAY
```

---

**5. Defense Dice System**
- **Custom dice sprites:** 6 symbols (🛡️ ⚔️ 🔥 💔 🗡️ ❌)
- **Roll animation:** 3D rotation + bounce
- **Result parsing:** Count symbols, apply effects
- **Estimated Time:** 3-4 days

**Implementation:**
```gdscript
class_name DefenseDice extends Node3D

enum Symbol { SHIELD, CRITICAL, HEAT, FLESH_WOUND, PIERCE, BLANK }

const SYMBOL_SPRITES = {
    Symbol.SHIELD: preload("res://assets/dice/shield.png"),
    Symbol.CRITICAL: preload("res://assets/dice/critical.png"),
    # etc...
}

func roll(num_dice: int) -> Dictionary:
    var results = {"shield": 0, "critical": 0, "heat": 0, "flesh_wound": 0, "pierce": 0}

    for i in range(num_dice):
        var roll = randi() % 6
        var symbol = get_symbol(roll)

        match symbol:
            Symbol.SHIELD: results.shield += 1
            Symbol.CRITICAL: results.critical += 1
            Symbol.HEAT: results.heat += 1
            Symbol.FLESH_WOUND: results.flesh_wound += 1
            Symbol.PIERCE: results.pierce += 1

    return results

func get_symbol(face: int) -> Symbol:
    # Custom distribution per die type
    match face:
        0, 1: return Symbol.SHIELD
        2: return Symbol.CRITICAL
        3: return Symbol.HEAT
        4: return Symbol.FLESH_WOUND
        5: return Symbol.PIERCE
```

---

**6. Faction-Specific Mechanics**
- **10 unique faction systems** (escalation, runes, bleed, etc.)
- **Each needs custom card effects + UI indicators**
- **Script architecture:** Inheritance or composition
- **Estimated Time:** 6-8 days (1 day per faction + refactoring)

**Implementation:**
```gdscript
# Base class
class_name FactionMechanic extends Resource

func on_attack(attacker: Casket, defender: Casket, damage: int) -> int:
    return damage # Default: no modification

# Church subclass
class_name ChurchMechanic extends FactionMechanic

var blood_offering_active: bool = false

func on_attack(attacker: Casket, defender: Casket, damage: int) -> int:
    if blood_offering_active:
        blood_offering_active = false
        return damage + 3 # +3 damage from self-harm
    return damage

func use_blood_offering(attacker: Casket):
    attacker.discard_cards(2) # Self-harm
    blood_offering_active = true

# Dwarves subclass
class_name DwarvesMechanic extends FactionMechanic

var rune_counters: int = 0

func on_take_damage(defender: Casket, damage: int) -> int:
    var reduction = rune_counters * 1
    return max(0, damage - reduction)

func gain_rune():
    rune_counters = min(rune_counters + 1, 2)
```

---

### HARD (Significant engineering)

**7. AI Opponent**
- **Decision tree:** Which card to play, which component to target
- **SP management:** Don't overspend, prioritize attacks
- **Tactical positioning:** Move toward/away from player
- **Difficulty levels:** Easy/Medium/Hard AI
- **Estimated Time:** 7-10 days

**Implementation (Simplified):**
```gdscript
class_name AI extends Node

func choose_action(game_state: GameState) -> Action:
    var actions = get_valid_actions(game_state)

    # Scoring heuristic
    var best_action = null
    var best_score = -INF

    for action in actions:
        var score = evaluate_action(action, game_state)
        if score > best_score:
            best_score = score
            best_action = action

    return best_action

func evaluate_action(action: Action, state: GameState) -> float:
    var score = 0.0

    # Prioritize damaging exposed components
    if action.type == Action.ATTACK:
        var target_zone = state.get_component_zone(action.target_component)
        if target_zone == "EXPOSURE":
            score += 10.0 # High priority!
        elif target_zone == "STRUCTURE":
            score += 5.0

    # Avoid wasting SP
    if action.sp_cost > state.current_sp:
        score -= 100.0 # Invalid!

    return score
```

---

**8. Multiplayer (Optional)**
- **Local multiplayer:** Hot-seat (easy)
- **Online multiplayer:** Godot's high-level networking API
- **Lobby system:** Matchmaking, room codes
- **Estimated Time:** 10-14 days (if implemented)

---

**9. Campaign Mode**
- **Mission progression:** Scenario selection, victory conditions
- **Pilot wounds persistence:** Save system
- **Casket repairs:** Shop/upgrade UI
- **Settlement phase:** Resource management
- **Estimated Time:** 14-21 days

---

## Total Time Estimates

### Minimum Viable Product (MVP - Arena Mode Only)
- Core mechanics (cards, dice, turns): **1 week**
- Component damage system: **1 week**
- Faction mechanics (basic): **1 week**
- Simple AI: **1 week**
- UI/UX polish: **1 week**
- **TOTAL: 5-6 weeks solo dev**

---

### Full Game (Campaign + Multiplayer)
- MVP: **5-6 weeks**
- AI improvements: **1 week**
- Campaign mode: **3 weeks**
- Multiplayer: **2 weeks**
- Art/Audio: **2-3 weeks**
- **TOTAL: 13-15 weeks solo dev**

---

## Asset Requirements

**Minimal (Prototype):**
- Card templates (1 PSD with text fields)
- Hex grid tileset (1 hex tile sprite)
- Component damage UI (5 progress bars)
- Dice sprites (6 symbols × 2 styles = 12 sprites)
- **Time:** 2-3 days for programmer art

**Polished:**
- 200+ unique card arts (or procedurally generated)
- Casket sprites (10 factions × 3 angles = 30 sprites)
- Animated dice rolls (3D models or sprite sheets)
- UI theme (buttons, panels, tooltips)
- Background art (hex grid terrain)
- **Time:** 4-6 weeks for artist

---

## Technology Stack

**Godot 4.5 Built-In:**
- GDScript (or C# if preferred)
- Control nodes for UI (Panel, Label, TextureRect)
- TileMap for hex grid
- Tween for animations
- Signal system for event-driven architecture
- Save/Load system (JSON or binary)

**External (Optional):**
- Nakama for multiplayer backend
- Godot Card Game Framework (open-source template)
- DialogueManager addon (for campaign story)

---

## Recommended Approach

### Phase 1: Core Prototype (2 weeks)
1. **Week 1:** Card system, deck management, basic UI
2. **Week 2:** Dice rolling, damage application, component tracking

**Goal:** Two players can play a full match with basic mechanics

---

### Phase 2: Faction Mechanics (2 weeks)
3. **Week 3:** Implement 5 factions (Church, Dwarves, Elves, Crucible, Nomads)
4. **Week 4:** Implement 5 factions (Ossuarium, Bloodlines, Emergent, Exchange, Wyrd)

**Goal:** All 10 factions playable with unique mechanics

---

### Phase 3: AI & Polish (2 weeks)
5. **Week 5:** Basic AI opponent, difficulty levels
6. **Week 6:** UI/UX polish, animations, sound effects

**Goal:** Single-player mode playable with AI

---

### Phase 4: Campaign (Optional, 3 weeks)
7. **Week 7-9:** Mission structure, settlement phase, pilot wounds persistence

**Goal:** Full campaign mode

---

## Biggest Challenges (Prioritized)

### 1. Component Damage UI Complexity ⚠️
**Problem:** 5 components × 3 zones × 2 players = complex UI state

**Solution:**
- Use Godot's GridContainer for organized layout
- Custom Component resource with signals for damage events
- Real-time tooltips showing zone effects

---

### 2. SCRAP Card System ⚠️
**Problem:** Cards dynamically change function when component destroyed

**Solution:**
```gdscript
class_name Card extends Resource

var original_effect: Callable
var is_scrap: bool = false

func execute_effect(game: GameState):
    if is_scrap:
        # SCRAP universal effect
        game.discard_this_card(self)
        game.draw_card()
    else:
        original_effect.call(game)
```

---

### 3. Dice Variance Balance ⚠️
**Problem:** Defense dice create high variance (lucky rolls = 4× SHIELD)

**Solution:**
- Weighted dice pools (adjust symbol probabilities)
- Playtesting dashboard to track dice outcomes
- **Option:** Use simplified deterministic defense (block X damage) instead of dice

---

### 4. AI Tactical Depth ⚠️
**Problem:** AI needs to understand component damage zones, SP economy, positioning

**Solution:**
- Monte Carlo Tree Search (MCTS) for tactical decisions
- Heuristic scoring (exposed components = high priority)
- Difficulty = search depth (Easy: 1 turn, Hard: 3 turns lookahead)

---

## Demo Scope (1-2 weeks)

**If you want a quick demo to test feasibility:**

**Features:**
- 2 factions (Church vs Dwarves)
- Basic card system (5 cards each)
- Simplified damage (no component zones, just HP)
- No AI (hot-seat 2-player only)
- Minimal UI (text-based)

**This would prove:**
- Card system works
- Faction mechanics distinguishable
- Godot is viable platform
- Core loop is fun

**Time:** 1-2 weeks

---

## Comparison: Godot vs Other Engines

| Feature | Godot 4.5 | Unity | Unreal |
|---------|-----------|-------|--------|
| **2D UI** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Good | ⭐⭐⭐ Okay |
| **Card Games** | ⭐⭐⭐⭐⭐ Perfect | ⭐⭐⭐⭐ Good | ⭐⭐⭐ Overkill |
| **Learning Curve** | ⭐⭐⭐⭐ Easy | ⭐⭐⭐ Medium | ⭐⭐ Hard |
| **Performance** | ⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐⭐ Overkill |
| **Export Targets** | Desktop, Web, Mobile | Desktop, Web, Mobile | Desktop, Consoles |
| **Cost** | FREE (MIT) | FREE (+ Unity fees) | FREE (5% royalty) |

**Verdict:** Godot 4.5 is IDEAL for this project (2D card game, turn-based, no 3D physics)

---

## Prototype Roadmap (If Starting Today)

### Week 1: Foundation
- **Day 1-2:** Project setup, card resource system, deck manager
- **Day 3-4:** Basic UI (hand display, deck counter, SP/Heat)
- **Day 5:** Turn structure state machine
- **Weekend:** Hex grid implementation

### Week 2: Combat
- **Day 8-9:** Damage application, component tracking
- **Day 10-11:** Defense dice system
- **Day 12:** Attack targeting, component selection
- **Weekend:** Playtesting, bug fixes

### Week 3: Factions
- **Day 15-19:** Implement 5 factions (1/day)
- **Weekend:** Polish faction UIs

### Week 4: AI
- **Day 22-24:** Basic AI decision-making
- **Day 25-26:** AI difficulty levels, playtesting
- **Weekend:** Final polish, trailer/screenshots

**By Week 4 end:** Playable demo with 5 factions, AI opponent, arena mode

---

## Risk Assessment

### LOW RISK ✅
- Card system (proven in Godot)
- Turn-based combat (no real-time complexity)
- 2D UI (Godot's strength)

### MEDIUM RISK ⚠️
- Component damage zones (custom UI needed)
- Faction mechanic variety (10 unique systems)
- AI tactical depth (needs tuning)

### HIGH RISK ⛔
- Multiplayer networking (if attempted)
- Campaign persistence (save system complexity)
- Balance (playtesting required)

---

## Conclusion

**Godot 4.5 is HIGHLY SUITABLE for this project.**

**Estimated Solo Dev Time:**
- **Prototype:** 2 weeks
- **MVP (Arena mode):** 6 weeks
- **Full game (Campaign):** 15 weeks

**Recommended First Step:**
Build a 1-week demo with:
- Church vs Dwarves
- 5 cards each
- Basic combat
- Hot-seat multiplayer

This will validate:
1. Godot works for this game type
2. Core mechanics are fun
3. Faction identity feels distinct
4. Project scope is realistic

**Then decide:** Continue in Godot or pivot to different approach

---

**Next Steps:**
1. Set up Godot 4.5 project
2. Create Card resource script
3. Build deck manager scene
4. Prototype first combat encounter

**Would you like me to start building the Godot prototype?**
