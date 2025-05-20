from flask import Flask, render_template

import datetime


app = Flask(__name__)


@app.route('/')
def index():
    with open('hello.txt', 'r') as file:
        messages = [process_line(line) for line in file]
    return render_template('index.html', messages=messages)


def process_line(line):
    '''Split each line at the first space and return the date string and message'''
    time, msg = line.strip().split(' ', maxsplit=1)
    date = datetime.datetime.fromtimestamp(float(time))
    return date.strftime("%d %B %Y"), msg


@app.route('/newpost/')
def new_post():
    return render_template('new-post.html')