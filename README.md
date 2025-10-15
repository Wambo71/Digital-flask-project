🛒 Digital Marketplace [Full E-Commerce] (Flask + React)

A full-stack web application that allows buyers and sellers to interact through product listings, cart management, reviews, and secure authentication.

✅ Features
👤 User Management

Sign up & login

Role-based access: buyer or seller

Password hashing with bcrypt

🛍 Products

Sellers can add and manage products

Buyers can view products and product details

Product statuses:

available

out of stock

reserved

sold out

🛒 Cart & Checkout

Add/remove products from cart

View cart items

Proceed to checkout

⭐ Reviews

Users can leave reviews on products

Ratings between 1–5

🔒 Protected Routes (Frontend)

Only logged-in users can:

View products

Access profile

View product details

Only sellers can add products

🏗️ Tech Stack
✅ Backend (Flask)

Flask

SQLAlchemy

Flask-Bcrypt

SerializerMixin

Validations using @validates

SQLite/PostgreSQL (depending on setup)

✅ Frontend (React)

React Router DOM

Protected routing (custom component)

useState for cart management

Component-based pages

CSS styling

Optional Toaster notifications

📁 Project Structure (Summary)
🔹 Backend (models.py)

Defines database models:

User

Product

Order

OrderItem

Review

Handles:

Relationships

Cascade deletes

Validations

Serialization

Password hashing

🔹 Frontend (App.jsx)

Handles:

Routing

Protected routes

Cart state

Navigation

Pages include:

Home

Login

Signup

Products

Product Details

Profile

Add Product

Cart

Checkout


🚀 How to Run the Project
1️⃣ Backend Setup
```
pip install -r requirements.txt
flask db upgrade   # or flask db init & migrate
flask run
```
Frontend Setup
```
cd client
npm install
npm run dev
```

✅ Models Overview

Each model has relationships and validators:

👤 User

Roles: buyer or seller

Password hashing methods

Validations for email, role, username

📦 Product

Linked to User (seller)

Status validation

🛒 Order & OrderItem

Many-to-many link between buyers and products

⭐ Review

Linked to product and user

Rating validation (1-5)

🔐 Authentication & Authorization

Passwords stored securely using bcrypt

ProtectedRoute component ensures:

Only logged-in users access private pages

Sellers-only access to adding products

Author:Eddah Kibet
