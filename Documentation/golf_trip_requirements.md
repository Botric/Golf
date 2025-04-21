# 🏌️ Golf Trip Scoring Web Application – Requirements & Implementation Guide

## 📌 Overview

A web application to manage golf trip scoring, including:

- Player and course management
- Per-hole score input and Stableford calculation
- Live individual and team leaderboards
- Persistent data storage
- Containerized deployment (Podman/Podman Compose)

---

## 🧑‍💼 Participants

### Players and Handicap Indexes

| Player Name | Handicap Index |
|-------------|---------------|
| Andy P      | 10.9          |
| Joe B       | 13.3          |
| Mark A      | 9.6           |
| Michael D   | 11.4          |
| Steve R     | 19.8          |
| John L      | 22.0          |
| Mark H      | 27.0          |
| Ray H       | 25.8          |

### Doubles Teams

| Team | Player 1  | Player 2 |
|------|-----------|----------|
| 1    | Andy P    | Mark H   |
| 2    | Joe B     | John L   |
| 3    | Michael D | Steve R  |
| 4    | Mark A    | Ray D    |

### Four-Player Teams

| Team | Player 1  | Player 2 | Player 3  | Player 4 |
|------|-----------|----------|-----------|----------|
| A    | Andy P    | Mark H   | Michael D | Ray D    |
| B    | Mark A    | Joe B    | John L    | Steve R  |

---

## 🗓️ Trip Schedule

| Day | Course  |
|-----|---------|
| 1   | Pasha   |
| 2   | Nobilis |
| 3   | Sultan  |
| 4   | Lykia   |
| 5   | Sultan  |
| 6   | Pasha   |

---

## 🏄 Functional Requirements

### 1. Player and Course Display

- List all players with Handicap Indexes.
- Select day to update displayed course info.
- Show course details: Par, Stroke Index (SI), Hole Number.

### 2. Scorecard Input

- Input box for each player's strokes per hole.
- Validate input as numeric.

### 3. Score Calculation

- Calculate total and Stableford points per player, adjusting for Course Handicap and SI.

### 4. Leaderboard

- Dynamic leaderboard for:
  - Individual total points (all days)
  - Doubles and four-player team totals
- Visually clear and responsive.

### 5. Data Persistence

- All scores and data saved in SQLite.
- Data persists across sessions and restarts.

---

## 💠 Technical Requirements

### Frontend

- HTML, CSS, JavaScript (with jsPDF/html2canvas for PDF export)
- Responsive design

### Backend

- Python 3, Flask, Flask-SQLAlchemy, Flask-Migrate

### Database

- SQLite (default, file-based)

### Containerization & Deployment

- Podman (or Docker) for containerization
- `podman-compose` for orchestration

#### **Build and Run with Podman Compose**

```sh
podman-compose build --no-cache
podman-compose up -d
```

- The app will be available on port 8585 by default.
- Data is persisted in the `golf_data` volume.

---

## 🛠️ Customization & Configuration

- **Players, teams, and courses:** Update via the database or admin scripts.
- **Course schedule:** Edit `COURSE_MAP` in `app.py`.
- **Team assignments:** Edit `doubles_teams` and `four_teams` in `templates/leaderboard.html`.
- **Course/hole data:** Seeded via `entrypoint.sh` and migrations.
- **App password:** Set `APP_PASSWORD` env variable (default: `golfer123`).
- **Secret key:** Set `SECRET_KEY` env variable (default: `devkey`).

See `Documentation/input.md` for details on updating players, teams, and course details.

---

## 📋 Notes

- The application is responsive and works on desktop and mobile.
- User authentication restricts score editing.
- PDF certificates can be generated for players and teams.
- For deployment with SSL and a custom domain, see `Documentation/deploy_golf_botric_subdomain.md`.

---

By following this guide and the provided scripts, you can deploy, customize, and operate a robust golf trip scoring web application.
