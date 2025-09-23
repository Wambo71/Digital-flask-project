from importlib import metadata
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Instantiate extensions (no app yet)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
ma = Marshmallow()
cors = CORS()


def init_cors(app):
    CORS(app, origins=["http://127.0.0.1:5000"])