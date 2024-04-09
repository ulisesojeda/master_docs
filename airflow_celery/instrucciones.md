1. Construir image de Airflow
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
    docker run --net host airflow_celery airflow db init
   ```

6. Crear usuario de administracion
  ```bash
    docker run --net host airflow_celery  airflow users create  -e admin@admin.com -f admin -l admin -r Admin -u admin -p admin
   ```
7. Ejecutar en una terminal nueva el scheduler
  ```bash
    docker run --net host -v ./dags:/opt/airflow/dags airflow_celery airflow scheduler
   ```

8. Ejecutar en una terminal nueva el webserver
  ```bash
    docker run --net host -v ./dags:/opt/airflow/dags airflow_celery airflow webserver
   ```

9. Ejecutar en una terminal nueva un worker
  ```bash
    docker run --net host -v ./dags:/opt/airflow/dags airflow_celery celery worker -H worker1
   ```

10. Ejecutar en una terminal nueva otro worker
  ```bash
    docker run --net host -v ./dags:/opt/airflow/dags airflow_celery celery worker -H worker2
   ```

11. Ejecutar en una nueva terminal el servicio de flower (monitorizacion)
  ```bash
    docker run --net host airflow_celery celery flower 
   ```

12. Verificar ambos workers en: http://localhost:5555/

13. Abrir UI: http://localhost:8080/ con las credenciasles admin/admin
