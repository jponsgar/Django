"""
Implementar un CRUD (Create, Read, Update, Delete) básico para un modelo, por ejemplo, un modelo Snake. Definir el modelo Snake en models.py con campos como nombre, descripción y puntos. Usar vistas basadas en clases (Class-Based Views) como ListView, DetailView, CreateView, UpdateView y DeleteView.  Crear formularios con ModelForm. Configurar las rutas y plantillas necesarias.
"""

### 1. Definir el modelo `Snake` en `models.py`:

from django.db import models

class Snake(models.Model):
    nombre = models.CharField(max_length=100)
    puntos = models.IntegerField()

    def __str__(self):
        return self.nombre

### 2. Crear el formulario con ModelForm, en myapp/forms.py:

from django import forms
from .models import Snake

class SnakeForm(forms.ModelForm):
    class Meta:
        model = Snake
        fields = ['nombre', 'puntos']

### 3. Configurar las vistas basadas en clases (Class-Based Views), en myapp/views.py:

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snake
from .forms import SnakeForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class SnakeListView(ListView):
    model = Snake
    template_name = 'snake_list.html'

class SnakeDetailView(DetailView):
    model = Snake
    template_name = 'snake_detail.html'

class SnakeCreateView(CreateView):
    model = Snake
    form_class = SnakeForm
    template_name = 'snake_form.html'
    success_url = reverse_lazy('snake_list')

class SnakeUpdateView(UpdateView):
    model = Snake
    form_class = SnakeForm
    template_name = 'snake_form.html'
    success_url = reverse_lazy('snake_list')

class SnakeDeleteView(DeleteView):
    model = Snake
    template_name = 'snake_confirm_delete.html'
    success_url = reverse_lazy('snake_list')


### 4. Configurar las rutas en `urls.py`, en myapp/urls.py:

from django.urls import path
from .views import (
    SnakeListView,
    SnakeDetailView,
    SnakeCreateView,
    SnakeUpdateView,
    SnakeDeleteView
)

urlpatterns = [
    path('', SnakeListView.as_view(), name='snake_list'),
    path('<int:pk>/', SnakeDetailView.as_view(), name='snake_detail'),
    path('nuevo/', SnakeCreateView.as_view(), name='snake_create'),
    path('<int:pk>/editar/', SnakeUpdateView.as_view(), name='snake_update'),
    path('<int:pk>/borrar/', SnakeDeleteView.as_view(), name='snake_delete'),
]

### 5. Crear htmls, en `myapp/templates`:

#### `index.html`

```html
<!-- myapp/templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Página Principal</title>
</head>
<body>
    <h1>Bienvenido a la Página Principal</h1>
    <a href="{% url 'snake_list' %}">Ver Snakes</a>
</body>
</html>

#### `snake_list.html`

<!DOCTYPE html>
<html>
<head>
    <title>Lista de Snakes</title>
</head>
<body>
    <h1>Lista de Snakes</h1>
    <a href="{% url 'snake_create' %}">Crear Snake</a>
    <ul>
        {% for snake in object_list %}
            <li>
                <a href="{% url 'snake_detail' snake.pk %}">{{ snake.nombre }}</a> - {{ snake.puntos }}
                <a href="{% url 'snake_update' snake.pk %}">Editar</a>
                <a href="{% url 'snake_delete' snake.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
    <br>
    <a href="{% url 'index' %}">Volver a la página de inicio</a>
</body>
</html>

#### `snake_detail.html`

<!DOCTYPE html>
<html>
<head>
    <title>Detalle del Snake</title>
</head>
<body>
    <h1>{{ object.nombre }}</h1>
    <p>{{ object.puntos }}</p>
    <a href="{% url 'snake_update' object.pk %}">Editar</a>
    <a href="{% url 'snake_delete' object.pk %}">Eliminar</a>
    <a href="{% url 'snake_list' %}">Volver a la lista</a>
</body>
</html>

#### `snake_form.html`

<!DOCTYPE html>
<html>
<head>
    <title>{% if object %}Editar{% else %}Crear{% endif %} Snake</title>
</head>
<body>
    <h1>{% if object %}Editar{% else %}Crear{% endif %} Snake</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">{% if object %}Actualizar{% else %}Crear{% endif %}</button>
    </form>
    <a href="{% url 'snake_list' %}">Volver a la lista</a>
</body>
</html>


#### `snake_confirm_delete.html`

<!-- myapp/templates/snake_confirm_delete.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Eliminar Snake</title>
</head>
<body>
    <h1>Eliminar Snake</h1>
    <p>¿Estás seguro de que deseas eliminar el snake "{{ object.nombre }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Sí, eliminar</button>
    </form>
    <a href="{% url 'snake_list' %}">Cancelar</a>
</body>
</html>

### 6. Configurar las URLs del proyecto, en project/urls.py:

from django.contrib import admin
from django.urls import path, include
from myapp.views import index  # Importar la vista index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snakes/', include('myapp.urls')),
    path('', index, name='index'),  # Configurar la URL principal
]

### 7. Migrar los cambios a la base de datos:

python manage.py makemigrations
python manage.py migrate

### 8. Ejecutar el servidor

python manage.py runserver

### 9. Prueba:

Acceder a la ruta:

http://127.0.0.1:8000/