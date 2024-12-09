from django.contrib.auth import views as auth_views
from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

    path("",index,name='index'),
    path("csv/", csvView, name='csv'),
    path("Crud/",crudView, name='crudView'),

    #Urls para Crud Personas
    path("Personas/",personasView,name='personasView'),
    path("Add Personas/",personaAdd ,name='personaAdd'),
    path("Mod Personas/<int:id>",personaMod, name='personaMod'),
    path("Del Personas/<int:id>",personaDel,name='personaDel'),

    #Urls para Crud Proyectos
    path('proyectos/', proyectosView, name='proyectosView'),
    path('proyectos/crear/', proyectoAdd, name='proyectoAdd'),
    path('proyectos/modificar/<int:id>/', proyectoMod, name='proyectoMod'),
    path('proyectos/eliminar/<int:id>/', proyectoDel, name='proyectoDel'),

    #Urls para Crud Tareas
    path('tareas/', tareasView, name='tareasView'),
    path('tareas/crear/', tareaAdd, name='tareaAdd'),
    path('tareas/modificar/<int:id>/', tareaMod, name='tareaMod'),
    path('tareas/eliminar/<int:id>/', tareaDel, name='tareaDel'),

    #Urls para Crud Comentarios
    path('comentarios/', comentariosView, name='comentariosView'),
    path('comentarios/crear/', comentarioAdd, name='comentarioAdd'),
    path('comentarios/modificar/<int:id>/', comentarioMod, name='comentarioMod'),
    path('comentarios/eliminar/<int:id>/', comentarioDel, name='comentarioDel'),

    #Urls para Crud Documentos
     path('documentos/', documentosView, name='documentosView'),
    path('documentos/crear/', documentoAdd, name='documentoAdd'),
    path('documentos/modificar/<int:id>/', documentoMod, name='documentoMod'),
    path('documentos/eliminar/<int:id>/', documentoDel, name='documentoDel'),


    #Urls para exportar archivos csv
    path('exportar personas/', csvPersonas,name='csvPersonas'),
    path('exportar proyectos/',csvProyectos, name='csvProyectos'),
    path('exportar tareas/', csvTareas, name='csvTareas'),
    path('exportar comentarios/',csvComentarios, name='csvComentarios'),
    path('exportar documentos/', csvDocumentos, name='csvDocumentos'),
]