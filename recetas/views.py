from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import FormularioReceta as RecetaForm


def inicio(request):
    return render(request, "recetas/inicio.html")


def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, "recetas/lista_recetas.html", {"recetas": recetas})


def nueva_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_recetas")
    else:
        form = RecetaForm()
    return render(request, "recetas/nueva_receta.html", {"form": form})


def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect("lista_recetas")
