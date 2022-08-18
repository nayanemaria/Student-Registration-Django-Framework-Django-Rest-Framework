from django.db import models

class Escola(models.Model):
    nome = models.CharField("nome", max_length=70, blank=True, null=True)
    email = models.EmailField("email", max_length=255, blank=False, unique=True,)
    telefone = models.CharField("telefone", max_length=20)
    endereco = models.CharField("endereco", max_length=300)
    cidade = models.CharField("cidade", max_length=100)
    estado = models.CharField("estado", max_length=100)

    class Meta:
        verbose_name = "Escola"
        verbose_name_plural = "Escolas" 

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField("nome", max_length=255, blank=True, null=True)
    telefone = models.CharField("telefone", max_length=20, blank=True, null=True)
    email = models.CharField("email", max_length=255, blank=True, null=True)
    endereco_completo = models.CharField("endereco_completo", max_length=300, blank=True, null=True)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos" 

    def __str__(self):
        return self.nome





