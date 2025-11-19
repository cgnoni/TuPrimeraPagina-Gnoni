import os
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares/", default="avatares/default.png")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

    def save(self, *args, **kwargs):
        try:
            old = Perfil.objects.get(pk=self.pk).imagen
        except Perfil.DoesNotExist:
            old = None

        super().save(*args, **kwargs)

        if old and old != self.imagen and old.name != "avatares/default.png":
            if os.path.isfile(old.path):
                os.remove(old.path)