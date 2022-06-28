from dataclasses import field
from pyexpat import model
from backend.models import Genero,Cancion,Artista,Album
from rest_framework import serializer

class GeneroSerializer(serializer.ModelSerializer):
    class Meta:
        model = Genero
        field = '__all__'
        
class CancionSerializer(serializer.ModelSerializer):
    class Meta:
        model = Cancion
        field = '__all__'
        
class ArtistaSerializer(serializer.ModelSerializer):
    class Meta:
        model = Artista
        field = '__all__'
        
class AlbumSerializer(serializer.ModelSerializer):
    class Meta:
        model = Album
        field = '__all__'
        


