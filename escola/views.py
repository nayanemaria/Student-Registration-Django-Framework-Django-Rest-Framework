from ast import If
import json
from multiprocessing import context
from unittest import loader
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import redirect, render

from escola.forms import AlunoForm
from .models import Aluno
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    print("ok")
    print(request.method)
    # teste = Aluno() 
    # teste.nome = "nayane"
    # teste.telefone = "85999468426"
    # teste.endereco_completo = "teste"
    # teste.email = "teste@email.com"
    # teste.save()
    todos_alunos = Aluno.objects.all().first()
    print("todos_alunos", todos_alunos)
    return render(request, "pages\home.html")

def form(request):
    try:
        print("request save")
        if request.user.is_authenticated:
            if request.method == 'POST':
                nome = request.POST['nome']
                email = request.POST['email']
                telefone = request.POST['telefone']
                endereco_completo = request.POST['endereco_completo']
                form = Aluno(nome=nome, email=email, telefone=telefone, endereco_completo=endereco_completo)
                form.save()
                data = Aluno.objects.all()
                context = {
                    'data': data,
                    'user': request.user
                }
                return render(request, "pages\home.html", context)

            if request.method == 'GET':
                data = Aluno.objects.all()
                context = {
                    'data': data,
                    'user': request.user
                }
                return render(request, "pages\home.html", context)

    except Exception as ERROR:
        retorno = json.dumps({"error":ERROR},cls=DjangoJSONEncoder,ensure_ascii=False)
        return HttpResponse(retorno, content_type='application/json', status=404, sort_keys=True)

def delete_aluno(request, id):
    print('delete', id)
    data = Aluno.objects.filter(id=id).first()
    data.delete()
    return HttpResponseRedirect(reverse('cadastrar_aluno'))

def update_aluno(request, id):
    if request.method == 'POST':
        aluno = Aluno.objects.filter(id=id).first()
        aluno.nome = request.POST['nome']
        aluno.email = request.POST['email']
        aluno.telefone = request.POST['telefone']
        aluno.endereco_completo = request.POST['endereco_completo']
        aluno.save()
        return HttpResponseRedirect(reverse('cadastrar_aluno'))
    if request.method == 'GET':
        print('entrei aqui')
        form = Aluno.objects.filter(id=id).first()
        context = {
            'form': form,
            'user': request.user
        }
        return render(request, "pages\editar_aluno.html", context)

def form_modelform(request):
    if request.method == 'GET':
        form = AlunoForm()
        context = {
            'form': form,
        }
        return render(request, "pages\home_form.html", context=context)
    else:
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            form = AlunoForm()
        context = {
            'form': form,
        }
        return render(request, "pages/home_form.html", context=context)


