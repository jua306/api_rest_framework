from django.db import models

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=100)
    codigo_barra = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre_producto

