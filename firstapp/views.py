from flask import render_template

from firstapp import app, db
from firstapp.models import TimeStamp

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/timestamp')
def timestamp():
    ts = TimeStamp()
    
    db.session.add(ts)
    db.session.commit()
    
    return '{}'.format(ts.id)