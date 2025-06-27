# runserver_open.py
import webbrowser
import time
import subprocess
import requests

# Ejecuta el servidor
proc = subprocess.Popen(['python', 'manage.py', 'runserver'])

# Espera hasta que el servidor esté disponible
url = 'http://127.0.0.1:8000'
max_retries = 10
wait_time = 1  # en segundos

for _ in range(max_retries):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            break
    except requests.ConnectionError:
        pass
    time.sleep(wait_time)
else:
    print("No se pudo conectar con el servidor después de varios intentos.")
    proc.terminate()
    exit(1)

# Abre el navegador
webbrowser.open(url)
