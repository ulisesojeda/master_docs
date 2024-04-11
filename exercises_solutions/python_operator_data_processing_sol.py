import datetime
from airflow.decorators import dag
from airflow.operators.python import task
from airflow.operators.python import PythonOperator


@dag(dag_id="dag_python_operator_data_processing", start_date=datetime.datetime(2024, 1, 1), schedule="@daily", catchup=False)
def generate_dag():
    @task(task_id="data_processing")
    def python_callable():
        import pandas as pd
        df = pd.DataFrame({"name": ["John", "Alex"], "nota": [4, 5]})
        media_nota = df['nota'].mean()
        print(f"Media: {media_nota}")

    python_callable()


generate_dag()
