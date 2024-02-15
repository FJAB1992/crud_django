from django.contrib import admin
from . import models

# Register your models here.


# Clase de configuración del modelo
class TestAdmin(admin.ModelAdmin):
    #Mostrar lista con parámetros
    list_display = ["nombre", "apellido1", "apellido2"]
    #otra forma,Puedo mostrar lo que mencione y en el orden que quiera
    # list_display = ["apellido2","nombre", "apellido1"]

    #barra de buscador, con los parámetros que se quiera
    search_fields = ["id","nombre","apellido1"]
    #Mostrar filtro
    list_filter = ["nombre","apellido1"]

# Registrar modelo
admin.site.register(models.Test, TestAdmin)


# #Opción2 (si no hay clase de administración)
# @admin.register(models.Test)
# class TestAdmin(admin.ModelAdmin):
#     x=0

