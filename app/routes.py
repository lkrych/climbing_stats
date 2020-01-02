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

@app_instance.route('/user/<id>')
def get_user(id):
    user = helpers.get_user(id)
    return user.to_json()

@app_instance.route('/workouts', methods=['POST'])
def create_workout():
    workout = helpers.create_workout(request.get_json())
    return workout

@app_instance.route('/workout/<id>')
def get_workout():
    workout = helpers.get_workout(id)
    return workout