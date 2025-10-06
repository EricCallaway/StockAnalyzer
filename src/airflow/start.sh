#!/bin/bash

# Exit on any error
set -e

# Function to wait for PostgreSQL to be ready
wait_for_postgres() {
    echo "Waiting for PostgreSQL to be ready..."
    while ! nc -z byte_sanctuary 5432; do
        echo "PostgreSQL is unavailable - sleeping"
        sleep 1
    done
    echo "PostgreSQL is up - executing command"
}

# Function to wait for Redis to be ready
wait_for_redis() {
    echo "Waiting for Redis to be ready..."
    while ! nc -z redis 6379; do
        echo "Redis is unavailable - sleeping"
        sleep 1
    done
    echo "Redis is up - executing command"
}

# Wait for dependencies
wait_for_postgres
wait_for_redis

# Initialize Airflow database
echo "Initializing Airflow database..."
airflow db migrate

# Create admin user (only if it doesn't exist)
echo "Creating admin user..."
airflow users add-user \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin || echo "Admin user already exists"

# Start the appropriate service based on command
if [ "$1" = "webserver" ]; then
    echo "Starting Airflow webserver..."
    exec airflow webserver -p 8080
elif [ "$1" = "scheduler" ]; then
    echo "Starting Airflow scheduler..."
    exec airflow scheduler
elif [ "$1" = "worker" ]; then
    echo "Starting Celery worker..."
    exec airflow celery worker
elif [ "$1" = "api-server" ]; then
    echo "Starting Airflow API server..."
    exec airflow api-server -p 8080
else
    # Default to webserver if no command specified
    echo "No command specified, starting Airflow webserver..."
    exec airflow webserver -p 8080
fi
