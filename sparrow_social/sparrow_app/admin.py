from django.contrib import admin
from .models import users,message,list_follow

# Register your models here.

admin.site.register(users)
admin.site.register(message)
admin.site.register(list_follow)
