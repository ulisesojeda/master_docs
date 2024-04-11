from datetime import datetime, timedelta
import time

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    'dag_reglas_ejecucion_ejercicio',
    schedule=None,
    start_date=datetime(2024, 1, 1),
) as dag:
    @task(task_id="enviar_eventos_tipo_1")
    def check_event_1():
        time.sleep(5)
        return True

    @task(task_id="enviar_eventos_tipo_2")
    def check_event_2():
        time.sleep(10)
        return True

    @task(task_id="enviar_eventos_tipo_3")
    def check_event_3():
        time.sleep(2)
        raise Exception()
        return True

    @task(task_id="evento_recibido", trigger_rule="one_success")
    def event_received():
        print("EVENTO RECIBIDO")

    task_event_received = event_received()

    check_event_1() >> task_event_received
    check_event_2() >> task_event_received
    check_event_3() >> task_event_received


