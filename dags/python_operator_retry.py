import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


def my_retry_callback(context):
    print("Mensaje de RETRY CALLBACK")

def my_failure_callback(context):
    print("Mensaje de FAILURE CALLBACK")

@dag(dag_id="dag_python_operator_retry", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="error_task", retries=3, on_failure_callback=my_failure_callback, on_retry_callback=my_retry_callback)
    def python_callable():
        print("Hello World")
        raise Exception("ERROR")

    python_callable()


generate_dag()
