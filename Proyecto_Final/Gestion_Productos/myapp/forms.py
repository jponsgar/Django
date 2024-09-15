from django import forms
from .models import Producto, Cliente, Factura

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['nombre', 'producto', 'cantidad']
