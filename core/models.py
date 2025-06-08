from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = RichTextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="Pendiente")

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - {self.fecha.strftime('%d/%m/%Y')}"