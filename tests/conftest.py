import pytest

from climbing_stats_backend import create_app
from climbing_stats_backend.helpers.factory_helpers import db, bcrypt
from climbing_stats_backend.models.user import Users
from climbing_stats_backend.models.workout import Workouts
from climbing_stats_backend.models.climb import Climbs

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    # https://flask.palletsprojects.com/en/1.1.x/appcontext/
    ctx = flask_app.app_context()
    ctx.push()
 
    yield testing_client  # this is where the testing happens!
 
    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()
 
    # Insert user data
    user1 = Users(username='blahblah',
        email='blah@gmail.com',
        password_hash=bcrypt.generate_password_hash('blahblah').decode('utf-8'))
    user2 = Users(username='cawcaw',
        email='cawcaw@gmail.com',
        password_hash=bcrypt.generate_password_hash('cawcaw').decode('utf-8'))
    db.session.add(user1)
    db.session.add(user2)

    workout1 = Workouts(
        date = "1578204182.000337",
        user_id = 2
    )
    climb1 = Climbs(
        type = 0,
        grade = 6,
        user_id = 2,
        workout_id = 1
    )
    climb2 = Climbs(
        type = 0,
        grade = 5,
        user_id = 2,
        workout_id = 1
    )

    db.session.add(workout1)
    db.session.add(climb1)
    db.session.add(climb2)
 
    # Commit the changes for the users
    db.session.commit()
 
    yield db  # this is where the testing happens!
 
    db.drop_all()