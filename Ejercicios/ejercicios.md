## Ejercicios

### Ejercicio 1: Páginas Protegidas por Login
Descripción: Crea un sistema de autenticación que permita a los usuarios registrarse, iniciar sesión y acceder a una página protegida.

**Pistas:**

- Utiliza el sistema de autenticación integrado de Django (django.contrib.auth).
- Crea vistas para registro (`SignupView`), inicio de sesión (`LoginView`) y cierre de sesión (`LogoutView`).
- Usa decoradores como `@login_required` para proteger las vistas.
- Configura las URLs correspondientes en `urls.py`.

### Ejercicio 2: CRUD Básico de un Modelo

Descripción: Implementa un CRUD (Create, Read, Update, Delete) básico para un modelo, por ejemplo, un modelo Producto.

**Pistas:**

- Define el modelo `Producto` en `models.py` con campos como nombre, descripción y precio.
- Usa vistas basadas en clases (Class-Based Views) como `ListView`, `DetailView`, `CreateView`, `UpdateView` y `DeleteView`.
- Crea formularios con ModelForm.
- Configura las rutas y plantillas necesarias.

### Ejercicio 3: Generación de Facturas Simples
Descripción: Crea una aplicación que permita generar y visualizar facturas simples.

**Pistas:**

- Define modelos para `Cliente`, `Factura` y `ProductoFactura` (relación muchos a muchos entre `Factura` y `Producto`).
- Implementa formularios para crear facturas, seleccionando clientes y productos.
- Crea una vista para mostrar el detalle de una factura, incluyendo los productos y el total.
- Usa plantillas para renderizar la información de la factura en formato HTML.

### Ejercicio 4: Sistema de Comentarios
Descripción: Implementa un sistema de comentarios donde los usuarios autenticados puedan comentar en artículos.

**Pistas:**

- Define modelos para `Articulo` y `Comentario`, donde `Comentario` tiene una relación de clave foránea con `Articulo`.
- Asegúrate de que solo los usuarios autenticados puedan agregar comentarios.
- Muestra los comentarios debajo de cada artículo.
- Utiliza formularios y vistas para manejar la creación y visualización de comentarios.

### Ejercicio 5: API REST Básica
Descripción: Crea una API REST para un modelo, por ejemplo, Producto, usando Django REST Framework.

**Pistas:**

- Instala y configura Django REST Framework.
- Define un serializer para el modelo Producto.
- Crea vistas de la API usando APIView o ViewSets.
- Configura las rutas de la API en urls.py usando DefaultRouter de DRF.
- Implementa autenticación básica para proteger ciertas rutas de la API.