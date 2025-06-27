from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
    fecha = forms.DateField(label="Fecha de Analítica", widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.ChoiceField(choices=Paciente.GENERO_CHOICES)
    tfg = forms.IntegerField(label="Tfg - [ >90 ml/min/1,73 m2 ]", min_value=1)
    presion_arterial_sistolica = forms.IntegerField(label="Presión Arterial Sistólica - [ <120 mm Hg ]", min_value=1)
    presion_arterial_diastolica = forms.IntegerField(label="Presión Arterial Diastólica - [ <80 mm Hg ]", min_value=1)
    obesidad = forms.ChoiceField(choices=Paciente.OBESIDAD_CHOICES)
    albumina = forms.IntegerField(label="Albúmina - g/L [ 34 - 48 ]", min_value=1)
    erc = forms.IntegerField(label="ERC - [ 1 - 5 ]", min_value=0, max_value=5, required=False, initial=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hacer el campo solo visible (no editable)
        self.fields['erc'].disabled = True