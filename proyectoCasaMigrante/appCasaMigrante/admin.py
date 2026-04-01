from django.contrib import admin
from .models import *


# Register your models here.

class RegistroMigranteAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "no_identificacion", "genero", "fecha_nacimiento", "nacionalidad", "fecha_ingreso", "fecha_salida")
    list_filter = ("fecha_ingreso",)

class RegistroColaboradorAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "telefono", "estado_disponible", "dias_disponible",)
    list_filter = ("estado_disponible" ,"dias_disponible",)

class RegistroActividadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "fecha", "colab_responsable",)

class EstadoDisponibleAdmin(admin.ModelAdmin):
    list_display = ("estado_disponible",)

class DiasDiponibleAdmin(admin.ModelAdmin):
    list_display = ("dias_disponible",)


admin.site.register(RegistroMigrante, RegistroMigranteAdmin)
admin.site.register(RegistroColaborador, RegistroColaboradorAdmin)
admin.site.register(RegistroActividad, RegistroActividadAdmin)
admin.site.register(EstadoDisponible, EstadoDisponibleAdmin)
admin.site.register(DiasDisponible, DiasDiponibleAdmin)

