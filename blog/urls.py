from django.urls import path
from . import views

blog/urls.py
urlpatterns = [
    path('', views.post_list, name='post_list'),
]