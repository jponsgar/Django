from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    ClienteListView, ClienteDetailView, ClienteCreateView, 
    ClienteUpdateView, ClienteDeleteView,
    FacturaListView, FacturaDetailView, FacturaCreateView, 
    FacturaUpdateView, FacturaDeleteView
)

urlpatterns = [
    # URLs para Producto
    path('', ProductoListView.as_view(), name='producto_list'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('<int:pk>/borrar/', ProductoDeleteView.as_view(), name='producto_delete'),

    # URLs para Cliente
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # URLs para Facturas
    path('facturas/', FacturaListView.as_view(), name='factura_list'),
    path('facturas/<int:pk>/', FacturaDetailView.as_view(), name='factura_detail'),
    path('facturas/nuevo/', FacturaCreateView.as_view(), name='factura_create'),
    path('facturas/<int:pk>/editar/', FacturaUpdateView.as_view(), name='factura_update'),
    path('facturas/<int:pk>/eliminar/', FacturaDeleteView.as_view(), name='factura_delete'),
]

