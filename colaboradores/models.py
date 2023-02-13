from django.db import models
from django.utils import timezone


class Setor(models.Model):
    setor = models.CharField(max_length=255)

    def __str__(self):
        return self.setor


class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=255)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    ramal = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_admissao = models.DateTimeField(default=timezone.now, blank=True)
    aniversario = models.CharField(max_length=5, blank=True)
    descricao = models.TextField(blank=True)
    situacao = models.BooleanField(default=True, verbose_name="Ativo")

    def __str__(self):
        return self.nome_completo

