from flask import render_template, request
from app import app
from models.event import Event
from models.events_list import events, add_new_event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['post'])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name_of_event']
    event_capacity = request.form['number_of_guests']
    event_location = request.form['room_location']
    event_description = request.form['description']
    event_recurring = request.form['recurring']
    new_event = Event(event_date, event_name, event_capacity, event_location, event_description, event_recurring)
    add_new_event(new_event)
    return render_template('index.html', title='Home', events=events)
