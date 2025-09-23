from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import MetaData

metadata=MetaData()
db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    
    orders = db.relationship("Order", back_populates="user", cascade="all")
    reviews = db.relationship("Review", back_populates="user", cascade="all")


class Product(db.Model, SerializerMixin):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Integer, nullable=False)   
    stock = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users,id"))

    order_items = db.relationship("OrderItem", back_populates="product", cascade="all")
    
    user = db.relationship("User", back_populates= "products")

