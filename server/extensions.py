from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Instantiate extensions (no app yet)
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
