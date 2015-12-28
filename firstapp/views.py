import random
import string

from flask import render_template

from firstapp import app, db
from firstapp.models import TimeStamp, Stuff

def generate_string():
    return ''.join([random.choice(string.ascii_uppercase) for _ in range(8)])

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/timestamp')
def timestamp():
    ts = TimeStamp()
    
    db.session.add(ts)
    
    stuff = Stuff(content=generate_string(), timestamp=ts)
    
    db.session.add(stuff)
    
    db.session.commit()
    
    return '{}'.format(stuff.id)
    
@app.route('/stuff/<int:id>')
def get_stuff(id):
    stuff = Stuff.query.get(id)
    if stuff is None:
        return 'no stuff found'
    else:
        return '{}, {}'.format(stuff.content, stuff.timestamp.current_time)