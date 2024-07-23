from django import forms
from .models import Snake

class SnakeForm(forms.ModelForm):
    class Meta:
        model = Snake
        fields = ['nombre']

