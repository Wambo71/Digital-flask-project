from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/auth/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "buyer")  

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400


    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password_hash=hashed_password,
        role=role
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "role": new_user.role
        }
    }), 201



@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    # if you’re using JWT
    from flask_jwt_extended import create_access_token
    access_token = create_access_token(identity=user.id)

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
    }), 200
