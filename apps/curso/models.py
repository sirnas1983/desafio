from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(
        max_length=50,
        )
    duracion = models.IntegerField(
        max_length=60        
        )
    fecha_inicio = models.DateField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre