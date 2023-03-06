from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='colaboradores'),
    path('busca/', views.busca, name='busca'),
    path('<int:colaborador_id>', views.ver_colaborador, name='ver_colaborador'),
]
