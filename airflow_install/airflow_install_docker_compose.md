# Instalación de Airflow
## Requisitos
- [Docker] (https://docs.docker.com/get-docker/)
- [Visual Studio Code] (https://code.visualstudio.com/download)

# Instalación
- Crear carpeta **docker_installation** en **Mis Documentos**
- Copiar fichero [docker-compose](https://github.com/ulisesojeda/master_docs/blob/master/airflow_install/docker-compose.yaml) en **docker_installation**
- Crear carpetas **dags**, **logs**, **plugins** y **config** en **docker_installation**
  ```bash
  mkdir dags
  mkdir logs
  mkdir plugins
  mkdir config

  echo -e "AIRFLOW_UID=$(id -u)" > .env  # si se ejecuta en Linux/MacOS
  ```
- Abrir carpeta **airflow_docker** con Visual Studio Code
    ```bash
  code .
  ```
- Abrir terminal en Visual Studio Code (**Terminal** -> **Nueva Terminal**)
- Ejecutar en la terminal (tardará aproximadamente unos 5 minutos)
```sh
docker compose up
```
- Abrir en el navegador http://localhost:8080/ con las credenciales: **airflow/airflow**
- Terminar Airflow
```
docker compose down
```

