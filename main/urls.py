from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("acerca-de-mi/", views.AcercaDeMiView.as_view(), name="acerca_de_mi"),
]