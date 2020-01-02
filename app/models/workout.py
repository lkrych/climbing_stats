from datetime import datetime
from app import db

class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(128), default=datetime.timestamp(datetime.now()))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('Users', back_populates="workouts")
    climbs = db.relationship('Climbs', back_populates="workout")

    def __repr__(self):
        return '<Workout {}>'.format(self.id)
    
    def to_json(self):
        return {
            "id": self.id,
            "date": datetime.fromtimestamp(float(self.date)),
            "user_id": self.user_id,
            "workouts": self.workouts
        }