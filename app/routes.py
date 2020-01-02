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

@app_instance.route('/users', methods=['POST'])
def create_user():
    user = helpers.create_user(request.get_json())
    return user.to_json()

@app_instance.route('/user/<user_id>')
def get_user(user_id):
    user = helpers.get_user(user_id)
    return user.to_json()

@app_instance.route('/user/<user_id>/workouts', methods=['POST'])
def create_workout(user_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        try:
            workout = helpers.create_workout(user_id, request.get_json())
            return workout
        except AssertionError as e:
            print(e)
            return jsonify({"message": str(e)}), 400
    else:
        helpers.user_dne_exception()
        return jsonify(), 400


@app_instance.route('/user/<user_id>/workout/<workout_id>')
def get_workout(user_id, workout_id):
    user_exists = helpers.check_if_user_exists(user_id)
    if user_exists:
        workout = helpers.get_workout(id)
        return workout.to_json()
    else:
        helpers.user_dne_exception()
        return jsonify(), 400