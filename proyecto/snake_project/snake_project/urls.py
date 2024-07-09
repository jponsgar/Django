from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snake/', include('snake_project.urls')),
]


urlpatterns = [
    path('', views.index, name='index'),
]

