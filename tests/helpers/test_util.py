import json

def get_auth_response(tc, username, password):
    response = tc.post(
        '/auth',
        data = json.dumps({
            'username': username,
            'password': password
        }),
        headers = {
            'Content-Type': 'application/json'
        }
    )
    return response

def create_jwt_header(response):
    token = json.loads(response)['access_token']
    return { 'Authorization': "JWT {}".format(token) }