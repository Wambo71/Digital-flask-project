from flask import Flask
from flask_cors import CORS
from extensions import db, migrate, ma
from config import Config
from models import User, Product, Order, Review

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions here
db.init_app(app)
migrate.init_app(app, db)
ma.init_app(app)

# Enable CORS (for React frontend requests)
CORS(app)



if __name__ == "__main__":
    app.run(debug=True, port=5500)
