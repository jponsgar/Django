'''
Método de IA utilizado
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

Resultado
Modelo SVM entrenado y guardado para futuras predicciones.
Escalador guardado para normalizar nuevos datos.
Archivo CSV con los datos originales y las predicciones del modelo.
Matriz de confusión guardada como imagen para analizar el rendimiento.
Resumen estadístico (mediana) de variables clínicas por estadio ERC.
Este modelo puede ser usado posteriormente para predecir el estadio ERC de nuevos pacientes y apoyar el diagnóstico clínico.
'''

# Entrenamiento de un modelo SVM para predecir el estadio de enfermedad renal crónica (ERC)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar datos desde el archivo CSV con el separador correcto
data = pd.read_csv('datos_aleatorios.csv', sep=';')

# Seleccionar características relevantes y la variable objetivo
features = ['Edad', 'Genero', 'Creatinina', 'TFG',
            'Presion Arterial Sistolica', 'Presion Arterial Diastolica',
            'Obesidad', 'Albumina']
target = 'Estadio ERC'

# Limpiar espacios y convertir a minúsculas para mapear correctamente y fecha en float
data['Genero'] = data['Genero'].str.strip().str.lower().map({'masculino': 1, 'femenino': 0})
data['Obesidad'] = data['Obesidad'].str.strip().str.lower().map({'si': 1, 'no': 0})
data['Estadio ERC']

# Eliminar filas con NaN en la variable objetivo
data = data.dropna(subset=['Estadio ERC'])
    
X = data[features]
y = data[target]

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entrenar SVM con kernel RBF
svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(X_train_scaled, y_train)

# Predicciones
y_pred = svm.predict(X_test_scaled)

# Métricas
print("Exactitud:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['ERC 1', 'ERC 2', 'ERC 3', 'ERC 4', 'ERC 5'], yticklabels=['ERC 1', 'ERC 2', 'ERC 3', 'ERC 4', 'ERC 5'])

# Generar predicciones para el conjunto de datos completo
data['Prediccion Estadio ERC'] = svm.predict(scaler.transform(data[features]))
plt.title('Matriz de Confusión')

# plt.show()

# guardar imagen en fichero jpg
plt.savefig("mi_app/static/matriz_confusion.jpg")

# Generar predicciones para el conjunto de datos completo
data['Prediccion Estadio ERC'] = svm.predict(scaler.transform(data[features]))

# Guardar el modelo entrenado
import joblib
joblib.dump(svm, 'modelo_entrenado.pkl')

# Guardar el modelo entrenado en csv
data.to_csv('datos_aleatorios_resultado.csv', index=False)

# Guardar el escalador
joblib.dump(scaler, 'escalador.pkl')

# calcular mediana por estadio ERC por 'Edad', 'Genero', 'Presion Arterial Sistolica', 'Presion Arterial Diastolica', 'Obesidad'
mediana_por_estadio = data.groupby('Estadio ERC')[['Edad', 'Genero', 'Presion Arterial Sistolica', 'Presion Arterial Diastolica', 'Obesidad']].median().reset_index()

# renombrar valores de las columnas 'Genero' y 'Obesidad' en el DataFrame de la mediana
mediana_por_estadio['Genero'] = mediana_por_estadio['Genero'].apply(lambda x: 'Masculino' if x > 0.5 else 'Femenino')
mediana_por_estadio['Obesidad'] = mediana_por_estadio['Obesidad'].apply(lambda x: 'Si' if x > 0.5 else 'No')
mediana_por_estadio['Edad'] = mediana_por_estadio['Edad'].astype(int)
mediana_por_estadio['Presion Arterial Sistolica'] = mediana_por_estadio['Presion Arterial Sistolica'].astype(int)
mediana_por_estadio['Presion Arterial Diastolica'] = mediana_por_estadio['Presion Arterial Diastolica'].astype(int)
mediana_por_estadio['Estadio ERC'] = mediana_por_estadio['Estadio ERC'].astype(int)

# mostrar el resultado
print("\nMediana por Estadio ERC:\n", mediana_por_estadio)