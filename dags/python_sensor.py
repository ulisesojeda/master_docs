from airflow import DAG
from airflow.sensors.python import PythonSensor
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta


dag = DAG(
    'dag_python_sensor_example',
    start_date=datetime(2024, 4, 1),
    description='Ejemplo de PythonSensor',
    schedule_interval=timedelta(days=1),  # Daily
)

def check_condition():
    import time
    time.sleep(2)  # Simular operaciones de comprobación
    return True

python_sensor_task = PythonSensor(
    task_id='python_sensor_task',
    python_callable=check_condition,
    mode='reschedule',
    timeout=600,
    poke_interval=30,
    dag=dag,
)

downstream_task = EmptyOperator(task_id='downstream_task', dag=dag)

python_sensor_task >> downstream_task
