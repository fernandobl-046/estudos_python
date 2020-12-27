from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from core.models import Contato


def home(request):
    return render(request, 'index.html')

def produtos(request):
    return render(request, 'produtos.html')

def empresa(request):
    return render(request, 'empresa.html')

@login_required
def contato(request):
    if request.method == 'GET':
        contatos = Contato.objects.filter(ativo=True).order_by('-data_criacao')
        context = {
            'contatos': contatos,
        }
        return render(request, 'contato.html', context)
    if request.method == 'POST':
        try:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            comment =  request.POST.get('comment')
            Contato.objects.create(nome=nome, email=email, conteudo=comment)
            return JsonResponse("Gravou", safe=False)
        except Exception as e:
            return JsonResponse("Erro" + e, safe=False)

def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')
    if request.method == 'POST':
        loginuser = request.POST['login']
        senhauser = request.POST['senha']
        usuario = authenticate(request, username=loginuser, password=senhauser)
        if usuario is not None:
            login(request, usuario)
            return redirect('/contato/')
        else:
            return render(request, 'logar.html', {'erro': 'Não foi possível logar'})