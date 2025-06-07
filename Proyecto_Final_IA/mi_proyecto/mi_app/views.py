from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Paciente
from .forms import PacienteForm
from django.shortcuts import render
import subprocess
from django.views.decorators.csrf import csrf_exempt
from .scripts.datos_paciente import procesar_paciente

@csrf_exempt  # Solo para pruebas; mejor usar el token CSRF en producción
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

def datos_paciente_view(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            estadio, grafico_html = procesar_paciente(form.cleaned_data)
            return render(request, 'resultado_paciente.html', {
                'nombre': form.cleaned_data['nombre'],
                'estadio': estadio,
                'grafico_html': grafico_html
            })
        else:
            # Si no es válido, re-renderiza con errores
            return render(request, 'datos_paciente.html', {'form': form})
    else:
        form = PacienteForm()
    return render(request, 'datos_paciente.html', {'form': form})

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
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'
    success_url = reverse_lazy('paciente_list')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')