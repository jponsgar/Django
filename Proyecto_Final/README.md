"""
Para la gestión de Productos de Papelería, se crea una página web usando Django:
Se implementa con CRUD, lo cual permite realizar (Create, Read, Update, Delete) de los productos.
Se define el modelo Producto en models.py con los campos; nombre, descripción y precio. 
Se crean vistas basadas en clases (Class-Based Views); ListView, DetailView, CreateView, UpdateView y DeleteView. 
Se crean formularios con ModelForm.
"""

### 0. Organización de directorios y principales ficheros creados o modificados:

- Gestion_Productos__
                     |
                     |- myapp____
                     |           |- __pycache__
                     |           |- migrations
                     |           |- static_____
                     |           |             |- favicon.jpg
                     |           |             |- stiles.css
                     |           |- templates__
                     |                         |- index.html
                     |                         |- producto_confirm_delete.html
                     |                         |- producto_detail.html
                     |                         |- producto_form.html
                     |                         |- producto_list.html
                     |- forms.py
                     |- models.py
                     |- urls.py
                     |- views.py
                     |
                     |- project__
                                 |- __pycache__
                                 |- settings.py
                                 |- urls.py

### 1. Modelo `Producto` en `models.py`:

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

### 2. Formulario con ModelForm, en myapp/forms.py:

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

### 3. Vistas basadas en clases (Class-Based Views), en myapp/views.py:

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')


### 4. Rutas en `urls.py`, en myapp/urls.py:

from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('<int:pk>/borrar/', ProductoDeleteView.as_view(), name='producto_delete'),
]

### 5. HTMLs, en `myapp/templates`:

#### `index.html`

#### `producto_list.html`

#### `producto_detail.html`

#### `producto_form.html`

#### `producto_confirm_delete.html`


### 6. URLs del proyecto, en project/urls.py:

from django.contrib import admin
from django.urls import path, include
from myapp.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('myapp.urls')),
    path('', index, name='index'),  
]

### 7. Se Migran los cambios a la base de datos:

python manage.py makemigrations
python manage.py migrate

### 8. Se ejecuta en la ruta del proyecto del servidor desde la carpeta "Gestion_Productos"

python manage.py runserver

### 9. Acceder con la URL:

http://127.0.0.1:8000/

### 10. Resultados de la aplicación.

 En la carpeta "Muestras_Aplicación", están los pantallazos de las diferentes URLs.

