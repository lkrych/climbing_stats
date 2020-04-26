from climbing_stats_backend.helpers import factory_helpers
from climbing_stats_backend.helpers import model_helpers

# used to authenticate user
# a post to the /auth endpoint routes to this function
# even though it returns the user it will only use the users id in the JWT
def authenticate(usernameOrEmail, password):
    user = model_helpers.get_user_by_username_or_email(usernameOrEmail)
    if user and factory_helpers.bcrypt.check_password_hash(user.password_hash, password):
        return user

# used when we receive a JWT
# unpacks JWT and gives payload data to identity
# the payload contains the user's id
def identity(payload):
    user_id = payload['identity']
    return model_helpers.get_user(user_id)
