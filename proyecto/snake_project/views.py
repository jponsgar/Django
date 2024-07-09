import os
from django.http import HttpResponse

def start_snake_game(request):
    os.system('python3 snake_game.py')
    return HttpResponse("Game Over!")
