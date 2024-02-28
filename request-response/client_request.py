import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://server:5005")

id = 0
while True:
    msg_out = "msg %s" % id
    print("Client sending:", msg_out)
    socket.send_string(msg_out)
    id = id + 1
    msg_in = socket.recv_string()
    print("Client received:", msg_in)
    time.sleep(1)
		