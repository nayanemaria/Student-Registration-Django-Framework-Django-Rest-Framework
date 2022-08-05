from django.db import models

class Aluno(models.Model):
    nome = models.CharField("nome", max_length=255)
    telefone = models.CharField("telefone", max_length=20)
    email = models.CharField("email", max_length=255, null=True)
    endereco_completo = models.CharField("endereco_completo", max_length=300, null=True)

class Meta:
    verbose_name = "Aluno"
    verbose_name_plural = "Alunos"

def __str__(self):
    return self.nome




