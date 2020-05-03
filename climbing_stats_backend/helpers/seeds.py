import click
from flask.cli import with_appcontext
import datetime
from random import randrange

from climbing_stats_backend.helpers.factory_helpers import db, bcrypt
from climbing_stats_backend.models.user import Users
from climbing_stats_backend.models.workout import Workouts
from climbing_stats_backend.models.climb import Climbs

@click.command()
@with_appcontext
def seed_db(users = 1, workouts = 50):
    """Seed Database"""
    for user in range(users):
        u = create_user()
        for workout in range(workouts):
            create_workout(u.id)

@click.command()
@with_appcontext
def reset_db():
    """Remove all items from DB"""
    Users.query.delete()
    Workouts.query.delete()
    Climbs.query.delete()
    db.session.commit()

def create_user():
    u = Users(username='blahblah',
        email='blah@example.com',
        password_hash=bcrypt.generate_password_hash('blahblah').decode('utf-8'))
    db.session.add(u)
    db.session.commit()
    return u

def create_workout(user_id, climbcount = 20):
    workout = Workouts(
        date = random_date(),
        user_id = user_id
    )
    db.session.add(workout)
    db.session.commit()

    climbs = []
    for b in range(climbcount // 2):
        climbs.append(create_boulders(user_id, workout.id))
    
    for r in range(climbcount // 2):
        climbs.append(create_routes(user_id, workout.id))

    for climb in climbs:
        db.session.add(climb)
        db.session.commit()

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

def random_date():
    #random between jan-mar
    d = datetime.datetime(2020, randrange(1,4), randrange(1, 29), 18, 00)
    return datetime.datetime.timestamp(d)
