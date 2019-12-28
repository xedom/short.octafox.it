from flask import Flask

shortener = Flask(__name__)

from shortener import routes
