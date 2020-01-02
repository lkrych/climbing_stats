from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    signup_date = db.Column(db.String(128), default=datetime.timestamp(datetime.now()))

    def __repr__(self):
        return '<User {}>'.format(self.username)