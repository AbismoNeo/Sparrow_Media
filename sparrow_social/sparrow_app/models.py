from django.db import models
from django.forms import CharField, DateField
from django.utils import timezone
# Create your models here.

# Modelo Sparrow
# Clase usuario con los datos del usuario
class users(models.Model):
    fullname = models.CharField(verbose_name = "Nombre Completo",max_length = 100)
    bday = models.DateField(verbose_name = "Fecha de Nacimiento")
    username = models.CharField(verbose_name = "Usuario", max_length = 20)
    password = models.CharField(verbose_name = "Contraseña", max_length = 15)
    email = models.EmailField(verbose_name = "Correo Electronico")
    description  = models.TextField (verbose_name="Descripcion")
    regdate = models.DateTimeField(default = timezone.now, verbose_name="Fecha de Registro" )
    profilepic = models.ImageField(verbose_name="Imagen de perfil")
    bgColor = models.CharField(verbose_name = "Color de Fondo", max_length = 15)
    txtColor = models.CharField(verbose_name = "Color de Texto", max_length= 15)
    
    def __str__(self):
        return f'Perfil de {self.username}'
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    

#Clase message con los datos de los post
class message(models.Model):
    datepost = models.DateTimeField(default = timezone.now, verbose_name = "Fecha de posteo")
    user_id = models.ForeignKey(users, on_delete=models.CASCADE, verbose_name="ID de usuario")
    Text = models.TextField(max_length=150, verbose_name = "Mensaje")
    Image = models.ImageField(verbose_name="Imagen")

    class Meta:   
        ordering = ['-datepost']
        verbose_name_plural = 'Mensajes'
        verbose_name = 'Mensaje'

    def __str__(self):
        return self.Text

# Clase list_follow con los datos de lista de followers
class list_follow(models.Model):
    id_list = models.ForeignKey(users,related_name="Seguidor", on_delete=models.CASCADE, verbose_name="Id de Usuario")
    id_friend = models.ForeignKey(users, related_name="Siguiendo", on_delete=models.CASCADE, verbose_name="Id de Seguidor")
    follow_date = models.DateTimeField(verbose_name="Fecha de seguimiento")

    def __str__(self):
        
        return self.id_f
    
    class Meta:
        verbose_name = 'Lista de Seguidores'
        verbose_name_plural = 'Listas de Seguidores'