# Docker Compose Setup

This docker-compose.yml file provides a complete Stock Analyzer stack with Airflow, PostgreSQL, Redis, FastAPI backend, and frontend services.

## Services Included

### Core Services
- **byte_sanctuary_db**: PostgreSQL database (port 5433)
- **redis**: Redis cache/message broker
- **backend**: FastAPI backend service (port 8000)

### Airflow Services
- **airflow-init**: Database initialization service
- **airflow-webserver**: Airflow web UI (port 8080)
- **airflow-scheduler**: Airflow task scheduler
- **airflow-worker**: Celery worker for task execution
- **airflow-api**: Airflow REST API server (port 8081)

### Frontend Services
- **frontend-server**: Node.js server (port 3000)
- **frontend-client**: React client (port 3001)

### Data Services
- **dbt**: DBT for data transformation

## Environment Variables

Create a `.env` file in the `src` directory with:

```bash
# Database Configuration
DB_USER=airflow
DB_PASSWORD=airflow
DB_NAME=airflow
DB_PORT=5433
```

## Usage

### Start All Services
```bash
cd src
docker-compose up -d
```

### Start Specific Services
```bash
# Start only Airflow services
docker-compose up -d airflow-init airflow-webserver airflow-scheduler airflow-worker

# Start only database and backend
docker-compose up -d byte_sanctuary_db redis backend

# Start with API server instead of webserver
docker-compose up -d airflow-init airflow-api airflow-scheduler airflow-worker
```

### Access Services
- **Airflow Web UI**: http://localhost:8080 (admin/admin)
- **Airflow API**: http://localhost:8081 (admin/admin)
- **Backend API**: http://localhost:8000
- **Frontend Server**: http://localhost:3000
- **Frontend Client**: http://localhost:3001
- **PostgreSQL**: localhost:5433

### Useful Commands

```bash
# View logs
docker-compose logs -f airflow-webserver

# Restart a service
docker-compose restart airflow-webserver

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Rebuild and start
docker-compose up --build -d
```

### Troubleshooting

1. **Database connection issues**: Ensure PostgreSQL is healthy before starting Airflow services
2. **Redis connection issues**: Check that Redis container is running
3. **Port conflicts**: Modify port mappings in docker-compose.yml
4. **Permission issues**: Ensure proper user permissions (UID 50000 for Airflow)

### Service Dependencies

```
byte_sanctuary_db + redis → airflow-init → {webserver, scheduler, worker, api}
byte_sanctuary_db → backend
backend → {frontend-server, frontend-client}
byte_sanctuary_db → dbt
```

### Standalone Mode

For development/testing without full stack:

```bash
# Build standalone image
docker build -f airflow/Dockerfile.standalone -t airflow-standalone:latest airflow/

# Run standalone (no dependencies)
docker run --name airflow-standalone -p 8080:8080 airflow-standalone:latest api-server
```
