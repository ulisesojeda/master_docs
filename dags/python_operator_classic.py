import datetime
from airflow.decorators import dag
from airflow.operators.python import PythonOperator


def python_callable():
    print("Ejecutando PythonOperator")


@dag(dag_id="dag_python_operator_classic", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    task_1 = PythonOperator(task_id="task_1", python_callable=python_callable)


generate_dag()
