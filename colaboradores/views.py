from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Colaborador


def index(request):
    colaboradores = Colaborador.objects.order_by('nome_completo').filter(
        situacao=True
    )

    return render(request, 'colaboradores/index.html', {
        'colaboradores': colaboradores
    })


def ver_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)

    if not colaborador.situacao:
        raise Http404

    return render(request, 'colaboradores/ver_colaborador.html', {
        'colaborador': colaborador
    })

