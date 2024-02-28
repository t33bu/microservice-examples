# 
# SERVER
#
FROM python:latest
RUN pip install pyzmq

COPY server_response.py ./server.py
CMD ["python","-u","./server.py"] 
