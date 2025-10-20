#!/usr/bin/env python3
"""
Team combat testing: Multiple caskets vs 1 Colossus
Tests whether smaller caskets working together can take down a Colossus
"""

from combat_simulator import *
import random

class TeamCombatSimulator:
    """Simulates team combat scenarios (multiple vs one)"""

    def __init__(self, team: List[Casket], enemy: Casket, verbose: bool = True):
        self.team = team
        self.enemy = enemy
        self.turn = 0
        self.log = [] if verbose else None
        self.verbose = verbose

    def log_event(self, message: str):
        """Log combat event (only if verbose mode enabled)"""
        if self.verbose:
            self.log.append(f"[Turn {self.turn}] {message}")

    def run_combat(self, max_turns: Optional[int] = None) -> Dict[str, any]:
        """Run team combat simulation

        Args:
            max_turns: Maximum number of turns before forced draw (None = unlimited)
        """
        self.log_event(f"TEAM COMBAT START: {len(self.team)} vs 1")
        for i, casket in enumerate(self.team):
            self.log_event(f"  Team[{i}]: {casket.name} ({casket.hp} HP, {casket.faction})")
        self.log_event(f"  Enemy: {self.enemy.name} ({self.enemy.hp} HP, {self.enemy.faction})")

        # Combat loop
        while self.enemy.is_alive and any(c.is_alive for c in self.team) and (max_turns is None or self.turn < max_turns):
            self.turn += 1

            # Team activations (each team member gets a turn)
            for i, casket in enumerate(self.team):
                if casket.is_alive and self.enemy.is_alive:
                    self.simulate_turn(casket, self.enemy, is_team_member=True, member_index=i)

            # Enemy activation (attacks random living team member)
            if self.enemy.is_alive and any(c.is_alive for c in self.team):
                living_targets = [c for c in self.team if c.is_alive]
                target = random.choice(living_targets)
                target_index = self.team.index(target)
                self.simulate_turn(self.enemy, target, is_team_member=False, member_index=target_index)

        # Determine winner
        winner = None
        team_alive = sum(1 for c in self.team if c.is_alive)

        if team_alive > 0 and not self.enemy.is_alive:
            winner = "Team"
        elif self.enemy.is_alive and team_alive == 0:
            winner = "Colossus"

        self.log_event(f"\n=== COMBAT END ===")
        if winner:
            self.log_event(f"WINNER: {winner}")
            if winner == "Team":
                self.log_event(f"  Team survivors: {team_alive}/{len(self.team)}")
                for i, casket in enumerate(self.team):
                    if casket.is_alive:
                        self.log_event(f"    {casket.name}: {casket.hp} HP remaining")
            else:
                self.log_event(f"  Colossus HP remaining: {self.enemy.hp}")
        else:
            if max_turns and self.turn >= max_turns:
                self.log_event(f"DRAW (turn limit of {max_turns} reached)")
            else:
                self.log_event(f"DRAW (both sides destroyed simultaneously)")

        return {
            "winner": winner if winner else "Draw",
            "turns": self.turn,
            "team_survivors": team_alive,
            "team_total_hp": sum(c.hp for c in self.team if c.is_alive),
            "enemy_hp": self.enemy.hp,
            "log": self.log if self.verbose else []
        }

    def simulate_turn(self, attacker: Casket, defender: Casket, is_team_member: bool, member_index: int):
        """Simulate one turn of combat"""

        # Phase 1: Refresh
        attacker.refresh_sp()
        attacker.draw_cards(3)

        # Check Heat (strain roll if 5+)
        if attacker.heat >= 5:
            strain_roll = random.randint(1, 6)
            if strain_roll <= 3:
                attacker.sp -= 1
                self.log_event(f"{attacker.name} failed Strain roll! -1 SP")

        # Phase 2: Action Phase - Simulate tactical decisions
        self.simulate_attack_phase(attacker, defender, is_team_member, member_index)

        # Phase 3: End phase
        # Bleed damage
        if defender.bleed_counters > 0:
            bleed_dmg = defender.bleed_counters
            defender.take_damage(bleed_dmg)
            self.log_event(f"{defender.name} takes {bleed_dmg} Bleed damage")
            defender.bleed_counters = max(0, defender.bleed_counters - 1)  # BALANCED: -1 decay (reverted)

        # Reduce heat slightly
        attacker.heat = max(0, attacker.heat - 1)

    def simulate_attack_phase(self, attacker: Casket, defender: Casket, is_team_member: bool, member_index: int) -> int:
        """Simulate attack decisions based on faction"""
        total_damage = 0

        # Church: Blood Offering (BUFFED - easier activation)
        if attacker.faction == "church":
            if len(attacker.hand) >= 2 and len(attacker.deck) >= 1:  # BUFFED: 2 instead of 3
                discarded = attacker.deck.popleft()
                attacker.discard.append(discarded)
                attacker._invalidate_hp_cache()
                attacker.blood_offering_bonus = 3
                self.log_event(f"{attacker.name} uses Blood Offering (discards 1 card, +3 damage)")
            else:
                attacker.blood_offering_bonus = 0

            base_damage = 4 + attacker.blood_offering_bonus
            defender.take_damage(base_damage)
            total_damage = base_damage
            attacker.blood_offering_bonus = 0
            self.log_event(f"{attacker.name} attacks {defender.name} for {base_damage} damage")

        # Dwarves: Defensive Runes (BALANCED - cap reduced to 2)
        elif attacker.faction == "dwarves":
            if self.turn % 2 == 0 and attacker.rune_counters < 2:  # BALANCED: cap 2
                attacker.rune_counters += 1
                self.log_event(f"{attacker.name} gains 1 Rune counter (defense, total: {attacker.rune_counters})")

            base_damage = 4
            defender.take_damage(base_damage)
            total_damage = base_damage
            self.log_event(f"{attacker.name} uses Crushing Blow for {base_damage} damage")

        # Ossuarium: Taint Exploitation (v3.0 - gains Taint from damage, spends for lifesteal)
        elif attacker.faction == "ossuarium":
            # Initialize Taint counters
            if not hasattr(attacker, 'taint_counters'):
                attacker.taint_counters = 0

            if attacker.sp >= 3:  # Soul Harvest: 3 SP
                attacker.sp -= 3
                base_damage = 4
                defender.take_damage(base_damage)
                total_damage = base_damage

                # FIXED: Ossuarium gains Taint from damage dealt
                taint_gained = base_damage // 2  # 4 dmg = 2 Taint
                attacker.taint_counters += taint_gained

                # Spend 2 Taint to recover 2 cards
                if attacker.taint_counters >= 2:
                    attacker.taint_counters -= 2
                    cards_recovered = 2
                    for _ in range(cards_recovered):
                        if attacker.discard:
                            recycled = attacker.discard.pop()
                            attacker.hand.append(recycled)
                    attacker._invalidate_hp_cache()
                    self.log_event(f"{attacker.name} uses Soul Harvest (3 SP) for {base_damage} damage, spends 2 Taint to recover {cards_recovered} cards")
                else:
                    self.log_event(f"{attacker.name} uses Soul Harvest (3 SP) for {base_damage} damage, gains {taint_gained} Taint (total: {attacker.taint_counters})")
            else:
                base_damage = 3
                defender.take_damage(base_damage)
                total_damage = base_damage
                self.log_event(f"{attacker.name} attacks {defender.name} for {base_damage} damage")

        # Elves: Bleed stacking (BALANCED - proper stacking with -1 decay)
        elif attacker.faction == "elves":
            base_damage = 2  # BALANCED: 2 instead of 3
            defender.take_damage(base_damage)
            total_damage = base_damage

            defender.bleed_counters = min(defender.bleed_counters + 2, 6)  # BALANCED: +2/cap 6
            self.log_event(f"{attacker.name} attacks {defender.name} for {base_damage} damage, applies 1 Bleed (total: {defender.bleed_counters})")

        # Generic attack for other factions
        else:
            base_damage = 4
            defender.take_damage(base_damage)
            total_damage = base_damage
            self.log_event(f"{attacker.name} attacks {defender.name} for {base_damage} damage")

        return total_damage


def run_team_vs_colossus_test(num_runs: int = 10):
    """Test random team sizes (1-3 caskets) vs 1 Colossus"""

    print("=" * 80)
    print(f"Team Combat Test: 1-3 Random Caskets vs 1 Colossus ({num_runs} runs)")
    print("=" * 80)

    factions = ["church", "dwarves", "ossuarium", "elves", "crucible", "exchange",
                "nomads", "bloodlines", "emergent", "wyrd"]
    classes = [CasketClass.SCOUT, CasketClass.WARDEN, CasketClass.VANGUARD]

    results = {
        "1v1": {"team_wins": 0, "colossus_wins": 0, "draws": 0},
        "2v1": {"team_wins": 0, "colossus_wins": 0, "draws": 0},
        "3v1": {"team_wins": 0, "colossus_wins": 0, "draws": 0}
    }

    for run in range(1, num_runs + 1):
        # Random team size (1-3)
        team_size = random.randint(1, 3)

        print(f"\n[RUN {run}/{num_runs}] {team_size} vs 1 Colossus")
        print("-" * 60)

        # Create random team
        team = []
        for i in range(team_size):
            faction = random.choice(factions)
            casket_class = random.choice(classes)
            casket_name = f"{faction.capitalize()}-{casket_class.value[0]}-{i+1}"
            team.append(create_test_casket(casket_name, faction, casket_class))
            print(f"  Team[{i}]: {casket_name} ({casket_class.value[0]}, {casket_class.value[4]} HP)")

        # Create Colossus enemy
        colossus_faction = random.choice(factions)
        colossus = create_test_casket(f"{colossus_faction.capitalize()}-Colossus", colossus_faction, CasketClass.COLOSSUS)
        print(f"  Enemy: {colossus.name} (Colossus, 60 HP)")

        # Run combat
        combat = TeamCombatSimulator(team, colossus, verbose=False)
        result = combat.run_combat()

        # Record results
        scenario_key = f"{team_size}v1"
        if result["winner"] == "Team":
            results[scenario_key]["team_wins"] += 1
            print(f"  RESULT: Team wins! ({result['team_survivors']}/{team_size} survivors, {result['turns']} turns)")
        elif result["winner"] == "Colossus":
            results[scenario_key]["colossus_wins"] += 1
            print(f"  RESULT: Colossus wins! ({result['enemy_hp']} HP remaining, {result['turns']} turns)")
        else:
            results[scenario_key]["draws"] += 1
            print(f"  RESULT: Draw ({result['turns']} turns)")

    # Generate report
    print("\n" + "=" * 80)
    print("TEAM COMBAT RESULTS SUMMARY")
    print("=" * 80)

    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append(f"Team vs Colossus Combat Report ({num_runs} runs)")
    report_lines.append("=" * 80)
    report_lines.append("")

    for scenario in ["1v1", "2v1", "3v1"]:
        stats = results[scenario]
        total = stats["team_wins"] + stats["colossus_wins"] + stats["draws"]

        if total > 0:
            team_wr = stats["team_wins"] / total * 100
            colossus_wr = stats["colossus_wins"] / total * 100
            draw_rate = stats["draws"] / total * 100

            report_lines.append(f"\n{scenario} Matchups ({total} games):")
            report_lines.append(f"  Team wins:     {stats['team_wins']:3} ({team_wr:5.1f}%)")
            report_lines.append(f"  Colossus wins: {stats['colossus_wins']:3} ({colossus_wr:5.1f}%)")
            report_lines.append(f"  Draws:         {stats['draws']:3} ({draw_rate:5.1f}%)")

    report_lines.append("\n" + "=" * 80)
    report_lines.append("INSIGHTS")
    report_lines.append("=" * 80)

    # Analyze if multiple caskets can beat Colossus
    if results["2v1"]["team_wins"] + results["2v1"]["colossus_wins"] + results["2v1"]["draws"] > 0:
        two_v_one_team_wr = results["2v1"]["team_wins"] / (results["2v1"]["team_wins"] + results["2v1"]["colossus_wins"] + results["2v1"]["draws"]) * 100
        if two_v_one_team_wr > 50:
            report_lines.append(f"\n- 2v1: Team has advantage ({two_v_one_team_wr:.1f}% winrate)")
        else:
            report_lines.append(f"\n- 2v1: Colossus still dominant ({100-two_v_one_team_wr:.1f}% winrate)")

    if results["3v1"]["team_wins"] + results["3v1"]["colossus_wins"] + results["3v1"]["draws"] > 0:
        three_v_one_team_wr = results["3v1"]["team_wins"] / (results["3v1"]["team_wins"] + results["3v1"]["colossus_wins"] + results["3v1"]["draws"]) * 100
        if three_v_one_team_wr > 70:
            report_lines.append(f"- 3v1: Team dominates ({three_v_one_team_wr:.1f}% winrate)")
        elif three_v_one_team_wr > 50:
            report_lines.append(f"- 3v1: Team has advantage ({three_v_one_team_wr:.1f}% winrate)")
        else:
            report_lines.append(f"- 3v1: Colossus still competitive ({100-three_v_one_team_wr:.1f}% winrate)")

    # Print to console
    print("\n" + "\n".join(report_lines))

    # Write to file
    report_path = "C:\\GAMES\\GitHub\\penance\\simulation\\team_combat_report.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\nTeam combat report saved to: {report_path}")
    print("\n" + "=" * 80)
    print("TEAM COMBAT TEST COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    run_team_vs_colossus_test(num_runs=30)  # 30 runs to get good distribution
