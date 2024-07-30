from django.db import models

class Snake(models.Model):
    nombre = models.CharField(max_length=100)
    puntos = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.puntos}'

