from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("lista/", views.lista_recetas, name="lista_recetas"),
    path("nueva/", views.nueva_receta, name="nueva_receta"),
    path("eliminar/<int:id>/", views.eliminar_receta, name="eliminar_receta"),
]
