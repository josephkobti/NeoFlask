import threading
import board
import neopixel
import eventlet
import socketio

# Socket Setup 
sio = socketio.Server()
app = socketio.WSGIApp(sio)

# Neo Setup
ORDER = neopixel.GRBW
pixels = neopixel.NeoPixel(board.D18, 180, brightness=0.5, auto_write=False, pixel_order=ORDER)

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def my_message(sid, data):
    if data['switch'] == 'on':
        pixels.fill((128,128,128,0))
        pixels.show()
    elif data['switch'] == 'off':
        pixels.fill((0,0,0,0))
        pixels.show()

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)