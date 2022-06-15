from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateField, ModelForm
from django.utils import timezone
# Create your models here.

# Modelo Sparrow
# Clase usuario con los datos del usuario
class user_profile(models.Model):
    Colors=(("NEGRO", "Negro"), ("BLANCO", "Blanco"), ("GRIS","Gris"))
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(verbose_name = "Nombre a Mostrar", max_length= 15)
    bday = models.DateField(verbose_name = "Fecha de Nacimiento")
    description  = models.TextField (verbose_name="Descripcion")
    regdate = models.DateTimeField(default = timezone.now, verbose_name="Fecha de Registro" )
    profilepic = models.ImageField(upload_to='media/profiles/', verbose_name="Imagen de perfil", blank =True, null = True)
    bgColor = models.CharField(verbose_name = "Color de Fondo", max_length = 15, choices=Colors, default="Blanco")
    txtColor = models.CharField(verbose_name = "Color de Texto", max_length= 15, choices=Colors, default = "Negro")
    
    def __str__(self):
        return f'Perfil de {self.username}'
    
    class Meta:
    
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

#Clase message con los datos de los post
class message(models.Model):
    datepost = models.DateTimeField(default = timezone.now, verbose_name = "Fecha de posteo")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")
    Text = models.TextField(max_length=150, verbose_name = "Mensaje")
    Image = models.ImageField(verbose_name="Imagen", blank =True, null = True )

    class Meta:   
        ordering = ['-datepost']
        verbose_name_plural = 'Mensajes'
        verbose_name = 'Mensaje'

    def __str__(self):
        return self.Text

# Clase list_follow con los datos de lista de followers
class list_follow(models.Model):
    id_list = models.ForeignKey(User,related_name="Seguidor", on_delete=models.CASCADE, verbose_name="Id de Usuario")
    id_friend = models.ForeignKey(User, related_name="Siguiendo", on_delete=models.CASCADE, verbose_name="Id de Seguidor")
    follow_date = models.DateTimeField(verbose_name="Fecha de seguimiento")

    def __str__(self):
        
        return self.id_f
    
    class Meta:
        verbose_name = 'Lista de Seguidores'
        verbose_name_plural = 'Listas de Seguidores'