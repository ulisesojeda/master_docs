import os

from airflow.plugins_manager import AirflowPlugin
from airflow.hooks.base import BaseHook


class FsHook(BaseHook):

    def __init__(self, conn_id='fs_default', *args, **kwargs):
        super().__init__(*args, **kwargs)

    def list(self, directory):
        return os.listdir(directory)

class AirflowFSPlugin(AirflowPlugin):
    name = 'file_system'
    hooks = [FsHook]


