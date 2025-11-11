from django import forms
from .models import Receta

class FormularioReceta(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ["titulo", "ingredientes", "instrucciones"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título de la receta"}),
            "ingredientes": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Ingredientes"}),
            "instrucciones": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Instrucciones paso a paso"}),
        }

