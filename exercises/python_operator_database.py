import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_database", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="database")
    def python_callable():
        import psycopg2
        conn = psycopg2.connect(
            dbname='airflow',
            user='airflow',
            password='airflow',
            host='postgres',
            port='5432'
        )

        cursor = conn.cursor()
        # Obtener todas las entradas en la tabla dag_run
        cursor.execute("...")
        result = cursor.fetchall()

        conn.close()
        print(result)

    python_callable()


generate_dag()
