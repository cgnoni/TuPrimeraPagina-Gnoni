from django.urls import path
from . import views
from .views import DetalleRecetaView, EditarRecetaView, EliminarRecetaView

app_name = "recetas"

urlpatterns = [
    path("lista/", views.lista_recetas, name="lista_recetas"),
    path("nueva/", views.nueva_receta, name="nueva_receta"),
    path("detalle/<int:pk>/", DetalleRecetaView.as_view(), name="detalle_receta"),
    path("editar/<int:pk>/", EditarRecetaView.as_view(), name="editar_receta"),
    path("eliminar/<int:pk>/", EliminarRecetaView.as_view(), name="eliminar_receta"),
]
