urlpatterns = [
    path('', views.index, name='index'),
    path('snake/', views.start_snake_game, name='start_snake_game'),
]
