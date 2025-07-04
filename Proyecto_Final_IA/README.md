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

Este script en Python genera un conjunto de datos clínicos sintéticos y los guarda en un archivo CSV para su uso en modelos de inteligencia artificial.

¿Qué hace el código?
Generación de datos aleatorios realistas:

Crea registros de pacientes con variables como edad, fecha, género, obesidad, creatinina, TFG, albúmina, presión arterial y estadio de ERC.
Los valores se generan usando distribuciones estadísticas y reglas clínicas (por ejemplo, la creatinina y el TFG se ajustan según la edad, género y obesidad).
Clasificación del estadio ERC:

El estadio de la enfermedad renal crónica se determina automáticamente a partir del valor de TFG, siguiendo criterios médicos estándar.
Guardado en CSV:

Los datos generados se guardan en un archivo llamado datos_aleatorios.csv con los nombres de las columnas apropiados.
Visualización rápida:

Muestra por pantalla las primeras filas del DataFrame generado para verificar el resultado.
Resultado
Se crea un archivo datos_aleatorios.csv con 15,000 registros de pacientes simulados, cada uno con variables clínicas relevantes y el estadio de ERC calculado.
Se imprime en consola una muestra de los primeros registros para comprobar la estructura y el contenido de los datos.
En resumen:
El script automatiza la creación de un dataset clínico sintético, útil para entrenar y probar modelos de IA en el ámbito de la nefrología, sin necesidad de datos reales de pacientes.

## entrenar.py

Este script en Python entrena y evalúa un modelo de Máquinas de Vectores de Soporte (SVM) para predecir el estadio de la Enfermedad Renal Crónica (ERC) a partir de datos clínicos de pacientes.

¿Qué hace el código?
Carga y prepara los datos:

Lee un archivo CSV con datos de pacientes.
Convierte variables categóricas (género, obesidad) a valores numéricos.
Elimina filas con datos faltantes.
Entrenamiento del modelo:

Divide los datos en conjuntos de entrenamiento y prueba.
Escala las variables numéricas.
Entrena un modelo SVM para clasificar el estadio ERC.
Evaluación:

Realiza predicciones sobre los datos de prueba.
Calcula métricas como exactitud, matriz de confusión, falsos positivos/negativos y muestra un reporte de clasificación.
Guarda la matriz de confusión como imagen.
Exporta resultados y modelos:

Guarda el modelo entrenado y el escalador para su uso posterior.
Realiza un muestreo estratificado y guarda un nuevo CSV con los datos y las predicciones.
Análisis y visualización:

Calcula la edad promedio y la proporción de género por estadio ERC.
Genera y guarda gráficos de edad promedio y proporción de género por estadio.
Resultado
Un modelo SVM entrenado y guardado para predecir el estadio ERC.
Imágenes de la matriz de confusión, edad promedio por estadio y proporción de género por estadio.
Un archivo CSV con los datos procesados y las predicciones.
Métricas impresas en consola que permiten evaluar el rendimiento del modelo.
En resumen:
El script automatiza el entrenamiento, evaluación y análisis de un modelo de IA para predecir el estadio de ERC, generando resultados visuales y archivos útiles para su integración en una aplicación clínica.

### 9. Pythons, en `mi_app`

## modelo_predictivo.py

Este código en Python utiliza técnicas de machine learning y visualización para predecir y mostrar el estadio de la Enfermedad Renal Crónica (ERC) de pacientes.

¿Qué hace el código?
Carga modelos entrenados:
Utiliza joblib para cargar un escalador (scaler.pkl) y un modelo SVM (modelo_entrenado.pkl) previamente entrenados.

Obtiene datos del paciente:
Recupera los registros de pacientes desde la base de datos y los convierte en un DataFrame de pandas.

Preprocesa los datos:
Renombra columnas y selecciona las variables clínicas relevantes.

Predice el estadio ERC:
Escala los datos y usa el modelo SVM para predecir el estadio de ERC de cada paciente. Si se predice para un paciente concreto, actualiza ese valor en la base de datos.

Prepara los datos para visualización:
Lee un archivo CSV con datos históricos y concatena el nuevo registro.

Visualiza en 3D:
Utiliza Plotly para crear un gráfico 3D interactivo donde:

Cada punto representa un paciente.
El color indica el estadio de ERC.
El último paciente analizado se resalta en amarillo.
Devuelve el resultado:
Retorna el HTML del gráfico, el nombre del paciente y el estadio predicho.

Resultado
El resultado es un gráfico 3D interactivo que permite visualizar la posición clínica del paciente respecto a otros, junto con el estadio de ERC predicho por el modelo de IA.
Esto ayuda a médicos y pacientes a entender el riesgo y la situación clínica de manera visual y sencilla.

## modelo_predictivo2.py

El código en tu archivo utiliza Python para analizar y predecir la evolución de variables clínicas de pacientes con enfermedad renal crónica (ERC) usando técnicas de inteligencia artificial.

¿Qué hace el código?
Obtiene el historial clínico de un paciente desde la base de datos, ordenado por fecha.
Selecciona variables clínicas importantes: ERC, TFG, Creatinina y Albúmina.
Entrena dos modelos de IA para cada variable:
Random Forest Regressor
Gradient Boosting Regressor
Evalúa el rendimiento de cada modelo usando métricas como MAE (error absoluto medio) y R² (coeficiente de determinación).
Proyecta la evolución futura de cada variable para los próximos 6 meses.
Genera gráficos interactivos con Plotly que muestran:
Los valores reales históricos.
Las predicciones de ambos modelos.
Las proyecciones a futuro.
Resultado
El resultado es un conjunto de gráficos interactivos (uno por variable clínica) que permiten visualizar:

Cómo han evolucionado las variables clínicas del paciente.
Qué tendencia predicen los modelos de IA para los próximos meses.
Esto ayuda a médicos y pacientes a anticipar posibles cambios en la salud renal y tomar decisiones informadas.

### 10. Migrar los cambios a la base de datos desde la ruta `/mi_proyecto`

bash: python manage.py makemigrations / python manage.py migrate

### 11. Ejecutar el servidor desde la ruta `/mi_proyecto`

bash: cd Proyecto_Final_IA / cd mi_proyecto
bash: python runserver_open.py ó python manage.py runserver

Se lanza la siguiente url: http://127.0.0.1:8000/