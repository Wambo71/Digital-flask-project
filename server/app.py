from flask import Flask, make_response,request
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



class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200
    
    def post(self):
      data=request.get_json()

      if not data.get("username") or not data.get("email") or not data.get("password_hash"):
            return {"error": "username, email and password_hash are required"}, 400

      new_user=User(
          username=data.get('username'),
          email=data.get('email'),
          password_hash=data.get("password_hash")
      )
      db.session.add(new_user)
      db.session.commit()
      return new_user.to_dict(), 201 
    

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200
    
    def put(self, user_id):
        
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        data = request.get_json()
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.password_hash = data.get("password_hash", user.password_hash)

        db.session.commit()
        return user.to_dict(), 200
    
    def delete(self, user_id):
        
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user_id} deleted"}, 200




api.add_resource(UserResource, "/api/users/<int:user_id>")

api.add_resource(UsersResource, "/api/users")

#products
class ProductsResource(Resource):
    def get(self):
        products = Product.query.all()
        return [product.to_dict() for product in products], 200
    
    def post(self):
        data = request.get_json()
        if not data.get("name") or not data.get("price") or not data.get("seller_id"):
            return {"error": "name, price, and seller_id are required"}, 400

        new_product = Product(
            name=data["name"],
            description=data.get("description"),
            price=data["price"],
            seller_id=data["seller_id"],
            stock=data.get("stock", 0)
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product.to_dict(), 201


if __name__ == "__main__":
    app.run(debug=True, port=5500)
