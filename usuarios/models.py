from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="perfiles", blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("usuarios:perfil_detalle", kwargs={"pk": self.pk})
