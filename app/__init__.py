from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


#initialize db
app_instance = Flask(__name__)
app_instance.config.from_object(Config)
db = SQLAlchemy(app_instance)

from app import routes