import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key_123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
