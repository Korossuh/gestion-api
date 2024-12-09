from django import forms
from api.models import *

class personaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'input-nombre'
            }
        )
    )
    email= forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'input-email'
            }
        )
    )
    telefono = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'input-telefono'
            }
        )
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'input-fecha-nacimiento',
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Persona
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input-nombre'
            }
        )
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'input-descripcion'
            }
        )
    )
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'input-fecha'
            }
        )
    )
    fecha_fin = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'input-fecha'
            }
        )
    )
    persona_responsable = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'input-persona'
            }
        )
    )

    class Meta:
        model = Proyecto
        fields = '__all__'

class TareaForm(forms.ModelForm):
    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input-titulo'
            }
        )
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'input-descripcion'
            }
        )
    )
    estado = forms.ChoiceField(
        choices=Tarea.estado.field.choices,
        widget=forms.Select(
            attrs={
                'class': 'input-estado'
            }
        )
    )
    proyecto = forms.ModelChoiceField(
        queryset=Proyecto.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'input-proyecto'
            }
        )
    )
    asignado_a = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'input-asignado'
            }
        )
    )

    class Meta:
        model = Tarea
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    contenido = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'input-contenido'
            }
        )
    )
    tarea = forms.ModelChoiceField(
        queryset=Tarea.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'input-tarea'
            }
        )
    )
    autor = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'input-autor'
            }
        )
    )

    class Meta:
        model = Comentario
        fields = '__all__'

class DocumentoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'input-nombre'
            }
        )
    )
    descripcion = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'input-descripcion'
            }
        )
    )
    enlace = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                'class': 'input-enlace'
            }
        )
    )
    tarea = forms.ModelChoiceField(
        queryset=Tarea.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'input-tarea'
            }
        )
    )
    tipo = forms.ChoiceField(
        choices=Documento.tipo.field.choices,
        widget=forms.Select(
            attrs={
                'class': 'input-tipo'
            }
        )
    )
    autor = forms.ModelChoiceField(
        queryset=Persona.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'input-autor'
            }
        )
    )

    class Meta:
        model = Documento
        fields = '__all__'
