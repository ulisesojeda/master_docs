import json

import pendulum
import requests

from airflow.decorators import dag, task
@dag(
    schedule=None,
    start_date=pendulum.datetime(2024, 4, 1, tz="UTC"),
    catchup=False,
    dag_id="xcom_ejercicio",
)
def dag_xcom_ejercicio():
    @task()
    def call_api():
        import requests
        response = requests.get("https://randomuser.me/api")
        json_res = response.json()
        return json_res

    @task()
    def store(response: dict):
        with open("/tmp/response.json", "w") as f:
            f.write(str(response))

        print(response)

    response = call_api()
    store(response)

dag_xcom_ejercicio()
