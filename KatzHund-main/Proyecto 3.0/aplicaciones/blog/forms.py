from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import Post, Comment

class NewRegister(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class":"u-border-1 u-border-white u-input u-input-rectangle u-radius-50 u-white", "placeholder": "Ingresa nombre de usuario"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "u-border-1 u-border-white u-input u-input-rectangle u-radius-50 u-white", "placeholder": "Ingresa mail"}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"class": "u-border-1 u-border-white u-input u-input-rectangle u-radius-50 u-white", "placeholder": "Ingresa contraseña"}))
    password2 = forms.CharField(label='Repita Cotraseña', widget=PasswordInput(attrs={"class": "u-border-1 u-border-white u-input u-input-rectangle u-radius-50 u-white", "placeholder": "Repita contraseña"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(attrs={"class":"u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", "placeholder":"Ingresa nombre de usuario"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"u-border-2 u-border-black u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", "placeholder":"Ingresa contraseña"}))

class post_form(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["fecha_creacion"]

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["fecha_creacion"]