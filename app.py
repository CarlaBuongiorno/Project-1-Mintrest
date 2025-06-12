from flask import Flask, render_template, request, redirect, url_for

import datetime


app = Flask(__name__)


@app.route('/')
def index():
    with open('pins.txt', 'r') as file:
        mintrest_data = file.readlines()
        pins_data = process_line(mintrest_data)
        pin_data = group_pins(pins_data)
        pins = [create_pin(date=pin[0], title=pin[1], description=pin[2], image=pin[3]) for pin in pin_data]
        sorted_pins = sorted(pins, key=lambda x: x['timestamp'], reverse=True)
    new_post = 'New Post'
    return render_template('index.html', pins=sorted_pins, new_post=new_post)


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
        'timestamp': date,
        'date': get_date(date),
        'title': title,
        'description': description,
        'image': image
    }


def get_date(date):
    # Displays the recorded date
    date = datetime.datetime.fromtimestamp(float(date))
    return date.strftime("%d %B %Y")


@app.route('/newpost/', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_data = get_post_data()
        save_post_to_file(post_data)
        return redirect(url_for('index'))
    return render_template('new-post.html')


def get_post_data():
    return {
        'date': get_current_date(),
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'image': request.form.get('image')
    }


def get_current_date():
    current_date = datetime.datetime.now()
    return current_date.timestamp()


def save_post_to_file(post_data):
    with open('pins.txt', 'a') as file:
        file.write(f'{post_data['date']}\n{post_data['title']}\n{post_data['description']}\n{post_data['image']}\n')