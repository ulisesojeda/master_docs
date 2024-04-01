from datetime import datetime
from airflow.decorators import dag, task

configs = {
    "YCombinator": {"url": "https://news.ycombinator.com/"},
    "Science": {"url": "https://www.science.org/"},
    "IEEE": {"url": "https://www.ieee.org/"},
}

for site, config in configs.items():
    dag_id = f"dag_dinamica_{site}"

    @dag(dag_id=dag_id, start_date=datetime(2024, 4, 1), catchup=False)
    def download_url_dags():
        @task
        def download_url(url):
            # Descargar e imprimir el contenido de la url
            ...

        # Pasar el parametro de configuración que contiene la URL
        download_url(...)

    download_url_dags()
