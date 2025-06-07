from django.http import JsonResponse
import subprocess

def ejecutar_python(request):
    # Código Python a ejecutar
    try:
        resultado = subprocess.check_output(['python', 'entrenar.py'], stderr=subprocess.STDOUT)
        # Convertir el resultado a texto
        nombre_archivo = resultado.decode('utf-8')
        return JsonResponse({'Datos aleatorios nefrología en': nombre_archivo})
        
    except subprocess.CalledProcessError as e:
        # Manejar errores
        return JsonResponse({'error': str(e)})
