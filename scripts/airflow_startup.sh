#!/bin/bash

echo "Changing permissions for dbt folder..."
cd ~/rhythmflow/ && sudo chmod -R 777 dbt # Changed path

echo "Building airflow docker images..."
cd ~/rhythmflow/airflow # Changed path
docker-compose build

echo "Running airflow-init..."
docker-compose up airflow-init

echo "Starting up airflow in detached mode..."
docker-compose up -d

echo "Airflow started successfully."
echo "Airflow is running in detached mode. "
echo "Run 'docker-compose logs --follow' to see the logs."