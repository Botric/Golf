from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_migrate import Migrate
from models import db, Player, Course, Hole, Score
from config import Config
import io
from reportlab.pdfgen import canvas
from datetime import datetime, timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

COURSE_MAP = {1:1, 2:2, 3:3, 4:4, 5:3, 6:1}

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    # Check for lockout
    lockout_until = session.get('lockout_until')
    if lockout_until:
        # Convert string to datetime if needed
        if isinstance(lockout_until, str):
            lockout_until = datetime.fromisoformat(lockout_until)
        if datetime.utcnow() < lockout_until:
            remaining = int((lockout_until - datetime.utcnow()).total_seconds() // 60) + 1
            error = f"Too many failed attempts. Try again in {remaining} minute(s)."
            return render_template('login.html', error=error)
        else:
            session.pop('lockout_until', None)
            session.pop('login_attempts', None)

    if request.method == 'POST':
        if request.form.get('password') == Config.APP_PASSWORD:
            session['logged_in'] = True
            session.pop('login_attempts', None)
            session.pop('lockout_until', None)
            return redirect(url_for('scorecard'))
        else:
            # Track failed attempts
            attempts = session.get('login_attempts', 0) + 1
            session['login_attempts'] = attempts
            if attempts >= 5:
                lockout_time = datetime.utcnow() + timedelta(minutes=5)
                session['lockout_until'] = lockout_time.isoformat()
                error = "Too many failed attempts. Try again in 5 minutes."
            else:
                error = f"Invalid password. {5 - attempts} attempt(s) left."
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/leaderboard')
def leaderboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    data = []
    players = Player.query.order_by(Player.name).all()
    for p in players:
        total = db.session.query(db.func.sum(Score.points)).filter(
            Score.player_id==p.id,
            Score.strokes > 0
        ).scalar() or 0
        data.append((p.name, total))
    data.sort(key=lambda x: x[1], reverse=True)
    return render_template('leaderboard.html', leaderboard=data)

@app.route('/certificate/<int:player_id>')
def certificate(player_id):
    player = Player.query.get_or_404(player_id)
    total = db.session.query(db.func.sum(Score.points)).filter(Score.player_id==player.id).scalar() or 0
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=(600,400))
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(300,350, "Certificate of Achievement")
    c.setFont("Helvetica", 18)
    c.drawCentredString(300,300, f"{player.name}")
    c.drawCentredString(300,260, f"Total Stableford Points: {total}")
    c.showPage()
    c.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True,
                     download_name=f"{player.name}_certificate.pdf",
                     mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, redirect, url_for, render_template
from models import Course, Hole, Player, Score, db
from utils import compute_course_handicap

@app.route('/', methods=['GET', 'POST'])
@app.route('/scorecard', methods=['GET', 'POST'])
def scorecard():
    # Require login
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    day = int(request.args.get('day', 1))
    course = Course.query.get(COURSE_MAP[day])
    holes = Hole.query.filter_by(course_id=course.id).order_by(Hole.hole_number).all()
    players = Player.query.order_by(Player.name).all()

    # Compute each player’s Course HCP
    for p in players:
        p.course_hcp = compute_course_handicap(p.handicap_index, course.slope)

    # Build a dict of {(player_id, hole_id): strokes}
    scores = {(s.player_id, s.hole_id): s.strokes for s in Score.query.filter_by(day_number=day).all()}

    if request.method == 'POST':
        for p in players:
            for h in holes:
                key = f"strokes-{p.id}-{h.id}"
                val = request.form.get(key)
                if val is not None and val != '':
                    strokes = int(val)
                    existing_score = Score.query.filter_by(player_id=p.id, hole_id=h.id, day_number=day).first()
                    if strokes == 0:
                        if existing_score:
                            db.session.delete(existing_score)
                    else:
                        # Calculate Stableford points
                        net_strokes = strokes - p.course_hcp // len(holes)  # crude per-hole allocation
                        points = max(0, 2 + (h.par - net_strokes))
                        if existing_score:
                            existing_score.strokes = strokes
                            existing_score.points = points
                        else:
                            score = Score(player_id=p.id, hole_id=h.id, day_number=day, strokes=strokes, points=points)
                            db.session.add(score)
        db.session.commit()
        return redirect(url_for('scorecard', day=day))

    return render_template(
        'scorecard.html',
        day=day,
        course=course,
        holes=holes,
        players=players,
        scores=scores
    )