import threading
import eventlet
import socketio
from neo_strip import NeoPixelStrip

# Socket Setup 
sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    if data['switch'] == 'on':
        print('turned on')
        neo_strip.turn_on()
    elif data['switch'] == 'off':
        print('turned off')
        neo_strip.turn_off()

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    neo_strip = NeoPixelStrip()
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)
