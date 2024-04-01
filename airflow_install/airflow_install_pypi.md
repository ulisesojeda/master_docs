# Instalación de Airflow mediante PyPi (pip)

## Requisitos

- [Docker] (https://docs.docker.com/get-docker/)

# Instalación

1. Ejecutar los siguientes comandos

```bash
mkdir airflow
cd airflow
docker run -it -p 8080:8080 -v .:/root/airflow ubuntu:22.04 bash

apt update
apt install -y software-properties-common
add-apt-repository ppa:deadsnakes/ppa -y
apt update
DEBIAN_FRONTEND=noninteractive apt install -y python3.9 python3-pip # DEBIAN_FRONTEND to avoid timezone questions during Python installation
export PYTHON_VERSION=3.9
export AIRFLOW_VERSION=2.7.1
pip install "apache-airflow[celery,virtualenv]==${AIRFLOW_VERSION}" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
airflow standalone
```

2. Obtener las credenciales de la salida del último comando ejecutado (admin/random string)
3. Abrir el navegador en [http://localhost:8080](http://localhost:8080)
