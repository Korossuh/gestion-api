from django.urls import path,include
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("csv/", csvView, name='csv'),

    #Urls para exportar archivos csv
    path('exportar personas/', csvPersonas,name='csvPersonas'),
    path('exportar proyectos/',csvProyectos, name='csvProyectos'),
    path('exportar tareas/', csvTareas, name='csvTareas'),
    path('exportar comentarios/',csvComentarios, name='csvComentarios'),
    path('exportar documentos/', csvDocumentos, name='csvDocumentos'),
]