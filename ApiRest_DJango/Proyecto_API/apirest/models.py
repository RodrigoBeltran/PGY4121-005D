from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreUsuario=models.CharField(max_length=50)
    correo=models.EmailField(max_length=100)
    contrasena=models.CharField(max_length=50)
    