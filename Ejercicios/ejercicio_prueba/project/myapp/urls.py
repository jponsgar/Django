from django.urls import path
from .views import (
    SnakeListView,
    SnakeDetailView,
    SnakeCreateView,
    SnakeUpdateView,
    SnakeDeleteView
)

urlpatterns = [
    path('', SnakeListView.as_view(), name='snake_list'),
    path('<int:pk>/', SnakeDetailView.as_view(), name='snake_detail'),
    path('nuevo/', SnakeCreateView.as_view(), name='snake_create'),
    path('<int:pk>/editar/', SnakeUpdateView.as_view(), name='snake_update'),
    path('<int:pk>/borrar/', SnakeDeleteView.as_view(), name='snake_delete'),
]

