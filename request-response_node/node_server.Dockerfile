FROM node:21-alpine
WORKDIR /server_app
COPY server.js .
CMD ["node","server.js"]

