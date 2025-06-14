from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cliente

@receiver(post_save, sender=User)
def crear_cliente(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance, nombre=instance.username, email=instance.email)
