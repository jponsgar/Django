from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Snake

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nombre = data.get('nombre')
        puntos = data.get('puntos')
        jugador = Snake(nombre=nombre, puntos=puntos)
        jugador.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)



