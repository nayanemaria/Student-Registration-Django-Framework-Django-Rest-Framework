import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render

from escola.forms import AlunoForm
from .models import Aluno, Escola
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

from .serializers import AlunoSerializer


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
    return render(request, "pages/home.html")

def form(request):
    try:
        print("request save")
        if request.user.is_authenticated:
            if request.method == 'POST':
                print('entrei no post')
                nome = request.POST['nome']
                email = request.POST['email']
                telefone = request.POST['telefone']
                endereco_completo = request.POST['endereco_completo']
                escola = request.POST['escola']
                dict = {
                    'nome': nome,
                    'email': email, 
                    'telefone': telefone, 
                    'endereco_completo': endereco_completo, 
                    'escola': Escola.objects.get(nome=escola)
                }
                Aluno(**dict).save()
                alunos = Aluno.objects.all().order_by('-id')
                print(alunos)
                context = {
                    'data': alunos,
                    'user': request.user
                }
                return render(request, "pages/home.html", context)

            if request.method == 'GET':
                alunos = Aluno.objects.all().order_by('-id') # Pega todos Alunos do banco
                # alunos_list = AlunoSerializer(alunos, many=True).data # serializa eles de forma listada
                # json_alunos_list = json.dumps(alunos_list) # faz a transformação dos dados para JSON
                
                escolas = Escola.objects.all()
                print(escolas)
                context = {
                    'escolas': escolas,
                    'data': alunos,
                    'user': request.user
                }

                return render(request, "pages/home.html", context)

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
        aluno = Aluno.objects.filter(id=id).first()
        escolas = Escola.objects.all()
        context = {
            'aluno': aluno,
            'escolas': escolas,
            'user': request.user
        }
        return render(request, "pages/editar_aluno.html", context)

def form_modelform(request):
    if request.method == 'GET':
        form = AlunoForm()
        context = {
            'form': form,
        }
        return render(request, "pages/home_form.html", context=context)
    else:
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            form = AlunoForm()
        context = {
            'form': form,
        }
        return render(request, "pages/home_form.html", context=context)


