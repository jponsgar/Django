from django.urls import path
from .views import index, save_score

urlpatterns = [
    path('', index, name='index'),
    path('save_score/', save_score, name='save_score'),
    path('top_scores/', top_scores, name='top_scores'),
]
