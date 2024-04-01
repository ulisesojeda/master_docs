from datetime import datetime

from airflow import DAG
from airflow.decorators import task

from hooks.fs.fs_hook import FsHook


with DAG('fs_dag', start_date=datetime(2024, 4, 1), schedule_interval='@daily', catchup=False) as dag:
	@task(task_id="print_fs_list")
	def print_fs_list():
		hook = FsHook()
		print(hook.list("/"))
	print_fs_list()
