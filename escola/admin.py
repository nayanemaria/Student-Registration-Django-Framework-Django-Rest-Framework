from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    search_fields = ["nome", "email", "telefone", "endereco_completo"]
    list_display = ["nome", "email", "telefone", "endereco_completo"]
    
admin.site.register(Aluno, AlunoAdmin) #nome do modelo e nome da administracao

