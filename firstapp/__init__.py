import os

from flask import Flask, render_template

from firstapp.config import DebugConfig

app = Flask(__name__)
app.config.from_object(DebugConfig)


@app.route('/')
def index():
    return render_template('index.html')
    
def start_app():
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))