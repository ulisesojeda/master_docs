from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta


dag_a = DAG(
    'DAG_BACKFILL',
    start_date=datetime(2024, 3, 1),
    description='DAG A Example',
    schedule_interval="@daily",
    catchup=False,
)

task_a1 = DummyOperator(task_id='task_a1', dag=dag_a)
task_a2 = DummyOperator(task_id='task_a2', dag=dag_a)

task_a1 >> task_a2
