from datetime import datetime

from airflow import DAG
from airflow.decorators import task

from hooks.fs.fs_hook import FsHook

hook = FsHook()
PATH_FILE = "/tmp/foo.txt"
COPY_FILE = "/tmp/copy.txt"

with DAG('fs_hook_ejercicio', start_date=datetime(2024, 4, 1), schedule_interval='@daily', catchup=False) as dag:
    @task(task_id="create_file")
    def create_file():
        hook.create_file(PATH_FILE, 50)

    @task(task_id="copy_file")
    def copy_file():
        hook.copy_file(PATH_FILE, COPY_FILE)

    @task(task_id="print_fs_list")
    def print_fs_list():
        print(hook.list("/tmp"))

    @task(task_id="print_file")
    def print_file():
        hook.print_file(PATH_FILE)

    @task(task_id="delete_file")
    def delete_file():
        hook.delete_file(PATH_FILE)

    create_file() >> copy_file() >> print_fs_list() >> print_file() >> delete_file() >> print_fs_list()
