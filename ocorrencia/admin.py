from django.contrib import admin
from .models import Categoria, Ocorrencia
from .filters import SemestreFilter, PeriodoFilter


class OcorrenciaAdmin(admin.ModelAdmin):
    fields = ['longitude', 'latitude', 'data', 'hora', 'descricao', 'validade', 'atendida', 'emergencia', 'vitimado',
              'repetida', 'resposta', 'usuario_ID', 'vigilante_ID',
              'tb_categoria_ID']
    list_filter = ['tb_categoria_ID', SemestreFilter, PeriodoFilter, 'atendida', 'vitimado']
    search_fields = ['usuario_ID', 'data', 'hora', 'vigilante_ID']
    list_display = ['data', 'hora', 'usuario_ID', 'vigilante_ID', 'atendida', 'emergencia', 'vitimado', 'tb_categoria_ID']


class CategoriaAdmin(admin.ModelAdmin):
    fields = ['descricao']
    search_fields = ['descricao']
    list_display = ['descricao']


admin.site.register(Ocorrencia, OcorrenciaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
