from sgfd.login.models import  Usuario
from django.contrib import admin
from django.contrib.auth.models import User

admin.site.unregister(User)

class UsuarioInline(admin.StackedInline):
    model = Usuario
    max_num = 1

class UsuarioAdmin(admin.ModelAdmin):
    inlines = [UsuarioInline, ]
    
admin.site.register(User, UsuarioAdmin)
