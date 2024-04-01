## Decoradores en Python
Permiten modificar o extender el funcionamiento de una función. Añaden funcionalidad extra a una función de manera sencilla.

```python
def mi_decorator(func):
    def wrapper():
        print("Esto se ejecutan antes de llamar a la función.")
        func()
        print("Esto se ejecuta después de que la función se ha ejecutado.")
    return wrapper

@mi_decorator
def hello():
    print("Hola!")

# Llamar a la función con decorador
hello()
```
### Ejemplo de decoradores en Airflow
```python
from airflow.decorators import task
...
    @task()
    def extract_data():
        return "Extracted data"

    @task()
    def transform_data(raw_data: str):
        return f"Transformed data: {raw_data}"
...
```


## Librería requests
Utilizada para realizar llamadas HTTP/HTTPS

### Instalación
```bash
# Descargar fichero https://bootstrap.pypa.io/get-pip.py
python get-pip.py
python -m pip install requests
```

### Llamada con método GET
```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### Paso de parámetros
```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### Llamada con método POST
```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post(url, json=data)

if response.status_code == 201:
    created_post = response.json()
    print(created_post)
else:
    print(f"Error: {response.status_code}")
```

### Envío de cabeceras HTTP
```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

## Librería json
Para codificar y decodificar datos en formato JSON

### Convertir Python diccionario a JSON
```python
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data, indent=2)  # indentación para mejor visualización
print(json_data)
type(json_data)
```

### Convertir JSON a diccionario
```python
import json

json_data = '{"name": "Alice", "age": 25, "city": "London"}'
decoded_data = json.loads(json_data)
print(decoded_data)
type(decoded_data)
```

### Guardar JSON en un fichero
```python
import json

data = {
    "name": "Bob",
    "age": 35,
    "city": "Paris"
}

with open('output.json', 'w') as file:
    json.dump(data, file, indent=2)
```

### Leer fichero JSON
```python
import json

# Windows: with open('C:\\Users\\TU_USUARIO\\Downloads\\output.json', 'r') as file:
with open('output.json', 'r') as file:
    json_data = json.load(file)

print(json_data)
```

## Librería pandas
Permite procesar y analizar datos. Funcionalidades similares a una base de datos relacional (MySQL, Postgres, etc) mediante código Python.

### Instalación
```bash
python -m pip install pandas
```

### Crear dataframe (tabla)
```python
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)
print(df)
```
### Leer y escribir ficheros
```bash
# Generar fichero csv
cat <<EOF > example.csv
Name,Age,City
Alice,25,New York
Bob,30,London
Charlie,35,Paris
EOF
```

```python
df = pd.read_csv('example.csv')
print(df)

df.to_csv('output2.csv', index=False)
```

### Acceso y manipulación de datos
```python
# Acceso a columna Name
nombres = df['Name']

# Filtrado de filas basado en condición
mayores_de_18 = df[df['Age'] > 18]

# Añadir columna
df['Salary'] = [50000, 60000, 70000]
df 

# Ordenar por columna
df_ordenado = df.sort_values(by='Age')
```

### Manejadores de contexto
Permiten reservar y liberar recursos cuando es necesario de manera implícita
```python
with open("file.txt", "r") as f:
    print(f.read())
# Cuando se sale del scope del manejador, el fichero se cierra automáticamente
# La variable 'f' que representa al fichero sólo es accesible dentro de este contexto
```
Los manejadores son objectos que tienen al menos las funciones "__enter__" y "__exit__" que se ejecutan al inicio y final respectivamente del contexto

El ejemplo anterior funciona pues la clase File se define parcialmente de esta forma:

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
```

