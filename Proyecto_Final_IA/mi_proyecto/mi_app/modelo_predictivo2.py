import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import timedelta
from .models import Paciente

def construir_tendencia_paciente(paciente):
    historial = Paciente.objects.filter(nombre=paciente.nombre).order_by('fecha')
    if historial.count() < 2:
        return "<p>No hay suficientes registros para mostrar tendencia.</p>"

    fechas = [p.fecha for p in historial]
    base_fecha = fechas[0]

    # Variables clínicas
    variables = {
        'ERC': [p.erc for p in historial],
        'TFG': [p.tfg for p in historial],
        'Creatinina': [p.creatinina for p in historial],
        'Albúmina': [p.albumina for p in historial],
    }

    graficos_html = ""

    for nombre_var, valores in variables.items():
        x = np.array([(f - base_fecha).days for f in fechas]).reshape(-1, 1)
        y = np.array(valores)

        modelo = LinearRegression().fit(x, y)

        # Proyección a 12 meses
        fechas_futuras = [fechas[-1] + timedelta(days=30 * i) for i in range(1, 13)]
        x_futuro = np.array([(f - base_fecha).days for f in fechas_futuras]).reshape(-1, 1)
        y_futuro = modelo.predict(x_futuro)
        y_estimada = modelo.predict(x)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fechas, y=valores, mode='lines+markers', name=f'{nombre_var} Real'))
        fig.add_trace(go.Scatter(x=fechas, y=y_estimada, mode='lines', name='Estimación'))
        fig.add_trace(go.Scatter(x=fechas_futuras, y=y_futuro, mode='lines+markers', name='Proyección 1 Año', line=dict(dash='dot')))

        fig.update_layout(
            title=f'Tendencia de {nombre_var} para {paciente.nombre}',
            xaxis_title='Fecha',
            yaxis_title=nombre_var,
            height=450
        )

        graficos_html += pyo.plot(fig, output_type='div')

    return graficos_html