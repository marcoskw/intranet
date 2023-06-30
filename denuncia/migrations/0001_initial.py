# Generated by Django 4.1.6 on 2023-04-06 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Criação')),
                ('nome_completo', models.CharField(blank=True, max_length=255, verbose_name='Nome Colaborador')),
                ('setor_colaborador', models.CharField(blank=True, max_length=255, verbose_name='Setor do Colaborador')),
                ('tipo_denuncia', models.CharField(blank=True, max_length=255, verbose_name='Tipo da Denuncia')),
                ('local_ocorrido', models.CharField(blank=True, max_length=255, verbose_name='Local Ocorrido')),
                ('setor_ocorrido', models.CharField(blank=True, max_length=255, verbose_name='Setor Ocorrido')),
                ('conhecimento', models.TextField(blank=True, max_length=255, verbose_name='Como tomou conhecimento')),
                ('vinculo_superior', models.CharField(blank=True, max_length=255, verbose_name='Envolvidos')),
                ('corpo_denuncia', models.TextField(blank=True, verbose_name='Denuncia')),
                ('testemunhas', models.CharField(blank=True, max_length=255, verbose_name='Testemunhas')),
                ('evidencias', models.CharField(blank=True, max_length=255, verbose_name='Evidencias')),
                ('sugestao_solucao', models.TextField(blank=True, verbose_name='Sugestão e Solução')),
                ('ciencia_veracidade', models.BooleanField(verbose_name='Veracidade')),
                ('ciencia_acao_judicial', models.BooleanField(verbose_name='Ciencia')),
                ('texto_ciencia', models.TextField(default='Declaro ter lido e compreendido que a prática de denúncia falsa constitui um crime passível de sanções legais, as quais podem ser significativas. Comprometo-me, a agir com responsabilidade e honestidade ao fazer uma denúncia.', verbose_name='Texto do Aceite 1')),
                ('texto_acao_judicial', models.TextField(default='Concordo que, em caso de ação judicial, as informações fornecidas na minha denúncia poderão ser compartilhadas com as autoridades competentes.', verbose_name='Texto do Aceite 2')),
            ],
        ),
    ]
