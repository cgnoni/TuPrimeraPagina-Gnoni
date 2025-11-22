from django.urls import path
from . import views
from django.conf.urls.static import static


app_name = "usuarios"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registro/", views.registro, name="registro"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/<int:pk>/", views.PerfilDetalleView.as_view(), name="perfil_detalle"),
    path("perfil/<int:pk>/editar/", views.PerfilActualizarView.as_view(), name="perfil_editar"),
]

