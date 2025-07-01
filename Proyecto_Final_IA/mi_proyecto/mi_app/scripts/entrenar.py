# Entrenamiento de un modelo SVM para predecir el estadio de enfermedad renal crónica (ERC)
# pip install --upgrade kaleido
# pip install plotly
# pip install joblib
# pip install seaborn
# pip install scikit-learn
# pip install matplotlib

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
data['Estadio ERC'] = pd.to_numeric(data['Estadio ERC'], errors='coerce')

# Eliminar filas con NaN en la variable objetivo
data = data.dropna(subset=features)
    
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

# falsos positivos y falsos negativos
falsos_positivos = np.sum((y_pred == 1) & (y_test != 1))
falsos_negativos = np.sum((y_pred != 1) & (y_test == 1))
print(f"Falsos positivos: {falsos_positivos}")
print(f"Falsos negativos: {falsos_negativos}")


# verdaderos positivos y verdaderos negativos
verdaderos_positivos = np.sum((y_pred == 1) & (y_test == 1))    
verdaderos_negativos = np.sum((y_pred != 1) & (y_test != 1))
print(f"Verdaderos positivos: {verdaderos_positivos}")
print(f"Verdaderos negativos: {verdaderos_negativos}")
print(f"Total de positivos: {np.sum(y_test == 1)}")

# Métricas
print("Exactitud:", accuracy_score(y_test, y_pred))
print("\nReporte de clasificación:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['ERC 1', 'ERC 2', 'ERC 3', 'ERC 4', 'ERC 5'], yticklabels=['ERC 1', 'ERC 2', 'ERC 3', 'ERC 4', 'ERC 5'])

# Generar predicciones para el conjunto de datos completo
data['Prediccion Estadio ERC'] = svm.predict(scaler.transform(data[features]))
plt.title('Matriz de Confusión')
plt.xlabel('Predicción')
plt.ylabel('Real')
# plt.show()

# guardar imagen en fichero jpg
plt.savefig("mi_app/static/matriz_confusion.jpg")

# Generar predicciones para el conjunto de datos completo
data['Prediccion Estadio ERC'] = svm.predict(scaler.transform(data[features]))

# Guardar el modelo entrenado
import joblib
joblib.dump(svm, 'modelo_entrenado.pkl')

# Muestreo estratificado: 50 pacientes por estadio
data_muestreado = data.groupby('Estadio ERC', group_keys=False).apply(
    lambda x: x.sample(n=min(len(x), 50), random_state=42)
)
# Guardar el modelo entrenado en csv
data_muestreado.to_csv('datos_aleatorios_resultado.csv', index=False)

# Guardar el escalador
joblib.dump(scaler, 'escalador.pkl')

# Proyecto Final IA: Análisis de Datos de Enfermedad Renal Crónica (ERC)
# Análisis de la edad promedio y proporción de género por estadio ERC

# Cargar los datos procesados
data = pd.read_csv('datos_aleatorios_resultado.csv', sep=',')

# Asegurar tipos adecuados
data['Genero'] = pd.to_numeric(data['Genero'], errors='coerce')
data['Edad'] = pd.to_numeric(data['Edad'], errors='coerce')
data['Estadio ERC'] = pd.to_numeric(data['Estadio ERC'], errors='coerce')

# Agrupación por Estadio ERC
resumen = data.groupby('Estadio ERC').agg(
    Edad_Promedio=('Edad', 'mean'),
    Proporcion_Masculino=('Genero', lambda x: (x == 1).mean()),
    Total_Pacientes=('Genero', 'count')
).reset_index()

# Añadir proporción femenina
resumen['Proporcion_Femenino'] = 1 - resumen['Proporcion_Masculino']

# -------- Gráfico 1: Edad Promedio por Estadio --------
plt.figure(figsize=(8, 5))
plt.bar(resumen['Estadio ERC'], resumen['Edad_Promedio'], color='skyblue', edgecolor='black')
for i, valor in enumerate(resumen['Edad_Promedio']):
    plt.text(resumen['Estadio ERC'][i], valor + 0.5, f'{valor:.1f}', ha='center')
plt.xlabel('Estadio ERC')
plt.ylabel('Edad Promedio (años)')
plt.title('Edad Promedio por Estadio ERC')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("mi_app/static/edad_promedio_por_estadio.jpg")

# -------- Gráfico 2: Proporción de Género por Estadio --------
anchos = 0.45
x = np.arange(len(resumen['Estadio ERC']))

plt.figure(figsize=(11, 7))
plt.bar(x - anchos/2, resumen['Proporcion_Masculino'], width=anchos, label='Masculino', color='#3366CC')
plt.bar(x + anchos/2, resumen['Proporcion_Femenino'], width=anchos, label='Femenino', color='#FF6666')

# Agregar textos sobre las barras
for i in range(len(x)):
    plt.text(x[i] - anchos/2, resumen['Proporcion_Masculino'][i] + 0.01, f"{resumen['Proporcion_Masculino'][i]:.0%}", ha='center')
    plt.text(x[i] + anchos/2, resumen['Proporcion_Femenino'][i] + 0.01, f"{resumen['Proporcion_Femenino'][i]:.0%}", ha='center')

plt.xticks(x, resumen['Estadio ERC'].astype(str).tolist())
plt.xlabel('Estadio ERC')
plt.ylabel('Proporción')
plt.title('Proporción Masculina vs Femenina por Estadio ERC')
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("mi_app/static/proporcion_genero_por_estadio.jpg")