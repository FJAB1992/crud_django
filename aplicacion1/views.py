from django.shortcuts import render

from . import models
# Create your views here.

def vista1(request):
    #Viene del modelo Test creado
    usuarios = models.Test.objects.all()
    nombre = "Francisco Javier Aranda Barba"
    contexto = {}
    contexto['nombre']=nombre
    contexto["usuarios"]=usuarios
    #Los campos del diccionario si tendré que tenerlos en cuenta para
    #utilizarlos en el template de la basededatos.html
    return render(request,'basedatos.html',contexto)