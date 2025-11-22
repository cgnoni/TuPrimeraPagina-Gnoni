from django.shortcuts import render, redirect
from .models import Receta
from .forms import FormularioReceta, BuscarReceta 
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def lista_recetas(request):
    formulario = BuscarReceta(request.GET)

    if formulario.is_valid():
        titulo = formulario.cleaned_data.get("titulo")

        if titulo:
            listado_de_recetas = Receta.objects.filter(titulo__icontains=titulo)
        else:
            listado_de_recetas = Receta.objects.all()
    else:
        listado_de_recetas = Receta.objects.all()

    return render(request, "recetas/lista_recetas.html", {
        "listado_de_recetas": listado_de_recetas,
        "formulario": formulario
    })

@login_required
def nueva_receta(request):
    if request.method == "POST":
        form = FormularioReceta(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recetas:lista_recetas")
    else:
        form = FormularioReceta()
    return render(request, "recetas/nueva_receta.html", {"form": form})


class DetalleRecetaView(DetailView):
    model = Receta
    template_name = "recetas/detalle_receta.html"
    context_object_name = "receta"


class EditarRecetaView(LoginRequiredMixin, UpdateView):
    model = Receta
    template_name = "recetas/editar_receta.html"
    fields = ["titulo", "ingredientes", "instrucciones"]
    success_url = reverse_lazy("recetas:lista_recetas")

class EliminarRecetaView(LoginRequiredMixin, DeleteView):
    model = Receta
    template_name = "recetas/eliminar_receta.html"
    success_url = reverse_lazy("recetas:lista_recetas")