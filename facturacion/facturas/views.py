from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura, ProductoFactura
from .forms import FacturaForm, ProductoFacturaFormSet

def crear_factura(request):
    if request.method == 'POST':
        factura_form = FacturaForm(request.POST)
        formset = ProductoFacturaFormSet(request.POST)

        if factura_form.is_valid() and formset.is_valid():
            factura = factura_form.save()
            productos = formset.save(commit=False)
            for producto in productos:
                producto.factura = factura
                producto.save()
            return redirect('detalle_factura', pk=factura.pk)
    else:
        factura_form = FacturaForm()
        formset = ProductoFacturaFormSet()

    return render(request, 'facturas/crear_factura.html', {
        'factura_form': factura_form,
        'formset': formset
    })

def detalle_factura(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    productos = ProductoFactura.objects.filter(factura=factura)

    return render(request, 'facturas/detalle_factura.html', {
        'factura': factura,
        'productos': productos,
        'total': factura.total(),
    })

