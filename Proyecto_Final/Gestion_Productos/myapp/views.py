from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Cliente, Factura
from .forms import ProductoForm, ClienteForm, FacturaForm
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'index.html')

# Vistas para Producto
class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')

# Vistas para Cliente
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')

# Vistas para Factura
class FacturaListView(ListView):
    model = Factura
    template_name = 'factura_list.html'

class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'factura_detail.html'

class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura_form.html'
    success_url = reverse_lazy('factura_list')

class FacturaUpdateView(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura_form.html'
    success_url = reverse_lazy('factura_list')

class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = 'factura_confirm_delete.html'
    success_url = reverse_lazy('factura_list')
