import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_hello_world", start_date=datetime.datetime(2024, 1, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="task_hello_world")
    def python_callable():
        print("Hello World")

    python_callable()


generate_dag()
