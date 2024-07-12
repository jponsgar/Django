from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname  = models.CharField(max_length=255)
  # El teléfono es opcional, puede ser None
  # Formato: +34 123 456 789
  phone     = models.CharField(max_length=15, blank=True, null=True)

  def __str__(self) -> str:
    return f"{self.id} - {self.firstname}, {self.lastname}"