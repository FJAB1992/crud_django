from django import forms
from . import models

class PersonaForm(forms.ModelForm):

    class Meta:
        # Asociamos al formulario del modelo Test (en models, lo llamamos así)
        model = models.Test
        fields = [
            "nombre",
            "apellido1",
            "apellido2"
        ]  # "__all__" ; en caso de que quiera traerme todos los campos

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido1": forms.TextInput(attrs={"class": "form-control"}),
            "apellido2": forms.TextInput(attrs={"class": "form-control"}),
        }
