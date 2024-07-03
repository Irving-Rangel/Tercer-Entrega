from django.db import models

# Modelo de la aplicacion

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

class Cita(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)       
    email = models.EmailField()
    fechaCita = models.DateField()

