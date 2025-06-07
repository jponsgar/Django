from django.db import models

class Paciente(models.Model):
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    ]
    
    OBESIDAD_CHOICES = [
        ('Sí', 'Sí'),
        ('No', 'No')
    ]
    
    nombre = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    creatinina = models.FloatField(default=0)
    tfg = models.PositiveIntegerField()
    presion_arterial_sistolica = models.PositiveIntegerField()
    presion_arterial_diastolica = models.PositiveIntegerField()
    obesidad = models.CharField(max_length=2, choices=OBESIDAD_CHOICES)
    albumina = models.PositiveIntegerField()
    

    def __str__(self):
        return self.nombre