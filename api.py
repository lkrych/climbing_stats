from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:db/climbing_stats.db'
db = SQLAlchemy(app)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

@app.route('/users', methods=['POST'])
def create_user():
    user = User.create_user(request.data)
    return user

@app.route('/user/<id>')
def get_user():
    user = User.get_user(id)
    return user

@app.route('/workouts', methods=['POST'])
def create_workout():
    workout = Workout.create_workout(request.data)
    return workout

@app.route('/workout/<id>')
def get_workout():
    workout = Workout.get_workout(id)
    return workout