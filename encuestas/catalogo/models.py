#core/models.py
from django.db import models


class TimeStampModel(models.Model):
    """
    clase base abstracta que actualiza de manera automatica los campos created y modified
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Catalogo(TimeStampModel):
    nombre = models.CharField(max_length=256, blank=False, default="")

    def __unicode__(self):
        return self.nombre

class Persona(TimeStampModel):
    pass

class Pregunta(TimeStampModel):
    texto = models.TextField(max_length=512, blank=False, default="")
    catalogo = models.ForeignKey(Catalogo)
    imagen = models.ImageField(upload_to='preguntas')
    persona = models.ManyToManyField(Persona)

    def __unicode__(self):
        return self.texto


class Respuesta(TimeStampModel):
    texto = models.TextField(max_length=512, blank=False, default="")
    imagen = models.ImageField(upload_to='respuestas')
    pregunta = models.ForeignKey(Pregunta)

    def __unicode__(self):
        return self.texto