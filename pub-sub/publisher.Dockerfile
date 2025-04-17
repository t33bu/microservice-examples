#
# PUBLISHER
#
FROM python:latest
RUN pip install pyzmq
COPY publisher.py .

CMD ["python","-u","./publisher.py"] 
