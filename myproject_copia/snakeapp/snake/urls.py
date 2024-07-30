from django.urls import path
from .views import IndexView, SaveScoreView, ScoreboardView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('save-score/', SaveScoreView.as_view(), name='save_score'),
    path('scoreboard/', ScoreboardView.as_view(), name='scoreboard'),
]

