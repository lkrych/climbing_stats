import json
def test_hello_world(test_client): 
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Hello World!" in response.data

def test_auth_happy(test_client, init_database):
    response = test_client.post(
        '/auth',
        data = json.dumps({
            'username': 'blahblah',
            'password': 'blahblah'
        }),
        headers = {
            'Content-Type': 'application/json'
        }
    )
    print(vars(response))
    assert response.status_code == 200
    assert b"access_token" in response.data

def test_auth_incorrect_password(test_client, init_database):
    response = test_client.post(
        '/auth',
        data = json.dumps({
            'username': 'blahblah',
            'password': 'cawcaw'
        }),
        headers = {
            'Content-Type': 'application/json'
        }
    )
    assert response.status_code == 401
    assert b"Invalid credentials" in response.data