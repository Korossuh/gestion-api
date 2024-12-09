from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import * 
from .forms import*
import csv

#Funcion para index
@login_required
def index (request):
    return render(request,'index.html')

#Funcion para csv
@login_required
def csvView(request):
    return render(request,'csv.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html') 

def crudView(request):
    return render(request, 'crud.html')

#=================================================
#======== FUNCIONES PARA CRUD PERSONAS ===========
#=================================================
@login_required
def personasView(request):
    query = request.GET.get('q', '')
    if query:
        personas = Persona.objects.filter(nombre__icontains=query) 
    else:
        personas = Persona.objects.all() 

    return render(request, 'crud/persona.html', {'personas': personas, 'query': query})

@login_required
def personaAdd(request):
    if request.method == 'POST':
        form= personaForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personasView")
    else:
        form =personaForm()
    return render(request, 'crud/formpersona.html',{'form':form})

@login_required
def personaMod(request, id):
    persona = Persona.objects.get(pk = id)

    if request.method == 'POST':
        form= personaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect("personasView")
    else:
        form =personaForm(instance=persona)
    return render(request, 'crud/formpersona.html',{'form':form})

@login_required
def personaDel(request, id):
    persona = Persona.objects.get(pk = id)
    persona.delete()
    return redirect("personasView")

#==================================================
#======== FUNCIONES PARA CRUD PROYECTOS ===========
#==================================================

@login_required
def proyectosView(request):
    query = request.GET.get('q', '')
    if query:
        proyectos = Proyecto.objects.filter(nombre__icontains=query)
    else:
        proyectos = Proyecto.objects.all()

    return render(request, 'crud/proyecto.html', {'proyectos': proyectos, 'query': query})

@login_required
def proyectoAdd(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("proyectosView")
    else:
        form = ProyectoForm()
    return render(request, 'crud/formproyecto.html', {'form': form})

@login_required
def proyectoMod(request, id):
    proyecto = Proyecto.objects.get(pk=id)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect("proyectosView")
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'crud/formproyecto.html', {'form': form})

@login_required
def proyectoDel(request, id):
    proyecto = Proyecto.objects.get(pk=id)
    proyecto.delete()
    return redirect("proyectosView")

#================================================
#======== FUNCIONES PARA CRUD TAREA =============
#================================================

@login_required
def tareasView(request):
    query = request.GET.get('q', '')
    if query:
        tareas = Tarea.objects.filter(titulo__icontains=query)
    else:
        tareas = Tarea.objects.all()

    return render(request, 'crud/tarea.html', {'tareas': tareas, 'query': query})

@login_required
def tareaAdd(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tareasView")
    else:
        form = TareaForm()
    return render(request, 'crud/formtarea.html', {'form': form})

@login_required
def tareaMod(request, id):
    tarea = Tarea.objects.get(pk=id)

    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("tareasView")
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'crud/formtarea.html', {'form': form})

@login_required
def tareaDel(request, id):
    tarea = Tarea.objects.get(pk=id)
    tarea.delete()
    return redirect("tareasView")

#===================================================
#======== FUNCIONES PARA CRUD COMENTARIOS ==========
#===================================================

@login_required
def comentariosView(request):
    query = request.GET.get('q', '')
    if query:
        comentarios = Comentario.objects.filter(contenido__icontains=query)
    else:
        comentarios = Comentario.objects.all()

    return render(request, 'crud/comentario.html', {'comentarios': comentarios, 'query': query})

@login_required
def comentarioAdd(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comentariosView")
    else:
        form = ComentarioForm()
    return render(request, 'crud/formcomentario.html', {'form': form})

@login_required
def comentarioMod(request, id):
    comentario = Comentario.objects.get(pk=id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect("comentariosView")
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'crud/formcomentario.html', {'form': form})

@login_required
def comentarioDel(request, id):
    comentario = Comentario.objects.get(pk=id)
    comentario.delete()
    return redirect("comentariosView")

#===================================================
#======== FUNCIONES PARA CRUD DOCUMENTOS ===========
#===================================================

@login_required
def documentosView(request):
    query = request.GET.get('q', '')
    if query:
        documentos = Documento.objects.filter(nombre__icontains=query)
    else:
        documentos = Documento.objects.all()

    return render(request, 'crud/documento.html', {'documentos': documentos, 'query': query})

@login_required
def documentoAdd(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("documentosView")
    else:
        form = DocumentoForm()
    return render(request, 'crud/formdocumento.html', {'form': form})

@login_required
def documentoMod(request, id):
    documento = Documento.objects.get(pk=id)

    if request.method == 'POST':
        form = DocumentoForm(request.POST, instance=documento)
        if form.is_valid():
            form.save()
            return redirect("documentosView")
    else:
        form = DocumentoForm(instance=documento)
    return render(request, 'crud/formdocumento.html', {'form': form})

@login_required
def documentoDel(request, id):
    documento = Documento.objects.get(pk=id)
    documento.delete()
    return redirect("documentosView")


#=================================================
#======== FUNCIONES PARA DESCARGAR CSV ===========
#=================================================
@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
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
