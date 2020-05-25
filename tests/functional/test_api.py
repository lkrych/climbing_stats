import base64
from datetime import datetime
import json
from flask_jwt_extended import decode_token
from tests.helpers import test_util

default_username = "blahblah"
default_password = "blahblah"
snoopy_username = "impersonator"
snoopy_password = "impersonator"
malicious_username =  "malicious"
malicious_password = "malicious"

###### / ######################
def test_hello_world(test_client, init_database): 
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data


##### /login ######################

def test_cannot_modify_jwt(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, malicious_username, malicious_password)
    data = json.loads(auth_response.data.decode('utf-8'))
    access_token = data['access_token']
    access_token = decode_token(access_token)
    access_token['identity']['id'] = 1 # an id that malicious wants to hack
    tampered_token = base64.b64encode(json.dumps(access_token).encode('utf-8'))
    jwt_header = test_util.create_jwt_header(json.dumps({'access_token': tampered_token.decode('utf-8')}).encode('utf-8'))

    #do something malicious shouldn't be able to do
    success_response = test_client.get('/user/1', headers = jwt_header)
    assert success_response.status_code != 200

def test_login_200_returns_jwt(test_client, init_database):
    response = test_util.get_auth_response(test_client, default_username, default_password)
    assert response.status_code == 200
    assert b"access_token" in response.data

def test_login_401_incorrect_password(test_client, init_database):
    response = test_util.get_auth_response(test_client, default_username, 'cawcaw')
    assert response.status_code == 401
    assert b"Bad username or password" in response.data

def test_login_401_user_dne(test_client, init_database):
    #user does not exist!
    response = test_util.get_auth_response(test_client, 'wahwah', default_password)
    assert response.status_code == 401
    assert b"Bad username or password" in response.data

##### /user ######################

def test_user_read_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, default_username, default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.get('/user/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    #request succeeds with jwt
    success_response = test_client.get('/user/1', headers = jwt_header)
    assert success_response.status_code == 200
    assert b"blahblah" in success_response.data
    assert b"blah@gmail" in success_response.data

def test_user_create(test_client, init_database):
    success_response = test_client.post(
        '/users',
        json = {
            "username": 'newnew',
            "email": "newuser@yahoo.com",
            "password": 'newnew'
        }
    )
    assert success_response.status_code == 200
    assert b"access_token" in success_response.data


def test_user_update_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, default_username, default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    #verify that record is unchanged before update call
    get_response = test_client.get('/user/1', headers = jwt_header)
    assert b"blah@gmail" in get_response.data

    success_response = test_client.put(
        '/user/1',
         json = {
             "email": "fancynewemail@gmail.com"
         },
         headers = jwt_header
    )
    assert success_response.status_code == 200
    assert b"blah@gmail" not in success_response.data

    #verify that record is changed after update call
    get_response_post_update = test_client.get('/user/1', headers = jwt_header)
    body = json.loads(get_response_post_update.data)
    assert "fancynewemail@gmail.com" == body['email']

def test_user_delete_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, default_username, default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

#   request fails without jwt
    fail_response = test_client.delete('/user/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    #assert user exists
    get_response = test_client.get('/user/1', headers = jwt_header)
    assert b"fancynewemail@gmail" in get_response.data

    #delete user
    success_response = test_client.delete('/user/1', headers = jwt_header)
    assert success_response.status_code == 200
    assert b"user_id" in success_response.data

    #assert user doesn't exist
    get_response_fail = test_client.get('/user/1', headers = jwt_header)
    assert get_response_fail.status_code == 400

###### /workouts ######################

# need to reset the variables
new_default_username = "cawcaw"
new_default_password = "cawcaw"

def test_workout_read_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.get('/user/2/workout/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    #request succeeds with jwt
    success_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert success_response.status_code == 200
    assert b"boulder" in success_response.data


def test_workout_read_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the workout can view it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_workout_read_user_cannot_read_anothers_workout(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.get('/user/3/workout/1', headers = jwt_header)
    assert fail_response.status_code == 400
    assert b"There was a problem fetching the workout" in fail_response.data

def test_workouts_read_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.get('/user/2/workout/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    #request succeeds with jwt
    success_response = test_client.get('/user/2/workouts', headers = jwt_header)
    assert success_response.status_code == 200
    assert len(success_response.json['workouts']) == 1

def test_workouts_read_belongs_only_to_user(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.get('/user/2/workouts', headers = jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_workout_create_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.post('/user/2/workouts')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    #requests succeeds with jwt
    success_response = test_client.post(
        '/user/2/workouts',
        headers = jwt_header,
        json = {
            "date": 1578702677,
            "boulders": [9, 10, 11],
            "routes": ['12a', '11a'],
            "notes": "That crimpy 12 was hard!"
        }
    )
    assert success_response.status_code == 200
    assert b"10" in success_response.data
    assert b"crimpy" in success_response.data

def test_workout_update_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/2/workout/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    success_response = test_client.get(
        '/user/2/workout/2',
        headers = jwt_header,
    )
    assert success_response.status_code == 200

    assert b"boulder" in success_response.data
    assert "14" not in success_response.json['climbs']

    #requests succeeds with jwt
    success_response = test_client.put(
        '/user/2/workout/2',
        headers = jwt_header,
        json = {
            'date': datetime.timestamp(datetime.now()),
            'climbs': [
                {'grade': 9, 'id': 3, 'letter_grade': None, 'type': 'boulder', 'user_id': 2, 'workout': 2},
                {'grade': 10, 'id': 4, 'letter_grade': None, 'type': 'boulder', 'user_id': 2, 'workout': 2},
                {'grade': 14, 'id': 5, 'letter_grade': None, 'type': 'boulder', 'user_id': 2, 'workout': 2},
                {'grade': 12, 'id': 6, 'letter_grade': 'a', 'type': 'route', 'user_id': 2, 'workout': 2},
                {'grade': 11, 'id': 7, 'letter_grade': 'a', 'type': 'route', 'user_id': 2, 'workout': 2}
            ],
            'notes': "This is the new note."
        }
    )
    assert success_response.status_code == 200
   
    assert b"climbs" in success_response.data
    assert success_response.json['climbs'][2]['grade'] == 14
    assert b"new note" in success_response.data

def test_workout_update_user_cannot_update_anothers_workout(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.get('/user/3/workout/1',
        headers = jwt_header,
        json = {
            'date': datetime.timestamp(datetime.now()),
            'climbs': [
                {'grade': 9, 'id': 3, 'letter_grade': None, 'type': 'boulder', 'user_id': 2, 'workout': 2},
                {'grade': 10, 'id': 4, 'letter_grade': None, 'type': 'boulder', 'user_id': 2, 'workout': 2},
                {'grade': 14, 'id': 5, 'letter_grade': None, 'type': 'boulder', 'user_id': 2, 'workout': 2},
                {'grade': 12, 'id': 6, 'letter_grade': 'a', 'type': 'route', 'user_id': 2, 'workout': 2},
                {'grade': 11, 'id': 7, 'letter_grade': 'a', 'type': 'route', 'user_id': 2, 'workout': 2}
            ]
        }
    )
    assert fail_response.status_code == 400
    assert b"There was a problem fetching the workout" in fail_response.data

def test_workout_update_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the workout can update it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/2/workout/1', headers=jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_workout_delete_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.delete('/user/2/workout/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    workouts_response = test_client.get('/user/2/workouts', headers = jwt_header)
    assert workouts_response.status_code == 200
    assert len(workouts_response.json['workouts']) == 2

    #requests succeeds with jwt
    success_response = test_client.delete(
        '/user/2/workout/2',
        headers = jwt_header,
    )
    assert success_response.status_code == 200

    workouts_response = test_client.get('/user/2/workouts', headers = jwt_header)
    assert workouts_response.status_code == 200
    assert len(workouts_response.json['workouts']) == 1
    

def test_workout_delete_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the workout can delete it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.delete('/user/2/workout/1', headers=jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_workout_delete_user_cannot_delete_anothers_workout(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.delete('/user/3/workout/1', headers = jwt_header)
    assert fail_response.status_code == 400
    assert b"There was a problem fetching the workout" in fail_response.data

###### /climbs ######################

def test_climb_read_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.get('/user/2/climb/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    #request succeeds with jwt
    success_response = test_client.get('/user/2/climb/1', headers = jwt_header)
    assert success_response.status_code == 200

def test_climb_read_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the climb can view it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request succeeds with jwt
    fail_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_climb_read_user_cannot_read_anothers_climb(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.get('/user/3/climb/1', headers = jwt_header)
    assert fail_response.status_code == 400
    assert b"There was a problem fetching the climb" in fail_response.data


def test_climb_create_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.post('/user/2/climbs')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    workouts_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert workouts_response.status_code == 200
    num_climbs =  len(workouts_response.json['climbs'])

    success_response = test_client.post(
        '/user/2/climbs',
        headers = jwt_header,
        json = {
            "type": "boulder",
            "grade": 5,
            "user_id": 2,
            "workout_id": 1
        }
    )
    assert success_response.status_code == 200
    
    #check to see if it was added to workout
    workouts_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert workouts_response.status_code == 200
    assert len(workouts_response.json['climbs']) == num_climbs + 1

def test_climb_create_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the climb can view it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.post(
        '/user/2/climbs',
        headers = jwt_header,
        json = {
            "type": "boulder",
            "grade": 5,
            "user_id": 2,
            "workout_id": 1
        }
    )
    assert fail_response.status_code == 403


def test_climb_update_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/2/climb/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

    climb_response = test_client.get('user/2/climb/1', headers = jwt_header)
    assert climb_response.status_code == 200
    assert climb_response.json['grade'] == 6

    success_response = test_client.put(
        '/user/2/climb/1',
        headers = jwt_header,
        json = {
            "type": "boulder",
            "grade": 5,
            "user_id": 2,
            "workout_id": 1
        }
    )
    assert success_response.status_code == 200

    climb_response = test_client.get('user/2/climb/1', headers = jwt_header)
    assert climb_response.status_code == 200
    assert climb_response.json['grade'] == 5

def test_climb_update_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the climb can update it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/2/climb/1', headers=jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_climb_update_user_cannot_update_anothers_climb(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.put('/user/3/climb/1',
        headers = jwt_header,
        json = {
            "type": "boulder",
            "grade": 5,
            "user_id": 2,
            "workout_id": 1
        }
    )
    assert fail_response.status_code == 400
    assert b"There was an error updating the climb" in fail_response.data

def test_climb_delete_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.delete('/user/3/climb/1')
    assert fail_response.status_code == 401

    workouts_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert workouts_response.status_code == 200
    num_climbs =  len(workouts_response.json['climbs'])

    success_response = test_client.delete( '/user/2/climb/1', headers = jwt_header)
    assert success_response.status_code == 200
    
    #check to see if it was added to workout
    workouts_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert workouts_response.status_code == 200
    assert len(workouts_response.json['climbs']) == num_climbs - 1

def test_climb_delete_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the climb can delete it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.delete('/user/2/climb/1', headers=jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_climb_delete_user_cannot_delete_anothers_climb(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.delete('/user/3/climb/1', headers = jwt_header)
    assert fail_response.status_code == 400
    assert b"There was a problem fetching the climb" in fail_response.data