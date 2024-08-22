from django.contrib import admin
from .models.comprasModel import Compra
from .models.clientesModel import Clientes
from .models.productosModel import Productos
from .models.tiendasModel import Tiendas
# Register your models here.

admin.site.register(Compra)
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Tiendas)