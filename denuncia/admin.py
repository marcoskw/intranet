from django.contrib import admin
from . models import Denuncia


class DenunciaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao',
                    'nome_completo',
                    'setor_ocorrido',
                    'setor_colaborador',
                    'tipo_denuncia',
                    'conhecimento')


admin.site.register(Denuncia, DenunciaAdmin)
