#https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pushpull.html
import zmq

#  socket to join queue
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://server:5557")

while True:       
    # pull event
    event = socket.recv_json()
    print('Client pulling event',event['eventId'],':',event['type'],'=',event['value'])
    
        