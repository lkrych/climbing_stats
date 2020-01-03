from app import bcrypt
from app.helpers import model_helpers

def authenticate(username, password):
    print(username)
    user = model_helpers.get_user_by_username(username)
    if user and bcrypt.check_password_hash(user.password_hash, password):
        return user #even though it returns the user it will only use the users id in the JWT

def identity(payload):
    user_id = payload['identity']
    return model_helpers.get_user(user_id)
