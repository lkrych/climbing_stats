import json
from tests.helpers import test_util

default_username = "blahblah"
default_password = "blahblah"
###### / ######################
def test_hello_world(test_client): 
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data

###### /auth ######################
def test_auth_200_returns_jwt(test_client, init_database):
    response = test_util.get_auth_response(test_client, default_username, default_password)
    print(vars(response))
    assert response.status_code == 200
    assert b"access_token" in response.data

def test_auth_401_incorrect_password(test_client, init_database):
    response = test_util.get_auth_response(test_client, default_username, 'cawcaw')
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data

def test_auth_401_user_dne(test_client, init_database):
    #user does not exist!
    response = test_util.get_auth_response(test_client, 'wahwah', default_password)
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data

###### /user ######################

def test_user_read_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, default_username, default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.get('/user/1')
    assert fail_response.status_code == 401
    assert b"Request does not contain an access token" in fail_response.data

    #request succeeds with jwt
    success_response = test_client.get('/user/1', headers = jwt_header)
    assert success_response.status_code == 200
    assert b"blahblah" in success_response.data
    assert b"blah@gmail" in success_response.data

def test_user_create(test_client, init_database):
    username = "newuser"
    password = "newnew"
    success_response = test_client.post(
        '/users',
        json = {
            "username": username,
            "email": "newuser@yahoo.com",
            "password": password
        }
    )
    assert success_response.status_code == 200
    assert b"newuser" in success_response.data

    new_user_id = json.loads(success_response.data)['id']

    #verify that new user can access auth_limited endpoints
    auth_response = test_util.get_auth_response(test_client, username, password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    success_response = test_client.get('/user/{}'.format(new_user_id), headers = jwt_header)
    assert success_response.status_code == 200
    assert b"newuser" in success_response.data


def test_user_update_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, default_username, default_password)
    jwt_header = test_util.create_jwt_header(auth_response.data)

    #request fails without jwt
    fail_response = test_client.put('/user/1')
    assert fail_response.status_code == 401
    assert b"Request does not contain an access token" in fail_response.data

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
    assert b"Request does not contain an access token" in fail_response.data

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

def test_workout_read_auth_limited():
    pass

def test_workout_read_belongs_only_to_user():
    #make sure only the user that owns the workout can view it
    pass

def test_workout_create_auth_limited():
    pass

def test_workout_update_auth_limited():
    pass

def test_workout_update_belongs_only_to_user():
    #make sure only the user that owns the workout can update it
    pass

def test_workout_delete_auth_limited():
    pass

def test_workout_delete_belongs_only_to_user():
    #make sure only the user that owns the workout can delete it
    pass

###### /climbs ######################

def test_climb_read_auth_limited():
    pass

def test_climb_read_belongs_only_to_user():
    #make sure only the user that owns the climb can view it
    pass

def test_climb_create_auth_limited():
    pass

def test_climb_update_auth_limited():
    pass

def test_climb_update_belongs_only_to_user():
    #make sure only the user that owns the climb can update it
    pass

def test_climb_delete_auth_limited():
    pass

def test_climb_delete_belongs_only_to_user():
    #make sure only the user that owns the climb can delete it
    pass