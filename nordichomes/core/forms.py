from django import forms # Importa o módulo de formulários do Django
from django.contrib.auth.forms import UserCreationForm # Importa a classe UserCreationForm do módulo de formulários de autenticação do Django
from django.contrib.auth.models import User # Importa a classe User do modelo de autenticação do Django

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']