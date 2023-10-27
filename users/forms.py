from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите имя пользователя",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль",
    }))

    class Meta:
        model = CustomUser
        fields = ('username', 'password')