from django.db import models

class Clientes(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"