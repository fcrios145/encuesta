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