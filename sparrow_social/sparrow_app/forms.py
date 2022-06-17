from dataclasses import fields
from tkinter.ttk import Widget
from django import forms
from django.forms import ModelForm, MultipleChoiceField, ChoiceField, Form, CheckboxSelectMultiple
from .models import message, user_profile
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
                                max_length=32, 
                                min_length=4, 
                                required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
                                label = 'Apellidos',
                                max_length=32, 
                                min_length=4, 
                                required=True, 
                                widget=(forms.TextInput(attrs={'class': 'form-control'})))
    email = forms.EmailField(label = 'Email',
                                max_length=50, 
                                min_length=10, 
                                required=True, 
                                widget=(forms.EmailInput(attrs={'class': 'form-control'}))
                                )                                
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
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2',)
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['first_name'].help_text = None
        self.fields['last_name'].help_text = None
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None



class User_ProfileForm (forms.ModelForm):
    class Meta:
        model = user_profile
        # bgColor = forms.MultipleChoiceField(widget=forms.Select(choices=user_profile.Colors) )
        # txtColor= forms.MultipleChoiceField(widget=forms.Select(choices=user_profile.Colors) )
        bday = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
        # fields = '__all__'
        exclude = ['user','regdate','bgColor','txtColor' ]
        labels = {
                    'watchname':'Nombre Usuario (a mostrar)',
                    'bday':'Cumpleaños (dd/mm/yyyy)',
                    'description':'Biografía',
                    'profilepic':'Foto de Perfil',
                    # 'bgColor':'Color de Fondo',
                    # 'txtColor':'Color de Texto'
                    }


class PostForm(forms.ModelForm):
    Text = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control w-100', 'id':'PostBox','rows':'3','placeholder':'¿Que estas haciendo?'}))
    class Meta:
        model = message
        fields=['Text']
        # exclude = ['Image','datepost','user_id']
        # labels = {'Text ':''}

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['Text'].help_text = None
        self.fields['Text'].required = False
        self.fields['Text'].label =None