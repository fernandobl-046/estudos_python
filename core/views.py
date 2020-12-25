from django.shortcuts import render
from django.urls import path
from django.http import JsonResponse
from core.models import Contato


def home(request):
    latest_question_list = "Django"
    context = {
        'teste': latest_question_list,
    }
    return render(request, 'index.html', context)


def produtos(request):
    latest_question_list = "Django"
    context = {
        'teste': latest_question_list,
    }
    return render(request, 'produtos.html', context)


def empresa(request):
    latest_question_list = "Django"
    context = {
        'teste': latest_question_list,
    }
    return render(request, 'empresa.html', context)


def contato(request):
    if request.method == 'GET':
        contatos = Contato.objects.all()        
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

    

    