import base64
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


def test_workout_read_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the workout can view it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.get('/user/2/workout/1', headers = jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data


def test_workout_create_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.post('/user/2/workouts')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

def test_workout_update_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/2/workout/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

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

def test_workout_delete_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the workout can delete it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.delete('/user/2/workout/1', headers=jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

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


def test_climb_create_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.post('/user/2/climbs')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

def test_climb_update_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/2/climb/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

def test_climb_update_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the climb can update it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/2/climb/1', headers=jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data

def test_climb_delete_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, new_default_username, new_default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.delete('/user/2/climb/1')
    assert fail_response.status_code == 401
    assert b"Missing Authorization Header" in fail_response.data

def test_climb_delete_belongs_only_to_user(test_client, init_database):
    #make sure only the user that owns the climb can delete it
    auth_response = test_util.get_auth_response(test_client, snoopy_username, snoopy_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.delete('/user/2/climb/1', headers=jwt_header)
    assert fail_response.status_code == 403
    assert b"Not Authorized" in fail_response.data