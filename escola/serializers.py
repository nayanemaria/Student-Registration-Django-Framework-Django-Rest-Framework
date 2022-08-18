from .models import Aluno, Escola
from rest_framework import serializers

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = "__all__"


class AlunoSerializer(serializers.ModelSerializer):
    escola = EscolaSerializer(source='escola', read_only=True)

    class Meta:
        model = Aluno
        fields = ("nome", "telefone", "email", "endereco_completo", "escola")

