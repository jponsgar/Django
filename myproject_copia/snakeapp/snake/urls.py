from django.urls import path
from .views import SnakeCreateView, SnakeListView, SnakeUpdateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', SnakeCreateView.as_view(), name='snake_create'),
    path('list/', SnakeListView.as_view(), name='snake_list'),
    path('update/<int:pk>/', SnakeUpdateView.as_view(), name='snake_update'),
]
