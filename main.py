from flask import Flask
app = Flask(__name__)
import socketio
import time 

sio = socketio.Client()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/start')
def start():
    sio.emit('my_message', {'switch': 'on'})
    return 'started'

@app.route('/stop')
def stop():
    sio.emit('my_message', {'switch': 'off'})
    return 'stopped'

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