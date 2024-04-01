import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dag_sin_task_group",
    schedule="@daily",
    start_date=pendulum.datetime(2024, 4, 1),
    catchup=True,
) as dag:
    task1 = EmptyOperator(task_id="task1")
    task2 = EmptyOperator(task_id="task2")
    task3 = EmptyOperator(task_id="task3")

    task1 >> task2 >> task3
