from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime, timedelta


dag_b = DAG(
    'DAG_B',
    start_date=datetime(2024, 4, 1),
    description='DAG B Example',
    schedule_interval="@daily",
    catchup=True,
)

task_b1 = DummyOperator(task_id='task_b1', dag=dag_b)

wait_for_task_a2 = ExternalTaskSensor(
    task_id='wait_for_task_a2',
    external_dag_id='DAG_A',
    external_task_id='task_a2',
    execution_delta=timedelta(days=0),
    dag=dag_b,
)

task_b2 = DummyOperator(task_id='task_b2', dag=dag_b)

task_b1 >> wait_for_task_a2 >> task_b2
