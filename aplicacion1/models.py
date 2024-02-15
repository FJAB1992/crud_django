from django.db import models

# Create your models here.


# Clase que representa una tabla en bbdd, el nombre es indiferente
class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50, verbose_name="Primer apellido")
    apellido2 = models.CharField(
        max_length=50, verbose_name="Segundo apellido", blank=True, null=True
    )

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        db_table = "usuario"

    # Definicion de "Método toString" típico
    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"