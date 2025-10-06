# Airflow Service

This Airflow service is configured to use PostgreSQL as the metadata database and Redis as the Celery broker for distributed task execution.

## Configuration

The service is pre-configured with the following environment variables:

- **Database**: PostgreSQL (byte_sanctuary_db:5432)
- **Broker**: Redis (redis:6379)
- **Executor**: CeleryExecutor
- **Port**: 8080

## Docker Setup

### Build the Docker Image
```bash
docker build -t airflow-dev:latest .
```

### Run with Docker Compose (Recommended)
The service is designed to work with the main docker-compose.yml file:

```bash
# Start all services including PostgreSQL and Redis
docker-compose up -d

# Or start just the Airflow services
docker-compose up airflow-webserver airflow-scheduler airflow-worker
```

### Individual Container Commands

To run specific Airflow components:

```bash
# Run webserver
docker run --name airflow-webserver -p 8080:8080 --network src_default airflow-dev:latest webserver

# Run scheduler
docker run --name airflow-scheduler --network src_default airflow-dev:latest scheduler

# Run worker
docker run --name airflow-worker --network src_default airflow-dev:latest worker

# Run API server
docker run --name airflow-api -p 8080:8080 --network src_default airflow-dev:latest api-server
```

### Access Airflow

- **Web UI**: http://localhost:8080
- **Username**: admin
- **Password**: admin

## Environment Variables

The following environment variables are set in the Dockerfile:

- `AIRFLOW__DATABASE__SQL_ALCHEMY_CONN`: PostgreSQL connection string
- `AIRFLOW__CELERY__RESULT_BACKEND`: Celery result backend (PostgreSQL)
- `AIRFLOW__CELERY__BROKER_URL`: Redis broker URL
- `AIRFLOW__CORE__EXECUTOR`: CeleryExecutor

## Database Initialization

The startup script automatically:
1. Waits for PostgreSQL and Redis to be ready
2. Initializes the Airflow database (`airflow db init`)
3. Creates an admin user
4. Starts the specified Airflow service

## Development

To connect to the container for development:
```bash
docker exec -it <container_name> bash
```