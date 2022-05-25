from django import forms
from django.forms import ModelForm, MultipleChoiceField, ChoiceField, Form, SelectMultiple
from .models import user_profile
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class UserForm(UserCreationForm):
    username = forms.CharField( 
                                label='Usuario',
                                max_length=15, 
                                help_text=('Requerido. 15 caracteres o menos, letras, digitos y @/./+/-/_ solamente.'), 
                                validators=[username_validator], 
                                error_messages={'unique': ("Ya existe un usuario con ese nombre de Usuario.")}, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
                                label='Nombre(s)',
                                max_length=12, 
                                min_length=4, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
                                label = 'Apellidos',
                                max_length=12, 
                                min_length=4, 
                                required=True, 
                                widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(
                                label='Contraseña',
                                widget=(forms.PasswordInput(attrs={'class': 'form-control'})), 
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(
                                label = 'Confirmación de Contraseña', 
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}), 
                                help_text=('Vuelva a ingresar la contraseña para confirmar'))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)

class User_ProfileForm (forms.ModelForm):
    class Meta:
        model = user_profile
        bgColor = forms.MultipleChoiceField(widget=forms.Select(choices=user_profile.Colors) )
        txtColor= forms.MultipleChoiceField(widget=forms.Select(choices=user_profile.Colors) )
        bday = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
        # fields = '__all__'
        exclude = ['user']
        labels = {
                    'username':'Nombre Usuario (a mostrar)',
                    'bday':'Cumpleaños',
                    'description':'Biografía',
                    'regdate':'Fecha de Registro',
                    'profilepic':'Foto de Perfil',
                    'bgColor':'Color de Fondo',
                    'txtColor':'Color de Texto'}