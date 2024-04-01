from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta


dag = DAG(
    'http_sensor_example',
    start_date=datetime(2024, 4, 1),
    description='Ejemplo de Http Sensor',
    schedule_interval=timedelta(days=1),  # Daily
)

http_sensor_task = HttpSensor(
    task_id='http_sensor_task',
	http_conn_id='user_api',
	endpoint='api/',
    dag=dag,
)

downstream_task = EmptyOperator(task_id='downstream_task', dag=dag)

http_sensor_task >> downstream_task
