from django.shortcuts import render
from .serializer import GeneroSerializer,CancionSerializer,ArtistaSerializer,AlbumSerializer
from backend.models import Genero,Cancion,Artista,Album
from rest_framework import viewsets

# Create your views here.
class GeneroViewSet(viewsets.ViewSet):
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()
    
class CancionViewSet(viewsets.ViewSet):
    serializer_class = CancionSerializer
    queryset = Cancion.objects.all()
    
class ArtistaViewSet(viewsets.ViewSet):
    serializer_class = ArtistaSerializer
    queryset = Artista.objects.all()
    
class AlbumViewSet(viewsets.ViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    
    
