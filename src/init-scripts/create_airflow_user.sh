#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER airflow WITH PASSWORD 'airflow';
  GRANT ALL PRIVILEGES ON DATABASE byte_sanctuary TO airflow;
EOSQL
