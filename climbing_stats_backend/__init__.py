from flask import Flask
from flask_jwt_extended import (JWTManager)
from flask_cors import CORS
import os

from . import config 

#application factory function - http://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
# https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/
environment = os.getenv('ENV')

def create_app(testing=False):
    #create and configure app
    app_instance = Flask(__name__)
    if environment == 'production':
        app_instance.config.from_object(config.ProductionConfig())
    elif environment == 'stage':
        app_instance.config.from_object(config.StageConfig())
    elif environment == 'development':
        app_instance.config.from_object(config.DevelopmentConfig())
    elif testing:
        app_instance.config.from_object(config.TestingConfig())

    from climbing_stats_backend.helpers import factory_helpers

    factory_helpers.db.init_app(app_instance)
    factory_helpers.bcrypt.init_app(app_instance)
    CORS(app_instance)
    jwt = JWTManager(app_instance)
    
    from climbing_stats_backend.routes import route_blueprint
    app_instance.register_blueprint(route_blueprint)

    from climbing_stats_backend.helpers.seeds import seed_db, reset_db
    app_instance.cli.add_command(seed_db)
    app_instance.cli.add_command(reset_db)

    return app_instance
