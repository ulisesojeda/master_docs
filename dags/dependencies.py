
import datetime
from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator
from airflow.models.baseoperator import chain


@dag(dag_id="dag_dependencies", start_date=datetime.datetime(2024, 4, 4), schedule="@daily", catchup=False)
def generate_dag():
    task_cat = BashOperator(
        task_id='cat',
        bash_command='cat /etc/passwd',
    )
    
    task_uname = BashOperator(
        task_id='uname',
        bash_command='uname',
    )
    
    task_echo = BashOperator(
        task_id='echo',
        bash_command='echo $ENV',
    )

    task_ls = BashOperator(
        task_id='ls',
        bash_command='ls',
    )

    task_cat >> task_uname >> task_echo >> task_ls

    #chain(task_cat, task_uname, task_echo, task_ls)

generate_dag()
