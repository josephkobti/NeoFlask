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
def switch(sid, data):
    if data['status'] == 'off':
        neo_strip.turn_off()
    elif data['status'] == 'on':
        neo_strip.switch(data['red'], data['green'], data['blue'], data['white'])

@sio.event
def change_brightness(sid, data):
    brightness = data['b']
    brightness = float(brightness)
    brightness = brightness / 100
    print(brightness)
    neo_strip.change_brightness(data['red'], data['green'], data['blue'], data['white'], brightness)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    neo_strip = NeoPixelStrip()
    eventlet.wsgi.server(eventlet.listen(('', 5002)), app)
