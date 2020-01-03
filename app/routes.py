from flask import request, jsonify

from app import app_instance
from app.models import helpers

@app_instance.route('/')
def hello_world():
    return 'Hello World!'

# @app_instance.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

### USER ROUTES ###########

@app_instance.route('/users', methods=['POST'])
def create_user():
    user = helpers.create_user(request.get_json())
    return user

@app_instance.route('/user/<user_id>')
def get_user(user_id):
    user = helpers.get_user(user_id)
    return user

@app_instance.route('/user/<user_id>', methods=['PUT', 'PATCH'])
def update_user(user_id):
    user = helpers.update_user(user_id, request.get_json())
    return user

@app_instance.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = helpers.delete_user(user_id)
    return user.id

### WORKOUT ROUTES ###########

@app_instance.route('/user/<user_id>/workouts', methods=['POST'])
def create_workout(user_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.create_workout(user_id, request.get_json())
            return workout
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400


@app_instance.route('/user/<user_id>/workout/<workout_id>')
def get_workout(user_id, workout_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.get_workout(workout_id)
            return workout
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

@app_instance.route('/user/<user_id>/workout/<workout_id>', methods=['PUT', 'PATCH'])
def update_workout(user_id, workout_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.update_workout(workout_id, request.get_json())
            return workout
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400

@app_instance.route('/user/<user_id>/workout/<workout_id>', methods=['DELETE'])
def delete_workout(user_id, workout_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.delete_workout(workout_id)
            return workout.id
        except Exception as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400