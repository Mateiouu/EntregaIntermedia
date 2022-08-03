from django.db import models

# Create your models here.
class Atleta(models.Model):

    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    nacimiento = models.DateField()
    diciplina = models.CharField(max_length = 40)
    pais = models.CharField(max_length = 40)
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.diciplina} - {self.pais}"

class Entrenador(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length= 30)
    entrena = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.entrena}"

class Deportes(models.Model):

    nombre = models.CharField(max_length=30)
    incluye = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f"{self.nombre} - {self.incluye}"

