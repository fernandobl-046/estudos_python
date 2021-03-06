from django.contrib import admin
from django.http import request
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/calcular', views.PagadorShipay.calcular_carrinho, name='calcular'),
    path('testes_api/', views.PesquisarAPI.as_view(), name='testes_api'),
    path('aula/', views.AulaPython.as_view(), name='aula'),
    path('accounts/login/', views.logar, name='logar'),
    path('produtos/', views.produtos, name='produtos'),
    path('empresa/', views.empresa, name='empresa'),
    path('contato/', views.contato, name='contato'),
    path('admin/', admin.site.urls, name='admin'),
]
