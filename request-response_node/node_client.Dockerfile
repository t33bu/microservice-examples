FROM node:21-alpine
WORKDIR /client_app
COPY client.js .
CMD ["node","client.js"]

