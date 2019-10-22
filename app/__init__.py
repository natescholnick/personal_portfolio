# From the flask.py file, import the Flask class

from flask import Flask
from flask_bootstrap import Bootstrap
# Create instance of Flask class in order to run this application
# name parameter will default to the folder name
app = Flask(__name__)

bootstrap = Bootstrap(app)
# From the app folder, import routes.py and startup at the index route
from app import routes
