from unicodedata import name
from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio, name ='inicio'),
    path('comidas/', comidas, name = 'comidas'),
    path('busquedaComidas/', busquedaComidas, name ='busquedaComidas' ),
    path('resultadoComidas/', buscarComidas, name = 'buscarComidas'),
    path('bebidas/', bebidas, name = 'bebidas'),
    path('busquedaBebidas/', busquedaBebidas, name ='busquedaBebidas' ),
    path('resultadoBebidas/', buscarBebidas, name = 'buscarBebidas'),
    path('otros/', otros, name = 'otros'),
    path('busquedaOtros/', busquedaOtros, name ='busquedaOtros' ),
    path('resultadoOtros/', buscarOtros, name = 'buscarOtros'),
    
]
