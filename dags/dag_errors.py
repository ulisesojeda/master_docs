# Error. Falta la importar la libreria datetime

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator


@dag(dag_id="dag_errors", start_date=datetime.datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    EmptyOperator(task_id="task")


generate_dag()


