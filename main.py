from flask import Flask, render_template
app = Flask(__name__)
import socketio
import time 
from flask_bootstrap import Bootstrap
Bootstrap(app)
sio = socketio.Client()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/start')
def start():
    sio.emit('my_message', {'switch': 'on'})
    return render_template('index.html')

@app.route('/stop')
def stop():
    sio.emit('my_message', {'switch': 'off'})
    return render_template('index.html')

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5001')