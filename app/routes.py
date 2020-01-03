from flask import request, jsonify, Blueprint
from flask_jwt import jwt_required

from app.helpers import model_helpers as helpers
route_blueprint = Blueprint('route_blueprint', __name__)

### INVISIBLE ROUTES #############
# /auth
# for jwt creation
# https://pythonhosted.org/Flask-JWT/

### USER ROUTES ###########

@route_blueprint.route('/users', methods=['POST'])
def create_user():
    user = helpers.create_user(request.get_json())
    return user.to_json()

@route_blueprint.route('/user/<user_id>')
@jwt_required()
def get_user(user_id):
    user = helpers.get_user(user_id)
    return user.to_json()

@route_blueprint.route('/user/<user_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_user(user_id):
    user = helpers.update_user(user_id, request.get_json())
    return user.to_json()

@route_blueprint.route('/user/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = helpers.delete_user(user_id)
    return jsonify({"user_id": user.id})

### WORKOUT ROUTES ###########

@route_blueprint.route('/user/<user_id>/workouts', methods=['POST'])
@jwt_required()
def create_workout(user_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.create_workout(user_id, request.get_json())
            return workout.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400


@route_blueprint.route('/user/<user_id>/workout/<workout_id>')
@jwt_required()
def get_workout(user_id, workout_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.get_workout(workout_id)
            return workout.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/workout/<workout_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_workout(user_id, workout_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.update_workout(workout_id, request.get_json())
            return workout.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/workout/<workout_id>', methods=['DELETE'])
@jwt_required()
def delete_workout(user_id, workout_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.delete_workout(workout_id)
            return jsonify({"workout_id": workout.id})
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

### CLIMBS ROUTES ###########

@route_blueprint.route('/user/<user_id>/climbs', methods=['POST'])
@jwt_required()
def create_climb(user_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = helpers.create_climb(request.get_json())
            return climb.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/climb/<climb_id>')
@jwt_required()
def get_climb(user_id, climb_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = helpers.get_climb(climb_id)
            return climb.to_json()
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/climb/<climb_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_climb(user_id, climb_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = helpers.update_climb(climb_id, request.get_json())
            return climb.to_json()
        except Exception as e:
                print(e)
                return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

@route_blueprint.route('/user/<user_id>/climb/<climb_id>', methods=['DELETE'])
@jwt_required()
def delete_climb(user_id, climb_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            climb = helpers.delete_climb(climb_id)
            return jsonify({"climb_id": climb.id})
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400