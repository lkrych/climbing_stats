from climbing_stats_backend.helpers.factory_helpers import db, bcrypt
from climbing_stats_backend.models.user import Users
from climbing_stats_backend.models.workout import Workouts
from climbing_stats_backend.models.climb import Climbs

### USER HELPER METHODS ###########

def get_user(user_id):
    user = db.session.query(Users).get(user_id)
    if user:
        return user
    else:
        return False

def get_user_by_username_or_email(username_or_email):
    try:
        user = db.session.query(Users).filter((Users.username == username_or_email) | (Users.email == username_or_email)).one()
        return user
    except Exception as e:
        print(e)
        return None

def check_if_user_exists(user_id):
    if get_user(user_id):
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
    db.session.commit() #adds user to dc
    return new_user

def update_user(user_id, req_json):
    user = get_user(user_id)
    for key, val in req_json.items():
        setattr(user, key, val)
    db.session.commit()
    return user

def delete_user(user_id):
    user = get_user(user_id)
    db.session.delete(user)
    db.session.commit()
    return user

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

def get_workout(workout_id):
    workout = db.session.query(Workouts).get(workout_id)
    if workout:
        return workout
    else:
        raise Exception("Workout: {} doesn't exist".format(workout_id))

def create_workout(user_id, req_json):
    new_workout = Workouts(
        date = req_json['date'],
        user_id = user_id
    )
    if 'boulder' in req_json:
        for b in req_json['boulder']:
            check_valid_grade(0, b)
            new_b = Climbs(
                type = 0,
                grade = int(b),
                user_id = user_id,
            )
            new_workout.climbs.append(new_b)

    if 'routes' in req_json:
        for r in req_json['routes']:
            check_valid_grade(1, r)
            grade, letter = grade_and_letter(r)
            new_r = Climbs(
                type = 1,
                grade = grade,
                letter_grade = letter,
                user_id = user_id,
            )
            new_workout.climbs.append(new_r)
    
    db.session.add(new_workout)
    db.session.commit()
    return new_workout

def update_workout(workout_id, req_json):
    workout = get_workout(workout_id)
    for key, val in req_json.items():
        setattr(workout, key, val)
    db.session.commit()
    return workout

def delete_workout(workout_id):
    workout = get_workout(workout_id)
    db.session.delete(workout)
    db.session.commit()
    return workout

### CLIMB HELPER METHODS ########

def get_climb(climb_id):
    climb = db.session.query(Climbs).get(climb_id)
    if climb:
        return climb
    else:
        raise Exception("Climb: {} doesn't exist".format(climb_id))

def create_climb(req_json):
    new_climb = {}
    if req_json['type'] == 'boulder':
        check_valid_grade(0, req_json['grade'])
        new_climb = Climbs(
            type = 0,
            grade = int(req_json['grade']),
            user_id = req_json['user_id'],
            workout_id = req_json['workout_id']
        )
    elif req_json['type'] == 'routes':
        check_valid_grade(1, req_json['grade'])
        grade, letter = grade_and_letter(req_json['grade'])
        new_climb = Climbs(
                type = 1,
                grade = grade,
                letter_grade = letter,
                user_id = req_json['user_id'],
                workout_id = req_json['workout_id']
            )
    else:
        raise Exception("Improperly formatted climb: {}".format(req_json))
    
    db.session.add(new_climb)
    db.session.commit()
    return new_climb

def update_climb(climb_id, req_json):
    climb = get_climb(climb_id)
    for key, val in req_json.items():
        setattr(climb, key, val)
    db.session.commit()
    return climb

def delete_climb(climb_id):
    climb = get_climb(climb_id)
    db.session.delete(climb)
    db.session.commit()
    return climb