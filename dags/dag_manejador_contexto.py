import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dag_manejador_contexto",
    start_date=datetime.datetime(2024, 4, 1),
    schedule="@daily",
    catchup=False,
):
    EmptyOperator(task_id="task")
