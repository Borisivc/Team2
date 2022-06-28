from nturl2path import url2pathname
from django.contrib import admin
from django.urls import URLPattern, path
 
URLPattern = [
    path('admin/', admin.site.urls),
    ]