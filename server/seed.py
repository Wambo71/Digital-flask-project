import random
from app import app
from extensions import db
from models import User, Product, Order, Review, OrderItem
from faker import Faker

fake = Faker()

with app.app_context():
    User.query.delete()
    db.session.commit()

    print("Seeding database...")
# users
    print("Seeding users...")
    users = []
    user1 = User(
        username="Alice Komie",
        email="alice@example.com",
        password_hash=fake.password(),
        role="seller"
    )
    user2 = User(
        username="Bob Marley",
        email="bob@example.com",
        password_hash=fake.password(),
        role="buyer"
    )
    user3 = User(
        username="Charlie Puth",
        email="charlie@example.com",
        password_hash=fake.password(),
        role="buyer"
    )
    user4 = User(
        username="Dave Grohl",
        email="dave@example.com",
        password_hash=fake.password(),
        role="buyer"
    )
    user5 = User(
        username="Eve Online",
        email="eve@example.com",
        password_hash=fake.password(),
        role="seller"
    )
    users.extend([user1, user2, user3, user4, user5])
    for user in users:
        db.session.add(user)
    db.session.commit()
# products
    Product.query.delete()
    db.session.commit()

    print("Seeding products...")
    products =  []
    product1 = Product(
        name="Maize",
        description="Fresh and organic maize",
        price="30.00 ksh per maize",
        stock=100,
        status="available",
        seller_id=user1.id,
        image_url="https://assets.grok.com/users/8f2f0d28-2e2a-4944-8700-cb09a56bba54/generated/a637810c-7039-4274-b9b2-f34993a9427b/image.jpg"
        )
    product2 = Product(
        name="Cabbages",
        description="Crisp and crunchy cabbages",
        price="70.00 ksh per cabbage",
        stock=150,
        status="available",
        seller_id=user2.id,
        image_url="https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?q=80&w=985&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    )
    product3 = Product(
        name="Tomatoes",
        description="Juicy and ripe tomatoes",
        price="10 ksh per tomato",
        stock=200,
        status="reserved",
        seller_id=user3.id,
        image_url="https://images.unsplash.com/photo-1742805286691-04a69edc3874?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    )
    product4 = Product(
        name="Potatoes",
        description="Earthy and flavorful potatoes",
        price="500.00 ksh per bucket",
        stock=250,
        status="sold out",
        seller_id=user4.id,
        image_url="https://assets.grok.com/users/8f2f0d28-2e2a-4944-8700-cb09a56bba54/generated/0319c633-39bd-46c5-8213-4fa6a8684293/image.jpg"
    )
    product5 = Product(
        name="Onions",
        description="Sharp and zesty onions",
        price="15.00 ksh per onion",
        stock=300,
        status="out of stock",
        seller_id=user5.id,
        image_url="https://plus.unsplash.com/premium_photo-1668076517573-fa01307d87ad?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    )
    product6 = Product(
        name="Garlic",
        description="Pungent and aromatic garlic",
        price="70.00 ksh per kilogram",
        stock=350,
        status="reserved",
        seller_id=user1.id,
        image_url="https://assets.grok.com/users/8f2f0d28-2e2a-4944-8700-cb09a56bba54/generated/0042c037-7fd3-44ba-99ad-ea50d4e98bfb/image.jpg"
    )
    product7 = Product(
        name="Sweet Potatoes",
        description="Sweet and starchy sweet potatoes",
        price="300.00 ksh per minibucket",
        stock=400,
        status="available",
        seller_id=user2.id,
        image_url="https://assets.grok.com/users/8f2f0d28-2e2a-4944-8700-cb09a56bba54/generated/b83763ef-37bf-47f9-9697-90ae7163fa05/image.jpg"
    )
    product8 = Product(
        name="Cassava",
        description="Nutty and versatile cassava",
        price="90.00 ksh per cassava",
        stock=450,
        status="sold out",
        seller_id=user3.id,
        image_url="https://assets.grok.com/users/8f2f0d28-2e2a-4944-8700-cb09a56bba54/generated/3e894267-7876-412a-a39a-f6b86d6db812/image.jpg"
    )
    product9 = Product(
        name="Carrot",
        description="Crunchy and sweet carrots",
        price="100.00 ksh per kilogram",
        stock=500,
        status="out of stock",
        seller_id=user4.id,
        image_url="https://assets.grok.com/users/8f2f0d28-2e2a-4944-8700-cb09a56bba54/generated/b23b1d98-3f9c-43c7-9303-74cd816efe6f/image.jpg"
    )
    product10 = Product(
        name="Cucumbers",
        description="Cool and refreshing cucumbers",
        price="25.00 ksh per cucumber",
        stock=550,
        status="available",
        seller_id=user5.id,
        image_url="https://assets.grok.com/users/8f2f0d28-2e2a-4944-8700-cb09a56bba54/generated/d7196f58-7667-41e8-b566-ba7082fdea65/image.jpg"
    )
    products.extend([product1, product2, product3, product4, product5, product6, product7, product8, product9, product10])
    for product in products:
        db.session.add(product)
        db.session.commit()

# orders
    Order.query.delete()
    db.session.commit()

    print("Seeding orders...")
    orders = []
    order1 = Order(
        buyer_id=user2.id,
        quantity=4,
        status="pending",
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
        status="shipped",
        total_amount=0, 
        created_at=fake.date_time_this_year()
    )
    order4 = Order(
        buyer_id=user5.id,
        quantity=3,
        status="delivered",
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
# orderitems
    OrderItem.query.delete()
    db.session.commit()

    print("Seeding order items...")
    order_items = []
    order_item1 = OrderItem(
        order_id=order1.id,
        product_id=product1.id,
        quantity=4,
        price=product1.price
    )
    order_item2 = OrderItem(
        order_id=order1.id,
        product_id=product2.id,
        quantity=2,
        price=product2.price
    )
    for order in OrderItem.query.all():
        total = 0
        for _ in range(order.quantity):
            product = random.choice(products)
            total += int(product.price.split()[0])  
        order.total_amount = total
        db.session.add(order)
    db.session.commit()
# reviews
    Review.query.delete()
    db.session.commit()

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
