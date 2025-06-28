'''Random Forest y Gradient Boosting para la predicción de tendencias clínicas de pacientes con ERC'''

import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
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

        # Random Forest
        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        rf.fit(x, y)
        y_rf_pred = rf.predict(x)

        # Gradient Boosting
        gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
        gb.fit(x, y)
        y_gb_pred = gb.predict(x)

        # Evaluación de rendimiento
        mae_rf = mean_absolute_error(y, y_rf_pred)
        r2_rf = r2_score(y, y_rf_pred)
        mae_gb = mean_absolute_error(y, y_gb_pred)
        r2_gb = r2_score(y, y_gb_pred)

        print(f"\nVariable: {nombre_var}")
        print(f"Random Forest → MAE: {mae_rf:.2f}, R²: {r2_rf:.2f}")
        print(f"Gradient Boosting → MAE: {mae_gb:.2f}, R²: {r2_gb:.2f}")

        # Proyección a 12 meses con ambos modelos
        fechas_futuras = [fechas[-1] + timedelta(days=30 * i) for i in range(1, 6)]
        x_futuro = np.array([(f - base_fecha).days for f in fechas_futuras]).reshape(-1, 1)
        y_rf_futuro = rf.predict(x_futuro)
        y_gb_futuro = gb.predict(x_futuro)

        # Crear gráfico con ambas predicciones
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fechas, y=valores, mode='lines+markers', name=f'{nombre_var} Real'))
        fig.add_trace(go.Scatter(x=fechas, y=y_rf_pred, mode='lines', name='Estimación RF', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=fechas, y=y_gb_pred, mode='lines', name='Estimación GB', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=fechas_futuras, y=y_rf_futuro, mode='lines+markers', name='Proy. RF 6 meses', line=dict(dash='dot', color='green')))
        fig.add_trace(go.Scatter(x=fechas_futuras, y=y_gb_futuro, mode='lines+markers', name='Proy. GB 6 meses', line=dict(dash='dot', color='blue')))

        fig.update_layout(
            title=f'Tendencia de {nombre_var} para {paciente.nombre}',
            xaxis_title='Fecha',
            yaxis_title=nombre_var,
            height=500
        )

        graficos_html += pyo.plot(fig, output_type='div')

    return graficos_html