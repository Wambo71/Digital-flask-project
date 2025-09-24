from flask import Flask, request
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


# ---users
class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200
    
    def post(self):
        data = request.get_json()

        if not data.get("username") or not data.get("email") or not data.get("password_hash"):
            return {"error": "username, email and password_hash are required"}, 400

        new_user = User(
            username=data["username"],
            email=data["email"],
            password_hash=data["password_hash"]
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


api.add_resource(UsersResource, "/api/users")
api.add_resource(UserResource, "/api/users/<int:user_id>")


# ---products
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


class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {"error": "Product not found"}, 404
        return product.to_dict(), 200
    
    def put(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {"error": "Product not found"}, 404

        data = request.get_json()
        product.name = data.get("name", product.name)
        product.description = data.get("description", product.description)
        product.price = data.get("price", product.price)
        product.stock = data.get("stock", product.stock)

        db.session.commit()
        return product.to_dict(), 200
    
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {"error": "Product not found"}, 404

        db.session.delete(product)
        db.session.commit()
        return {"message": f"Product {product_id} deleted"}, 200


api.add_resource(ProductsResource, "/api/products")
api.add_resource(ProductResource, "/api/products/<int:product_id>")

#---orders
class OrdersResource(Resource):
    def get(self):
        orders = Order.query.all()
        return [order.to_dict() for order in orders], 200
    

class OrderResource(Resource):
      def get(self, order_id):
        order = Order.query.get(order_id)
        if not order:
            return {"error": "Order not found"}, 404
        return order.to_dict(), 200
      
      def delete(self, order_id):
        order = Order.query.get(order_id)
        if not order:
            return {"error": "Order not found"}, 404

        db.session.delete(order)
        db.session.commit()
        return {"message": f"Order {order_id} deleted"}, 200
      
api.add_resource(OrdersResource, "/api/orders")
api.add_resource(OrderResource, "/api/orders/<int:order_id>") 


# ---reviews
class ReviewsResource(Resource):
    def get(self):
        reviews = Review.query.all()
        return [review.to_dict() for review in reviews], 200
    
    def post(self):
        data = request.get_json()

        if not data.get("user_id") or not data.get("product_id") or not data.get("rating"):
            return {"error": "user_id, product_id, and rating are required"}, 400

        # Validate product and user exist
        user = User.query.get(data["user_id"])
        product = Product.query.get(data["product_id"])
        if not user:
            return {"error": f"User {data['user_id']} not found"}, 404
        if not product:
            return {"error": f"Product {data['product_id']} not found"}, 404

        new_review = Review(
            user_id=data["user_id"],
            product_id=data["product_id"],
            rating=data["rating"],
            comment=data.get("comment", "")
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict(), 201


class ReviewResource(Resource):
    def get(self, review_id):
        review = Review.query.get(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review.to_dict(), 200
    
    def put(self, review_id):
        review = Review.query.get(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        data = request.get_json()
        review.rating = data.get("rating", review.rating)
        review.comment = data.get("comment", review.comment)

        db.session.commit()
        return review.to_dict(), 200
    
    def delete(self, review_id):
        review = Review.query.get(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        db.session.delete(review)
        db.session.commit()
        return {"message": f"Review {review_id} deleted"}, 200


# Register resources
api.add_resource(ReviewsResource, "/api/reviews")
api.add_resource(ReviewResource, "/api/reviews/<int:review_id>")




if __name__ == "__main__":
    app.run(debug=True, port=5500)
