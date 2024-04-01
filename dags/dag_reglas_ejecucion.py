from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    'dag_reglas_ejecucion',
    schedule=None,
    start_date=datetime(2024, 4, 1),
) as dag:
    @task(task_id="comprobar_tabla_1")
    def check_table_1():
        # Para activar task alert
        #raise Exception()
        return True

    @task(task_id="comprobar_tabla_2")
    def check_table_2():
        return True

    @task(task_id="comprobar_tabla_3")
    def check_table_3():
        return True

    @task(task_id="enviar_email")
    def send_email():
        print("Email enviado")

    @task(task_id="generar_alerta", trigger_rule="one_failed")
    def alert():
        print("Alerta generada")

    task_send_email = send_email()
    task_alert = alert()

    check_table_1() >> [task_send_email, task_alert]
    check_table_2() >> [task_send_email, task_alert]
    check_table_3() >> [task_send_email, task_alert]


