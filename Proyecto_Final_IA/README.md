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

## `entrenar.html`

## `datos_paciente.html`

## `entrenar_resultados.html`

## `grafico_renal.html`

## `grafico_tendencia.html`

## `index.html`

## `paciente_confirm_delete.html`

## `paciente_detail.html`

## `paciente_list`

## `resultado_paciente.html`

### 8. Pythons, en `mi_app/scripts/`

## crear_datos.py

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

## datos_paciente.py

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

## entrenar.py

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

### 9. Pythons, en `mi_app`

## modelo_predictivo.py

Modelo de IA utilizado
En este proyecto se utiliza un modelo de Máquina de Vectores de Soporte (SVM) para predecir el estadio de la Enfermedad Renal Crónica (ERC) de los pacientes. El flujo es el siguiente:

Preprocesamiento:
Los datos de los pacientes se escalan usando un objeto scaler previamente entrenado (probablemente un StandardScaler de scikit-learn), cargado desde el archivo escalador.pkl.

Predicción:
El modelo SVM, cargado desde modelo_entrenado.pkl, toma las variables clínicas del paciente (edad, género, creatinina, TFG, presión arterial, obesidad, albúmina) y predice el estadio de ERC.

Actualización en base de datos:
Si se predice para un paciente concreto, el estadio predicho se guarda en la base de datos en el campo erc del paciente.

Resultado de la función
La función construir_grafico_desde_bd devuelve:

Un gráfico 3D interactivo generado con Plotly, que muestra la relación entre Creatinina, TFG y Albúmina, coloreando los puntos según el estadio de ERC.
El nombre del paciente para el que se ha realizado la predicción.
El estadio predicho por el modelo para ese paciente.
Este resultado permite visualizar de forma clara el riesgo renal y comparar el caso del paciente con otros datos almacenados.

Resumen:
El modelo SVM predice el estadio de ERC a partir de variables clínicas, y el resultado se muestra en un gráfico 3D junto con el nombre y el estadio predicho del paciente.

## modelo_predictivo2.py

Modelo de IA utilizado
En este caso, se utiliza un modelo de Regresión Lineal (LinearRegression de scikit-learn) para analizar la tendencia temporal de diferentes variables clínicas de un paciente concreto.
El modelo aprende la evolución de cada variable (ERC, TFG, Creatinina, Albúmina) a lo largo del tiempo, usando el historial de registros del paciente.

¿Qué hace la función?
Recopila el historial del paciente ordenado por fecha.
Para cada variable clínica (ERC, TFG, Creatinina, Albúmina):
Ajusta un modelo de regresión lineal para estimar la tendencia de la variable a lo largo del tiempo.
Proyecta la evolución de la variable durante los próximos 12 meses.
Genera un gráfico interactivo con:
Los valores reales históricos.
La estimación de la tendencia.
La proyección a futuro (1 año).
Resultado
La función devuelve un HTML con varios gráficos interactivos (uno por variable), donde se puede visualizar:

La evolución real de cada variable clínica.
La tendencia estimada por el modelo.
La proyección de esa variable para el próximo año.
Esto permite al usuario ver de forma visual y predictiva cómo podrían evolucionar los parámetros clínicos del paciente si la tendencia actual se mantiene.

Resumen:
Se usa regresión lineal para estimar y proyectar la evolución de variables clínicas de un paciente, mostrando los resultados en gráficos interactivos que permiten visualizar tanto el pasado como la posible evolución futura.

### 10. Migrar los cambios a la base de datos desde la ruta `/mi_proyecto`

bash: python manage.py makemigrations / python manage.py migrate

### 11. Ejecutar el servidor desde la ruta `/mi_proyecto`

bash: cd Proyecto_Final_IA / cd mi_proyecto
bash: python runserver_open.py ó python manage.py runserver

Se lanza la siguiente url: http://127.0.0.1:8000/