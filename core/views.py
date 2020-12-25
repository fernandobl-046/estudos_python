from django.shortcuts import render
from django.urls import path


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
    latest_question_list = "Django"
    context = {
        'teste': latest_question_list,
    }
    return render(request, 'contato.html', context)

    

    