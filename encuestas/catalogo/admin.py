from django.contrib import admin
from .models import Catalogo, Persona, Pregunta, Respuesta, Seleccion, Carrera

# Register your models here.

admin.site.register(Catalogo)
admin.site.register(Persona)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Seleccion)
admin.site.register(Carrera)
