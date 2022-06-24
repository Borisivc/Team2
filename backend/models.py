from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    
    def str(self):
        return self.nombre
    

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete = models.DO_NOTHING)
    artista = models.ForeignKey()
    duracion = models.IntegerField()
    
    def str(self):
        return self.nombre

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nombre_artistico = models.CharField(max_length=100)

    def str(self):
        return self.nombre_artistico