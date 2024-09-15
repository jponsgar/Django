from django.urls import path
from . import views

urlpatterns = [
    path('factura/nueva/', views.crear_factura, name='crear_factura'),
    path('factura/<int:pk>/', views.detalle_factura, name='detalle_factura'),
]



