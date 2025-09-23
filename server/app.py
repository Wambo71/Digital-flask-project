from flask import Flask, jsonify
from flask_cors import CORS
from extensions import db, migrate, ma
# from model import User, Product, Order

app = Flask(__name__)
CORS(app)  

@app.route("/")
def hello():
    return "<h1>Welcome to backend</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5500)