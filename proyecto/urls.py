from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('', views.index, name='index'),
    path('snake_project/', views.snake_project, name='snake_project'),
]
