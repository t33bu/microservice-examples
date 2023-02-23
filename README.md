# Microservices and Containers (KM00DT91)

This repository contains example containers using different technology stacks and communication patterns for microservices.

The examples require Docker Desktop in running in the background.

## Automatic start-up

Examples can be started using the provided yaml-file. Command syntax is: ```docker-compose -f <filename> up```. For example: 
```
docker-compose -f .\pushpull_example.yaml up
```

This will (first build and) start the configured containers. Then, typing <kbd>Ctrl-C</kbd> several times stops the example running. 

## Manual start-up

Individual containers can also be started using command line with additional steps:
1. Create private internal network (MyNet) to connect the containers. Command syntax: ```docker network create <network name>```. For example:
```
docker network create MyNet
```

2. Build the all images for containers using the corresponding Dockerfiles, where file and image names depend on the example. Command syntax: ```docker build -f <Dockerfile> -t <image name> <location>```. For example:

```
docker build -f .\server.Dockerfile -t push_server .
docker build -f .\client.Dockerfile -t pull_client .
``` 

3. Next, run the containers and connect them to the private network. Command syntax: ```docker run --network <network name> --hostname <network hostname> <image name>```. For example:

```
docker run --network MyNet --hostname server push_server
docker run --network MyNet --hostname client pull_client
``` 
You can then use the network hostname (here *server* or *client*) in your python program, as Docker will automatically find the network address of that container. So, no need to use IP address or localhost. 

4. To stop the containers use the command ```docker stop <image name>``` for all containers. For example:
```
docker stop push_server
docker stop pull_client
```


