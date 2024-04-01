import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_modern", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="python_task_decorator")
    def python_callable():
        print("Ejecutando PythonOperator")

    python_callable()


generate_dag()
