'''
Método de IA utilizado:
En este script no se utiliza un método de Inteligencia Artificial (IA) propiamente dicho. 
El programa genera datos sintéticos de pacientes usando reglas lógicas y funciones aleatorias, 
pero no aplica modelos de aprendizaje automático ni técnicas de IA para analizar o predecir resultados.

Cómo funciona el programa:
Generación de datos aleatorios:
El script crea registros ficticios de pacientes con variables clínicas relevantes (edad, género, creatinina, TFG, presión arterial, obesidad, albúmina).
Asignación de estadio ERC:
Según los valores generados de TFG, creatinina y albúmina, se asigna un estadio de Enfermedad Renal Crónica (ERC) usando reglas condicionales.
Exportación a CSV:
Todos los registros se guardan en un archivo CSV llamado datos_aleatorios.csv.
Visualización:
Se muestra por pantalla un resumen de los primeros registros generados usando pandas.
Resultado
El resultado es un archivo CSV con 6000 registros simulados de pacientes, cada uno con variables clínicas y el estadio de ERC asignado según reglas médicas básicas.
Este archivo puede usarse posteriormente para entrenar o probar modelos de IA, pero el script en sí solo genera datos, no aplica IA.
'''

# generar fichero csv con datos aleatorios, con los siguientes encabezados: ID,Edad,Género,Creatinina,TFG,Presión Arterial Sistólica,Presión Arterial Diastólica,Obesidad,Albumina,Estadio ERC
import csv
import random
from datetime import date

def generar_datos_aleatorios(num_registros):
    datos = []
    for i in range(num_registros):
        id_registro = i + 1
        edad = int(random.uniform(13, 90))
        fecha = date.today()
        genero = random.choice(['Masculino', 'Femenino'])
        creatinina = round(random.uniform(0.3, 3.0),1)
        # creatinina = str(creatinina).replace('.', ',')
        tfg = int(random.uniform(10, 100))
        # tfg = str(tfg).replace('.', ',')
        presion_arterial_sistolica = int(random.randint(90, 180))
        presion_arterial_diastolica = int(random.randint(60, 120))
        Obesidad = random.choice(['Si', 'No'])
        albumina = int(random.uniform(20, 48))
        if tfg > 90 and creatinina >= 0.3 and creatinina <= 1.3 and albumina <= 50 and albumina >= 40:
            estadio_erc = int(1)
        elif tfg > 60 and tfg <= 90 and creatinina > 1.3 and creatinina <= 1.5 and albumina >= 38 and albumina < 48:
            estadio_erc = int(2)
        elif tfg >= 30 and tfg <= 60 and creatinina > 1.5 and creatinina <= 2.0 and albumina >= 35 and albumina < 38:
            estadio_erc = int(3)
        elif tfg >= 15 and tfg < 30 and creatinina > 2.0 and creatinina <= 2.5 and albumina >= 30 and albumina < 35:
            estadio_erc = int(4)
        elif tfg < 15 and creatinina > 2.5 and albumina < 30:
            estadio_erc = int(5)
        else:
            estadio_erc = ''
        datos.append([
            id_registro, edad, fecha, genero, creatinina, tfg,
            presion_arterial_sistolica, presion_arterial_diastolica,
            Obesidad, albumina, estadio_erc
        ])
    return datos
def guardar_datos_csv(nombre_archivo, datos):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv, delimiter=';')
        escritor.writerow([
            'ID', 'Edad', 'Fecha', 'Genero', 'Creatinina', 'TFG',
            'Presion Arterial Sistolica', 'Presion Arterial Diastolica',
            'Obesidad', 'Albumina', 'Estadio ERC'
        ])
        escritor.writerows(datos)
if __name__ == "__main__":  
    num_registros = 6000  # Número de registros a generar
    datos_aleatorios = generar_datos_aleatorios(num_registros)
    nombre_archivo = 'datos_aleatorios.csv'
    guardar_datos_csv(nombre_archivo, datos_aleatorios)
    print(f'Datos aleatorios nefrología en {nombre_archivo}')
    # Este script genera un archivo CSV con datos aleatorios relacionados con la salud renal.
    # Los datos incluyen ID, edad, fecha, género, creatinina, TFG, presión arterial, Obesidad, hipertensión y estadio de la ERC.
    # El archivo se guarda con el nombre 'datos_aleatorios.csv'.
    import pandas as pd
    df = pd.DataFrame(datos_aleatorios, columns=[
    'ID', 'Edad', 'Fecha', 'Genero', 'Creatinina', 'TFG',
    'Presion Arterial Sistolica', 'Presion Arterial Diastolica',
    'Obesidad', 'Albumina', 'Estadio ERC'
    ])
    print(df.head())