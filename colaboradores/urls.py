from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:colaborador_id>', views.ver_colaborador, name='ver_colaborador'),
]
