from django.contrib import admin
from .models import user_profile,message,list_follow

# Register your models here.

admin.site.register(user_profile)
admin.site.register(message)
admin.site.register(list_follow)
