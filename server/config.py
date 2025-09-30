import os

class Config:
    ENV = os.getenv('APP_ENV', 'development')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False