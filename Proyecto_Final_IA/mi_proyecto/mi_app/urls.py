from django.urls import path
from .views import PacienteListView, PacienteDetailView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView, grafico_tendencia_view
from . import views
from mi_app.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('nuevo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('<int:pk>/editar/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('<int:pk>/eliminar/', PacienteDeleteView.as_view(), name='paciente_delete'),
    path('crear_datos/', views.crear_datos_view, name='crear_datos'),
    path('datos_paciente/', views.datos_paciente_view, name='datos_paciente'),
    path('grafico_renal/<int:pk>/', views.grafico_3d_view, name='grafico_renal'),
    path('grafico_tendencia/<int:pk>/', grafico_tendencia_view, name='grafico_tendencia'),
]