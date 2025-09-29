from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiate extensions (no app yet)
db = SQLAlchemy()
migrate = Migrate()


