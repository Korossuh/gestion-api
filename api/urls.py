from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, ProyectoViewSet,TareaViewSet,ComentarioViewSet,ArchivoViewSet
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'personas', PersonaViewSet, basename='personas')
router.register(r'proyectos', ProyectoViewSet, basename='proyectos')
router.register(r'tareas',TareaViewSet, basename='tareas')
router.register(r'comentarios',ComentarioViewSet, basename='comentarios')
router.register(r'archivos', ArchivoViewSet,basename='archivos')

urlpatterns = [
    path("api/",include(router.urls),name='api')
]
