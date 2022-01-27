from models.event import *

event1 = Event("01/01/22", "John's Birthday Party", 25, "office", "birthday party for john: BYOB", True)
event2 = Event("21/02/22", "Dave's Graduation", 5000, "Campus", "Graduation for Dave: BYOB", False)
events = [event1, event2]

def add_new_event(event):
    events.append(event)