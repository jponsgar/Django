'''
Método de IA utilizado
El programa utiliza un modelo de Aprendizaje Automático (IA), concretamente un clasificador SVM (Máquinas de Vectores de Soporte),
previamente entrenado y guardado en el archivo modelo_entrenado.pkl. Además, emplea un escalador de características (escalador.pkl)
para normalizar los datos antes de hacer la predicción.

Cómo funciona el programa
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
'''

import pandas as pd
import joblib
import plotly.express as px
import io

scaler = joblib.load('escalador.pkl')
svm = joblib.load('modelo_entrenado.pkl')

def procesar_paciente(data_dict):
    nombre = data_dict['nombre']
    edad = int(data_dict['edad'])
    fecha = data_dict('Fecha')
    genero = int(data_dict['genero'])
    creatinina = float(data_dict['creatinina'])
    tfg = int(data_dict['tfg'])
    presion_arterial_sistolica = int(data_dict['presion_arterial_sistolica'])
    presion_arterial_diastolica = int(data_dict['presion_arterial_diastolica'])
    obesidad = int(data_dict['obesidad'])
    albumina = int(data_dict['albumina'])

    nuevo_paciente = pd.DataFrame([{
        'nombre': nombre,
        'Edad': edad,
        'Fecha': fecha,
        'Genero': genero,
        'Creatinina': creatinina,
        'TFG': tfg,
        'Presion Arterial Sistolica': presion_arterial_sistolica,
        'Presion Arterial Diastolica': presion_arterial_diastolica,
        'Obesidad': obesidad,
        'Albumina': albumina
    }])

    features = ['Edad', 'Genero', 'Creatinina', 'TFG',
                'Presion Arterial Sistolica', 'Presion Arterial Diastolica',
                'Obesidad', 'Albumina']

    nuevo_paciente_scaled = scaler.transform(nuevo_paciente[features])
    estadio_usuario = svm.predict(nuevo_paciente_scaled)[0]
    nuevo_paciente['Prediccion Estadio ERC'] = estadio_usuario
    nuevo_paciente['ID'] = nombre

    data = pd.read_csv('datos_aleatorios_resultado.csv')
    if 'ID' not in data.columns:
        data['ID'] = data.index

    data = pd.concat([data, nuevo_paciente], ignore_index=True)

    fig = px.scatter_3d(
        data,
        x='Creatinina',
        y='TFG',
        z='Albumina',
        color='Estadio ERC',
        color_continuous_scale='Bluered',
        title='Riesgo Renal por ID - Femenino=0 - Masculino=1 - Obesidad=1 - No Obesidad=0',
        hover_data=['ID', 'Estadio ERC', 'Edad', 'Fecha', 'Genero', 'Presion Arterial Sistolica', 'Presion Arterial Diastolica', 'Obesidad']
)

    fig.add_trace(
     px.scatter_3d(
        nuevo_paciente,
        x='Creatinina',
        y='TFG',
        z='Albumina',
        hover_data=['ID', 'Prediccion Estadio ERC', 'Edad', 'Fecha', 'Genero', 'Presion Arterial Sistolica', 'Presion Arterial Diastolica', 'Obesidad'],
        ).update_traces(marker=dict(color='yellow', size=10, symbol='diamond'), showlegend=False).data[0]
)

    grafico_path = 'grafico_3d_riesgo_renal.html'
    fig.write_html(grafico_path)
  
    buffer = io.StringIO()
    fig.write_html(buffer, include_plotlyjs='cdn')
    html_graph = buffer.getvalue()

    return estadio_usuario, html_graph