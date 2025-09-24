#!/usr/bin/env python3

import random
from extensions import db
from models import User, Product, Order, Review
from faker import Faker

fake = Faker()

with app.app_context():
    print("🌱 Seeding database...")
  

    # ---- USERS ----
    print("Seeding users...")
    users = []
    user1 = User(
        username="alice",
        email="alice@example.com",
        password_hash=fake.password()
    )
    user2 = User(
        username="bob",
        email="bob@example.com",
        password_hash=fake.password()
    )
    user3 = User(
        username="charlie",
        email="charlie@example.com",
        password_hash=fake.password()
    )
    user4 = User(
        username="dave",
        email="dave@example.com",
        password_hash=fake.password()
    )
    user5 = User(
        username="eve",
        email="eve@example.com",
        password_hash=fake.password()
    )
    users.extend([user1, user2, user3, user4, user5])
    for user in users:
        db.session.add(user)
    db.session.commit()

    # ---- PRODUCTS ----
    print("Seeding products...")
    products =  []
    product1 = Product(
        name="Maize",
        description="Fresh and organic maize",
        price="50.00 ksh",
        stock=100,
        status="available",
        seller_id=user1.id
    )
    product2 = Product(
        name="Cabbages",
        description="Crisp and crunchy cabbages",
        price="70.00 ksh",
        stock=150,
        status="available",
        seller_id=user2.id
    )
    product3 = Product(
        name="Tomatoes",
        description="Juicy and ripe tomatoes",
        price="100.00 ksh",
        stock=200,
        status="reserved",
        seller_id=user3.id
    )
    product4 = Product(
        name="Potatoes",
        description="Earthy and flavorful potatoes",
        price="500.00 ksh",
        stock=250,
        status="sold out",
        seller_id=user4.id
    )
    product5 = Product(
        name="Onions",
        description="Sharp and zesty onions",
        price="20.00 ksh",
        stock=300,
        status="out of stock",
        seller_id=user5.id
    )
    product6 = Product(
        name="Garlic",
        description="Pungent and aromatic garlic",
        price="70.00 ksh",
        stock=350,
        status="reserved",
        seller_id=user1.id
    )
    product7 = Product(
        name="Sweet Potatoes",
        description="Sweet and starchy sweet potatoes",
        price="80.00 ksh",
        stock=400,
        status="available",
        seller_id=user2.id
    )
    product8 = Product(
        name="Cassava",
        description="Nutty and versatile cassava",
        price="90.00 ksh",
        stock=450,
        status="sold out",
        seller_id=user3.id
    )
    product9 = Product(
        name="Pumkins",
        description="Sweet and creamy pumkins",
        price="100.00 ksh",
        stock=500,
        status="out of stock",
        seller_id=user4.id
    )
    product10 = Product(
        name="Cucumbers",
        description="Cool and refreshing cucumbers",
        price="25.00 ksh",
        stock=550,
        status="available",
        seller_id=user5.id
    )
    products.extend([product1, product2, product3, product4, product5, product6, product7, product8, product9, product10])
    for product in products:
        db.session.add(product)
    db.session.commit()

    for order in Order.query.all():
        total = 0
        for _ in range(order.quantity):
            product = random.choice(products)
            total += int(product.price.split()[0])  
        order.total_amount = total
        db.session.add(order)
    db.session.commit()

    # ---- ORDERS ----
    # status = available, out of stock, delievered, reserved, sold out
    print("Seeding orders...")
    orders = []
    order1 = Order(
        buyer_id=user2.id,
        quantity=4,
        status="reserved",
        total_amount=0, 
        created_at=fake.date_time_this_year()
    )
    order2 = Order(
        buyer_id=user3.id,
        quantity=2,
        status="delivered",
        total_amount=0, 
        created_at=fake.date_time_this_year()
    )
    order3 = Order(
        buyer_id=user4.id,
        quantity=1,
        status="reserved",
        total_amount=0, 
        created_at=fake.date_time_this_year()
    )
    order4 = Order(
        buyer_id=user5.id,
        quantity=3,
        status="delievered",
        total_amount=0, 
        created_at=fake.date_time_this_year()
    )

    orders.extend([order1, order2, order3, order4])
    for order in orders:
        db.session.add(order)
    db.session.commit()


    for order in Order.query.all():
        total = 0
        for _ in range(order.quantity):
            product = random.choice(products)
            total += round(float(product.price.split()[0]))  
        order.total_amount = total
        db.session.add(order)
    db.session.commit()


    # ---- REVIEWS ----
    print("Seeding reviews...")
    reviews = []
    review1 = Review(
        rating=4,
        comment="Great product, very satisfied!",
        user=random.choice(users),
        product=random.choice(products),
        )
    review2 = Review(
        rating=5,
        comment="Exceeded my expectations!",
        user=random.choice(users),
        product=random.choice(products),
    )
    review3 = Review(
        rating=3,
        comment="Good quality, but a bit pricey.",
        user=random.choice(users),
        product=random.choice(products),
    )
    review4 = Review(
        rating=2,
        comment="Not as described, disappointed.",
        user=random.choice(users),
        product=random.choice(products),
    )
    review5 = Review(
        rating=1,
        comment="Poor quality, would not recommend.",
        user=random.choice(users),
        product=random.choice(products),
    )
    db.session.add_all([review1, review2, review3, review4, review5])
    db.session.commit()

    print(" Done seeding!")
