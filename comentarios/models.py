from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from posts.models import Post


class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150, verbose_name='Nome')
    email_comentario = models.EmailField(verbose_name='E-mail')
    comentario = models.TextField(verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Usuário', blank=True, null=True)
    data_comentario = models.TimeField(default=timezone.now, verbose_name='Data')
    publicado_comentario = models.BooleanField(default=False, verbose_name='Status')

    def __str__(self):
        return self.nome_comentario
