# Contributing to Penance: Absolution Through Steel

Thank you for your interest in contributing to Penance! This document provides guidelines for contributing to this tabletop game design project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Process](#development-process)
- [Style Guides](#style-guides)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)

---

## Code of Conduct

This project adheres to a code of mutual respect and constructive collaboration. By participating, you are expected to uphold this standard. Please report unacceptable behavior by opening an issue.

---

## How Can I Contribute?

### 1. Playtesting & Feedback

**Most Valuable Contribution!**

- Play the game using the [Playtest Kit](/playtest-kit/)
- Report balance issues, unclear rules, or gameplay problems
- Share battle reports and session summaries
- Use the **Playtest Feedback** issue template

### 2. Rules & Documentation

- Fix typos, grammatical errors, or unclear wording
- Improve rule explanations with examples
- Add cross-references between related rules
- Update outdated documentation

### 3. Card Balance & Design

- Propose new cards or equipment
- Suggest balance adjustments with supporting data
- Run simulations using `/simulation/faction_balance_MULTIUNIT.py`
- Provide statistical analysis

### 4. Interactive Tools

- Improve the [Card Browser](/docs/cards/index.html)
- Enhance the [Deck Builder](/docs/cards/deck-builder.html)
- Fix bugs in the [Pilot Generator](/docs/tools/pilot-generator.html)
- Add new features to web tools

### 5. Lore & World-Building

- Expand faction histories
- Create new NPCs or locations
- Ensure consistency with existing canon (check `docs/lore/`)
- Follow the established grimdark tone

### 6. Code & Utilities

- Fix bugs in Python simulation scripts
- Improve PDF generation (`tools/generate-pdfs.py`)
- Optimize card database loading
- Add error handling

---

## Development Process

### Setting Up Your Environment

#### Prerequisites

- **Python 3.8+** (for simulation and utilities)
- **Modern web browser** (for interactive tools)
- **Git** (for version control)

#### Installation

```bash
# Clone the repository
git clone https://github.com/KeeberGoblin/penance.git
cd penance

# Install Python dependencies (if any)
pip install -r requirements.txt  # Optional: WeasyPrint for PDFs

# Test the card browser locally
cd docs/cards
python3 -m http.server 8000
# Visit http://localhost:8000/index.html
```

### Branch Naming Convention

- `feature/your-feature-name` - New features
- `fix/issue-description` - Bug fixes
- `docs/what-changed` - Documentation updates
- `balance/faction-name` - Balance adjustments

### Making Changes

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/my-awesome-feature
   ```

2. **Make your changes** following the style guides below

3. **Test your changes**:
   - For rules: Review against existing documentation
   - For code: Run simulations or test web tools locally
   - For balance: Use `/simulation/faction_balance_MULTIUNIT.py`

4. **Commit with clear messages**:
   ```bash
   git add .
   git commit -m "Add Nomad faction equipment cards

   - Added 3 new equipment items for Nomads
   - Balanced costs against existing equipment
   - Updated complete-card-data.json"
   ```

---

## Style Guides

### Markdown Documentation

- Use **sentence case** for headings (not Title Case)
- Use `**bold**` for emphasis, `*italics*` for game terms
- Include examples for complex rules
- Keep line length under 120 characters
- Add blank lines between sections

**Example:**
```markdown
## Component damage system

When a **DAMAGED** card is drawn, it is immediately moved to the *graveyard* instead of your hand.

**Example:** You draw *Desperate Lunge (DAMAGED)*. It goes directly to your graveyard without entering your hand.
```

### Python Code Style

Follow **PEP 8** with these specifics:

- **Indentation:** 4 spaces
- **Line length:** 100 characters max
- **Naming:**
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants

```python
# Good
def calculate_win_rate(battles: int, wins: int) -> float:
    """Calculate win rate percentage."""
    return (wins / battles) * 100

# Bad
def CalculateWinRate(b,w):
    return (w/b)*100
```

### JavaScript Code Style

- **Indentation:** 2 spaces
- **Semicolons:** Use them
- **Naming:**
  - `camelCase` for functions and variables
  - `PascalCase` for classes
  - Descriptive names (not `x`, `y`, `temp`)

```javascript
// Good
function renderCardGrid(cards) {
  const container = document.getElementById('cardGrid');
  container.innerHTML = cards.map(card => generateCardHTML(card)).join('');
}

// Bad
function render(c){
  let x=document.getElementById('cardGrid')
  x.innerHTML=c.map(y=>gen(y)).join('')
}
```

### Card Data Format

When adding cards to `complete-card-data.json`:

```json
{
  "id": "unique-kebab-case-id",
  "name": "Card Name",
  "type": "Attack|Defense|Movement|Utility",
  "cost": 2,
  "range": "Range 1|Range 2|Melee|Self",
  "effect": "Clear, concise effect text.",
  "damage": 4,  // Optional
  "heat": 1,    // Optional
  "keywords": ["keyword1", "keyword2"]  // Optional
}
```

### Git Commit Messages

- **First line:** Imperative mood, < 50 chars (e.g., "Add X", "Fix Y", "Update Z")
- **Body:** Explain *why*, not *what* (code shows what)
- **Reference issues:** Use `Fixes #123` or `Relates to #456`

```
Add Taint exploitation mechanic (v3.0 optional rule)

Allows players to spend Taint for temporary power boosts.
Encourages risk/reward gameplay in desperate situations.

Relates to #42
```

---

## Pull Request Process

### Before Submitting

- [ ] I have tested my changes locally
- [ ] I have followed the style guides
- [ ] I have updated documentation if needed
- [ ] I have checked for merge conflicts
- [ ] My commit messages are clear and descriptive

### Submitting

1. **Push your branch** to GitHub:
   ```bash
   git push -u origin feature/my-awesome-feature
   ```

2. **Open a Pull Request** with:
   - **Title:** Clear summary (e.g., "Add Church faction equipment")
   - **Description:** Use the PR template (explain changes, testing done)
   - **Link related issues:** `Fixes #123` or `Closes #456`

3. **Respond to feedback**:
   - Address review comments promptly
   - Make requested changes in new commits
   - Mark conversations as resolved when fixed

### PR Review Criteria

Your PR will be reviewed for:

- **Functionality:** Does it work as intended?
- **Balance:** Does it maintain game balance? (for game content)
- **Code quality:** Is it readable and maintainable?
- **Documentation:** Are changes documented?
- **Testing:** Have you tested it?

---

## Testing

### Testing Rules Changes

1. **Read your change aloud** - Does it make sense?
2. **Check examples** - Do they match the rule?
3. **Cross-reference** - Does it contradict other rules?
4. **Playtest** - Try it in actual gameplay

### Testing Code Changes

#### For Web Tools (HTML/JavaScript)

```bash
# Serve files locally
cd docs/cards  # or docs/tools
python3 -m http.server 8000

# Test in browser
# Visit http://localhost:8000/index.html
```

#### For Python Scripts

```bash
# Test simulation
cd simulation
python3 faction_balance_MULTIUNIT.py

# Test card database validation
cd utilities
python3 validate-card-database.py
```

#### For Card Balance

```bash
# Run combat simulator with your changes
cd simulation
python3 faction_balance_MULTIUNIT.py

# Check win rates - should be 45-55% ideally
# Outliers beyond 40-60% need review
```

---

## Questions?

- **Rules questions:** Open an issue with the "Question" label
- **Bug reports:** Use the "Bug" issue template
- **Feature requests:** Use the "Feature Request" template
- **General discussion:** Start a GitHub Discussion

---

## Attribution

Contributors will be acknowledged in the project README. By contributing, you agree that your contributions will be licensed under the project's **CC BY-NC-SA 4.0** license.

---

**Thank you for contributing to Penance!** Your help makes this grimdark world of mech combat even more brutal and balanced.
