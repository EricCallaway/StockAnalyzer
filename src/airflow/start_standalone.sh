#!/bin/bash

# Exit on any error
set -e

# Initialize Airflow database (SQLite)
echo "Initializing Airflow database (SQLite)..."
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
elif [ "$1" = "api-server" ]; then
    echo "Starting Airflow API server..."
    exec airflow api-server -p 8080
else
    # Default to webserver if no command specified
    echo "No command specified, starting Airflow webserver..."
    exec airflow webserver -p 8080
fi