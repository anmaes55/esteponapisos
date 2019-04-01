from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('callesestepona', views.callesestepona, name='callesestepona'),
    path('orquidarioestepona', views.orquidarioestepona, name='orquidarioestepona'),
    path('catalogo_4A', views.catalogo_4A, name='catalogo_4A'),
    path('catalogo_4B', views.catalogo_4B, name='catalogo_4B'),
    path('catalogo_4C', views.catalogo_4C, name='catalogo_4C'),
    path('catalogo_4D', views.catalogo_4D, name='catalogo_4D'),
    path('contactar', views.contactar, name='contactar'),
    path('mensaje-enviado', views.mensaje_enviado, name='mensaje-enviado'),
    path('menu', views.menu, name='menu'),

    path('carrusel', views.carrusel, name='carrusel'),

]