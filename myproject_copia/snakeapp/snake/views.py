from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Snake

def index(request):
    return render(request, 'index.html')

def snakes(request):
    snakes_list = Snake.objects.all()
    return render(request, 'snakes.html', {'snakes': snakes_list})


@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        player_name = request.POST.get('playerName')
        puntos = request.POST.get('puntos')
        snake = Snake(nombre=player_name, puntos=int(puntos))
        snake.save()
        return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail'})



