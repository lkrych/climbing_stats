from app import db, bcrypt
from app.models.user import Users
from app.models.workout import Workouts
from app.models.climb import Climbs

### USER HELPER METHODS ###########
def get_user(id):
    return db.session.query(Users).get(id)

def check_if_user_exists(id):
    if get_user(id):
        return True
    else:
        return False

def create_user(req_json):
    new_user = Users(
        username = req_json['username'],
        email = req_json['email'],
        password_hash = bcrypt.generate_password_hash(req_json['password']).decode('utf-8')
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def user_dne_exception():
    try:
        raise Exception("User does not exist")
    except Exception as e:
        print(e)

### WORKOUT HELPER METHODS ########

def check_valid_grade(type, g):
    if type == 0: #boulder
        assert(int(g) >= 0 and int(g) <= 16), "Improper Boulder Grading: {} is not between 0 or 16".format(g)
    elif type == 1:
        grade = int(g[:2])
        letter = g[2:]
        assert(grade >= 0 and grade <= 15 and letter in ['a','b','c','d']), "Improper Route Grading: {} is not a valid grade".format(g)
    

def grade_and_letter(g):
    grade = int(g[:2])
    letter = g[2:]
    return grade, letter

def get_workout():
    return db.session.query(Workouts).get(id)

def create_workout(user_id, req_json):
    new_workout = Workouts(
        date = req_json['date'],
        user_id = user_id
    )
    if req_json['boulder']:
        for b in req_json['boulder']:
            check_valid_grade(0, b)
            new_b = Climbs(
                type = 0,
                grade = int(b),
                user_id = user_id,
            )
            new_workout.climbs.append(new_b)

    if req_json['routes']:
        for r in req_json['routes']:
            check_valid_grade(1, r)
            grade, letter = grade_and_letter(r)
            new_r = Climbs(
                type = 0,
                grade = grade,
                letter_grade = letter,
                user_id = user_id,
            )
            new_workout.climbs.append(new_r)
    
    db.session.add(new_workout)
    db.session.commit()
    return new_workout
        