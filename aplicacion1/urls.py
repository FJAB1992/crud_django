from django.urls import path
from . import views

app_name='aplicacion1'

urlpatterns = [
    path('',views.vista1),
    path('basedatos/', views.vista1),
]