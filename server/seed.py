import random
from app import app, bcrypt
from extensions import db
from models import User, Product, Order, OrderItem, Review
from faker import Faker

fake = Faker()

with app.app_context():
    print("Clearing database...")
    OrderItem.query.delete()
    Order.query.delete()
    Review.query.delete()
    Product.query.delete()
    User.query.delete()
    db.session.commit()

    print("Seeding users...")
    users = []
    user_data = [
        ("Alice Komie", "alice@example.com", "seller"),
        ("Bob Marley", "bob@example.com", "buyer"),
        ("Charlie Puth", "charlie@example.com", "buyer"),
        ("Dave Grohl", "dave@example.com", "buyer"),
        ("Eve Online", "eve@example.com", "seller"),
    ]

    for username, email, role in user_data:
        password_hash = bcrypt.generate_password_hash("password123").decode("utf-8")
        user = User(username=username, email=email, password_hash=password_hash, role=role)
        db.session.add(user)
        users.append(user)
    db.session.commit()

    print("Seeding products...")
    products_data = [
        ("Maize", "Fresh and organic maize", 50, 100, "available", users[0].id, "/static/images/maize.jpg"),
        ("Cabbages", "Crisp and crunchy cabbages", 70, 150, "available", users[1].id, "/static/images/cabbage.jpg"),
        ("Tomatoes", "Juicy and ripe tomatoes", 100, 200, "reserved", users[2].id, "/static/images/tomatoes.jpg"),
        ("Potatoes", "Earthy and flavorful potatoes", 500, 250, "sold out", users[3].id, "/static/images/potatoes.jpg"),
        ("Onions", "Sharp and zesty onions", 20, 300, "out of stock", users[4].id, "/static/images/onions.jpg"),
        ("Garlic", "Pungent and aromatic garlic", 70, 350, "reserved", users[0].id, "/static/images/garlic.jpg"),
        ("Sweet Potatoes", "Sweet and starchy sweet potatoes", 80, 400, "available", users[1].id, "/static/images/potatoes.jpg"),
        ("Cassava", "Nutty and versatile cassava", 90, 450, "sold out", users[2].id, "/static/images/cassava.jpg"),
        ("Carrot", "Crunchy and sweet carrots", 100, 500, "out of stock", users[3].id, "/static/images/carrot.jpg"),
        ("Cucumbers", "Cool and refreshing cucumbers", 25, 550, "available", users[4].id, "/static/images/cucumber.jpg"),
    ]
    products = []
    for name, desc, price, stock, status, seller_id, img in products_data:
        product = Product(name=name, description=desc, price=price, stock=stock, status=status, seller_id=seller_id, image_url=img)
        db.session.add(product)
        products.append(product)
    db.session.commit()

    print("Seeding orders...")
    orders = []
    for buyer in users[1:]:  # buyers only
        order = Order(
            buyer_id=buyer.id,
            quantity=random.randint(1, 5),
            status=random.choice(["pending", "shipped", "delivered"]),
            total_amount=0
        )
        db.session.add(order)
        orders.append(order)
    db.session.commit()

    # Assign products to orders and calculate total
    print("Seeding order items...")
    for order in orders:
        total = 0
        for _ in range(order.quantity):
            product = random.choice(products)
            price = product.price
            order_item = OrderItem(order_id=order.id, product_id=product.id, quantity=1, price=price)
            db.session.add(order_item)
            total += price
        order.total_amount = total
        db.session.add(order)
    db.session.commit()

    print("Seeding reviews...")
    for _ in range(10):
        review = Review(
            rating=random.randint(1, 5),
            comment=fake.sentence(),
            user_id=random.choice(users).id,
            product_id=random.choice(products).id
        )
        db.session.add(review)
    db.session.commit()

    print("Database seeding complete!")
