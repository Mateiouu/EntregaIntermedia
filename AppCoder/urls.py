
from django.contrib import admin
from django.urls import path
from AppCoder.views import *
urlpatterns = [
    
    
    path('', inicio ,name = 'inicio'),
    path('atletas/', atleta, name = 'atleta'),
    path('entrenador/', entrenador, name = 'entrenador'),
    path('deportes/', deporte, name = 'deporte'),
    path('lista-atletas', lista_atletas,name = 'lista_atletas'),
    path('lista-deportes', lista_deportes,name = 'lista_deportes'),
    path('lista-entrenadores', lista_entrenadores,name = 'lista_entrenadores'),
    path('busqueda-atleta', busquedaAtleta,name = 'busquedaAtleta'),
    path('buscaratleta', buscarAtleta,name = 'buscarAtleta'),
    path('busqueda-entrenador', busquedaEntrenador,name = 'busquedaEntrenador'),
    path('buscarentrenador', buscarEntrenador,name = 'buscarEntrenador'),
    path('busqueda-deporte', busquedaDeporte,name = 'busquedaDeporte'),
    path('buscardeporte', buscarDeporte,name = 'buscarDeporte'),
    
    
]
