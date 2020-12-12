from django.shortcuts import render
from django.urls import path


def home(request):
    latest_question_list = "Django"
    context = {
        'teste': latest_question_list,
    }
    return render(request, 'index.html', context)


    