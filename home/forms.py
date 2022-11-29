from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from home.models import Avatar
class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label="Nombre de usuario", min_length=3)
    email = forms.EmailField(label="Correo electrónico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

class UserUpdateForm(UserChangeForm):
    username = forms.CharField(label="Nombre de usuario", min_length=3)
    email = forms.EmailField(label="Correo electrónico")
    password = None


    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]
       
        widgets = {
            "email": forms.TextInput(attrs={"readonly": "readonly"}),
        }



class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("image", )



