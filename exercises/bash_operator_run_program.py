import datetime
from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator


@dag(dag_id="dag_bash_operator_run_program", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    run_program_task = BashOperator(
        task_id='run_program',
        # Ejecutar programa que muestre TODA la información el sistema operativo (nombre del SO, kernel version, arquitectura, etc)
        bash_command='...',
    )

generate_dag()
