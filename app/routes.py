# Import app variable instance in order to run application + necessary functions
from app import app
from flask import render_template

# Create all routes associated with the application, starting with the index
# flask app always starts up on '/' which is the base route
@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    return render_template('index.html', title=title)


@app.route('/about')
def about():
    title = 'About'
    return render_template('about.html', title=title)
