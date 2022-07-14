from django.db import models

class Clientes(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    dni= models.IntegerField()

class Proveedores(models.Model):

    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=50)
    cantidad_de_productos= models.IntegerField()

class Productos(models.Model):

    marca= models.CharField(max_length=30)
    precio= models.IntegerField()
    cantidad= models.IntegerField()
