'''Gráfico de predicción de estadio de ERC utilizando SVM y visualización con Plotly'''

import pandas as pd
import joblib
import plotly.express as px
import io
from .models import Paciente

# Cargar modelos previamente entrenados
scaler = joblib.load('escalador.pkl')
svm = joblib.load('modelo_entrenado.pkl')

def construir_grafico_desde_bd(paciente_id=None):
    if paciente_id is not None:
        registros = Paciente.objects.filter(id=paciente_id).values()
    else:
        registros = Paciente.objects.all().values()

    df = pd.DataFrame(list(registros))

    if df.empty:
        return "<p>No hay datos disponibles para generar el gráfico.</p>"

    df.rename(columns={
        'nombre': 'ID',
        'edad': 'Edad',
        'fecha': 'Fecha',
        'genero': 'Genero',
        'creatinina': 'Creatinina',
        'tfg': 'TFG',
        'presion_arterial_sistolica': 'Presion Arterial Sistolica',
        'presion_arterial_diastolica': 'Presion Arterial Diastolica',
        'obesidad': 'Obesidad',
        'albumina': 'Albumina'
    }, inplace=True)

    features = ['Edad', 'Genero', 'Creatinina', 'TFG',
                'Presion Arterial Sistolica', 'Presion Arterial Diastolica',
                'Obesidad', 'Albumina']

    try:
        df_scaled = scaler.transform(df[features])
        df['Prediccion Estadio ERC'] = svm.predict(df_scaled)
        nombre_paciente = df['ID'].iloc[-1]
        estadio_predicho = df['Prediccion Estadio ERC'].iloc[-1]

        # ✅ Actualizar el valor en la base de datos
        if paciente_id is not None:
            try:
                paciente_obj = Paciente.objects.get(id=paciente_id)
                paciente_obj.erc = estadio_predicho
                paciente_obj.save()
            except Paciente.DoesNotExist:
                return "<p>Paciente no encontrado en la base de datos.</p>"

    except Exception as e:
        return f"<p>Error al procesar los datos: {e}</p>"

    data = pd.read_csv('datos_aleatorios_resultado.csv')
    if 'ID' not in data.columns:
        data['ID'] = data.index

    data = pd.concat([data, df], ignore_index=True)

    fig = px.scatter_3d(
        data,
        x='Creatinina',
        y='TFG',
        z='Albumina',
        color='Estadio ERC',
        color_continuous_scale='Bluered',
        title='Riesgo Renal por ID - Femenino=0 - Masculino=1 - Obesidad=1 - No Obesidad=0',
        hover_data=['ID', 'Estadio ERC', 'Edad', 'Fecha', 'Genero',
                    'Presion Arterial Sistolica', 'Presion Arterial Diastolica', 'Obesidad']
    )

    fig.add_trace(
        px.scatter_3d(
            df,
            x='Creatinina',
            y='TFG',
            z='Albumina',
            hover_data=['ID', 'Prediccion Estadio ERC', 'Edad', 'Fecha', 'Genero',
                        'Presion Arterial Sistolica', 'Presion Arterial Diastolica', 'Obesidad']
        ).update_traces(marker=dict(color='yellow', size=10, symbol='diamond'), showlegend=False).data[0]
    )

    buffer = io.StringIO()
    fig.write_html(buffer, include_plotlyjs='cdn')
    html_graph = buffer.getvalue()

    return html_graph, nombre_paciente, estadio_predicho
