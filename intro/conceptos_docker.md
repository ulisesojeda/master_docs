# Docker
Docker es una plataforma para facilitar la creación y ejecución de aplicaciones en contenedores. Los contenedores permiten empaquetar una aplicación con todas sus partes, como bibliotecas y otras dependencias, y distribuirlo todo como un único paquete. Esto asegura que la aplicación se ejecute de manera consistente en diferentes sistemas operativos.

## Descargar imagen
```bash
docker pull nginx:latest
```

### Ejecutar un contenedor
```bash
docker run --name myserver -d -p 8888:80 nginx:latest
# Comprobar servicio en http://localhost:8888
# Comprobar que se está ejecutando el contenedor
docker ps
```

### Acceder al contenedor mediante terminal de usuario
```bash
docker exec -it myserver bash
```

### Eliminar un contenedor
``` bash
docker rm -f myserver
# Comprobar que el contenedor no está en ejecución
docker ps
```
