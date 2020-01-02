from app import db

class Climb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    letter_grade = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))

    def __repr__(self):
        return '<Workout {}>'.format(self.id)