from flask import Flask
from config import SECRET_KEY

shortener = Flask(__name__)
shortener.config['SECRET_KEY'] = SECRET_KEY

from shortener import routes
