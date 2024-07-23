from django.db import models

class Snake(models.Model):
    nombre = models.CharField(max_length=100)
    puntos = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

