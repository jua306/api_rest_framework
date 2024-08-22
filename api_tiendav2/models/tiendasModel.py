from django.db import models

class Tiendas(models.Model):
    nombre_tienda = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    nit = models.CharField(max_length=20, unique=True)
    dueño = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_tienda