# Proyecto Final IA: CRUD Django para Pacientes y Predicción de Estadio ERC

Prompt: Implementar con Django un CRUD (Create, Read, Update, Delete) básico para un modelo. Definir el modelo Paciente en models.py con campos; Nombre, Fechas, 'Edad: int', 'Genero', 'Creatinina: float', 'TFG: int', 'Presion_Arterial_Sistolica: int ', 'Presion_Arterial_Diastolica: int', 'Obesidad', 'Albumina: int', 'Estacio_ERC: int'. Usar vistas basadas en clases (Class-Based Views) como ListView, DetailView, CreateView, UpdateView y DeleteView.  Crear formularios con ModelForm. Configurar las rutas y plantillas necesarias. Se solicitarán los datos del paciente manualmente; Nombre, Fechas, 'Edad', 'Genero: "Masculino" o "Femenino"', 'Creatinina: float', 'TFG: int', 'Presion Arterial Sistolica:int ', 'Presion Arterial Diastolica: int', 'Obesidad: "Sí" o "No"', 'Albumina: int''. Que se procesarán como entrada en el programa python datos_paciente.py, el cual sacará un print con el "Estadio ERC" y un html llamado Estadio_ERC.html, esta información deberá mostrarse en la web.
También crear el urls.py y los htmls en la carpeta templates.

## 0. Configuración e Instalación del Proyecto Django

pip install django
python -m django startproject mi_proyecto
cd mi_proyecto
python -m django startapp mi_app

### 1. Crear `mi_app/models.py`

### 2. Crear el formulario con ModelForm, en `mi_app/forms.py`

### 3. Configurar las rutas en `urls.py`, en `mi_app/urls.py`

### 4. Configurar las rutas en `views.py`, en `mi_app/views.py`

### 5. Crear `mi_poyecto/urls.py`

### 6. Añadir mi_app `mi_poyecto/settings.py`

### 7. Crear Htmls, en `mi_app/templates`

## `crear_datos.html`

## `datos_paciente.html`

## `grafico_renal.html`

## `grafico_tendencia.html`

## `index.html`

## `paciente_confirm_delete.html`

## `paciente_detail.html`

## `paciente_list`

### 8. Pythons, en `mi_app/scripts/`

## crear_datos.py

El código utiliza un enfoque completo de machine learning para analizar y predecir el estadio de la Enfermedad Renal Crónica (ERC) en pacientes simulados.

Método IA utilizado
Generación de datos sintéticos:
Se crean 15,000 registros de pacientes con variables clínicas realistas (edad, género, creatinina, TFG, presión arterial, albúmina, obesidad, estadio ERC).

Preprocesamiento:
Las variables categóricas (género, obesidad) se convierten a valores numéricos.
Se eliminan registros incompletos.

Entrenamiento del modelo:
Se utiliza un Random Forest Classifier (un modelo de árboles de decisión en conjunto) para predecir el estadio ERC a partir de las variables clínicas.
Los datos se dividen en entrenamiento y prueba, y se escalan para mejorar el rendimiento del modelo.

Evaluación:
Se calcula la exactitud, matriz de confusión, reporte de clasificación y métricas de falsos/verdaderos positivos y negativos.

Exportación:
El modelo y el escalador se guardan para su uso posterior.
Se genera un muestreo estratificado de pacientes por estadio y se guarda en un nuevo CSV.

Análisis y visualización:
Se calcula la edad promedio y la proporción de género por estadio ERC.
Se generan gráficos de edad promedio y proporción de género por estadio.

Resultado
Un modelo de IA entrenado capaz de predecir el estadio ERC de nuevos pacientes a partir de sus datos clínicos.
Imágenes de la matriz de confusión, edad promedio por estadio y proporción de género por estadio.
Archivos CSV con los datos simulados y las predicciones.
Métricas impresas en consola para evaluar el rendimiento del modelo.
En resumen:
El método permite simular, analizar y predecir el estadio de ERC usando IA, y visualizar los resultados de forma clara y útil para aplicaciones clínicas.

### 9. Pythons, en `mi_app`

## modelo_predictivo.py

El método de IA utilizado en este código es una Máquina de Vectores de Soporte (SVM) para la predicción del estadio de la Enfermedad Renal Crónica (ERC) de pacientes.

¿Cómo funciona el método?
Carga de modelos entrenados:
Se cargan un escalador (scaler.pkl) y un modelo SVM (modelo_entrenado.pkl) previamente entrenados con datos clínicos.

Obtención y preprocesamiento de datos:
Se extraen los datos del paciente desde la base de datos y se preparan las variables relevantes (edad, género, creatinina, TFG, presión arterial, obesidad, albúmina).

Predicción:
Los datos se escalan y se pasan al modelo SVM, que predice el estadio ERC para cada paciente.

Actualización en la base de datos:
Si se trata de un paciente concreto, el estadio predicho se guarda en la base de datos.

Visualización:
Se genera un gráfico 3D interactivo con Plotly, donde:

Cada punto representa un paciente.
El color indica el estadio ERC.
El paciente analizado se resalta en amarillo.
Resultado devuelto:
Se retorna el HTML del gráfico, el nombre del paciente y el estadio predicho.

Resultado
Predicción personalizada: El modelo SVM estima el estadio ERC del paciente analizado.
Visualización clínica: El gráfico 3D permite comparar la situación del paciente con otros casos.
Actualización automática: El estadio predicho se guarda en la base de datos para futuras consultas.
En resumen:
El método permite predecir el estadio ERC de un paciente usando IA y visualizar su situación clínica de forma interactiva y comparativa.

## modelo_predictivo2.py

El método de IA utilizado en este código es la predicción de tendencias clínicas mediante dos modelos de regresión:

Random Forest Regressor
Gradient Boosting Regressor
¿Cómo funciona el método?
Obtención de historial clínico:
Se extraen los registros históricos de un paciente (por nombre) desde la base de datos.

Selección de variables:
Se analizan las variables ERC, TFG, Creatinina y Albúmina a lo largo del tiempo.

Entrenamiento de modelos:
Para cada variable, se entrena un modelo Random Forest y uno Gradient Boosting usando los días transcurridos como variable independiente y los valores clínicos como variable dependiente.

Evaluación:
Se calculan métricas de rendimiento (MAE y R²) para cada modelo y variable.

Proyección futura:
Los modelos predicen la evolución de cada variable para los próximos 6 meses.

Visualización:
Se generan gráficos interactivos con Plotly que muestran:

Valores reales históricos.
Predicciones de ambos modelos.
Proyección a futuro.
Rangos clínicos normales y alertas si hay valores fuera de rango.
Gráfico combinado:
Se crea un gráfico adicional que muestra la evolución conjunta de TFG, Creatinina y Albúmina.

Resultado
Gráficos interactivos que permiten visualizar la evolución histórica y futura de las variables clínicas del paciente.
Alertas automáticas si algún valor está fuera del rango clínico recomendado.
Comparación visual entre la tendencia real y la estimada por los modelos de IA.
Herramienta de apoyo para el seguimiento y la toma de decisiones clínicas personalizadas.
En resumen:
El método permite anticipar la evolución clínica de un paciente con ERC usando IA y visualizar los resultados de forma clara y útil para médicos y pacientes.

### 10. Migrar los cambios a la base de datos desde la ruta `/mi_proyecto`

bash: python manage.py makemigrations / python manage.py migrate

### 11. Ejecutar el servidor desde la ruta `/mi_proyecto`

bash: cd Proyecto_Final_IA / cd mi_proyecto
bash: python runserver_open.py ó python manage.py runserver

Se lanza la siguiente url: [http://127.0.0.1:8000/]