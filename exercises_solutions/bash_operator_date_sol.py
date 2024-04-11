import datetime
from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator


@dag(dag_id="dag_bash_operator_date", start_date=datetime.datetime(2024, 1, 1), schedule="@daily", catchup=False)
def generate_dag():
    print_date_task = BashOperator(
        task_id='print_date_task',
        bash_command='date',
    )

generate_dag()
