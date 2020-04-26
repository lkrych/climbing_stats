import os
from app import create_app

create_app(os.environ.get('FLASK_ENV'))