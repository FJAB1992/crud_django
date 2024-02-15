from django.shortcuts import render

from . import models
from . import forms

# Create your views here.

from django.views import generic


def ejemplo(request):
    return render(request, "ejemplo.html", {})


def vista1(request):
    # Viene del modelo Test creado
    contexto = {}
    usuarios = models.Test.objects.all()
    nombre = "Francisco Javier Aranda Barba"
    contexto["nombre"] = nombre
    contexto["usuarios"] = usuarios
    # Los campos del diccionario si tendré que tenerlos en cuenta para
    # utilizarlos en el template de la basededatos.html
    return render(request, "basedatos.html", contexto)


# Creamos la vista para la Lista
class ListadoView(generic.ListView):
    model = models.Test
    # Por defecto Django usa test_list, esta la creamos
    template_name = "listado.html"


class DetalleView(generic.DetailView):
    model = models.Test
    template_name = "detalle.html"
    # Se puede dar un nombre al contexto del objeto de la siguiente forma
    # context_object_name = "datos"


class NuevoView(generic.CreateView):
    model = models.Test
    # Si se menciona un formulario con dichos campos, creará conflicto
    # fields = ["nombre","apellido1","apellido2"]
    form_class = forms.PersonaForm
    template_name = "nuevo.html"
    success_url = "/aplicacion1/listado/"


class ActualizarView(generic.UpdateView):
    model = models.Test
    fields = ["nombre", "apellido1", "apellido2"]
    template_name = "actualizar.html"
    success_url = "/aplicacion1/listado/"


class BorrarView(generic.DeleteView):
    model = models.Test
    fields = ["nombre", "apellido1", "apellido2"]
    template_name = "borrar.html"
    success_url = "/aplicacion1/listado/"

    def get_context_data(self, **kwargs):
        contexto = super(BorrarView, self).get_context_data(**kwargs)
        contexto["saludo"] = "HOLA A TODOS"
        contexto["personas"] = models.Test.objects.all()
        return contexto
