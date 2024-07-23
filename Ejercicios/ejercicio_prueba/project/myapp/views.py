from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snake
from .forms import SnakeForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class SnakeListView(ListView):
    model = Snake
    template_name = 'snake_list.html'

class SnakeDetailView(DetailView):
    model = Snake
    template_name = 'snake_detail.html'

class SnakeCreateView(CreateView):
    model = Snake
    form_class = SnakeForm
    template_name = 'snake_form.html'
    success_url = reverse_lazy('snake_list')

class SnakeUpdateView(UpdateView):
    model = Snake
    form_class = SnakeForm
    template_name = 'snake_form.html'
    success_url = reverse_lazy('snake_list')

class SnakeDeleteView(DeleteView):
    model = Snake
    template_name = 'snake_confirm_delete.html'
    success_url = reverse_lazy('snake_list')


