from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.operators.bash_operator import BashOperator


@dag(dag_id="dag_templates", start_date=datetime(2024, 4, 1), schedule="@daily", catchup=False)
def generate_dag():
    print_date_task = BashOperator(
        task_id='template',
        bash_command='echo DATA_INTERVAL_START: $DATA_INTERVAL_START',
        env={"DATA_INTERVAL_START": "{{ ds }}"},
    )

    @task(task_id="python_task")
    def python_task(val):
        tomorrow = datetime.fromisoformat(val) + timedelta(days=1)
        print(f"Mañana será: {tomorrow}")

    print_date_task >> python_task("{{ ds }}")

generate_dag()
