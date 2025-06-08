from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = RichTextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"