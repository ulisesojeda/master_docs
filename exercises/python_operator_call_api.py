import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_call_url", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="call_url")
    def python_callable():
        import requests
        # Obtener el contenido de la página web "https://news.ycombinator.com/" en modo texto y mostrarlo en pantalla
        # Pista: Utilizar función "get" de la librería "requests"
        response = .......  # Hacer llamada GET al sitio web
        data = ....  # Obtener la respuesta en modo texto
        print(f"Data recibida: {data}")

    python_callable()


generate_dag()
