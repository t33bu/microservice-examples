import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.connect("tcp://subscriber:5555") 

topic = "temperature"
print(f"Publish to topic: {topic}")

while True:
    message = random.randint(20, 25)
    socket.send_string(f"{topic} {message}")    
    print(f"Sent: {topic} {message}")
    time.sleep(3)

