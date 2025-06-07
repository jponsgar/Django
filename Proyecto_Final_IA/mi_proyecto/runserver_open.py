# runserver_open.py
import webbrowser
import time
import subprocess

# Ejecuta el servidor
proc = subprocess.Popen(['python', 'manage.py', 'runserver'])

# Espera un poco a que arranque
time.sleep(1)

# Abre el navegador
webbrowser.open('http://127.0.0.1:8000')
