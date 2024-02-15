from django.urls import path
from . import views

app_name = "aplicacion1"

urlpatterns = [
    path("", views.vista1),
    path("ejemplo/", views.ejemplo, name="ejemplo"),
    path("basedatos/", views.vista1, name="basedatos"),
    # Le indico que quiero usar la vista creada para el listado
    # as_view() habrá que añadirlo cuando es una clase y no una función
    path("listado/", views.ListadoView.as_view(), name="listado"),
    path("detalle/<int:pk>/", views.DetalleView.as_view(), name="detalle"),
    path("nuevo/", views.NuevoView.as_view(), name="nuevo"),
    path("actualizar/<int:pk>/", views.ActualizarView.as_view(), name="actualizar"),
    path("borrar/<int:pk>/", views.BorrarView.as_view(), name="borrar"),
]
