from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_tiendav2.views import ClientesViewSet, ProductoViewSet, TiendasViewSet, CompraView

router = DefaultRouter()
router.register(r'clientes', ClientesViewSet, basename='cliente')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'tiendas', TiendasViewSet, basename='tienda')
router.register(r'compras', CompraView, basename='compra')

urlpatterns = [
    path('', include(router.urls)),
]
