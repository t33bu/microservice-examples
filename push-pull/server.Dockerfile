# 
# SERVER
#
FROM python:latest
RUN pip install pyzmq

COPY server_push.py ./server.py
CMD ["python","-u","./server.py"] 

