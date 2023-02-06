from django.shortcuts import render
from .models import Colaborador


def index(request):
    colaboradores = Colaborador.objects.all()

    return render(request, 'colaboradores/index.html', {
        'colaboradores': colaboradores
    })

