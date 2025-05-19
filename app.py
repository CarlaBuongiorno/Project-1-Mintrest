from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/newpost/')
def new_post():
    return render_template('new-post.html')