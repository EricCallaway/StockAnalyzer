### Docker Documentation
To build docker image
```
docker build -t server-dev:latest .
```

To run the docker container
```
docker run --name server -p 127.0.0.1:4000:4000 server-dev:latest
```

To connect to the container via interactive terminal
```
docker exec -it server sh
```
NOTE:
Above it's sh and not bash because alpine does not have bash
