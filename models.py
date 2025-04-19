from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    handicap_index = db.Column(db.Float, nullable=False)
    scores = db.relationship('Score', back_populates='player')

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=False)
    slope = db.Column(db.Integer, nullable=False)
    holes = db.relationship('Hole', back_populates='course')

class Hole(db.Model):
    __tablename__ = 'holes'
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    hole_number = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    stroke_index = db.Column(db.Integer, nullable=False)
    course = db.relationship('Course', back_populates='holes')

class Competition(db.Model):
    __tablename__ = 'competitions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class CompetitionDay(db.Model):
    __tablename__ = 'competition_days'
    competition_id = db.Column(db.Integer, db.ForeignKey('competitions.id'), primary_key=True)
    day_number = db.Column(db.Integer, primary_key=True)

class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    hole_id = db.Column(db.Integer, db.ForeignKey('holes.id'), nullable=False)
    day_number = db.Column(db.Integer, nullable=False)
    strokes = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    player = db.relationship('Player', back_populates='scores')
    hole = db.relationship('Hole')
