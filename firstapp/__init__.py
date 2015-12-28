import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from firstapp.config import DebugConfig, ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

db = SQLAlchemy(app)

from firstapp import views
    
def start_app():
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))