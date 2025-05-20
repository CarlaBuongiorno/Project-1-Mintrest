from flask import Flask, render_template

import datetime


app = Flask(__name__)


@app.route('/')
def index():
    with open('hello.txt', 'r') as file:
        date = datetime.datetime.now()
        messages = [message.strip() for message in file]
    return render_template('index.html', messages=messages, date=date.strftime("%d %B %Y"))


@app.route('/newpost/')
def new_post():
    return render_template('new-post.html')