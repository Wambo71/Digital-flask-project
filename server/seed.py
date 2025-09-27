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
        price="50.00 ksh",
        stock=100,
        status="available",
        seller_id=user1.id,
        image_url = "maize.jpg"   
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
        seller_id=user5.id,
        image_url= "onions.jpg"
    )
    product6 = Product(
        name="Garlic",
        description="Pungent and aromatic garlic",
        price="70.00 ksh",
        stock=350,
        status="reserved",
        seller_id=user1.id,
        image_url = "garlic.jpg"
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
        name="Carrot",
        description="Crunchy and sweet carrots",
        price="100.00 ksh",
        stock=500,
        status="out of stock",
        seller_id=user4.id,
        image_url = "carrot.jpg"
    )
    product10 = Product(
        name="Cucumbers",
        description="Cool and refreshing cucumbers",
        price="25.00 ksh",
        stock=550,
        status="available",
        seller_id=user5.id,
        image_url = "cucumbers.jpg"
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
