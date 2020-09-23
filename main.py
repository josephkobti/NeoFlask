from flask import Flask, render_template, request
app = Flask(__name__)
import socketio
import time 
from flask_bootstrap import Bootstrap
Bootstrap(app)
sio = socketio.Client()

status = 'off'
red = '255'
green = '255'
blue = '255'
white = '255'
brightness = 10

@app.route('/')
def index():
    global brightness
    return render_template('index.html', brightness=brightness, status = status)

@app.route('/switch')
def switch():
    global white, red, green, blue
    white = request.args.get('w')
    red = request.args.get('r')
    green = request.args.get('g')
    blue = request.args.get('b')
    sio.emit('switch', {'status': 'on', 'red': red, 'green': green, 'blue': blue, 'white' : white})
    status = 'on'
    return {"msg": "Changed Successfully"}, 200


@app.route('/turn_off')
def stop():
    sio.emit('switch', {'status': 'off'})
    status = 'off'
    return {"msg": "Changed Successfully"}, 200

@app.route('/turn_on')
def start():
    sio.emit('switch', {'status': 'on', 'red': red, 'green': green, 'blue': blue, 'white' : white})
    sio.emit('change_brightness', {'status': 'on', 'red': red, 'green': green, 'blue': blue, 'white' : white, 'b' : brightness})
    status = 'on'
    return {"msg": "Changed Successfully"}, 200

@app.route('/brightness')
def change_brightness():
    print(request.args.get('b'))
    global brightness
    brightness = request.args.get('b')
    print(brightness)
    sio.emit('change_brightness', {'status': 'on', 'red': red, 'green': green, 'blue': blue, 'white' : white, 'b' : brightness})
    return {"msg": "Changed Successfully"}, 200
    

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('change_brightness', {'b': request.args.get('b')})
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5002')