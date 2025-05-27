from flask import Flask, render_template, request

import datetime


app = Flask(__name__)


@app.route('/')
def index():
    with open('pins.txt', 'r') as file:
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
    date = datetime.datetime.fromtimestamp(float(date))
    return date.strftime("%d %B %Y")


@app.route('/newpost/')
def new_post():
    return render_template('new-post.html')


@app.route('/', methods=['POST'])
def add_post():
    date = get_current_date()
    title = request.form.get('title')
    image = request.form.get('image')
    description = request.form.get('description')
    with open('pins.txt', 'a') as file:
        file.write(f'{date}\n{title}\n{description}\n{image}\n')
    return render_template('index.html', title=title, image=image, description=description)


def get_current_date():
    current_date = datetime.datetime.now()
    return current_date.timestamp()