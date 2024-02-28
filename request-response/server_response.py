import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5005")
print("Server listening..")

while True:
    msg_in = socket.recv_string()
    print("Server received: ", msg_in)
    print("Server Wait for 3s")
    time.sleep(3)
    reply = "OK"
    socket.send_string(reply)
    print("Server send: ", reply)
	
