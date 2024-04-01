import pendulum
from airflow import DAG
from airflow.operators.latest_only import LatestOnlyOperator
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="dag_latest_only_exercise",
    schedule="@daily",
    start_date=pendulum.datetime(2024, 4, 1),
    catchup=True,
) as dag:
    latest_only = LatestOnlyOperator(task_id="latest_only")

    descargar_ficheros = EmptyOperator(task_id="descargar_ficheros")
    comprobar_usuarios_file = EmptyOperator(task_id="comprobar_existencia_usuarios_file")
    procesar_usuarios_file = EmptyOperator(task_id="procesar_fichero_usuarios")
    backup_usuarios = EmptyOperator(task_id="crear_backup_usuarios_file")

    # Requerimientos:
    # 1. La task "descargar_ficheros" se ejecutará en cada ejecución
    # 2. La comprobación del fichero de usuarios (Task comprobar_usuarios_file) se ejecutará sólo en la ejecución más reciente de la DAG
    # 3. Si el fichero existe, procesar el fichero de usuarios (procesar_usuarios_file)
    # 4. Una vez procesado, realizar un backup (backup_usuarios)

    # Defina las dependencias entre las tasks basado en los requerimientos anteriores
    # ... >> ... >>> ...
