#
# CLIENT
#
FROM python:latest
RUN pip install pyzmq

COPY client_request.py ./client.py
CMD ["python","-u","./client.py"] 
