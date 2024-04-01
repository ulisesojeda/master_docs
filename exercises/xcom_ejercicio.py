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
        # Importar librearia para llamadas HTTP
        import ...
        # Llamada GET a url https://randomuser.me/api 
        response = ...
        # Obtener la respuesta de la llamada en formato json
        json_res = ...
        # Guardar la respuesta como un XCom
        return ...

    @task()
    def store(response: dict):
        with open("/tmp/response.json", "w") as f:
            f.write(str(response))

        print(response)

    # Obtener el valor de XCom devuelto por la task call_api
    ...
    # Llamar a la task "store" con el valor anteriormente obtenido
    store(response)

dag_xcom_ejercicio()
