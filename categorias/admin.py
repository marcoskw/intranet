from django.contrib import admin

from categorias.models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    list_display_links = ('id', )


admin.site.register(Categoria, CategoriaAdmin)
