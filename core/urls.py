from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('pedido/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
]
