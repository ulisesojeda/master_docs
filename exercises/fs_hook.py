import os
import random
import shutil
import string

from airflow.plugins_manager import AirflowPlugin
from airflow.hooks.base import BaseHook


class FsHook(BaseHook):

    def __init__(self, conn_id='fs_default', *args, **kwargs):
        super().__init__(*args, **kwargs)

    def list(self, directory):
        return os.listdir(directory)

    def copy_file(self, source, destination):
        # Copiar el el fichero source hacia destination
        ...

    def delete_file(self, path):
        # Eliminar el fichero path
        ....

    def create_file(self, path, length):
        # Generar una string aleatoria de length caracteres
        random_string = ....
        # Crear un fichero con el contenido de random_string
        ...

    def print_file(self, path):
        # Mostrar en pantalla el contenido del fichero de texto path
        ...


class AirflowFSPlugin(AirflowPlugin):
    name = 'file_system'
    hooks = [FsHook]


