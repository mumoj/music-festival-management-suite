from django.contrib import admin
from .models import (
    Institution, Class,
    Performance, Theater,
    Event, Locality)

# Register your models here.
admin.site.register(Institution)
admin.site.register(Class)
admin.site.register(Performance)
admin.site.register(Theater)
admin.site.register(Event)
admin.site.register(Locality)
