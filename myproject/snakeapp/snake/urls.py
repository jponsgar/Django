from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snakes/', views.snakes, name='snakes'),
    path('save_score/', views.save_score, name='save_score'),
]
