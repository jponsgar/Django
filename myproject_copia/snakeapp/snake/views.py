from django.shortcuts import render
from .models import Snake

def index(request):
    return render(request, 'index.html')

def snakes(request):
    snakes_list = Snake.objects.all()
    return render(request, 'snakes.html', {'snakes': snakes_list})


