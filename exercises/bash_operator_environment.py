import datetime
from airflow.decorators import dag
from airflow.operators.bash_operator import BashOperator


@dag(dag_id="dag_bash_operator_environment", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    environment_task = BashOperator(
        task_id='environment_task',
        # Mostrar en pantalla el contenido de las variables de entorno PATH y MYENV
        # Pista: posibles comandos: printf, echo
        bash_command='...',
        env={"MYENV": "VALOR_DE_VARIABLE"},
    )

generate_dag()
