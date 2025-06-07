from django.urls import path
from .views import PacienteListView, PacienteDetailView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView
from . import views
from mi_app.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('nuevo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('<int:pk>/eliminar/', PacienteDeleteView.as_view(), name='paciente_delete'),
    path('entrenar/', views.entrenar_view, name='entrenar'),
    path('crear_datos/', views.crear_datos_view, name='crear_datos'),
    path('datos_paciente/', views.datos_paciente_view, name='datos_paciente'),
    path('resultado_paciente/', views.datos_paciente_view, name='resultado_paciente'),
]