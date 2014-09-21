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
    pass

class Persona(TimeStampModel):
    pass

class Pregunta(TimeStampModel):
    catalogo = models.ForeignKey(Catalogo)
    persona = models.ManyToManyField(Persona)


class Respuesta(TimeStampModel):
    pregunta = models.ForeignKey(Pregunta)