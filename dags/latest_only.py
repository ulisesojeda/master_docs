import pendulum
from airflow import DAG
from airflow.operators.latest_only import LatestOnlyOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dag_latest_only",
    schedule="@daily",
    start_date=pendulum.datetime(2024, 4, 1),
    catchup=True,
) as dag:
    latest_only = LatestOnlyOperator(task_id="latest_only")
    task1 = EmptyOperator(task_id="obtener_datos_base_datos")
    task2 = EmptyOperator(task_id="guardar_s3")
    task3 = EmptyOperator(task_id="enviar_notificacion_email")

    task1 >> task2 >> latest_only >> task3
