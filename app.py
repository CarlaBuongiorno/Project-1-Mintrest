from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open('hello.txt', 'r') as file:
        messages = [message.strip() for message in file]
    return render_template('index.html', messages=messages)


@app.route('/newpost/')
def new_post():
    return render_template('new-post.html')