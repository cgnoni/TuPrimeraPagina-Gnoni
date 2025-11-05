from django.db import models


class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()

    def __str__(self):
        return self.titulo
