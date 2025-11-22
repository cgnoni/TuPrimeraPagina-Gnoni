from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("recetas/", include("recetas.urls")),
    path("usuarios/", include("usuarios.urls")),
    path("cuentas/login/", auth_views.LoginView.as_view(), name="login_default")
]