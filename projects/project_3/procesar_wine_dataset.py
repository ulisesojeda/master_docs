import logging

from datetime import datetime
from airflow import DAG, Dataset
from airflow.decorators import task
from airflow.operators.python import is_venv_installed

log = logging.getLogger(__name__)

RAW_WINE_DATASET = Dataset("file://localhost/airflow/datasets/raw_wine_dataset.csv")

with DAG(
    dag_id="wine_dataset_consumer",
    schedule=[RAW_WINE_DATASET],
    start_date=datetime(2024, 4, 1),
    tags=["example"],
) as dag:

    if not is_venv_installed():
        raise RuntimeError("virtualenv is not installed!")
    else:
        @task.virtualenv(
            task_id="virtualenv_python", requirements=["pandas==2.0.3"],
            system_site_packages=False
        )
        def clean_dataset():
            import pandas as pd
            df = pd.read_csv("~/raw_wine_dataset.csv", index_col=0)
            df = df.replace({"\r": ""}, regex=True)
            df = df.replace({"\n": " "}, regex=True)
            df.drop(['grape'], axis=1, inplace=True)
            df.to_csv("~/cleaned_dataset.csv")

        @task.virtualenv(
            task_id="sqlite_persist_wine_data", requirements=["pandas==2.0.3", "sqlalchemy==2.0.21"],
            system_site_packages=False
        )
        def persist_dataset():
            import pandas as pd
            from sqlalchemy import create_engine
            engine = create_engine('sqlite:////tmp/wine_dataset.db', echo=True)
            df = pd.read_csv("~/cleaned_dataset.csv", index_col=0)
            df.to_sql('wine_dataset', engine)
            df.notes.to_sql("wine_notes", engine)

        @task(task_id="query_db")
        def query_db():
            import sqlite3
            conn = sqlite3.connect('/tmp/wine_dataset.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM wine_dataset;')
            results = cursor.fetchall()
            for row in results:
                print(row)
            cursor.close()
            conn.close()

        clean_dataset() >> persist_dataset() >> query_db()
