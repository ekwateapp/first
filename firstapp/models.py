import datetime

from firstapp import db

class TimeStamp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
class Stuff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(64))
    time_stamp_id = db.Column(db.Integer, db.ForeignKey('time_stamp.id'))
    timestamp = db.relationship(TimeStamp, backref=db.backref('stuff', lazy='dynamic'))