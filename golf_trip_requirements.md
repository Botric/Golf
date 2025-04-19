
# 🏈 Golf Trip Scoring Web Application – Requirements Sheet

## 📌 Overview

This project aims to develop a web application that:

- Displays player information and course details.
- Allows input of individual hole scores.
- Calculates adjusted scores based on handicaps and stroke indices.
- Maintains a live leaderboard for individual and team performances over multiple days.
- Ensures data persistence across sessions.
- Is containerized using Podman for deployment on Fedora.

## 🧑‍💼 Participants

### Players and Handicap Indexes

| Player Name | Handicap Index |
|-------------|----------------|
| Andy P      | 10.9           |
| Joe B       | 13.3           |
| Mark A      | 9.6            |
| Michael D   | 11.4           |
| Steve R     | 19.8           |
| John L      | 22.0           |
| Mark H      | 27.0           |
| Ray H       | 25.8           |

### Doubles Teams

| Team | Player 1  | Player 2 |
|------|-----------|----------|
| Set1 | Andy P    | Mark H   |
| Set2 | Joe B     | John L   |
| Set3 | Michael D | Steve R  |
| Set4 | Mark A    | Ray D    |

### Four-Player Teams

| Team | Player 1  | Player 2 | Player 3  | Player 4 |
|------|-----------|----------|-----------|----------|
| A    | Andy P    | Mark H   | Michael D | Ray D    |
| B    | Mark A    | Joe B    | John L    | Steve R  |

## 🗓️ Trip Schedule

| Day | Course  |
|-----|---------|
| 1   | Pasha   |
| 2   | Nobilis |
| 3   | Sultan  |
| 4   | Lykia   |
| 5   | Sultan  |
| 6   | Pasha   |

## 🏄️‍♂️ Functional Requirements

### 1. Player and Course Display

- Display a list of all players with their Handicap Indexes.
- Provide a selector to choose the day of the trip, which updates the displayed course information accordingly.
- Show course details including Par, Stroke Index (SI), and Hole Number, with the Hole Number prominently displayed at the top.

### 2. Scorecard Input

- For each hole, provide an input box to enter the player's stroke count.
- Ensure the input is validated for numerical correctness.

### 3. Score Calculation

- Calculate the total score for each player, adjusting for Course Handicap and Stroke Index.
- Implement the [Stableford scoring system](https://en.wikipedia.org/wiki/Stableford) or another agreed-upon method for point calculation.

### 4. Leaderboard

- Display a dynamic leaderboard showing:
  - Individual total points across all 3 competition days.
  - Team totals for both doubles and four-player teams.
- Design the leaderboard to be visually appealing and easily interpretable.

### 5. Data Persistence

- Ensure that all entered scores and calculated data are saved persistently.
- Allow users to return to the website at any time and see the latest scores without data loss.

## 💠 Technical Requirements

### Frontend

- Use **HTML**, **CSS**, and **JavaScript** for the frontend development.
- Consider using frameworks like **React** or **Vue.js** for enhanced interactivity.

### Backend

- Implement the backend using **Python** with the **Flask** framework for simplicity and ease of use.
- Alternatively, **Node.js** with **Express** can be used for a JavaScript-based stack.

### Database

- Use **SQLite** for a lightweight, file-based database solution.
- For more scalability, consider **PostgreSQL** or **MySQL**.

### Containerization

- Use **[Podman](https://podman.io/getting-started/installation)** to containerize the application for deployment on Fedora.
- Create a `Dockerfile` (compatible with Podman) to define the container image.
- Use `podman-compose` for managing multi-container setups if needed.

### Hosting

- Host the application on a Fedora server using Podman.
- Ensure proper network configurations to expose the application on the desired ports.

## 🔧 Recommended Technologies

- **Frontend**: HTML, CSS, JavaScript, React or Vue.js.
- **Backend**: Python (Flask) or Node.js (Express).
- **Database**: SQLite, PostgreSQL, or MySQL.
- **Containerization**: Podman.
- **Version Control**: Git.
- **Deployment**: Fedora Server with Podman.

## 📋 Notes

- Ensure that the application is responsive and works well on various devices, including tablets and smartphones.
- Implement user authentication if needed, to restrict access to score editing.
- Consider adding features like score export (e.g., to CSV) for record-keeping.

By following this requirements sheet, you can develop a robust and user-friendly web application to manage and display golf trip scores effectively.
