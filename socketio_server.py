import threading
import eventlet
import socketio
from neo_strip import NeoPixelStrip
import yaml
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
    neo_strip.change_brightness(brightness)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    with open('config/settings.yaml') as f:
        settings = yaml.full_load(f)

    LED_COUNT = settings['LED_COUNT']     
    port = settings['PORT']  
    neo_strip = NeoPixelStrip(LED_COUNT)
    eventlet.wsgi.server(eventlet.listen(('', port)), app)
