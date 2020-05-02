from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token

from climbing_stats_backend.helpers import auth_helpers 
from climbing_stats_backend.helpers import model_helpers
from climbing_stats_backend.helpers import factory_helpers 
route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/', methods=['GET'])
def hello_world():
    return  { 'msg': 'Hello World!' }, 200

@route_blueprint.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    usernameOrEmail = request.json.get('username', None)
    password = request.json.get('password', None)
    if not usernameOrEmail:
        return jsonify({"msg": "Missing username or email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = model_helpers.get_user_by_username_or_email(usernameOrEmail)
    if user and not factory_helpers.bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"msg": "Bad username or password"}), 401

    if not user:
        return jsonify({"msg": "Bad username or password"}), 401
    
    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=user.to_json())
    return jsonify({"access_token": access_token}), 200


@route_blueprint.route('/users', methods=['POST'])
def create_user():
    user = model_helpers.create_user(request.get_json())
    access_token = create_access_token(identity=user.to_json())
    return jsonify({"access_token": access_token}), 200

@route_blueprint.route('/user/<user_id>')
@auth_helpers.authorize
def get_user(user_id):
    try:
        user = model_helpers.get_user(user_id)
        return user.to_json()
    except Exception as e:
        print(e)
        return jsonify({"message": str(e)}), 400

@route_blueprint.route('/user/<user_id>', methods=['PUT', 'PATCH'])
@auth_helpers.authorize
def update_user(user_id):
    user = model_helpers.update_user(user_id, request.get_json())
    return user.to_json()

@route_blueprint.route('/user/<user_id>', methods=['DELETE'])
@auth_helpers.authorize
def delete_user(user_id):
    user = model_helpers.delete_user(user_id)
    return jsonify({"user_id": user.id})

### WORKOUT ROUTES ###########

@route_blueprint.route('/user/<user_id>/workouts', methods=['POST'])
@auth_helpers.authorize
def create_workout(user_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = model_helpers.create_workout(user_id, request.get_json())
            return workout.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/workouts', methods=['GET'])
@auth_helpers.authorize
def get_all_workouts(user_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climbs = model_helpers.get_all_workouts()
            return jsonify ({ "workouts": workouts }), 200
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/workout/<workout_id>')
@auth_helpers.authorize
def get_workout(user_id, workout_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = model_helpers.get_workout(workout_id)
            return workout.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/workout/<workout_id>', methods=['PUT', 'PATCH'])
@auth_helpers.authorize
def update_workout(user_id, workout_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = model_helpers.update_workout(workout_id, request.get_json())
            return workout.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/workout/<workout_id>', methods=['DELETE'])
@auth_helpers.authorize
def delete_workout(user_id, workout_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = model_helpers.delete_workout(workout_id)
            return jsonify({"workout_id": workout.id})
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

### CLIMBS ROUTES ###########

@route_blueprint.route('/user/<user_id>/climbs', methods=['POST'])
@auth_helpers.authorize
def create_climb(user_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = model_helpers.create_climb(request.get_json())
            return climb.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/climb/<climb_id>')
@auth_helpers.authorize
def get_climb(user_id, climb_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = model_helpers.get_climb(climb_id)
            return climb.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/climbs', methods=['GET'])
@auth_helpers.authorize
def get_all_climbs(user_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climbs = model_helpers.get_all_climbs()
            return jsonify ({ "climbs": climbs }), 200
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/climb/<climb_id>', methods=['PUT', 'PATCH'])
@auth_helpers.authorize
def update_climb(user_id, climb_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = model_helpers.update_climb(climb_id, request.get_json())
            return climb.to_json()
        except Exception as e:
                print(e)
                return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/climb/<climb_id>', methods=['DELETE'])
@auth_helpers.authorize
def delete_climb(user_id, climb_id):
    user_exists = model_helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = model_helpers.delete_climb(climb_id)
            return jsonify({"climb_id": climb.id})
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        model_helpers.user_dne_exception()
        return jsonify(), 400