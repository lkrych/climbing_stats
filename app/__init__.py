from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt import JWT

from config import Config


app_instance = Flask(__name__)
app_instance.config.from_object(Config)
db = SQLAlchemy(app_instance)
bcrypt = Bcrypt(app_instance)

# hack for resolving circular import between auth_helpers and this file
from app.helpers import auth_helpers
jwt = JWT(app_instance, auth_helpers.authenticate, auth_helpers.identity)

from app import routes