from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Portfolio


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'id': 'unamef',
            'name': 'username',
            'placeholder': 'Usuario',
            'class': 'input input-bordered'
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'id': 'upwf',
            'placeholder': 'Contraseña',
            'class': 'input input-bordered'
        })
    )

    class Meta:
        model = User
        fields = ("username", "password")

    error_messages = {
        'username': {
            'required': 'El campo usuario es requerido',
            'invalid': 'El campo usuario no es valido',
        },
        'password': {
            'required': 'El campo contraseña es requerido',
            'invalid': 'El campo contraseña no es valido',
        },
        'invalid_login': 'Usuario o contraseña incorrecta'
    }


class PortfolioForm(forms.ModelForm):

    title = forms.CharField(
        max_length=100,
        label="Titulo",
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'pint',
            'name': 'title',
            'placeholder': 'Titulo',
            'class': 'input input-bordered'
        })
    )
    description = forms.CharField(
        max_length=200,
        label="Descripción",
        required=True,
        widget=forms.Textarea(attrs={
            'id': 'pindes',
            'name': 'description',
            'class': 'input input-bordered'
        })
    )
    tags = forms.CharField(
        max_length=100,
        label="Tags",
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'pintags',
            'name': 'tags',
            'placeholder': 'Ejemplo HTML, CSS, PYTHON',
            'class': 'input input-bordered'
        })
    )
    image = forms.URLField(
        max_length=100,
        label="Imagen",
        required=True,
        widget=forms.URLInput(attrs={
            'id': 'pinimage',
            'name': 'image',
            'placeholder': 'Ingrese una url de imagen',
            'class': 'input input-bordered'
        })
    )
    urlgithub = forms.CharField(
        max_length=100,
        label="Url de github",
        required=True,
        widget=forms.URLInput(attrs={
            'id': 'pingit',
            'name': 'github',
            'placeholder': 'Ingrese una url de github',
            'class': 'input input-bordered'
        })
    )

    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'tags', 'image', 'urlgithub']

    error_messages = {
        'title': {
            'required': 'El campo título es requerido',
            'invalid': 'El campo título no es valido',
        },
        'description': {
            'required': 'El campo descripción es requerido',
            'invalid': 'El campo descripción no es valido',
        },
        'tags': {
            'required': 'Ingrese algunos tags',
            'invalid': 'Los tags ingresados no son validos',
        },
        'image': {
            'required': 'El campo imagen es requerido',
            'invalid': 'El campo imagen no es valido',
        },
        'urlgithub': {
            'required': 'El campo github es requerido',
            'invalid': 'El campo github no es valido',
        }
    }
