from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    fields = ['user','nome', 'cpf', 'rg', 'matricula', 'sexo', 'email', 'status', 'data_nasc',
              'grupo_usuario']
    list_filter = ['sexo', 'status', 'data_nasc', 'grupo_usuario']
    search_fields = ['nome', 'email']
    list_display = ['nome', 'email', 'sexo', 'status', 'data_nasc', 'grupo_usuario']
    exclude = ["login", "senha"]


admin.site.register(Usuario, UsuarioAdmin)

