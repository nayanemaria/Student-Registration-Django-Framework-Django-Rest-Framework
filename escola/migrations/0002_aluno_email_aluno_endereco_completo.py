# Generated by Django 4.0.6 on 2022-08-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='endereco_completo',
            field=models.CharField(max_length=300, null=True, verbose_name='endereco_completo'),
        ),
    ]
