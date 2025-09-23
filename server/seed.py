#!/usr/bin/env python3

import random
from faker import Faker

from app import app   # ✅ import the app directly
from extensions import db
from models import User, Product, Order, Review

fake = Faker()

with app.app_context():
    print("🌱 Seeding database...")

    # ---- Clear old data ----
    print("Deleting old data...")
    Review.query.delete()
    Order.query.delete()
    Product.query.delete()
    User.query.delete()

    # ---- USERS ----
    print("Seeding users...")
    users = []
    for _ in range(5):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password_hash=fake.password()
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()

    # ---- PRODUCTS ----
    print("Seeding products...")
    products = []
    for _ in range(10):
        product = Product(
            name=fake.word().title(),
            description=fake.sentence(),
            price=round(random.uniform(10, 500), 2),
            stock=random.randint(1, 100),
            seller=random.choice(users)
        )
        products.append(product)
        db.session.add(product)
    db.session.commit()

    # ---- ORDERS ----
    print("Seeding orders...")
    for _ in range(8):
        order = Order(
            quantity=random.randint(1, 5),
            buyer=random.choice(users),
            total_amount=0,  # will calculate below
            status=random.choice(["pending", "shipped", "delivered"]),
            created_at=fake.date_time_this_year()
        )
        db.session.add(order)
    db.session.commit()

    # ---- REVIEWS ----
    print("Seeding reviews...")
    for _ in range(15):
        review = Review(
            rating=random.randint(1, 5),
            comment=fake.sentence(),
            product=random.choice(products),
        )
        db.session.add(review)
    db.session.commit()

    print("✅ Done seeding!")
