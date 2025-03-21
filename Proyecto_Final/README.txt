Para la generación de Facturas Simples, se crea la aplicación "myapp" usando Django:

 . Se implementa con CRUD, lo cual permite realizar (Create, Read, Update, Delete) de los productos.
 . Se define el modelo Producto en models.py con los campos; nombre, descripción y precio. 
 . Se define el modelo Cliente en models.py con los campos; nombre, apellido y correo. 
 . Se define el modelo Factura en models.py con los campos; nombre, producto, cantidad y subtotal. 
 . Se crean vistas basadas en clases (Class-Based Views); ListView, DetailView, CreateView, UpdateView y DeleteView. 
 . Se crean formularios con ModelForm.
 . Se implementan formularios para crear facturas, seleccionando clientes y productos.
 . Se crean plantillas para renderizar la información de la factura en formato HTML.
 . Se crean usuarios y perfiles de usuarios, con login, para "Create, Update y Delete". Por defecto en la Página Principal se puede consultar e imprimir la listas de "Productos, Clientes y Facturas".


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
                     |                         |- cliente_confirm_delete.html
                     |                         |- cliente_detail.html
                     |                         |- cliente_form.html
                     |                         |- cliente_list.html
                     |                         |- producto_confirm_delete.html
                     |                         |- producto_detail.html
                     |                         |- producto_form.html
                     |                         |- producto_list.html
                     |                         |- factura_confirm_delete.html
                     |                         |- factura_detail.html
                     |                         |- factura_form.html
                     |                         |- factura_list.html
                     |- forms.py
                     |- models.py
                     |- urls.py
                     |- views.py
                     |
                     |- project__
                                 |- __pycache__
                                 |- settings.py
                                 |- urls.py


### 1.  Diagrama de flujo de la aplicación, desde la "Página Principal Papelería":
                                                                |
                                                            index.html 
                                                                |
                  ---------------------------------------------------------------------------------------------
                  |                               |                             |                             |
    -----------------------------    -----------------------------   ------------------------------     -----------------
    -Lista de Facturas Papelería-    -Lista de Clientes Papelería-   -Lista de Productos Papelería-     -Login Papelería-
    -----------------------------    -----------------------------   ------------------------------     -----------------
               |                                 |                              |                             |
        factura_list.html                 cliente_list.html             producto_list.html                  /admin
               |                                 |                              |                             |
               |                                 |                              |       -----------------------------------------
               |                                 |                              |       |     |       |       |         |       |
               |                                 |                              |   /group /user /cliente /factura /producto index.html
               |                                 |                              |
               |                                 |           ----------------------------------------------------
               |                                 |           |                  |                               |
               |                                 |   ------------------   -------------------- -----------------------------------------
               |                                 |   -Detalle producto-   -Imprimir Productos- -Volver al incio | a la página de inicio-
               |                                 |   ------------------   -------------------- -----------------------------------------
               |                                 |           |
               |                                 |   producto_detail.html
               |                                 |           |   
               |                                 |   -------------------
               |                                 |   -Volver a la lista-
               |                                 |   -------------------
               |                                 |
               |           -------------------------------------------------
               |           |                     |                         |
               |   -----------------   ------------------- ----------------------------------------
               |   -Detalle cliente-   -Imprimir Clientes- -Volver al incio | a la página de inicio-
               |   -----------------   ------------------- ----------------------------------------
               |           |
               |  cliente_detail.html
               |           |   
               |   -------------------
               |   -Volver a la lista-
               |   -------------------
               |
               ---------------------------------------------------
               |                     |                           |
       -----------------    ------------------- -----------------------------------------
       -Detalle factura-    -Imprimir Facturas- -Volver al incio | a la página de inicio-
       -----------------    ------------------- -----------------------------------------
               |
       factura_detail.html
               |   
               -------------------------------
               |                             |
       ------------------ -----------------------------------------
       -Imprimir Factura- -Volver a la Lista de Facturas Papelería-
       ------------------ -----------------------------------------


### 2. Modelo en `models.py`:

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Factura(models.Model):
    nombre = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f'Factura: {self.id} - Cliente: {self.nombre} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad} - Subtotal: {self.cantidad * self.producto.precio}€'

### 3. Formulario con ModelForm, en myapp/forms.py:

from django import forms
from .models import Producto, Cliente, Factura

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['nombre', 'producto', 'cantidad']


### 4. Vistas basadas en clases (Class-Based Views), en myapp/views.py:

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Cliente, Factura
from .forms import ProductoForm, ClienteForm, FacturaForm
from django.shortcuts import render, redirect, get_object_or_404

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

# Vistas para Factura
class FacturaListView(ListView):
    model = Factura
    template_name = 'factura_list.html'

class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'factura_detail.html'

class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura_form.html'
    success_url = reverse_lazy('factura_list')

class FacturaUpdateView(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura_form.html'
    success_url = reverse_lazy('factura_list')

class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = 'factura_confirm_delete.html'
    success_url = reverse_lazy('factura_list')

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
    ClienteUpdateView, ClienteDeleteView,
    FacturaListView, FacturaDetailView, FacturaCreateView, 
    FacturaUpdateView, FacturaDeleteView
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

    # URLs para Facturas
    path('facturas/', FacturaListView.as_view(), name='factura_list'),
    path('facturas/<int:pk>/', FacturaDetailView.as_view(), name='factura_detail'),
    path('facturas/nuevo/', FacturaCreateView.as_view(), name='factura_create'),
    path('facturas/<int:pk>/editar/', FacturaUpdateView.as_view(), name='factura_update'),
    path('facturas/<int:pk>/eliminar/', FacturaDeleteView.as_view(), name='factura_delete'),
]


### 6. HTMLs, en `myapp/templates`:

#### `index.html`

#### `cliente_list.html`

#### `cliente_detail.html`

#### `cliente_form.html`

#### `cliente_confirm_delete.html`

#### `factura_list.html`

#### `factura_detail.html`

#### `factura_form.html`

#### `factura_confirm_delete.html`

#### `producto_list.html`

#### `producto_detail.html`

#### `producto_form.html`

#### `producto_confirm_delete.html`


### 7. URLs del proyecto, en project/urls.py:

from django.contrib import admin
from django.urls import path, include
from myapp.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('myapp.urls')),
    path('', index, name='index'),  # Configurar la URL principal
]


### 8. Se registran los modelos en el admin (myapp/admin.py):

from django.contrib import admin
from .models import Cliente, Producto, Factura

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Factura)


### 9. Se crea un superusuario para poder acceder al panel de administración:

python manage.py createsuperuser


### 10. Se Migran los cambios a la base de datos:

python manage.py makemigrations
python manage.py migrate


### 11. Se ejecuta en la ruta del proyecto del servidor desde el directorio "Gestion_Productos"

python manage.py runserver

### 12. Acceder con la URL:

http://127.0.0.1:8000/

### 13. Usuario Administrador:

User: Admin-1
Password: Administrador-1

### 14. Resultados de la aplicación.

 En la carpeta "Muestras_Aplicación", están algunos pantallazos de las diferentes URLs, y una impresión de la "Lista de Productos", "Lista de Clientes", "Lista de Facturas" y "Detalle de la Factura", en PDF.
 También se añade pantallazo "GitHub" de los últimos commits.
