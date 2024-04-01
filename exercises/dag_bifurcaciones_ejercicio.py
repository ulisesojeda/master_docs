from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    'dag_bifurcaciones_ejercicio',
    schedule=None,
    start_date=datetime(2024, 4, 1),
) as dag:
    @task.branch(task_id="branch_task")
    def branch_func(response: dict):
        # Si la response tiene la key "status" a True, continuar con "continue_task", si no "stop_task"
        if ...
            return "continue_task"
        else:
            return "stop_task"

    @task(task_id="start_task")
    def start_op():
        import os
        # Si el fichero "/etc/passwd" existe devolver status a True
        if ...
            return {"status": True}
        else:
            return {"status": False}

    valor = start_op()
    branch_op = branch_func(valor)

    continue_op = EmptyOperator(task_id="continue_task", dag=dag)
    stop_op = EmptyOperator(task_id="stop_task", dag=dag)

    branch_op >> [continue_op, stop_op]


