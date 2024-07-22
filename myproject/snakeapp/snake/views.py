from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Snake

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def snakes(request):
    snakes = Snake.objects.all()
    return render(request, 'snakes.html', {'snakes': snakes})
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        puntos = request.POST.get('puntos')
        snake = Snake(nombre=nombre, puntos=int(puntos))
        snake.save()
        return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail'})



