from django.contrib import admin
from . models import Setor, Colaborador


class ColaboradorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_completo',
        'cargo',
        'setor',
        'ramal',
        'email',
        'situacao',)
    list_display_links = (
        'id',
        'nome_completo')
    list_filter = (
        'setor', )
    list_editable = (
        'situacao', )
    search_fields = (
        'nome_completo',
        'setor',
        'ramal',
        'email',
        'aniversario')


class SetorAdmin(admin.ModelAdmin):
    list_display = ('id', 'setor')


admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Setor, SetorAdmin)


