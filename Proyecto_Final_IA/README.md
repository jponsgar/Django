"""
Prompt: Implementar con Django un CRUD (Create, Read, Update, Delete) básico para un modelo. Definir el modelo Paciente en models.py con campos; Nombre, Fechas, 'Edad: int', 'Genero', 'Creatinina: float', 'TFG: int', 'Presion_Arterial_Sistolica: int ', 'Presion_Arterial_Diastolica: int', 'Obesidad', 'Albumina: int', 'Estacio_ERC: int'. Usar vistas basadas en clases (Class-Based Views) como ListView, DetailView, CreateView, UpdateView y DeleteView.  Crear formularios con ModelForm. Configurar las rutas y plantillas necesarias. Se solicitarán los datos del paciente manualmente; Nombre, Fechas, 'Edad', 'Genero: "Masculino" o "Femenino"', 'Creatinina: float', 'TFG: int', 'Presion Arterial Sistolica:int ', 'Presion Arterial Diastolica: int', 'Obesidad: "Sí" o "No"', 'Albumina: int''. Que se procesarán como entrada en el programa python datos_paciente.py, el cual sacará un print con el "Estadio ERC" y un html llamado Estadio_ERC.html, esta información deberá mostrarse en la web.
También crear el urls.py y los htmls en la carpeta templates.
"""

### 0. Configuración e Instalación del Proyecto Django

pip install django
python -m django startproject mi_proyecto
cd mi_proyecto
python -m django startapp mi_app

### 1. Definir el modelo `Paciente` en `mi_app/models.py`:

from django.db import models

class Paciente(models.Model):
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    ]
    
    OBESIDAD_CHOICES = [
        ('Sí', 'Sí'),
        ('No', 'No')
    ]
    
    nombre = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    creatinina = models.FloatField(default=0)
    tfg = models.PositiveIntegerField()
    presion_arterial_sistolica = models.PositiveIntegerField()
    presion_arterial_diastolica = models.PositiveIntegerField()
    obesidad = models.CharField(max_length=2, choices=OBESIDAD_CHOICES)
    albumina = models.PositiveIntegerField()
    

    def __str__(self):
        return self.nombre

### 2. Crear el formulario con ModelForm, en `mi_app/forms.py`:

from django import forms

class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length=10)
    edad = forms.IntegerField(min_value=1)
    genero = forms.ChoiceField(choices=[('1', 'Masculino'), ('0', 'Femenino')])
    creatinina = forms.FloatField(label="Creatinina - mg/dL [ 0.30 - 1.30 ]", min_value=0.1)
    tfg = forms.IntegerField(label="Tfg - [ >90 ml/min/1,73 m2 ]", min_value=1)
    pas = forms.IntegerField(label="Presión Arterial Sistólica - [ <120 mm Hg ]", min_value=1)
    pad = forms.IntegerField(label="Presión Arterial Diastólica - [ <80 mm Hg ]", min_value=1)
    obesidad = forms.ChoiceField(choices=[('1', 'Sí'), ('0', 'No')])
    albumina = forms.IntegerField(label="Albúmina - g/L [ 34 - 48 ]", min_value=1)

### 3. Configurar las vistas basadas en clases `'Paciente`, `Entrenamiento`, etc. en `mi_app/views.py`:

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm
from django.shortcuts import render
import subprocess
from django.views.decorators.csrf import csrf_exempt
from .scripts.datos_paciente import procesar_paciente

@csrf_exempt  # Solo para pruebas; mejor usar el token CSRF en producción
def entrenar_view(request):
    resultado = ""
    if request.method == "POST":
        try:
            # Ejecutar el script Python
            proceso = subprocess.run(
                ['python3', 'mi_app/scripts/entrenar.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            resultado = proceso.stdout if proceso.returncode == 0 else proceso.stderr
        except Exception as e:
            resultado = f"Error al ejecutar el script: {e}"

    return render(request, 'entrenar.html', {'resultado': resultado})

def crear_datos_view(request):
    resultado = ""
    if request.method == "POST":
        try:
            # Ejecutar el script Python
            proceso = subprocess.run(
                ['python3', 'mi_app/scripts/crear_datos.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            resultado = proceso.stdout if proceso.returncode == 0 else proceso.stderr
        except Exception as e:
            resultado = f"Error al ejecutar el script: {e}"

    return render(request, 'crear_datos.html', {'resultado': resultado})

def datos_paciente_view(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            estadio, grafico_html = procesar_paciente(form.cleaned_data)
            return render(request, 'resultado_paciente.html', {
                'nombre': form.cleaned_data['nombre'],
                'estadio': estadio,
                'grafico_html': grafico_html
            })
        else:
            # Si no es válido, re-renderiza con errores
            return render(request, 'datos_paciente.html', {'form': form})
    else:
        form = PacienteForm()
    return render(request, 'datos_paciente.html', {'form': form})

def index(request):
    return render(request, 'index.html')

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')

### 4. Configurar las rutas en `urls.py`, en `mi_app/urls.py`:

from django.urls import path
from .views import PacienteListView, PacienteDetailView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView
from . import views
from mi_app.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('nuevo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('<int:pk>/eliminar/', PacienteDeleteView.as_view(), name='paciente_delete'),
    path('entrenar/', views.entrenar_view, name='entrenar'),
    path('crear_datos/', views.crear_datos_view, name='crear_datos'),
    path('datos_paciente/', views.datos_paciente_view, name='datos_paciente'),
    path('resultado_paciente/', views.datos_paciente_view, name='resultado_paciente'),
]

### 5. `mi_app/models.py`

from django.db import models

class Paciente(models.Model):
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    ]
    
    OBESIDAD_CHOICES = [
        ('Sí', 'Sí'),
        ('No', 'No')
    ]
    
    nombre = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    creatinina = models.FloatField(default=0)
    tfg = models.PositiveIntegerField()
    presion_arterial_sistolica = models.PositiveIntegerField()
    presion_arterial_diastolica = models.PositiveIntegerField()
    obesidad = models.CharField(max_length=2, choices=OBESIDAD_CHOICES)
    albumina = models.PositiveIntegerField()
    

    def __str__(self):
        return self.nombre

### 6. Crear htmls, en `mi_app/templates`:

#### `index.html`

<!DOCTYPE html>
{% load static %}
<html lang="es">
<head>
    <meta name="descripcion" content="Pacientes Estadio ERC">
    <meta name="autor" content="Jordi">
    <title>{% block title %}Pacientes Estadio ERC{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
</head>
<body>
    <header>
      <h1><ins>Pacientes Estadio ERC</ins></h1>
    </header>
  <div class="container">
    <nav class="sidebar">
      <ul>
          <br>
          <li><a href="{% url 'crear_datos' %}">Crear Dataframe "Estadio ERC"</a></li>
          <br>
          <li><a href="{% url 'entrenar' %}">Entrenar Datos "Estadio ERC"</a></li>
          <br>
          <li><a href="{% url 'datos_paciente' %}">Introducir Datos Paciente</a></li>
      </ul>
    </nav>
    <main class="contenido">
        {% block content %}
        {% endblock %}
        <br>
        <h2>¿Qué son los Estados de Enfermedad Renal Crónica?</h2>
        <br>
        <p>La Enfermedad Renal Crónica (ERC) se clasifica en cinco estados según la función renal medida por el 
          Filtrado Glomerular Estimado (FGe). A medida que la enfermedad progresa, los riñones pierden su capacidad 
          para filtrar desechos y líquidos de manera eficiente.</p>
        <br>
        <ul>
            <li><strong>Estado 1:</strong> Daño renal con función normal (Tfg ≥ 90 ml/min).</li>
            <li><strong>Estado 2:</strong> Disminución leve de la función renal (Tfg 60-89 ml/min).</li>
            <li><strong>Estado 3:</strong> Disminución moderada de la función renal (Tfg 30-59 ml/min).</li>
            <li><strong>Estado 4:</strong> Disminución grave de la función renal (Tfg 15-29 ml/min).</li>
            <li><strong>Estado 5:</strong> Insuficiencia renal terminal (Tfg menor 15 ml/min o diálisis).</li>
        </ul>
        <br>
        <h2>Parámetros de Analítica de Sangre con Indicios de ERC</h2>
        <br>
        <p>Existen varios indicadores en la analítica de sangre que pueden señalar la presencia de ERC:</p>
        <br>
        <ul>
            <li><strong>Creatinina:</strong> Elevados niveles indican posible deterioro de la función renal.</li>
            <li><strong>Filtrado Glomerular Estimado (Tfg):</strong> Menor Tfg sugiere un avance de la ERC.</li>
            <li><strong>Albúmina:</strong> Valores bajos en sangre, puede indicar la pérdida de albúmina en orina, y una mala función renal.</li>
        </ul>
        <br>
        <p>Dependiendo de algunos de estos valores, el paciente puede situarse en uno de los estados de la ERC mencionados anteriormente.</p>
        <br>
        <h2>Simulación del Estado ERC con Inteligencia Artificial</h2>
        <br>
        <p>Esta web tiene como propósito realizar simulaciones del estado 
          ERC de un paciente utilizando un modelo de Aprendizaje Automático: el **Support Vector Machine (SVM)**.</p>
          <br>
        <p>El **SVM** es un algoritmo de aprendizaje supervisado que clasifica 
          datos en distintas categorías. En este caso, se entrenará con historiales clínicos para predecir el estado 
          de la ERC según los parámetros de análisis de sangre.</p>
        <br>
        <p>El proceso incluye:</p>
        <br>
        <ul>
            <li><strong>Recopilación de datos de pacientes con antecedentes de ERC.</strong></li>
            <li><strong>Entrenamiento del modelo con características clave.</strong></li>
            <li><strong>Evaluación de nuevos pacientes para estimar su estado ERC.</strong></li>
        </ul>
        <br>
    </main>
  </div>
  <footer>
    <p>&copy; 2025 Hospital ERC. Todos los derechos reservados.</p>
  </footer>
</body>
</html>

#### `crear_datos.html`

<!DOCTYPE html>
{% load static %}
<html lang="es">
<head>
    <meta name="descripcion" content="Pacientes Estadio ERC">
    <meta name="autor" content="Jordi">
    <title>{% block title %}Pacientes Estadio ERC{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
</head>
<body>
    <header>
      <h1><ins>Crear Datos Entrenados</ins></h1>
    </header>
  <div class="container2">
    <nav class="sidebar2">
    </nav>
     <main class="contenido">
      <form method="post">
        <br><br>
        {% csrf_token %}
        <button type="submit">Ejecutar creación</button>
        <br><br>
        <a href="{% url 'index' %}">  Cancelar</a>
    </form>
    {% if resultado %}
        <h2>Resumen de los Datos</h2>
        <br>
        <pre>{{ resultado }}</pre>
        <br><br>
        <p style="text-align:center;">
        <a href="{% url 'index' %}">  Volver a la página Principal</a>
        </p>
    {% endif %}
    </main>
  </div>
  <footer>
    <p>&copy; 2025 Hospital ERC. Todos los derechos reservados.</p>
  </footer>
</body>
</html>

#### `entrenar.html`

<!DOCTYPE html>
{% load static %}
<html lang="es">
<head>
    <meta name="descripcion" content="Pacientes Estadio ERC">
    <meta name="autor" content="Jordi">
    <title>{% block title %}Pacientes Estadio ERC{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
</head>
<body>
    <header>
      <h1><ins>Entrenar modelo</ins></h1>
    </header>
  <div class="container2">
    <nav class="sidebar2">
    </nav>
     <main class="contenido">
      <form method="post">
        <br><br>
        {% csrf_token %}
        <button type="submit">Ejecutar entrenamiento</button>
        <br><br>
        <a href="{% url 'index' %}">  Cancelar</a>
    </form>
    {% if resultado %}
        <h2 style="text-align:center;">Resumen del Resultado</h2>
        <img src="{% static 'matriz_confusion.jpg' %}">
        <pre>{{ resultado }}</pre>
        <br>
        <p style="text-align:center;">
        <a href="{% url 'index' %}">  Volver a la página Principal</a>
        </p>
    {% endif %}
    </main>
  </div>
  <footer>
    <p>&copy; 2025 Hospital ERC. Todos los derechos reservados.</p>
  </footer>
</body>
</html>

#### `datos_paciente.html`

<!DOCTYPE html>
{% load static %}
<html lang="es">
<head>
    <meta name="descripcion" content="Pacientes Estadio ERC">
    <meta name="autor" content="Jordi">
    <title>{% block title %}Pacientes Estadio ERC{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
</head>
<body>
    <header>
      <h1><ins>Formulario de Datos del Paciente</ins></h1>
    </header>
  <div class="container2">
    <nav class="sidebar2">
    </nav>
     <main class="contenido">
      <form method="post">
         <br><br>
         {% csrf_token %}
         <br><br>
         {{ form.as_p }}
         <br><br>
         <button type="submit">Enviar</button>
         <br><br>
         <a href="{% url 'index' %}">  Cancelar</a>
      </form>
    </main>
  </div>
  <footer>
    <p>&copy; 2025 Hospital ERC. Todos los derechos reservados.</p>
  </footer>
</body>
</html>

#### `resultado_paciente.html`

<!DOCTYPE html>
{% load static %}
<html lang="es">
<head>
    <meta name="descripcion" content="Pacientes Estadio ERC">
    <meta name="autor" content="Jordi">
    <title>{% block title %}Pacientes Estadio ERC{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">
</head>
<body>
    <header>
      <h1><ins>Resultado para {{ nombre }}</ins></h1>
    </header>
  <div class="container2">
    <nav class="sidebar2">
    </nav>
     <main class="contenido">
        <p style="text-decoration: underline;";>Estadio ERC Predicho para {{ nombre }} 'en amarillo': <strong>{{ estadio }}</strong></p>
        <div>
         {{ grafico_html|safe }}
        <p style="text-align:center;">
        <a href="{% url 'index' %}">  Volver a la página Principal</a>
        </p>
        </div>
    </main>
  </div>
  <footer>
    <p>&copy; 2025 Hospital ERC. Todos los derechos reservados.</p>
  </footer>
</body>
</html>

### 7. Pythons, en `mi_app/scripts/`:

crear_datos.py
datos_paciente.py
entrenar.py

### 8. Configurar las URLs del proyecto, en `project/urls.py`:

from django.contrib import admin
from django.urls import path, include
from mi_app.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('mi_app.urls')),
    path('', index, name='index'),  # Configurar la URL principal
]

### 9. Migrar los cambios a la base de datos desde la ruta `/mi_proyecto` :

en bash:
python manage.py makemigrations
python manage.py migrate

### 10. Ejecutar el servidor desde la ruta `/mi_proyecto` :

en bash:
cd Proyecto_Final_IA
cd mi_proyecto
python runserver_open.py 
o
python manage.py runserver

Este python lanza la siguiente url: http://127.0.0.1:8000/