# INCORRECTO
import pendulum
import time

from airflow import DAG
from airflow.decorators import task

import numpy as np  # <-- NO HACER
import pandas as pd

def long_task():
    for i in range(100000000):
        i = i ** i

long_task()  # Para simular un tiempo de carga mayor

with DAG(
    dag_id="load_error",
    schedule=None,
    start_date=pendulum.datetime(2024, 4, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    @task()
    def print_array():
        """Print Numpy array."""
        a = np.arange(15).reshape(3, 5)
        print(a)
        return a

    print_array()

