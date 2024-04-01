import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_multiplication", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="multiplication")
    def python_callable(a, b):
        # Calcular la multiplicacion de los parámetros a y b en la variable res
        ...
        print(f"Result: {res}")

    python_callable(10, 30)


generate_dag()
