from app import db

class Climbs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    letter_grade = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))

    user = db.relationship('Users', back_populates="climbs")
    workout = db.relationship('Workouts', back_populates="climbs")

    def __repr__(self):
        return '<Workout {}>'.format(self.id)
    
    def type_of_climb(self, type):
        if type == 0:
            return "boulder"
        else:
            return "route"
    
    def to_json(self):
        return {
            "id": self.id,
            "type": self.type_of_climb(self.type),
            "grade": self.grade,
            "letter_grade": self.letter_grade,
            "user": self.user_id,
            "workout": self.workout_id
        }