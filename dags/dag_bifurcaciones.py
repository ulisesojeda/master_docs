from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    'dag_bifurcaciones',
    schedule=None,
    start_date=datetime(2024, 4, 1),
) as dag:
    @task.branch(task_id="branch_task")
    def branch_func(ti=None):
        xcom_value = ti.xcom_pull(task_ids="start_task")
        if xcom_value >= 5:
            return "continue_task"
        elif xcom_value >= 3:
            return "stop_task"
        else:
            return None


    @task(task_id="start_task")
    def start_op():
        # Hacer algun procesamiento
        return 5

    branch_op = branch_func()

    continue_op = EmptyOperator(task_id="continue_task", dag=dag)
    stop_op = EmptyOperator(task_id="stop_task", dag=dag)

    start_op() >> branch_op >> [continue_op, stop_op]


