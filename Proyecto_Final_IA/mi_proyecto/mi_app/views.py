from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm
from django.shortcuts import render, redirect, get_object_or_404
import subprocess
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
# Asegúrate de que 'modelo_predictivo.py' existe en el directorio 'mi_app'
from .modelo_predictivo import construir_grafico_desde_bd
from .modelo_predictivo2 import construir_tendencia_paciente

@csrf_protect
def entrenar_view(request):
    resultado = ""
    if request.method == "POST":
        try:
            # Ejecutar el script Python
            proceso = subprocess.run(
                ['python3', 'mi_app/scripts/entrenar.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            resultado = proceso.stdout if proceso.returncode == 0 else proceso.stderr
        except Exception as e:
            resultado = f"Error al ejecutar el script: {e}"

    return render(request, 'entrenar.html', {'resultado': resultado})

@csrf_protect 
def crear_datos_view(request):
    resultado = ""
    if request.method == "POST":
        try:
            # Ejecutar el script Python
            proceso = subprocess.run(
                ['python3', 'mi_app/scripts/crear_datos.py'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            resultado = proceso.stdout if proceso.returncode == 0 else proceso.stderr
        except Exception as e:
            resultado = f"Error al ejecutar el script: {e}"

    return render(request, 'crear_datos.html', {'resultado': resultado})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PacienteForm
from .models import Paciente

def datos_paciente_view(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = Paciente.objects.create(**form.cleaned_data)
            messages.success(request, f'Paciente "{paciente.nombre}" creado con éxito.')
            return redirect('paciente_list')  # Cambia esta línea si quieres redirigir a otra vista
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = PacienteForm()

    return render(request, 'datos_paciente.html', {'form': form})

def grafico_3d_view(request, pk):
    from .models import Paciente
    try:
        paciente = Paciente.objects.get(pk=pk)
    except Paciente.DoesNotExist:
        return render(request, 'grafico_renal.html', {
            'grafico': 'Paciente no encontrado.',
            'nombre': 'Desconocido',
            'estadio': 'N/A'
        })

    resultado = construir_grafico_desde_bd(paciente_id=pk)

    if isinstance(resultado, str):
        return render(request, 'grafico_renal.html', {
            'grafico': resultado,
            'nombre': paciente.nombre,
            'estadio': 'Error'
        })

    html_graph, nombre_paciente, estadio_predicho = resultado

    return render(request, 'grafico_renal.html', {
        'grafico': html_graph,
        'nombre': nombre_paciente,
        'estadio': estadio_predicho
    })

def grafico_tendencia_view(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    grafico_html = construir_tendencia_paciente(paciente)
    return render(request, 'grafico_tendencia.html', {'grafico': grafico_html, 'nombre': paciente.nombre})

def index(request):
    return render(request, 'index.html')

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente_detail.html'

class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'datos_paciente.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    
    def get_success_url(self):
        return reverse_lazy('paciente_detail', kwargs={'pk': self.get_object().pk})

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')