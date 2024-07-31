## Pistas

### HTML
1. **Crear una página HTML simple**
   - **Ejemplo**:
     ```html
     <!DOCTYPE html>
     <html>
     <head>
       <title>Mi Página</title>
     </head>
     <body>
       <h1>Bienvenidos a mi página</h1>
       <p>Este es un párrafo de ejemplo.</p>
     </body>
     </html>
     ```
   - **Caso de uso**: Crear la página principal de un sitio web personal.

2. **Añadir una lista ordenada y una lista desordenada**
   - **Ejemplo**:
     ```html
     <h2>Lista Ordenada</h2>
     <ol>
       <li>Elemento 1</li>
       <li>Elemento 2</li>
       <li>Elemento 3</li>
     </ol>
     <h2>Lista Desordenada</h2>
     <ul>
       <li>Elemento A</li>
       <li>Elemento B</li>
       <li>Elemento C</li>
     </ul>
     ```
   - **Caso de uso**: Listar los pasos de un tutorial y los ingredientes de una receta.

3. **Incorporar una imagen**
   - **Ejemplo**:
     ```html
     <img src="https://via.placeholder.com/150" alt="Imagen de ejemplo">
     ```
   - **Caso de uso**: Añadir una imagen de perfil en una página de biografía.

### CSS
4. **Aplicar estilos básicos**
   - **Ejemplo**:
     ```html
     <style>
       body {
         background-color: lightblue;
         color: darkblue;
       }
     </style>
     ```
   - **Caso de uso**: Personalizar los colores de una página web para que coincidan con la identidad de la marca.

5. **Crear una barra de navegación**
   - **Ejemplo**:
     ```html
     <style>
       .nav {
         display: flex;
         justify-content: space-around;
         background-color: #333;
         padding: 1em;
       }
       .nav a {
         color: white;
         text-decoration: none;
       }
     </style>
     <div class="nav">
       <a href="#home">Inicio</a>
       <a href="#about">Acerca de</a>
       <a href="#contact">Contacto</a>
     </div>
     ```
   - **Caso de uso**: Crear una barra de navegación para un sitio web corporativo.

6. **Estilizar un formulario**
   - **Ejemplo**:
     ```html
     <style>
       form {
         background-color: #f2f2f2;
         padding: 20px;
         border-radius: 5px;
       }
       input[type="text"], input[type="email"] {
         width: 100%;
         padding: 10px;
         margin: 5px 0;
       }
     </style>
     <form>
       <label for="name">Nombre:</label>
       <input type="text" id="name" name="name">
       <label for="email">Correo:</label>
       <input type="email" id="email" name="email">
       <input type="submit" value="Enviar">
     </form>
     ```
   - **Caso de uso**: Diseñar un formulario de contacto para una página web.

### JavaScript
7. **Manipulación básica del DOM**
   - **Ejemplo**:
     ```html
     <p id="demo">Este es un párrafo.</p>
     <button onclick="document.getElementById('demo').innerHTML = 'Texto cambiado!'">Cambiar texto</button>
     ```
   - **Caso de uso**: Cambiar el contenido de un elemento en respuesta a una acción del usuario, como un clic.

8. **Validar un formulario**
   - **Ejemplo**:
     ```html
     <form onsubmit="return validateForm()">
       <label for="name">Nombre:</label>
       <input type="text" id="name" name="name">
       <input type="submit" value="Enviar">
     </form>
     <script>
       function validateForm() {
         var name = document.getElementById('name').value;
         if (name == "") {
           alert("El nombre debe ser completado");
           return false;
         }
         return true;
       }
     </script>
     ```
   - **Caso de uso**: Validar que un campo obligatorio no esté vacío antes de enviar el formulario.

9. **Crear un contador**
   - **Ejemplo**:
     ```html
     <p>Contador: <span id="counter">0</span></p>
     <button onclick="incrementCounter()">Incrementar</button>
     <script>
       var count = 0;
       function incrementCounter() {
         count++;
         document.getElementById('counter').innerText = count;
       }
     </script>
     ```
   - **Caso de uso**: Implementar una función de "Me gusta" en una página de redes sociales.

### Python
10. **Crear una clase y un objeto**
    - **Ejemplo**:
      ```python
      class Persona:
          def __init__(self, nombre, edad):
              self.nombre = nombre
              self.edad = edad

          def saludar(self):
              return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

      persona1 = Persona("Juan", 30)
      print(persona1.saludar())
      ```
    - **Caso de uso**: Modelar datos de usuarios en una aplicación.

11. **Manipular un diccionario**
    - **Ejemplo**:
      ```python
      datos = {
          "nombre": "Juan",
          "edad": 30,
          "ciudad": "Madrid"
      }
      for clave, valor in datos.items():
          print(f"{clave}: {valor}")
      ```
    - **Caso de uso**: Extraer y mostrar información del perfil de un usuario almacenado en un diccionario.

12. **Ordenar una lista**
    - **Ejemplo**:
      ```python
      lista = [5, 3, 8, 1, 2]
      lista_ordenada = sorted(lista)
      print(lista_ordenada)
      ```
    - **Caso de uso**: Ordenar calificaciones de exámenes para determinar el rendimiento de los estudiantes.

### Django
13. **Crear un proyecto Django**
    - **Ejemplo**:
      ```bash
      django-admin startproject mi_proyecto
      cd mi_proyecto
      python manage.py runserver
      ```
    - **Caso de uso**: Inicializar un nuevo proyecto web con Django.

14. **Crear una aplicación en Django**
    - **Ejemplo**:
      ```bash
      python manage.py startapp mi_aplicacion
      ```
    - **Caso de uso**: Añadir una nueva funcionalidad modular a tu proyecto Django.

15. **Configurar una ruta y vista**
    - **Ejemplo**:
      ```python
      # en mi_aplicacion/views.py
      from django.http import HttpResponse

      def hola(request):
          return HttpResponse("Hello, Django!")

      # en mi_proyecto/urls.py
      from django.urls import path
      from mi_aplicacion import views

      urlpatterns = [
          path('hola/', views.hola),
      ]
      ```
    - **Caso de uso**: Configurar una vista que devuelva una respuesta simple en una aplicación Django.

### SQLite (conexión con Django)
16. **Definir un modelo**
    - **Ejemplo**:
      ```python
      # en mi_aplicacion/models.py
      from django.db import models

      class Libro(models.Model):
          titulo = models.CharField(max_length=100)
          autor = models.CharField(max_length=100)
          fecha_publicacion = models.DateField()
      ```
    - **Caso de uso**: Crear una base de datos para almacenar información de libros.

17. **Hacer una migración**
    - **Ejemplo**:
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```
    - **Caso de uso**: Aplicar cambios en la estructura de la base de datos.

18. **Crear un superusuario**
    - **Ejemplo**:
      ```bash
      python manage.py createsuperuser
      ```
    - **Caso de uso**: Acceder al panel de administración de Django para gestionar datos.

### API y JSON
19. **Realizar una solicitud GET**
    - **Ejemplo**:
      ```python
      import requests

      response = requests.get('https://api.github.com')
      print(response.json())
      ```
    - **Caso de uso**: Obtener datos públicos de la API de GitHub.

20. **Extraer datos de un JSON**
    - **Ejemplo**:
      ```python
      import requests

      response = requests.get('https://api.github.com')
      datos = response.json()
      print(f"GitHub API status: {datos['status']}")
      ```
    - **Caso de uso**: Mostrar el estado de la API de GitHub en tu aplicación.

21. **Mostrar datos en HTML**
    - **Ejemplo**:
      ```python
      # en views.py
      from django.shortcuts import render
      import requests

      def mostrar_datos(request):
          response = requests.get('https

://api.github.com')
          datos = response.json()
          return render(request, 'datos.html', {'datos': datos})

      # en datos.html
      <html>
      <body>
          <h1>GitHub API Status: {{ datos.status }}</h1>
      </body>
      </html>
      ```
    - **Caso de uso**: Mostrar datos dinámicos de una API en tu página web.

### Numpy
22. **Crear y manipular arrays**
    - **Ejemplo**:
      ```python
      import numpy as np

      array = np.array([1, 2, 3, 4, 5])
      print("Suma:", np.sum(array))
      print("Media:", np.mean(array))
      ```
    - **Caso de uso**: Realizar operaciones matemáticas en grandes conjuntos de datos.

23. **Matriz de identidad**
    - **Ejemplo**:
      ```python
      import numpy as np

      matriz_identidad = np.eye(3)
      print(matriz_identidad)
      ```
    - **Caso de uso**: Utilizar una matriz de identidad en cálculos matemáticos avanzados.

24. **Operaciones elementales**
    - **Ejemplo**:
      ```python
      import numpy as np

      a = np.array([1, 2, 3])
      b = np.array([4, 5, 6])
      suma = np.add(a, b)
      print(suma)
      ```
    - **Caso de uso**: Sumar dos vectores en un análisis científico.

### Matplotlib
25. **Crear un gráfico de líneas**
    - **Ejemplo**:
      ```python
      import matplotlib.pyplot as plt

      x = [1, 2, 3, 4, 5]
      y = [2, 3, 5, 7, 11]

      plt.plot(x, y)
      plt.xlabel('X')
      plt.ylabel('Y')
      plt.title('Gráfico de líneas')
      plt.show()
      ```
    - **Caso de uso**: Visualizar el crecimiento de una serie de datos a lo largo del tiempo.

26. **Gráfico de barras**
    - **Ejemplo**:
      ```python
      import matplotlib.pyplot as plt

      categorias = ['A', 'B', 'C']
      valores = [10, 20, 15]

      plt.bar(categorias, valores)
      plt.xlabel('Categorías')
      plt.ylabel('Valores')
      plt.title('Gráfico de barras')
      plt.show()
      ```
    - **Caso de uso**: Comparar diferentes categorías en una encuesta.

27. **Gráfico de dispersión**
    - **Ejemplo**:
      ```python
      import matplotlib.pyplot as plt

      x = [1, 2, 3, 4, 5]
      y = [2, 4, 1, 3, 5]

      plt.scatter(x, y)
      plt.xlabel('X')
      plt.ylabel('Y')
      plt.title('Gráfico de dispersión')
      plt.show()
      ```
    - **Caso de uso**: Mostrar la relación entre dos variables en un estudio científico.

### Pandas
28. **Crear un DataFrame**
    - **Ejemplo**:
      ```python
      import pandas as pd

      datos = {
          'Nombre': ['Ana', 'Luis', 'Carlos'],
          'Edad': [28, 34, 29],
          'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
      }
      df = pd.DataFrame(datos)
      print(df)
      ```
    - **Caso de uso**: Crear una tabla de datos con información de empleados.

29. **Filtrar datos en un DataFrame**
    - **Ejemplo**:
      ```python
      import pandas as pd

      datos = {
          'Nombre': ['Ana', 'Luis', 'Carlos'],
          'Edad': [28, 34, 29],
          'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
      }
      df = pd.DataFrame(datos)
      df_filtrado = df[df['Edad'] > 30]
      print(df_filtrado)
      ```
    - **Caso de uso**: Filtrar empleados mayores de 30 años en una base de datos.

30. **Describir un DataFrame**
    - **Ejemplo**:
      ```python
      import pandas as pd

      datos = {
          'Nombre': ['Ana', 'Luis', 'Carlos'],
          'Edad': [28, 34, 29],
          'Ciudad': ['Madrid', 'Barcelona', 'Valencia']
      }
      df = pd.DataFrame(datos)
      print(df.describe())
      ```
    - **Caso de uso**: Obtener estadísticas descriptivas sobre la edad de los empleados en una empresa.
