from airflow import DAG
from airflow.sensors.time_sensor import TimeSensor
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta, timezone


dag = DAG(
    'dag_time_sensor_example',
    start_date=datetime(2024, 4, 1),
    description='Ejemplo de Time Sensor',
    schedule_interval=timedelta(days=1),  # Daily
)

time_sensor_task = TimeSensor(
    task_id='time_sensor_task',
    mode="poke",
    target_time=(datetime.now() + timedelta(seconds=5)).time(),
    soft_fail=True,
    dag=dag,
)

downstream_task = EmptyOperator(task_id='downstream_task', dag=dag)

time_sensor_task >> downstream_task
