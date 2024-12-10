from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    persona_responsable = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='proyectos')

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=[('PENDIENTE', 'Pendiente'), ('EN PROGRESO', 'En Progreso'), ('COMPLETADA', 'Completada')]
    )
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    asignado_a = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tareas_asignadas')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f"Comentario de {self.autor} en {self.tarea}"

class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    enlace = models.URLField(blank=True, null=True)
    tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE, related_name='documentos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, choices=[('DOCUMENTO', 'Documento'), ('ENLACE', 'Enlace')], default='DOCUMENTO')
    autor = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='documentos')


    def __str__(self):
        return self.nombre