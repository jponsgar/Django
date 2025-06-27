from django.db import models

class Paciente(models.Model):

    OBESIDAD_CHOICES = [
    ('1', 'Sí'),
    ('0', 'No')
    ]

    GENERO_CHOICES = [
        ('1', 'Masculino'),
        ('0', 'Femenino')
    ]

    nombre = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    fecha = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    creatinina = models.FloatField(default=0)
    tfg = models.PositiveIntegerField()
    presion_arterial_sistolica = models.PositiveIntegerField()
    presion_arterial_diastolica = models.PositiveIntegerField()
    obesidad = models.CharField(max_length=1, choices=OBESIDAD_CHOICES)
    albumina = models.PositiveIntegerField()
    erc = models.PositiveIntegerField()
    

    def __str__(self):
        return self.nombre