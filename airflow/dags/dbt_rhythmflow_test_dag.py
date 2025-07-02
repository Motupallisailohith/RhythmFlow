from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'airflow'
}

with DAG(
    dag_id = 'dbt_rhythmflow_test', # Changed from dbt_test to dbt_rhythmflow_test
    default_args = default_args,
    description = 'Test dbt for RhythmFlow', # Changed description
    schedule_interval="@once", #At the 5th minute of every hour
    start_date=datetime(2022,3,20),
    catchup=True,
    tags=['rhythmflow', 'dbt'] # Changed tag
) as dag:

    dbt_test_task = BashOperator(
        task_id = "dbt_test",
        bash_command = "cd /dbt && dbt deps && dbt compile --profiles-dir ."
    )

    dbt_test_task