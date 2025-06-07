from django.contrib import admin
from django.urls import path, include
from mi_app.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('mi_app.urls')),
    path('', index, name='index'),  # Configurar la URL principal
]