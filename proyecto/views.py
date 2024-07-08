import os
from django.http import HttpResponse

def start_snake_game(request):
    os.system('python3 snake_game.py')
    return HttpResponse("Game Over!")

from django.shortcuts import render
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('snake_project/', admin.site.urls),
    path('snake/', include('snake_game.urls')),
]

def index(request):
    return render(request, 'snake_game/index.html')




