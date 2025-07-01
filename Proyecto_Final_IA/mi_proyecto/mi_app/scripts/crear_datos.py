#pip install pandas numpy scikit-learn matplotlib seaborn plotly joblib kaleido

import csv
import random
from datetime import date
import pandas as pd

def generar_datos_aleatorios(num_registros):
    datos = []
    for i in range(num_registros):
        id_registro = i + 1
        edad = int(min(max(random.gauss(55, 15), 13), 90))
        fecha = date.today()
        genero = random.choice(['Masculino', 'Femenino'])

        # Obesidad
        obesidad = random.choices(['Si', 'No'], weights=[0.35, 0.65])[0]

        # Creatinina y TFG con ruido controlado y ajustes por edad/género/obesidad
        creatinina = max(0.3, round(random.gauss(1.0, 0.3), 2))
        tfg = int(max(5, min(random.gauss(75, 20), 120)))
        albumina = int(min(max(random.gauss(40, 5), 20), 48))

        # Ajustes por edad
        if edad > 65:
            creatinina += random.uniform(0.2, 0.5)
            tfg -= random.randint(5, 15)

        # Ajustes por género
        if genero == 'Femenino':
            creatinina -= 0.1
            tfg += random.randint(3, 7)

        # Ajustes por obesidad
        presion_arterial_sistolica = random.randint(100, 160)
        presion_arterial_diastolica = random.randint(60, 100)
        if obesidad == 'Si':
            presion_arterial_sistolica += random.randint(5, 15)
            presion_arterial_diastolica += random.randint(3, 10)

        # Clasificación ERC solo por TFG
        if tfg >= 90:
            estadio_erc = 1
        elif tfg >= 60:
            estadio_erc = 2
        elif tfg >= 30:
            estadio_erc = 3
        elif tfg >= 15:
            estadio_erc = 4
        else:
            estadio_erc = 5

        datos.append([
            id_registro, edad, fecha, genero, round(creatinina, 2), tfg,
            presion_arterial_sistolica, presion_arterial_diastolica,
            obesidad, albumina, estadio_erc
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
    num_registros = 15000
    datos_aleatorios = generar_datos_aleatorios(num_registros)
    nombre_archivo = 'datos_aleatorios.csv'
    guardar_datos_csv(nombre_archivo, datos_aleatorios)
    print(f'Datos aleatorios realistas generados en {nombre_archivo}')

    df = pd.DataFrame(datos_aleatorios, columns=[
        'ID', 'Edad', 'Fecha', 'Genero', 'Creatinina', 'TFG',
        'Presion Arterial Sistolica', 'Presion Arterial Diastolica',
        'Obesidad', 'Albumina', 'Estadio ERC'
    ])
    print(df.head())