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

    def__str__(self):
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
    path('[int:pk](int:pk)/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('nuevo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('[int:pk](int:pk)/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('[int:pk](int:pk)/eliminar/', PacienteDeleteView.as_view(), name='paciente_delete'),
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

    def__str__(self):
        return self.nombre


### 6. Htmls, en `mi_app/templates`:

## `index.html`

## `crear_datos.html`

## `entrenar.html`

## `datos_paciente.html`

## `resultado_paciente.html`


### 7. Pythons, en `mi_app/scripts/`:

**crear_datos.py**

Método de IA utilizado en crear_datos.py:

En este script no se utiliza un método de Inteligencia Artificial (IA) propiamente dicho.
El programa genera datos sintéticos de pacientes usando reglas lógicas y funciones aleatorias,
pero no aplica modelos de aprendizaje automático ni técnicas de IA para analizar o predecir resultados.

Cómo funciona el programa (Generación de datos aleatorios):
El script crea registros ficticios de pacientes con variables clínicas relevantes (edad, género, creatinina, TFG, presión arterial, obesidad, albúmina).
Asignación de estadio ERC:
Según los valores generados de TFG, creatinina y albúmina, se asigna un estadio de Enfermedad Renal Crónica (ERC) usando reglas condicionales.
Exportación a CSV:
Todos los registros se guardan en un archivo CSV llamado datos_aleatorios.csv.
Visualización:
Se muestra por pantalla un resumen de los primeros registros generados usando pandas.
Resultado:
El resultado es un archivo CSV con 6000 registros simulados de pacientes, cada uno con variables clínicas y el estadio de ERC asignado según reglas médicas básicas.
Este archivo puede usarse posteriormente para entrenar o probar modelos de IA, pero el script en sí solo genera datos, no aplica IA.

**datos_paciente.py**

Método de IA utilizado en datos_paciente.py

El programa utiliza un modelo de Aprendizaje Automático (IA), concretamente un clasificador SVM (Máquinas de Vectores de Soporte),
previamente entrenado y guardado en el archivo modelo_entrenado.pkl. Además, emplea un escalador de características (escalador.pkl)
para normalizar los datos antes de hacer la predicción.

Cómo funciona el programa:
Carga de modelos:
Se cargan el modelo SVM y el escalador desde archivos previamente entrenados.

Procesamiento de datos del paciente:
Se recibe un diccionario con los datos clínicos de un paciente (edad, género, creatinina, TFG, presión arterial, obesidad, albúmina, etc.).

Normalización:
Los datos del paciente se transforman usando el escalador para que tengan la misma escala que los datos usados en el entrenamiento del modelo.

Predicción:
El modelo SVM predice el estadio de Enfermedad Renal Crónica (ERC) del paciente a partir de sus datos clínicos.

Visualización:
Se genera un gráfico 3D interactivo con Plotly, mostrando la posición del paciente respecto a otros datos y su estadio ERC predicho.

El Resultado es:

La Predicción automática del estadio ERC para el paciente introducido, usando IA.
Visualización interactiva en 3D de los datos clínicos y el estadio predicho.
El estadio predicho y el gráfico pueden ser usados para apoyar el diagnóstico y seguimiento clínico.

**entrenar.py**

Método de IA utilizado en entrenar.py

El programa utiliza un modelo de Aprendizaje Automático llamado SVM (Máquinas de Vectores de Soporte), que es un clasificador supervisado.
Este modelo se entrena para predecir el estadio de Enfermedad Renal Crónica (ERC) a partir de variables clínicas de los pacientes.

Cómo funciona el programa
Carga y preparación de datos:
Se cargan los datos sintéticos de pacientes desde un archivo CSV. Se seleccionan las variables relevantes y se convierten los datos categóricos
(género y obesidad) a valores numéricos.

División de datos:
Los datos se dividen en conjuntos de entrenamiento y prueba para evaluar el rendimiento del modelo.

Normalización:
Se normalizan las variables numéricas usando un escalador (StandardScaler) para que todas tengan la misma escala.

Entrenamiento del modelo:
Se entrena un clasificador SVM con kernel RBF usando los datos de entrenamiento.

Evaluación:
Se hacen predicciones sobre el conjunto de prueba y se calculan métricas como la exactitud, el reporte de clasificación y la matriz de confusión,
que se guarda como imagen.

Guardado de resultados:
El modelo entrenado y el escalador se guardan en archivos (modelo_entrenado.pkl y escalador.pkl). También se guarda un CSV con las predicciones y
se calcula la mediana de variables clínicas por estadio ERC.

Resultado:
Modelo SVM entrenado y guardado para futuras predicciones.
Escalador guardado para normalizar nuevos datos.
Archivo CSV con los datos originales y las predicciones del modelo.
Matriz de confusión guardada como imagen para analizar el rendimiento.
Resumen estadístico (mediana) de variables clínicas por estadio ERC.
Este modelo puede ser usado posteriormente para predecir el estadio ERC de nuevos pacientes y apoyar el diagnóstico clínico.

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

bash: python manage.py makemigrations / python manage.py migrate

### 10. Ejecutar el servidor desde la ruta `/mi_proyecto` :

bash: cd Proyecto_Final_IA / cd mi_proyecto / python runserver_open.py
o
python manage.py runserver

Este python lanza la siguiente url: http://127.0.0.1:8000/