import json

def get_auth_response(tc, username, password):
    response = tc.post(
        '/auth',
        json = {
            'username': username,
            'password': password
        }
    )
    return response

def create_jwt_header(response):
    token = json.loads(response)['access_token']
    return { 'Authorization': "JWT {}".format(token) }