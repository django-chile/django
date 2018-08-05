# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.contrib import admin

# Register your models here.

from apps.mascota.models import Vacuna, Mascota 

# Register your models here.
admin.site.register(Vacuna)
admin.site.register(Mascota)

