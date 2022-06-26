from django.contrib import admin
from .models import Genero,Cancion,Artista,Album

# Register your models here.
class GeneroAdmin(admin.ModelAdmin):
    list = ('nombre')
    admin.site.register(Genero)
    
class CancionAdmin(admin.ModelAdmin):
    list = ('nombre','genero','artista','duracion')
    admin.site.register(Cancion)
    
class ArtistaAdmin(admin.ModelAdmin):
    list = ('nombre','nombre_artistico')
    admin.site.register(Artista)

class AlbumAdmin(admin.ModelAdmin):
    list = ('nombre_album')
    admin.site.register(Album)