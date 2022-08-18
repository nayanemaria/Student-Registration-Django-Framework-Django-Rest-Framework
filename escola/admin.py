from django.contrib import admin
from .models import Aluno, Escola

class AlunoAdmin(admin.ModelAdmin):
    search_fields = ["nome", "email", "telefone", "endereco_completo", "escola"]
    list_display = ["nome", "email", "telefone", "endereco_completo", "escola"]

class EscolaAdmin(admin.ModelAdmin):
    search_fields = ["nome", "email", "telefone", "endereco", "cidade", "estado"]
    list_display = ["nome", "email", "telefone", "endereco", "cidade", "estado"]
    
admin.site.register(Aluno, AlunoAdmin) #nome do modelo e nome da administracao
admin.site.register(Escola, EscolaAdmin)

