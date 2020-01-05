import json
from tests.helpers import test_util

###### / ######################
def test_hello_world(test_client): 
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data

###### /auth ######################
def test_auth_200_returns_jwt(test_client, init_database):
    response = test_util.get_auth_response(test_client, 'blahblah', 'blahblah')
    print(vars(response))
    assert response.status_code == 200
    assert b"access_token" in response.data

def test_auth_401_incorrect_password(test_client, init_database):
    response = test_util.get_auth_response(test_client, 'blahblah', 'cawcaw')
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data

def test_auth_401_user_dne(test_client, init_database):
    #user does not exist!
    response = test_util.get_auth_response(test_client, 'wahwah', 'blahblah')
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data

###### /user ######################

def test_user_read_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, 'blahblah', 'blahblah')
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.get('/user/1')
    assert fail_response.status_code == 401
    assert b"Request does not contain an access token" in fail_response.data

    success_response = test_client.get('/user/1', headers = jwt_header)
    assert success_response.status_code == 200
    assert b"username" in success_response.data
    assert b"email" in success_response.data

def test_user_create(test_client, init_database):
    pass

def test_user_update_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, 'blahblah', 'blahblah')
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.put('/user/1')
    assert fail_response.status_code == 401
    assert b"Request does not contain an access token" in fail_response.data

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
    # assert b"blah@gmail" not in success_response.data

    get_response_post_update = test_client.get('/user/1', headers = jwt_header)
    body = json.loads(get_response_post_update.data)
    assert "fancynewemail@gmail.com" == body['email']

def test_user_delete_auth_limited(test_client, init_database):
    auth_response = test_util.get_auth_response(test_client, 'blahblah', 'blahblah')
    jwt_header = test_util.create_jwt_header(auth_response.data)

    fail_response = test_client.delete('/user/1')
    assert fail_response.status_code == 401
    assert b"Request does not contain an access token" in fail_response.data

    # success_response = test_client.delete('/user/1', headers = jwt_header)
    # assert success_response.status_code == 200
    # assert b"user_id" in success_response.data


