from flask import Flask
from flask_jwt import JWT
import os

from config import app_config

#application factory function - http://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
# https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/

def create_app(environment='development'):
    #create and configure app
    app_instance = Flask(__name__)
    app_instance.config.from_object(app_config[environment])

    from app.helpers import factory_helpers

    factory_helpers.db.init_app(app_instance)
    factory_helpers.bcrypt.init_app(app_instance)
    # hack for resolving circular import between auth_helpers and this file
    from app.helpers import auth_helpers
    jwt = JWT(app_instance, auth_helpers.authenticate, auth_helpers.identity)
    
    from app.routes import route_blueprint
    app_instance.register_blueprint(route_blueprint)

    from app.helpers.seeds import seed_db, reset_db
    app_instance.cli.add_command(seed_db)
    app_instance.cli.add_command(reset_db)

    return app_instance

if __name__ == __main__ :
    create_app(os.environ.get('FLASK_ENV'))