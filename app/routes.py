from flask import request

from app import app_instance
from app.models.user import User
from app.models.workout import Workout

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
    user = User.create_user(request.data)
    return user

@app_instance.route('/user/<id>')
def get_user():
    user = User.get_user(id)
    return user

@app_instance.route('/workouts', methods=['POST'])
def create_workout():
    workout = Workout.create_workout(request.data)
    return workout

@app_instance.route('/workout/<id>')
def get_workout():
    workout = Workout.get_workout(id)
    return workout