import datetime

from firstapp import db

class TimeStamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)