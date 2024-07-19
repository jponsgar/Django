from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Snake
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

class SnakeCreateView(CreateView):
    model = Snake
    fields = ['nombre', 'puntos']
    template_name = 'index.html'
    success_url = reverse_lazy('snake_list')

class SnakeListView(ListView):
    model = Snake
    template_name = 'snake_list.html'
    context_object_name = 'snakes'

class SnakeUpdateView(UpdateView):
    model = Snake
    fields = ['nombre', 'puntos']
    template_name = 'snake_update.html'
    success_url = reverse_lazy('snake_list')





