### Docker Documentation
To build docker image
```
docker build -t frontend-server-dev:latest .
```

To run the docker container
```
docker run --name frontend-server -p 127.0.0.1:4000:4000 frontend-server-dev:latest
```

To connect to the container via interactive terminal
```
docker exec -it frontend-server sh
```
NOTE:
Above it's sh and not bash because alpine does not have bash
