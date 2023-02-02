from django.db import models
from django.utils import timezone


class Setor(models.Model):
    setor = models.CharField(max_length=255)


class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=255)
    setor = models.CharField(max_length=255)
    ramal = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_admissao = models.DateTimeField(default=timezone.now, blank=True)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
