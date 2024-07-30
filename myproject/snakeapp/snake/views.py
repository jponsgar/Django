from django.shortcuts import render, redirect
from django.views import View
from .models import Snake

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class SaveScoreView(View):
    def post(self, request):
        nombre = request.POST.get('nombre')
        puntos = request.POST.get('puntos')
        Snake.objects.create(nombre=nombre, puntos=puntos)
        return redirect('scoreboard')

class ScoreboardView(View):
    def get(self, request):
        jugadores = Snake.objects.all().order_by('-puntos')
        return render(request, 'scoreboard.html', {'jugadores': jugadores})




