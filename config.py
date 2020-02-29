import os

SECRET_KEY = os.urandom(32)
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB = os.getenv('MONGODB_DB')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')
