# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.db import models

# Importamos el modelo
from apps.adopcion.models import Persona

# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    
    # Relacion Unos a Varios
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    
    # Relacion de Muchos es a Muchos
    vacuna = models.ManyToManyField(Vacuna, blank=True)
