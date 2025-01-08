"""Small example OSC client

This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""


"""
pip install python-osc
pip install Flask
pip install Flask-Cors
"""
import argparse
import random
import time
from flask_cors import CORS , cross_origin

from pythonosc import udp_client

from flask import Flask, request, jsonify


# This is setting up the OSC Connection.
client = udp_client.SimpleUDPClient("127.0.0.1", 7287)


app = Flask(__name__)
CORS(app) 


@app.route('/sayHi', methods=['POST'])
@cross_origin() 
def sayHi():
	content = request.json
	message = content['message']
	client.send_message("/sayHi", message)
	return jsonify({'message': 'Message sent to OSC client'})


@app.route('/sendData', methods=['POST'])
def sendData():
	content = request.json
	message = content['data']
	client.send_message("/sendData", message)
	return jsonify({'message': 'Data sent to OSC client'})



@app.route('/sendOSCMessage', methods=['POST'])
def sendOSCMessage():
	content = request.json
	message = content['data']
	address = content['address']
	client.send_message("/" + address, message)
	return jsonify({'message': 'OSC Message sent to client'})




if __name__ == "__main__":
    app.run(debug=True)