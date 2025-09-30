#!/usr/bin/env python3
from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_bcrypt import Bcrypt
import os
from extensions import db
from config import Config
from models import User, Product, Order, OrderItem, Review


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
bcrypt = Bcrypt(app)

CORS(app, supports_credentials=True)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "buyer")

    if not username or not email or not password:
        return {"error": "Username, email, and password are required"}, 400

    if User.query.filter_by(email=email).first():
        return {"error": "Email already exists"}, 400
    if User.query.filter_by(username=username).first():
        return {"error": "Username already exists"}, 400

    new_user = User(
        username=username,
        email=email,
        role=role
    )
    new_user.set_password(password)  

    db.session.add(new_user)
    db.session.commit()

    return {"message": "User created successfully", "user": new_user.to_dict()}, 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return {"error": "Email and password are required"}, 400

    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password_hash, password):
        session['user_id'] = user.id
        session['role'] = getattr(user, "role", "buyer")
        return {"message": "Login successful", "user": user.to_dict()}, 200

    return {"error": "Invalid email or password"}, 401

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return {"message": "Logged out successfully"}, 200

class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users], 200

    def post(self):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return {"error": "username, email, and password are required"}, 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password_hash=hashed_password, role=data.get("role", "buyer"))
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
        if "password" in data:
            user.password_hash = bcrypt.generate_password_hash(data["password"]).decode('utf-8')

        db.session.commit()
        return user.to_dict(), 200

    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user_id} deleted"}, 200

# products
class ProductsResource(Resource):
    def get(self):
        products = Product.query.all()
        return [product.to_dict() for product in products], 200

    def post(self):
        data = request.get_json()
        name = data.get("name")
        price = data.get("price")
        seller_id = data.get("seller_id")

        if not name or not price or not seller_id:
            return {"error": "name, price, and seller_id are required"}, 400

        new_product = Product(
            name=name,
            description=data.get("description"),
            price=price,
            seller_id=seller_id,
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

#oders
class OrdersResource(Resource):
    def get(self):
        orders = Order.query.all()
        return [order.to_dict() for order in orders], 200

    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)
        total_amount = data.get("total_amount", 0)

        if not user_id or not product_id:
            return {"error": "user_id and product_id are required"}, 400

        new_order = Order(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity,
            total_amount=total_amount,
            status=data.get("status", "pending")
        )
        db.session.add(new_order)
        db.session.commit()
        return new_order.to_dict(), 201

class OrderResource(Resource):
    def get(self, order_id):
        order = Order.query.get(order_id)
        if not order:
            return {"error": "Order not found"}, 404
        return order.to_dict(), 200

    def put(self, order_id):
        order = Order.query.get(order_id)
        if not order:
            return {"error": "Order not found"}, 404

        data = request.get_json()
        order.status = data.get("status", order.status)
        order.quantity = data.get("quantity", order.quantity)
        order.total_amount = data.get("total_amount", order.total_amount)
        db.session.commit()
        return order.to_dict(), 200

    def delete(self, order_id):
        order = Order.query.get(order_id)
        if not order:
            return {"error": "Order not found"}, 404

        db.session.delete(order)
        db.session.commit()
        return {"message": f"Order {order_id} deleted"}, 200
#order items
class OrderItemsResource(Resource):
    def get(self):
        items = OrderItem.query.all()
        return [item.to_dict() for item in items], 200

    def post(self):
        data = request.get_json()
        order_id = data.get("order_id")
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)
        total_amount = data.get("total_amount", 0)

        if not order_id or not product_id:
            return {"error": "order_id and product_id are required"}, 400

        new_item = OrderItem(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            total_amount=total_amount,
            status=data.get("status", "pending")
        )
        db.session.add(new_item)
        db.session.commit()
        return new_item.to_dict(), 201

class OrderItemResource(Resource):
    def get(self, item_id):
        item = OrderItem.query.get(item_id)
        if not item:
            return {"error": "Order item not found"}, 404
        return item.to_dict(), 200

    def put(self, item_id):
        item = OrderItem.query.get(item_id)
        if not item:
            return {"error": "Order item not found"}, 404

        data = request.get_json()
        item.status = data.get("status", item.status)
        item.quantity = data.get("quantity", item.quantity)
        item.total_amount = data.get("total_amount", item.total_amount)
        db.session.commit()
        return item.to_dict(), 200

    def delete(self, item_id):
        item = OrderItem.query.get(item_id)
        if not item:
            return {"error": "Order item not found"}, 404

        db.session.delete(item)
        db.session.commit()
        return {"message": f"Order item {item_id} deleted"}, 200

#reviews
class ReviewsResource(Resource):
    def get(self):
        reviews = Review.query.all()
        return [review.to_dict() for review in reviews], 200

    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        product_id = data.get("product_id")
        rating = data.get("rating")

        if not user_id or not product_id or not rating:
            return {"error": "user_id, product_id, and rating are required"}, 400

        user = User.query.get(user_id)
        product = Product.query.get(product_id)

        if not user:
            return {"error": f"User {user_id} not found"}, 404
        if not product:
            return {"error": f"Product {product_id} not found"}, 404

        new_review = Review(
            user_id=user_id,
            product_id=product_id,
            rating=rating,
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

api.add_resource(UsersResource, "/users")
api.add_resource(UserResource, "/users/<int:user_id>")
api.add_resource(ProductsResource, "/products")
api.add_resource(ProductResource, "/products/<int:product_id>")
api.add_resource(OrdersResource, "/orders")
api.add_resource(OrderResource, "/orders/<int:order_id>")
api.add_resource(OrderItemsResource, "/order_items")
api.add_resource(OrderItemResource, "/order_items/<int:item_id>")
api.add_resource(ReviewsResource, "/reviews")
api.add_resource(ReviewResource, "/reviews/<int:review_id>")

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")


if __name__ == "__main__":
    app.run(debug=True, port=5500)