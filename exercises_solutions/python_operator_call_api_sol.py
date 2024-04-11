import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_call_url", start_date=datetime.datetime(2024, 1, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="call_url")
    def python_callable():
        import requests
        response = requests.get('https://news.ycombinator.com/')
        data = response.text
        print(f"Data recibida: {data}")

    python_callable()


generate_dag()
