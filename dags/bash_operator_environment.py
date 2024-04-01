import datetime
from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator


@dag(dag_id="dag_bash_operator_environment", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    environment_task = BashOperator(
        task_id='environment_task',
        bash_command='echo $PATH $MYENV',
        env={"MYENV": "VALOR_DE_VARIABLE"},
    )

generate_dag()
