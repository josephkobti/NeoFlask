# Setup: 
The socketio server and the socketio client in the flask app talk over the same port. 
* For the server: write the PORT_ID in `eventlet.wsgi.server(eventlet.listen(('', PORT_ID)), app)` in socketio_server.py. for example 5002
* For the client: write the same PORT_ID in `sio.connect('http://localhost:PORT_ID')`

* The `neo_strip.py` file has the class for the neo strip, the file `socketio_server.py` instantiates the class with the proper number of leds which also can be configuered in `settings.yaml`.

# Running the apps: 
* To run the Socketio Server that controls the Neo strip:
   
  `sudo python socketio_server.py`

* To run the front end flask app: 
  
`export FLASK_APP=/home/pi/Documents/projects/NeoFlask/main.py`
`python3 -m flask run --host=0.0.0.0`
this app can be accessed from local network using the ip of raspbery pi plus the port at the end, as in `192.168.188.81:5000`

# Running the apps on start-up: 
The files `flask.service` and `socketio.service` are systemd service files. 
Variables in these services need to be edited first:
* `FLASK_APP` is the path to the main.py file in this project
* `User` is the raspberrypi user name 
* in `socketio.service` the path to socketio_server.py 

These files need to be copied to the folder `/etc/systemd/system`

Then the following commands will start and enable the services for next boot:
`sudo systemctl daemon-reload`
`sudo systemctl start flask.service`
`sudo systemctl enable flask.service`
`sudo systemctl start socketio.service`
`sudo systemctl enable socketio.service`

to check for the logs for any service: 
`journalctl -u flask.service -e` or `journalctl -u socketio.service -e`