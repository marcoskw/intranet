from dataclasses import dataclass
from django.contrib import messages
from denuncia.models import Denuncia
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    if request.method != 'POST':
        return render(request, 'denuncia/index.html')

    data_criacao = request.POST.get('data_criacao')
    nome_completo = request.POST.get('nome_completo')
    setor_colaborador = request.POST.get('setor_colaborador')
    tipo_denuncia = request.POST.get('tipo_denuncia')
    local_ocorrido = request.POST.get('local_ocorrido')
    setor_ocorrido = request.POST.get('setor_ocorrido')
    conhecimento = request.POST.get('conhecimento')
    vinculo_superior = request.POST.get('vinculo_superior')
    corpo_denuncia = request.POST.get('corpo_denuncia')
    testemunhas = request.POST.get('testemunhas')
    evidencias = request.POST.get('evidencias')
    sugestao_solucao = request.POST.get('sugestao_solucao')
    ciencia_veracidade = request.POST.get('ciencia_veracidade')
    ciencia_acao_judicial = request.POST.get('ciencia_acao_judicial')

    if ciencia_veracidade is '1' and ciencia_acao_judicial is '1':
        denuncia = Denuncia.objects.create(
            nome_completo=nome_completo,
            setor_colaborador=setor_colaborador,
            tipo_denuncia=tipo_denuncia,
            local_ocorrido=local_ocorrido,
            setor_ocorrido=setor_ocorrido,
            conhecimento=conhecimento,
            vinculo_superior=vinculo_superior,
            corpo_denuncia=corpo_denuncia,
            testemunhas=testemunhas,
            evidencias=evidencias,
            sugestao_solucao=sugestao_solucao,
            ciencia_veracidade=ciencia_veracidade,
            ciencia_acao_judicial=ciencia_acao_judicial,
        )

        send_mail(
            'Nova Denuncia registrada na Intranet',
            f'Nome Completo:\n {nome_completo} \n\n' \
            f'Indique o seu setor:\n {setor_colaborador} \n\n' \
            f'Que tipo de denúncia melhor se enquadra ao fato que você está registrando:\n {tipo_denuncia} \n\n' \
            f'Indique o local onde ocorreu o fato que você está denunciando:\n {local_ocorrido} \n\n' \
            f'Indique o setor onde ocorreu:\n {setor_ocorrido} \n\n' \
            f'Como tomou conhecimento deste fato/transgressão?\n {conhecimento} \n\n' \
            f'Você sabe se tem Diretor(es), Gestor(s), Coordenador(es), Supervisor(es) e/outros Colaborador(es) ENVOLVIDO(S):\n {vinculo_superior} \n\n' \
            f'O que você quer denunciar?\n {denuncia}  \n\n' \
            f'Existem testemunhas? Em caso positivo, indique-as.\n {testemunhas} \n\n' \
            f'Você sabe se existem evidências sobre o fato? Em caso positivo, indique-as.\n {evidencias} \n\n' \
            f'Caso você tenha alguma sugestão de como solucionar o problema, descreva-a:\n {sugestao_solucao} \n\n',
            'intranet.exatron@gmail.com',
            [
                'email@email.com',
                'email@email.com',
            ]
        )
        return render(request, 'denuncia/success.html')

    else:
        messages.add_message(request, messages.ERROR, 'Marque as opções do "Leia com Atenção" para continuar com sua denúncia')
        return render(request, 'denuncia/index.html')

