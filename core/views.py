from django.shortcuts import render
from django.http import HttpResponse
from api.models import * 
import csv

#Funcion para index
def index (request):
    return render(request,'index.html')

#Funcion para csv
def csvView(request):
    return render(request,'csv.html')

#=================================================
#======== FUNCIONES PARA DESCARGAR CSV ===========
#=================================================
def csvPersonas(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Persona.csv"'

    # Crear el archivo
    writer = csv.writer(response)
    # Definir encabezado de los campos
    writer.writerow(['ID','Nombre','Email','Telefono','Fecha Nacimiento'])

    personas = Persona.objects.all()
    for persona in personas:
        writer.writerow([
            persona.id,
            persona.nombre,
            persona.email,
            persona.telefono,
            persona.fecha_nacimiento
        ])

    return response

def csvProyectos(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Proyectos.csv"'

    # Crear el archivo
    writer = csv.writer(response)
    # Definir encabezado de los campos
    writer.writerow(['ID', 'Nombre', 'Descripción', 'Fecha Inicio', 'Fecha Fin', 'Persona Responsable'])

    # Escribir los datos en filas
    proyectos = Proyecto.objects.all()
    for proyecto in proyectos:
        writer.writerow([
            proyecto.id,
            proyecto.nombre,
            proyecto.descripcion,
            proyecto.fecha_inicio,
            proyecto.fecha_fin,
            proyecto.persona_responsable.nombre
        ])

    return response

def csvTareas(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Tareas.csv"'

    # Crear el archivo
    writer = csv.writer(response)
    # Definir encabezado de los campos
    writer.writerow(['ID', 'Título', 'Descripción', 'Estado', 'Proyecto', 'Asignado a'])

    # Escribir los datos en filas
    tareas = Tarea.objects.all()
    for tarea in tareas:
        writer.writerow([
            tarea.id,
            tarea.titulo,
            tarea.descripcion,
            tarea.estado,
            tarea.proyecto.nombre,
            tarea.asignado_a.nombre
        ])

    return response

def csvComentarios(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Comentarios.csv"'

    # Crear el archivo
    writer = csv.writer(response)
    # Definir encabezado de los campos
    writer.writerow(['ID', 'Contenido', 'Fecha Creación', 'Tarea', 'Autor'])

    # Escribir los datos en filas
    comentarios = Comentario.objects.all()
    for comentario in comentarios:
        writer.writerow([
            comentario.id,
            comentario.contenido,
            comentario.fecha_creacion,
            comentario.tarea.titulo,
            comentario.autor.nombre
        ])

    return response

def csvDocumentos(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Documentos.csv"'

    # Crear el archivo CSV
    writer = csv.writer(response)
    # Definir encabezado de los campos
    writer.writerow(['ID', 'Nombre', 'Descripción', 'Enlace', 'Tarea', 'Tipo', 'Fecha Creación','Autor'])

    # Escribir los datos en filas
    documentos = Documento.objects.all()
    for documento in documentos:
        writer.writerow([
            documento.id,
            documento.nombre,
            documento.descripcion,
            documento.enlace, 
            documento.tarea.titulo, 
            documento.tipo,
            documento.fecha_creacion,
            documento.autor.nombre
        ])

    return response
