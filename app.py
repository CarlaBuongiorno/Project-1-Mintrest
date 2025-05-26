from flask import Flask, render_template

import datetime


app = Flask(__name__)


@app.route('/')
def index():
    with open('hello.txt', 'r') as file:
        mintrest_data = file.readlines()
        pins_data = process_line(mintrest_data)
        pin_data = group_pins(pins_data)
        pins = [create_pin(date=pin[0], title=pin[1], description=pin[2], image=pin[3]) for pin in pin_data]
    return render_template('index.html', pins=pins)


def process_line(mintrest_data):
    # Put all the lines into a single list
    return [line.strip() for line in mintrest_data]


def group_pins(pins):
    # Separate the single list items into lists containing 4 items
    # (title, description, image)
    # Each list is 1 pin
    return [pins[i:i+4] for i in range(0, len(pins), 4)]
     

def create_pin(date, title, description, image):
    # Create a list dictionaries for each each pin)
    return {
        'date': get_date(date),
        'title': title,
        'description': description,
        'image': image
    }


def get_date(date):
    # Displays the recorded date
    date = datetime.datetime.fromtimestamp(int(date))
    return date.strftime("%d %B %Y")


@app.route('/newpost/')
def new_post():
    return render_template('new-post.html')