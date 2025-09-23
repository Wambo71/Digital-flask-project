from flask import Flask, make_response
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from extensions import db, migrate
from config import Config
from models import User, Product, Order, Review

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
api = Api(app)

# Enable CORS
CORS(app)


@app.route("/")
def hello():
    return "<h1>Welcome to backend</h1>"



class UserResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200
    
    
# Register the resource
api.add_resource(UserResource, "/api/users")


if __name__ == "__main__":
    app.run(debug=True, port=5500)
