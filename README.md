# 🏌️ Golf Trip Scoring Web Application

A Flask-based web application for managing golf trip scoring, including individual and team leaderboards, scorecards, and certificate generation. Designed for multi-day golf events with persistent data storage and containerized deployment.

---

## Features

- **Player Management:** Track players and their handicap indexes.
- **Course Management:** Supports multiple courses with hole-by-hole par and stroke index.
- **Scorecard Input:** Enter and save strokes per player per hole for each day.
- **Stableford Scoring:** Automatic calculation of Stableford points based on net scores.
- **Leaderboards:** Live leaderboards for individuals, doubles, and four-player teams.
- **PDF Certificates:** Generate and download achievement certificates for players and teams.
- **Authentication:** Simple password-protected login.
- **Data Persistence:** All data stored in a SQLite database.
- **Responsive UI:** Mobile-friendly HTML/CSS templates.
- **Containerized:** Ready for deployment with Podman or Docker.

---

## Participants

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

## Trip Schedule

| Day | Course  |
|-----|---------|
| 1   | Pasha   |
| 2   | Nobilis |
| 3   | Sultan  |
| 4   | Lykia   |
| 5   | Sultan  |
| 6   | Pasha   |

---

## Stack

- **Backend:** Python 3, Flask, Flask-SQLAlchemy, Flask-Migrate
- **Frontend:** HTML, CSS, JavaScript (with jsPDF and html2canvas for PDF export)
- **Database:** SQLite
- **Containerization:** Podman (or Docker) with `podman-compose`
- **PDF Generation:** reportlab (for backend), jsPDF/html2canvas (for frontend)

---

## Quick Start

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/golf.git
cd golf
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Initialize the database

```sh
flask db upgrade
```

### 4. Run the app (development)

```sh
flask run
```
Or with Gunicorn (recommended for production):
```sh
gunicorn --bind 0.0.0.0:8585 app:app
```

### 5. Access the app

Open your browser to [http://localhost:5000](http://localhost:5000) or the port you specified.

---

## Containerization & Deployment

- Use the provided `Dockerfile` and `podman-compose.yml` for containerized deployment.

### Build and Run with Podman Compose

```sh
podman-compose build --no-cache
podman-compose up -d
```

- The app will be available on port 8585 by default.
- Data is persisted in the `golf_data` volume.

---

## Configuration & Customization

- **Players, teams, and courses:** Update via the database or admin scripts.
- **Course schedule:** Edit `COURSE_MAP` in `app.py`.
- **Team assignments:** Edit `doubles_teams` and `four_teams` in `templates/leaderboard.html`.
- **Course/hole data:** Seeded via `entrypoint.sh` and migrations.
- **App password:** Set `APP_PASSWORD` env variable (default: `golfer123`).
- **Secret key:** Set `SECRET_KEY` env variable (default: `devkey`).

See `Documentation/input.md` for details on updating players, teams, and course details.

---

## License

MIT License

---

## Further Documentation

- For requirements and implementation details, see `Documentation/golf_trip_requirements.md`.