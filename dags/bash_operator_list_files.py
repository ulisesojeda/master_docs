import datetime
from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator


@dag(dag_id="dag_bash_operator_list_files", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    list_files_task = BashOperator(
        task_id='list_files_task',
        bash_command='ls /etc',
    )

generate_dag()
