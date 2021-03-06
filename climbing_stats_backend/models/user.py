from datetime import datetime
from climbing_stats_backend.helpers.factory_helpers import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    signup_date = db.Column(db.String(128), default=datetime.timestamp(datetime.now()))

    workouts = db.relationship('Workouts', back_populates="user")
    climbs = db.relationship('Climbs', back_populates='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "signup_date": datetime.fromtimestamp(float(self.signup_date))
        }
    
