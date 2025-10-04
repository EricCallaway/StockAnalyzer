- Creating a virtual environment with uv

```
uv venv
```

- Activate the virtual environement with 
```
source .venv/bin/activate
```

```
uv pip install -r requirements.txt
```

### Docker

To build the docker image
```
docker build -t backend-dev:latest .
```

To run the docker container
```
docker run --name fastapi -p 127.0.0.1:8000:8000 dev:latest
```

To connect to the container via interactive terminal
```
docker exec -it fastapi bash
```