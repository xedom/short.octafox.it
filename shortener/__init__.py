from flask import Flask
from config import Config

shortener = Flask(__name__)
shortener.config.from_object(Config)

from shortener import routes
