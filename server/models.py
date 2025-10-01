from extensions import db, bcrypt
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

# ------------------ USER MODEL ------------------
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ("-password_hash", "-orders", "-reviews", "-products")

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="buyer")

    # Relationships
    products = db.relationship("Product", back_populates="seller", cascade="all, delete-orphan")
    orders = db.relationship("Order", back_populates="buyer", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")

    # Password methods
    def set_password(self, password):
        """Hash and set the user's password."""
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Verify the user's password."""
        return bcrypt.check_password_hash(self.password_hash, password)

    # Validators
    @validates("email")
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Invalid email format")
        return email

    @validates("role")
    def validate_role(self, key, role):
        if role not in ['buyer', 'seller']:
            raise ValueError("Role must either be buyer or seller")
        return role

    @validates("username")
    def validate_username(self, key, username):
        if len(username) < 4:
            raise ValueError("Username must be at least 4 characters")
        return username

    def __repr__(self):
        return f"<User {self.username}>"


# ------------------ PRODUCT MODEL ------------------
class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    serialize_rules = (
        "-seller.password_hash",
        "-order_items",
        "-reviews",
        "-reviews.user.password_hash",
        "-seller.products",
        "-reviews.product",
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.String(50), nullable=False, default="available")
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image_url = db.Column(db.Text(500))

    seller = db.relationship("User", back_populates="products")
    order_items = db.relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="product", cascade="all, delete-orphan")

    @validates("status")
    def validate_status(self, key, status):
        allowed = ["available", "out of stock", "reserved", "sold out"]
        if status not in allowed:
            raise ValueError("Invalid product status")
        return status

    def __repr__(self):
        return f"<Product {self.name}>"


# ------------------ ORDER MODEL ------------------
class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    serialize_rules = ("-buyer.password_hash", "-order_items")

    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    quantity = db.Column(db.Integer, nullable=False, default=1)

    buyer = db.relationship("User", back_populates="orders")
    order_items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    @validates("status")
    def validate_status(self, key, status):
        allowed = ["pending", "completed", "cancelled", "shipped", "delivered"]
        if status not in allowed:
            raise ValueError("Invalid order status")
        return status

    def __repr__(self):
        return f"<Order {self.id} by Buyer {self.buyer_id}>"


# ------------------ ORDER ITEM MODEL ------------------
class OrderItem(db.Model, SerializerMixin):
    __tablename__ = "order_items"

    serialize_rules = ("-order.buyer.password_hash", "-product.seller.password_hash")

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    order = db.relationship("Order", back_populates="order_items")
    product = db.relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem {self.id} for Order {self.order_id}>"


# ------------------ REVIEW MODEL ------------------
class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    serialize_rules = (
        "-user.password_hash",
        "-user.reviews",
        "-product.reviews",
        "-product.seller.products",
    )

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)

    user = db.relationship("User", back_populates="reviews")
    product = db.relationship("Product", back_populates="reviews")

    @validates("rating")
    def validate_rating(self, key, rating):
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating

    def __repr__(self):
        return f"<Review {self.id} by User {self.user_id}>"
