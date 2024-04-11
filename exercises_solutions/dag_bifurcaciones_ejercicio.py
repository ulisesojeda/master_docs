from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    'dag_bifurcaciones_ejercicio',
    schedule=None,
    start_date=datetime(2024, 1, 1),
) as dag:
    @task.branch(task_id="branch_task")
    def branch_func(response: dict):
        if response["status"]:
            return "continue_task"
        else:
            return "stop_task"

    @task(task_id="start_task")
    def start_op():
        # Hacer algun procesamiento
        import os
        if os.path.exists("/etc/passwd"):
            return {"status": True}
        else:
            return {"status": False}

    valor = start_op()
    branch_op = branch_func(valor)

    continue_op = EmptyOperator(task_id="continue_task", dag=dag)
    stop_op = EmptyOperator(task_id="stop_task", dag=dag)

    # No hay necesidad de definir la dependencia con start_op, está implicita al utilizar branch_op el valor devuelto por start_op
    branch_op >> [continue_op, stop_op]


