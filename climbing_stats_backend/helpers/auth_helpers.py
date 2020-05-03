from flask import jsonify
from flask_jwt_extended import (
    verify_jwt_in_request, get_jwt_identity
)
from functools import wraps

def authorize(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()

        if int(kwargs['user_id']) != int(identity['id']):
            return jsonify({'msg': 'Not Authorized!'}), 403
        else:
            return fn(*args, **kwargs)
    return wrapper
