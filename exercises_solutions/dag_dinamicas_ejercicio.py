from datetime import datetime
from airflow.decorators import dag, task

configs = {
    "YCombinator": {"url": "https://news.ycombinator.com/"},
    "Science": {"url": "https://www.science.org/"},
    "IEEE": {"url": "https://www.ieee.org/"},
}

for site, config in configs.items():
    dag_id = f"dag_dinamica_{site}"

    @dag(dag_id=dag_id, start_date=datetime(2024, 1, 31), catchup=False)
    def download_url_dags():
        @task
        def download_url(url):
            import requests
            req = requests.get(url)
            print(req.text)

        download_url(config["url"])

    download_url_dags()
