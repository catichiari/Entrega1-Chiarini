import email
from django.db import models

class Libro (models.Model):
    nombre = models.CharField(max_length=128)
    genero = models.CharField(max_length=128)
    editorial = models.CharField(max_length=128)
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True)

class Autor (models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    nacionalidad = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()

class Lector (models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    usuario = models.CharField(max_length=128)