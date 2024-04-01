from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file = Dataset('/tmp/my_file.txt')

with DAG(
    dag_id='consumer_v1',
    schedule=[my_file],
    start_date=datetime(2024, 4, 1),
    catchup=True,
):
    @task
    def read_dataset():
        with open(my_file.uri, 'r') as f:
            print(f.read())

    read_dataset()
