from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy 
from .forms import RegistroForm, LoginForm, PerfilForm
from .models import Perfil


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        perfil_form = PerfilForm(request.POST, request.FILES)

        if form.is_valid() and perfil_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()

            return redirect("usuarios:login")
    else:
        form = RegistroForm()
        perfil_form = PerfilForm()

    return render(request, "usuarios/registro.html", {"form": form, "perfil_form": perfil_form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("main:inicio")
    else:
        form = LoginForm()

    return render(request, "usuarios/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main:inicio")


@login_required
def perfil(request):
    perfil_usuario = Perfil.objects.get_or_create(user=request.user)[0]

    if request.method == "POST":
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_usuario)
        if perfil_form.is_valid():
            perfil_form.save()
            return redirect("usuarios:perfil")
    else:
        perfil_form = PerfilForm(instance=perfil_usuario)

    return render(request, "usuarios/perfil.html", {"perfil": perfil_usuario, "perfil_form": perfil_form})

class PerfilDetalleView(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = "usuarios/perfil_detalle.html"
    context_object_name = "perfil"

class PerfilActualizarView(LoginRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = "usuarios/perfil_editar.html"
    success_url = reverse_lazy("usuarios:perfil")

    def get_object(self):
        return self.request.user.perfil
