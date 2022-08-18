# Generated by Django 4.0.6 on 2022-08-17 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_escola'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='escola',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escola.escola'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='endereco_completo',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='endereco_completo'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='telefone'),
        ),
    ]