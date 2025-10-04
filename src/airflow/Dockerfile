# Airflow service Dockerfile
FROM apache/airflow:2.8.1

# Copy requirements and install dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Copy project files
COPY . /opt/airflow/

# Set working directory
WORKDIR /opt/airflow
