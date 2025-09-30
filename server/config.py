import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"  # Provided by Render
    SQLALCHEMY_TRACK_MODIFICATIONS = False