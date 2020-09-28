This repository has simple server/client apps that can be ran on a raspberry pi to control a neo led strip. 
The socketio server controls the led strip and receives commands from the django client server that hosts a web page with some options to turn the light on/off or choose a color. 

**<span style="background-color:yellow">More commands and featuers to be added soon</span>**

# Setup: 
The socketio server and the socketio client in the flask app talk over the same port which should be configuered in `settings.yaml`

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