"""test Flask with this"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'


@app.route('/newpost/')
def new_post():
    return 'New Post page'