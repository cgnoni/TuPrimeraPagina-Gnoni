from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import FormularioReceta, BuscarReceta 


def inicio(request):
    return render(request, "recetas/inicio.html")


def lista_recetas(request):
    formulario = BuscarReceta(request.GET or None)
    recetas = Receta.objects.all()

    if formulario.is_valid():
        titulo = formulario.cleaned_data.get("titulo")
        if titulo: 
            recetas = recetas.filter(titulo__icontains=titulo)

    return render(
        request,
        "recetas/lista_recetas.html",
        {"formulario": formulario, "recetas": recetas},
    )


def nueva_receta(request):
    if request.method == "POST":
        form = FormularioReceta(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_recetas")
    else:
        form = FormularioReceta()
    return render(request, "recetas/nueva_receta.html", {"form": form})


def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect("lista_recetas")
