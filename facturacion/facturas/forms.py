from django import forms
from .models import Factura, ProductoFactura, Cliente, Producto

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
        fields = ['cliente']

class ProductoFacturaForm(forms.ModelForm):
    class Meta:
        model = ProductoFactura
        fields = ['producto', 'cantidad']

ProductoFacturaFormSet = forms.inlineformset_factory(
    Factura, ProductoFactura, form=ProductoFacturaForm, extra=1, can_delete=True
)


