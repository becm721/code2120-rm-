
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from rhino3dm import *

app = Flask(__name__)

@app.route('/urlend')
def hello_world():
    return 'Hello from Flask!'
def test_something():
    input("Say something ")
    return test_something