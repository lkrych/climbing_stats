from app.models.user import Users
from app.models.workout import Workouts
from app.models.climb import Climbs

def seed_database(db, users = 1, workouts = 50):
    print("==== seeding the database =====")
    for user in range(users):
        u = create_user(db)
        for workout in range(workouts):
            create_workout(db, u.id)
    db.session.commit()


def create_user(db):
    u = Users(username='blahblah',
        email='blah@example.com',
        password_hash=bcrypt.generate_password_hash('blahblah').decode('utf-8'))
    db.session.add(u)
    return u

def create_workout(db, user_id, climbcount = 20):
    workout = Workouts(
        date = random_date(),
        user_id = user_id
    )
    db.session.add(workout)
    climbs = []
    for b in range(climbcount // 2):
        climbs.append(create_boulders(user_id, workout_id))
    
    for r in range(climbcount // 2):
        climbs.append(create_routes(user_id, workout_id))

    for climb in climbs:
        db.session.add(climb)

def create_boulders(user_id, workout_id):
    c = Climbs(
        type = 0,
        grade = randrange(0,14),
        user_id = user_id,
        workout_id = workout_id
    )
    return c

def create_routes(user_id, workout_id):
    c = Climbs(
        type = 1,
        grade = randrange(7,14),
        user_id = user_id,
        workout_id = workout_id
    )
    return c

def random_date(day, month):
    #random between jan-mar
    d = datetime.datetime(2020, randrange(1,4), randrange(1, 29), 18, 00)
    return datetime.timestamp(d)
