from django.db import models

class Snake(models.Model):
    nombre = models.CharField(max_length=50)
    puntos = models.IntegerField()

    def __str__(self):
        return self.nombre
