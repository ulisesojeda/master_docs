import pendulum
from airflow.decorators import task
from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
import json
import pandas as pd
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


with DAG('proyecto_1', schedule='@daily', start_date=pendulum.datetime(2024, 4, 1), catchup=False) as dag:
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='''
        CREATE TABLE IF NOT EXISTS users(
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            country TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL PRIMARY KEY
        );
        '''
    )

    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='user_api',
        endpoint='api/'
    )

    extract_user = SimpleHttpOperator(
        task_id='extract_user',
        http_conn_id='user_api',
        endpoint='api/',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    @task
    def process_user(**kwargs):
        ti = kwargs["ti"]
        user = ti.xcom_pull(task_ids='extract_user')
        user = user['results'][0]
        processed_user = pd.json_normalize({
            'firstname': user['name']['first'],
            'lastname': user['name']['last'],
            'country': user['location']['country'],
            'username': user['login']['username'],
            'password': user['login']['password'],
            'email': user['email']
        })
        processed_user.to_csv('/tmp/processed_user.csv', index=None, header=False)

    @task
    def store_user():
        hook = PostgresHook(postgres_conn_id='postgres')
        hook.copy_expert(
            sql="COPY users FROM stdin WITH DELIMITER as ','",
            filename='/tmp/processed_user.csv'
        )

    @task
    def print_file():
        with open("/tmp/processed_user.csv", "r") as f:
            print(f.read())

    create_table >> is_api_available >> extract_user >> process_user() >> store_user() >> print_file()
