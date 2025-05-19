from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open('hello.txt', 'r') as file:
        message = file.read()
    return render_template('index.html', message=message)


@app.route('/newpost/')
def new_post():
    return render_template('new-post.html')