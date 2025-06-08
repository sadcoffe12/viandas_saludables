from django.urls import path
from . import views
from .views import ListarProductoView, ListarPedidoView

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('pedido/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path("buscar-producto/", ListarProductoView.as_view(), name="buscar_producto"),
    path("buscar_pedido/", ListarPedidoView.as_view(), name="buscar_pedido"),
    path('about/', views.about, name='about'),
]
