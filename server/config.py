import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///app.db" 
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for sessions / security
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
