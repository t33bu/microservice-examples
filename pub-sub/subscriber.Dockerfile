#
# SUBSCRIBER
#
FROM python:latest
RUN pip install pyzmq
COPY subscriber.py .

CMD ["python","-u","./subscriber.py"] 
