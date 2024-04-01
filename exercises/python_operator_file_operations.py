import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_file_operation", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="file_operations")
    def python_callable():
        with open('/etc/passwd', 'r') as file:
            # Leer todo el contenido del fichero
            data = ...
            # Convertir a mayusculas todo el fichero
            processed_data = ...

        with open('output.txt', 'w') as file:
            # Guardar el contenido en mayusculas (processed_data) en el fichero output.txt
            ...

        with open('output.txt', 'r') as file:
            # Leer el contenido de output.txt
            ....
            # Mostrar el contenido en pantalla
            ...

        print("Procesado completado")

    python_callable()


generate_dag()
