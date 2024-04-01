# Bash
Bash es un intérprete de comandos y un lenguaje de scripting utilizado principalmente en sistemas operativos basados en Unix y Linux.

```bash
# Ejecutar bash en un contenedor
docker run -it ubuntu bash

# Listar ficheros
ls

# Ejecutar comandos
echo HOLA
find / -name "*.conf"
hostname

# Leer ficheros
cat /etc/passwd

# Crear fichero
echo "Nombre: Juan, Departamento: IT" > juan.txt

# Copiar fichero
cp juan.txt /tmp/juan_copia.txt

# Eliminar ficheros y carpetas
rm -rf /tmp/juan_copia.txt

# Buscar contenido en archivos de texto
grep -i 'departamento' juan.txt

# Esperar un tiempo determinado
sleep 5  #(5 segundos)
```
