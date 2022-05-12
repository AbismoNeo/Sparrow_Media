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
    regdate = models.DateTimeField(default = timezone.now )
    profilepic = models.ImageField()
    bgColor = models.CharField(verbose_name = "Color de Fondo", max_length = 15)
    txtColor = models.CharField(verbose_name = "Color de Texto", max_length= 15)
    
    def __str__(self):
        return f'Perfil de {self.username}'
    

#Clase message con los datos de los post
class message(models.Model):
    datepost = models.DateTimeField(default = timezone.now)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    Text = models.TextField(max_length=150, verbose_name = "Mensaje")
    Image = models.ImageField()

    class Meta:   
        ordering = ['-datepost']

    def __str__(self):
        return self.Text

# Clase list_follow con los datos de lista de followers
class list_follow(models.Model):
    id_list = models.ForeignKey(users, on_delete=models.CASCADE)
    id_friend = models.CharField(max_length=20)
    follow_date = models.DateTimeField()

    def __str__(self):
        return self.id_friend