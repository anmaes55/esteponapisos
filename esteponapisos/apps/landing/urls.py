from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('callesestepona', views.callesestepona, name='callesestepona'),
    path('orquidarioestepona', views.orquidarioestepona, name='orquidarioestepona'),
    path('catalogo_4B', views.catalogo_4B, name='catalogo_4B'),

]