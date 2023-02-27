from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Colaborador
from django.db.models import Q
from django.contrib import messages


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


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(request, messages.WARNING, 'O campo de pesquisa não pode estar vazio para consulta.')
        return redirect('index')

    colaboradores = Colaborador.objects.order_by('nome_completo').filter(
        Q(nome_completo__icontains=termo)
    )

    return render(request, 'colaboradores/busca.html', {
        'colaboradores': colaboradores
    })
