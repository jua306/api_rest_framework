from django.db  import models
from .clientesModel import Clientes
from .productosModel import Productos
from .tiendasModel import Tiendas



class Compra(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tiendas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cliente: {self.cliente.nombre}, Producto: {self.producto.nombre_producto}, Tienda: {self.tienda.nombre_tienda}"
