#!/bin/sh
set -e

# Ensure we are always in the project root
cd /app

# Ensure data directory exists
test -d /app/data || mkdir -p /app/data

# Initialize and migrate database if needed
if [ ! -d migrations ]; then
  flask db init
fi
flask db migrate -m "Initial schema" || true
flask db upgrade

# Seed courses and holes
python << 'EOF'
from app import app
from models import db, Course, Hole
hole_data = {
    'Pasha': [(1,4,7),(2,3,17),(3,4,13),(4,4,9),(5,3,11),(6,5,3),(7,3,15),(8,4,5),(9,4,1),
              (10,5,6),(11,4,14),(12,4,16),(13,5,4),(14,4,12),(15,4,2),(16,4,8),(17,3,18),(18,4,10)],
    'Nobilis': [(1,4,2),(2,4,6),(3,4,14),(4,3,10),(5,4,17),(6,5,11),(7,4,9),(8,5,5),(9,3,12),
                (10,4,7),(11,5,18),(12,4,1),(13,3,4),(14,4,16),(15,4,3),(16,3,8),(17,4,13),(18,5,15)],
    'Sultan': [(1,4,5),(2,3,17),(3,5,15),(4,4,1),(5,4,7),(6,3,11),(7,5,3),(8,3,13),(9,4,9),
               (10,4,16),(11,4,12),(12,5,2),(13,4,10),(14,4,4),(15,4,14),(16,5,6),(17,3,18),(18,4,8)],
    'Lykia': [(1,4,4),(2,5,14),(3,4,2),(4,3,6),(5,4,12),(6,5,8),(7,4,10),(8,3,18),(9,4,16),
              (10,4,7),(11,4,9),(12,4,5),(13,5,1),(14,4,15),(15,4,13),(16,5,11),(17,3,17),(18,4,3)]
}
with app.app_context():
    # Always seed holes for all courses
    courses = [
        ('Pasha', 67.7, 123),   # Day 1
        ('Nobilis', 70.7, 125), # Day 2
        ('Sultan', 71.6, 138),  # Day 3
        ('Nobilis', 70.7, 125), # Day 4
        ('Lykia', 71.7, 126),   # Day 5
        ('Pasha', 67.7, 123)    # Day 6
    ]
    for name, rating, slope in courses:
        course = Course.query.filter_by(name=name).first()
        if not course:
            course = Course(name=name, rating=rating, slope=slope)
            db.session.add(course)
            db.session.flush()
        # Seed holes if not already present
        if Hole.query.filter_by(course_id=course.id).count() == 0:
            for hn, par, si in hole_data[name]:
                db.session.add(Hole(course_id=course.id, hole_number=hn, par=par, stroke_index=si))
    db.session.commit()

        # Seed players if none exist
    if Player.query.count() == 0:
        players = [
            ("Andy P", 10.9), ("Joe B", 13.3), ("Mark A", 9.6), ("Michael D", 11.4),
            ("Steve R", 19.8), ("John L", 22.0), ("Mark H", 27.0), ("Ray H", 25.8)
        ]
        for name, hcp in players:
            db.session.add(Player(name=name, handicap_index=hcp))
    db.session.commit()
EOF

# Finally, launch the server
exec gunicorn --bind 0.0.0.0:8585 app:app