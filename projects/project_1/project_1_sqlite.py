import pendulum
from airflow.decorators import task
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
import json
import pandas as pd
import sqlite3


with DAG('proyecto_1_sqlite', schedule='@daily', start_date=pendulum.datetime(2024, 4, 5), catchup=False) as dag:
    @task
    def create_table():
        conn = sqlite3.connect('/tmp/base.db')
        cursor = conn.cursor()
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
        cursor.execute(sql)
        cursor.close()

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
        processed_user.to_csv('/tmp/processed_user.csv', index=None, header=True)

    @task
    def store_user():
        with sqlite3.connect('/tmp/base.db') as cnx:
            df = pd.read_csv("/tmp/processed_user.csv")
            df.to_sql("users", con=cnx, if_exists='replace', index=False)

    @task
    def print_file():
        with open("/tmp/processed_user.csv", "r") as f:
            print("Content of csv file")
            print(f.read())
        with sqlite3.connect('/tmp/base.db') as cnx:
            print("Content of Sqlite users table")
            cursor = cnx.cursor()
            cursor.execute("select * from users")
            res = cursor.fetchall()
            print(res)

    create_table() >> is_api_available >> extract_user >> process_user() >> store_user() >> print_file()