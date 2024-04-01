from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def push_function(**kwargs):
    value_to_push = "Hello, this is a message!"
    kwargs['ti'].xcom_push(key='my_key', value=value_to_push)

def pull_function(**kwargs):
    ti = kwargs['ti']
    pulled_value = ti.xcom_pull(task_ids='push_task', key='my_key')
    print(f"Received message: {pulled_value}")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'xcom_example',
    default_args=default_args,
    schedule=timedelta(days=1),
)

push_task = PythonOperator(
    task_id='push_task',
    python_callable=push_function,
    provide_context=True,
    dag=dag,
)

pull_task = PythonOperator(
    task_id='pull_task',
    python_callable=pull_function,
    provide_context=True,
    dag=dag,
)

push_task >> pull_task
