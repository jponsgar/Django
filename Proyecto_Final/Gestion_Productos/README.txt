Para la gestión de Productos de Papelería, se crea una página web usando Django:

 . Se implementa con CRUD, lo cual permite realizar (Create, Read, Update, Delete) de los productos.
 . Se define el modelo Producto en models.py con los campos; nombre, descripción y precio. 
 . Se define el modelo Cliente en models.py con los campos; nombre, apellido y correo. 
 . Se crean vistas basadas en clases (Class-Based Views); ListView, DetailView, CreateView, UpdateView y DeleteView. 
 . Se crean formularios con ModelForm.


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
                     |                         |- cliente_confirm_delete.html
                     |                         |- cliente_detail.html
                     |                         |- cliente_form.html
                     |                         |- cliente_list.html
                     |- forms.py
                     |- models.py
                     |- urls.py
                     |- views.py
                     |
                     |- project__
                                 |- __pycache__
                                 |- settings.py
                                 |- urls.py


### 1. Organigrama aplicación:

                                   index.html 
                                       |
                                       |
             -------------------------------------------------------
             |                                                     |
-----------------------------                         -----------------------------
-Lista de Clientes Papelería-                         -Lista de Producto Papelería-
-----------------------------                         -----------------------------
             |                                                     |
      cliente_list.html                                    producto_list.html
             |                                                     |
             |                            -------------------------------------------------------------
             |                            |                   |                   |                   |
             |                  producto_detail.html   producto_form.html         |                   |
             |                            |                   |                   |                   |
             |                   ------------------  ----------------  -------------------- ------------------------------
             |                   -Detalle producto-  -Crear producto-  -Imprimir productos- -Volver a la página de inicio-
             |                   ------------------  ----------------  -------------------- ------------------------------
             |                            |                   |
             |                            |                   |
             |                            |                   ---------------------
             |                            |                   |                   |
             |                            |                   |                   |
             |                            |                -------        -------------------   
             |                            |                -Crear-        -Volver a la lista-
             |                            |                -------        -------------------
             |                            |
             |                            -------------------------------------------------------------
             |                            |                                       |                   |
             |                    producto_form.html                   producto_confirm_delete        |
             |                            |                                       |                   |
             |                      ----------------                    -------------------  -------------------
             |                     -Editar producto-                    -Eliminar producto-  -Volver a la lista-
             |                      ----------------                    -------------------  -------------------
             |                            |                                       |
             |                            ---------------------                   --------------------- 
             |                            |                   |                   |                   |
             |                       ------------    -------------------    --------------        ----------
             |                       -Actualizar-    -Volver a la lista-    -Si, Eliminar-        -Cancelar-
             |                       ------------    -------------------    --------------        ---------- 
             |
             |_____________________________________________________
                                                                   |
                                         -------------------------------------------------------------
                                         |                   |                   |                   |
                                 cliente_detail.html   cliente_form.html         |                   |
                                         |                   |                   |                   |
                                -----------------  ---------------  -------------------  -----------------------------
                                -Detalle cliente-  -Crear cliente-  -Imprimir clientes-  -Volver a la página de inicio-
                                -----------------  ---------------  -------------------  -----------------------------
                                         |                   |
                                         |                   |
                                         |                   ---------------------
                                         |                   |                   |
                                         |                   |                   |
                                         |                -------        -------------------   
                                         |                -Crear-        -Volver a la lista-
                                         |                -------        -------------------
                                         |
                                         -------------------------------------------------------------
                                         |                                       |                   |
                                  cliente_form.html                    cliente_confirm_delete        |
                                         |                                       |                   |
                                   ---------------                    ------------------  -------------------
                                  -Editar cliente-                    -Eliminar cliente-  -Volver a la lista-
                                   ---------------                    ------------------  -------------------
                                         |                                       |
                                         ---------------------                   --------------------- 
                                         |                   |                   |                   |
                                    ------------    -------------------    --------------        ----------
                                    -Actualizar-    -Volver a la lista-    -Si, Eliminar-        -Cancelar-
                                    ------------    -------------------    --------------        ---------- 


### 2. Modelo en `models.py`:

from django.db import models

class Producto(models.Model):
    producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.producto

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

### 3. Formulario con ModelForm, en myapp/forms.py:

from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['producto', 'descripcion', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo']

### 4. Vistas basadas en clases (Class-Based Views), en myapp/views.py:

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# Vistas para Producto
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

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')


### 5. Rutas en `urls.py`, en myapp/urls.py:

from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    ClienteListView, ClienteDetailView, ClienteCreateView, 
    ClienteUpdateView, ClienteDeleteView
)

urlpatterns = [
    # URLs para Producto
    path('', ProductoListView.as_view(), name='producto_list'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('<int:pk>/borrar/', ProductoDeleteView.as_view(), name='producto_delete'),

    # URLs para Cliente
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),
]

### 6. HTMLs, en `myapp/templates`:

#### `index.html`

#### `producto_list.html`

#### `producto_detail.html`

#### `producto_form.html`

#### `producto_confirm_delete.html`

#### `cliente_list.html`

#### `cliente_detail.html`

#### `cliente_form.html`

#### `cliente_confirm_delete.html`


### 7. URLs del proyecto, en project/urls.py:

from django.contrib import admin
from django.urls import path, include
from myapp.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('myapp.urls')),
    path('', index, name='index'),  
]

### 8. Se Migran los cambios a la base de datos:

python manage.py makemigrations
python manage.py migrate

### 9. Se ejecuta en la ruta del proyecto del servidor desde el directorio "Gestion_Productos"

python manage.py runserver

### 10. Acceder con la URL:

http://127.0.0.1:8000/

### 11. Resultados de la aplicación.

 En la carpeta "Muestras_Aplicación", están los pantallazos de las diferentes URLs, y una impresión de la "Lista de Productos" y "Lista de Clientes", en PDF.
 También se añade pantallazo "GitHub" de los últimos commits.
