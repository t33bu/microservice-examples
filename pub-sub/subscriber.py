import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind("tcp://*:5555")

topic = "temperature"
socket.setsockopt_string(zmq.SUBSCRIBE, topic)

print(f"Subscribing to topic: {topic}")

while True:
    message = socket.recv_string()
    print(f"Received: {message}")
