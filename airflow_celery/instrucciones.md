# Con Docker

1. Crear docker network
   ```bash
   docker network create mynet
   ```
   
2. Construir image de Airflow
  ```bash
    docker build -t airflow_celery .
   ```

3. Ejecutar contenedores con Postgres y Redis
  ```bash
    docker compose up
   ```

4. Crear carpeta de dags
  ```bash
    mkdir dags
   ```

5. Iniciar la BD de Airflow
  ```bash
    docker run --net mynet airflow_celery airflow db init
   ```

6. Crear usuario de administracion
  ```bash
    docker run --net mynet airflow_celery  airflow users create  -e admin@admin.com -f admin -l admin -r Admin -u admin -p admin
   ```
7. Ejecutar en una terminal nueva el scheduler
  ```bash
    docker run --net mynet -v ./dags:/opt/airflow/dags airflow_celery airflow scheduler
   ```

8. Ejecutar en una terminal nueva el webserver
  ```bash
    docker run -p 8080:8080 --net mynet -v ./dags:/opt/airflow/dags airflow_celery airflow webserver
   ```

9. Ejecutar en una terminal nueva un worker
  ```bash
    docker run --net mynet -v ./dags:/opt/airflow/dags airflow_celery celery worker -H worker1
   ```

10. Ejecutar en una terminal nueva otro worker
  ```bash
    docker run --net mynet -v ./dags:/opt/airflow/dags airflow_celery celery worker -H worker2
   ```

11. Ejecutar en una nueva terminal el servicio de flower (monitorizacion)
  ```bash
    docker run -p 5555:5555 --net mynet airflow_celery celery flower 
   ```

12. Verificar ambos workers en: http://localhost:5555/

13. Abrir UI: http://localhost:8080/ con las credenciales admin/admin


# Con Python
## Requisitos: Python 3.9

1. Crear carpeta airflow_celery y acceder a ella
2. Instalar, crear y activar virtualenv
   ```bash
   pip install virtualenv
   python -m virtualenv env
   ./env/bin/activate
   ```
3. Instalar Airflow con pip
   ```bash
   pip install "apache-airflow[celery,virtualenv]==2.7.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.9.txt"
   pip install Redis
   pip install psycopg2
   ```
4. Definir las siguientes variables de entorno
   ```bash
   export AIRFLOW__CORE__EXECUTOR=CeleryExecutor
   export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@localhost/airflow
   export AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL=30
   export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@localhost/airflow
   export AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://airflow:airflow@localhost/airflow
   export AIRFLOW__CELERY__BROKER_URL=redis://:@localhost:6379/0
   export AIRFLOW__CORE__FERNET_KEY=''
   export AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION='true'
   export AIRFLOW__CORE__LOAD_EXAMPLES='true'
   export AIRFLOW__API__AUTH_BACKENDS='airflow.api.auth.backend.basic_auth,airflow.api.auth.backend.session'
   export AIRFLOW__SCHEDULER__ENABLE_HEALTH_CHECK='true'
   export AIRFLOW__WEBSERVER__SECRET_KEY='alpha'
   ```
5. Ejecutar Postgres y Redis
   ```bash
   docker compose up
   ```
6. Abrir una nueva terminal e ir a la carpeta airflow_celery
   ```bash
   ./env/bin/activate
   # Definir las variables de entorno anteriores
   airflow db init # Inicializar DB
   airflow users create  -e admin@admin.com -f admin -l admin -r Admin -u admin -p admin  # Crear admin user
   airflow scheduler
7. Abrir una nueva terminal e ir a la carpeta airflow_celery
   ```bash
   ./env/bin/activate
   # Definir las variables de entorno anteriores
   airflow webserver
8. Abrir una nueva terminal e ir a la carpeta airflow_celery
   ```bash
   ./env/bin/activate
   # Definir las variables de entorno anteriores
   airflow celery worker -H worker1
9. Abrir una nueva terminal e ir a la carpeta airflow_celery
   ```bash
   ./env/bin/activate
   # Definir las variables de entorno anteriores
   airflow celery worker -H worker2
10. Abrir una nueva terminal e ir a la carpeta airflow_celery
   ```bash
   ./env/bin/activate
   # Definir las variables de entorno anteriores
   airflow celery flower
11. Verificar ambos workers en: http://localhost:5555/
12. Abrir UI: http://localhost:8080/ con las credenciales admin/admin
   
