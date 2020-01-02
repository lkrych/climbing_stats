from datetime import datetime
from app import db

class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(128), default=datetime.timestamp(datetime.now()))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # climbs = db.relationship('climb',
    #     backref=db.backref('workout', lazy=True))

    def __repr__(self):
        return '<Workout {}>'.format(self.id)