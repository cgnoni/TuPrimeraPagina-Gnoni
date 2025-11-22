from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo
