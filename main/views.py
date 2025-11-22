from django.shortcuts import render
from django.views.generic import TemplateView


def inicio(request):
    return render(request, "main/inicio.html")

class AcercaDeMiView(TemplateView):
    template_name = "main/acerca_de_mi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = "Camila Ayelén Gnoni"
        context['profesion'] = "Bibliotecaria / UX Designer"
        return context
