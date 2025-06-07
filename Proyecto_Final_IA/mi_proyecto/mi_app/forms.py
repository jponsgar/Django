from django import forms

class PacienteForm(forms.Form):
    nombre = forms.CharField(max_length=10)
    edad = forms.IntegerField(min_value=1)
    genero = forms.ChoiceField(choices=[('1', 'Masculino'), ('0', 'Femenino')])
    creatinina = forms.FloatField(label="Creatinina - mg/dL [ 0.30 - 1.30 ]", min_value=0.1)
    tfg = forms.IntegerField(label="Tfg - [ >90 ml/min/1,73 m2 ]", min_value=1)
    pas = forms.IntegerField(label="Presión Arterial Sistólica - [ <120 mm Hg ]", min_value=1)
    pad = forms.IntegerField(label="Presión Arterial Diastólica - [ <80 mm Hg ]", min_value=1)
    obesidad = forms.ChoiceField(choices=[('1', 'Sí'), ('0', 'No')])
    albumina = forms.IntegerField(label="Albúmina - g/L [ 34 - 48 ]", min_value=1)