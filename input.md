# Golf App: How to Update Players, Teams, and Course Details

This guide explains where to update player names, team assignments, course stats, handicaps (HCP), and stroke index (SI) in your Golf app.

---

## 1. Player Names & Points

**File:** `leaderboard.html` (and likely your backend data source)

- Player names and their points are listed in the `leaderboard` variable.
- To change player names or points, update the data source that populates `leaderboard` (e.g., your Python backend or database).

**Example in leaderboard.html:**
```jinja
{% for name, pts in leaderboard|sort(attribute=1, reverse=True) %}
  <tr>
    <td>{{ name }}</td>
    <td>{{ pts }}</td>
    ...
  </tr>
{% endfor %}
```
_Update the `leaderboard` variable in your backend to change names or points._

---

## 2. Team Assignments

### Doubles Teams

**File:** `leaderboard.html`

- Doubles teams are defined in a list called `doubles_teams`.

```jinja
{% set doubles_teams = [
  (1, 'Andy P', 'Mark H'),
  (2, 'Joe B', 'John L'),
  (3, 'Michael D', 'Steve R'),
  (4, 'Mark A', 'Ray D')
] %}
```
_Edit this list to change team members or add/remove teams._

### Four-Player Teams

**File:** `leaderboard.html`

- Four-player teams are defined in a list called `four_teams`.

```jinja
{% set four_teams = [
  ('A', 'Andy P', 'Mark H', 'Michael D', 'Ray D'),
  ('B', 'Mark A', 'Joe B', 'John L', 'Steve R')
] %}
```
_Edit this list to change team members or add/remove teams._

---

## 3. Course Stats, HCP, and SI

**File:** _Check your project for a file like_ `scorecard.html`, `course.py`, or a similar backend file.

- Course stats (hole pars, lengths, etc.), HCP (handicap), and SI (stroke index) are usually defined in a data structure in your backend or in a scorecard template.

**Example (Python):**
```python
holes = [
    {"number": 1, "par": 4, "hcp": 10, "si": 12, "length": 350},
    {"number": 2, "par": 3, "hcp": 18, "si": 16, "length": 150},
    # ... more holes ...
]
```
_Edit this data structure to update course stats, HCP, or SI for each hole._

---

## 4. Summary Table

| What to Change      | Where to Edit                |
|---------------------|-----------------------------|
| Player Names/Points | Backend data source (`leaderboard`) |
| Doubles Teams       | `doubles_teams` in `leaderboard.html` |
| Four-Player Teams   | `four_teams` in `leaderboard.html`    |
| Course Stats/HCP/SI | Backend or scorecard file (e.g., `scorecard.html` or Python data) |

---

**Tip:**  
Always restart your backend server after making changes to Python files or data sources to see updates reflected in the app.
