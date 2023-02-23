#
# CLIENT
#
FROM python:latest
RUN pip install pyzmq

COPY client_pull.py ./client.py
CMD ["python","-u","./client.py"] 

