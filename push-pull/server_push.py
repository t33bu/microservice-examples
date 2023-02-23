#https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pushpull.html

import zmq
import time
import random

#  socket to join queue
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind('tcp://*:5557')

# Event
sensor_data = {
    'type': 'humidity',
    'sensorId': 123,
    'value': 0,
    'unit': '%',
    'eventId': 0
}

while True:
    # new sensor data
    time.sleep(3)
    sensor_data['value'] = random.randint(40,80)    
    
    # push event
    print('Server pushing event', sensor_data['eventId'],':',
        sensor_data['type'],'=',sensor_data['value'])
    socket.send_json(sensor_data)
    
    # upate event id
    sensor_data['eventId'] = sensor_data['eventId'] + 1 	
    

	