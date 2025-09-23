from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend requests

@app.route("/")
def hello():
    return "<h1>Welcome to backend</h1>"

if __name__ == "__main__":
    app.run(debug=True)