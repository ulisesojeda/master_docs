FROM apache/airflow:2.7.1

ENV AIRFLOW__CORE__EXECUTOR=CeleryExecutor
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
ENV AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL=30
ENV AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://airflow:airflow@postgres/airflow
ENV AIRFLOW__CELERY__BROKER_URL=redis://:@redis:6379/0
ENV AIRFLOW__CORE__FERNET_KEY=''
ENV AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION='true'
ENV AIRFLOW__CORE__LOAD_EXAMPLES='true'
ENV AIRFLOW__API__AUTH_BACKENDS='airflow.api.auth.backend.basic_auth,airflow.api.auth.backend.session'
ENV AIRFLOW__SCHEDULER__ENABLE_HEALTH_CHECK='true'
ENV AIRFLOW__WEBSERVER__SECRET_KEY='alpha'
