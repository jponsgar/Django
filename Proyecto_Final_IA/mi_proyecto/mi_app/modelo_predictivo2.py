'''Random Forest y Gradient Boosting para la predicción de tendencias clínicas de pacientes con ERC'''
#pip install plotly
#pip install joblib
#pip install seaborn
#pip install scikit-learn
#pip install matplotlib

import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from datetime import timedelta
from .models import Paciente

# Rango clínico de referencia por variable
RANGOS_CLINICOS = {
    'Creatinina': {'min': 0.30, 'max': 1.30, 'unidad': 'mg/dL'},
    'TFG': {'min': 90, 'unidad': 'ml/min/1.73 m²'},
    'Albúmina': {'min': 34, 'max': 48, 'unidad': 'g/L'},
    'ERC': {'min': 1, 'max': 4}
}

def agregar_rango_clinico(fig, fechas, nombre_var):
    """Agrega una franja visual del rango clínico (si aplica)"""
    rangos = RANGOS_CLINICOS.get(nombre_var, {})
    if 'min' in rangos and 'max' in rangos:
        fig.add_trace(go.Scatter(
            x=fechas + fechas[::-1],  # ida y vuelta para rellenar entre límites
            y=[rangos['min']] * len(fechas) + [rangos['max']] * len(fechas),
            fill='toself',
            fillcolor='rgba(0, 200, 0, 0.1)',  # verde suave
            line=dict(color='rgba(255,255,255,0)'),  # invisible
            hoverinfo='skip',
            showlegend=True,
            name='Rango Clínico Normal'
        ))

def agregar_anotaciones_y_lineas(fig, fechas, valores, nombre_var):
    rangos = RANGOS_CLINICOS.get(nombre_var, {})
    alertas = []

    # Líneas de referencia
    if 'min' in rangos:
        fig.add_shape(type="line", x0=fechas[0], x1=fechas[-1], y0=rangos['min'], y1=rangos['min'],
                      line=dict(color='red', dash='dot'))
    if 'max' in rangos:
        fig.add_shape(type="line", x0=fechas[0], x1=fechas[-1], y0=rangos['max'], y1=rangos['max'],
                      line=dict(color='red', dash='dot'))

    # Anotaciones por fuera de rango
    for i, valor in enumerate(valores):
        fuera = (
            ('min' in rangos and valor < rangos['min']) or
            ('max' in rangos and valor > rangos['max']) or
            (nombre_var == 'TFG' and valor < rangos.get('min', 0))
        )
        if fuera:
            fig.add_annotation(
                x=fechas[i], y=valor,
                text="🔴",
                showarrow=True,
                arrowhead=2,
                bgcolor='rgba(255,255,0,0.6)',
                font=dict(color='black')
            )
            alertas.append(fechas[i])
    return alertas

def construir_tendencia_paciente(paciente):
    historial = list(Paciente.objects.filter(nombre=paciente.nombre).order_by('fecha'))
    if len(historial) < 2:
        return "<p>No hay suficientes registros para mostrar tendencia.</p>"

    fechas = [p.fecha for p in historial]
    base_fecha = fechas[0]

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

        # Modelos de predicción
        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        rf.fit(x, y)
        y_rf_pred = rf.predict(x)

        gb = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
        gb.fit(x, y)
        y_gb_pred = gb.predict(x)

        # Métricas
        mae_rf = mean_absolute_error(y, y_rf_pred)
        r2_rf = r2_score(y, y_rf_pred)
        mae_gb = mean_absolute_error(y, y_gb_pred)
        r2_gb = r2_score(y, y_gb_pred)

        print(f"\nVariable: {nombre_var}")
        print(f"Random Forest → MAE: {mae_rf:.2f}, R²: {r2_rf:.2f}")
        print(f"Gradient Boosting → MAE: {mae_gb:.2f}, R²: {r2_gb:.2f}")

        # Proyección futura
        fechas_futuras = [fechas[-1] + timedelta(days=30 * i) for i in range(1, 6)]
        x_futuro = np.array([(f - base_fecha).days for f in fechas_futuras]).reshape(-1, 1)
        y_rf_futuro = rf.predict(x_futuro)
        y_gb_futuro = gb.predict(x_futuro)

        # Gráfico
        fig = go.Figure()
        agregar_rango_clinico(fig, fechas, nombre_var)
        fig.add_trace(go.Scatter(x=fechas, y=valores, mode='lines+markers', name=f'{nombre_var} Real', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=fechas, y=y_rf_pred, mode='lines', name='Estimación RF', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=fechas, y=y_gb_pred, mode='lines', name='Estimación GB', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=fechas_futuras, y=y_rf_futuro, mode='lines+markers', name='Proy. RF 6 meses', line=dict(dash='dot', color='green')))
        fig.add_trace(go.Scatter(x=fechas_futuras, y=y_gb_futuro, mode='lines+markers', name='Proy. GB 6 meses', line=dict(dash='dot', color='blue')))

        # Añadir anotaciones automáticas y líneas de referencia
        alertas = agregar_anotaciones_y_lineas(fig, fechas, valores, nombre_var)

        fig.update_layout(
            title=dict(
        text=f"<u>Tendencia de {nombre_var} para {paciente.nombre}</u>",
        x=0.5,
        xanchor='center'
        ),
            xaxis_title='Fecha',
            yaxis_title=nombre_var,
            height=500
        )

        graficos_html += pyo.plot(fig, output_type='div')

        # Mostrar rango clínico esperado como texto
        rangos = RANGOS_CLINICOS.get(nombre_var, {})
        if 'min' in rangos and 'max' in rangos:
            unidad = rangos.get('unidad', '')
            graficos_html += f"<p><em>Rango Clínico Esperado para {nombre_var}: {rangos['min']} - {rangos['max']} {unidad}</em></p>"
        elif 'min' in rangos:
            unidad = rangos.get('unidad', '')
            graficos_html += f"<p><em>Valor mínimo esperado para {nombre_var}: {rangos['min']} {unidad}</em></p>"

        if alertas:
            graficos_html += f"<p style='color:red'><strong>🔴Alerta:</strong> Se detectaron valores fuera de rango clínico en <strong>{nombre_var}</strong>.</p>"

    # Gráfico combinado de TFG, Creatinina y Albúmina

    # Diccionario de colores para cada variable
    colores = {'TFG': 'orange', 'Creatinina': 'red', 'Albúmina': 'teal'}

    # Rangos normales para cada parámetro
    rangos_normales = {
      'TFG': {'min': 90, 'max': 100},
      'Creatinina': {'min': 0.3, 'max': 1.3},
      'Albúmina': {'min': 34, 'max': 48}
    }

    fig_combinado = go.Figure()

    for var in ['TFG', 'Creatinina', 'Albúmina']:
        fig_combinado.add_trace(go.Scatter(
            x=fechas,
            y=variables[var],
            mode='lines+markers',
            name=var,
            line=dict(color=colores[var]),
            customdata=[f"{var}: {v:.2f}" for v in variables[var]],
            hovertemplate='%{customdata}<br>Fecha: %{x}<extra></extra>'
        ))
        
        # Bandas de rango saludable
        fig_combinado.add_shape(type='rect',
            xref='paper', yref='y',
            x0=0, x1=1,
            y0=rangos_normales[var]['min'],
            y1=rangos_normales[var]['max'],
            fillcolor=colores[var],
            opacity=0.1,
            line_width=0,
            layer='below'
        )

        # Línea de referencia media
        media = sum(variables[var]) / len(variables[var])
        fig_combinado.add_shape(type='line',
            xref='paper', yref='y',
            x0=0, x1=1,
            y0=media, y1=media,
            line=dict(color=colores[var], dash='dash')
        )

    fig_combinado.update_layout(
        title=dict(
        text=f"<u>Tendencia combinada: TFG, Creatinina y Albúmina para {paciente.nombre}</u>",
        x=0.5,
        xanchor='center'
    ),
        xaxis_title='Fecha',
        yaxis_title='Valor',
        height=600
    )

    graficos_html += pyo.plot(fig_combinado, output_type='div')

    return graficos_html