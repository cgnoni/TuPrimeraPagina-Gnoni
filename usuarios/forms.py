from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Perfil

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["imagen", "bio"]
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'initial_text': '', 'input_text': 'Seleccionar archivo', 'clear_checkbox_label': ''}),
        }

class LoginForm(AuthenticationForm):
    pass

